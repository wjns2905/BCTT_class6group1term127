import os
from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_valid_images(folder):
    res = []
    for f in sorted(os.listdir(folder)):
        p = f"{folder}/{f}".replace('\\', '/')
        if p.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            try:
                with Image.open(p) as im:
                    w, h = im.size
                    if w >= 250 and h >= 180 and 'logo' not in p.lower() and 'ads' not in p.lower():
                        res.append(p)
            except:
                pass
    return res

trending_pool = get_valid_images('assets/images/trending')
society_pool = get_valid_images('assets/images/society')
human_pool = get_valid_images('assets/images/human_stories')
mind_pool = get_valid_images('assets/images/mind_&_soul')
indepth_pool = get_valid_images('assets/images/in-dept')
editorial_pool = get_valid_images('assets/images/editorial')
notes_pool = get_valid_images('assets/images/note_giao_diện')

print(f"Pool sizes: Trending={len(trending_pool)}, Society={len(society_pool)}, Human={len(human_pool)}, Mind={len(mind_pool)}, Indepth={len(indepth_pool)}, Editorial={len(editorial_pool)}, Notes={len(notes_pool)}")

# Allocate 20 unique images to Trending
trending_assigned = trending_pool[:20]
assert len(trending_assigned) == 20

# Allocate 20 unique images to Society
society_assigned = society_pool[:20]
assert len(society_assigned) == 20

# Allocate 20 unique images to Human Stories
human_assigned = human_pool[:20]
assert len(human_assigned) == 20

# Allocate 20 unique images to Mind & Soul (19 from mind + 1 from notes)
mind_assigned = mind_pool[:19] + [notes_pool[0]]
assert len(mind_assigned) == 20

# Allocate 20 unique images to In-Depth (17 from in-dept + 3 from editorial)
indepth_assigned = indepth_pool[:17] + editorial_pool[:3]
assert len(indepth_assigned) == 20

# Check total unique across all 100
all_100 = trending_assigned + society_assigned + human_assigned + mind_assigned + indepth_assigned
print(f"Total assigned images: {len(all_100)}")
print(f"Unique assigned images: {len(set(all_100))}")
assert len(all_100) == len(set(all_100)), "Duplicates detected in assigned pool!"

print("PERFECT: All 100 images are 100% DISTINCT, VALID, and EXIST ON DISK!")
