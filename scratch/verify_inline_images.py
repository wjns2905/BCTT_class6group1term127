import sys, json, re, os

sys.stdout.reconfigure(encoding='utf-8')
articles = json.loads(re.search(r'const ARTICLES_DATA = (\[.*?\]);', open('js/data.js', encoding='utf-8').read(), re.DOTALL).group(1))

broken = []
total_found = 0
for a in articles:
    c = a.get('content', [])
    for p in c:
        if '<figure' in p:
            m = re.search(r'src="([^"]+)"', p)
            if m:
                total_found += 1
                src = m.group(1)
                if not os.path.exists(src):
                    broken.append((a['id'], src))

print(f"Total inline images checked: {total_found}")
print(f"Broken inline images: {len(broken)}")
for aid, src in broken:
    print(f"  [BROKEN] {aid} -> {src}")
