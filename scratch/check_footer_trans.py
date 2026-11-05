import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\translations.js', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.splitlines():
    if any(k in line for k in ['footer_desc', 'footer_group', 'footer_copy', 'footer_model']):
        print(line)
