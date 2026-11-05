import sys
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect lines 80 to 260 of index.html
lines = html.splitlines()
print("Lines 80 to 240 of index.html:")
for i in range(80, min(240, len(lines))):
    print(f"{i+1:3d}: {lines[i]}")
