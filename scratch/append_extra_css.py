# -*- coding: utf-8 -*-
import os

target = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\css\style.css"

extra_css = """
/* ===================================================================
   HEADER EMAIL PILL & ABOUT US SECTION ENHANCEMENTS
   =================================================================== */
.header-email-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.35rem 0.85rem;
  background: var(--color-surface-blush, #FBF3F4);
  border: 1px solid var(--color-border-hairline, rgba(84, 17, 30, 0.12));
  border-radius: var(--radius-full, 9999px);
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--color-brand-primary, #54111E);
  text-decoration: none;
  transition: all var(--duration-fast, 0.2s);
}
.header-email-pill:hover {
  background: #FFFFFF;
  border-color: var(--color-brand-primary, #54111E);
  box-shadow: 0 2px 8px rgba(84, 17, 30, 0.15);
  transform: translateY(-1px);
}
@media (max-width: 900px) {
  .header-email-pill {
    display: none;
  }
}

/* About Us Section Tabs & Galleries */
.about-tabs-nav {
  display: flex;
  gap: 0.75rem;
  margin-bottom: 2rem;
  border-bottom: 2px solid var(--color-border-hairline, rgba(84, 17, 30, 0.1));
  padding-bottom: 0.5rem;
  overflow-x: auto;
}
.about-tab-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.6rem 1.25rem;
  font-size: 0.875rem;
  font-weight: 700;
  color: var(--color-text-body, #4A4036);
  background: transparent;
  border: none;
  border-radius: var(--radius-md, 8px);
  cursor: pointer;
  text-decoration: none;
  transition: all var(--duration-fast, 0.2s);
}
.about-tab-btn:hover {
  background: var(--color-surface-blush, #FBF3F4);
  color: var(--color-brand-primary, #54111E);
}
.about-tab-btn.active {
  background: var(--color-brand-primary, #54111E);
  color: #FFFFFF;
}

.about-photo-mosaic-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}
.about-photo-item {
  position: relative;
  border-radius: var(--radius-md, 8px);
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
  background: #FFF;
  cursor: pointer;
  transition: transform var(--duration-fast, 0.2s), box-shadow var(--duration-fast, 0.2s);
}
.about-photo-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(84, 17, 30, 0.14);
}
.about-photo-img {
  width: 100%;
  aspect-ratio: 16 / 10;
  object-fit: cover;
  display: block;
}
.about-photo-caption {
  padding: 1rem;
}
.about-photo-caption h4 {
  font-family: var(--font-editorial);
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--color-text-headline, #141011);
  margin-bottom: 0.25rem;
}
.about-photo-caption p {
  font-size: 0.8rem;
  color: var(--color-text-muted, #7A6F68);
  margin: 0;
}

/* Subscribe card on About page */
.about-subscribe-card {
  background: linear-gradient(135deg, #FFFDFD 0%, #FDF4F5 100%);
  border: 1px solid rgba(84, 17, 30, 0.15);
  border-radius: var(--radius-lg, 12px);
  padding: 2.5rem 2rem;
  text-align: center;
  max-width: 680px;
  margin: 2rem auto;
}
"""

with open(target, 'r', encoding='utf-8') as f:
    cur = f.read()

if 'header-email-pill' not in cur:
    cur += '\n' + extra_css
    with open(target, 'w', encoding='utf-8') as f:
        f.write(cur)
    print("SUCCESS: Appended extra_css to style.css!")
else:
    print("extra_css already in style.css.")
