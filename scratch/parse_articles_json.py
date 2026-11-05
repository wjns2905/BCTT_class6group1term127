# -*- coding: utf-8 -*-
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\data.js", "r", encoding="utf-8") as f:
    text = f.read()

# Load as JS/JSON if possible, or parse objects
# Find all objects in ARTICLES_DATA
start = text.find("const ARTICLES_DATA = [") + len("const ARTICLES_DATA = [")
end = text.rfind("];")
json_str = text[start:end].strip()

# Let's parse with a simple python regex or json parser
# Since JS objects might be standard JSON
try:
    articles = json.loads("[" + json_str + "]")
    print(f"Successfully parsed {len(articles)} articles via json.loads")
except Exception as e:
    print(f"json.loads failed: {e}, falling back to regex")
    # Let's inspect why json.loads failed
