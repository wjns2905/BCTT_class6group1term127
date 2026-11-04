import os

target = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\css\style.css"
source_script = r"C:\Users\camka\OneDrive\Desktop\BCTT\scratch\append_update_css.py"

with open(source_script, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('new_css = """') + len('new_css = """')
end = text.find('"""', start)
new_css = text[start:end]

with open(target, 'r', encoding='utf-8') as f:
    cur = f.read()

if 'top-hero-3col-cluster' not in cur:
    cur += '\n' + new_css
    with open(target, 'w', encoding='utf-8') as f:
        f.write(cur)
    print('SUCCESS: Appended new_css to BCTT_class6group1term127/css/style.css!')
else:
    print('ALREADY PRESENT in BCTT_class6group1term127/css/style.css')
