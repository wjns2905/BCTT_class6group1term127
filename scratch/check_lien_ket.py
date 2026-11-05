import os, sys, zipfile
from xml.etree import ElementTree as ET
sys.stdout.reconfigure(encoding='utf-8')

tn_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\Tài nguyên'

# Read [BCTT] Liên kết.docx
for f in os.listdir(tn_dir):
    if 'kết' in f.lower() or 'lien' in f.lower():
        p = os.path.join(tn_dir, f)
        print("Reading:", f)
        with zipfile.ZipFile(p) as z:
            xml = z.read('word/document.xml')
            tree = ET.fromstring(xml)
            for node in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                if node.text:
                    print(node.text, end=' ')
            print("\n" + "="*50)
