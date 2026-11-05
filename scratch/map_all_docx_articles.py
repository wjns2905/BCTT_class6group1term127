import sys, os, docx, json, re

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()
articles_data = json.loads(re.search(r'const ARTICLES_DATA = (\[.*?\]);', text, re.DOTALL).group(1))

docx_files = {
    'trending': 'Tài nguyên/[BCTT] Trending.docx',
    'society': 'Tài nguyên/[BCTT] Society.docx',
    'human-stories': 'Tài nguyên/[BCTT] Human stories.docx',
    'mind-soul': 'Tài nguyên/[BCTT] Mind & Soul.docx',
    'in-depth': 'Tài nguyên/[BCTT] In-dept.docx'
}

for cat_key, fpath in docx_files.items():
    doc = docx.Document(fpath)
    print(f"\n==================== {cat_key} ====================")
    
    # Extract linear paragraphs and tables
    elements = []
    for el in doc.element.body:
        tag = el.tag.split('}')[-1]
        if tag == 'p':
            p = docx.text.paragraph.Paragraph(el, doc)
            t = p.text.strip()
            imgs = el.xpath('.//a:blip')
            elements.append(('p', t, len(imgs)))
        elif tag == 'tbl':
            t = docx.table.Table(el, doc)
            cell_texts = []
            img_count = 0
            for r in t.rows:
                for c in r.cells:
                    imgs = c._element.xpath('.//a:blip')
                    img_count += len(imgs)
                    if c.text.strip(): cell_texts.append(c.text.strip())
            elements.append(('tbl', " | ".join(cell_texts), img_count))

    # Split into articles
    doc_arts = []
    curr = None
    for it in elements:
        t = it[1]
        m = re.match(r'^(\d+)\.\s*(.*)', t)
        is_start = False
        if m and int(m.group(1)) <= 30:
            rest = m.group(2).lower()
            if ('http' in t) or ('link' in rest) or ('bài' in rest) or (curr is None and m.group(1) == '1'):
                is_start = True
            elif curr and int(m.group(1)) == int(curr['num']) + 1:
                is_start = True
        if is_start:
            if curr: doc_arts.append(curr)
            curr = {'num': m.group(1), 'header': t, 'flow': []}
        elif curr:
            curr['flow'].append(it)
    if curr: doc_arts.append(curr)
    
    for da in doc_arts:
        # Find candidate title in flow
        cand_titles = [it[1] for it in da['flow'] if it[0] == 'p' and it[1] and len(it[1]) < 180 and not it[1].startswith('http') and not it[1].startswith('By ') and not it[1].startswith('Photo') and not it[1].startswith('Saturday') and not it[1].startswith('Mon ') and not it[1].startswith('Get VnExpress')]
        title = cand_titles[0] if cand_titles else da['header']
        
        # Link in header or flow
        link = ''
        m_link = re.search(r'https?://[^\s]+', da['header'])
        if m_link: link = m_link.group(0)
        else:
            for it in da['flow']:
                m_l = re.search(r'https?://[^\s]+', it[1])
                if m_l:
                    link = m_l.group(0)
                    break
                    
        # Match with articles_data
        matches = []
        for a in articles_data:
            s_url = a.get('sourceUrl', '')
            if link and s_url and (link.rstrip('/') in s_url or s_url.rstrip('/') in link):
                matches.append(a['id'])
            elif title.lower()[:30] in a.get('title_en', '').lower() or title.lower()[:30] in a.get('title', '').lower():
                if a['id'] not in matches:
                    matches.append(a['id'])
                    
        print(f"Doc Art #{da['num']:2} -> {matches} | Title: {title[:55]} | Link: {link[:50]}")

