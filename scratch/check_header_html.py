import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'(<div class="fashion-masthead-hero">.*?</div>\s*</header>)', html, re.DOTALL)
if m:
    print(m.group(1)[:1500])
else:
    m2 = re.search(r'(<header.*?</header>)', html, re.DOTALL)
    if m2:
        print(m2.group(1)[:2000])
