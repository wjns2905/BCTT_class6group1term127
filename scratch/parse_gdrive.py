# -*- coding: utf-8 -*-
import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\scratch\gdrive_page.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("HTML length:", len(html))

# Look for filename patterns
img_patterns = re.findall(r'[\w\-\._\s]+\.(?:png|jpg|jpeg|webp|heic)', html, re.IGNORECASE)
print("Found image filename patterns:", set(img_patterns))

# Look for patterns like ["<id>", ["<name>"]] or drive items
# In modern Drive web pages, items are in JS objects or arrays
# Let's search for drive file IDs (alphanumeric 25-45 characters)
# and find any associated filenames
items = []
for m in re.finditer(r'([a-zA-Z0-9_-]{28,40})', html):
    token = m.group(1)
    # Check if this token is near an image filename
    start = max(0, m.start() - 200)
    end = min(len(html), m.end() + 200)
    surrounding = html[start:end]
    if any(ext in surrounding.lower() for ext in ['.jpg', '.png', '.jpeg', '.webp']):
        # Find the filename
        fn = re.findall(r'[\w\-\._\s]+\.(?:jpg|png|jpeg|webp|heic)', surrounding, re.IGNORECASE)
        if fn:
            items.append((token, fn[0]))

print(f"Candidate drive files with filenames ({len(items)}):")
unique_items = {}
for file_id, name in items:
    if name not in unique_items:
        unique_items[name] = file_id
        print(f"  Name: {name} | ID: {file_id}")

# Also search for names of the 5 group members in the HTML:
for member in ['Ngọc Mai', 'Hà Anh', 'Phương Anh', 'Bảo Ngân', 'Như Quỳnh', 'Mai', 'Anh', 'Ngân', 'Quỳnh']:
    matches = [m.start() for m in re.finditer(re.escape(member), html, re.IGNORECASE)]
    if matches:
        print(f"Found '{member}': {len(matches)} times")
        for pos in matches[:3]:
            print("  Context:", repr(html[max(0, pos-40):min(len(html), pos+120)]))
