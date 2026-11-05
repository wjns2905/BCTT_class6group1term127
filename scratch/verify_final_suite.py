import os, sys, glob, re
sys.stdout.reconfigure(encoding='utf-8')

print("=== FINAL VERIFICATION SUITE ===")
errors = []

# 1. Check HTML files
html_files = glob.glob(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\*.html')
print(f"Total HTML files: {len(html_files)}")
if len(html_files) != 7:
    errors.append(f"Expected 7 HTML files, found {len(html_files)}")

# 2. Check title
for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if 'Class6group1term127' not in c:
        errors.append(f"Missing Class6group1term127 in {os.path.basename(f)}")
    if 'hls.min.js' not in c:
        errors.append(f"Missing hls.min.js in {os.path.basename(f)}")
    if 'fashion-footer-logo-img' not in c:
        errors.append(f"Missing full logo in footer in {os.path.basename(f)}")
    if 'fashion-slogan-heart' not in c:
        errors.append(f"Missing slogan heart in {os.path.basename(f)}")

# 3. Check BCTT absence
for f in html_files + glob.glob(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\*.js') + glob.glob(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\css\*.css'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        for idx, line in enumerate(fp, 1):
            if 'bctt' in line.lower():
                errors.append(f"Found BCTT in {os.path.basename(f)}:{idx}")

# 4. Check video clips in app.js
with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as fp:
    app_js = fp.read()

clips_match = re.findall(r'id:\s*"clip-(\d+)"', app_js)
print(f"Total clips found in app.js: {len(clips_match)}")
if len(clips_match) != 12:
    errors.append(f"Expected 12 clips, found {len(clips_match)}")

# 5. Check Mission text in app.js
if "Welcome to HEARTICLES" not in app_js:
    errors.append("Welcome to HEARTICLES missing in app.js")

# 6. Check style.css
with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\css\style.css', 'r', encoding='utf-8') as fp:
    css = fp.read()

if ".video-native-player" not in css:
    errors.append(".video-native-player not found in style.css")
if ".fashion-subscribe-btn" not in css:
    errors.append(".fashion-subscribe-btn not found in style.css")

print("\n--- RESULTS ---")
if errors:
    print(f"FAILED with {len(errors)} error(s):")
    for e in errors:
        print("  -", e)
else:
    print("ALL 8 VERIFICATION CHECKS PASSED WITH 100% SUCCESS!")
