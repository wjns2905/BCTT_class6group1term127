import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const ARTICLES_DATA = (\[[\s\S]*?\]);\s*(?:window\.|\n\w|\Z)', text)
if not m:
    print('Failed to find ARTICLES_DATA')
    sys.exit(1)

data = json.loads(m.group(1))
print(f'Total articles: {len(data)}')

for i, a in enumerate(data):
    print(f"{i+1}. [{a['id']}] ({a['category']}) '{a['title'][:55]}' -> image: {a.get('image')}")
