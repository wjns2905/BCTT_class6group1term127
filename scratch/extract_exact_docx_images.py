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

# For each docx, let's list every article and the EXACT media file name:
for cat, path in docx_files.items():
    doc = docx.Document(path)
    print(f'=== DOCX: {cat} ===')
    current_art = "Header"
    for elem in doc.element.body:
        if elem.tag.endswith('p'):
            t = "".join(elem.itertext()).strip()
            if any(t.startswith(f'{i}.') or t.startswith(f'Bài {i}') for i in range(1, 25)) or 'link bài' in t.lower() or 'link gốc' in t.lower():
                current_art = t[:60]
            for b in elem.findall('.//' + qn('a:blip')):
                rId = b.get(qn('r:embed'))
                if rId in doc.part.rels:
                    print(f'  Art: [{current_art}] -> {doc.part.rels[rId].target_ref}')
        elif elem.tag.endswith('tbl'):
            for b in elem.findall('.//' + qn('a:blip')):
                rId = b.get(qn('r:embed'))
                if rId in doc.part.rels:
                    print(f'  Art (in table): [{current_art}] -> {doc.part.rels[rId].target_ref}')
