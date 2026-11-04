
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
window.setLanguage('vi');
renderAboutUsSection();

const html = elements['aboutUsSection'] ? elements['aboutUsSection'].innerHTML : '';

console.log('VI render contains Tổng Biên Tập:', html.includes('Tổng Biên Tập'));
console.log('VI render contains Lê Hà Anh:', html.includes('Lê Hà Anh'));
console.log('VI render contains Chính Xác & Khách Quan:', html.includes('Chính Xác & Khách Quan'));
console.log('VI render contains Liêm Chính & Đạo Đức Nghề Báo:', html.includes('Liêm Chính & Đạo Đức Nghề Báo'));
console.log('VI render contains Trải Nghiệm Độc Giả Hiện Đại:', html.includes('Trải Nghiệm Độc Giả Hiện Đại'));
