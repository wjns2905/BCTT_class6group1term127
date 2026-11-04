# -*- coding: utf-8 -*-
import sys, os, shutil
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

src_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\update_docx_media'
dest_dir = r'C:\Users\camka\.gemini\antigravity\brain\50d7ed23-5f2b-4287-91eb-56c336819532\update_media'
os.makedirs(dest_dir, exist_ok=True)

for f in sorted(os.listdir(src_dir)):
    src_file = os.path.join(src_dir, f)
    dest_file = os.path.join(dest_dir, f)
    shutil.copy2(src_file, dest_file)
    print(f"Copied {f} to artifacts update_media")
