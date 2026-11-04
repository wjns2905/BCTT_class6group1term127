import zipfile
import xml.etree.ElementTree as ET
import sys

sys.stdout.reconfigure(encoding='utf-8')

docx_path = r"c:\Users\camka\OneDrive\Desktop\BCTT\Tài nguyên\[BCTT] Trending.docx"

with zipfile.ZipFile(docx_path, 'r') as z:
    rels_xml = z.read('word/_rels/document.xml.rels')
    rels_tree = ET.fromstring(rels_xml)
    rid_map = {}
    for rel in rels_tree:
        rid = rel.attrib.get('Id')
        target = rel.attrib.get('Target')
        if target and 'media/' in target:
            rid_map[rid] = os.path.basename(target) if 'os' in globals() else target.split('/')[-1]
            
    doc_xml = z.read('word/document.xml')
    doc_tree = ET.fromstring(doc_xml)
    
    ns = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    }
    
    body = doc_tree.find('w:body', ns)
    for p in body.findall('w:p', ns):
        texts = [t.text for t in p.findall('.//w:t', ns) if t.text]
        p_text = "".join(texts).strip()
        for blip in p.findall('.//a:blip', ns):
            embed_id = blip.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
            if embed_id and embed_id in rid_map:
                print(f"{rid_map[embed_id]}: text='{p_text[:80]}'")
