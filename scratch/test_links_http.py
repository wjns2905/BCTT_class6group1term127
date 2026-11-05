import sys, json, re, urllib.request, urllib.error

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

articles = json.loads(re.search(r'const ARTICLES_DATA = (\[.*?\]);', text, re.DOTALL).group(1))

# Headers to avoid bot blocking
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

print("Testing accessibility of primary docx and key articles...")

# Let's test the docx articles first
docx_ids = [
    'trending-1', 'trending-2', 'trending-3', 'trending-4', 'trending-5', 'trending-6',
    'society-1', 'society-6', 'society-7', 'society-8', 'society-9', 'society-10',
    'human-1', 'human-2', 'human-3', 'human-4', 'human-9', 'human-10',
    'mind-1', 'mind-2', 'mind-3', 'mind-5', 'mind-7',
    'indepth-1', 'indepth-2', 'indepth-3', 'indepth-4', 'indepth-5'
]

results = []
for aid in docx_ids:
    art = next((a for a in articles if a['id'] == aid), None)
    if not art: continue
    url = art.get('sourceUrl', '')
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            code = resp.getcode()
            results.append((aid, code, "OK", url))
            print(f"[{aid:12}] HTTP {code} OK -> {url[:60]}")
    except urllib.error.HTTPError as e:
        results.append((aid, e.code, "HTTPError", url))
        print(f"[{aid:12}] HTTP {e.code} Error -> {url[:60]}")
    except Exception as e:
        results.append((aid, 0, str(e)[:30], url))
        print(f"[{aid:12}] Connection Error: {str(e)[:30]} -> {url[:60]}")

print("\nSummary:")
success = sum(1 for r in results if r[1] == 200)
print(f"Total checked: {len(results)}, Successful (HTTP 200): {success}")
