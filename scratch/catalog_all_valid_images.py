import os
from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

all_valid = []
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            rel = os.path.relpath(os.path.join(root, f), '.').replace('\\', '/')
            try:
                with Image.open(rel) as im:
                    w, h = im.size
                    # Filter out tiny spacers, logos, or icon bars
                    if w >= 250 and h >= 180 and 'logo' not in rel.lower() and 'ads' not in rel.lower() and 'profiles' not in rel.lower():
                        all_valid.append((rel, w, h))
            except:
                pass

print(f"Total valid article images (>= 250x180): {len(all_valid)}")

by_folder = {}
for p, w, h in all_valid:
    folder = p.split('/')[2]
    by_folder.setdefault(folder, []).append((p, w, h))

for folder, imgs in sorted(by_folder.items()):
    print(f"\nFolder '{folder}': {len(imgs)} valid images")
    for p, w, h in sorted(imgs):
        print(f"  {p} ({w}x{h})")
