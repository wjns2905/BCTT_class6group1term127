import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
e = c.rfind('];') + 1

articles = json.loads(c[s:e])

queries = ['Hà Nội', 'Kindness', 'Porsche', 'Michelin', 'Gánh mưu sinh', 'ADN', 'AI', 'UNESCO', 'Bến Tre', 'Voọc']
for q in queries:
    matched = [a for a in articles if q.lower() in a['title'].lower() or q.lower() in a['subtitle'].lower() or any(q.lower() in t.lower() for t in a.get('tags', []))]
    print(f"Search '{q}': {len(matched)} matches found")
