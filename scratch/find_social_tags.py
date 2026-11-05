import glob, os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

root = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127'

for ext in ['*.html', 'js/app.js']:
    for fpath in glob.glob(os.path.join(root, ext)):
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        matches = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(?:(?!</a>).)*(?:facebook|instagram|twitter|\bx\b)[^<]*</a>', content, re.IGNORECASE | re.DOTALL)
        for m in re.finditer(r'<a\b[^>]*>(?:(?!</a>).)*(?:facebook|instagram|twitter|x-twitter)[^<]*</a>', content, re.IGNORECASE | re.DOTALL):
            print(f"{os.path.basename(fpath)}: {m.group(0).strip()}")
