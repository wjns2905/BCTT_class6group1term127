# -*- coding: utf-8 -*-
import sys, os, zipfile
from xml.etree import ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

docx_path = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\Tài nguyên\[BCTT] Update giao diện.docx'

with zipfile.ZipFile(docx_path, 'r') as z:
    file_list = z.namelist()
    print("Files in docx zip:", len(file_list))
    
    # List images
    media_files = [f for f in file_list if f.startswith('word/media/')]
    print(f"Media files ({len(media_files)}):")
    for m in media_files:
        info = z.getinfo(m)
        print(f" - {m} ({info.file_size} bytes)")
        
    # Read document.xml text
    if 'word/document.xml' in file_list:
        xml_content = z.read('word/document.xml')
        tree = ET.fromstring(xml_content)
        
        namespaces = {
            'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
            'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
            'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
            'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'
        }
        
        paragraphs = tree.findall('.//w:p', namespaces)
        print(f"\nTotal paragraphs: {len(paragraphs)}")
        for i, p in enumerate(paragraphs):
            texts = p.findall('.//w:t', namespaces)
            p_text = "".join([t.text for t in texts if t.text])
            if p_text.strip():
                print(f"P{i+1}: {p_text.strip()}")
