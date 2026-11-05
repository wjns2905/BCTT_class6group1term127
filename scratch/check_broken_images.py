# -*- coding: utf-8 -*-
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

root_dir = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127"
broken = []
valid = []
all_refs = 0

for root, dirs, files in os.walk(root_dir):
    if "scratch" in root or ".git" in root:
        continue
    for f in files:
        if f.endswith((".html", ".js", ".json")):
            fp = os.path.join(root, f)
            with open(fp, "r", encoding="utf-8", errors="ignore") as fl:
                content = fl.read()
            # Match quotes around assets/images
            matches = re.findall(r'["\'](assets/images/[^"\']+)["\']', content)
            for img in matches:
                all_refs += 1
                disk_path = os.path.join(root_dir, img.replace('/', os.sep))
                if not os.path.exists(disk_path):
                    broken.append((f, img))
                else:
                    valid.append((f, img))

print(f"Total image references checked: {all_refs}")
print(f"Broken image references count: {len(broken)}")
for f, img in sorted(set(broken)):
    print(f"  FILE: {f} -> MISSING: {img}")
