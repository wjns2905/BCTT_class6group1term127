
const fs = require('fs');

const elements = {};
function getOrCreate(id) {
  if (!elements[id]) {
    elements[id] = {
      innerHTML: '',
      id,
      classList: { contains: () => false, add: () => {}, remove: () => {} },
      getAttribute: () => null,
      setAttribute: () => {}
    };
  }
  return elements[id];
}

global.document = {
  documentElement: { lang: 'en' },
  body: { dataset: {} },
  getElementById: getOrCreate,
  querySelectorAll: () => [],
  addEventListener: () => {}
};
global.localStorage = { getItem: () => null, setItem: () => {} };
global.window = {};

const translationsCode = fs.readFileSync('C:/Users/camka/OneDrive/Desktop/BCTT_class6group1term127/js/translations.js', 'utf8');
eval(translationsCode);

const appCode = fs.readFileSync('C:/Users/camka/OneDrive/Desktop/BCTT_class6group1term127/js/app.js', 'utf8');
eval(appCode);

// Call through window.setLanguage
window.setLanguage('en');
renderAboutUsSection();

const html = elements['aboutUsSection'] ? elements['aboutUsSection'].innerHTML : '';

console.log('EN render contains Editor-in-Chief:', html.includes('Editor-in-Chief'));
console.log('EN render contains Nguyễn Thị Ngọc Mai:', html.includes('Nguyễn Thị Ngọc Mai'));
console.log('EN render contains Accuracy & Objectivity:', html.includes('Accuracy & Objectivity'));
console.log('EN render contains Ethical Integrity:', html.includes('Ethical Integrity'));
console.log('EN render contains Modern Reader Experience:', html.includes('Modern Reader Experience'));
