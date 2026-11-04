import zipfile
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with zipfile.ZipFile(r'c:\Users\camka\OneDrive\Desktop\BCTT\Tài nguyên\[BCTT] Trending.docx', 'r') as z:
    rels = z.read('word/_rels/document.xml.rels').decode('utf-8')
    doc_xml = z.read('word/document.xml').decode('utf-8')
    
    # find all image references
    rids = re.findall(r'rId\d+', doc_xml)
    print(f'Total rIds mentioned in doc_xml: {len(rids)}')
    for r in sorted(set(rids)):
        match = re.search(r'Id="' + r + r'"[^>]*Target="([^"]+)"', rels)
        if match and 'media/' in match.group(1):
            print(f'{r} -> {match.group(1)}')
