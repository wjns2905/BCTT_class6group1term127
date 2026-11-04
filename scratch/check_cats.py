import re

with open("js/data.js", "r", encoding="utf-8") as f:
    s = f.read()

matches = re.findall(r'"category":\s*"([^"]+)"', s)
from collections import Counter
counts = Counter(matches)
print("Categories and counts in data.js:")
for cat, count in counts.items():
    print(f"  - {cat}: {count} articles")
