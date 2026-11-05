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
    print(f"\n==================== {cat} ====================")
    
    # Map rel_id to media file
    rels = {}
    for r_id, rel in doc.part.rels.items():
        if "image" in rel.target_ref:
            rels[r_id] = os.path.basename(rel.target_ref)
            
    # Iterate through body
    body_items = []
    for el in doc.element.body:
        tag = el.tag.split('}')[-1]
        if tag == 'p':
            p = docx.text.paragraph.Paragraph(el, doc)
            t = p.text.strip()
            imgs = el.xpath('.//a:blip')
            img_files = [rels.get(im.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')) for im in imgs]
            img_files = [x for x in img_files if x]
            body_items.append(('p', t, img_files))
        elif tag == 'tbl':
            t = docx.table.Table(el, doc)
            for r in t.rows:
                for c in r.cells:
                    imgs = c._element.xpath('.//a:blip')
                    img_files = [rels.get(im.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')) for im in imgs]
                    img_files = [x for x in img_files if x]
                    txt = c.text.strip()
                    if txt or img_files:
                        body_items.append(('tbl_cell', txt, img_files))
                        
    # Detect articles
    arts = []
    curr = None
    for item in body_items:
        t = item[1]
        m = re.match(r'^(\d+)\.\s*(.*)', t)
        is_start = False
        if m and int(m.group(1)) <= 30:
            rest = m.group(2).lower()
            if ('http' in t) or ('link' in rest) or ('bài' in rest) or (curr is None and m.group(1) == '1'):
                is_start = True
            elif curr and int(m.group(1)) == int(curr['num']) + 1:
                is_start = True
        
        if is_start:
            if curr: arts.append(curr)
            curr = {'num': m.group(1), 'header': t, 'flow': []}
        elif curr:
            curr['flow'].append(item)
    if curr: arts.append(curr)
    
    print(f"Total articles parsed: {len(arts)}")
    for a in arts:
        imgs = [it[2] for it in a['flow'] if it[2]]
        print(f"  Art #{a['num']}: {len(a['flow'])} flow items, {len(imgs)} image slots")
        for idx, it in enumerate(a['flow']):
            if it[2]: # has image
                print(f"    Slot {idx}: IMAGE {it[2]} | Text: {it[1][:60]}")
