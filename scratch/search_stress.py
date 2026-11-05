import os, sys

for fname in ['index.html', 'about.html', 'js/app.js', 'js/translations.js']:
    fpath = os.path.join(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127', fname)
    if not os.path.exists(fpath): continue
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    for phrase in ['Stress Reliever', 'loving heartbeats', 'compassionate solidarity', 'Mindful Heart']:
        if phrase.lower() in content.lower():
            idx = content.lower().find(phrase.lower())
            print(f"{fname} contains '{phrase}' at pos {idx}:")
            print(content[max(0, idx-100):min(len(content), idx+200)])
            print('-'*40)
