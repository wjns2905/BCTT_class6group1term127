import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos1 = html.find('<section class="heart-tap-container"')
pos2 = html.find('</section>', pos1) + 10
print(html[pos1:pos2])
