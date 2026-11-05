import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.fashion-header')
print(text[idx:idx+1500])
