import sys, docx, os
sys.stdout.reconfigure(encoding='utf-8')

docx_files = {
    'Trending': 'Tài nguyên/[BCTT] Trending.docx',
    'Society': 'Tài nguyên/[BCTT] Society.docx',
    'Human stories': 'Tài nguyên/[BCTT] Human stories.docx',
    'Mind & Soul': 'Tài nguyên/[BCTT] Mind & Soul.docx',
    'In-dept': 'Tài nguyên/[BCTT] In-dept.docx'
}

for cat, path in docx_files.items():
    print('======================================================================')
    print(f'CATEGORY: {cat}')
    print('======================================================================')
    doc = docx.Document(path)
    
    # Let's inspect all paragraphs and find each article header & link
    art_count = 0
    for p in doc.paragraphs:
        t = p.text.strip()
        if not t: continue
        if any(t.startswith(f'{i}.') or t.startswith(f'Bài {i}') for i in range(1, 20)) or 'link bài' in t.lower() or 'link gốc' in t.lower() or 'https://' in t:
            if len(t) < 250:
                print(f'  [Doc Line] {t}')
