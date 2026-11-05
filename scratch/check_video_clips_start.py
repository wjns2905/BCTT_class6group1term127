import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

m = re.search(r'(const\s+VIDEO_CLIPS\s*=\s*\[.*?\];)', js, re.DOTALL)
if m:
    print(m.group(1)[:2000])
