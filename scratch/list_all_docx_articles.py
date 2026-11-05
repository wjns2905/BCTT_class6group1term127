import docx
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

resource_dir = 'Tài nguyên'
docs = [
    '[BCTT] Trending.docx',
    '[BCTT] Society.docx',
    '[BCTT] Human stories.docx',
    '[BCTT] Mind & Soul.docx',
    '[BCTT] In-dept.docx'
]

for doc_name in docs:
    p = os.path.join(resource_dir, doc_name)
    doc = docx.Document(p)
    print("=" * 60)
    print(f"FILE: {doc_name}")
    print("=" * 60)
    for idx, para in enumerate(doc.paragraphs):
        t = para.text.strip()
        # Find lines with URLs or titles
        if any(keyword in t.lower() for keyword in ['http://', 'https://', 'bài', 'tên bài', 'link']) or para.style.name.startswith('Heading 1'):
            if len(t) < 180:
                print(f"  [{idx:3d}] {t}")
