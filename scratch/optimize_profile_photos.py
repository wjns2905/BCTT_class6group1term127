# -*- coding: utf-8 -*-
import os
import sys
from PIL import Image, ImageOps

sys.stdout.reconfigure(encoding='utf-8')

profiles_dir = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\assets\images\profiles"

for f in os.listdir(profiles_dir):
    if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        fp = os.path.join(profiles_dir, f)
        try:
            with Image.open(fp) as im:
                print(f"File: {f} | Size: {im.size} | Format: {im.format} | Mode: {im.mode}")
                # Auto-transpose based on EXIF orientation
                transposed = ImageOps.exif_transpose(im)
                
                # If RGB or RGBA, keep quality high
                if transposed.mode not in ('RGB', 'RGBA'):
                    transposed = transposed.convert('RGB')
                
                # Overwrite with properly oriented, optimized JPEG
                transposed.save(fp, "JPEG", quality=92, optimize=True)
                new_size = os.path.getsize(fp)
                print(f"  -> Properly oriented & saved {f}: {transposed.size}, {new_size} bytes")
        except Exception as e:
            print(f"Error processing {f}: {e}")
