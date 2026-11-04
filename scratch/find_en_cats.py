# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/build_multi_pages.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos_head = text.find('def get_header(active_key):')
pos_foot = text.find('def get_footer():')
print(text[pos_head:pos_head+1000])
print("\n" + "="*50 + "\n")
print(text[pos_foot:pos_foot+1200])
