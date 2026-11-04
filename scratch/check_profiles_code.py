import sys
sys.stdout.reconfigure(encoding='utf-8')

p = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js"
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="profiles"')
if idx != -1:
    print(text[idx-50:idx+2500])
else:
    print("Not found")
