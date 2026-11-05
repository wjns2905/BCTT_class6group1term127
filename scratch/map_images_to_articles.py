import sys, docx, os
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls, qn

sys.stdout.reconfigure(encoding='utf-8')

docx_files = {
    'Trending': 'Tài nguyên/[BCTT] Trending.docx',
    'Society': 'Tài nguyên/[BCTT] Society.docx',
    'Human stories': 'Tài nguyên/[BCTT] Human stories.docx',
    'Mind & Soul': 'Tài nguyên/[BCTT] Mind & Soul.docx',
    'In-dept': 'Tài nguyên/[BCTT] In-dept.docx'
}

for cat, path in docx_files.items():
    print(f'================ {cat} ================')
    doc = docx.Document(path)
    
    # Traverse body elements
    current_title = "START"
    for elem in doc.element.body:
        if elem.tag.endswith('p'):
            text = "".join(elem.itertext()).strip()
            if any(text.startswith(f'{i}.') or text.startswith(f'Bài {i}') for i in range(1, 20)) or 'link bài' in text.lower() or 'link gốc' in text.lower():
                current_title = text[:80]
                print(f'\n--> NEW ARTICLE: {current_title}')
            
            # Check for blip (image) in this paragraph
            blips = elem.findall('.//' + qn('a:blip'))
            if blips:
                for b in blips:
                    rId = b.get(qn('r:embed'))
                    target = doc.part.rels[rId].target_ref if rId in doc.part.rels else 'unknown'
                    print(f'    [IMAGE IN P] under \"{current_title}\": {target}')
                    
        elif elem.tag.endswith('tbl'):
            # Check for blips in table
            blips = elem.findall('.//' + qn('a:blip'))
            if blips:
                for b in blips:
                    rId = b.get(qn('r:embed'))
                    target = doc.part.rels[rId].target_ref if rId in doc.part.rels else 'unknown'
                    print(f'    [IMAGE IN TBL] under \"{current_title}\": {target}')
