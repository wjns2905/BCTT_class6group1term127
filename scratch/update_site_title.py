import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

html_titles = {
    'index.html': 'Class6group1term127',
    'trending.html': 'Class6group1term127 - Trending',
    'society.html': 'Class6group1term127 - Society',
    'human-stories.html': 'Class6group1term127 - Human Stories',
    'mind-soul.html': 'Class6group1term127 - Mind & Soul',
    'in-depth.html': 'Class6group1term127 - In-depth',
    'about.html': 'Class6group1term127 - About Us'
}

for fname, title in html_titles.items():
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace title
    html = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html, count=1)

    # Ensure meta site_name and application-name are in head
    meta_tags = f'''  <meta name="application-name" content="Class6group1term127">
  <meta property="og:site_name" content="Class6group1term127">'''
    
    if 'og:site_name' not in html:
        html = html.replace('</head>', f'{meta_tags}\n</head>', 1)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✓ Updated site title and meta tags in {fname} -> <title>{title}</title>")

print("\nDone updating site title to Class6group1term127!")
