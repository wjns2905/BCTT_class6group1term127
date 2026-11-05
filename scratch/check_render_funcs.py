import sys, re

sys.stdout.reconfigure(encoding='utf-8')
with open('js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

funcs = re.findall(r'function\s+(render\w+)\s*\(', text)
print("Render functions in app.js:", funcs)
