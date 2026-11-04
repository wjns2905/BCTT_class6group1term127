# -*- coding: utf-8 -*-
import sys, os, zipfile
from xml.etree import ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

docx_path = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\Tài nguyên\[BCTT] Update giao diện.docx'
out_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT\scratch\update_docx_media'
os.makedirs(out_dir, exist_ok=True)

with zipfile.ZipFile(docx_path, 'r') as z:
    for f in z.namelist():
        if f.startswith('word/media/'):
            basename = os.path.basename(f)
            data = z.read(f)
            out_path = os.path.join(out_dir, basename)
            with open(out_path, 'wb') as img_out:
                img_out.write(data)
            print(f"Extracted {basename} ({len(data)} bytes)")

    # Read relationships
    rels_map = {}
    if 'word/_rels/document.xml.rels' in z.namelist():
        rels_xml = z.read('word/_rels/document.xml.rels')
        rels_tree = ET.fromstring(rels_xml)
        for rel in rels_tree:
            r_id = rel.attrib.get('Id')
            target = rel.attrib.get('Target')
            rels_map[r_id] = target

    # Read document.xml sequentially
    xml_content = z.read('word/document.xml')
    tree = ET.fromstring(xml_content)
    namespaces = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
        'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
        'blip': 'http://schemas.openxmlformats.org/drawingml/2006/main'
    }

    paragraphs = tree.findall('.//w:p', namespaces)
    print(f"\nSequential Walkthrough ({len(paragraphs)} paragraphs):")
    for i, p in enumerate(paragraphs):
        texts = p.findall('.//w:t', namespaces)
        p_text = "".join([t.text for t in texts if t.text]).strip()
        
        # Check drawings / images
        drawings = p.findall('.//w:drawing', namespaces)
        img_info = []
        for d in drawings:
            blips = d.findall('.//a:blip', namespaces)
            for b in blips:
                embed_id = b.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                if embed_id and embed_id in rels_map:
                    img_info.append(rels_map[embed_id])

        if p_text or img_info:
            print(f"\n--- [P{i+1}] ---")
            if p_text:
                print(f"TEXT: {p_text}")
            if img_info:
                print(f"IMAGES: {img_info}")
