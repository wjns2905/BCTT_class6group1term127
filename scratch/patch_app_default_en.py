# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Change default fallback language from 'vi' to 'en'
old_lang1 = "let currentLanguage = localStorage.getItem('hearticles_lang') || 'vi';"
new_lang1 = "let currentLanguage = localStorage.getItem('hearticles_lang') || 'en';"

old_lang2 = "currentLanguage = localStorage.getItem('hearticles_lang') || 'vi';"
new_lang2 = "currentLanguage = localStorage.getItem('hearticles_lang') || 'en';"

norm_text = text.replace('\r\n', '\n')
if old_lang1 in norm_text:
    norm_text = norm_text.replace(old_lang1, new_lang1, 1)
    print("SUCCESS: Default currentLanguage initialized to 'en'!")
else:
    print("FAIL: old_lang1 not found")

if old_lang2 in norm_text:
    norm_text = norm_text.replace(old_lang2, new_lang2, 1)
    print("SUCCESS: initLanguage updated to default to 'en'!")
else:
    print("FAIL: old_lang2 not found")

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(norm_text)
print("js/app.js saved successfully!")
