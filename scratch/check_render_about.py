import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

pos = js.find('function renderAboutUsSection(')
print(js[pos:pos+3500])
