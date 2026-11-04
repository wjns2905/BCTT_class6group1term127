# -*- coding: utf-8 -*-
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

ROOT = r"c:\Users\camka\OneDrive\Desktop\BCTT"
PAGES = [
    "index.html",
    "trending.html",
    "society.html",
    "human-stories.html",
    "mind-soul.html",
    "in-depth.html",
    "about.html"
]

print("=== 1. VERIFY HTML FILES EXISTENCE & CORE INJECTIONS ===")
all_passed = True
for p in PAGES:
    path = os.path.join(ROOT, p)
    if not os.path.exists(path):
        print(f"FAILED: {p} not found!")
        all_passed = False
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    has_trans = 'src="js/translations.js"' in html
    has_data = 'src="js/data.js"' in html
    has_app = 'src="js/app.js"' in html
    has_pill = 'lang-switch-pill' in html
    has_i18n = 'data-i18n=' in html
    has_ulis = 'Trường Đại học Ngoại ngữ' in html
    no_ajc = 'Học viện Báo chí' not in html

    status = (has_trans and has_data and has_app and has_pill and has_i18n and has_ulis and no_ajc)
    if not status:
        all_passed = False
        print(f"FAILED: {p} checks: trans={has_trans}, data={has_data}, app={has_app}, pill={has_pill}, i18n={has_i18n}, ulis={has_ulis}, no_ajc={no_ajc}")
    else:
        print(f"PASSED: {p} (Size: {len(html)} bytes | Scripts, Pill, ULIS & i18n OK)")

print("\n=== 2. VERIFY TRANSLATION DICTIONARY COVERAGE ===")
with open(os.path.join(ROOT, 'index.html'), 'r', encoding='utf-8') as f:
    index_html = f.read()

used_keys = set(re.findall(r'data-i18n="([^"]+)"', index_html))
print(f"Total data-i18n keys used in index.html: {len(used_keys)}")

with open(os.path.join(ROOT, 'js', 'translations.js'), 'r', encoding='utf-8') as f:
    trans_js = f.read()

vi_keys = set(re.findall(r'([a-zA-Z0-9_\-]+)\s*:', trans_js[trans_js.find('vi: {'):trans_js.find('en: {')]))
en_keys = set(re.findall(r'([a-zA-Z0-9_\-]+)\s*:', trans_js[trans_js.find('en: {'):]))

missing_in_vi = used_keys - vi_keys
missing_in_en = used_keys - en_keys

if missing_in_vi:
    print(f"WARNING: Keys in index.html missing from vi: {missing_in_vi}")
else:
    print("PASSED: All index.html keys exist in I18N_TRANSLATIONS.vi!")

if missing_in_en:
    print(f"WARNING: Keys in index.html missing from en: {missing_in_en}")
else:
    print("PASSED: All index.html keys exist in I18N_TRANSLATIONS.en!")

print("\n=== 3. VERIFY LOCAL IMAGES INTEGRITY ===")
img_srcs = set(re.findall(r'src="([^"]+\.(?:jpg|jpeg|png|svg|webp))"', index_html))
missing_imgs = []
for src in img_srcs:
    if src.startswith('http'):
        continue
    img_path = os.path.join(ROOT, src.replace('/', os.sep))
    if not os.path.exists(img_path):
        missing_imgs.append(src)

if missing_imgs:
    print(f"FAILED: Missing images: {missing_imgs}")
else:
    print(f"PASSED: All {len(img_srcs)} local images referenced on index.html exist on disk!")

print("\n=== OVERALL RESULT ===")
if all_passed and not missing_in_vi and not missing_in_en and not missing_imgs:
    print("ALL VERIFICATION CHECKS PASSED WITH 100% SUCCESS!")
else:
    print("SOME CHECKS FAILED. PLEASE REVIEW ABOVE LOGS.")
