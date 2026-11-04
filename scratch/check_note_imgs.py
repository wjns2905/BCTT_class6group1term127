import docx
import zipfile
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

docx_path = r"c:\Users\camka\OneDrive\Desktop\BCTT\Tài nguyên\[BCTT] Note giao diện.docx"

with zipfile.ZipFile(docx_path, 'r') as z:
    rels = z.read('word/_rels/document.xml.rels').decode('utf-8')
    rid_map = {}
    for m in re.finditer(r'Id="(rId\d+)"[^>]*Target="([^"]+)"', rels):
        if 'media/' in m.group(2):
            rid_map[m.group(1)] = m.group(2).split('/')[-1]

doc = docx.Document(docx_path)
for i, p in enumerate(doc.paragraphs):
    xml = p._p.xml
    rids = re.findall(r'rId\d+', xml)
    imgs = [rid_map[r] for r in rids if r in rid_map]
    if imgs or p.text.strip():
        print(f"P{i:2} {imgs}: {p.text.strip()[:80]}")
