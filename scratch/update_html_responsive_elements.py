import os
import re

base_dir = 'C:/Users/camka/OneDrive/Desktop/BCTT_class6group1term127'
html_files = {
    'index.html': 'home',
    'trending.html': 'trending',
    'society.html': 'society',
    'human-stories.html': 'human',
    'mind-soul.html': 'mind',
    'in-depth.html': 'indepth',
    'about.html': 'about'
}

for fname, page_type in html_files.items():
    fpath = os.path.join(base_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update viewport meta tag with viewport-fit=cover
    html = re.sub(
        r'<meta name="viewport" content="width=device-width, initial-scale=1\.0">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">',
        html
    )

    # 2. Add mobile brand sticky link inside fashion-header-container if not present
    mobile_brand_tag = '      <!-- Mobile Sticky Nav Brand Mark -->\n      <a href="index.html" class="fashion-mobile-brand" aria-label="HEARTICLES. - Home">HEARTICLES.</a>\n'
    if 'class="fashion-mobile-brand"' not in html:
        html = re.sub(
            r'(<div class="container fashion-header-container">\s*)',
            r'\1' + mobile_brand_tag,
            html,
            count=1
        )
        print(f"Added mobile brand to {fname}")

    # 3. Update mobile bottom dock with active states and data-i18n
    active_home = 'active' if page_type == 'home' else ''
    active_trending = 'active' if page_type == 'trending' else ''
    active_human = 'active' if page_type == 'human' else ''

    dock_replacement = f'''  <!-- MOBILE BOTTOM DOCK -->
  <nav class="mobile-bottom-dock" aria-label="Quick mobile navigation">
    <a href="index.html" class="dock-btn {active_home}">
      <i class="fas fa-home"></i>
      <span data-i18n="nav_home">Home</span>
    </a>
    <a href="trending.html" class="dock-btn {active_trending}">
      <i class="fas fa-fire"></i>
      <span data-i18n="nav_trending">Trending</span>
    </a>
    <a href="human-stories.html" class="dock-btn {active_human}">
      <i class="fas fa-heart"></i>
      <span data-i18n="nav_human_stories">Human</span>
    </a>
    <a href="javascript:void(0)" class="dock-btn" onclick="openSearchModal()">
      <i class="fas fa-search"></i>
      <span data-i18n="dock_search">Search</span>
    </a>
    <a href="javascript:void(0)" class="dock-btn" onclick="openDrawer()">
      <i class="fas fa-bars"></i>
      <span data-i18n="dock_menu">Menu</span>
    </a>
  </nav>'''

    # Replace mobile dock
    dock_pattern = r'<!-- MOBILE BOTTOM DOCK -->[\s\S]*?</nav>'
    if re.search(dock_pattern, html):
        html = re.sub(dock_pattern, dock_replacement, html, count=1)
        print(f"Updated mobile dock in {fname}")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Saved {fname}")

print("All HTML files updated with responsive enhancements.")
