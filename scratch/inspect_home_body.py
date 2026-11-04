# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/build_multi_pages.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('home_body =')
if pos != -1:
    print("Found home_body at pos", pos)
    print(text[pos:pos+1500])

