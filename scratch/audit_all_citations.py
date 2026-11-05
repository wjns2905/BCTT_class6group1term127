import sys, json, re, urllib.parse

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

articles = json.loads(re.search(r'const ARTICLES_DATA = (\[.*?\]);', text, re.DOTALL).group(1))

print(f"Auditing {len(articles)} article citation links...\n")

source_name_map = {
    'nhandan.vn': ('Báo Nhân Dân điện tử', 'Nhân Dân Online (NDO)'),
    'theguardian.com': ('The Guardian (UK)', 'The Guardian (UK)'),
    'vnexpress.net': ('VnExpress Quốc tế', 'VnExpress International'),
    'vietnamnews.vn': ('Việt Nam News (TTXVN)', 'Việt Nam News (VNA)'),
    'vietnamnet.vn': ('VietNamNet Quốc tế', 'VietNamNet Global'),
    'laodong.vn': ('Báo Lao Động', 'Lao Động News'),
    'cnn.com': ('CNN Quốc tế', 'CNN International'),
    'positive.news': ('Positive News (UK)', 'Positive News (UK)'),
    'harvard.edu': ('Harvard Health Publishing', 'Harvard Health Publishing'),
    'vovworld.vn': ('VOV World (Đài Tiếng nói Việt Nam)', 'VOV World (Voice of Vietnam)'),
    'washingtonpost.com': ('The Washington Post', 'The Washington Post'),
    'goodnewsnetwork.org': ('Good News Network', 'Good News Network'),
    'tuoitre.vn': ('Báo Tuổi Trẻ Quốc tế', 'Tuoi Tre News'),
    'abcnews.com': ('ABC News', 'ABC News'),
    'youtube.com': ('YouTube (Nền tảng Video)', 'YouTube Media')
}

issues = []
for idx, a in enumerate(articles):
    aid = a.get('id')
    title = a.get('title_en', a.get('title', ''))
    url = a.get('sourceUrl', '')
    
    if not url:
        issues.append((aid, "Missing URL", url))
        continue
        
    if not url.startswith('http://') and not url.startswith('https://'):
        issues.append((aid, "Invalid Protocol", url))
        continue

    # Parse domain
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc.lower()
    
    # Check tracking params
    if '_gl=' in url or 'utm_source=' in url:
        clean_url = url.split('?')[0]
        issues.append((aid, f"Has tracking params -> clean to: {clean_url}", url))

    # Match source name
    matched_source = False
    for k in source_name_map:
        if k in domain:
            matched_source = True
            break
            
    print(f"[{aid:12}] {domain:22} | {title[:40]}...")

print(f"\nAudit complete. Issues found: {len(issues)}")
for item in issues:
    print(f"  Issue in {item[0]}: {item[1]}")
