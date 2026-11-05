import json
import collections
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
e = c.rfind('];') + 1
articles = json.loads(c[s:e])

print(f"Total articles currently: {len(articles)}")

# 1. Check duplicate images
img_map = collections.defaultdict(list)
for a in articles:
    img_map[a.get('image', '')].append(a['id'])

print("\n--- DUPLICATE IMAGES DETECTED ---")
dup_img_count = 0
for img, ids in img_map.items():
    if len(ids) > 1:
        dup_img_count += 1
        print(f"  Image: '{img}' used in {ids}")

if dup_img_count == 0:
    print("  None! All images are unique.")

# 2. Check duplicate titles or subtitles
print("\n--- TITLE OVERLAPS ---")
title_words = collections.defaultdict(list)
for a in articles:
    # First 6 words of title
    prefix = ' '.join(a['title'].strip().lower().split()[:5])
    title_words[prefix].append(a['id'])

for prefix, ids in title_words.items():
    if len(ids) > 1:
        print(f"  Prefix '{prefix}': {ids}")

# 3. Check video articles vs regular articles
print("\n--- ALL ARTICLE IDS AND TITLES ---")
for i, a in enumerate(articles, 1):
    print(f"{i:2d}. [{a['category']:14s}] {a['id']:12s} | {a['image']:42s} | {a['title'][:50]}")
