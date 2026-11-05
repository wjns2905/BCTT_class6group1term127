import sys, json, re

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

articles = json.loads(re.search(r'const ARTICLES_DATA = (\[.*?\]);', text, re.DOTALL).group(1))

# Let's count articles with < 6 items
short_arts = [a for a in articles if len(a.get('content', [])) < 6]
print(f"Total short articles (< 6 items): {len(short_arts)}")
for a in short_arts[:10]:
    print(f"  {a['id']}: {len(a['content'])} items | {a['title_en'][:50]}")
