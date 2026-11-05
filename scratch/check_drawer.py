import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<div class="offcanvas-drawer">.*?</div>', html, re.DOTALL)
if m:
    print(m.group(0))
