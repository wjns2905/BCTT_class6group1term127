import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

for m in re.finditer(r'([^\n]*about-tab[^\n]*)', js):
    print(m.group(0))
