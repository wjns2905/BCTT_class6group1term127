import sys, docx, os, re
sys.stdout.reconfigure(encoding='utf-8')

docx_files = {
    'Trending': 'Tài nguyên/[BCTT] Trending.docx',
    'Society': 'Tài nguyên/[BCTT] Society.docx',
    'Human stories': 'Tài nguyên/[BCTT] Human stories.docx',
    'Mind & Soul': 'Tài nguyên/[BCTT] Mind & Soul.docx',
    'In-dept': 'Tài nguyên/[BCTT] In-dept.docx'
}

for cat, path in docx_files.items():
    print('****************************************************************')
    print(f'*** DOCX: {cat}')
    print('****************************************************************')
    doc = docx.Document(path)
    
    # Split paragraphs by numbered items (e.g. 1. , 2. , 3. )
    current_art_title = None
    current_paras = []
    
    for p in doc.paragraphs:
        t = p.text.strip()
        if not t: continue
        
        # Check if start of article
        m = re.match(r'^(\d+)\.\s*(.*)', t)
        if m and len(m.group(2)) > 5:
            if current_art_title:
                print(f"ARTICLE: {current_art_title}")
                print(f"  First paragraph: {current_paras[0][:120] if current_paras else 'EMPTY'}")
                print(f"  Paragraph count: {len(current_paras)}\n")
            current_art_title = t[:120]
            current_paras = []
        else:
            current_paras.append(t)
            
    if current_art_title:
        print(f"ARTICLE: {current_art_title}")
        print(f"  First paragraph: {current_paras[0][:120] if current_paras else 'EMPTY'}")
        print(f"  Paragraph count: {len(current_paras)}\n")
