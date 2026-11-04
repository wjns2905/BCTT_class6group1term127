import docx
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT = r"c:\Users\camka\OneDrive\Desktop\BCTT\Tài nguyên"

def inspect_file(fn):
    p = os.path.join(ROOT, fn)
    doc = docx.Document(p)
    print(f"\n==========================================")
    print(f"FILE: {fn}")
    print(f"==========================================")
    
    # Read all paragraphs
    articles = []
    current = None
    for idx, para in enumerate(doc.paragraphs):
        t = para.text.strip()
        if not t:
            continue
        is_link_header = any(k in t.lower() for k in ['http://', 'https://', 'link gốc', 'link bài', 'bài gốc'])
        if is_link_header:
            if current:
                articles.append(current)
            current = {
                'link': t,
                'title': '',
                'paras': [],
                'para_idx': idx
            }
        else:
            if current:
                if not current['title'] and len(t) > 5 and not t.startswith('http'):
                    current['title'] = t
                current['paras'].append(t)
            else:
                current = {
                    'link': '',
                    'title': t,
                    'paras': [t],
                    'para_idx': idx
                }
    if current:
        articles.append(current)
        
    for i, a in enumerate(articles):
        print(f"  [{i+1}] Title: {a['title']}")
        print(f"      Link: {a['link'][:80]}")
        print(f"      Paragraphs: {len(a['paras'])}")

for f in ['[BCTT] Trending.docx', '[BCTT] Society.docx', '[BCTT] Human stories.docx', '[BCTT] Mind & Soul.docx', '[BCTT] In-dept.docx']:
    inspect_file(f)
