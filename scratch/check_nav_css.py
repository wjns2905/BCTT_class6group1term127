import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# find masthead and category bar styles
for m in re.finditer(r'(\.fashion-masthead[^{]*\{[^}]+\}|\.fashion-category[^{]*\{[^}]+\}|\.category-bar[^{]*\{[^}]+\}|\.main-nav[^{]*\{[^}]+\})', css):
    print(m.group(0))
    print('-'*50)
