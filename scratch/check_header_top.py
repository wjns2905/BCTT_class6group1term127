import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('<body')
pos_end = html.find('<!-- =================================================================\n       3. STICKY EDITORIAL NAVIGATION')
print(html[pos:pos+3000])
