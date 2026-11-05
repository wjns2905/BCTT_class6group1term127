import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('Tài nguyên/[BCTT] Society.docx')
for i in range(160, len(doc.paragraphs)):
    t = doc.paragraphs[i].text.strip()
    if t:
        print(f"P{i:3d}: {t[:100]}")
