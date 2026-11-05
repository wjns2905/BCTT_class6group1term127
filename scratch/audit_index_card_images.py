import sys, json, re

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()
m = re.search(r'const ARTICLES_DATA = (\[.*?\]);', text, re.DOTALL)
articles_by_id = {a['id']: a for a in json.loads(m.group(1))}

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all blocks with onclick="openArticleModal('...')" and their img src
cards = re.findall(r'(<article[^>]*onclick="openArticleModal\(\'([^\']+)\'\)"[^>]*>.*?<\/article>)', html, re.DOTALL)
print(f"Found {len(cards)} article cards in index.html")

mismatches = []
for full_card, aid in cards:
    art = articles_by_id.get(aid)
    if not art:
        print(f"Article {aid} not found in ARTICLES_DATA!")
        continue
    img_match = re.search(r'src="([^"]+)"', full_card)
    current_src = img_match.group(1) if img_match else None
    target_src = art.get('image')
    if current_src != target_src and not (current_src and current_src.startswith('data:')):
        mismatches.append((aid, current_src, target_src))

print(f"\nTotal image mismatches in index.html: {len(mismatches)}")
for aid, cur, target in mismatches:
    print(f"  [{aid}]: current='{cur}' -> target='{target}'")
