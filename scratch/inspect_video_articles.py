import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

data = json.loads(re.search(r'const ARTICLES_DATA = (\[[\s\S]*?\]);', text).group(1))

for a in data:
    if a['id'].startswith('video-'):
        print(f"{a['id']} ({a['category']}) -> '{a['title']}' | image: {a.get('image')}")
