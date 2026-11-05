import glob, os, sys
sys.stdout.reconfigure(encoding='utf-8')

root = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127'
found = False

for ext in ['*.html', 'js/*.js', 'css/*.css']:
    for fpath in glob.glob(os.path.join(root, ext)):
        # Skip scratch files
        if 'scratch' in fpath: continue
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            for lno, line in enumerate(f, 1):
                if 'bctt' in line.lower():
                    # Check if it is a word boundary or in text
                    print(f"{os.path.basename(fpath)}:{lno}: {line.strip()[:100]}")
                    found = True

if not found:
    print("SUCCESS: EXACTLY ZERO occurrences of BCTT found in web files!")
