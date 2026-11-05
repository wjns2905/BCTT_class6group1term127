import sys, re

sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for term in ['mosaic-grid-cluster', 'culture-list-col']:
    idx = text.find(term)
    if idx != -1:
        print(f"=== {term} ===")
        print(text[idx-50:idx+600])
