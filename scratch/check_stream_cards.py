import sys, json, re

sys.stdout.reconfigure(encoding='utf-8')
with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()
m = re.search(r'const ARTICLES_DATA = (\[.*?\]);', text, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    for aid in ['trending-4', 'trending-5', 'mind-1', 'mind-2', 'human-5', 'society-1']:
        art = next((x for x in data if x['id'] == aid), None)
        if art:
            print(f"{aid}: img={art['image']} | vi={art['title'][:40]}")
