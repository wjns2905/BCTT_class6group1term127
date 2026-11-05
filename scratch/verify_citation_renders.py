import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
e = c.rfind('];') + 1

articles = json.loads(c[s:e])

# Test on 3 diverse articles: trending-4 (Hội An), society-1 (Cost of living), indepth-9 (Tycoon villa)
test_ids = ['trending-4', 'society-1', 'indepth-9', 'human-3', 'mind-1']
test_arts = [a for a in articles if a['id'] in test_ids]

for a in test_arts:
    print("=" * 60)
    print(f"Article ID: {a['id']}")
    print("VIETNAMESE OUTPUT:")
    print(f'Source: "{a["title"]}", {a["sourceName"]}, viết bởi {a["author"].split("•")[0].strip()}, {a["date"]}, {a["sourceUrl"]}')
    print("ENGLISH OUTPUT:")
    print(f'Source: "{a["title_en"]}", {a["sourceName"]}, by {a["author"].split("•")[0].strip()}, {a["date"]}, {a["sourceUrl"]}')
