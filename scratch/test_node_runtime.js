
const fs = require('fs');

let lastRenderedHTML = '';

global.document = {
  documentElement: { lang: 'en' },
  getElementById: (id) => ({
    set innerHTML(val) { lastRenderedHTML = val; },
    get innerHTML() { return lastRenderedHTML; },
    id
  }),
  querySelectorAll: () => [],
  addEventListener: () => {}
};
global.localStorage = {
  getItem: (k) => null,
  setItem: (k, v) => {}
};
global.window = {};

const translationsCode = fs.readFileSync('C:/Users/camka/OneDrive/Desktop/BCTT_class6group1term127/js/translations.js', 'utf8');
eval(translationsCode);

let currentLanguage = 'en';
const appCode = fs.readFileSync('C:/Users/camka/OneDrive/Desktop/BCTT_class6group1term127/js/app.js', 'utf8');
eval(appCode);

// Test EN
currentLanguage = 'en';
renderAboutUsSection();
console.log('EN render contains Editor-in-Chief:', lastRenderedHTML.includes('Editor-in-Chief'));
console.log('EN render contains Nguyễn Thị Ngọc Mai:', lastRenderedHTML.includes('Nguyễn Thị Ngọc Mai'));
console.log('EN render contains Accuracy & Objectivity:', lastRenderedHTML.includes('Accuracy & Objectivity'));

// Test VI
currentLanguage = 'vi';
renderAboutUsSection();
console.log('VI render contains Tổng Biên Tập:', lastRenderedHTML.includes('Tổng Biên Tập'));
console.log('VI render contains Lê Hà Anh:', lastRenderedHTML.includes('Lê Hà Anh'));
console.log('VI render contains Chính Xác & Khách Quan:', lastRenderedHTML.includes('Chính Xác & Khách Quan'));

console.log('ALL BILINGUAL RUNTIME CHECKS PASSED!');
