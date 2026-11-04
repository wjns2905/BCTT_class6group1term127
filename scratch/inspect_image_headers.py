# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

img_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops'

# Let's crop im1.png to where the logo text is
im1 = Image.open(os.path.join(img_dir, 'im1.png'))
# find non-transparent or non-white
im1_rgb = im1.convert('RGB')
im1_rgb.save(os.path.join(img_dir, 'im1_view.png'))

# Let's crop im8.png to where the title text is
im8 = Image.open(os.path.join(img_dir, 'im8.png'))
im8_rgb = im8.convert('RGB')
im8_rgb.save(os.path.join(img_dir, 'im8_view.png'))

# Let's check im5 (section to change to video)
im5 = Image.open(os.path.join(img_dir, 'im5.png'))
# crop header of im5
im5.crop((0, 0, im5.width, min(250, im5.height))).save(os.path.join(img_dir, 'im5_header.png'))

# Let's check im6 (game/donate section)
im6 = Image.open(os.path.join(img_dir, 'im6.png'))
im6.crop((0, 0, im6.width, min(250, im6.height))).save(os.path.join(img_dir, 'im6_header.png'))

# Let's check im7 (op-ed & poll)
im7 = Image.open(os.path.join(img_dir, 'im7.png'))
im7.crop((0, 0, im7.width, min(250, im7.height))).save(os.path.join(img_dir, 'im7_header.png'))

print("Saved headers and views for inspection!")
