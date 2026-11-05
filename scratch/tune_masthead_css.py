import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace padding in .fashion-masthead-hero
target = """/* ===================================================================
   FULL-SIZE CENTERED BRAND MASTHEAD (EDITORIAL LOGO BANNER)
   =================================================================== */
.fashion-masthead-hero {
  background: #FFFFFF;
  padding: 1.35rem 1rem 1.05rem 1rem;
  margin: 0;
  text-align: center;
  border-bottom: 1px solid var(--color-border-hairline);
  position: relative;
  overflow: hidden;
}"""

replacement = """/* ===================================================================
   FULL-SIZE CENTERED BRAND MASTHEAD (EDITORIAL LOGO BANNER)
   =================================================================== */
.fashion-masthead-hero {
  background: #FFFFFF;
  padding: 0 1rem 0.5rem 1rem;
  margin: 0;
  text-align: center;
  border-bottom: 1px solid var(--color-border-hairline);
  position: relative;
  overflow: hidden;
}"""

target_mobile = """  .fashion-masthead-hero {
    padding: 0.85rem 0.5rem 0.65rem 0.5rem;
  }"""

replacement_mobile = """  .fashion-masthead-hero {
    padding: 0 0.5rem 0.35rem 0.5rem;
  }"""

if target in text:
    text = text.replace(target, replacement)
    print("✓ Replaced desktop padding in .fashion-masthead-hero!")
else:
    text = re.sub(
        r'(\.fashion-masthead-hero\s*\{[^}]*padding:\s*)[^;]+;',
        r'\g<1>0 1rem 0.5rem 1rem;',
        text
    )
    print("✓ Replaced desktop padding via regex!")

if target_mobile in text:
    text = text.replace(target_mobile, replacement_mobile)
    print("✓ Replaced mobile padding in .fashion-masthead-hero!")
else:
    text = re.sub(
        r'(@media\s*\([^)]*768px\)[^{]*\{[^}]*\.fashion-masthead-hero\s*\{[^}]*padding:\s*)[^;]+;',
        r'\g<1>0 0.5rem 0.35rem 0.5rem;',
        text
    )
    print("✓ Replaced mobile padding via regex!")

# Make sure .fashion-brand-logo-fullsize has max-height: 145px;
text = re.sub(
    r'(\.fashion-brand-logo-fullsize\s*\{[^}]*max-height:\s*)[^;]+;',
    r'\g<1>145px;',
    text
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved css/style.css successfully!")
