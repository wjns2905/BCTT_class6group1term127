import glob, os, sys
sys.stdout.reconfigure(encoding='utf-8')

for fpath in glob.glob(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\*.html'):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'videoHubContent' in html or 'video-hub-section' in html:
        print("Found video hub in:", os.path.basename(fpath))
