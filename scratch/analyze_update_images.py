# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

img_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\update_docx_media'

def analyze_img(fname):
    p = os.path.join(img_dir, fname)
    with Image.open(p) as im:
        w, h = im.size
        # sample some colors or detect content
        print(f"\n=== {fname} ({w}x{h}) ===")
        # check if it has text or specific features
        # let's save a smaller preview or check color histogram
        colors = im.convert('RGB').getcolors(maxcolors=1000000)
        top_colors = sorted(colors, key=lambda c: c[0], reverse=True)[:5]
        print("Top colors:", [(count, col) for count, col in top_colors])

for f in ['image1.png', 'image2.jpg', 'image3.png', 'image4.png', 'image5.png', 'image6.png', 'image7.png', 'image8.png', 'image9.png', 'image10.png', 'image11.png', 'image12.png']:
    analyze_img(f)
