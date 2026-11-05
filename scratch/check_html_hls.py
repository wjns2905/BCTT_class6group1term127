import glob, os, sys
sys.stdout.reconfigure(encoding='utf-8')

for fpath in glob.glob(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\*.html'):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    has_hls = 'hls.min.js' in html
    print(f"{os.path.basename(fpath)}: has_hls={has_hls}")
