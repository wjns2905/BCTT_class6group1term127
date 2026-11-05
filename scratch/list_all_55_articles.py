# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\data.js", "r", encoding="utf-8") as f:
    text = f.read()

start = text.find("const ARTICLES_DATA = [") + len("const ARTICLES_DATA = [")
end = text.rfind("];")
articles = json.loads("[" + text[start:end].strip() + "]")

print(f"Total articles: {len(articles)}\n")

by_cat = {}
for i, a in enumerate(articles):
    by_cat.setdefault(a["category"], []).append((i, a))

for cat, list_art in by_cat.items():
    print(f"==================================================")
    print(f"CATEGORY: {cat} ({len(list_art)} articles)")
    print(f"==================================================")
    for idx, a in list_art:
        print(f"  [{a['id']}] {a['title'][:70]}")
        print(f"       Source: {a.get('sourceName', '')} | Author: {a.get('author', '')}")
        print(f"       Image: {a.get('image', '')}")
    print()
