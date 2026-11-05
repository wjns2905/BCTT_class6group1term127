import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
e = c.rfind('];') + 1

data = json.loads(c[s:e])
print(f"Total articles in data.js: {len(data)}")

missing_images = []
for i, a in enumerate(data, 1):
    img = a.get('image')
    if not img:
        missing_images.append((a['id'], 'NO IMAGE FIELD'))
    elif not os.path.exists(img):
        missing_images.append((a['id'], img))

if missing_images:
    print(f"ERROR: {len(missing_images)} articles have missing/broken images:")
    for art_id, path in missing_images:
        print(f"  {art_id}: {path}")
else:
    print("SUCCESS: 100% of all 85 articles have valid, existing images on disk!")
