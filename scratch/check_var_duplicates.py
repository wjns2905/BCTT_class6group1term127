import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

lines = js.splitlines()
for idx, line in enumerate(lines):
    if 'currentActiveClipId' in line or 'isVideoPlaying' in line or 'currentVideoCategoryFilter' in line:
        print(f"Line {idx+1}: {line}")
