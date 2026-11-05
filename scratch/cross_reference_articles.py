import sys, os, docx, json, re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load data.js
with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()
m = re.search(r'const ARTICLES_DATA = (\[.*?\]);', text, re.DOTALL)
articles_data = json.loads(m.group(1))
print(f"Loaded {len(articles_data)} articles from js/data.js")

# 2. Load docx articles
docx_map = {
    'Trending': 'Tài nguyên/[BCTT] Trending.docx',
    'Society': 'Tài nguyên/[BCTT] Society.docx',
    'Human stories': 'Tài nguyên/[BCTT] Human stories.docx',
    'Mind & Soul': 'Tài nguyên/[BCTT] Mind & Soul.docx',
    'In-dept': 'Tài nguyên/[BCTT] In-dept.docx'
}

for cat_name, fpath in docx_map.items():
    doc = docx.Document(fpath)
    print(f"\n==================== {cat_name} DOCX ====================")
    
    # Extract articles
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
                for c in r.cells:
                    imgs = c._element.xpath('.//a:blip')
                    r_ids = [im.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed') for im in imgs]
                    txt = c.text.strip()
                    if txt or r_ids:
                        tbl_data.append((txt, r_ids))
            elements.append(('tbl', tbl_data, []))
            
    # Partition into articles
    doc_arts = []
    curr = None
    for item in elements:
        if item[0] == 'p':
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
                if curr: doc_arts.append(curr)
                curr = {'num': m.group(1), 'header': t, 'items': []}
            elif curr:
                curr['items'].append(item)
        elif item[0] == 'tbl' and curr:
            curr['items'].append(item)
    if curr: doc_arts.append(curr)
    
    print(f"Total articles in docx: {len(doc_arts)}")
    
    for da in doc_arts:
        header = da['header']
        # Find match in articles_data
        matched = []
        for a in articles_data:
            # check link
            sourceUrl = a.get('sourceUrl', '')
            link_m = re.search(r'https?://[^\s]+', header)
            if link_m and sourceUrl and link_m.group(0).rstrip('/') == sourceUrl.rstrip('/'):
                matched.append(a)
                continue
            # check title similarity
            title_en = a.get('title_en', '').lower()
            title_vi = a.get('title', '').lower()
            for it in da['items']:
                if it[0] == 'p' and it[1]:
                    txt = it[1].lower()
                    if (len(txt) > 20 and (txt in title_en or title_en in txt or txt in title_vi or title_vi in txt)):
                        if a not in matched:
                            matched.append(a)
                            break
        
        match_str = ", ".join(m.get('id') for m in matched) if matched else "NO MATCH"
        p_count = sum(1 for it in da['items'] if it[0] == 'p' and it[1])
        img_count = sum(len(it[2]) for it in da['items'] if it[0] == 'p')
        tbl_img_count = sum(sum(len(c[1]) for c in it[1]) for it in da['items'] if it[0] == 'tbl')
        total_imgs = img_count + tbl_img_count
        print(f"  Doc Art #{da['num']:2} -> Matched: {match_str:25} | {p_count:2} paras | {total_imgs:2} imgs | Header: {header[:50]}")

