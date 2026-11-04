# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/translations.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('en: {')
pos2 = text.find('// 12. Category Pages', pos)
pos3 = text.find('// 13. About Page', pos2)

en_cat_block = text[pos2:pos3]
print("Original en_cat_block:")
print(repr(en_cat_block))

new_en_cat_block = en_cat_block.rstrip() + """
    cat_feat_trending_kicker: "CATEGORY SPOTLIGHT · ARTICLE 4 TRENDING",
    cat_feat_trending_title: "Street Vendors: The Gentle Soul Across Hoi An Ancient Alleys",
    cat_feat_trending_excerpt: "The heavy carrying poles bearing daily livelihoods, rustic labor beauty, and mossy heritage memories across ancient alleys portrayed through VnExpress journalism.",
    cat_feat_society_kicker: "COMMUNITY SPOTLIGHT · THE GUARDIAN",
    cat_feat_society_title: "Cost of Living Crisis: Community Pantries Preserving Dignity",
    cat_feat_society_excerpt: "The Vale Pantry in Dorset provides affordable groceries while empowering families to choose with autonomy and dignity amid Britain\\'s cost-of-living hardships.",
    cat_feat_human_kicker: "INSPIRATIONAL STORY · ARTICLE 3 HUMAN STORIES",
    cat_feat_human_title: "“I was given a second chance at life”",
    cat_feat_human_excerpt: "The miraculous rebirth of a man who survived near-death adversity and rediscovered purpose through community compassion and devotion.",
    cat_feat_mind_kicker: "MUSIC & CULTURE · LAO DONG NEWSPAPER",
    cat_feat_mind_title: "Taeyang (BigBang) expresses deep love for pho and 'best show' at My Dinh Stadium",
    cat_feat_mind_excerpt: "BigBang lead vocalist shares heartfelt gratitude toward tens of thousands of Vietnamese fans, naming Hanoi one of the most unforgettable stages of his career.",
    cat_feat_indepth_kicker: "CULTURAL DISPATCH · VIETNAM NEWS",
    cat_feat_indepth_title: "A Hanoi that never stands still: Milk flower scent and autumn memories",
    cat_feat_indepth_excerpt: "Amid the bustling rhythm of a modern capital, the poignant scent of milk flowers along classic avenues preserves the timeless elegance and soul of thousand-year Hanoi.",
  
"""

text = text[:pos2] + new_en_cat_block + text[pos3:]
with open('js/translations.js', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated en category block in js/translations.js successfully!")
