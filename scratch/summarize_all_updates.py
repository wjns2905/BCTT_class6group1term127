# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

analysis_dir = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\scratch\updated_docs_analysis"

docs = [
    ("[BCTT] In-dept", "In-Depth (Phóng sự & Chuyên đề Chuyên sâu)", "in-dept"),
    ("[BCTT] Mind & Soul", "Mind & Soul (Tâm hồn & Lối sống)", "mind_&_soul"),
    ("[BCTT] Society", "Society (Xã hội & Đời sống Số)", "society"),
    ("[BCTT] Human stories", "Human Stories (Câu chuyện Nhân văn)", "human_stories"),
    ("[BCTT] Trending", "Trending (Dòng sự kiện & Xu hướng)", "trending")
]

for doc_folder, cat_title, img_folder in docs:
    p = os.path.join(analysis_dir, doc_folder, "content.txt")
    media_dir = os.path.join(analysis_dir, doc_folder, "media")
    media_count = len(os.listdir(media_dir)) if os.path.exists(media_dir) else 0
    
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()
        
    print(f"=======================================================")
    print(f"CHUYÊN MỤC: {cat_title}")
    print(f"Tệp docx: {doc_folder}.docx | Hình ảnh: {media_count} ảnh")
    print(f"=======================================================")
    
    # Let's find sections starting with a number e.g. "1.", "2.", "3."
    lines = text.split("\n")
    current_art = None
    articles = []
    
    for line in lines:
        l = line.strip()
        import re
        if re.match(r'^(?:Bài\s*\d+|\d+[\.\/])\s*', l) and len(l) < 180 and not l.lower().startswith("search for") and not l.lower().startswith("complete the") and not l.lower().startswith("conduct dna") and not l.lower().startswith("develop, complete"):
            if current_art:
                articles.append(current_art)
            current_art = {"header": l, "lines": []}
        elif current_art:
            if l:
                current_art["lines"].append(l)
                
    if current_art:
        articles.append(current_art)
        
    print(f"Số lượng bài viết: {len(articles)}")
    for idx, art in enumerate(articles):
        # find URL
        url_match = re.search(r'https?://[^\s\)]+', "\n".join([art["header"]] + art["lines"][:3]))
        url = url_match.group(0) if url_match else "N/A"
        # find author or member tag
        member = ""
        for tag in ["(Quỳnh)", "(pa)", "(Mai)", "(qa)"]:
            if tag.lower() in art["header"].lower() or any(tag.lower() in ln.lower() for ln in art["lines"][:3]):
                member = f" [BTV: {tag}]"
                break
        title = art["lines"][0] if art["lines"] and not art["lines"][0].startswith("http") else art["header"]
        print(f"  {idx+1}. {title[:90]}{member}")
        print(f"     Nguồn / Link: {url}")
        print(f"     Độ dài: {len(art['lines'])} đoạn ({sum(len(ln.split()) for ln in art['lines']):,} từ)")
    print()
