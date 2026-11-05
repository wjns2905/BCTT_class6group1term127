import glob, os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

root = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127'

for ext in ['*.html', 'js/*.js']:
    for fpath in glob.glob(os.path.join(root, ext)):
        if 'scratch' in fpath: continue
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        matches = re.findall(r'([^\n]*(?:Mindful Heart Beats|Stress Reliever|loving heartbeats|compassionate solidarity)[^\n]*)', content, re.IGNORECASE)
        if matches:
            print(f"=== {os.path.basename(fpath)} ===")
            for m in matches:
                print(" ", m.strip())
