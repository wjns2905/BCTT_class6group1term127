# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

im12 = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im12.png')
w, h = im12.size
# Let's inspect rows 0 to 300 in im12:
im12_top = im12.crop((0, 0, w, 280))
im12_top_small = im12_top.convert('L').resize((120, 20))

print("=== ASCII ART OF IM12 TOP (HEADER AD) ===")
for y in range(20):
    row_chars = []
    for x in range(120):
        val = im12_top_small.getpixel((x, y))
        if val < 80:
            row_chars.append('#')
        elif val < 160:
            row_chars.append(':')
        elif val < 220:
            row_chars.append('.')
        else:
            row_chars.append(' ')
    print("".join(row_chars))
