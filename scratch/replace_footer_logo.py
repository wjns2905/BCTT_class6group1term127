import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

footer_logo_css = """
.fashion-footer-logo-link {
  display: inline-block;
  text-decoration: none;
  margin-bottom: 0.75rem;
  transition: opacity var(--duration-fast, 0.2s);
}
.fashion-footer-logo-link:hover {
  opacity: 0.9;
}
.fashion-footer-logo-img {
  max-width: 290px;
  width: 100%;
  height: auto;
  max-height: 85px;
  object-fit: contain;
  display: block;
}
"""

if '.fashion-footer-logo-img' not in css:
    css = css.replace('.fashion-footer-logo {', footer_logo_css + '\n.fashion-footer-logo {')
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("✓ Added .fashion-footer-logo-img CSS to css/style.css!")
else:
    print(".fashion-footer-logo-img already in css/style.css")

# 2. Update all 7 HTML files
html_files = [
    'index.html',
    'trending.html',
    'society.html',
    'human-stories.html',
    'mind-soul.html',
    'in-depth.html',
    'about.html'
]

old_tag = '<span class="fashion-footer-logo">HEARTICLES<span class="fashion-brand-period">.</span></span>'
new_tag = """<a href="index.html" class="fashion-footer-logo-link" aria-label="HEARTICLES. - Trang chủ">
            <img src="assets/images/logo/brand_logo_updated.png" alt="HEARTICLES." class="fashion-footer-logo-img">
          </a>"""

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    if old_tag in html:
        html = html.replace(old_tag, new_tag)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✓ Replaced footer text with full logo in {fpath}!")
    else:
        print(f"Old tag not found in {fpath}")

print("\nDone updating footer logo across all pages!")
