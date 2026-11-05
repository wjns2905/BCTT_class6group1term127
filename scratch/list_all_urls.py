# -*- coding: utf-8 -*-
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

analysis_dir = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\scratch\updated_docs_analysis"

def extract_detailed_articles(doc_name):
    p = os.path.join(analysis_dir, doc_name, "content.txt")
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Find all numbered headers like "1. ", "2. ", "3. " etc.
    # We can split by lines that start with digits followed by dot/slash/parenthesis
    pattern = r'(?:\n|^)(?:Bài\s*\d+|\d+[\.\/]\s*|[A-Z]\.\s+)'
    
    # Also find URLs
    urls = re.findall(r'https?://[^\s\)\"\'>]+', text)
    
    return text, urls

for d in ["[BCTT] In-dept", "[BCTT] Mind & Soul", "[BCTT] Society", "[BCTT] Human stories", "[BCTT] Trending"]:
    text, urls = extract_detailed_articles(d)
    print(f"=== {d} ===")
    print(f"Total characters: {len(text):,} | Total words: {len(text.split()):,}")
    print(f"All Unique URLs in {d}:")
    for u in sorted(set(urls)):
        print(f"  * {u}")
    print()
