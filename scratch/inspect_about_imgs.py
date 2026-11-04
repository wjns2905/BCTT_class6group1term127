# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

img_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\update_docx_media'

# Save image11 as is
with Image.open(os.path.join(img_dir, 'image11.png')) as im:
    im.save(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im11.png')

# Let's crop header of image10
with Image.open(os.path.join(img_dir, 'image10.png')) as im:
    im.crop((0, 0, im.width, min(400, im.height))).save(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im10_top.png')

print("Saved im11 and im10_top!")
