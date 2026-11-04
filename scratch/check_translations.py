# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('js/translations.js', 'r', encoding='utf-8') as f:
    text = f.read()

vi_part = text[text.find('vi: {'):text.find('en: {')]
keys = re.findall(r'([a-zA-Z0-9_\-]+)\s*:', vi_part)
print(f"Total keys in vi: {len(keys)}")
for k in keys:
    print(k)
