import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function applyLanguage(lang)')
print(text[idx+700:idx+1500])
