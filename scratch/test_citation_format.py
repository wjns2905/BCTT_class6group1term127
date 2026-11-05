import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
e = c.rfind('];') + 1

articles = json.loads(c[s:e])

def format_date_clean(d, is_en):
    if not d:
        return '2026'
    # strip time after ' - '
    d_clean = d.split(' - ')[0].strip()
    # strip day of week
    d_clean = re.sub(r'^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),\s*', '', d_clean, flags=re.I)
    
    # If Vietnamese format needed: convert Month Name YYYY to DD tháng MM, YYYY
    months_en = {
        'January': 'Tháng 1', 'February': 'Tháng 2', 'March': 'Tháng 3',
        'April': 'Tháng 4', 'May': 'Tháng 5', 'June': 'Tháng 6',
        'July': 'Tháng 7', 'August': 'Tháng 8', 'September': 'Tháng 9',
        'October': 'Tháng 10', 'November': 'Tháng 11', 'December': 'Tháng 12'
    }
    if not is_en:
        # e.g. "October 31, 2026" -> "31 Tháng 10, 2026"
        m = re.match(r'([A-Za-z]+)\s+(\d{1,2}),?\s+(\d{4})', d_clean)
        if m:
            month_name = m.group(1)
            day = m.group(2)
            year = m.group(3)
            vn_month = months_en.get(month_name, month_name)
            return f"ngày {day} {vn_month.lower()} năm {year}"
    return d_clean

for a in articles[:5]:
    title_vi = a.get('title', '')
    title_en = a.get('title_en', title_vi)
    author = a.get('author', '').split('•')[0].strip()
    source = a.get('sourceName', 'HEARTICLES.')
    url = a.get('sourceUrl', '#')
    
    date_en = format_date_clean(a.get('date'), True)
    date_vi = format_date_clean(a.get('date'), False)
    
    vi_citation = f'Source: "{title_vi}", {source}, viết bởi {author}, {date_vi}, {url}'
    en_citation = f'Source: "{title_en}", {source}, by {author}, {date_en}, {url}'
    
    print("--- VI ---")
    print(vi_citation)
    print("--- EN ---")
    print(en_citation)
    print()
