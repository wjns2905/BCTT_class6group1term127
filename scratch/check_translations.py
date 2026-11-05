import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\translations.js', 'r', encoding='utf-8') as f:
    text = f.read()

print("Contains btn_subscribe:", "btn_subscribe" in text)
for line in text.splitlines():
    if "btn_subscribe" in line or "subscribe" in line.lower() and ":" in line:
        print(" ", line)
