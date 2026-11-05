# -*- coding: utf-8 -*-
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\data.js", "r", encoding="utf-8") as f:
    text = f.read()

articles = re.findall(r'"id":\s*"([^"]+)",\s*"category":\s*"([^"]+)",\s*"categoryName":\s*"([^"]+)",\s*"title":\s*"([^"]+)"', text)
print(f"Total current articles in data.js: {len(articles)}")
by_cat = {}
for aid, cat, catName, title in articles:
    by_cat.setdefault(cat, []).append((aid, title))

for cat, arts in by_cat.items():
    print(f"=== Category: {cat} ({len(arts)} articles) ===")
    for aid, title in arts:
        print(f"  [{aid}] {title[:80]}")
