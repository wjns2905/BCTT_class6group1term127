import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
end = content.rfind('];') + 1
articles = json.loads(content[start:end])

# Check duplicate titles
titles = {}
for a in articles:
    t = a['title'].strip().lower()
    if t in titles:
        print(f"DUPLICATE DETECTED: '{a['title']}' in {a['id']} and {titles[t]}")
    titles[t] = a['id']

print("Checked for duplicates. Any found printed above.")

# Check all images in assets/images
all_images = []
for root, dirs, files in os.walk('assets/images'):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            rel = os.path.relpath(os.path.join(root, file), '.').replace('\\', '/')
            all_images.append(rel)

print(f"Total image files on disk in assets/images: {len(all_images)}")
by_dir = {}
for img in all_images:
    d = os.path.dirname(img)
    by_dir[d] = by_dir.get(d, 0) + 1
for d, c in sorted(by_dir.items()):
    print(f"  {d}: {c} files")
