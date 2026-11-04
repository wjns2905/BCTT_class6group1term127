with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

target = """.fashion-nav {
  display: flex;
  align-items: center;
  gap: 2rem;
}
.fashion-nav .nav-item {
  font-family: var(--font-sans);
  font-size: 0.9375rem;
  font-weight: 500;
  color: var(--color-text-headline);
  text-decoration: none;
  position: relative;
  padding: 0.4rem 0;
  transition: color var(--duration-fast) var(--ease-spring);
}
.fashion-nav .nav-item:hover,
.fashion-nav .nav-item.active {
  color: var(--color-brand-primary);
  font-weight: 600;
}
.fashion-nav .nav-item.active::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: var(--color-brand-primary);
  border-radius: 2px;
}"""

replacement = """.fashion-nav {
  display: flex;
  align-items: center;
  gap: 2.25rem;
}
.fashion-nav .nav-item {
  font-family: var(--font-sans);
  font-size: 0.975rem;
  font-weight: 500;
  color: var(--color-text-headline);
  text-decoration: none;
  position: relative;
  padding: 0.5rem 0;
  letter-spacing: -0.01em;
  transition: color var(--duration-fast) var(--ease-spring);
}
.fashion-nav .nav-item:hover {
  color: var(--color-brand-primary);
}
.fashion-nav .nav-item.active {
  color: var(--color-brand-primary);
  font-weight: 700;
}
.fashion-nav .nav-item.active::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 0;
  width: 100%;
  height: 2.5px;
  background-color: var(--color-brand-primary);
  border-radius: 2px;
}"""

norm_css = css.replace("\r\n", "\n")
norm_target = target.replace("\r\n", "\n")
norm_rep = replacement.replace("\r\n", "\n")

if norm_target in norm_css:
    norm_css = norm_css.replace(norm_target, norm_rep, 1)
    with open("css/style.css", "w", encoding="utf-8") as f:
        f.write(norm_css)
    print("Nav styling updated to match mockup perfectly!")
else:
    print("Could not find nav target in css/style.css")
