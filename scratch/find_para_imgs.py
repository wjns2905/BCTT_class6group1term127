import docx
import zipfile
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

docx_path = r"c:\Users\camka\OneDrive\Desktop\BCTT\Tài nguyên\[BCTT] Trending.docx"

with zipfile.ZipFile(docx_path, 'r') as z:
    rels = z.read('word/_rels/document.xml.rels').decode('utf-8')
    rid_to_file = {}
    for m in re.finditer(r'Id="(rId\d+)"[^>]*Target="([^"]+)"', rels):
        if 'media/' in m.group(2):
            rid_to_file[m.group(1)] = m.group(2).split('/')[-1]

doc = docx.Document(docx_path)
print("Paragraphs with image references:")
for i, p in enumerate(doc.paragraphs):
    xml = p._p.xml
    rids = re.findall(r'rId\d+', xml)
    img_files = [rid_to_file[r] for r in rids if r in rid_to_file]
    if img_files:
        print(f"Para {i:3} has {img_files}: text='{p.text[:70]}'")
