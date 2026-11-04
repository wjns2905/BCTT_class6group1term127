# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

im2 = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im2.jpg')
print("im2 size:", im2.size)

# Let's see what is inside im2: is it 3 columns?
# Left col: 0 to ~30%, Center: ~30% to ~70%, Right: ~70% to 100%
w, h = im2.size
col1 = im2.crop((0, 0, int(w*0.32), h))
col2 = im2.crop((int(w*0.32), 0, int(w*0.68), h))
col3 = im2.crop((int(w*0.68), 0, w, h))

col1.thumbnail((400, 400))
col2.thumbnail((400, 400))
col3.thumbnail((400, 400))

col1.save(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im2_col1.jpg')
col2.save(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im2_col2.jpg')
col3.save(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im2_col3.jpg')

print("Saved im2 3-column thumbnails!")
