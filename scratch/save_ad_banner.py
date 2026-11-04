# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

src_banner = r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\header_ad_banner_clean.png'
dest_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT\assets\images\ads'
os.makedirs(dest_dir, exist_ok=True)
dest_banner = os.path.join(dest_dir, 'header_ad_banner.png')

with Image.open(src_banner) as im:
    im.save(dest_banner)
    print(f"Saved banner ad ({im.size}) to {dest_banner}!")
