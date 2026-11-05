import os, sys, glob
from PIL import Image
sys.stdout.reconfigure(encoding='utf-8')

media_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\scratch\extracted_update_media'

# Let's check size and aspect ratios
for img_name in sorted(os.listdir(media_dir)):
    p = os.path.join(media_dir, img_name)
    im = Image.open(p)
    print(f"{img_name}: size={im.size}, aspect={im.size[0]/im.size[1]:.2f}")
