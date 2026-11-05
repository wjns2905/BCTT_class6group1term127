import os, sys, zipfile
from xml.etree import ElementTree as ET
sys.stdout.reconfigure(encoding='utf-8')

docx_path = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\Tài nguyên\[BCTT] Video.docx'
with zipfile.ZipFile(docx_path) as z:
    xml_content = z.read('word/document.xml')
    tree = ET.fromstring(xml_content)
    text = []
    for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
        p_text = ''.join(node.text for node in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text)
        if p_text.strip():
            text.append(p_text.strip())
    print('\n'.join(text))

    # Also check hyperlinks
    try:
        rels_xml = z.read('word/_rels/document.xml.rels')
        rels_tree = ET.fromstring(rels_xml)
        print("\n--- HYPERLINKS ---")
        for rel in rels_tree.iter('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
            if 'hyperlink' in rel.attrib.get('Type', ''):
                print(rel.attrib.get('Id'), rel.attrib.get('Target'))
    except Exception as e:
        print("Error reading rels:", e)
