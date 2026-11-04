import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("js/data.js", "r", encoding="utf-8") as f:
    text = f.read()

m = re.search(r'const ARTICLES_DATA\s*=\s*(\[\s*\{.*\}\s*\]);', text, re.DOTALL)
if m:
    articles = json.loads(m.group(1))
    print(f"Total articles: {len(articles)}")
    by_cat = {}
    for a in articles:
        cat = a["category"]
        by_cat.setdefault(cat, []).append(a)

    for cat, arts in by_cat.items():
        print(f"\n--- Category: {cat} ({len(arts)} articles) ---")
        for a in arts:
            print(f"  [{a['id']}] {a['title'][:65]}...")
else:
    print("Could not parse ARTICLES_DATA with regex")
