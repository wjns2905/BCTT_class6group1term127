import os, sys, zipfile
from xml.etree import ElementTree as ET
sys.stdout.reconfigure(encoding='utf-8')

tn_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\Tài nguyên'

def dump_docx(filename):
    p = os.path.join(tn_dir, filename)
    print(f"=== {filename} ===")
    try:
        with zipfile.ZipFile(p) as z:
            xml = z.read('word/document.xml')
            tree = ET.fromstring(xml)
            paras = []
            for p_node in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                text = ''.join(n.text for n in p_node.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if n.text)
                if text.strip():
                    paras.append(text.strip())
            print('\n'.join(paras))
            
            # also rels for hyperlinks
            try:
                rels_xml = z.read('word/_rels/document.xml.rels')
                rels_tree = ET.fromstring(rels_xml)
                print("\n--- HYPERLINKS ---")
                for rel in rels_tree.iter('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
                    if 'hyperlink' in rel.attrib.get('Type', ''):
                        print(rel.attrib.get('Id'), rel.attrib.get('Target'))
            except Exception as e:
                pass
    except Exception as e:
        print("Error:", e)
    print("\n" + "="*60 + "\n")

for f in os.listdir(tn_dir):
    if f.endswith('.docx') and any(k in f.lower() for k in ['kết', 'kết', 'note', 'update']):
        dump_docx(f)
