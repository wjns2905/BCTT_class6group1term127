import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

pos_start = js.find('function renderAboutUsSection()')
pos_end = js.find('/* ===================================================================\n   ARTICLE DETAIL MODAL', pos_start)
if pos_end == -1:
    pos_end = js.find('function formatArticleSource(', pos_start)

print(f"renderAboutUsSection length: {pos_end - pos_start}")
print(js[pos_start:pos_start+1500])
print("\n" + "="*50 + "\nTAIL OF renderAboutUsSection:")
print(js[pos_end-1500:pos_end])
