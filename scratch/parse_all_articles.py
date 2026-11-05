# -*- coding: utf-8 -*-
import os
import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

analysis_dir = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\scratch\updated_docs_analysis"

docs = [
    "[BCTT] Human stories",
    "[BCTT] In-dept",
    "[BCTT] Mind & Soul",
    "[BCTT] Society",
    "[BCTT] Trending"
]

all_extracted_articles = {}

for d in docs:
    p = os.path.join(analysis_dir, d, "content.txt")
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()
        
    # Split text into sections by "1. ", "2. ", "3. ", "4. ", etc. at start of line or with Link
    # Let's find all URLs in the document and match them with article titles
    paras = text.split("\n\n")
    articles = []
    curr = None
    
    for para in paras:
        para_clean = para.strip()
        # Check if starts with a number like "1. ", "2. ", "3. " or "Bài 1"
        m = re.match(r'^(?:Bài\s*(\d+)|(\d+)[\.\/])\s*(.*)', para_clean)
        # Check if it looks like a new article header (e.g. contains URL or Link or title-like)
        is_num = False
        if m:
            num = int(m.group(1) or m.group(2))
            rest = m.group(3)
            # Avoid list items inside an article (e.g. "1. Search for and collect...")
            if num <= 15 and ('http' in para_clean.lower() or 'link' in para_clean.lower() or 'bài' in para_clean.lower() or len(rest) > 15):
                is_num = True
                
        if is_num:
            if curr:
                articles.append(curr)
            curr = {
                "num": num,
                "header": para_clean[:150],
                "paragraphs": []
            }
        elif curr:
            curr["paragraphs"].append(para_clean)
            
    if curr:
        articles.append(curr)
        
    all_extracted_articles[d] = articles
    print(f"=== {d}: {len(articles)} articles found ===")
    for a in articles:
        urls = re.findall(r'https?://[^\s\)]+', "\n".join([a["header"]] + a["paragraphs"][:4]))
        title = a["paragraphs"][0][:100] if a["paragraphs"] else a["header"]
        print(f"  #{a['num']}: {title}")
        if urls:
            print(f"      URL: {urls[0]}")
        print(f"      Content paragraphs: {len(a['paragraphs'])}")
    print()
