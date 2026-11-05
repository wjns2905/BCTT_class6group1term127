import sys, docx, os, re

sys.stdout.reconfigure(encoding='utf-8')

docx_files = {
    'Trending': 'Tài nguyên/[BCTT] Trending.docx',
    'Society': 'Tài nguyên/[BCTT] Society.docx',
    'Human stories': 'Tài nguyên/[BCTT] Human stories.docx',
    'Mind & Soul': 'Tài nguyên/[BCTT] Mind & Soul.docx',
    'In-dept': 'Tài nguyên/[BCTT] In-dept.docx'
}

for cat, fpath in docx_files.items():
    doc = docx.Document(fpath)
    articles = []
    curr = None
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        m = re.match(r'^(\d+)\.\s*(.*)', t)
        # Check if line indicates start of an article:
        # e.g., "1. Link gốc ...", "2. https://...", "1. Bài gốc...", or "1. Title"
        if m and (int(m.group(1)) <= 25) and (
            'http' in t or 'link' in t.lower() or 'bài' in t.lower() or 
            (curr is None and m.group(1) == '1') or
            (curr and int(m.group(1)) == int(curr['num']) + 1)
        ):
            if curr: articles.append(curr)
            curr = {
                'num': m.group(1),
                'start_p': i,
                'header': t,
                'paragraphs': [],
                'images': [],
                'captions': []
            }
        elif curr:
            curr['paragraphs'].append(t)
            imgs = p._element.xpath('.//a:blip')
            if imgs:
                for img in imgs:
                    r_id = img.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                    curr['images'].append((len(curr['paragraphs'])-1, r_id))
            if 'photo:' in t.lower() or '(photo' in t.lower() or 'ảnh:' in t.lower() or '(ảnh' in t.lower():
                curr['captions'].append((len(curr['paragraphs'])-1, t))
                
    if curr: articles.append(curr)
    
    print('=' * 75)
    print(f'CATEGORY: {cat} (Total detected: {len(articles)})')
    print('=' * 75)
    for a in articles:
        img_info = f"{len(a['images'])} imgs"
        cap_info = f"{len(a['captions'])} caps"
        print(f"  Art #{a['num']:2} (p#{a['start_p']:3}): {img_info:8} | {cap_info:8} | {a['header'][:65]}")

