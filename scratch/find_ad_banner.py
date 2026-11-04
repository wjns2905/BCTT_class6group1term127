# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

im12 = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im12.png')
w, h = im12.size
print(f"im12 size: {w}x{h}")

# In news sites, banner ad is typically across the top (e.g. y=0 to y=200, or y=50 to y=250)
# Let's crop vertical slices of 150px and see where the IELTS ad banner is
for i in range(0, min(h, 600), 100):
    crop_h = min(150, h - i)
    im_c = im12.crop((0, i, w, i + crop_h))
    im_c.save(rf'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im12_slice_{i}.png')
    print(f"Saved slice {i}")
