# -*- coding: utf-8 -*-
import sys, os, zipfile
from xml.etree import ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

docx_path = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\Tài nguyên\[BCTT] Update giao diện.docx'

with zipfile.ZipFile(docx_path, 'r') as z:
    rels_map = {}
    if 'word/_rels/document.xml.rels' in z.namelist():
        rels_xml = z.read('word/_rels/document.xml.rels')
        rels_tree = ET.fromstring(rels_xml)
        for rel in rels_tree:
            r_id = rel.attrib.get('Id')
            target = rel.attrib.get('Target')
            rels_map[r_id] = target

    xml_content = z.read('word/document.xml')
    tree = ET.fromstring(xml_content)
    namespaces = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
        'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
        'blip': 'http://schemas.openxmlformats.org/drawingml/2006/main'
    }

    tables = tree.findall('.//w:tbl', namespaces)
    print(f"Total tables: {len(tables)}")
    
    for t_idx, tbl in enumerate(tables):
        rows = tbl.findall('.//w:tr', namespaces)
        print(f"\n=================== TABLE {t_idx+1} ({len(rows)} rows) ===================")
        for r_idx, row in enumerate(rows):
            cells = row.findall('.//w:tc', namespaces)
            cell_texts = []
            cell_images = []
            for c_idx, cell in enumerate(cells):
                # text
                p_list = cell.findall('.//w:p', namespaces)
                c_text = []
                for p in p_list:
                    t_list = p.findall('.//w:t', namespaces)
                    txt = "".join([t.text for t in t_list if t.text]).strip()
                    if txt:
                        c_text.append(txt)
                cell_texts.append(" \n ".join(c_text))
                
                # images
                drawings = cell.findall('.//w:drawing', namespaces)
                imgs = []
                for d in drawings:
                    blips = d.findall('.//a:blip', namespaces)
                    for b in blips:
                        embed_id = b.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                        if embed_id and embed_id in rels_map:
                            imgs.append(rels_map[embed_id])
                cell_images.append(imgs)
            
            print(f"\n--- ROW {r_idx+1} ---")
            for c_idx in range(len(cells)):
                txt = cell_texts[c_idx] if c_idx < len(cell_texts) else ""
                img = cell_images[c_idx] if c_idx < len(cell_images) else []
                print(f"  Col {c_idx+1} Text: {txt[:200]}")
                if img:
                    print(f"  Col {c_idx+1} Imgs: {img}")
