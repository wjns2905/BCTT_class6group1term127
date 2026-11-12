const fs = require('fs');
const path = require('path');

const baseDir = path.resolve(__dirname, '..');

// Load data and translations
const dataCode = fs.readFileSync(path.join(baseDir, 'js', 'data.js'), 'utf8');
const transCode = fs.readFileSync(path.join(baseDir, 'js', 'translations.js'), 'utf8');
const appCode = fs.readFileSync(path.join(baseDir, 'js', 'app.js'), 'utf8');

// Mock DOM environment
function createMockEnv(pathname, lang) {
  let innerHtmlResult = '';
  const dom = {
    location: {
      pathname: pathname,
      search: '',
      hostname: 'wjns2905.github.io'
    },
    document: {
      title: '',
      documentElement: { lang: lang },
      getElementById: (id) => {
        if (id === 'standaloneArticleHost') {
          return {
            set innerHTML(val) { innerHtmlResult = val; },
            get innerHTML() { return innerHtmlResult; }
          };
        }
        return { style: {}, classList: { add(){}, remove(){}, toggle(){} }, innerHTML: '', textContent: '', appendChild(){} };
      },
      querySelectorAll: () => [],
      addEventListener: () => {}
    },
    localStorage: {
      getItem: (k) => k === 'hearticles_lang' ? lang : null,
      setItem: () => {}
    },
    window: {}
  };
  dom.window = dom;
  dom.addEventListener = () => {};
  return { dom, getHtml: () => innerHtmlResult };
}

function runTest(pathname, lang) {
  console.log(`\n========================================`);
  console.log(`TESTING: ${pathname} [Lang: ${lang}]`);
  console.log(`========================================`);

  const { dom, getHtml } = createMockEnv(pathname, lang);

  // Execute in isolated function scope
  const fn = new Function('window', 'document', 'location', 'localStorage', `
    ${dataCode}
    ${transCode}
    ${appCode}
    currentLanguage = '${lang}';
    renderDedicatedArticlePage('trending-1');
  `);

  fn(dom.window, dom.document, dom.location, dom.localStorage);

  const html = getHtml();
  console.log('Generated HTML length:', html.length);

  // Find all video tags
  const vidMatches = [...html.matchAll(/<video\b([^>]*?)>/gi)];
  console.log(`Found ${vidMatches.length} <video> tags.`);
  vidMatches.forEach(v => {
    const pm = v[0].match(/poster=["']([^"']+)["']/);
    console.log(`  Video poster: ${pm ? pm[1] : 'none'}`);
  });
  const srcMatches = [...html.matchAll(/<source\b([^>]*?)>/gi)];
  srcMatches.forEach(s => {
    const sm = s[0].match(/src=["']([^"']+)["']/);
    console.log(`  Source src: ${sm ? sm[1] : 'none'}`);
  });

  // Find all img tags
  const imgMatches = [...html.matchAll(/<img\b([^>]*?)>/gi)];
  console.log(`Found ${imgMatches.length} <img> tags.`);

  let allValid = true;
  imgMatches.forEach((m, idx) => {
    const tag = m[0];
    const srcMatch = tag.match(/src=["']([^"']+)["']/i);
    const src = srcMatch ? srcMatch[1] : '';
    const hasOnError = tag.includes('onerror="handleImageError(this)"');

    console.log(`\nImg #${idx + 1}:`);
    console.log(`  src: ${src}`);
    console.log(`  has onerror: ${hasOnError}`);

    if (!hasOnError) {
      console.error('  ERROR: Missing onerror handler!');
      allValid = false;
    }

    // Resolve path relative to document location
    let resolvedOnDisk = '';
    if (src.startsWith('../../')) {
      resolvedOnDisk = path.resolve(baseDir, 'hearticles', 'madeuparticle', src);
    } else {
      resolvedOnDisk = path.resolve(baseDir, src);
    }

    const fileExists = fs.existsSync(resolvedOnDisk);
    console.log(`  resolves on disk to: ${resolvedOnDisk}`);
    console.log(`  file exists on disk: ${fileExists}`);

    if (!fileExists) {
      console.error('  ERROR: File does NOT exist on disk!');
      allValid = false;
    }
  });

  if (allValid) {
    console.log(`\n>> PASS: All ${imgMatches.length} images are 100% valid with existing files and onerror handlers!`);
  } else {
    console.error(`\n>> FAIL: One or more images failed validation!`);
    process.exit(1);
  }
}

// Test 1: /BCTT_class6group1term127/hearticles/madeuparticle/index.html in Vietnamese
runTest('/BCTT_class6group1term127/hearticles/madeuparticle/index.html', 'vi');

// Test 2: /BCTT_class6group1term127/hearticles/madeuparticle/index.html in English
runTest('/BCTT_class6group1term127/hearticles/madeuparticle/index.html', 'en');

// Test 3: /BCTT_class6group1term127/article.html in Vietnamese
runTest('/BCTT_class6group1term127/article.html', 'vi');

// Test 4: /BCTT_class6group1term127/article.html in English
runTest('/BCTT_class6group1term127/article.html', 'en');
