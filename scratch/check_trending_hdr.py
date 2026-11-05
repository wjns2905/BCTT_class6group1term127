import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('trending.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('class="fashion-header"')
print(text[idx-50:idx+800])
