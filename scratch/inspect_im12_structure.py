# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

im12 = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im12.png')
w, h = im12.size

# Let's save 10 slices across im12
step = h // 10
for i in range(10):
    y1 = i * step
    y2 = min(h, (i + 1) * step)
    sl = im12.crop((0, y1, w, y2))
    sl.thumbnail((600, 100))
    sl.save(rf'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im12_thumb_{i}.png')

print("Saved 10 slices of im12")
