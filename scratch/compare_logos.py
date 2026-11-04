# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

im1 = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im1.png')
print("im1 size:", im1.size)

# Let's crop into sections or check text
# We can also check image8.png
im8 = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im8.png')
print("im8 size:", im8.size)

# Let's check image12.png (header ad)
im12 = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im12.png')
print("im12 size:", im12.size)
# The IELTS ad banner is usually at the top or a banner across the page
# Let's crop the ad from im12
