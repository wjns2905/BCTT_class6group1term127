import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\data.js', 'r', encoding='utf-8') as f:
    text = f.read()

for i in range(1, 13):
    vid = f"video-{i}"
    found = f'id: "{vid}"' in text or f'id: \'{vid}\'' in text
    print(f"{vid}: found={found}")
