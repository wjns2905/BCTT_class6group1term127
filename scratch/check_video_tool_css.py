import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

m = re.findall(r'(\.video-tool[^{]*\{[^}]+\}|\.video-toolbar[^{]*\{[^}]+\})', css)
for r in m:
    print(r)
    print('-'*40)
