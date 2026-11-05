import json
import collections

with open('js/data.js', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
e = c.rfind('];') + 1
articles = json.loads(c[s:e])

img_counts = collections.Counter(a['image'] for a in articles)
print("Images used more than once:")
for img, cnt in img_counts.items():
    if cnt > 1:
        arts = [a['id'] for a in articles if a['image'] == img]
        print(f"  {img}: used {cnt} times in {arts}")
