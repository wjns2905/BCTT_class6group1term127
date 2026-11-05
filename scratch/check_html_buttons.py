import glob, re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

for fpath in glob.glob(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\*.html'):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    btns = re.findall(r'<button[^>]*class=["\'][^"\']*subscribe[^"\']*["\'][^>]*>.*?</button>', html, re.DOTALL | re.IGNORECASE)
    print(os.path.basename(fpath), len(btns))
    for b in btns:
        print("  ->", b.strip())
