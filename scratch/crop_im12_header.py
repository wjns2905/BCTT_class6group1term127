# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

im12 = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im12.png')

# Let's inspect where the ad banner is:
# Usually ads on websites like VietnamNet / Tuoi Tre / Thanh Nien have a leaderboard banner at top (728x90 or 970x90 or 970x250)
# Let's find rows where the ad starts and ends
# In a typical screenshot, the browser top bar is at y=0..80, then the leaderboard banner is at y=80..250, then the site masthead
# Let's save a clear crop of y=0 to y=350
im12.crop((0, 0, im12.width, 350)).save(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im12_header_region.png')
print("Saved im12_header_region.png")
