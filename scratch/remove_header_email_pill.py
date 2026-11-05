# -*- coding: utf-8 -*-
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

root_dir = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127"
html_files = [
    "index.html", "about.html", "trending.html", "society.html",
    "human-stories.html", "mind-soul.html", "in-depth.html"
]

pattern = re.compile(
    r'\s*<!--\s*Email Pill[^-]*-->\s*<a href="mailto:class6group1term127@gmail\.com"[^>]*>.*?</a>',
    re.DOTALL
)

for f in html_files:
    fp = os.path.join(root_dir, f)
    if os.path.exists(fp):
        with open(fp, "r", encoding="utf-8") as fl:
            content = fl.read()
        
        new_content, count = pattern.subn("", content)
        if count == 0:
            # Fallback broader pattern matching just the header-email-pill anchor tag
            broad_pattern = re.compile(r'\s*<a href="mailto:class6group1term127@gmail\.com"\s+class="header-email-pill"[^>]*>.*?</a>', re.DOTALL)
            new_content, count = broad_pattern.subn("", content)
            
        with open(fp, "w", encoding="utf-8") as fl:
            fl.write(new_content)
        print(f"File {f}: removed {count} header email pill instances")

print("Finished removing header email pills.")
