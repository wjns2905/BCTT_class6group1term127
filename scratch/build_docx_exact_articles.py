import sys, os, docx, json, re
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

docx_files = {
    'trending': 'Tài nguyên/[BCTT] Trending.docx',
    'society': 'Tài nguyên/[BCTT] Society.docx',
    'human-stories': 'Tài nguyên/[BCTT] Human stories.docx',
    'mind-soul': 'Tài nguyên/[BCTT] Mind & Soul.docx',
    'in-depth': 'Tài nguyên/[BCTT] In-dept.docx'
}

# Let's inspect media mapping for each docx
for cat_key, fpath in docx_files.items():
    doc = docx.Document(fpath)
    print(f"\n{'='*35} {cat_key.upper()} {'='*35}")
    
    # 1. Map rId to target_ref
    rels = {}
    for r_id, rel in doc.part.rels.items():
        if "image" in rel.target_ref:
            rels[r_id] = os.path.basename(rel.target_ref)
            
    # 2. Extract linear sequence of body elements
    sequence = []
    for el in doc.element.body:
        tag = el.tag.split('}')[-1]
        if tag == 'p':
            p = docx.text.paragraph.Paragraph(el, doc)
            t = p.text.strip()
            imgs = el.xpath('.//a:blip')
            img_names = [rels.get(im.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')) for im in imgs]
            img_names = [x for x in img_names if x]
            sequence.append(('p', t, img_names))
        elif tag == 'tbl':
            t = docx.table.Table(el, doc)
            # check if table is an image card or a data table
            tbl_rows = []
            for r in t.rows:
                r_cells = []
                for c in r.cells:
                    imgs = c._element.xpath('.//a:blip')
                    img_names = [rels.get(im.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')) for im in imgs]
                    img_names = [x for x in img_names if x]
                    txt = c.text.strip()
                    r_cells.append((txt, img_names))
                tbl_rows.append(r_cells)
            sequence.append(('tbl', tbl_rows, []))

    # 3. Partition sequence into articles
    articles = []
    curr = None
    
    for item in sequence:
        itype = item[0]
        if itype == 'p':
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
                if curr: articles.append(curr)
                curr = {'num': m.group(1), 'header': t, 'items': []}
            elif curr:
                curr['items'].append(item)
        elif curr:
            curr['items'].append(item)
            
    if curr: articles.append(curr)
    
    print(f"Total articles in {cat_key}: {len(articles)}")
    for a in articles:
        p_count = sum(1 for it in a['items'] if it[0] == 'p' and it[1])
        imgs = []
        for it in a['items']:
            if it[0] == 'p' and it[2]:
                imgs.extend(it[2])
            elif it[0] == 'tbl':
                for r in it[1]:
                    for c in r:
                        if c[1]: imgs.extend(c[1])
        print(f"  Art #{a['num']}: {p_count} text paras, {len(imgs)} imgs -> {imgs} | Header: {a['header'][:60]}")
