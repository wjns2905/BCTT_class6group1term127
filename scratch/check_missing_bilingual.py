import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
e = c.rfind('];') + 1

articles = json.loads(c[s:e])

missing_title_en = []
missing_sub_en = []

for a in articles:
    if not a.get('title_en'):
        missing_title_en.append(a['id'])
    if not a.get('subtitle_en'):
        missing_sub_en.append(a['id'])

print(f"Missing title_en: {len(missing_title_en)} -> {missing_title_en}")
print(f"Missing subtitle_en: {len(missing_sub_en)} -> {missing_sub_en}")
