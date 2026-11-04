with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

lang_css = """
/* ===================================================================
   LANGUAGE SWITCHER (VI / EN) MINIMALIST STYLING
   =================================================================== */
.lang-switch-pill {
  display: inline-flex;
  align-items: center;
  background: var(--color-canvas);
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-full);
  padding: 3px 5px;
  gap: 2px;
}
.lang-pill-btn {
  background: transparent;
  border: none;
  border-radius: var(--radius-full);
  font-family: var(--font-sans);
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--color-text-muted);
  padding: 0.25rem 0.55rem;
  cursor: pointer;
  transition: all var(--duration-fast);
  line-height: 1;
}
.lang-pill-btn:hover {
  color: var(--color-brand-primary);
}
.lang-pill-btn.active {
  background: var(--color-brand-primary);
  color: #FFFFFF;
  box-shadow: 0 1px 4px rgba(84, 17, 30, 0.25);
}
.lang-pill-divider {
  font-size: 0.75rem;
  color: var(--color-border-strong);
  user-select: none;
  padding: 0 1px;
}
.drawer-lang-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.75rem 0;
  border-top: 1px solid #332B25;
  margin-top: 1rem;
}
"""

if ".lang-switch-pill" not in css:
    with open("css/style.css", "a", encoding="utf-8") as f:
        f.write(lang_css)
    print("Language switcher CSS appended to style.css!")
else:
    print("Language switcher CSS already exists in style.css")
