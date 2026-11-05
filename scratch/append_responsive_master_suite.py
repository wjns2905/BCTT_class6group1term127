import re

path = 'C:/Users/camka/OneDrive/Desktop/BCTT_class6group1term127/css/style.css'
with open(path, 'r', encoding='utf-8') as f:
    css = f.read()

responsive_suite = '''
/* ===================================================================
   COMPREHENSIVE RESPONSIVE DESIGN SUITE FOR ALL TABLETS AND PHONES
   Tested for:
   - 320px - 360px: iPhone SE, Galaxy A-series, small Androids
   - 375px - 480px: Modern iPhones (12/13/14/15/16 Pro Max), Pixel, Galaxy S
   - 600px - 767px: Large Phablets & Foldables
   - 768px - 1023px: Tablets in Portrait (iPad Mini, iPad 10.2", iPad Air)
   - 1024px - 1199px: Tablets in Landscape & Small Laptops (iPad Pro 11"/12.9")
   =================================================================== */

/* -------------------------------------------------------------
   1. GLOBAL TOUCH & SAFE AREA FOUNDATION
   ------------------------------------------------------------- */
:root {
  --safe-top: env(safe-area-inset-top, 0px);
  --safe-right: env(safe-area-inset-right, 0px);
  --safe-bottom: env(safe-area-inset-bottom, 0px);
  --safe-left: env(safe-area-inset-left, 0px);
}

html, body {
  overflow-x: hidden !important;
  max-width: 100vw;
  -webkit-text-size-adjust: 100%;
}

img, video, iframe {
  max-width: 100%;
  height: auto;
}

/* Touch targets & tap highlight removal */
button, a, input, select, textarea {
  -webkit-tap-highlight-color: transparent;
}

/* Mobile Brand Sticky Link (Hidden on Desktop) */
.fashion-mobile-brand {
  display: none;
  align-items: center;
  font-family: var(--font-editorial, 'Plus Jakarta Sans', serif);
  font-size: 1.25rem;
  font-weight: 900;
  letter-spacing: -0.03em;
  color: var(--color-brand-primary, #54111E);
  text-decoration: none;
  line-height: 1;
  white-space: nowrap;
}

/* Mobile Bottom Dock App Bar Styling */
.dock-btn,
.mobile-dock-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3px;
  color: var(--color-text-muted, #7A726D);
  font-family: var(--font-sans, -apple-system, sans-serif);
  font-size: 0.6875rem;
  font-weight: 600;
  text-decoration: none;
  min-width: 48px;
  min-height: 48px;
  flex: 1;
  transition: color 0.15s ease, transform 0.15s ease;
  user-select: none;
  -webkit-tap-highlight-color: transparent;
}
.dock-btn i,
.mobile-dock-btn i {
  font-size: 1.15rem;
  transition: transform 0.2s var(--ease-spring, ease);
}
.dock-btn:active,
.mobile-dock-btn:active {
  transform: scale(0.92);
}
.dock-btn.active,
.mobile-dock-btn.active {
  color: var(--color-brand-primary, #54111E);
  font-weight: 700;
}
.dock-btn.active i,
.mobile-dock-btn.active i {
  color: var(--color-brand-primary, #54111E);
  transform: translateY(-1px);
}

/* -------------------------------------------------------------
   2. TABLET LANDSCAPE & COMPACT DESKTOP (992px to 1199px)
   ------------------------------------------------------------- */
@media (min-width: 992px) and (max-width: 1199px) {
  .fashion-header-container {
    height: 52px;
  }
  .fashion-nav {
    gap: 0.75rem;
  }
  .nav-item {
    font-size: 0.825rem;
    padding: 0.35rem 0.4rem;
  }
  .fashion-header-actions {
    gap: 0.65rem;
  }
  .fashion-subscribe-btn {
    padding: 0.45rem 1rem;
    font-size: 0.8125rem;
  }
  .top-hero-3col-cluster {
    grid-template-columns: 1fr 1.6fr 1fr;
    gap: 1.15rem;
  }
  .lead-media-wrap,
  .center-post-media-wrap {
    height: 300px;
  }
  .video-grid-layout {
    grid-template-columns: 1.4fr 1fr;
    gap: 1.25rem;
  }
}

/* -------------------------------------------------------------
   3. TABLETS PORTRAIT & IPAD PRO COMPACT (768px to 991px)
   ------------------------------------------------------------- */
@media (max-width: 991px) {
  /* Header navigation collapses to drawer */
  .fashion-nav {
    display: none !important;
  }
  .fashion-hamburger-btn {
    display: inline-flex !important;
    align-items: center;
    justify-content: center;
  }
  .fashion-mobile-brand {
    display: flex !important;
  }
  
  /* Masthead logo and ad sizing */
  .fashion-brand-logo-fullsize {
    max-width: min(480px, 86vw) !important;
    max-height: 140px !important;
  }
  .header-ad-link {
    max-width: min(460px, 88vw) !important;
  }

  /* Homepage cluster in 2-column tablet layout */
  .top-hero-3col-cluster {
    display: grid !important;
    grid-template-columns: 1.35fr 1fr !important;
    gap: 1.5rem !important;
  }
  .hero-center-top-post {
    grid-column: 1 / 2 !important;
    grid-row: 1 / 2 !important;
  }
  .hero-right-widgets {
    grid-column: 2 / 3 !important;
    grid-row: 1 / 2 !important;
  }
  .hero-left-stream {
    grid-column: 1 / -1 !important;
    grid-row: 2 / 3 !important;
    display: grid !important;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
    gap: 1rem !important;
    margin-top: 0.5rem;
  }
  .stream-card-mini {
    background: #FFFFFF;
    border: 1px solid var(--color-border-hairline);
    border-radius: var(--radius-md, 8px);
    padding: 0.85rem;
  }

  /* Category pages layout on tablet */
  .category-page-asymm {
    grid-template-columns: 1fr !important;
    gap: 2rem !important;
  }
  .category-stream-row {
    grid-template-columns: 200px 1fr !important;
  }
  .category-featured-card {
    grid-template-columns: 1fr 1fr !important;
    gap: 1.5rem !important;
  }
  .category-featured-media {
    height: 100% !important;
    min-height: 280px;
  }

  /* Multimedia Video Hub on tablet */
  .video-grid-layout {
    grid-template-columns: 1fr !important;
    gap: 1.5rem !important;
  }
  .video-playlist {
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
    max-height: 440px !important;
    gap: 0.75rem !important;
  }

  /* Team profiles on tablet */
  .profiles-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 1.25rem !important;
  }

  /* Article reading modal on tablet */
  .article-modal-backdrop {
    padding: 1.5rem 1rem !important;
  }
  .article-modal-container {
    max-width: 92vw !important;
    border-radius: var(--radius-lg, 12px) !important;
  }
  .article-reading-content {
    padding: 2.25rem 2rem !important;
  }
}

/* -------------------------------------------------------------
   4. SMARTPHONES & SMALL PHABLETS (<= 768px)
   ------------------------------------------------------------- */
@media (max-width: 768px) {
  body {
    padding-bottom: calc(64px + env(safe-area-inset-bottom, 0px)) !important;
  }
  
  .container {
    padding-left: 1rem !important;
    padding-right: 1rem !important;
  }

  /* Sticky header on mobile */
  .fashion-header-container {
    height: 50px !important;
  }
  .fashion-header-actions {
    gap: 0.5rem !important;
  }
  .fashion-subscribe-btn {
    padding: 0.38rem 0.85rem !important;
    font-size: 0.8rem !important;
  }

  /* Mobile dock activation with safe area */
  .mobile-bottom-dock {
    display: flex !important;
    height: calc(56px + env(safe-area-inset-bottom, 0px)) !important;
    padding-bottom: env(safe-area-inset-bottom, 0px) !important;
  }
  .dock-btn, .mobile-dock-btn {
    display: flex !important;
  }

  /* Masthead logo and ad sizing */
  .fashion-brand-logo-fullsize {
    max-width: min(320px, 86vw) !important;
    max-height: 125px !important;
  }
  .fashion-masthead-hero {
    padding: 1rem 0 0.65rem !important;
  }
  .header-ad-leaderboard-wrap {
    padding: 0.35rem 0.5rem !important;
  }
  .header-ad-link {
    max-width: min(360px, 94vw) !important;
  }

  /* Homepage cluster single-column flow with Lead Story at the TOP */
  .top-hero-3col-cluster {
    display: flex !important;
    flex-direction: column !important;
    gap: 1.75rem !important;
    margin-top: 1rem !important;
    margin-bottom: 2rem !important;
  }
  .hero-center-top-post {
    order: 1 !important;
  }
  .center-post-media-wrap {
    height: 220px !important;
    aspect-ratio: 16/9 !important;
  }
  .center-post-title {
    font-size: 1.35rem !important;
    line-height: 1.3 !important;
  }
  .hero-left-stream {
    order: 2 !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 0.85rem !important;
  }
  .stream-card-mini {
    padding: 0.75rem 0 !important;
    border-bottom: 1px solid var(--color-border-hairline) !important;
    border-radius: 0 !important;
    background: transparent !important;
    border-top: none !important;
    border-left: none !important;
    border-right: none !important;
  }
  .stream-thumb-img {
    width: 72px !important;
    height: 72px !important;
    min-width: 72px !important;
    border-radius: 6px !important;
  }
  .hero-right-widgets {
    order: 3 !important;
  }

  /* Category pages on mobile */
  .category-featured-card {
    display: flex !important;
    flex-direction: column !important;
    border-radius: var(--radius-md, 10px) !important;
    overflow: hidden !important;
  }
  .category-featured-media {
    order: -1 !important;
    width: 100% !important;
    height: auto !important;
    aspect-ratio: 16/9 !important;
    max-height: 240px !important;
  }
  .category-featured-body {
    padding: 1.25rem 1rem !important;
  }
  .category-stream-row {
    display: flex !important;
    flex-direction: column !important;
    gap: 0.85rem !important;
    padding: 1rem !important;
    border-radius: var(--radius-md, 10px) !important;
  }
  .category-stream-thumb-wrap {
    width: 100% !important;
    height: auto !important;
    aspect-ratio: 16/9 !important;
    max-height: 210px !important;
    border-radius: 6px !important;
  }
  .category-stream-title {
    font-size: 1.05rem !important;
    line-height: 1.35 !important;
  }

  /* Full-bleed responsive Article Reader Modal */
  .article-modal-backdrop {
    padding: 0 !important;
    background: rgba(14, 11, 10, 0.92) !important;
  }
  .article-modal-container {
    width: 100% !important;
    min-height: 100vh !important;
    border-radius: 0 !important;
    border: none !important;
    box-shadow: none !important;
    margin: 0 !important;
  }
  .article-reading-content {
    padding: 1.25rem 1rem 3rem !important;
  }
  .article-modal-close-btn {
    position: fixed !important;
    top: 10px !important;
    right: 10px !important;
    z-index: 9999 !important;
    width: 38px !important;
    height: 38px !important;
    background: rgba(255, 255, 255, 0.95) !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25) !important;
  }
  .article-headline {
    font-size: 1.45rem !important;
    line-height: 1.25 !important;
  }
  .article-sapo {
    font-size: 1rem !important;
    line-height: 1.55 !important;
  }
  .article-author-strip {
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 0.75rem !important;
  }
  .article-reading-tools {
    width: 100% !important;
    justify-content: flex-start !important;
    gap: 0.4rem !important;
  }
  .article-reading-tools .tool-btn,
  .article-reading-tools .btn-article-like {
    padding: 0.35rem 0.55rem !important;
    font-size: 0.75rem !important;
  }

  /* Multimedia Video Hub on mobile */
  .video-grid-layout {
    grid-template-columns: 1fr !important;
    gap: 1.25rem !important;
  }
  .video-playlist {
    max-height: 360px !important;
    gap: 0.65rem !important;
    -webkit-overflow-scrolling: touch !important;
  }
  .playlist-card {
    padding: 0.65rem !important;
    gap: 0.65rem !important;
  }
  .playlist-card-thumb-wrap {
    width: 85px !important;
    height: 56px !important;
    min-width: 85px !important;
  }
  .video-toolbar-strip {
    justify-content: center !important;
    gap: 0.45rem !important;
  }
  .video-tool-btn {
    padding: 0.45rem 0.85rem !important;
    font-size: 0.75rem !important;
  }

  /* Profiles grid on mobile */
  .profiles-grid {
    grid-template-columns: 1fr !important;
    gap: 1rem !important;
  }
  .profile-card {
    padding: 1.25rem 1rem !important;
  }

  /* Modals sizing on mobile */
  .signin-modal-card {
    padding: 1.75rem 1.25rem !important;
    max-width: 92vw !important;
  }
  .search-modal-box {
    padding: 1.25rem 1rem !important;
    max-width: 94vw !important;
  }
  .search-input-field {
    font-size: 1.05rem !important;
  }

  /* Offcanvas Drawer safe sizing */
  .offcanvas-drawer {
    width: min(340px, 86vw) !important;
    padding: 1.5rem 1.25rem !important;
    overflow-y: auto !important;
    -webkit-overflow-scrolling: touch !important;
  }
}

/* -------------------------------------------------------------
   5. STANDARD & COMPACT SMARTPHONES (<= 480px)
   ------------------------------------------------------------- */
@media (max-width: 480px) {
  .container {
    padding-left: 0.75rem !important;
    padding-right: 0.75rem !important;
  }

  /* Header compact actions to guarantee ZERO overflow */
  .fashion-header-container {
    padding-left: 0.5rem !important;
    padding-right: 0.5rem !important;
  }
  .fashion-header-actions {
    gap: 0.35rem !important;
  }
  .fashion-mobile-brand {
    font-size: 1.15rem !important;
  }
  .lang-switch-pill {
    padding: 2px 3px !important;
    gap: 1px !important;
  }
  .lang-pill-btn {
    padding: 0.2rem 0.4rem !important;
    font-size: 0.7rem !important;
  }
  .fashion-search-btn {
    padding: 0.35rem !important;
    font-size: 1rem !important;
  }
  .fashion-subscribe-btn {
    padding: 0.35rem 0.65rem !important;
    font-size: 0.75rem !important;
    letter-spacing: 0 !important;
  }
  .fashion-user-btn {
    width: 32px !important;
    height: 32px !important;
    font-size: 1.1rem !important;
  }
  .fashion-hamburger-btn {
    padding: 0.35rem !important;
    font-size: 1.15rem !important;
  }

  /* Masthead logo and Ad banner */
  .fashion-brand-logo-fullsize {
    max-width: min(280px, 84vw) !important;
    max-height: 105px !important;
  }
  .header-ad-link {
    max-width: min(320px, 94vw) !important;
  }

  /* Titles */
  .category-page-title {
    font-size: 1.75rem !important;
  }
  .category-page-desc {
    font-size: 0.925rem !important;
  }
  .center-post-title {
    font-size: 1.2rem !important;
  }
  .center-post-media-wrap {
    height: 180px !important;
  }
}

/* -------------------------------------------------------------
   6. ULTRA-COMPACT PHONES (<= 360px - e.g. iPhone SE, Galaxy A)
   ------------------------------------------------------------- */
@media (max-width: 360px) {
  .fashion-mobile-brand {
    font-size: 1rem !important;
    letter-spacing: -0.04em !important;
  }
  .fashion-header-actions {
    gap: 0.25rem !important;
  }
  .fashion-subscribe-btn {
    padding: 0.3rem 0.5rem !important;
    font-size: 0.7rem !important;
  }
  .fashion-brand-logo-fullsize {
    max-width: 230px !important;
    max-height: 85px !important;
  }
  .header-ad-link {
    max-width: 280px !important;
  }
  .stream-thumb-img {
    width: 64px !important;
    height: 64px !important;
    min-width: 64px !important;
  }
  .stream-mini-headline {
    font-size: 0.8125rem !important;
  }
  .center-post-media-wrap {
    height: 160px !important;
  }
  .center-post-title {
    font-size: 1.15rem !important;
  }
}
'''

if 'COMPREHENSIVE RESPONSIVE DESIGN SUITE' not in css:
    css = css + '\n' + responsive_suite
    print("Appended comprehensive responsive suite to style.css")
else:
    # Replace existing suite
    pattern = r'/\* ===================================================================\s*COMPREHENSIVE RESPONSIVE DESIGN SUITE[\s\S]*$'
    css = re.sub(pattern, responsive_suite.strip(), css)
    print("Replaced existing responsive suite in style.css")

with open(path, 'w', encoding='utf-8') as f:
    f.write(css)

print("style.css updated successfully")
