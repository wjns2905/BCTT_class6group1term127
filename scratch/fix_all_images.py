# -*- coding: utf-8 -*-
"""
Fix image paths and URL routing across GitHub Pages and standalone route:
1. Update handleImageError in all HTML files and app.js with multi-tier fallback
2. Add <base href="../../"> in hearticles/madeuparticle/index.html
3. Update openArticleModal in app.js to fix asset paths dynamically
4. Update pushState in app.js to preserve GitHub Pages repository base
"""

import os
import re

BASE_DIR = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127"
APP_PATH = os.path.join(BASE_DIR, "js", "app.js")
DATA_PATH = os.path.join(BASE_DIR, "js", "data.js")
MADEUP_INDEX = os.path.join(BASE_DIR, "hearticles", "madeuparticle", "index.html")

# =====================================================================
# 1. UPDATE JS/APP.JS
# =====================================================================
print("1. Updating js/app.js...")
with open(APP_PATH, "r", encoding="utf-8") as f:
    app_code = f.read()

# 1.1 Robust handleImageError
new_image_error = """function handleImageError(img) {
  if (!img) return;
  const currentSrc = img.getAttribute('src') || '';
  if (!currentSrc) return;

  // Level 1: If in subfolder, try ../../ prefix
  if (currentSrc.startsWith('assets/') && !img.dataset.triedSubfolder) {
    img.dataset.triedSubfolder = 'true';
    img.src = '../../' + currentSrc;
    return;
  }

  // Level 2: If on GitHub Pages, try full repository path
  if (window.location.hostname.includes('github.io') && !img.dataset.triedGithub) {
    img.dataset.triedGithub = 'true';
    const cleanPath = currentSrc.replace(/^(\\.\\.\\/)+/, '').replace(/^\\//, '');
    img.src = '/BCTT_class6group1term127/' + cleanPath;
    return;
  }

  // Level 3: Fallback image
  img.onerror = null;
  img.src = img.src.includes('ngoc_mai') ? 'assets/images/trending/image8.jpg' : 'assets/images/trending/image8.jpg';
}
window.handleImageError = handleImageError;
"""

if "function handleImageError" in app_code:
    app_code = re.sub(
        r"function handleImageError\([^)]*\)\s*\{[\s\S]*?\}\s*window\.handleImageError\s*=\s*handleImageError;",
        new_image_error,
        app_code
    )
else:
    app_code += "\n" + new_image_error

# 1.2 In openArticleModal: dynamically prefix relative assets if in subfolder OR if URL changed
old_open_modal_start = """  const isEn = (currentLanguage === 'en');
  const title = (isEn && article.title_en) ? article.title_en : article.title;
  const subtitle = (isEn && article.subtitle_en) ? article.subtitle_en : article.subtitle;
  const readTime = isEn ? (article.readTime || '').replace('phút đọc', 'min read') : article.readTime;
  const breadcrumbHome = isEn ? 'Home' : 'Trang chủ';
  const breadcrumbDetail = isEn ? 'Article Detail' : 'Chi tiết bài viết';

  const savedComments = JSON.parse(localStorage.getItem(`comments_${article.id}`) || '[]');
  const isLiked = localStorage.getItem(`liked_${article.id}`) === 'true';

  let bodyHtml = '';
  const contentSource = (isEn && article.content_en) ? article.content_en : article.content;
  if (typeof contentSource === 'string') {
    bodyHtml = contentSource;
  } else if (Array.isArray(contentSource)) {
    bodyHtml = contentSource.map(p => {
      if (typeof p !== 'string') return '';
      const trimmed = p.trim();
      if (trimmed.startsWith('### ')) {
        return `<h3 class="article-section-heading" style="font-family:var(--font-editorial); font-size:1.35rem; font-weight:800; color:var(--color-brand-primary); margin:1.75rem 0 0.75rem 0;">${trimmed.replace('### ', '')}</h3>`;
      }
      if (trimmed.startsWith('## ')) {
        return `<h2 class="article-section-heading-lg" style="font-family:var(--font-editorial); font-size:1.55rem; font-weight:800; color:var(--color-brand-primary); margin:2rem 0 0.85rem 0;">${trimmed.replace('## ', '')}</h2>`;
      }
      if (trimmed.startsWith('<figure') || trimmed.startsWith('<table') || trimmed.startsWith('<div') || trimmed.startsWith('<blockquote')) {
        return trimmed;
      }
      return `<p style="margin-bottom:1.15rem; line-height:1.8; text-align:justify;">${p}</p>`;
    }).join('');
  }"""

new_open_modal_start = """  const isEn = (currentLanguage === 'en');
  const title = (isEn && article.title_en) ? article.title_en : article.title;
  const subtitle = (isEn && article.subtitle_en) ? article.subtitle_en : article.subtitle;
  const readTime = isEn ? (article.readTime || '').replace('phút đọc', 'min read') : article.readTime;
  const breadcrumbHome = isEn ? 'Home' : 'Trang chủ';
  const breadcrumbDetail = isEn ? 'Article Detail' : 'Chi tiết bài viết';

  const savedComments = JSON.parse(localStorage.getItem(`comments_${article.id}`) || '[]');
  const isLiked = localStorage.getItem(`liked_${article.id}`) === 'true';

  // Determine correct asset prefix (handles subfolder or root view)
  const isSubfolder = window.location.pathname.includes('/hearticles/');
  const assetPrefix = isSubfolder ? '../../' : '';

  let bodyHtml = '';
  const contentSource = (isEn && article.content_en) ? article.content_en : article.content;
  if (typeof contentSource === 'string') {
    bodyHtml = contentSource;
  } else if (Array.isArray(contentSource)) {
    bodyHtml = contentSource.map(p => {
      if (typeof p !== 'string') return '';
      let trimmed = p.trim();
      if (trimmed.startsWith('### ')) {
        return `<h3 class="article-section-heading" style="font-family:var(--font-editorial); font-size:1.35rem; font-weight:800; color:var(--color-brand-primary); margin:1.75rem 0 0.75rem 0;">${trimmed.replace('### ', '')}</h3>`;
      }
      if (trimmed.startsWith('## ')) {
        return `<h2 class="article-section-heading-lg" style="font-family:var(--font-editorial); font-size:1.55rem; font-weight:800; color:var(--color-brand-primary); margin:2rem 0 0.85rem 0;">${trimmed.replace('## ', '')}</h2>`;
      }
      if (trimmed.startsWith('<figure') || trimmed.startsWith('<table') || trimmed.startsWith('<div') || trimmed.startsWith('<blockquote')) {
        // Automatically inject onerror handler to all img tags inside figure
        if (trimmed.includes('<img') && !trimmed.includes('onerror=')) {
          trimmed = trimmed.replace(/<img\\b/g, '<img onerror="handleImageError(this)"');
        }
        if (assetPrefix) {
          trimmed = trimmed.replace(/src=["']assets\\//g, `src="${assetPrefix}assets/`);
        }
        return trimmed;
      }
      return `<p style="margin-bottom:1.15rem; line-height:1.8; text-align:justify;">${p}</p>`;
    }).join('');
  }"""

if old_open_modal_start in app_code:
    app_code = app_code.replace(old_open_modal_start, new_open_modal_start)
    print("SUCCESS: Updated openArticleModal with smart assetPrefix and onerror injection.")

# 1.3 Fix pushState so it doesn't break base repository URL on GitHub Pages
old_pushstate = """  // URL Routing: update URL to /hearticles/madeuparticle for trending-1
  try {
    const articleUrl = (article.url || article.sourceUrl);
    if (articleUrl && articleUrl.startsWith('/')) {
      if (window.location.protocol === 'file:') {
        window.location.hash = articleUrl.replace(/^\\//, '');
      } else {
        history.pushState({ articleId: article.id }, '', articleUrl);
      }
    }
  } catch (e) {}"""

new_pushstate = """  // URL Routing: update URL to /hearticles/madeuparticle for trending-1 safely
  try {
    const articleUrl = (article.url || article.sourceUrl);
    if (articleUrl && articleUrl.includes('madeuparticle')) {
      // Use clean hash routing on web hosts to NEVER disrupt base image asset resolution
      const isGH = window.location.hostname.includes('github.io');
      if (window.location.protocol === 'file:' || isGH) {
        window.location.hash = 'hearticles/madeuparticle';
      } else {
        history.pushState({ articleId: article.id }, '', '/hearticles/madeuparticle');
      }
    }
  } catch (e) {}"""

if old_pushstate in app_code:
    app_code = app_code.replace(old_pushstate, new_pushstate)
    print("SUCCESS: Fixed pushState in app.js to use safe hash routing on GitHub Pages.")

with open(APP_PATH, "w", encoding="utf-8") as f:
    f.write(app_code)
print("Finished updating js/app.js.")


# =====================================================================
# 2. UPDATE HEARTICLES/MADEUPARTICLE/INDEX.HTML
# =====================================================================
print("2. Updating hearticles/madeuparticle/index.html with <base href> and robust image fallbacks...")
with open(MADEUP_INDEX, "r", encoding="utf-8") as f:
    html = f.read()

# Add <base href="../../"> right after <head>
if "<base href=" not in html:
    html = html.replace("<head>", '<head>\n  <base href="../../">')
    print("SUCCESS: Added <base href=\"../../\"> to hearticles/madeuparticle/index.html.")

# Update handleImageError inside head script
old_head_script = """  <script>
    function handleImageError(img) {
      img.onerror = null;
      img.src = '../../assets/images/trending/ngoc_mai/hat_and_jacket.jpg';
    }
  </script>"""

new_head_script = """  <script>
    function handleImageError(img) {
      if (!img) return;
      const currentSrc = img.getAttribute('src') || '';
      if (!img.dataset.triedFallback) {
        img.dataset.triedFallback = 'true';
        if (currentSrc.startsWith('assets/')) {
          img.src = '../../' + currentSrc;
          return;
        }
      }
      img.onerror = null;
      img.src = '../../assets/images/trending/ngoc_mai/hat_and_jacket.jpg';
    }
  </script>"""

if old_head_script in html:
    html = html.replace(old_head_script, new_head_script)
    print("SUCCESS: Updated handleImageError in hearticles/madeuparticle/index.html.")

with open(MADEUP_INDEX, "w", encoding="utf-8") as f:
    f.write(html)
print("Finished updating hearticles/madeuparticle/index.html.")

# =====================================================================
# 3. UPDATE ALL HTML FILES' HEAD SCRIPT (handleImageError)
# =====================================================================
for fname in ['index.html', 'trending.html', 'society.html', 'human-stories.html', 'mind-soul.html', 'in-depth.html', 'about.html']:
    fpath = os.path.join(BASE_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        page_html = f.read()

    # Ensure handleImageError in head script is robust
    target_snippet = """  <script>
    function handleImageError(img) {
      img.onerror = null;
      img.src = 'assets/images/trending/image8.jpg';
    }
  </script>"""

    replacement_snippet = """  <script>
    function handleImageError(img) {
      if (!img) return;
      const cur = img.getAttribute('src') || '';
      if (cur.startsWith('assets/') && !img.dataset.triedRel) {
        img.dataset.triedRel = 'true';
        if (window.location.hostname.includes('github.io')) {
          img.src = '/BCTT_class6group1term127/' + cur;
          return;
        }
      }
      img.onerror = null;
      img.src = 'assets/images/trending/image8.jpg';
    }
  </script>"""

    if target_snippet in page_html:
        page_html = page_html.replace(target_snippet, replacement_snippet)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(page_html)
        print(f"SUCCESS: Updated handleImageError in {fname}.")

print("\nALL IMAGE FIXES APPLIED SUCCESSFULLY!")
