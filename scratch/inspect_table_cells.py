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
    row2 = tables[0].findall('.//w:tr', namespaces)[1]
    cell1, cell2 = row2.findall('.//w:tc', namespaces)
    
    print("=== CELL 1 (FEEDBACK ITEMS) ===")
    p1_list = cell1.findall('.//w:p', namespaces)
    item_idx = 1
    for p in p1_list:
        t_list = p.findall('.//w:t', namespaces)
        txt = "".join([t.text for t in t_list if t.text]).strip()
        drawings = p.findall('.//w:drawing', namespaces)
        imgs = []
        for d in drawings:
            blips = d.findall('.//a:blip', namespaces)
            for b in blips:
                embed_id = b.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                if embed_id and embed_id in rels_map:
                    imgs.append(rels_map[embed_id])
        if txt or imgs:
            print(f"\n[Item {item_idx}]")
            if txt:
                print(f"TEXT: {txt}")
            if imgs:
                print(f"IMGS: {imgs}")
            item_idx += 1

    print("\n=== CELL 2 (ILLUSTRATION IMAGES) ===")
    p2_list = cell2.findall('.//w:p', namespaces)
    img_idx = 1
    for p in p2_list:
        drawings = p.findall('.//w:drawing', namespaces)
        imgs = []
        for d in drawings:
            blips = d.findall('.//a:blip', namespaces)
            for b in blips:
                embed_id = b.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                if embed_id and embed_id in rels_map:
                    imgs.append(rels_map[embed_id])
        t_list = p.findall('.//w:t', namespaces)
        txt = "".join([t.text for t in t_list if t.text]).strip()
        if imgs or txt:
            print(f"Img block {img_idx}: txt='{txt}', imgs={imgs}")
            img_idx += 1
