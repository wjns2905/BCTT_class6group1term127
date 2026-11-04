# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

im1 = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im1.png')
print("im1 size:", im1.size)

# Let's inspect where non-white pixels are in im1
# Let's see if there's a heart or text
# Let's sample colors: what is the color of the text in im1?
colors = im1.convert('RGB').getcolors(maxcolors=100000)
dark_colors = [c for c in colors if c[1][0] < 150 and c[1][1] < 150]
sorted_dark = sorted(dark_colors, key=lambda x: x[0], reverse=True)[:5]
print("Dark colors in im1:", sorted_dark)
