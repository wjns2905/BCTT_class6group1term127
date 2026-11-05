import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
e = c.rfind('];') + 1
articles = json.loads(c[s:e])

print(f"Total articles: {len(articles)}")

by_cat = {}
for a in articles:
    by_cat.setdefault(a['category'], []).append(a)

for cat, arts in by_cat.items():
    print(f"\n=================== {cat.upper()} ({len(arts)} articles) ===================")
    for i, a in enumerate(arts, 1):
        print(f"  {i:2d}. [{a['id']}] {a['title']}")
