import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_start = text.find('<aside class="hero-left-stream"')
idx_end = text.find('</aside>', idx_start) + len('</aside>')
print(text[idx_start:idx_end])
