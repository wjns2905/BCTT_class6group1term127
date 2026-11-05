import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

pos = js.find('heartTapBtn')
if pos != -1:
    print("Found heartTapBtn in js/app.js at pos", pos)
    print(js[max(0, pos-200):min(len(js), pos+2000)])
else:
    print("heartTapBtn not found in js/app.js")
