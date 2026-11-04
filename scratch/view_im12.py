# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

im12 = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im12.png')
w, h = im12.size
# Let's find the IELTS ad inside im12:
# What colors are prominent in im12?
# Let's save a thumbnail of im12 so we can view the whole layout
im12_small = im12.resize((1024, int(1024 * h / w)))
im12_small.save(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im12_overview.png')
print(f"im12 overview saved: {im12_small.size}")
