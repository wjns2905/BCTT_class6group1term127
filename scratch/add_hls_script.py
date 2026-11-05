import glob, os, sys
sys.stdout.reconfigure(encoding='utf-8')

for fpath in glob.glob(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\*.html'):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if 'js/hls.min.js' not in html:
        new_html = html.replace('<script src="js/translations.js"></script>', '<script src="js/hls.min.js"></script>\n  <script src="js/translations.js"></script>')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Added hls.min.js to:", os.path.basename(fpath))
    else:
        print("Already present in:", os.path.basename(fpath))
