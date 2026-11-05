import glob, re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

for fpath in glob.glob(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\*.html'):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    m = re.search(r'<footer.*?</footer>', html, re.DOTALL)
    if m:
        footer = m.group(0)
        # Check first 500 chars of footer
        print(f"=== {os.path.basename(fpath)} ===")
        print(footer[:600])
        print()
