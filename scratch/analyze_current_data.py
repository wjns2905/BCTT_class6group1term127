# -*- coding: utf-8 -*-
import json
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

with open(r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\data.js", "r", encoding="utf-8") as f:
    text = f.read()

# Extract JSON array or regex
items = re.findall(r'"id":\s*"([^"]+)",\s*"category":\s*"([^"]+)"', text)
print(f"Total current articles: {len(items)}")
counts = Counter(cat for aid, cat in items)
for cat, count in sorted(counts.items()):
    print(f"  Category '{cat}': {count} articles")

# Check article titles to find exact duplicates
titles = re.findall(r'"id":\s*"([^"]+)",\s*"category":\s*"([^"]+)"(?:[^}]+?)"title":\s*"([^"]+)"', text)
title_map = {}
for aid, cat, title in titles:
    title_clean = title.strip().lower()
    title_map.setdefault(title_clean, []).append((aid, cat, title))

print("\n--- Duplicate or Shared Titles across categories ---")
for t_clean, occurrences in title_map.items():
    if len(occurrences) > 1:
        print(f"Title: {occurrences[0][2][:60]}...")
        for aid, cat, _ in occurrences:
            print(f"   -> [{aid}] in '{cat}'")
