# -*- coding: utf-8 -*-
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Import prepared new articles
from prepare_new_articles import new_articles

data_js_path = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\data.js"
with open(data_js_path, "r", encoding="utf-8") as f:
    js_text = f.read()

# Check which new articles are not yet in data.js by id
for art in new_articles:
    if f'"{art["id"]}"' in js_text:
        print(f"Article {art['id']} already in data.js, skipping or replacing")
    else:
        # Insert before closing bracket of ARTICLES_DATA array: "];"
        # Find the last occurrence of "];"
        last_bracket = js_text.rfind("];")
        if last_bracket != -1:
            art_json = json.dumps(art, indent=2, ensure_ascii=False)
            # Indent each line
            indented = ",\n  " + art_json.replace("\n", "\n  ")
            js_text = js_text[:last_bracket] + indented + "\n" + js_text[last_bracket:]
            print(f"Inserted new article: {art['id']} - {art['title'][:50]}")

with open(data_js_path, "w", encoding="utf-8") as f:
    f.write(js_text)

print("Updated data.js with new authentic articles from updated Word docs.")
