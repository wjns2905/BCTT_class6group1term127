import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

found = []
for root, dirs, files in os.walk('.'):
    if any(x in root for x in ['scratch', 'Tài nguyên', '.git', 'node_modules']):
        continue
    for f in files:
        if f.endswith(('.html', '.js', '.css', '.json')):
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()
            for idx, line in enumerate(lines):
                if 'bctt' in line.lower():
                    found.append((fp, idx + 1, line.strip()))

print(f"Total occurrences of 'bctt' found in site files: {len(found)}")
for fp, lnum, text in found:
    print(f"[{fp}:{lnum}] {text[:90]}")
