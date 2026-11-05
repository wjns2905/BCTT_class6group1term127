import glob, os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

root = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127'

for ext in ['*.html', 'js/*.js']:
    for fpath in glob.glob(os.path.join(root, ext)):
        if 'scratch' in fpath: continue
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Find any <a> with social icon (fa-facebook, fa-instagram, fa-twitter, fa-x-twitter, fa-share)
        for m in re.finditer(r'(<a\b[^>]*>(?:(?!</a>).)*(?:fa-facebook|fa-instagram|fa-twitter|fa-x-twitter|fa-share)[^<]*</a>)', content, re.IGNORECASE | re.DOTALL):
            tag = m.group(0).strip()
            print(f"{os.path.basename(fpath)}: {tag}")
