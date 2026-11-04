import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\camka\OneDrive\Desktop\BCTT\js\data.js', 'r', encoding='utf-8') as f:
    text = f.read()

json_text = text.split('const ARTICLES_DATA = ', 1)[1].rsplit(';', 1)[0].strip()
data = json.loads(json_text)
print(f'Total articles currently in data.js: {len(data)}')

for i, a in enumerate(data):
    img = a.get('image', '')
    exists = os.path.exists(os.path.join(r'c:\Users\camka\OneDrive\Desktop\BCTT', img))
    sz = os.path.getsize(os.path.join(r'c:\Users\camka\OneDrive\Desktop\BCTT', img)) if exists else 0
    print(f"[{i+1:2}] ID: {a['id']:22} Cat: {a['category']:14} Img: {img:45} ({sz:7}b) Exists: {exists}")
    print(f"     Title: {a['title'][:75]}")
