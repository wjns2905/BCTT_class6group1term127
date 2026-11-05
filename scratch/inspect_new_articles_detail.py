# -*- coding: utf-8 -*-
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

analysis_dir = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\scratch\updated_docs_analysis"

new_articles_specs = [
    ("[BCTT] In-dept", "Meet the educators using science to teach kindness"),
    ("[BCTT] In-dept", "Meet three people who make a living"),
    ("[BCTT] In-dept", "Rory Kinnear on his father Roy’s death"),
    ("[BCTT] Mind & Soul", "The women’s boxing nights helping abuse survivors"),
    ("[BCTT] Mind & Soul", "Canadian ‘outside skirt’ beef"),
    ("[BCTT] Mind & Soul", "Michelin-honored Saigon eatery serves banh cuon"),
    ("[BCTT] Society", "Vietnamese Buddhist temples embrace TikTok sermons"),
    ("[BCTT] Society", "Vietnam's GDP grows 9.01%"),
    ("[BCTT] Society", "A Vietnamese voice in a South African home"),
    ("[BCTT] Society", "Inside Hanoi tycoon’s 100-year-old villa"),
    ("[BCTT] Society", "Vietnam for first-timers"),
    ("[BCTT] Human stories", "On World Kindness Day, how one nonprofit has given the gift of mobility"),
    ("[BCTT] Human stories", "Stable electricity brings light to homes in remote")
]

for doc_name, keyword in new_articles_specs:
    p = os.path.join(analysis_dir, doc_name, "content.txt")
    if not os.path.exists(p):
        continue
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()
    
    pos = text.lower().find(keyword.lower())
    if pos != -1:
        start = max(0, pos - 100)
        end = min(len(text), pos + 1200)
        print(f"=== FOUND: {doc_name} -> '{keyword}' ===")
        print(text[start:end])
        print("------------------------------------------------------\n")
    else:
        print(f"*** NOT FOUND: {doc_name} -> '{keyword}' ***")
