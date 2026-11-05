import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
end = content.rfind('];') + 1
articles = json.loads(content[start:end])

used_images = set(a.get('image') for a in articles if a.get('image'))

all_images = []
for root, dirs, files in os.walk('assets/images'):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            rel = os.path.relpath(os.path.join(root, file), '.').replace('\\', '/')
            all_images.append(rel)

unused = [img for img in all_images if img not in used_images]
print(f"Total images: {len(all_images)}")
print(f"Used images: {len(used_images)}")
print(f"Unused images: {len(unused)}")

by_cat = {}
for img in unused:
    cat = img.split('/')[2] if len(img.split('/')) > 2 else 'root'
    by_cat.setdefault(cat, []).append(img)

for cat, imgs in sorted(by_cat.items()):
    print(f"\nUnused in '{cat}' ({len(imgs)} images):")
    for img in sorted(imgs)[:10]:
        print(f"  {img}")
    if len(imgs) > 10:
        print(f"  ... and {len(imgs) - 10} more")
