import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('<footer')
pos_end = html.find('</footer>')
print(html[pos:pos_end+9])
