import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

pos_start = js.find('function renderAboutUsSection()')
pos_end = js.find('/* ===================================================================\n   ARTICLE DETAIL MODAL', pos_start)

about_body = js[pos_start:pos_end]

for word in ['facebook', 'instagram', 'twitter', 'x.com']:
    print(f"Contains {word}: {word in about_body.lower()}")
