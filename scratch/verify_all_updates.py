import os
import re
import sys

base_dir = 'C:/Users/camka/OneDrive/Desktop/BCTT_class6group1term127'
html_files = ['index.html', 'trending.html', 'society.html', 'human-stories.html', 'mind-soul.html', 'in-depth.html', 'about.html']

print("=== 1. VERIFYING NO 'BCTT' IN USER-FACING FILES ===")
bctt_found = 0
for fname in html_files + ['js/translations.js', 'js/app.js', 'js/data.js']:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Check if BCTT appears anywhere outside file paths or comments
    # Remove comments
    clean = re.sub(r'<!--[\s\S]*?-->', '', content)
    clean = re.sub(r'//.*', '', clean)
    clean = re.sub(r'/\*[\s\S]*?\*/', '', clean)
    matches = re.findall(r'\bBCTT\b', clean)
    if matches:
        print(f"FAILED: Found {len(matches)} occurrences of BCTT in {fname}")
        bctt_found += len(matches)
    else:
        print(f"PASS: {fname} has 0 occurrences of BCTT")

print(f"Total user-facing BCTT found: {bctt_found}")

print("\n=== 2. VERIFYING LANGUAGE SWITCH PILLS IN HTML FILES ===")
for fname in html_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    pills = re.findall(r'<div class="lang-switch-pill"([^>]*)>', html)
    print(f"{fname}: {len(pills)} lang-switch-pill(s) found")
    for p in pills:
        if 'display:none' in p:
            print(f"  WARNING: A pill in {fname} still has display:none!")

print("\n=== 3. VERIFYING ARTICLE VIDEOS IN DATA.JS ===")
with open(os.path.join(base_dir, 'js/data.js'), 'r', encoding='utf-8') as f:
    data_text = f.read()

# Check trending-1
m_t1 = re.search(r'"id":\s*"trending-1"[\s\S]*?"video":\s*"([^"]*)"', data_text)
if m_t1:
    print(f"trending-1 video: '{m_t1.group(1)}' (Expected empty: {m_t1.group(1) == ''})")

# Check all non-empty videos
import json
non_empty_videos = []
for m in re.finditer(r'"id":\s*"([^"]+)"[\s\S]*?"video":\s*"([^"]+)"', data_text):
    if m.group(2):
        non_empty_videos.append((m.group(1), m.group(2)))

print(f"Total articles with non-empty video: {len(non_empty_videos)}")
for art_id, vid in non_empty_videos:
    print(f"  {art_id}: {vid}")

print("\n=== 4. VERIFYING TITLE ===")
for fname in html_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    m_title = re.search(r'<title>([^<]+)</title>', html)
    if m_title:
        print(f"{fname} title: {m_title.group(1)}")

print("\nVERIFICATION COMPLETED.")
