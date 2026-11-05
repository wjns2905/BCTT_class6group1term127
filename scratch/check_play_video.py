import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    code = f.read()

m = re.search(r'function\s+playActiveVideo\b.*?(?=function|\Z)', code, re.DOTALL)
if m:
    print(m.group(0)[:1500])
