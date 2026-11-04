# -*- coding: utf-8 -*-
import sys, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

img_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\update_docx_media'
crop_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\crops'

# 1. Let's inspect image1.png (logo)
im1 = Image.open(os.path.join(img_dir, 'image1.png'))
im1.save(os.path.join(crop_dir, 'im1.png'))
print(f"im1 size: {im1.size}")

# 2. Let's crop and inspect image2.jpg (3-col layout)
im2 = Image.open(os.path.join(img_dir, 'image2.jpg'))
im2.save(os.path.join(crop_dir, 'im2.jpg'))
print(f"im2 size: {im2.size}")

# 3. image3.png (left col)
im3 = Image.open(os.path.join(img_dir, 'image3.png'))
im3.save(os.path.join(crop_dir, 'im3.png'))

# 4. image4.png (right col)
im4 = Image.open(os.path.join(img_dir, 'image4.png'))
im4.save(os.path.join(crop_dir, 'im4.png'))

# 5. image5.png (video replacement)
im5 = Image.open(os.path.join(img_dir, 'image5.png'))
im5.save(os.path.join(crop_dir, 'im5.png'))

# 6. image6.png (game / donate)
im6 = Image.open(os.path.join(img_dir, 'image6.png'))
im6.save(os.path.join(crop_dir, 'im6.png'))

# 7. image7.png (op-ed & poll)
im7 = Image.open(os.path.join(img_dir, 'image7.png'))
im7.save(os.path.join(crop_dir, 'im7.png'))

# 8. image8.png (title font)
im8 = Image.open(os.path.join(img_dir, 'image8.png'))
im8.save(os.path.join(crop_dir, 'im8.png'))

# 9. image9.png (welcome/subscribe)
im9 = Image.open(os.path.join(img_dir, 'image9.png'))
im9.save(os.path.join(crop_dir, 'im9.png'))

# 10. image10.png & image11.png (about us)
im10 = Image.open(os.path.join(img_dir, 'image10.png'))
im10.save(os.path.join(crop_dir, 'im10.png'))
im11 = Image.open(os.path.join(img_dir, 'image11.png'))
im11.save(os.path.join(crop_dir, 'im11.png'))

# 11. image12.png (header ad)
im12 = Image.open(os.path.join(img_dir, 'image12.png'))
im12.save(os.path.join(crop_dir, 'im12.png'))

print("All 12 images processed and saved to crops!")
