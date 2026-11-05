import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

data = json.loads(re.search(r'const ARTICLES_DATA = (\[[\s\S]*?\]);', text).group(1))

from collections import Counter
counts = Counter(a['category'] for a in data)
print('Category counts in data:', counts)
print('All IDs in data:')
for cat in ['trending', 'society', 'human-stories', 'mind-soul', 'in-depth']:
    cat_ids = [a['id'] for a in data if a['category'] == cat]
    print(f'  {cat} ({len(cat_ids)}): {cat_ids}')
