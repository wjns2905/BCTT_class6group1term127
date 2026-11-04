import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("js/data.js", "r", encoding="utf-8") as f:
    text = f.read()

m = re.search(r'const ARTICLES_DATA\s*=\s*(\[\s*\{.*\}\s*\]);', text, re.DOTALL)
articles = json.loads(m.group(1))

for a in articles:
    if a['id'] in ['mind-1', 'indepth-1']:
        print(f"\n=== Article {a['id']} ===")
        print(f"Title: {a['title']}")
        print(f"Subtitle: {a['subtitle']}")
        print(f"Content length: {len(a['content'])} paragraphs")
        for i, p in enumerate(a['content'][:3]):
            print(f"  P{i+1}: {p[:80]}...")
