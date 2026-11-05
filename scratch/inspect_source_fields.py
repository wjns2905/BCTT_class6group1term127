import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
e = c.rfind('];') + 1

articles = json.loads(c[s:e])

print("Sample article metadata (10 articles):")
for a in articles[:10]:
    print(f"ID: {a['id']}")
    print(f"  Author: '{a.get('author')}'")
    print(f"  Date:   '{a.get('date')}'")
    print(f"  Source: '{a.get('sourceName')}'")
    print(f"  URL:    '{a.get('sourceUrl')}'")
    print()
