# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

img_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops'

# Let's inspect im5 (the section user wants to change to video):
# Let's crop the text area in im5 (e.g. top-left header)
im5 = Image.open(os.path.join(img_dir, 'im5.png'))
w, h = im5.size

# Let's crop multiple areas: top-left (section title), middle, right
im5_title = im5.crop((0, 0, min(w, 800), min(h, 200)))
im5_title.save(os.path.join(img_dir, 'im5_title_crop.png'))

# In im6:
im6 = Image.open(os.path.join(img_dir, 'im6.png'))
w6, h6 = im6.size
im6_title = im6.crop((0, 0, min(w6, 800), min(h6, 200)))
im6_title.save(os.path.join(img_dir, 'im6_title_crop.png'))

# In im7:
im7 = Image.open(os.path.join(img_dir, 'im7.png'))
w7, h7 = im7.size
im7_title = im7.crop((0, 0, min(w7, 800), min(h7, 200)))
im7_title.save(os.path.join(img_dir, 'im7_title_crop.png'))

print("Saved title crops for im5, im6, im7!")
