import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

sub = js[27296:57486]
import re
funcs = re.findall(r'function\s+([A-Za-z0-9_]+)\(', sub)
print("Functions between playActiveVideo and formatArticleSource:")
print(funcs)
