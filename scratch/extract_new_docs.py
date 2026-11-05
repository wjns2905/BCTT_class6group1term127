# -*- coding: utf-8 -*-
import os
import sys
import zipfile
import xml.etree.ElementTree as ET
import shutil
import docx

sys.stdout.reconfigure(encoding='utf-8')

resource_dir = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\Tài nguyên"
target_files = [
    "[BCTT] Human stories.docx",
    "[BCTT] In-dept.docx",
    "[BCTT] Mind & Soul.docx",
    "[BCTT] Society.docx",
    "[BCTT] Trending.docx"
]

out_analysis_dir = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\scratch\updated_docs_analysis"
os.makedirs(out_analysis_dir, exist_ok=True)

for fn in target_files:
    fp = os.path.join(resource_dir, fn)
    base = os.path.splitext(fn)[0]
    doc_out = os.path.join(out_analysis_dir, base)
    os.makedirs(doc_out, exist_ok=True)
    img_out = os.path.join(doc_out, "media")
    os.makedirs(img_out, exist_ok=True)
    
    # Extract images from zip
    img_list = []
    with zipfile.ZipFile(fp) as z:
        for zinfo in z.infolist():
            if zinfo.filename.startswith("word/media/"):
                iname = os.path.basename(zinfo.filename)
                target_img_p = os.path.join(img_out, iname)
                with z.open(zinfo) as s, open(target_img_p, "wb") as d:
                    shutil.copyfileobj(s, d)
                img_list.append((iname, zinfo.file_size))
                
    # Read text with python-docx
    doc = docx.Document(fp)
    paras = [p.text for p in doc.paragraphs if p.text.strip()]
    tables_data = []
    for t in doc.tables:
        t_rows = []
        for r in t.rows:
            t_rows.append([c.text.strip() for c in r.cells])
        tables_data.append(t_rows)
        
    # Write extracted text
    text_path = os.path.join(doc_out, "content.txt")
    with open(text_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(paras))
        if tables_data:
            f.write("\n\n--- TABLES ---\n")
            for t in tables_data:
                for row in t:
                    f.write(" | ".join(row) + "\n")
                f.write("\n")
                
    print(f"=== {fn} ===")
    print(f"  Paragraphs: {len(paras)}")
    print(f"  Tables: {len(tables_data)}")
    print(f"  Images: {len(img_list)} files")
    for iname, isize in img_list[:5]:
        print(f"    - {iname} ({isize:,} bytes)")
    if len(img_list) > 5:
        print(f"    ... and {len(img_list) - 5} more images")
    print(f"  First 3 paragraphs:")
    for p in paras[:3]:
        print(f"    * {p[:120]}...")
    print()
