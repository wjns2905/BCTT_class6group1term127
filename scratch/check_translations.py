import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/translations.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Check keys related to cat_feat
for line in text.splitlines():
    if 'cat_feat' in line or 'trending_desc' in line or 'society_desc' in line:
        print(line[:100])
