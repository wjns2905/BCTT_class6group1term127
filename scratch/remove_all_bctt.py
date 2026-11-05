import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

# 1. HTML files
html_files = [
    'about.html',
    'human-stories.html',
    'in-depth.html',
    'index.html',
    'mind-soul.html',
    'society.html',
    'trending.html'
]

footer_target = 'Học phần Báo chí &amp; Truyền thông (BCTT)'
footer_replacement = 'Tòa soạn Báo chí &amp; Truyền thông Đa phương tiện'

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Footer
    html = html.replace(footer_target, footer_replacement)
    
    # Category page hero descriptions
    html = re.sub(r'\s*trích xuất từ.*?\[BCTT\]\s*Human stories\.', '.', html)
    html = re.sub(r'\s*trích xuất từ.*?\[BCTT\]\s*In-dept\.', '.', html)
    html = re.sub(r'\s*trích xuất từ.*?\[BCTT\]\s*Mind &amp; Soul\.', '.', html)
    html = re.sub(r'\s*trích xuất từ.*?\[BCTT\]\s*Society\.', '.', html)
    html = re.sub(r'\s*trích xuất từ.*?\[BCTT\]\s*Trending\.', '.', html)

    # Index specific
    html = html.replace('Ấn phẩm BCTT • ULIS - VNU', 'Ấn phẩm Báo điện tử • ULIS - VNU')
    html = html.replace('(BCTT Project).', '.')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✓ Cleaned HTML: {fpath}")

# 2. js/translations.js
with open('js/translations.js', 'r', encoding='utf-8') as f:
    tjs = f.read()

# Replace in translations.js
tjs = tjs.replace(' • BCTT</span>', '</span>')
tjs = tjs.replace('Ấn phẩm BCTT • ULIS - VNU', 'Ấn phẩm Báo điện tử • ULIS - VNU')
tjs = tjs.replace('Học phần Báo chí & Truyền thông (BCTT)', 'Tòa soạn Báo chí & Truyền thông Đa phương tiện')
tjs = tjs.replace('(BCTT Project).', '.')
tjs = tjs.replace('BCTT Journal • ULIS - VNU', 'Digital Journal • ULIS - VNU')
tjs = tjs.replace('Journalism & Media Studies (BCTT)', 'Multimedia Journalism & Publishing')

# Remove docx references in descriptions
tjs = re.sub(r'\s*trích xuất từ.*?\[BCTT\]\s*Trending\.', '.', tjs)
tjs = re.sub(r'\s*trích xuất từ.*?\[BCTT\]\s*Society\.', '.', tjs)
tjs = re.sub(r'\s*trích xuất từ.*?\[BCTT\]\s*Human stories\.', '.', tjs)
tjs = re.sub(r'\s*trích xuất từ.*?\[BCTT\]\s*Mind & Soul\.', '.', tjs)
tjs = re.sub(r'\s*trích xuất từ.*?\[BCTT\]\s*In-dept\.', '.', tjs)

tjs = re.sub(r'\s*extracted from official \[BCTT\] Trending resources\.', '.', tjs)
tjs = re.sub(r'\s*from \[BCTT\] Society\.', '.', tjs)
tjs = re.sub(r'\s*from \[BCTT\] Human stories\.', '.', tjs)
tjs = re.sub(r'\s*from \[BCTT\] Mind & Soul\.', '.', tjs)
tjs = re.sub(r'\s*from \[BCTT\] In-dept\.', '.', tjs)

# Comments
tjs = tjs.replace('[BCTT] Profiles.docx', 'Editorial Profiles')

with open('js/translations.js', 'w', encoding='utf-8') as f:
    f.write(tjs)
print("✓ Cleaned js/translations.js")

# 3. js/app.js
with open('js/app.js', 'r', encoding='utf-8') as f:
    ajs = f.read()

ajs = ajs.replace('[BCTT] Video', 'Video Journal')
ajs = ajs.replace('BCTT', '') # any remaining stray occurrences

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(ajs)
print("✓ Cleaned js/app.js")

# 4. css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('[BCTT] PROFILES.DOCX', 'EDITORIAL PROFILES')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("✓ Cleaned css/style.css")

print("\nDone removing all BCTT text from site files!")
