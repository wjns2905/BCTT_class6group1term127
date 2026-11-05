import sys, json, re

sys.stdout.reconfigure(encoding='utf-8')
with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()
m = re.search(r'const ARTICLES_DATA = (\[.*?\]);', text, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    videos = [a for a in data if a.get('video')]
    print(f'Total video articles: {len(videos)}')
    for v in videos:
        print(f"{v['id']}: video={v.get('video')} | img={v.get('image')} | title={v.get('title')}")
