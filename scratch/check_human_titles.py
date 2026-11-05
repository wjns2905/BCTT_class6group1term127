import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
e = c.rfind('];') + 1

articles = json.loads(c[s:e])
human_arts = [a for a in articles if a['category'] == 'human-stories']

print(f"Human Stories ({len(human_arts)} articles):")
for i, a in enumerate(human_arts, 1):
    print(f"{i:2d}. [{a['id']}] {a['title']}")
