import sys
from PIL import Image
sys.stdout.reconfigure(encoding='utf-8')

img_path = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\assets\images\logo\brand_logo_updated.png'
im = Image.open(img_path)
print("Image size:", im.size, "Mode:", im.mode)

# Let's inspect bottom rows of pixels
w, h = im.size
print("Bottom 20 rows sample colors:")
for y in range(h - 20, h, 2):
    row_colors = [im.getpixel((x, y)) for x in range(0, w, w // 10)]
    print(f"y={y}: center={im.getpixel((w//2, y))}, left={im.getpixel((10, y))}")
