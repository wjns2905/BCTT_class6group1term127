import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
e = c.rfind('];') + 1

articles = json.loads(c[s:e])

for a in articles:
    # If missing title_en, use title
    if not a.get('title_en'):
        a['title_en'] = a['title']
    
    # If missing subtitle_en, use subtitle
    if not a.get('subtitle_en'):
        a['subtitle_en'] = a['subtitle']

formatted = json.dumps(articles, ensure_ascii=False, indent=2)
new_c = c[:s] + formatted + c[e:]

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(new_c)

print("Populated title_en and subtitle_en across all articles!")
