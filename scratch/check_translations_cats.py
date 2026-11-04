# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/build_multi_pages.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
featured_matches = re.findall(r'<article class="category-featured-card".*?</article>', text, re.DOTALL)
print(f"Total category featured cards: {len(featured_matches)}")
for i, m in enumerate(featured_matches):
    print(f"--- Card {i+1} ---")
    print(m[:300])
