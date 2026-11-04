# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

im11 = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops\im11.png')
# Let's see what colors are in im11
print("im11 mode:", im11.mode)
# Let's inspect rows to find where text lines are
im_gray = im11.convert('L')
w, h = im11.size
row_brightness = []
for y in range(h):
    row = [im_gray.getpixel((x, y)) for x in range(w)]
    avg = sum(row) / w
    row_brightness.append(avg)

# find text regions (where brightness differs from background)
bg = row_brightness[0]
print(f"Background brightness: {bg:.1f}")
text_lines = []
in_line = False
start_y = 0
for y, b in enumerate(row_brightness):
    if abs(b - bg) > 5:
        if not in_line:
            in_line = True
            start_y = y
    else:
        if in_line:
            in_line = False
            text_lines.append((start_y, y))

print(f"Detected {len(text_lines)} text bands in im11:")
for i, (sy, ey) in enumerate(text_lines):
    print(f" Band {i+1}: y={sy} to {ey} (height={ey-sy})")
