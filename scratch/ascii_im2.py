# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

im2 = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im2.jpg')
w, h = im2.size
# Let's inspect im2: what site is it?
# Let's resize to 120 x 40
im_small = im2.convert('L').resize((120, 35))

print("=== ASCII ART OF IMAGE2.JPG ===")
for y in range(35):
    row_chars = []
    for x in range(120):
        val = im_small.getpixel((x, y))
        if val < 80:
            row_chars.append('#')
        elif val < 160:
            row_chars.append(':')
        elif val < 220:
            row_chars.append('.')
        else:
            row_chars.append(' ')
    print("".join(row_chars))
