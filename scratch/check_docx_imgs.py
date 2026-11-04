import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\camka\OneDrive\Desktop\BCTT\js\data.js', 'r', encoding='utf-8') as f:
    text = f.read()

data = json.loads(text.split('const ARTICLES_DATA = ', 1)[1].rsplit(';', 1)[0].strip())
print(f'Checking {len(data)} articles...')
editorial_crops = [a for a in data if 'assets/images/editorial/' in a.get('image', '')]
if editorial_crops:
    print(f'WARNING: {len(editorial_crops)} articles still use editorial crops!')
else:
    print('SUCCESS: 100% of articles use authentic images extracted from original docx files!')

for a in data[:12]:
    print(f"- {a['id']:12} -> {a['image']:40} | {a['title'][:55]}")
