import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\about.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print("Occurrences of 'mission' in about.html:")
for m in re.finditer(r'([^\n]*mission[^\n]*)', html, re.IGNORECASE):
    print(m.group(0))
