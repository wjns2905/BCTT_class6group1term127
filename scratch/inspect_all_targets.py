# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

img_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops'

# Let's inspect image1.png (logo)
im1 = Image.open(os.path.join(img_dir, 'im1.png'))
print(f"im1 size: {im1.size}")

# Let's inspect image8.png (title font)
im8 = Image.open(os.path.join(img_dir, 'im8.png'))
print(f"im8 size: {im8.size}")

# Let's inspect image5.png (video section)
im5 = Image.open(os.path.join(img_dir, 'im5.png'))
print(f"im5 size: {im5.size}")

# Let's inspect image6.png (game/donate)
im6 = Image.open(os.path.join(img_dir, 'im6.png'))
print(f"im6 size: {im6.size}")

# Let's inspect image7.png (op-ed & poll)
im7 = Image.open(os.path.join(img_dir, 'im7.png'))
print(f"im7 size: {im7.size}")

# Let's inspect image10.png (about us)
im10 = Image.open(os.path.join(img_dir, 'im10.png'))
print(f"im10 size: {im10.size}")
