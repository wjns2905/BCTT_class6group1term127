import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Match the json array
start = content.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
end = content.rfind('];') + 1

json_str = content[start:end]
articles = json.loads(json_str)

print(f"Total articles: {len(articles)}")
cat_counts = {}
for a in articles:
    c = a.get('category', 'unknown')
    cat_counts[c] = cat_counts.get(c, 0) + 1

print("\nCounts per category:")
for cat, cnt in sorted(cat_counts.items()):
    print(f"  {cat}: {cnt}")

print("\nListing all articles:")
for i, a in enumerate(articles, 1):
    print(f"{i:2d}. [{a['category']:14s}] {a['id']:12s} | {a['title'][:65]}")
