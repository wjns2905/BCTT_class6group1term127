# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

img_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops'

# Let's inspect im1: what colors, text letters, aspect ratio
im1 = Image.open(os.path.join(img_dir, 'im1.png'))
print("im1 size:", im1.size)
# What is the font style in im1? Let's check colors
# In im1, is it Didone / Bodoni serif, or script, or sans?
# Let's inspect where dark pixels are in im1
w, h = im1.size
im1_gray = im1.convert('L')
# count dark pixels
dark_pixels = sum(1 for y in range(h) for x in range(w) if im1_gray.getpixel((x, y)) < 100)
print(f"im1 dark pixels: {dark_pixels} ({dark_pixels/(w*h)*100:.1f}%)")

# Let's check im8 (what title font the user likes)
im8 = Image.open(os.path.join(img_dir, 'im8.png'))
w8, h8 = im8.size
im8_gray = im8.convert('L')
dark8 = sum(1 for y in range(h8) for x in range(w8) if im8_gray.getpixel((x, y)) < 100)
print(f"im8 dark pixels: {dark8} ({dark8/(w8*h8)*100:.1f}%)")

# Let's check im5_header
im5 = Image.open(os.path.join(img_dir, 'im5_header.png'))
print(f"im5 header size: {im5.size}")

# Let's check im6_header
im6 = Image.open(os.path.join(img_dir, 'im6_header.png'))
print(f"im6 header size: {im6.size}")
