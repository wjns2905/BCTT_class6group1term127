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
    
    # Check relationships (media in docx package)
    image_parts = []
    for rel_id, rel in doc.part.rels.items():
        if "image" in rel.target_ref:
            image_parts.append((rel_id, rel.target_ref))
    print(f"Total media files in docx package: {len(image_parts)}")

    # Let's inspect the paragraphs and tables to see where images are and what text is around them
    items = []
    for p in doc.paragraphs:
        t = p.text.strip()
        imgs = p._element.xpath('.//a:blip')
        r_ids = [im.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed') for im in imgs]
        if t or r_ids:
            items.append(('p', t, r_ids))
            
    for t in doc.tables:
        for r in t.rows:
            for c in r.cells:
                imgs = c._element.xpath('.//a:blip')
                r_ids = [im.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed') for im in imgs]
                txt = c.text.strip()
                if txt or r_ids:
                    items.append(('table_cell', txt, r_ids))

    print(f"Total non-empty elements: {len(items)}")
    # Print sample of items
    for idx, (itype, txt, r_ids) in enumerate(items[:15]):
        if r_ids:
            print(f"  [{idx}] {itype.upper()} [IMGS: {r_ids}]: {txt[:70]}")
        else:
            print(f"  [{idx}] {itype.upper()}: {txt[:70]}")
