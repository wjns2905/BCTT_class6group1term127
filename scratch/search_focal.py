import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/translations.js', 'r', encoding='utf-8') as f:
    tr = f.read()

with open('js/app.js', 'r', encoding='utf-8') as f:
    app = f.read()

for term in ['focal_lead_title', 'focal_lead_sapo', 'focal_badge', 'center-post-title', 'applyLanguage']:
    print(f"Term: {term}")
    for l in tr.splitlines():
        if term in l:
            print("  in translations.js:", l.strip()[:100])
    for l in app.splitlines():
        if term in l:
            print("  in app.js:", l.strip()[:100])
