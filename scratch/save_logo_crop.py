# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

im1 = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im1.png')

# In im1, crop the logo:
# Let's crop tight bbox
gray = im1.convert('L')
bbox = gray.point(lambda p: 255 if p < 240 else 0).getbbox()
print("im1 bbox:", bbox)
if bbox:
    logo_crop = im1.crop(bbox)
    
    # Save to assets/images/logo/ in both BCTT and BCTT_class6group1term127
    paths = [
        r'C:\Users\camka\OneDrive\Desktop\BCTT\assets\images\logo\brand_logo_updated.png',
        r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\assets\images\logo\brand_logo_updated.png'
    ]
    for p in paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        logo_crop.save(p)
        print("Saved logo to:", p)
