import sys, docx, os

sys.stdout.reconfigure(encoding='utf-8')

for fname in ['[BCTT] Trending.docx', '[BCTT] Society.docx', '[BCTT] Human stories.docx', '[BCTT] Mind & Soul.docx', '[BCTT] In-dept.docx']:
    d = docx.Document(os.path.join('Tài nguyên', fname))
    print(f'=== {fname} ===')
    print(f'Paragraphs: {len(d.paragraphs)}, Tables: {len(d.tables)}')
    for ti, t in enumerate(d.tables):
        print(f'  Table #{ti}: rows={len(t.rows)}, cols={len(t.columns)}')
        for ri, row in enumerate(t.rows[:3]):
            cell_texts = [c.text.strip()[:60].replace('\n', ' ') for c in row.cells]
            print(f'    Row {ri}: {cell_texts}')
