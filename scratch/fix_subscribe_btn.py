import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Fix css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove @import "tokens.css"; from line 46
css = re.sub(r'@import\s+["\']tokens\.css["\'];\s*', '', css)

# Put @import "tokens.css"; at the very top of style.css
css = '@import "tokens.css";\n\n' + css.lstrip()

# Add bulletproof fallbacks to .fashion-subscribe-btn
css = re.sub(
    r'\.fashion-subscribe-btn\s*\{[^}]*\}',
    """.fashion-subscribe-btn {
  background-color: #54111E;
  background-color: var(--color-brand-primary, #54111E);
  color: #FFFFFF !important;
  border: none;
  border-radius: var(--radius-full, 9999px);
  font-family: var(--font-sans, system-ui, -apple-system, sans-serif);
  font-size: 0.875rem;
  font-weight: 700;
  padding: 0.55rem 1.45rem;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(84, 17, 30, 0.25);
  transition: all var(--duration-fast, 0.2s) var(--ease-spring, ease);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}""",
    css
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("✓ Fixed @import position and .fashion-subscribe-btn in css/style.css!")

# 2. Add tokens.css explicitly to all 7 HTML files before style.css
html_files = [
    'index.html',
    'trending.html',
    'society.html',
    'human-stories.html',
    'mind-soul.html',
    'in-depth.html',
    'about.html'
]

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    if '<link rel="stylesheet" href="css/tokens.css">' not in html:
        html = html.replace(
            '<link rel="stylesheet" href="css/style.css">',
            '<link rel="stylesheet" href="css/tokens.css">\n  <link rel="stylesheet" href="css/style.css">'
        )
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✓ Linked tokens.css explicitly in {fpath}!")
    else:
        print(f"tokens.css already linked in {fpath}")

print("\nDone fixing signup/subscribe button!")
