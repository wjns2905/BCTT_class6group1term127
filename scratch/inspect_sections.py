# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

img_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops'

for name in ['im5.png', 'im6.png', 'im7.png', 'im8.png', 'im9.png', 'im10.png']:
    p = os.path.join(img_dir, name)
    with Image.open(p) as im:
        print(f"\n=== {name} ({im.size}) ===")
        # let's save a clear preview
        preview = im.copy()
        preview.thumbnail((800, 800))
        preview.save(os.path.join(img_dir, 'prev_' + name))
