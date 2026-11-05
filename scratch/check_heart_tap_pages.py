import glob, os, sys
sys.stdout.reconfigure(encoding='utf-8')

root = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127'

for fpath in glob.glob(os.path.join(root, '*.html')):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'heartTapSection' in html or 'heartTapBtn' in html:
        print("Found heartTap in:", os.path.basename(fpath))
