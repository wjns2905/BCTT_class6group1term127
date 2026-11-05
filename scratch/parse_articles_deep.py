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

all_articles_data = []

for d in docs:
    p = os.path.join(analysis_dir, d, "content.txt")
    with open(p, "r", encoding="utf-8") as f:
        full_text = f.read()
        
    paras = [para.strip() for para in full_text.split("\n\n") if para.strip()]
    
    # We want to segment paragraphs into discrete articles.
    # Most documents begin articles with lines like:
    # "1. Link bài:..." or "1.https://..." or "1. Link gốc..."
    # "2. Link bài:..." or "2. https://..."
    # Let's locate the split indices:
    split_indices = []
    for idx, para in enumerate(paras):
        # Match pattern at start of paragraph: "1.", "2.", "3.", "10." etc.
        m = re.match(r'^(\d+)[\.\/]\s*(.*)', para)
        if m:
            num = int(m.group(1))
            line_start = m.group(2).strip()
            # Verify if this is an article header:
            # Usually has 'http' or 'link' or len > 20 or starts a major story
            # In Human Stories: 1. Link bài, 2. Link bài, 3. (Link bài ), 4.https://, 5. Link bài, 6. The Kindness, 7. Gánh mưu sinh, 8. On World Kindness Day
            is_article_header = False
            if 'http' in para.lower() or 'link' in para.lower() or 'bài' in para.lower() or 'optimist' in para.lower() or 'kindness' in para.lower():
                is_article_header = True
            elif num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and len(para) < 250 and not para.lower().startswith("search for"):
                is_article_header = True
                
            if is_article_header:
                split_indices.append((idx, num, para))
                
    # Filter split indices to remove sub-lists (like "1. Search for... 2. Complete the collection...")
    filtered_splits = []
    last_num = 0
    for idx, num, para in split_indices:
        if "search for and collect" in para.lower() or "complete the collection" in para.lower() or "conduct dna testing" in para.lower() or "develop, complete" in para.lower():
            continue
        filtered_splits.append((idx, num, para))
        
    print(f"=== {d}: Filtered into {len(filtered_splits)} articles ===")
    for s_i, (idx, num, para) in enumerate(filtered_splits):
        end_idx = filtered_splits[s_i + 1][0] if s_i + 1 < len(filtered_splits) else len(paras)
        art_paras = paras[idx:end_idx]
        header = art_paras[0]
        
        # Extract URL
        urls = re.findall(r'https?://[^\s\)\"\'>]+', "\n".join(art_paras[:5]))
        url = urls[0] if urls else ""
        
        # Extract title (first line that is not just a link)
        title_candidates = [p for p in art_paras[:4] if not p.strip().startswith("http") and not p.strip().startswith("Link") and len(p.strip()) > 10]
        title = title_candidates[0] if title_candidates else header
        
        print(f"  Article #{num}: {title[:80]}")
        print(f"    URL: {url}")
        print(f"    Paras: {len(art_paras)} | Words: {sum(len(p.split()) for p in art_paras):,}")
        
    print()
