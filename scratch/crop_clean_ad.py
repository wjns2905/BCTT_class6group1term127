# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

im12 = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im12.png')

# Crop the ad banner:
# from row ~25 to ~260
ad_banner = im12.crop((160, 20, 1888, 260))
ad_banner.save(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\header_ad_banner_clean.png')
print("Saved header_ad_banner_clean.png, size:", ad_banner.size)
