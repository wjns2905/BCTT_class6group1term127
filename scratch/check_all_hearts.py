import glob, re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

for fpath in glob.glob(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\*.html'):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    has_heart = '<svg class="fashion-slogan-heart"' in html
    has_pulse = 'stroke="#7D1728"' in html
    print(f"{os.path.basename(fpath)}: has_heart={has_heart}, has_pulse={has_pulse}")
