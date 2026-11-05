import os
from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Collect all valid image paths
valid_images = []
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            rel = os.path.relpath(os.path.join(root, f), '.').replace('\\', '/')
            try:
                with Image.open(rel) as im:
                    w, h = im.size
                    if w >= 250 and h >= 180 and 'logo' not in rel.lower() and 'ads' not in rel.lower() and 'profiles' not in rel.lower():
                        valid_images.append(rel)
            except:
                pass

print(f"Total available valid images: {len(valid_images)}")

# Group by category folder
by_cat = {
    'trending': [],
    'society': [],
    'human_stories': [],
    'mind_&_soul': [],
    'in-dept': [],
    'editorial': [],
    'note_giao_diện': []
}

for img in valid_images:
    folder = img.split('/')[2]
    if folder in by_cat:
        by_cat[folder].append(img)

for folder, imgs in by_cat.items():
    print(f"  {folder}: {len(imgs)} images")
