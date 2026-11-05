import sys, os, docx, re

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
    print(f"\n{'='*30} {cat} {'='*30}")
    
    # Map r_id to image part
    rels = {}
    for r_id, rel in doc.part.rels.items():
        if "image" in rel.target_ref:
            rels[r_id] = rel.target_ref
            
    # Traverse body elements (paragraphs and tables in order)
    elements = []
    for el in doc.element.body:
        tag = el.tag.split('}')[-1]
        if tag == 'p':
            p = docx.text.paragraph.Paragraph(el, doc)
            t = p.text.strip()
            imgs = el.xpath('.//a:blip')
            r_ids = [im.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed') for im in imgs]
            elements.append(('p', t, r_ids))
        elif tag == 'tbl':
            t = docx.table.Table(el, doc)
            tbl_data = []
            for r in t.rows:
                row_cells = []
                for c in r.cells:
                    imgs = c._element.xpath('.//a:blip')
                    r_ids = [im.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed') for im in imgs]
                    row_cells.append((c.text.strip(), r_ids))
                tbl_data.append(row_cells)
            elements.append(('tbl', tbl_data, []))

    # Now let's split into articles
    # Each article usually starts with a paragraph containing a number like "1.", "2.", "3." with a link or title
    articles = []
    curr_art = None
    
    for idx, item in enumerate(elements):
        itype = item[0]
        if itype == 'p':
            t = item[1]
            r_ids = item[2]
            # Detect article header
            m = re.match(r'^(\d+)\.\s*(.*)', t)
            # check if it's an article starter
            is_start = False
            if m and int(m.group(1)) <= 30:
                rest = m.group(2).lower()
                if ('http' in t) or ('link' in rest) or ('bài' in rest) or (curr_art is None and m.group(1) == '1'):
                    is_start = True
                elif curr_art and int(m.group(1)) == int(curr_art['num']) + 1:
                    is_start = True
                elif curr_art and int(m.group(1)) == int(curr_art['num']): # duplicate number
                    is_start = False
            
            if is_start:
                if curr_art:
                    articles.append(curr_art)
                curr_art = {
                    'num': m.group(1),
                    'header': t,
                    'items': [],
                    'title': '',
                    'link': ''
                }
                # extract link if in header
                link_m = re.search(r'https?://[^\s]+', t)
                if link_m:
                    curr_art['link'] = link_m.group(0)
            elif curr_art:
                curr_art['items'].append(('p', t, r_ids))
        elif itype == 'tbl' and curr_art:
            curr_art['items'].append(('tbl', item[1], []))
            
    if curr_art:
        articles.append(curr_art)
        
    print(f"Total articles detected in {cat}: {len(articles)}")
    for a in articles:
        img_count = sum(len(it[2]) for it in a['items'] if it[0] == 'p')
        tbl_img_count = sum(sum(len(c[1]) for c in row) for it in a['items'] if it[0] == 'tbl' for row in it[1])
        total_imgs = img_count + tbl_img_count
        # find title
        title_candidates = [it[1] for it in a['items'] if it[0] == 'p' and it[1] and len(it[1]) < 180 and not it[1].startswith('http') and not it[1].startswith('By ') and not it[1].startswith('Photo')]
        title = title_candidates[0] if title_candidates else ''
        print(f"  Art #{a['num']:2}: {total_imgs} images | Link: {a['link'][:45]} | Title: {title[:50]}")

