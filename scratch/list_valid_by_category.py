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

trending_imgs = get_valid_images('assets/images/trending')
society_imgs = get_valid_images('assets/images/society')
human_imgs = get_valid_images('assets/images/human_stories')
mind_imgs = get_valid_images('assets/images/mind_&_soul')
indepth_imgs = get_valid_images('assets/images/in-dept')
editorial_imgs = get_valid_images('assets/images/editorial')
notes_imgs = get_valid_images('assets/images/note_giao_diện')

print(f"Trending valid images: {len(trending_imgs)}")
print(f"Society valid images: {len(society_imgs)}")
print(f"Human Stories valid images: {len(human_imgs)}")
print(f"Mind & Soul valid images: {len(mind_imgs)}")
print(f"In-depth valid images: {len(indepth_imgs)}")
print(f"Editorial valid images: {len(editorial_imgs)}")
print(f"Notes valid images: {len(notes_imgs)}")
