import shutil, os, sys
sys.stdout.reconfigure(encoding='utf-8')

src = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127'
dst = r'C:\Users\camka\OneDrive\Desktop\BCTT'

print(f"Syncing from {src} to {dst}...")

# Ignore scratch and git
def ignore_patterns(path, names):
    return [n for n in names if n in ['.git', 'scratch', '.vscode']]

for item in os.listdir(src):
    if item in ['.git', 'scratch', '.vscode']:
        continue
    s = os.path.join(src, item)
    d = os.path.join(dst, item)
    if os.path.isdir(s):
        if os.path.exists(d):
            shutil.rmtree(d)
        shutil.copytree(s, d)
        print(f"Copied directory {item}")
    else:
        shutil.copy2(s, d)
        print(f"Copied file {item}")

print("Sync completed successfully!")
