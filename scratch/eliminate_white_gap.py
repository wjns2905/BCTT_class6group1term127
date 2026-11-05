import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace masthead styling
old_block = """/* ===================================================================
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
  max-height: 145px;
  object-fit: contain;
  display: block;
}

@media (max-width: 768px) {
  .fashion-brand-logo-fullsize {
    max-width: 310px;
    max-height: 145px;
  }
  .fashion-masthead-hero {
    padding: 0 0.5rem 0.35rem 0.5rem;
  }
}"""

new_block = """/* ===================================================================
   FULL-SIZE CENTERED BRAND MASTHEAD (EDITORIAL LOGO BANNER)
   =================================================================== */
.fashion-masthead-hero {
  background: #FFFFFF;
  padding: 0;
  margin: 0;
  text-align: center;
  border-bottom: 1px solid var(--color-border-hairline);
  position: relative;
  overflow: hidden;
  line-height: 0;
}
.masthead-hero-inner {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0;
  margin: 0;
  line-height: 0;
}
.fashion-brand-logo-masthead {
  display: block;
  text-decoration: none;
  line-height: 0;
  transition: transform var(--duration-fast) var(--ease-spring);
}
.fashion-brand-logo-masthead:hover {
  transform: scale(1.015);
}
.fashion-brand-logo-fullsize {
  max-width: 580px;
  width: 100%;
  height: auto;
  max-height: 145px;
  object-fit: contain;
  display: block;
  margin: 0 auto;
}

@media (max-width: 768px) {
  .fashion-brand-logo-fullsize {
    max-width: 310px;
    max-height: 145px;
  }
  .fashion-masthead-hero {
    padding: 0;
  }
}"""

if old_block in text:
    text = text.replace(old_block, new_block)
    print("✓ Replaced masthead block cleanly!")
else:
    print("Target block not exact match, using regex...")
    text = re.sub(
        r'/\* =+\s*FULL-SIZE CENTERED BRAND MASTHEAD.*?@media[^{]*\{[^}]*\}',
        new_block,
        text,
        flags=re.DOTALL
    )
    print("✓ Replaced via regex!")

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved css/style.css successfully!")
