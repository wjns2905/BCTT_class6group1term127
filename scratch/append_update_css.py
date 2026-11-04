# -*- coding: utf-8 -*-
import sys

new_css = """
/* ===================================================================
   HEADER LEADERBOARD ADVERTISEMENT (IELTS BANNER)
   =================================================================== */
.header-ad-leaderboard-wrap {
  background: #FDFBFB;
  padding: 0.6rem 0;
  border-bottom: 1px solid var(--color-border-hairline);
  text-align: center;
}
.ad-label-strip {
  font-size: 0.625rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  color: var(--color-text-muted);
  text-transform: uppercase;
  margin-bottom: 0.3rem;
}
.header-ad-link {
  display: inline-block;
  max-width: 100%;
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  transition: transform var(--duration-fast) var(--ease-spring), box-shadow var(--duration-fast);
}
.header-ad-link:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(84, 17, 30, 0.12);
}
.header-ad-banner-img {
  width: 100%;
  max-width: 980px;
  height: auto;
  max-height: 110px;
  object-fit: cover;
  display: block;
}

/* ===================================================================
   UPDATED BRAND LOGO (DIDONE HIGH-FASHION)
   =================================================================== */
.fashion-brand-logo-img {
  height: 44px;
  width: auto;
  object-fit: contain;
  display: block;
  transition: transform var(--duration-fast);
}
.fashion-brand-logo-img:hover {
  transform: scale(1.02);
}
.fashion-brand-slogan-sub {
  font-family: var(--font-editorial);
  font-style: italic;
  font-size: 0.75rem;
  color: var(--color-brand-accent);
  letter-spacing: 0.02em;
  display: block;
  margin-top: -2px;
}

/* ===================================================================
   3-COLUMN TOP POST CLUSTER (CENTER HERO, RIGHT TRENDING, LEFT STREAM)
   =================================================================== */
.top-hero-3col-cluster {
  display: grid;
  grid-template-columns: 280px minmax(0, 1fr) 300px;
  gap: 1.5rem;
  align-items: start;
  margin-top: 1.5rem;
  margin-bottom: 3rem;
}

/* 1. Left Column: Curated Stories Stream */
.hero-left-stream {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.stream-header-strip {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 0.4rem;
  border-bottom: 2px solid var(--color-brand-primary);
  margin-bottom: 0.25rem;
}
.stream-title-text {
  font-size: 0.8125rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  color: var(--color-brand-primary);
  text-transform: uppercase;
}
.stream-card-mini {
  display: flex;
  gap: 0.75rem;
  padding-bottom: 0.85rem;
  border-bottom: 1px solid var(--color-border-hairline);
  cursor: pointer;
  transition: transform var(--duration-fast);
}
.stream-card-mini:last-child {
  border-bottom: none;
  padding-bottom: 0;
}
.stream-card-mini:hover {
  transform: translateX(3px);
}
.stream-card-mini:hover .stream-mini-headline {
  color: var(--color-brand-primary);
}
.stream-thumb-img {
  width: 76px;
  height: 76px;
  border-radius: var(--radius-sm);
  object-fit: cover;
  flex-shrink: 0;
}
.stream-mini-body {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.stream-mini-cat {
  font-size: 0.65rem;
  font-weight: 800;
  color: var(--color-brand-accent);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.stream-mini-headline {
  font-family: var(--font-editorial);
  font-size: 0.875rem;
  font-weight: 700;
  line-height: 1.35;
  color: #141011;
  margin: 0.2rem 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.stream-mini-time {
  font-size: 0.7rem;
  color: var(--color-text-muted);
}

/* 2. Center Column: Top Post (Lead Hero Story) */
.hero-center-top-post {
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-md);
  padding: 1.25rem;
  cursor: pointer;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
  transition: transform var(--duration-normal), box-shadow var(--duration-normal);
}
.hero-center-top-post:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(84, 17, 30, 0.1);
}
.center-post-media-wrap {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9.5;
  border-radius: var(--radius-sm);
  overflow: hidden;
  margin-bottom: 1rem;
}
.center-post-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform var(--duration-slow);
}
.hero-center-top-post:hover .center-post-img {
  transform: scale(1.03);
}
.center-post-badge {
  position: absolute;
  top: 0.75rem;
  left: 0.75rem;
  background: var(--color-brand-primary);
  color: #FFFFFF;
  font-size: 0.6875rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: var(--radius-full);
}
.center-post-headline {
  font-family: var(--font-editorial);
  font-size: 1.65rem;
  font-weight: 800;
  line-height: 1.25;
  color: #141011;
  margin-bottom: 0.65rem;
  letter-spacing: -0.02em;
}
.center-post-sapo {
  font-size: 0.925rem;
  line-height: 1.65;
  color: var(--color-text-body);
  margin-bottom: 0.85rem;
}
.center-post-meta {
  display: flex;
  gap: 1rem;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--color-brand-primary);
  padding-bottom: 0.85rem;
  border-bottom: 1px solid var(--color-border-hairline);
  margin-bottom: 0.85rem;
}
.center-post-related-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.center-related-row {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.85rem;
  font-weight: 600;
  color: #2D2522;
  cursor: pointer;
  transition: color var(--duration-fast);
}
.center-related-row:hover {
  color: var(--color-brand-primary);
}
.red-bullet-icon {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--color-brand-primary);
  flex-shrink: 0;
}

/* 3. Right Column: Trending & Most Read */
.hero-right-col {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}
.right-widget-box {
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-md);
  padding: 1rem 1.15rem;
}
.widget-head-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 0.45rem;
  border-bottom: 2px solid var(--color-brand-primary);
  margin-bottom: 0.75rem;
}
.widget-head-title {
  font-size: 0.8125rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  color: var(--color-brand-primary);
  text-transform: uppercase;
}
.widget-more-link {
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--color-brand-primary);
  text-decoration: none;
  transition: opacity var(--duration-fast);
}
.widget-more-link:hover {
  opacity: 0.8;
  text-decoration: underline;
}
.right-article-item {
  display: flex;
  gap: 0.65rem;
  padding: 0.5rem 0;
  border-bottom: 1px solid var(--color-border-hairline);
  cursor: pointer;
  transition: transform var(--duration-fast);
}
.right-article-item:last-child {
  border-bottom: none;
}
.right-article-item:hover .right-art-headline {
  color: var(--color-brand-primary);
}
.right-art-num {
  font-family: var(--font-editorial);
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--color-brand-accent);
  line-height: 1;
  width: 20px;
  flex-shrink: 0;
}
.right-art-thumb {
  width: 58px;
  height: 58px;
  border-radius: var(--radius-sm);
  object-fit: cover;
  flex-shrink: 0;
}
.right-art-headline {
  font-family: var(--font-editorial);
  font-size: 0.85rem;
  font-weight: 700;
  line-height: 1.3;
  color: #141011;
  margin-bottom: 0.15rem;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.right-art-meta {
  font-size: 0.7rem;
  color: var(--color-text-muted);
}
.widget-footer-btn {
  display: block;
  text-align: center;
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--color-brand-primary);
  background: rgba(84, 17, 30, 0.05);
  padding: 0.45rem;
  border-radius: var(--radius-sm);
  text-decoration: none;
  margin-top: 0.65rem;
  transition: all var(--duration-fast);
}
.widget-footer-btn:hover {
  background: var(--color-brand-primary);
  color: #FFFFFF;
}

/* ===================================================================
   ABOUT US DROPDOWN MENU
   =================================================================== */
.nav-item-dropdown {
  position: relative;
  display: inline-block;
}
.about-dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  min-width: 170px;
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-md);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  padding: 0.4rem 0;
  opacity: 0;
  visibility: hidden;
  transform: translateY(8px);
  transition: all var(--duration-fast) var(--ease-spring);
  z-index: 100;
}
.nav-item-dropdown:hover .about-dropdown-menu,
.nav-item-dropdown:focus-within .about-dropdown-menu {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}
.about-dropdown-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.55rem 1rem;
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--color-text-headline);
  text-decoration: none;
  transition: background var(--duration-fast), color var(--duration-fast);
}
.about-dropdown-item:hover {
  background: var(--color-surface-blush);
  color: var(--color-brand-primary);
}

/* ===================================================================
   HEART TAP MINIGAME & STRESS RELIEVER
   =================================================================== */
.heart-tap-container {
  background: linear-gradient(135deg, #FFF9F9 0%, #FBF3F4 100%);
  border: 1px solid #F3DEDF;
  border-radius: var(--radius-lg);
  padding: 2.25rem 2rem;
  margin: 3.5rem 0;
  text-align: center;
  position: relative;
  overflow: hidden;
}
.heart-tap-title {
  font-family: var(--font-editorial);
  font-size: 1.65rem;
  font-weight: 800;
  color: var(--color-brand-primary);
  margin-bottom: 0.4rem;
}
.heart-tap-subtitle {
  font-size: 0.9rem;
  color: var(--color-text-body);
  max-width: 600px;
  margin: 0 auto 1.5rem auto;
}
.heart-btn-circle {
  width: 76px;
  height: 76px;
  border-radius: 50%;
  background: var(--color-brand-primary);
  color: #FFFFFF;
  border: none;
  font-size: 2rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 8px 24px rgba(84, 17, 30, 0.35);
  transition: transform var(--duration-fast) var(--ease-spring), box-shadow var(--duration-fast);
  user-select: none;
  outline: none;
}
.heart-btn-circle:hover {
  transform: scale(1.1);
  box-shadow: 0 10px 28px rgba(84, 17, 30, 0.45);
}
.heart-btn-circle:active {
  transform: scale(0.92);
}
.heart-counter-badge {
  display: inline-block;
  margin-top: 1rem;
  font-size: 0.8125rem;
  font-weight: 700;
  color: var(--color-brand-primary);
  background: rgba(84, 17, 30, 0.08);
  padding: 4px 14px;
  border-radius: var(--radius-full);
}
.heart-affirmation-msg {
  font-style: italic;
  font-size: 0.875rem;
  color: var(--color-brand-accent);
  margin-top: 0.5rem;
  min-height: 1.5rem;
}
.floating-heart-particle {
  position: absolute;
  pointer-events: none;
  animation: floatUpFade 1.2s cubic-bezier(0.2, 0.8, 0.3, 1) forwards;
  font-size: 1.5rem;
}
@keyframes floatUpFade {
  0% {
    opacity: 1;
    transform: translateY(0) scale(1) rotate(0deg);
  }
  100% {
    opacity: 0;
    transform: translateY(-90px) scale(1.4) rotate(15deg);
  }
}

/* ===================================================================
   POLL "READ RELATED STORY" BUTTON
   =================================================================== */
.poll-read-related-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  margin-top: 0.85rem;
  padding: 0.6rem 1.25rem;
  background: var(--color-brand-primary);
  color: #FFFFFF;
  border-radius: var(--radius-full);
  font-size: 0.8125rem;
  font-weight: 700;
  text-decoration: none;
  border: none;
  cursor: pointer;
  transition: all var(--duration-fast);
  box-shadow: 0 2px 8px rgba(84, 17, 30, 0.25);
  animation: fadeInSlideUp 0.35s ease-out;
}
.poll-read-related-btn:hover {
  background: var(--primitive-burgundy-900);
  transform: translateY(-1px);
}

/* Responsive adjustments for 3-col Hero */
@media (max-width: 1024px) {
  .top-hero-3col-cluster {
    grid-template-columns: 1fr 1fr;
  }
  .hero-left-stream {
    grid-column: span 2;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  }
}
@media (max-width: 768px) {
  .top-hero-3col-cluster {
    grid-template-columns: 1fr;
  }
  .hero-left-stream {
    grid-column: span 1;
    display: flex;
    flex-direction: column;
  }
}
"""

with open('css/style.css', 'r', encoding='utf-8') as f:
    cur_css = f.read()

if 'top-hero-3col-cluster' not in cur_css:
    cur_css += "\n" + new_css
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(cur_css)
    print("SUCCESS: Appended new styles to css/style.css!")
else:
    print("Styles already present in css/style.css!")
