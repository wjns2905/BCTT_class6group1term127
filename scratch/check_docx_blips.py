import docx
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's see the images inside Society.docx and Mind & Soul.docx
for doc_name in ['[BCTT] Mind & Soul.docx', '[BCTT] Society.docx']:
    doc = docx.Document(f'Tài nguyên/{doc_name}')
    print(f"\nImages in {doc_name}:")
    for i, p in enumerate(doc.paragraphs):
        # Check if paragraph has drawing / blip
        xml = p._p.xml
        if 'graphicData' in xml or 'blip' in xml:
            print(f"  P{i:3d}: {p.text[:60]} (has graphic/image)")
