# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

extra_css = """
/* ===================================================================
   ACADEMIC EMAIL & GROUP INFO LINK
   =================================================================== */
.academic-email-link {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--color-brand-primary);
  text-decoration: none;
  background: rgba(84, 17, 30, 0.08);
  padding: 3px 10px;
  border-radius: var(--radius-full);
  transition: all var(--duration-fast);
  border: 1px solid rgba(84, 17, 30, 0.15);
}
.academic-email-link:hover {
  background: var(--color-brand-primary);
  color: #FFFFFF;
  box-shadow: 0 1px 4px rgba(84, 17, 30, 0.25);
}
@media (max-width: 900px) {
  .academic-email-link {
    display: none;
  }
}
"""

if '.academic-email-link' not in css:
    css += extra_css
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Added .academic-email-link to css/style.css!")
else:
    print(".academic-email-link already in css/style.css")
