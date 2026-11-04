# -*- coding: utf-8 -*-
import os, re

target_dir = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127"
html_files = [
    "index.html", "trending.html", "society.html",
    "human-stories.html", "mind-soul.html", "in-depth.html", "about.html"
]

pattern = re.compile(
    r'[ \t]*<!-- Email Pill.*?-->\s*'
    r'[ \t]*<a\s+href="mailto:class6group1term127@gmail\.com"\s+class="header-email-pill"[^>]*>.*?'
    r'</a>\s*',
    re.DOTALL
)

for f in html_files:
    p = os.path.join(target_dir, f)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Remove any lingering partial lines from index.html if present
        content = re.sub(r'[ \t]*<!-- Email Pill.*?-->\s*', '', content)
        content = re.sub(
            r'[ \t]*<a\s+href="mailto:class6group1term127@gmail\.com"\s+class="header-email-pill"[^>]*>[\s\S]*?</a>\s*',
            '',
            content
        )
        # Also clean up index.html if lines were left from previous edit
        content = re.sub(r'[ \t]*<i class="fas fa-envelope"></i>\s*<span>class6group1term127@gmail\.com</span>\s*</a>\s*', '', content)
        
        with open(p, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Cleaned header email from {f}!")

# Also update build_multi_pages_updated.py so future runs don't include it in header
build_script = os.path.join(target_dir, "scratch", "build_multi_pages_updated.py")
if os.path.exists(build_script):
    with open(build_script, 'r', encoding='utf-8') as file:
        code = file.read()
    
    code = re.sub(
        r'        <!-- Email Pill as requested -->\s*<a href="mailto:class6group1term127@gmail\.com" class="header-email-pill" title="Email Tòa soạn">\s*<i class="fas fa-envelope"></i>\s*<span>class6group1term127@gmail\.com</span>\s*</a>\s*',
        '',
        code
    )
    with open(build_script, 'w', encoding='utf-8') as file:
        file.write(code)
    print("Updated build_multi_pages_updated.py!")

print("All done!")
