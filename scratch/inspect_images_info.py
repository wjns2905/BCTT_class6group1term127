# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

img_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\update_docx_media'
for f in sorted(os.listdir(img_dir)):
    p = os.path.join(img_dir, f)
    with Image.open(p) as im:
        print(f"{f}: size={im.size}, mode={im.mode}")
