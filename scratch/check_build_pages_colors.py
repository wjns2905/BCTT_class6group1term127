import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/build_multi_pages.py", "r", encoding="utf-8") as f:
    code = f.read()

import re
matches = re.findall(r'color:\s*([^;"]+)', code)
print(f"Colors found in build_multi_pages.py: {set(matches)}")
