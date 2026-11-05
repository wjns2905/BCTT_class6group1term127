import docx
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Banh cuon
doc_mind = docx.Document('Tài nguyên/[BCTT] Mind & Soul.docx')
banh_cuon_paras = []
recording = False
for p in doc_mind.paragraphs:
    t = p.text.strip()
    if 'michelin-honored saigon eatery' in t.lower():
        recording = True
    if recording:
        if t:
            banh_cuon_paras.append(t)

print("=== BANH CUON PARAS ===")
for p in banh_cuon_paras[:10]:
    print(p[:100])

# 2. Tycoon villa
doc_soc = docx.Document('Tài nguyên/[BCTT] Society.docx')
tycoon_paras = []
recording = False
for p in doc_soc.paragraphs:
    t = p.text.strip()
    if 'inside hanoi tycoon' in t.lower():
        recording = True
    if recording:
        if t:
            tycoon_paras.append(t)

print("\n=== TYCOON PARAS ===")
for p in tycoon_paras[:10]:
    print(p[:100])

# 3. Vietnam for first-timers
vn_first_paras = []
recording = False
for p in doc_soc.paragraphs:
    t = p.text.strip()
    if 'vietnam for first-timers' in t.lower():
        recording = True
    elif 'inside hanoi tycoon' in t.lower():
        recording = False
    if recording:
        if t:
            vn_first_paras.append(t)

print("\n=== VN FIRST TIMERS PARAS ===")
for p in vn_first_paras[:10]:
    print(p[:100])
