import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

for m in re.finditer(r'function\s+([A-Za-z0-9_]*share[A-Za-z0-9_]*)\(', js, re.IGNORECASE):
    print("Found function:", m.group(0))

for m in re.finditer(r'([^\n]*facebook[^\n]*)', js, re.IGNORECASE):
    print("Facebook in js:", m.group(0)[:150])

for m in re.finditer(r'([^\n]*instagram[^\n]*)', js, re.IGNORECASE):
    print("Instagram in js:", m.group(0)[:150])

for m in re.finditer(r'([^\n]*twitter[^\n]*)', js, re.IGNORECASE):
    print("Twitter in js:", m.group(0)[:150])
