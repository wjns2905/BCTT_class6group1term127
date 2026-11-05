import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\translations.js', 'r', encoding='utf-8') as f:
    text = f.read()

print("Contains ad_label:", "ad_label" in text)
for line in text.splitlines():
    if "ad_label" in line:
        print(" ", line)
