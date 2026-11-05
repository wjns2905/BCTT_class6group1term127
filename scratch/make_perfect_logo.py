import sys, os, shutil
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

# 1. Backup current logo
current_logo = 'assets/images/logo/brand_logo_updated.png'
shutil.copyfile(current_logo, 'scratch/brand_logo_backup.png')

# 2. Open source image1.png
source_im1 = 'scratch/update_docx_media/image1.png'
im = Image.open(source_im1)
print(f"Source image1 size: {im.size}")

# Crop with generous pink aura on top (y=60) and clean bottom (y=385), width x=55 to 1285
# Text Y is 131 to 364.
# From y=60 to 131: 71px of pink aura above text.
# From y=364 to 385: 21px of clean space below text/slogan.
crop_box = (55, 60, 1285, 385)
cropped = im.crop(crop_box)
print(f"Cropped logo size: {cropped.size}")

# Save to assets/images/logo/brand_logo_updated.png
cropped.save(current_logo, 'PNG', optimize=True)
print(f"✓ Saved updated logo to {current_logo} ({os.path.getsize(current_logo)} bytes)")
