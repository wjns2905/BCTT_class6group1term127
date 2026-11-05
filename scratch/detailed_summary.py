# -*- coding: utf-8 -*-
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

analysis_dir = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\scratch\updated_docs_analysis"

docs = [
    "[BCTT] Human stories",
    "[BCTT] In-dept",
    "[BCTT] Mind & Soul",
    "[BCTT] Society",
    "[BCTT] Trending"
]

report = []

for d in docs:
    p = os.path.join(analysis_dir, d, "content.txt")
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Let's count characters, words, paragraphs
    paras = [para.strip() for para in text.split("\n\n") if para.strip()]
    media_dir = os.path.join(analysis_dir, d, "media")
    media_files = os.listdir(media_dir) if os.path.exists(media_dir) else []
    
    print(f"\n=======================================================")
    print(f"DOCUMENT: {d}")
    print(f"Total Words: {len(text.split()):,} | Total Paragraphs: {len(paras)} | Total Media: {len(media_files)}")
    print(f"=======================================================")
    
    # Find all URLs in this document
    urls = re.findall(r'https?://[^\s\)\"\'>]+', text)
    print(f"URLs found in doc ({len(urls)}):")
    for u in set(urls):
        print(f"  * {u}")
        
    # Also find any mentions of members who wrote or contributed:
    members = re.findall(r'\((?:Quỳnh|Mai|Ngọc Mai|Hà Anh|Phương Anh|Bảo Ngân|pa|qa|quỳnh|mai)\)', text, re.IGNORECASE)
    if members:
        print(f"Member tags found: {set(members)}")

