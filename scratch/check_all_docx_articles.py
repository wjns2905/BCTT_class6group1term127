import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

for name in ['[BCTT] Mind & Soul.docx', '[BCTT] In-dept.docx', '[BCTT] Human stories.docx', '[BCTT] Trending.docx']:
    doc = docx.Document(f'Tài nguyên/{name}')
    print(f"\n=================== {name} ===================")
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if p.style.name.startswith('Heading 1') or (t and t[0].isdigit() and ('.' in t[:4] or ',' in t[:4])):
            print(f"P{i:3d}: {t[:120]}")
