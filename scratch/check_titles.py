import glob, os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

root = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127'

for fpath in glob.glob(os.path.join(root, '*.html')):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    m_title = re.search(r'<title>(.*?)</title>', html)
    print(f"{os.path.basename(fpath)}: <title>{m_title.group(1) if m_title else 'NONE'}</title>")
