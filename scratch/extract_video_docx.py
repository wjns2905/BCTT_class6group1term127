# -*- coding: utf-8 -*-
import os
import sys
import zipfile
import shutil
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

docx_path = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\Tài nguyên\[BCTT] Video.docx"
target_dir = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127"
out_img_dir = os.path.join(target_dir, "assets", "images", "video")
os.makedirs(out_img_dir, exist_ok=True)

scratch_dir = os.path.join(target_dir, "scratch", "extracted")
os.makedirs(scratch_dir, exist_ok=True)
out_txt_file = os.path.join(scratch_dir, "video_docx_content.txt")

if not os.path.exists(docx_path):
    print(f"ERROR: Docx not found at {docx_path}")
    sys.exit(1)

print(f"Opening docx: {docx_path} ({os.path.getsize(docx_path)} bytes)")

with zipfile.ZipFile(docx_path, 'r') as z:
    file_list = z.namelist()
    print(f"Archive contains {len(file_list)} files.")
    
    # 1. Extract hyperlinks map from document.xml.rels
    rels_map = {}
    if 'word/_rels/document.xml.rels' in file_list:
        rels_xml = z.read('word/_rels/document.xml.rels')
        try:
            tree_rels = ET.fromstring(rels_xml)
            for elem in tree_rels:
                r_id = elem.attrib.get('Id')
                target = elem.attrib.get('Target')
                type_str = elem.attrib.get('Type', '')
                if r_id and target:
                    rels_map[r_id] = target
                    if 'hyperlink' in type_str.lower() or target.startswith('http'):
                        print(f"Found hyperlink [{r_id}]: {target}")
        except Exception as e:
            print("Error parsing rels:", e)

    # 2. Extract media
    media_count = 0
    for name in file_list:
        if name.startswith('word/media/'):
            base_img = os.path.basename(name)
            dst_path = os.path.join(out_img_dir, base_img)
            with z.open(name) as src, open(dst_path, 'wb') as dst:
                shutil.copyfileobj(src, dst)
            media_count += 1
            print(f"Extracted media: {base_img} ({os.path.getsize(dst_path)} bytes)")
    print(f"Total media extracted: {media_count}")

    # 3. Extract text and hyperlinks from document.xml
    doc_xml = z.read('word/document.xml')
    tree = ET.fromstring(doc_xml)
    
    namespaces = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    }

    paragraphs = []
    for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
        p_parts = []
        for child in p.iter():
            # Check for hyperlink
            if child.tag.endswith('}hyperlink'):
                rel_id = child.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
                if rel_id and rel_id in rels_map:
                    p_parts.append(f" [LINK: {rels_map[rel_id]}] ")
            elif child.tag.endswith('}t'):
                if child.text:
                    p_parts.append(child.text)
        
        p_text = ''.join(p_parts).strip()
        if p_text:
            paragraphs.append(p_text)

    full_text = '\n\n'.join(paragraphs)
    with open(out_txt_file, 'w', encoding='utf-8') as f:
        f.write(full_text)

    print("\n" + "="*50)
    print("EXTRACTED CONTENT:")
    print("="*50)
    print(full_text)
    print("="*50)
    print(f"Saved full text to: {out_txt_file}")
