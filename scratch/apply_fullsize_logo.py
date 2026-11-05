import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

masthead_css = """
/* ===================================================================
   FULL-SIZE CENTERED BRAND MASTHEAD (EDITORIAL LOGO BANNER)
   =================================================================== */
.fashion-masthead-hero {
  background: #FFFFFF;
  padding: 1.75rem 1rem 1.25rem 1rem;
  text-align: center;
  border-bottom: 1px solid var(--color-border-hairline);
  position: relative;
  overflow: hidden;
}
.masthead-hero-inner {
  display: flex;
  justify-content: center;
  align-items: center;
}
.fashion-brand-logo-masthead {
  display: inline-block;
  text-decoration: none;
  transition: transform var(--duration-fast) var(--ease-spring);
}
.fashion-brand-logo-masthead:hover {
  transform: scale(1.015);
}
.fashion-brand-logo-fullsize {
  max-width: 580px;
  width: 100%;
  height: auto;
  max-height: 190px;
  object-fit: contain;
  display: block;
}

@media (max-width: 768px) {
  .fashion-brand-logo-fullsize {
    max-width: 310px;
    max-height: 110px;
  }
  .fashion-masthead-hero {
    padding: 1rem 0.5rem 0.75rem 0.5rem;
  }
}
"""

if '.fashion-masthead-hero' not in css:
    css = masthead_css + "\n" + css

# Ensure .fashion-header-container height is sleeker for categories navbar (54px instead of 76px)
css = re.sub(r'(\.fashion-header-container\s*\{[^}]*height:\s*)76px;', r'\g<1>54px;', css)

# In .fashion-nav, add margin: 0 auto; to center categories
if 'margin: 0 auto;' not in css:
    css = re.sub(
        r'(\.fashion-nav\s*\{\s*display:\s*flex;\s*align-items:\s*center;\s*gap:\s*2\.25rem;)',
        r'\1\n  margin: 0 auto;',
        css
    )

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("✓ Updated css/style.css with Full-Size Brand Masthead!")

# 2. Update all 7 HTML pages
html_files = [
    'index.html',
    'trending.html',
    'society.html',
    'human-stories.html',
    'mind-soul.html',
    'in-depth.html',
    'about.html'
]

masthead_html_block = """  <!-- =================================================================
       2. BRAND MASTHEAD (FULL-SIZE CENTERED EDITORIAL LOGO BANNER)
       ================================================================= -->
  <div class="fashion-masthead-hero">
    <div class="container masthead-hero-inner">
      <a href="index.html" class="fashion-brand-logo-masthead" aria-label="HEARTICLES. - Where News Begins with a Heartbeat">
        <img src="assets/images/logo/brand_logo_updated.png" alt="HEARTICLES. - Where News Begins with a Heartbeat" class="fashion-brand-logo-fullsize">
      </a>
    </div>
  </div>

  <!-- =================================================================
       3. STICKY EDITORIAL NAVIGATION (FULL-WIDTH CATEGORIES BAR)
       ================================================================= -->
  <header class="fashion-header">
    <div class="container fashion-header-container">"""

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    pattern = re.compile(
        r'(<!--\s*=+\s*2\.\s*BRAND MASTHEAD.*?-->\s*)?<header class="fashion-header">\s*<div class="container fashion-header-container">\s*(<!-- Brand Logo.*?-->\s*)?<a href="index.html" class="fashion-brand-logo"[^>]*>.*?<\/a>',
        re.DOTALL
    )

    if pattern.search(html):
        new_html = pattern.sub(masthead_html_block, html)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"✓ Replaced header with Full-Size Masthead in {fpath}!")
    else:
        print(f"Pattern not found in {fpath}, inspecting...")

print("\nDone updating all HTML files!")
