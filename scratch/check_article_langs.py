import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("js/data.js", "r", encoding="utf-8") as f:
    text = f.read()

m = re.search(r'const ARTICLES_DATA\s*=\s*(\[\s*\{.*\}\s*\]);', text, re.DOTALL)
articles = json.loads(m.group(1))

print(f"Total articles: {len(articles)}")
for a in articles:
    # Check if title has Vietnamese marks
    has_vn = any(c in a['title'] for c in 'àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđĐ')
    lang = "VI" if has_vn else "EN"
    print(f"[{lang}] {a['id']}: {a['title'][:60]}")
