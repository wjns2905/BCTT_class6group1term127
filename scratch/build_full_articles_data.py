import sys, os, docx, json, re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load existing ARTICLES_DATA
data_path = 'js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const ARTICLES_DATA = (\[.*?\]);', text, re.DOTALL)
if not m:
    print("Could not find ARTICLES_DATA in js/data.js")
    sys.exit(1)

articles_data = json.loads(m.group(1))
articles_by_id = {a['id']: a for a in articles_data}
print(f"Loaded {len(articles_data)} existing articles from js/data.js")

# 2. Docx parser
def parse_docx(fpath):
    doc = docx.Document(fpath)
    rels = {}
    for r_id, rel in doc.part.rels.items():
        if "image" in rel.target_ref:
            rels[r_id] = os.path.basename(rel.target_ref)
            
    items = []
    for el in doc.element.body:
        tag = el.tag.split('}')[-1]
        if tag == 'p':
            p = docx.text.paragraph.Paragraph(el, doc)
            t = p.text.strip()
            imgs = el.xpath('.//a:blip')
            img_names = [rels.get(im.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')) for im in imgs]
            img_names = [x for x in img_names if x]
            items.append(('p', t, img_names))
        elif tag == 'tbl':
            t = docx.table.Table(el, doc)
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
            items.append(('tbl', tbl_rows, []))
    return items

def split_into_articles(items, cat_folder):
    articles = []
    curr = None
    for item in items:
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
                elif curr and m.group(1) == '5' and 'accelerate' in rest:
                    is_start = True
                elif curr and m.group(1) == '5' and 'volunteer farmers' in rest:
                    is_start = True
                elif curr and m.group(1) == '8' and 'stable electricity' in rest:
                    is_start = True
            if is_start:
                if curr: articles.append(curr)
                curr = {'num': m.group(1), 'header': t, 'flow': [], 'folder': cat_folder}
            elif curr:
                curr['flow'].append(item)
        elif curr:
            curr['flow'].append(item)
    if curr: articles.append(curr)
    return articles

def flow_to_content(flow, folder_name):
    content = []
    i = 0
    while i < len(flow):
        item = flow[i]
        itype = item[0]
        
        if itype == 'p':
            txt = item[1]
            imgs = item[2]
            
            if imgs:
                valid_imgs = []
                for img in imgs:
                    img_path = os.path.join('assets/images', folder_name, img)
                    if os.path.exists(img_path) and os.path.getsize(img_path) > 2000:
                        valid_imgs.append((img, img_path))
                
                caption = txt
                if not caption and i + 1 < len(flow) and flow[i+1][0] == 'p' and not flow[i+1][2]:
                    next_txt = flow[i+1][1]
                    if any(k in next_txt.lower() for k in ['photo', 'ảnh', 'by ', 'huyền chi', 'thùy trang', 'nguồn', 'minh nga', 'ndo']):
                        caption = next_txt
                        i += 1
                    elif len(next_txt) < 180 and not next_txt.endswith('.'):
                        caption = next_txt
                        i += 1
                        
                for img, img_path in valid_imgs:
                    cap_clean = caption.replace('"', '&quot;')
                    fig_html = f'''<figure class="article-body-figure" style="margin:2rem 0; text-align:center;">
  <img src="assets/images/{folder_name}/{img}" alt="{cap_clean or 'Article photo'}" style="max-width:100%; height:auto; border-radius:8px; box-shadow:0 4px 16px rgba(0,0,0,0.06); display:block; margin:0 auto;">
  {f'<figcaption class="article-body-figcaption" style="font-family:var(--font-sans); font-size:0.875rem; color:var(--color-text-muted); margin-top:0.6rem; font-style:italic; line-height:1.5; text-align:center;">{caption}</figcaption>' if caption else ''}
</figure>'''
                    content.append(fig_html)
                    
            elif txt:
                # Check if metadata or regular paragraph
                if re.match(r'^(monday|tuesday|wednesday|thursday|friday|saturday|sunday|mon|tue|wed|thu|fri|sat|sun),', txt, re.I):
                    pass
                elif any(txt.lower().startswith(x) for x in ['by ', 'get vnexpress', 'link bài', 'link gốc', 'bài gốc']):
                    pass
                elif any(txt.lower().startswith(x) for x in ['photo:', '(photo', 'ảnh:']):
                    pass
                elif len(txt) < 85 and not txt.endswith('.') and not txt.endswith('!') and not txt.endswith('?') and not txt.endswith('”') and not txt.endswith('"'):
                    content.append(f"### {txt}")
                else:
                    content.append(txt)
                    
        elif itype == 'tbl':
            tbl_rows = item[1]
            has_table_imgs = any(any(c[1] for c in r) for r in tbl_rows)
            if has_table_imgs:
                if len(tbl_rows) >= 2:
                    imgs = [c[1] for c in tbl_rows[0] if c[1]]
                    caps = [c[0] for c in tbl_rows[1] if c[0]]
                    flat_imgs = [im for sub in imgs for im in sub]
                    for idx, img in enumerate(flat_imgs):
                        img_path = os.path.join('assets/images', folder_name, img)
                        if os.path.exists(img_path) and os.path.getsize(img_path) > 2000:
                            cap = caps[idx] if idx < len(caps) else ''
                            cap_clean = cap.replace('"', '&quot;')
                            fig_html = f'''<figure class="article-body-figure" style="margin:2rem 0; text-align:center;">
  <img src="assets/images/{folder_name}/{img}" alt="{cap_clean or 'Photo'}" style="max-width:100%; height:auto; border-radius:8px; box-shadow:0 4px 16px rgba(0,0,0,0.06); display:block; margin:0 auto;">
  {f'<figcaption class="article-body-figcaption" style="font-family:var(--font-sans); font-size:0.875rem; color:var(--color-text-muted); margin-top:0.6rem; font-style:italic; line-height:1.5; text-align:center;">{cap}</figcaption>' if cap else ''}
</figure>'''
                            content.append(fig_html)
            else:
                table_html = ['<div class="article-table-wrap" style="overflow-x:auto; margin:2rem 0;"><table class="article-data-table" style="width:100%; border-collapse:collapse; font-size:0.9rem;">']
                for ri, r in enumerate(tbl_rows):
                    table_html.append('<tr>')
                    tag = 'th' if ri == 0 or ri == 1 else 'td'
                    for c in r:
                        table_html.append(f'<{tag} style="border:1px solid #E5E5E5; padding:0.6rem 0.8rem; text-align:left;">{c[0]}</{tag}>')
                    table_html.append('</tr>')
                table_html.append('</table></div>')
                content.append("".join(table_html))
                
        i += 1
    return content

print("Docx parser & flow converter initialized.")
