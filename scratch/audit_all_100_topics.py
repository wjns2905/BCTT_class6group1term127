import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const ARTICLES_DATA = (\[[\s\S]*?\]);\s*(?:window\.|\n\w|\Z)', text)
data = json.loads(m.group(1))

print(f"Total articles: {len(data)}")
for i, a in enumerate(data):
    cat = a.get('category')
    aid = a.get('id')
    title = a.get('title')
    title_en = a.get('title_en', '')
    cur_img = a.get('image')
    src_url = a.get('sourceUrl', '')
    print(f"[{aid}] ({cat})\n  Title: {title}\n  Title_EN: {title_en}\n  Current Image: {cur_img}\n  SourceUrl: {src_url}\n")
