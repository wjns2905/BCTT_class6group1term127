import sys, json, re

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

articles = json.loads(re.search(r'const ARTICLES_DATA = (\[.*?\]);', text, re.DOTALL).group(1))

print(f"Total articles: {len(articles)}")

missing_or_hash = []
urls = []
for a in articles:
    url = a.get('sourceUrl', '')
    if not url or url == '#' or not url.startswith('http'):
        missing_or_hash.append((a['id'], a.get('title_en', a.get('title', ''))[:40], url))
    else:
        urls.append((a['id'], a.get('title_en', a.get('title', ''))[:40], url))

print(f"Valid HTTP URLs: {len(urls)}")
print(f"Missing or invalid URLs: {len(missing_or_hash)}")

for item in missing_or_hash:
    print(f"  [INVALID] {item[0]}: {item[1]} -> URL: {item[2]}")

print("\nSample 15 URLs:")
for item in urls[:15]:
    print(f"  [{item[0]:12}] {item[2]}")
