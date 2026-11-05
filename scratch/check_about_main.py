import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\about.html', 'r', encoding='utf-8') as f:
    html = f.read()

body_start = html.find('<main')
body_end = html.find('</main>')
print(html[body_start:body_start+2000])
