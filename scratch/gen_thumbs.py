# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

img_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\update_docx_media'
crop_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops'
os.makedirs(crop_dir, exist_ok=True)

# Let's inspect image1.png
# Save smaller thumbnails or info
for fname in sorted(os.listdir(img_dir)):
    p = os.path.join(img_dir, fname)
    with Image.open(p) as im:
        w, h = im.size
        # create thumbnail for quick inspection
        im_thumb = im.copy()
        im_thumb.thumbnail((400, 400))
        thumb_name = 'thumb_' + fname
        if im_thumb.mode == 'RGBA':
            im_thumb.save(os.path.join(crop_dir, thumb_name.replace('.jpg', '.png')), 'PNG')
        else:
            im_thumb.save(os.path.join(crop_dir, thumb_name), 'JPEG')
        print(f"Generated thumbnail for {fname} ({w}x{h})")
