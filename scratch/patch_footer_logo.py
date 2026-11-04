with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

target = """.fashion-footer-logo {
  font-family: var(--font-editorial);
  font-size: 2.25rem;
  font-weight: 800;
  font-style: italic;
  color: var(--color-brand-primary);
  display: block;"""

rep = """.fashion-footer-logo {
  font-family: var(--font-editorial);
  font-size: 2.25rem;
  font-weight: 900;
  font-style: normal;
  letter-spacing: -0.04em;
  color: var(--color-brand-primary);
  display: block;"""

norm_css = css.replace("\r\n", "\n")
norm_target = target.replace("\r\n", "\n")
norm_rep = rep.replace("\r\n", "\n")

if norm_target in norm_css:
    norm_css = norm_css.replace(norm_target, norm_rep, 1)
    with open("css/style.css", "w", encoding="utf-8") as f:
        f.write(norm_css)
    print("Updated fashion-footer-logo successfully!")
else:
    print("Could not match fashion-footer-logo")
