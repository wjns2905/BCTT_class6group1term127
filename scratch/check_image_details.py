from PIL import Image
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

for folder in ['assets/images/mind_&_soul', 'assets/images/society']:
    print(f"\nFolder: {folder}")
    files = sorted(os.listdir(folder))
    for f in files:
        fp = os.path.join(folder, f)
        try:
            with Image.open(fp) as im:
                print(f"  {f:15s} : {im.size} {im.format}")
        except Exception as e:
            print(f"  {f:15s} : {e}")
