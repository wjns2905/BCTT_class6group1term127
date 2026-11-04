# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

im12 = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im12.png')

# Let's find rows with high color variance or specific banner colors (purple (90, 0, 191), red (226, 24, 55))
w, h = im12.size
banner_rows = []
for y in range(h):
    row_pixels = [im12.getpixel((x, y)) for x in range(0, w, 10)]
    has_purple = any(abs(p[0] - 90) < 30 and abs(p[1] - 0) < 30 and abs(p[2] - 191) < 30 for p in row_pixels)
    has_red = any(abs(p[0] - 226) < 30 and abs(p[1] - 24) < 30 and abs(p[2] - 55) < 30 for p in row_pixels)
    if has_purple or has_red:
        banner_rows.append(y)

if banner_rows:
    print(f"IELTS Banner detected from y={min(banner_rows)} to y={max(banner_rows)}")
    # crop the full ad banner
    y1 = max(0, min(banner_rows) - 5)
    y2 = min(h, max(banner_rows) + 5)
    ad_crop = im12.crop((0, y1, w, y2))
    ad_out = r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\ielts_banner_ad.png'
    ad_crop.save(ad_out)
    print(f"Saved extracted IELTS banner ad ({ad_crop.size}) to {ad_out}!")
else:
    print("Could not detect purple/red rows automatically, let's inspect colors")
