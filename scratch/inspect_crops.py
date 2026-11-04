# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

img_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\update_docx_media'

# Let's inspect image1.png
with Image.open(os.path.join(img_dir, 'image1.png')) as im:
    print("image1 size:", im.size)

# Let's inspect image11.png (344x470) - small image!
with Image.open(os.path.join(img_dir, 'image11.png')) as im:
    print("image11 size:", im.size)
    # let's print some row profiles
    # or let's inspect where text is

# Let's inspect image12.png (2048x1085) - IELTS ad header
with Image.open(os.path.join(img_dir, 'image12.png')) as im:
    print("image12 size:", im.size)
    # header is likely top 200px
    im_header = im.crop((0, 0, im.width, min(300, im.height)))
    im_header.save(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im12_top_ad.png')
    print("Saved im12_top_ad.png")

# Let's crop image1.png
with Image.open(os.path.join(img_dir, 'image1.png')) as im:
    im.save(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im1_logo.png')
    print("Saved im1_logo.png")
