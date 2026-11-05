import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
e = c.rfind('];') + 1
articles = json.loads(c[s:e])

categories = ['trending', 'society', 'human-stories', 'mind-soul', 'in-depth']

for cat in categories:
    filtered = [a for a in articles if a['category'] == cat]
    print(f"\n================ CATEGORY: {cat.upper()} ({len(filtered)} articles) ================")
    for i, a in enumerate(filtered, 1):
        has_title_en = 'title_en' in a and bool(a['title_en'])
        print(f"  {i:2d}. [{a['id']:12s}] {a['title'][:55]}... | En: {has_title_en} | Img: {a['image']}")
