with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

target1 = """  /* Authentic Editorial Newspaper Typography (Georgia from Article 2 & Newsreader) */
  --font-serif: 'Newsreader', Georgia, 'Times New Roman', serif;
  --font-body: Georgia, 'Newsreader', 'Times New Roman', serif;
  --font-sans: 'Source Sans 3', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  --font-mono: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;"""

rep1 = """  /* Modern Minimalist Typography System (Inter & Plus Jakarta Sans) */
  --font-serif: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-sans: 'Inter', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;"""

target2 = """.fashion-brand-logo {
  font-family: var(--font-editorial);
  font-size: 2.15rem;
  font-weight: 800;
  font-style: italic;
  color: var(--color-brand-primary);
  text-decoration: none;
  letter-spacing: -0.02em;
  display: inline-flex;
  align-items: baseline;
  transition: opacity var(--duration-fast) var(--ease-spring);
}"""

rep2 = """.fashion-brand-logo {
  font-family: var(--font-editorial);
  font-size: 2.15rem;
  font-weight: 900;
  font-style: normal;
  color: var(--color-brand-primary);
  text-decoration: none;
  letter-spacing: -0.04em;
  display: inline-flex;
  align-items: baseline;
  transition: opacity var(--duration-fast) var(--ease-spring);
}"""

target3 = """.fashion-footer-logo {
  font-family: var(--font-editorial);
  font-size: 1.85rem;
  font-weight: 800;
  font-style: italic;
  color: var(--color-brand-primary);
  display: block;
  margin-bottom: 0.5rem;
}"""

rep3 = """.fashion-footer-logo {
  font-family: var(--font-editorial);
  font-size: 2rem;
  font-weight: 900;
  font-style: normal;
  letter-spacing: -0.04em;
  color: var(--color-brand-primary);
  display: block;
  margin-bottom: 0.5rem;
}"""

norm_css = css.replace("\r\n", "\n")
subs = [
    (target1, rep1),
    (target2, rep2),
    (target3, rep3)
]

applied = 0
for t, r in subs:
    nt = t.replace("\r\n", "\n")
    nr = r.replace("\r\n", "\n")
    if nt in norm_css:
        norm_css = norm_css.replace(nt, nr, 1)
        applied += 1
    else:
        print(f"FAILED on block: {t[:35]}...")

with open("css/style.css", "w", encoding="utf-8") as f:
    f.write(norm_css)

print(f"Applied {applied}/{len(subs)} minimalist font styles to style.css!")
