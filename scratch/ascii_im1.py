# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

im1 = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im1.png')
# resize to 120 x 30
im_small = im1.convert('L').resize((120, 28))

print("=== ASCII ART OF IMAGE1.PNG (LOGO) ===")
for y in range(28):
    row_chars = []
    for x in range(120):
        val = im_small.getpixel((x, y))
        if val < 100:
            row_chars.append('#')
        elif val < 180:
            row_chars.append(':')
        elif val < 230:
            row_chars.append('.')
        else:
            row_chars.append(' ')
    print("".join(row_chars))
