import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

for sel in ['header-ad-leaderboard-wrap', 'header-ad-banner-img', 'ad-label-strip']:
    m = re.findall(rf'(\.{sel}[^{{]*\{{[^}}]+\}})', css)
    print(f"{sel}: found {len(m)}")
    for r in m:
        print(r)
