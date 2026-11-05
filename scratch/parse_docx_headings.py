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
    if not os.path.exists(p):
        print(f"File not found: {p}")
        continue
    doc = docx.Document(p)
    print("=" * 70)
    print(f"DOCUMENT: {doc_name} (Paragraphs: {len(doc.paragraphs)}, Tables: {len(doc.tables)})")
    print("=" * 70)
    # Print paragraphs that look like titles or headings
    for idx, para in enumerate(doc.paragraphs):
        text = para.text.strip()
        if not text:
            continue
        # If styled as heading or is all caps or short or bold
        is_bold = any(run.bold for run in para.runs if run.bold is not None)
        if len(text) < 120 and (is_bold or para.style.name.startswith('Heading') or text.startswith(('I.', 'II.', 'III.', 'IV.', 'V.', '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', 'Bài', 'Topic', 'Tên bài', 'Title'))):
            print(f"  P{idx:3d} [{para.style.name}]: {text}")
