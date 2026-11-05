import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# find VIDEO_CLIPS definition
m = re.search(r'const\s+VIDEO_CLIPS\s*=\s*\[(.*?)\];', code, re.DOTALL)
if m:
    print("Found VIDEO_CLIPS definition, length:", len(m.group(1)))
    # print all items in VIDEO_CLIPS
    import json
    lines = m.group(1).splitlines()
    for l in lines[:30]:
        print(l)
else:
    print("VIDEO_CLIPS not found with regex")
