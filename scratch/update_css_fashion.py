import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

CSS_PATH = r"c:\Users\camka\OneDrive\Desktop\BCTT\css\style.css"

with open(CSS_PATH, "r", encoding="utf-8") as f:
    css = f.read()

fashion_css = """
/* ===================================================================
   HIGH-FASHION EDITORIAL MAGAZINE SUITE (VOGUE / ELLE / KINFOLK)
   Directly matching the official HEARTICLES brand mockup
   =================================================================== */

/* Page Background & Base Typography */
body {
  background-color: var(--color-canvas);
  color: var(--color-text-body);
  font-family: var(--font-sans);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* 1. Academic Utility Line */
.fashion-academic-bar {
  background: #FFFFFF;
  border-bottom: 1px solid var(--color-border-hairline);
  padding: 0.45rem 0;
  font-size: 0.75rem;
  color: var(--color-text-muted);
}
.fashion-academic-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.academic-tag-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-weight: 600;
  color: var(--color-brand-primary);
  letter-spacing: 0.02em;
}

/* 2. Brand Header / Masthead */
.fashion-header {
  background: #FFFFFF;
  border-bottom: 1px solid var(--color-border-hairline);
  position: sticky;
  top: 0;
  z-index: 900;
  backdrop-filter: blur(8px);
}
.fashion-header-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 76px;
}
.fashion-brand-logo {
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
}
.fashion-brand-logo:hover {
  opacity: 0.9;
}
.fashion-brand-period {
  color: var(--color-brand-accent);
}

/* Center Navigation */
.fashion-nav {
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
}
.nav-item-her {
  color: var(--color-brand-primary) !important;
  font-weight: 600 !important;
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
}
.nav-badge-dot {
  width: 6px;
  height: 6px;
  background-color: var(--color-brand-accent);
  border-radius: 50%;
  display: inline-block;
}

/* Header Right Actions */
.fashion-header-actions {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}
.fashion-search-btn {
  background: none;
  border: none;
  font-size: 1.15rem;
  color: var(--color-text-headline);
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 50%;
  transition: color var(--duration-fast) var(--ease-spring);
}
.fashion-search-btn:hover {
  color: var(--color-brand-primary);
}
.fashion-subscribe-btn {
  background-color: var(--color-brand-primary);
  color: #FFFFFF;
  border: none;
  border-radius: var(--radius-full);
  font-family: var(--font-sans);
  font-size: 0.875rem;
  font-weight: 600;
  padding: 0.55rem 1.45rem;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(89, 23, 36, 0.15);
  transition: all var(--duration-fast) var(--ease-spring);
}
.fashion-subscribe-btn:hover {
  background-color: var(--color-brand-hover);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(89, 23, 36, 0.25);
}
.fashion-hamburger-btn {
  display: none;
  background: none;
  border: none;
  font-size: 1.35rem;
  color: var(--color-text-headline);
  cursor: pointer;
}

/* ===================================================================
   3. HERO BENTO GRID (COVER STORY + THE LATEST)
   =================================================================== */
.fashion-hero-grid {
  display: grid;
  grid-template-columns: 1.8fr 1fr;
  gap: 1.5rem;
  margin-top: 2rem;
  margin-bottom: 2rem;
}

/* Giant Cover Story Card */
.fashion-cover-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-md);
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  cursor: pointer;
  transition: transform var(--duration-normal) var(--ease-spring), box-shadow var(--duration-normal) var(--ease-spring);
}
.fashion-cover-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-lg);
}
.fashion-cover-text {
  padding: 2.25rem 2rem 2.25rem 2.25rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.fashion-kicker-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
}
.fashion-kicker {
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
}
.fashion-action-row {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}
.fashion-btn-pill {
  background-color: var(--color-brand-primary);
  color: #FFFFFF;
  border: none;
  border-radius: var(--radius-full);
  font-family: var(--font-sans);
  font-size: 0.875rem;
  font-weight: 600;
  padding: 0.65rem 1.4rem;
  cursor: pointer;
  transition: background-color var(--duration-fast) var(--ease-spring);
}
.fashion-btn-pill:hover {
  background-color: var(--color-brand-hover);
}
.fashion-meta-pill {
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  font-weight: 500;
}
.fashion-cover-media {
  position: relative;
  overflow: hidden;
  height: 100%;
}
.fashion-cover-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.6s var(--ease-spring);
}
.fashion-cover-card:hover .fashion-cover-image {
  transform: scale(1.03);
}

/* Right: THE LATEST. Column */
.fashion-latest-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-lg);
  padding: 1.75rem 1.5rem;
  box-shadow: var(--shadow-md);
  display: flex;
  flex-direction: column;
}
.fashion-latest-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--color-border-hairline);
  padding-bottom: 0.85rem;
  margin-bottom: 1.25rem;
}
.fashion-latest-title {
  font-family: var(--font-editorial);
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--color-text-headline);
  letter-spacing: -0.01em;
}
.fashion-view-all {
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--color-text-muted);
  text-decoration: none;
  transition: color var(--duration-fast);
}
.fashion-view-all:hover {
  color: var(--color-brand-primary);
}
.fashion-latest-list {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  flex-grow: 1;
  justify-content: space-between;
}
.fashion-latest-item {
  display: flex;
  gap: 1rem;
  align-items: center;
  cursor: pointer;
  padding: 0.4rem;
  border-radius: var(--radius-md);
  transition: background-color var(--duration-fast);
}
.fashion-latest-item:hover {
  background-color: var(--color-surface-subtle);
}
.latest-thumb-wrap {
  width: 72px;
  height: 72px;
  flex-shrink: 0;
  border-radius: var(--radius-md);
  overflow: hidden;
  background-color: var(--color-surface-blush);
}
.latest-thumb-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.latest-content {
  flex-grow: 1;
}
.latest-kicker {
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
}

/* ===================================================================
   4. SECONDARY CURATED BENTO ROW (3 FEATURE CARDS)
   =================================================================== */
.fashion-feature-row {
  display: grid;
  grid-template-columns: 1fr 1.3fr 1fr;
  gap: 1.5rem;
  margin-bottom: 3rem;
}

.fashion-bento-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-lg);
  padding: 1.5rem;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  cursor: pointer;
  transition: transform var(--duration-normal) var(--ease-spring), box-shadow var(--duration-normal) var(--ease-spring);
}
.fashion-bento-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}

/* Card 1: What's the buzz */
.bento-buzz .bento-text {
  margin-bottom: 1rem;
}
.bento-kicker {
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
}
.bento-media {
  border-radius: var(--radius-md);
  overflow: hidden;
}
.bento-img {
  width: 100%;
  height: 140px;
  object-fit: cover;
  display: block;
}

/* Card 2: Her Voice. Her Story */
.bento-her-voice {
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
}
.bento-arrow-link {
  font-size: 0.75rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--color-brand-primary);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  transition: transform var(--duration-fast);
}
.bento-arrow-link:hover {
  transform: translateX(3px);
}
.bento-img-square {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: var(--radius-md);
  display: block;
}

/* Card 3: A Little More Human */
.bento-human .bento-text {
  margin-bottom: 1rem;
  position: relative;
}
.bento-human .bento-headline {
  font-family: var(--font-editorial);
  font-size: 1.3rem;
  font-weight: 700;
  line-height: 1.25;
  margin-top: 0.35rem;
}
.bento-doodle-heart {
  width: 24px;
  height: 22px;
  display: block;
  margin-top: 0.5rem;
}

/* ===================================================================
   5. MAGAZINE SECTION TITLES & FILTER PILLS
   =================================================================== */
.fashion-section-divider {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 3.5rem 0 1.5rem 0;
  border-bottom: 1px solid var(--color-border-hairline);
  padding-bottom: 1rem;
}
.fashion-section-title-wrap {
  display: flex;
  align-items: baseline;
  gap: 0.75rem;
}
.fashion-section-main-title {
  font-family: var(--font-editorial);
  font-size: 1.75rem;
  font-weight: 800;
  color: var(--color-text-headline);
}
.fashion-section-sub {
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
}

/* ===================================================================
   6. MAGAZINE ARTICLE GRID
   =================================================================== */
.fashion-articles-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.75rem;
  margin-bottom: 3.5rem;
}
.fashion-article-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  cursor: pointer;
  transition: transform var(--duration-normal) var(--ease-spring), box-shadow var(--duration-normal) var(--ease-spring);
}
.fashion-article-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
}
.fashion-card-media {
  position: relative;
  width: 100%;
  height: 220px;
  overflow: hidden;
  background-color: var(--color-surface-blush);
}
.fashion-card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.6s var(--ease-spring);
}
.fashion-article-card:hover .fashion-card-img {
  transform: scale(1.04);
}
.fashion-card-category-tag {
  position: absolute;
  top: 1rem;
  left: 1rem;
  background: rgba(89, 23, 36, 0.92);
  color: #FFFFFF;
  font-size: 0.6875rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 0.3rem 0.75rem;
  border-radius: var(--radius-full);
  backdrop-filter: blur(4px);
}
.fashion-card-body {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}
.fashion-card-title {
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
}
.fashion-card-byline {
  font-weight: 600;
}
.fashion-card-stats {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

/* ===================================================================
   7. LUXURY FOOTER WITH SKETCH HEART
   =================================================================== */
.fashion-footer {
  background: #FFFFFF;
  border-top: 1px solid var(--color-border-hairline);
  padding: 3.5rem 0 2rem 0;
  margin-top: 4rem;
}
.fashion-footer-container {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  border-bottom: 1px solid var(--color-border-hairline);
  padding-bottom: 2.5rem;
  margin-bottom: 1.5rem;
}
.fashion-footer-brand {
  max-width: 540px;
}
.fashion-footer-logo {
  font-family: var(--font-editorial);
  font-size: 2.25rem;
  font-weight: 800;
  font-style: italic;
  color: var(--color-brand-primary);
  display: block;
  margin-bottom: 0.5rem;
}
.fashion-footer-desc {
  font-size: 0.875rem;
  color: var(--color-text-headline);
  font-weight: 600;
  margin-bottom: 0.25rem;
}
.fashion-footer-group {
  font-size: 0.8125rem;
  color: var(--color-text-muted);
}
.fashion-footer-slogan-wrap {
  text-align: right;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}
.fashion-slogan-heart {
  width: 72px;
  height: 54px;
  margin-bottom: 0.5rem;
}
.fashion-slogan-text {
  font-family: var(--font-editorial);
  font-style: italic;
  font-size: 1.25rem;
  color: var(--color-brand-primary);
}
.fashion-footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.75rem;
  color: var(--color-text-muted);
}

/* ===================================================================
   8. MOBILE RESPONSIVE ADAPTATIONS (< 992px & < 768px)
   =================================================================== */
@media (max-width: 992px) {
  .fashion-hero-grid {
    grid-template-columns: 1fr;
  }
  .fashion-feature-row {
    grid-template-columns: 1fr;
  }
  .fashion-articles-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .fashion-nav {
    display: none;
  }
  .fashion-hamburger-btn {
    display: block;
  }
  .fashion-cover-card {
    grid-template-columns: 1fr;
  }
  .fashion-cover-text {
    padding: 1.5rem;
    order: 2;
  }
  .fashion-cover-media {
    height: 280px;
    order: 1;
  }
  .fashion-headline {
    font-size: 1.65rem;
  }
  .fashion-articles-grid {
    grid-template-columns: 1fr;
  }
  .bento-her-voice {
    grid-template-columns: 1fr;
  }
  .fashion-footer-container {
    flex-direction: column;
    align-items: flex-start;
    gap: 2rem;
  }
  .fashion-footer-slogan-wrap {
    align-items: flex-start;
  }
}
"""

with open(CSS_PATH, "a", encoding="utf-8") as f:
    f.write("\n\n" + fashion_css)

print("Successfully appended Fashion Magazine CSS suite to style.css!")
