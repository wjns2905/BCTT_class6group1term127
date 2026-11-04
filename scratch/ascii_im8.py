# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

im8 = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im8.png')
im_small = im8.convert('L').resize((120, 24))

print("=== ASCII ART OF IMAGE8.PNG (TITLE FONT) ===")
for y in range(24):
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
