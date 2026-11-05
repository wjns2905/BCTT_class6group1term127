import os
import re

base_dir = 'C:/Users/camka/OneDrive/Desktop/BCTT_class6group1term127'

cat_configs = {
    'trending.html': {
        'nav_key': 'nav_trending',
        'heading_key': 'cat_heading_trending',
        'heading_text': 'TRENDING.',
        'desc_key': 'trending_desc',
        'desc_en': 'Cultural pulses, viral trends, and contemporary social movements.',
        'feat_excerpt_key': 'cat_feat_trending_excerpt',
        'feat_excerpt_en': 'The heavy carrying poles bearing daily livelihoods, rustic labor beauty, and mossy heritage memories across ancient alleys portrayed through VnExpress journalism.'
    },
    'society.html': {
        'nav_key': 'nav_society',
        'heading_key': 'cat_heading_society',
        'heading_text': 'SOCIETY.',
        'desc_key': 'society_desc',
        'desc_en': 'Civic livelihoods, international study policies, cost-of-living resilience, and grassroots solidarity.',
        'feat_excerpt_key': 'cat_feat_society_excerpt',
        'feat_excerpt_en': 'The Vale Pantry community shop in Dorset and initiatives giving 3 million pairs of shoes to underprivileged children redefine charitable giving: uplifting communities while honoring self-dignity.'
    },
    'human-stories.html': {
        'nav_key': 'nav_human_stories',
        'heading_key': 'cat_heading_human',
        'heading_text': 'HUMAN STORIES.',
        'desc_key': 'human_desc',
        'desc_en': 'Unforgettable lives, extraordinary courage, and heartwarming acts of kindness that restore faith in humanity.',
        'feat_excerpt_key': 'cat_feat_human_excerpt',
        'feat_excerpt_en': 'Miraculously surviving a devastating bombing and losing his eyesight, Qusay Hussein alongside extraordinary figures share near-death turning points that reshaped their lives forever.'
    },
    'mind-soul.html': {
        'nav_key': 'nav_mind_soul',
        'heading_key': 'cat_heading_mind',
        'heading_text': 'MIND &amp; SOUL.',
        'desc_key': 'mind_desc',
        'desc_en': 'Nurturing inner peace, slow living, holistic wellbeing, and cultural heritage.',
        'feat_excerpt_key': 'cat_feat_mind_excerpt',
        'feat_excerpt_en': 'The acclaimed Korean artist expresses deep gratitude to Vietnamese fans after two sensational nights of his 20th-anniversary tour in Hanoi.'
    },
    'in-depth.html': {
        'nav_key': 'nav_indepth',
        'heading_key': 'cat_heading_indepth',
        'heading_text': 'IN-DEPTH.',
        'desc_key': 'indepth_desc',
        'desc_en': 'Longform investigative features, multimedia cultural essays, and diplomatic scholarly analyses.',
        'feat_excerpt_key': 'cat_feat_indepth_excerpt',
        'feat_excerpt_en': 'The poignant fragrance of milk flowers in October is not simply a matter of personal fragrance preference, but an enduring mirror reflecting the heartbeat of a Hanoi that never stands still.'
    },
    'about.html': {
        'nav_key': 'nav_about',
        'heading_key': 'nav_about',
        'heading_text': 'ABOUT HEARTICLES.',
        'desc_key': 'about_hero_sub',
        'desc_en': '"Where News Begins with a Heartbeat - Where journalism springs from empathy and human connection."',
        'feat_excerpt_key': None,
        'feat_excerpt_en': None
    }
}

# 1. Update index.html header pill
index_path = os.path.join(base_dir, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

index_html = index_html.replace(
    '<div class="lang-switch-pill" style="display:none !important;" role="group" aria-label="Language Selector">',
    '<div class="lang-switch-pill" role="group" aria-label="Language Selector">'
)
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_html)
print('Updated index.html header lang-switch-pill')

# 2. Update all category pages
for fname, conf in cat_configs.items():
    fpath = os.path.join(base_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Unhide header lang-switch-pill
    html = html.replace(
        '<div class="lang-switch-pill" style="display:none !important;" role="group" aria-label="Language Selector">',
        '<div class="lang-switch-pill" role="group" aria-label="Language Selector">'
    )

    # Hero breadcrumb + lang switch row replacement
    hero_header_row = f'''      <div class="category-hero-header-row" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.75rem;">
        <div class="category-breadcrumb">
          <a href="index.html" data-i18n="nav_home">Home</a> <span>/</span> <span data-i18n="{conf['nav_key']}">{conf['nav_key'].replace('nav_', '').replace('_', ' ').title()}</span>
        </div>
        <div class="lang-switch-pill" role="group" aria-label="Language Selector">
          <button class="lang-pill-btn" data-lang="vi" onclick="setLanguage('vi')">VI</button>
          <span class="lang-pill-divider">/</span>
          <button class="lang-pill-btn active" data-lang="en" onclick="setLanguage('en')">EN</button>
        </div>
      </div>'''

    # Replace breadcrumb block inside category-page-hero
    breadcrumb_pattern = r'<div class="category-breadcrumb">[\s\S]*?</div>'
    if '<div class="category-hero-header-row"' not in html:
        html = re.sub(breadcrumb_pattern, hero_header_row, html, count=1)
        print(f'Added hero lang switch row to {fname}')

    # Update category-page-title
    old_h1_pattern = rf'<h1 class="category-page-title"[^>]*>[\s\S]*?</h1>'
    new_h1 = f'<h1 class="category-page-title" data-i18n="{conf["heading_key"]}">{conf["heading_text"]}</h1>'
    html = re.sub(old_h1_pattern, new_h1, html, count=1)

    # Update category-page-desc static English
    old_desc_pattern = rf'<p class="category-page-desc" data-i18n="{conf["desc_key"]}">[\s\S]*?</p>'
    new_desc = f'<p class="category-page-desc" data-i18n="{conf["desc_key"]}">\n        {conf["desc_en"]}\n      </p>'
    html = re.sub(old_desc_pattern, new_desc, html, count=1)

    # Update featured excerpt if applicable
    if conf['feat_excerpt_key']:
        old_excerpt_pattern = rf'<p class="category-featured-excerpt" data-i18n="{conf["feat_excerpt_key"]}">[\s\S]*?</p>'
        new_excerpt = f'<p class="category-featured-excerpt" data-i18n="{conf["feat_excerpt_key"]}">\n          {conf["feat_excerpt_en"]}\n        </p>'
        html = re.sub(old_excerpt_pattern, new_excerpt, html, count=1)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Updated {fname} successfully')

print('All HTML pages updated successfully.')
