import sys, json, re

sys.stdout.reconfigure(encoding='utf-8')
articles = json.loads(re.search(r'const ARTICLES_DATA = (\[.*?\]);', open('js/data.js', encoding='utf-8').read(), re.DOTALL).group(1))
lengths = [len(a.get('content', [])) for a in articles]
print(f'Total articles: {len(articles)}')
print(f'Min content length: {min(lengths)}, Max: {max(lengths)}, Avg: {sum(lengths)/len(lengths):.1f}')
short_articles = [a for a in articles if len(a.get('content', [])) < 6]
print(f'Articles with < 6 paragraphs: {len(short_articles)}')
for a in short_articles:
    print(f"  {a.get('id'):12}: {len(a.get('content', []))} paras | {a.get('title_en', '')[:60]}")
