import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

# The new pristine, symmetrical SVG with delicate heartbeat pulse
new_svg = """<svg class="fashion-slogan-heart" viewBox="0 0 80 70" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M40 22 C35 12, 22 8, 14 16 C4 26, 6 42, 40 64 C74 42, 76 26, 66 16 C58 8, 45 12, 40 22 Z" stroke="#54111E" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="rgba(84, 17, 30, 0.04)"/>
            <path d="M26 40 L33 40 L36 32 L40 48 L44 34 L47 40 L54 40" stroke="#7D1728" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>"""

html_files = [
    'index.html',
    'trending.html',
    'society.html',
    'human-stories.html',
    'mind-soul.html',
    'in-depth.html',
    'about.html'
]

pattern = re.compile(r'<svg class="fashion-slogan-heart"[^>]*>.*?<\/svg>', re.DOTALL)

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    new_html, count = pattern.subn(new_svg, html)
    if count > 0:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"✓ Replaced crooked heart SVG in {fpath} ({count} occurrence)")
    else:
        print(f"Warning: SVG not found in {fpath}")

# Update CSS for .fashion-slogan-heart
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(
    r'\.fashion-slogan-heart\s*\{[^}]*\}',
    """.fashion-slogan-heart {
  width: 56px;
  height: 50px;
  margin-bottom: 0.5rem;
  transition: transform var(--duration-fast, 0.2s) ease;
}
.fashion-slogan-heart:hover {
  transform: scale(1.08);
}""",
    css
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("✓ Updated .fashion-slogan-heart in css/style.css!")
print("\nDone fixing crooked heart graphic!")
