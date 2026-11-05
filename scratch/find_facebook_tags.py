import glob, os, sys
sys.stdout.reconfigure(encoding='utf-8')

root = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127'

for ext in ['*.html', 'js/*.js']:
    for fpath in glob.glob(os.path.join(root, ext)):
        if 'scratch' in fpath: continue
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        idx = 0
        while True:
            pos = content.find('fa-facebook', idx)
            if pos == -1: break
            print(f"{os.path.basename(fpath)} at {pos}:")
            print(content[max(0, pos-150):min(len(content), pos+200)])
            print('-'*40)
            idx = pos + 1
