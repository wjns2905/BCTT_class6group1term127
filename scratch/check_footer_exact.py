import glob, os, sys
sys.stdout.reconfigure(encoding='utf-8')

root = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127'

for fpath in glob.glob(os.path.join(root, '*.html')):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    p1 = html.find('<footer')
    p2 = html.find('</footer>')
    print(f"=== {os.path.basename(fpath)} ===")
    print(html[p1:p2+9])
    print("\n" + "="*50 + "\n")
    break # Just print one to see structure
