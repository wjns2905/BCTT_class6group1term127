with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Update root tokens in the beginning of style.css
target_root = """:root {
  --bg-cream: #FAF7F2;
  --bg-surface: #FFFFFF;
  --bg-subtle: #F5EFE6;
  --bg-card-hover: #FDFBF8;
  --bg-dark: #161412;
  --bg-dark-card: #201D1A;

  --primary-red: #8B1E2D;
  --primary-red-hover: #701420;
  --primary-dark-red: #570404;
  --accent-gold: #B38634;
  --tag-live: #C92020;

  --text-main: #141312;
  --text-secondary: #3D3934;
  --text-muted: #6B655D;
  --text-inverse: #FAF7F2;

  --border-cream: #E2D9CC;
  --border-subtle: #EBE4D8;
  --border-strong: #C7BCA9;"""

rep_root = """:root {
  --bg-cream: #FAF7F4;
  --bg-surface: #FFFFFF;
  --bg-subtle: #F5EFEA;
  --bg-card-hover: #FDFBF9;
  --bg-dark: #151011;
  --bg-dark-card: #1E1719;

  --primary-red: #54111E;
  --primary-red-hover: #420A13;
  --primary-dark-red: #2E070D;
  --accent-gold: #7D1728;
  --tag-live: #D92338;

  --text-main: #151011;
  --text-secondary: #221B1C;
  --text-muted: #4C413E;
  --text-inverse: #FFFFFF;

  --border-cream: #E8DDD7;
  --border-subtle: #E8DDD7;
  --border-strong: #D2C2B9;"""

# 2. Update fashion academic bar
target_academic = """.fashion-academic-bar {
  background: #FFFFFF;
  border-bottom: 1px solid var(--color-border-hairline);
  padding: 0.45rem 0;
  font-size: 0.75rem;
  color: var(--color-text-muted);
}"""

rep_academic = """.fashion-academic-bar {
  background: #FFFFFF;
  border-bottom: 1px solid var(--color-border-hairline);
  padding: 0.5rem 0;
  font-size: 0.8125rem;
  color: var(--color-text-body);
  font-weight: 500;
}"""

# 3. Update subscribe button
target_subscribe = """.fashion-subscribe-btn {
  background-color: var(--color-brand-accent);
  color: #FFFFFF;
  border: none;
  border-radius: var(--radius-full);
  padding: 0.5rem 1.25rem;
  font-family: var(--font-sans);
  font-size: 0.8125rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  cursor: pointer;
  transition: all var(--duration-fast) var(--ease-spring);
}
.fashion-subscribe-btn:hover {
  background-color: var(--color-brand-primary);
  transform: translateY(-1px);
}"""

rep_subscribe = """.fashion-subscribe-btn {
  background-color: var(--color-brand-primary);
  color: #FFFFFF;
  border: none;
  border-radius: var(--radius-full);
  padding: 0.55rem 1.35rem;
  font-family: var(--font-sans);
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(84, 17, 30, 0.25);
  transition: all var(--duration-fast) var(--ease-spring);
}
.fashion-subscribe-btn:hover {
  background-color: var(--color-brand-hover);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(84, 17, 30, 0.35);
}"""

# 4. Update cover card text
target_cover_text = """.fashion-kicker {
  font-family: var(--font-sans);
  font-size: 0.75rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: var(--color-brand-primary);
}
.fashion-doodle-heart {
  width: 28px;
  height: 26px;
  opacity: 0.85;
}
.fashion-headline {
  font-family: var(--font-editorial);
  font-size: 2.25rem;
  font-weight: 700;
  line-height: 1.22;
  color: var(--color-text-headline);
  margin-bottom: 1rem;
}
.fashion-italic {
  font-style: italic;
  font-weight: 400;
  color: var(--color-brand-primary);
}
.fashion-excerpt {
  font-family: var(--font-serif);
  font-size: 1.05rem;
  line-height: 1.55;
  color: var(--color-text-muted);
  margin-bottom: 1.75rem;
}"""

rep_cover_text = """.fashion-kicker {
  font-family: var(--font-sans);
  font-size: 0.775rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--color-brand-primary);
}
.fashion-doodle-heart {
  width: 28px;
  height: 26px;
  opacity: 0.95;
}
.fashion-headline {
  font-family: var(--font-editorial);
  font-size: 2.35rem;
  font-weight: 800;
  line-height: 1.22;
  color: var(--color-text-headline);
  margin-bottom: 1rem;
}
.fashion-italic {
  font-style: italic;
  font-weight: 600;
  color: var(--color-brand-primary);
}
.fashion-excerpt {
  font-family: var(--font-serif);
  font-size: 1.1rem;
  line-height: 1.65;
  color: var(--color-text-body);
  font-weight: 400;
  margin-bottom: 1.75rem;
}"""

# 5. Update latest card
target_latest = """.fashion-view-all {
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--color-text-muted);
  text-decoration: none;
  transition: color var(--duration-fast);
}
.fashion-view-all:hover {
  color: var(--color-brand-primary);
}"""

rep_latest = """.fashion-view-all {
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--color-brand-primary);
  text-decoration: none;
  transition: color var(--duration-fast);
}
.fashion-view-all:hover {
  text-decoration: underline;
}"""

target_latest_items = """.latest-kicker {
  font-size: 0.6875rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--color-brand-accent);
  display: block;
  margin-bottom: 0.25rem;
}
.latest-title {
  font-family: var(--font-serif);
  font-size: 0.9375rem;
  font-weight: 700;
  line-height: 1.35;
  color: var(--color-text-headline);
  margin-bottom: 0.25rem;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.latest-meta {
  font-size: 0.75rem;
  color: var(--color-text-muted);
}"""

rep_latest_items = """.latest-kicker {
  font-size: 0.725rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--color-brand-accent);
  display: block;
  margin-bottom: 0.25rem;
}
.latest-title {
  font-family: var(--font-serif);
  font-size: 0.975rem;
  font-weight: 700;
  line-height: 1.4;
  color: var(--color-text-headline);
  margin-bottom: 0.35rem;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.latest-meta {
  font-size: 0.8rem;
  color: var(--color-text-muted);
  font-weight: 600;
}"""

# 6. Update secondary bento row
target_bento = """.bento-kicker {
  font-size: 0.75rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--color-text-headline);
  display: block;
  margin-bottom: 0.35rem;
}
.bento-sub {
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  line-height: 1.4;
}"""

rep_bento = """.bento-kicker {
  font-size: 0.775rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--color-brand-primary);
  display: block;
  margin-bottom: 0.4rem;
}
.bento-sub {
  font-size: 0.9rem;
  color: var(--color-text-body);
  font-weight: 600;
  line-height: 1.45;
}"""

target_her_voice = """.bento-her-voice {
  background: linear-gradient(135deg, #FCF4F5 0%, #F6E6E8 100%);
  border-color: #EED8DC;
  position: relative;
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  align-items: center;
  gap: 1rem;
}
.bento-her-voice .bento-kicker {
  color: var(--color-brand-primary);
}
.bento-headline {
  font-family: var(--font-editorial);
  font-size: 1.35rem;
  font-weight: 700;
  line-height: 1.25;
  color: var(--color-text-headline);
  margin-bottom: 0.5rem;
}
.bento-excerpt {
  font-size: 0.8125rem;
  color: var(--color-charcoal-600);
  line-height: 1.45;
  margin-bottom: 1rem;
}"""

rep_her_voice = """.bento-her-voice {
  background: linear-gradient(135deg, #FCF4F6 0%, #F6E6E9 100%);
  border-color: #E6D2D6;
  position: relative;
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  align-items: center;
  gap: 1rem;
}
.bento-her-voice .bento-kicker {
  color: var(--color-brand-primary);
  font-weight: 800;
}
.bento-headline {
  font-family: var(--font-editorial);
  font-size: 1.4rem;
  font-weight: 800;
  line-height: 1.25;
  color: var(--color-text-headline);
  margin-bottom: 0.5rem;
}
.bento-excerpt {
  font-size: 0.875rem;
  color: var(--color-text-body);
  font-weight: 500;
  line-height: 1.5;
  margin-bottom: 1rem;
}"""

# 7. Update section titles & filter pills
target_section = """.fashion-section-sub {
  font-size: 0.875rem;
  color: var(--color-text-muted);
}
.fashion-filter-pills {
  display: flex;
  gap: 0.5rem;
  overflow-x: auto;
  padding-bottom: 0.25rem;
}
.fashion-filter-pill {
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-full);
  padding: 0.45rem 1.1rem;
  font-family: var(--font-sans);
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--color-text-headline);
  cursor: pointer;
  white-space: nowrap;
  transition: all var(--duration-fast);
}
.fashion-filter-pill:hover,
.fashion-filter-pill.active {
  background-color: var(--color-brand-primary);
  color: #FFFFFF;
  border-color: var(--color-brand-primary);
}"""

rep_section = """.fashion-section-sub {
  font-size: 0.95rem;
  color: var(--color-text-body);
  font-weight: 500;
}
.fashion-filter-pills {
  display: flex;
  gap: 0.5rem;
  overflow-x: auto;
  padding-bottom: 0.25rem;
}
.fashion-filter-pill {
  background: #FFFFFF;
  border: 1px solid var(--color-border-strong);
  border-radius: var(--radius-full);
  padding: 0.5rem 1.15rem;
  font-family: var(--font-sans);
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--color-text-headline);
  cursor: pointer;
  white-space: nowrap;
  transition: all var(--duration-fast);
}
.fashion-filter-pill:hover,
.fashion-filter-pill.active {
  background-color: var(--color-brand-primary);
  color: #FFFFFF;
  border-color: var(--color-brand-primary);
}"""

# 8. Update article card text
target_card_body = """.fashion-card-title {
  font-family: var(--font-editorial);
  font-size: 1.25rem;
  font-weight: 700;
  line-height: 1.35;
  color: var(--color-text-headline);
  margin-bottom: 0.6rem;
}
.fashion-card-excerpt {
  font-size: 0.875rem;
  line-height: 1.55;
  color: var(--color-text-muted);
  margin-bottom: 1.25rem;
  flex-grow: 1;
}
.fashion-card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid var(--color-border-hairline);
  padding-top: 0.85rem;
  font-size: 0.75rem;
  color: var(--color-text-muted);
}"""

rep_card_body = """.fashion-card-title {
  font-family: var(--font-editorial);
  font-size: 1.28rem;
  font-weight: 800;
  line-height: 1.35;
  color: var(--color-text-headline);
  margin-bottom: 0.6rem;
}
.fashion-card-excerpt {
  font-size: 0.925rem;
  line-height: 1.6;
  color: var(--color-text-body);
  font-weight: 400;
  margin-bottom: 1.25rem;
  flex-grow: 1;
}
.fashion-card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid var(--color-border-hairline);
  padding-top: 0.85rem;
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--color-text-muted);
}"""

# 9. Update category pages
target_cat_page = """.category-breadcrumb {
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  margin-bottom: 0.75rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.category-breadcrumb a {
  color: var(--color-text-headline);
  text-decoration: none;
  font-weight: 500;
  transition: color var(--duration-fast);
}
.category-breadcrumb a:hover {
  color: var(--color-brand-primary);
}
.category-page-title {
  font-family: var(--font-editorial);
  font-size: 2.75rem;
  font-weight: 800;
  color: var(--color-brand-primary);
  letter-spacing: -0.02em;
  margin-bottom: 0.5rem;
}
.category-page-desc {
  font-family: var(--font-serif);
  font-size: 1.15rem;
  color: var(--color-text-muted);
  max-width: 780px;
  line-height: 1.6;
}"""

rep_cat_page = """.category-breadcrumb {
  font-size: 0.875rem;
  color: var(--color-text-muted);
  font-weight: 600;
  margin-bottom: 0.75rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.category-breadcrumb a {
  color: var(--color-text-headline);
  text-decoration: none;
  font-weight: 700;
  transition: color var(--duration-fast);
}
.category-breadcrumb a:hover {
  color: var(--color-brand-primary);
  text-decoration: underline;
}
.category-page-title {
  font-family: var(--font-editorial);
  font-size: 2.85rem;
  font-weight: 800;
  color: var(--color-brand-primary);
  letter-spacing: -0.02em;
  margin-bottom: 0.5rem;
}
.category-page-desc {
  font-family: var(--font-serif);
  font-size: 1.18rem;
  color: var(--color-text-body);
  font-weight: 500;
  max-width: 820px;
  line-height: 1.65;
}"""

target_cat_featured = """.category-featured-kicker {
  font-size: 0.75rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--color-brand-accent);
  margin-bottom: 0.75rem;
}
.category-featured-title {
  font-family: var(--font-editorial);
  font-size: 2rem;
  font-weight: 700;
  line-height: 1.25;
  color: var(--color-text-headline);
  margin-bottom: 1rem;
}
.category-featured-excerpt {
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--color-text-muted);
  margin-bottom: 1.75rem;
}"""

rep_cat_featured = """.category-featured-kicker {
  font-size: 0.775rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--color-brand-accent);
  margin-bottom: 0.75rem;
}
.category-featured-title {
  font-family: var(--font-editorial);
  font-size: 2.1rem;
  font-weight: 800;
  line-height: 1.25;
  color: var(--color-text-headline);
  margin-bottom: 1rem;
}
.category-featured-excerpt {
  font-size: 1.05rem;
  line-height: 1.65;
  color: var(--color-text-body);
  font-weight: 400;
  margin-bottom: 1.75rem;
}"""

# 10. Update footer text
target_footer = """.fashion-footer-desc {
  font-size: 0.875rem;
  color: var(--color-text-headline);
  font-weight: 600;
  margin-bottom: 0.25rem;
}
.fashion-footer-group {
  font-size: 0.8125rem;
  color: var(--color-text-muted);
}"""

rep_footer = """.fashion-footer-desc {
  font-size: 0.925rem;
  color: var(--color-text-headline);
  font-weight: 700;
  margin-bottom: 0.35rem;
}
.fashion-footer-group {
  font-size: 0.85rem;
  color: var(--color-text-body);
  font-weight: 500;
}"""

# Apply substitutions
norm_css = css.replace("\r\n", "\n")
subs = [
    (target_root, rep_root),
    (target_academic, rep_academic),
    (target_subscribe, rep_subscribe),
    (target_cover_text, rep_cover_text),
    (target_latest, rep_latest),
    (target_latest_items, rep_latest_items),
    (target_bento, rep_bento),
    (target_her_voice, rep_her_voice),
    (target_section, rep_section),
    (target_card_body, rep_card_body),
    (target_cat_page, rep_cat_page),
    (target_cat_featured, rep_cat_featured),
    (target_footer, rep_footer)
]

applied = 0
for t, r in subs:
    nt = t.replace("\r\n", "\n")
    nr = r.replace("\r\n", "\n")
    if nt in norm_css:
        norm_css = norm_css.replace(nt, nr, 1)
        applied += 1
    else:
        print(f"FAILED to match block starting with: {t[:40]}...")

with open("css/style.css", "w", encoding="utf-8") as f:
    f.write(norm_css)

print(f"Applied {applied}/{len(subs)} style enhancements successfully!")
