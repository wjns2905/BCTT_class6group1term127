# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

img_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops'

# Let's inspect image1.png (the logo)
im1 = Image.open(os.path.join(img_dir, 'im1.png'))
# It has a logo: Let's find bounding box of non-white pixels
# Convert to grayscale
im1_gray = im1.convert('L')
bbox1 = im1_gray.point(lambda p: 255 if p < 240 else 0).getbbox()
print("im1 non-white bbox:", bbox1)

# Let's crop and inspect image11.png (344x470) - this is About Us dropdown menu!
im11 = Image.open(os.path.join(img_dir, 'im11.png'))
print("im11 size:", im11.size)

# Let's inspect image8.png (1338x426) - title font
im8 = Image.open(os.path.join(img_dir, 'im8.png'))
print("im8 size:", im8.size)

# Let's inspect image12.png top area (header ad)
im12 = Image.open(os.path.join(img_dir, 'im12.png'))
print("im12 size:", im12.size)
