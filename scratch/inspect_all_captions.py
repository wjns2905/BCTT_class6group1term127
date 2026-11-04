import docx
import zipfile
import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

ROOT = r"c:\Users\camka\OneDrive\Desktop\BCTT\Tài nguyên"

def inspect_all_media_captions(fn):
    docx_path = os.path.join(ROOT, fn)
    print(f"\n==========================================")
    print(f"ANALYZING: {fn}")
    print(f"==========================================")
    
    with zipfile.ZipFile(docx_path, 'r') as z:
        rels = z.read('word/_rels/document.xml.rels').decode('utf-8')
        rid_map = {}
        for m in re.finditer(r'Id="(rId\d+)"[^>]*Target="([^"]+)"', rels):
            if 'media/' in m.group(2):
                rid_map[m.group(1)] = m.group(2).split('/')[-1]

    doc = docx.Document(docx_path)
    
    # Check paragraphs
    for i, p in enumerate(doc.paragraphs):
        xml = p._p.xml
        rids = re.findall(r'rId\d+', xml)
        imgs = [rid_map[r] for r in rids if r in rid_map]
        if imgs:
            # Find neighboring text
            prev_t = doc.paragraphs[i-1].text.strip() if i > 0 else ""
            curr_t = p.text.strip()
            next_t = doc.paragraphs[i+1].text.strip() if i+1 < len(doc.paragraphs) else ""
            print(f"P{i} Imgs: {imgs}")
            if prev_t: print(f"   Prev: {prev_t[:80]}")
            if curr_t: print(f"   Curr: {curr_t[:80]}")
            if next_t: print(f"   Next: {next_t[:80]}")
            
    # Check tables
    for i, t in enumerate(doc.tables):
        for r in t.rows:
            for c in r.cells:
                xml = c._tc.xml
                rids = re.findall(r'rId\d+', xml)
                imgs = [rid_map[r] for r in rids if r in rid_map]
                if imgs:
                    print(f"Table {i} Imgs: {imgs} -> Text: '{c.text.strip()[:80]}'")

for f in ['[BCTT] Trending.docx', '[BCTT] Society.docx', '[BCTT] Human stories.docx', '[BCTT] Mind & Soul.docx', '[BCTT] In-dept.docx']:
    inspect_all_media_captions(f)
