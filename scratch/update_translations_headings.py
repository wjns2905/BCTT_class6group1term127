import re

path = 'C:/Users/camka/OneDrive/Desktop/BCTT_class6group1term127/js/translations.js'
with open(path, 'r', encoding='utf-8') as f:
    code = f.read()

# Add to vi
vi_addition = '''    cat_heading_trending: "XU HƯỚNG.",
    cat_heading_society: "XÃ HỘI.",
    cat_heading_human: "CÂU CHUYỆN NHÂN VĂN.",
    cat_heading_mind: "TÂM HỒN & TRÍ TUỆ.",
    cat_heading_indepth: "CHUYÊN SÂU.",
    breadcrumb_home: "Trang chủ",
'''

# Add to en
en_addition = '''    cat_heading_trending: "TRENDING.",
    cat_heading_society: "SOCIETY.",
    cat_heading_human: "HUMAN STORIES.",
    cat_heading_mind: "MIND & SOUL.",
    cat_heading_indepth: "IN-DEPTH.",
    breadcrumb_home: "Home",
'''

# Insert in vi before cat_feat_trending_kicker
if 'cat_heading_trending' not in code:
    code = code.replace('cat_feat_trending_kicker:', vi_addition + '    cat_feat_trending_kicker:', 1)
    # Then for second occurrence (in en)
    code = code.replace('cat_feat_trending_kicker:', en_addition + '    cat_feat_trending_kicker:', 1)
    print("Added heading keys to translations.js")
else:
    print("Heading keys already exist")

with open(path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated translations.js successfully")
