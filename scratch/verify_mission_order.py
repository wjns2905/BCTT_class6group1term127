import glob, os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

print("=== VERIFYING MISSION ON TOP ===")

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

pos_start = js.find('function renderAboutUsSection()')
pos_end = js.find('/* ===================================================================\n   ARTICLE DETAIL MODAL', pos_start)

about_body = js[pos_start:pos_end]

# Check tabs order
tab_matches = re.findall(r'<a href="([^"]+)" class="about-tab-btn">', about_body)
print("Tabs order:", tab_matches)
assert tab_matches == ['#mission', '#profiles', '#photo', '#subscribe'], f"Tabs order mismatch: {tab_matches}"

# Check sections order
sec_matches = re.findall(r'<section id="([^"]+)"', about_body)
print("Sections order:", sec_matches)
assert sec_matches == ['mission', 'profiles', 'photo', 'subscribe'], f"Sections order mismatch: {sec_matches}"

# Check dropdown order across all 7 HTML files
for hf in glob.glob(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\*.html'):
    with open(hf, 'r', encoding='utf-8') as f:
        html = f.read()
    m = re.findall(r'<a href="about\.html#([^"]+)" class="about-dropdown-item">', html)
    print(f"{os.path.basename(hf)} dropdown items:", m)
    assert m == ['mission', 'profiles', 'photo', 'subscribe'], f"Dropdown order mismatch in {hf}: {m}"

print("\nSUCCESS! Mission is now on top everywhere!")
