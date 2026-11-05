import os, sys, zipfile
from xml.etree import ElementTree as ET
sys.stdout.reconfigure(encoding='utf-8')

docx_path = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\Tài nguyên\[BCTT] Update giao diện.docx'
with zipfile.ZipFile(docx_path) as z:
    rels_xml = z.read('word/_rels/document.xml.rels')
    rels_tree = ET.fromstring(rels_xml)
    rel_map = {}
    for rel in rels_tree.iter('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
        rel_map[rel.attrib.get('Id')] = rel.attrib.get('Target')
    
    xml = z.read('word/document.xml')
    tree = ET.fromstring(xml)
    for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
        p_text = ''.join(n.text for n in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if n.text).strip()
        imgs = []
        for blip in p.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}blip'):
            embed_id = blip.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
            if embed_id in rel_map:
                imgs.append(rel_map[embed_id])
        if p_text or imgs:
            print(f"Text: {p_text}")
            if imgs:
                print(f"  --> IMAGES: {imgs}")
