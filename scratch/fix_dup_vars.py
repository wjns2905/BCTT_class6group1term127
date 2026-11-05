import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

target = """let currentActiveClipId = 'clip-1';
let isVideoPlaying = false;"""

# Replace the second occurrence
parts = js.split(target)
if len(parts) == 3:
    # Keep the first, remove the second
    new_js = parts[0] + target + parts[1] + "// State managed above" + parts[2]
    with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'w', encoding='utf-8') as f:
        f.write(new_js)
    print("Fixed duplicate variable declaration!")
else:
    print(f"Count of target is {len(parts)-1}")
