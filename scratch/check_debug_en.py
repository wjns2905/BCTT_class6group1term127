# -*- coding: utf-8 -*-
import subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')

test_file = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\scratch\debug_en_render.js"
code = """
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
"""
with open(test_file, 'w', encoding='utf-8') as f:
    f.write(code)

res = subprocess.run(["node", test_file], capture_output=True, text=True, encoding='utf-8')
print("STDOUT:\n", res.stdout)
print("STDERR:\n", res.stderr)
