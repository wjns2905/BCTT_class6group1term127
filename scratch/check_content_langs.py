import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("js/data.js", "r", encoding="utf-8") as f:
    text = f.read()

m = re.search(r'const ARTICLES_DATA\s*=\s*(\[\s*\{.*\}\s*\]);', text, re.DOTALL)
articles = json.loads(m.group(1))

vn_content_ids = []
en_content_ids = []

for a in articles:
    first_p = a['content'][0] if isinstance(a['content'], list) and len(a['content']) > 0 else (a['content'] if isinstance(a['content'], str) else "")
    has_vn = any(c in first_p for c in 'àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđĐ')
    if has_vn:
        vn_content_ids.append(a['id'])
    else:
        en_content_ids.append(a['id'])

print(f"Articles with Vietnamese content: {len(vn_content_ids)} -> {vn_content_ids}")
print(f"Articles with English content: {len(en_content_ids)} -> {en_content_ids}")
