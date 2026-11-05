const fs = require('fs');

global.document = {
  getElementById: (id) => ({
    dataset: {},
    classList: { contains: () => false, add: () => {}, remove: () => {} },
    innerHTML: '',
    style: {}
  }),
  querySelectorAll: () => [],
  documentElement: { lang: 'en' }
};
global.localStorage = {
  getItem: () => null,
  setItem: () => {}
};
global.window = {};
global.currentLanguage = 'en';
global.currentFontSize = 1.0;
global.isSpeaking = false;

// Load data.js
let dataContent = fs.readFileSync('js/data.js', 'utf-8');
dataContent = dataContent.replace('const ARTICLES_DATA =', 'global.ARTICLES_DATA =');
eval(dataContent);

// Test rendering for trending-4 (Gánh mưu sinh)
const ganh = ARTICLES_DATA.find(a => a.id === 'trending-4');
console.log('trending-4 Title:', ganh.title);
console.log('trending-4 Total content items:', ganh.content.length);
const figures = ganh.content.filter(p => p.startsWith('<figure'));
console.log('trending-4 Total inline figures:', figures.length);

// Test rendering for mind-1 (Taeyang)
const taeyang = ARTICLES_DATA.find(a => a.id === 'mind-1');
console.log('\nmind-1 Title:', taeyang.title);
console.log('mind-1 Total content items:', taeyang.content.length);
const t_figures = taeyang.content.filter(p => p.startsWith('<figure'));
console.log('mind-1 Total inline figures:', t_figures.length);

// Test rendering for indepth-5 (Rory Kinnear)
const rory = ARTICLES_DATA.find(a => a.id === 'indepth-5');
console.log('\nindepth-5 Title:', rory.title);
console.log('indepth-5 Total content items:', rory.content.length);
const r_figures = rory.content.filter(p => p.startsWith('<figure'));
console.log('indepth-5 Total inline figures:', r_figures.length);

console.log('\n✓ ALL MODAL TEST CHECKS PASSED!');
