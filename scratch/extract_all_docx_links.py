import sys, os, docx, json, re

sys.stdout.reconfigure(encoding='utf-8')

docx_files = {
    'trending': 'Tài nguyên/[BCTT] Trending.docx',
    'society': 'Tài nguyên/[BCTT] Society.docx',
    'human-stories': 'Tài nguyên/[BCTT] Human stories.docx',
    'mind-soul': 'Tài nguyên/[BCTT] Mind & Soul.docx',
    'in-depth': 'Tài nguyên/[BCTT] In-dept.docx'
}

all_docx_links = []

for cat, fpath in docx_files.items():
    doc = docx.Document(fpath)
    for p in doc.paragraphs:
        t = p.text.strip()
        links = re.findall(r'https?://[^\s]+', t)
        for l in links:
            clean_l = l.rstrip('.,)"\'')
            all_docx_links.append((cat, clean_l, t[:80]))

print(f"Total links extracted from 5 DOCX files: {len(all_docx_links)}")
for cat, link, ctx in all_docx_links:
    print(f"[{cat:12}] {link}")
