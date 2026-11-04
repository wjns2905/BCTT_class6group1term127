# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

im8 = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im8.png')
# let's crop bounding box of text
im8_gray = im8.convert('L')
bbox = im8_gray.point(lambda p: 255 if p < 240 else 0).getbbox()
print("im8 text bbox:", bbox)
if bbox:
    im8_crop = im8.crop(bbox)
    im8_crop.save(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im8_cropped_text.png')
    print("Saved im8_cropped_text.png, size:", im8_crop.size)
