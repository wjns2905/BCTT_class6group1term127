import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

pos_start = js.find('function renderAboutUsSection()')
pos_end = js.find('/* ===================================================================\n   ARTICLE DETAIL MODAL', pos_start)

about_body = js[pos_start:pos_end]

# Find markers
p1 = about_body.find('<!-- SECTION 1: PROFILES (#profiles) -->')
p2 = about_body.find('<!-- SECTION 2: PHOTOJOURNALISM MOSAIC (#photo) -->')
p3 = about_body.find('<!-- SECTION 3: NEWSLETTER SUBSCRIPTION (#subscribe) -->')
p4 = about_body.find('<!-- SECTION 4: MISSION & EDITORIAL PHILOSOPHY (#mission) -->')

print(f"p1={p1}, p2={p2}, p3={p3}, p4={p4}")
print("\n" + "="*50)
print("Header and Nav block:")
print(about_body[:p1])
print("\n" + "="*50)
print("Section 4 Mission block:")
print(about_body[p4:])
