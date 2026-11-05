import sys, os, docx, json, re
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

# Function to parse a docx file into structured articles with text and images
def parse_docx_articles(fpath, cat_name, folder_name):
    doc = docx.Document(fpath)
    
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
            img_names = [rels.get(im.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')) for im in imgs]
            img_names = [x for x in img_names if x]
            items.append(('p', t, img_names))
        elif tag == 'tbl':
            t = docx.table.Table(el, doc)
            # Check if this table is an image card or a data table
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

    # Split into articles
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
                    is_start = True # Article 5 part 1
                elif curr and m.group(1) == '5' and 'volunteer farmers' in rest:
                    is_start = True # Article 5 part 2
                elif curr and m.group(1) == '8' and 'stable electricity' in rest:
                    is_start = True # Article 8 part 2
            if is_start:
                if curr: articles.append(curr)
                curr = {'num': m.group(1), 'header': t, 'flow': [], 'cat': cat_name, 'folder': folder_name}
            elif curr:
                curr['flow'].append(item)
        elif curr:
            curr['flow'].append(item)
    if curr: articles.append(curr)
    return articles

# Test parsing all 5 docx files
all_parsed = []
for name, cat, folder in [
    ('[BCTT] Trending.docx', 'trending', 'trending'),
    ('[BCTT] Society.docx', 'society', 'society'),
    ('[BCTT] Human stories.docx', 'human-stories', 'human_stories'),
    ('[BCTT] Mind & Soul.docx', 'mind-soul', 'mind_&_soul'),
    ('[BCTT] In-dept.docx', 'in-depth', 'in-dept')
]:
    arts = parse_docx_articles('Tài nguyên/' + name, cat, folder)
    print(f"Parsed {len(arts)} articles from {name}")
    all_parsed.extend(arts)

print(f"\nTotal parsed articles across 5 docx files: {len(all_parsed)}")
