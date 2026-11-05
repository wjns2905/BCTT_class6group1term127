import sys, os, docx, re, json

sys.stdout.reconfigure(encoding='utf-8')

docx_files = {
    'trending': 'Tài nguyên/[BCTT] Trending.docx',
    'society': 'Tài nguyên/[BCTT] Society.docx',
    'human-stories': 'Tài nguyên/[BCTT] Human stories.docx',
    'mind-soul': 'Tài nguyên/[BCTT] Mind & Soul.docx',
    'in-depth': 'Tài nguyên/[BCTT] In-dept.docx'
}

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()
m = re.search(r'const ARTICLES_DATA = (\[.*?\]);', text, re.DOTALL)
articles_data = json.loads(m.group(1))
articles_by_id = {a['id']: a for a in articles_data}

print(f"Loaded {len(articles_data)} articles from data.js")

# Let's inspect each DOCX and print out each article's details
for cat_key, fpath in docx_files.items():
    doc = docx.Document(fpath)
    print(f"\n==================== {cat_key.upper()} ====================")
    
    # Map rel_id to media file
    rels = {}
    for r_id, rel in doc.part.rels.items():
        if "image" in rel.target_ref:
            rels[r_id] = os.path.basename(rel.target_ref)
            
    # Iterate through elements
    items = []
    for el in doc.element.body:
        tag = el.tag.split('}')[-1]
        if tag == 'p':
            p = docx.text.paragraph.Paragraph(el, doc)
            t = p.text.strip()
            imgs = el.xpath('.//a:blip')
            img_files = [rels.get(im.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')) for im in imgs]
            img_files = [x for x in img_files if x]
            items.append(('p', t, img_files))
        elif tag == 'tbl':
            t = docx.table.Table(el, doc)
            # check if it's image table or data table
            for r in t.rows:
                cell_imgs = []
                cell_texts = []
                for c in r.cells:
                    imgs = c._element.xpath('.//a:blip')
                    img_files = [rels.get(im.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')) for im in imgs]
                    cell_imgs.extend([x for x in img_files if x])
                    txt = c.text.strip()
                    if txt: cell_texts.append(txt)
                if cell_imgs or cell_texts:
                    items.append(('tbl_row', " | ".join(cell_texts), cell_imgs))

    # Split into articles
    doc_arts = []
    curr = None
    for it in items:
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
    
    print(f"Total articles in docx: {len(doc_arts)}")
    for da in doc_arts:
        imgs = [it[2] for it in da['flow'] if it[2]]
        flat_imgs = [img for sub in imgs for img in sub]
        print(f"  Art #{da['num']}: {len(da['flow'])} flow items, {len(flat_imgs)} images: {flat_imgs[:5]} | Header: {da['header'][:60]}")
