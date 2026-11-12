# -*- coding: utf-8 -*-
"""
Script to transform article reading from pop-up modal to dedicated link/page per article:
1. Create article.html with full editorial page layout, responsive sticky header, reading tools, comments, and related articles.
2. Update js/app.js so openArticleModal navigates to article.html?id=... (or hearticles/madeuparticle/ for trending-1).
3. Update hearticles/madeuparticle/index.html to render directly in page (no modal popup).
4. Update getArticleLink helper for card hrefs.
"""

import os
import re

BASE_DIR = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127"
ARTICLE_HTML_PATH = os.path.join(BASE_DIR, "article.html")
APP_PATH = os.path.join(BASE_DIR, "js", "app.js")
MADEUP_INDEX = os.path.join(BASE_DIR, "hearticles", "madeuparticle", "index.html")

# =====================================================================
# 1. CREATE ARTICLE.HTML
# =====================================================================
print("1. Creating article.html...")

article_html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title id="pageTitle">Class6group1term127 - Article</title>
  <meta name="description" content="Chuyên trang tạp chí HEARTICLES. — ULIS - VNU">
  <link rel="icon" type="image/svg+xml" href="assets/images/logo/heart-logo.svg">
  
  <!-- Modern Minimalist Editorial Typography: Plus Jakarta Sans & Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600;1,700&display=swap" rel="stylesheet">
  
  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  
  <!-- Stylesheets -->
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <script>
    function handleImageError(img) {
      if (!img) return;
      const cur = img.getAttribute('src') || '';
      if (cur.startsWith('assets/') && !img.dataset.triedRel) {
        img.dataset.triedRel = 'true';
        if (window.location.hostname.includes('github.io')) {
          img.src = '/BCTT_class6group1term127/' + cur;
          return;
        }
      }
      img.onerror = null;
      img.src = 'assets/images/trending/image8.jpg';
    }
  </script>
  <link rel="stylesheet" href="css/tokens.css">
  <link rel="stylesheet" href="css/style.css">
  <meta name="application-name" content="Class6group1term127">
  <meta property="og:site_name" content="Class6group1term127">
</head>
<body data-category="article">
  <!-- Reading Progress Bar -->
  <div class="reading-progress-bar" id="readingProgressBar"></div>

  <!-- Offline Status Banner -->
  <div class="offline-indicator-banner" id="offlineBanner" data-i18n="offline_banner">
    <i class="fas fa-wifi-slash"></i>
    <span>Chế độ ngoại tuyến: Bạn đang đọc các bài viết đã lưu đệm. Hệ thống sẽ tự động cập nhật khi có mạng.</span>
  </div>

  <!-- Header Leaderboard Advertisement -->
  <div class="header-ad-leaderboard-wrap">
    <div class="container" style="display:flex; flex-direction:column; align-items:center;">
      <span class="ad-label-strip" data-i18n="ad_label">ADVERTISEMENT</span>
      <a href="https://www.britishcouncil.vn/thi-ielts/one-skill-retake" target="_blank" rel="noopener noreferrer" class="header-ad-link" title="British Council IELTS - One Skill Retake">
        <img src="assets/images/ads/header_ad_banner.png" alt="British Council IELTS One Skill Retake Leaderboard Ad" class="header-ad-banner-img" width="1444" height="378">
      </a>
    </div>
  </div>

  <!-- Brand Masthead Hero -->
  <div class="fashion-masthead-hero">
    <div class="container masthead-hero-inner">
      <a href="index.html" class="fashion-brand-logo-masthead" aria-label="HEARTICLES. - Where News Begins with a Heartbeat">
        <img src="assets/images/logo/brand_logo_updated.png" alt="HEARTICLES. - Where News Begins with a Heartbeat" class="fashion-brand-logo-fullsize">
      </a>
    </div>
  </div>

  <!-- Sticky Categories Header Navigation -->
  <header class="fashion-header">
    <div class="container fashion-header-container">
      <a href="index.html" class="fashion-mobile-brand" aria-label="HEARTICLES. - Home">HEARTICLES.</a>
      <nav class="fashion-nav" aria-label="Thanh điều hướng tạp chí">
        <a href="index.html" class="nav-item" data-i18n="nav_home">Home</a>
        <a href="trending.html" class="nav-item" data-i18n="nav_trending">Trending</a>
        <a href="society.html" class="nav-item" data-i18n="nav_society">Society</a>
        <a href="human-stories.html" class="nav-item" data-i18n="nav_human_stories">Human Stories</a>
        <a href="mind-soul.html" class="nav-item" data-i18n="nav_mind_soul">Mind & Soul</a>
        <a href="in-depth.html" class="nav-item" data-i18n="nav_indepth">In-depth</a>
        <div class="nav-item-dropdown">
          <a href="about.html" class="nav-item" data-i18n="nav_about" style="display:inline-flex; align-items:center; gap:0.35rem;">
            About Us <i class="fas fa-chevron-down" style="font-size:0.65rem;"></i>
          </a>
          <div class="about-dropdown-menu">
            <a href="about.html#mission" class="about-dropdown-item"><i class="fas fa-bullseye"></i> <span data-i18n="about_opt_mission">Mission</span></a>
            <a href="about.html#profiles" class="about-dropdown-item"><i class="fas fa-users"></i> <span data-i18n="about_opt_profiles">Profiles</span></a>
            <a href="about.html#photo" class="about-dropdown-item"><i class="fas fa-camera"></i> <span data-i18n="about_opt_photo">Photo</span></a>
            <a href="about.html#subscribe" class="about-dropdown-item"><i class="fas fa-paper-plane"></i> <span data-i18n="about_opt_subscribe">Subscribe</span></a>
          </div>
        </div>
      </nav>

      <div class="fashion-header-actions">
        <div class="lang-switch-pill" role="group" aria-label="Language Selector">
          <button class="lang-pill-btn" data-lang="vi" onclick="setLanguage('vi')">VI</button>
          <span class="lang-pill-divider">/</span>
          <button class="lang-pill-btn active" data-lang="en" onclick="setLanguage('en')">EN</button>
        </div>
        <button class="fashion-search-btn" onclick="openSearchModal()" title="Tìm kiếm bài viết (/)" aria-label="Tìm kiếm"><i class="fas fa-search"></i></button>
        <button class="fashion-subscribe-btn" onclick="openSubscribeModal()" title="Đăng ký nhận bản tin">Subscribe</button>
        <button class="fashion-user-btn" id="headerUserBtn" onclick="openSignInModal()" title="Đăng nhập tài khoản" aria-label="Tài khoản"><i class="far fa-user-circle"></i></button>
        <button class="fashion-hamburger-btn" onclick="openDrawer()" aria-label="Menu"><i class="fas fa-bars"></i></button>
      </div>
    </div>
  </header>

  <!-- Main Article Content Container (Dedicated Full Page) -->
  <main class="container" style="flex-grow:1; max-width:960px; margin:2.5rem auto 4rem auto; padding:0 1rem;">
    <div id="standaloneArticleHost">
      <!-- Article injected dynamically via renderDedicatedArticlePage() -->
    </div>

    <!-- Related Articles Section -->
    <section class="article-related-section" id="articleRelatedSection" style="margin-top:4rem; padding-top:2.5rem; border-top:1px solid var(--color-border-hairline);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem;">
        <h3 style="font-family:var(--font-editorial); font-size:1.45rem; font-weight:800; color:var(--color-brand-primary); margin:0;">
          <i class="fas fa-newspaper" style="margin-right:0.5rem;"></i>
          <span id="relatedSectionHeading">Tin cùng chuyên mục</span>
        </h3>
        <a id="relatedCategoryLink" href="trending.html" style="font-size:0.875rem; font-weight:700; color:var(--color-brand-accent); text-decoration:none;">
          <span id="relatedViewAllText">Xem tất cả</span> &rarr;
        </a>
      </div>
      <div id="relatedArticlesGrid" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:1.5rem;">
        <!-- Injected dynamically -->
      </div>
    </section>
  </main>

  <!-- Footer -->
  <footer class="fashion-footer">
    <div class="container">
      <div class="footer-grid-top">
        <div class="footer-col-brand">
          <a href="index.html" class="footer-brand-logo">HEARTICLES.</a>
          <p class="footer-brand-tagline" data-i18n="footer_tagline">Where News Begins with a Heartbeat.</p>
          <p class="footer-academic-credit">Class 6 Group 1 Term 127 • Faculty of English Language and Culture • ULIS - VNU</p>
        </div>
      </div>
      <div class="footer-bottom-bar">
        <p class="footer-copyright">&copy; 2026 Class6group1term127 • All Rights Reserved.</p>
      </div>
    </div>
  </footer>

  <!-- Search Modal -->
  <div class="fashion-modal-backdrop" id="searchModal" onclick="closeSearchModal(event)">
    <div class="fashion-search-modal-box" onclick="event.stopPropagation()">
      <div class="search-input-wrap">
        <i class="fas fa-search search-icon"></i>
        <input type="text" id="searchInput" class="search-input" placeholder="Tìm kiếm bài viết..." oninput="handleInstantSearch(this.value)">
        <button class="search-close-btn" onclick="closeSearchModal()"><i class="fas fa-times"></i></button>
      </div>
      <div class="search-results-container" id="searchResultsContainer"></div>
    </div>
  </div>

  <!-- Subscribe Modal -->
  <div class="fashion-modal-backdrop" id="subscribeModal" onclick="closeSubscribeModal(event)">
    <div class="fashion-subscribe-modal-box" onclick="event.stopPropagation()">
      <button class="modal-close-icon" onclick="closeSubscribeModal()"><i class="fas fa-times"></i></button>
      <h3 style="font-family:var(--font-editorial); font-size:1.6rem; margin-bottom:0.75rem; color:var(--color-brand-primary);">HEARTICLES. DISPATCH</h3>
      <p style="color:var(--color-text-muted); font-size:0.9rem; margin-bottom:1.5rem;">Đăng ký nhận tuyển tập những câu chuyện nhân văn sâu lắng mỗi tuần.</p>
      <form onsubmit="handleSubscribeSubmit(event)" style="display:flex; flex-direction:column; gap:0.75rem;">
        <input type="email" id="subscribeEmailInput" required placeholder="Nhập địa chỉ email của bạn..." style="padding:0.75rem 1rem; border:1px solid var(--color-border-hairline); border-radius:var(--radius-md); font-size:0.95rem; outline:none;">
        <button type="submit" class="fashion-btn-pill" style="padding:0.8rem; background:var(--color-brand-primary); color:#FFF; font-weight:700; border:none; cursor:pointer;">Đăng ký ngay</button>
      </form>
    </div>
  </div>

  <!-- User Sign-in Modal -->
  <div class="fashion-modal-backdrop" id="signinModal" onclick="closeSignInModal(event)">
    <div class="fashion-subscribe-modal-box" onclick="event.stopPropagation()">
      <button class="modal-close-icon" onclick="closeSignInModal()"><i class="fas fa-times"></i></button>
      <div style="text-align:center; margin-bottom:1.25rem;">
        <i class="far fa-user-circle" style="font-size:3rem; color:var(--color-brand-primary);"></i>
        <h3 style="font-family:var(--font-editorial); font-size:1.5rem; margin-top:0.5rem; color:var(--color-brand-primary);" id="signinModalTitle">Đăng nhập tài khoản</h3>
      </div>
      <form onsubmit="handleSignInSubmit(event)" style="display:flex; flex-direction:column; gap:0.75rem;">
        <input type="text" id="signinUsernameInput" required placeholder="Tên độc giả / Username..." style="padding:0.75rem 1rem; border:1px solid var(--color-border-hairline); border-radius:var(--radius-md); font-size:0.95rem; outline:none;">
        <button type="submit" class="fashion-btn-pill" style="padding:0.8rem; background:var(--color-brand-primary); color:#FFF; font-weight:700; border:none; cursor:pointer;">Xác nhận</button>
      </form>
    </div>
  </div>

  <!-- Mobile Navigation Drawer -->
  <div class="fashion-drawer-backdrop" id="fashionDrawerBackdrop" onclick="closeDrawer()"></div>
  <aside class="fashion-drawer" id="fashionDrawer">
    <div class="drawer-header">
      <span class="drawer-brand">HEARTICLES.</span>
      <button class="drawer-close-btn" onclick="closeDrawer()"><i class="fas fa-times"></i></button>
    </div>
    <nav class="drawer-nav">
      <a href="index.html" class="drawer-nav-item" data-i18n="nav_home">Home</a>
      <a href="trending.html" class="drawer-nav-item" data-i18n="nav_trending">Trending</a>
      <a href="society.html" class="drawer-nav-item" data-i18n="nav_society">Society</a>
      <a href="human-stories.html" class="drawer-nav-item" data-i18n="nav_human_stories">Human Stories</a>
      <a href="mind-soul.html" class="drawer-nav-item" data-i18n="nav_mind_soul">Mind & Soul</a>
      <a href="in-depth.html" class="drawer-nav-item" data-i18n="nav_indepth">In-depth</a>
      <a href="about.html" class="drawer-nav-item" data-i18n="nav_about">About Us</a>
    </nav>
  </aside>

  <!-- Core Scripts -->
  <script src="js/data.js"></script>
  <script src="js/translations.js"></script>
  <script src="js/app.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      initArticlePage();
    });

    function initArticlePage() {
      const urlParams = new URLSearchParams(window.location.search);
      const articleId = urlParams.get('id') || 'trending-1';
      renderDedicatedArticlePage(articleId);
    }
  </script>
</body>
</html>
"""

with open(ARTICLE_HTML_PATH, "w", encoding="utf-8") as f:
    f.write(article_html_content)
print("SUCCESS: Created article.html.")

# =====================================================================
# 2. UPDATE JS/APP.JS
# =====================================================================
print("2. Updating js/app.js for direct page navigation and renderDedicatedArticlePage...")
with open(APP_PATH, "r", encoding="utf-8") as f:
    app_code = f.read()

# 2.1 Update openArticleModal to NAVIGATE to distinct link instead of opening popup modal
old_open_modal_full = """function openArticleModal(articleId) {

  const article = ARTICLES_DATA.find(a => a.id === articleId);
  if (!article) return;

  const modal = document.getElementById('articleReaderModal');
  const body = document.getElementById('articleModalBody');
  if (!modal || !body) return;"""

new_open_modal_nav = """function getArticleUrl(articleId) {
  if (articleId === 'trending-1') {
    const isSub = window.location.pathname.includes('/hearticles/');
    return isSub ? 'index.html' : 'hearticles/madeuparticle/index.html';
  }
  const isSub = window.location.pathname.includes('/hearticles/');
  const prefix = isSub ? '../../' : '';
  return `${prefix}article.html?id=${encodeURIComponent(articleId)}`;
}
window.getArticleUrl = getArticleUrl;

function openArticleModal(articleId) {
  // Direct navigation: each article has its own dedicated link/page!
  const targetUrl = getArticleUrl(articleId);
  window.location.href = targetUrl;
}
window.openArticleModal = openArticleModal;

function openArticleModalLegacy(articleId) {
  const article = ARTICLES_DATA.find(a => a.id === articleId);
  if (!article) return;

  const modal = document.getElementById('articleReaderModal');
  const body = document.getElementById('articleModalBody');
  if (!modal || !body) return;"""

if old_open_modal_full in app_code:
    app_code = app_code.replace(old_open_modal_full, new_open_modal_nav)
    print("SUCCESS: Replaced openArticleModal with direct URL navigation.")
else:
    print("WARNING: old_open_modal_full not found verbatim, checking regex...")
    app_code = re.sub(
        r"function openArticleModal\(articleId\)\s*\{\s*const article = ARTICLES_DATA\.find\(a => a\.id === articleId\);\s*if \(!article\) return;\s*const modal = document\.getElementById\('articleReaderModal'\);\s*const body = document\.getElementById\('articleModalBody'\);\s*if \(!modal \|\| !body\) return;",
        new_open_modal_nav,
        app_code
    )
    print("SUCCESS (via regex): Replaced openArticleModal.")

# 2.2 Add renderDedicatedArticlePage to js/app.js
dedicated_renderer = """
/* ===================================================================
   DEDICATED FULL-PAGE ARTICLE RENDERER (article.html)
   =================================================================== */
function renderDedicatedArticlePage(articleId) {
  const host = document.getElementById('standaloneArticleHost');
  if (!host || typeof ARTICLES_DATA === 'undefined') return;

  const article = ARTICLES_DATA.find(a => a.id === articleId) || ARTICLES_DATA[0];
  if (!article) return;

  const isEn = (currentLanguage === 'en');
  const title = (isEn && article.title_en) ? article.title_en : article.title;
  const subtitle = (isEn && article.subtitle_en) ? article.subtitle_en : article.subtitle;
  const readTime = isEn ? (article.readTime || '').replace('phút đọc', 'min read') : article.readTime;
  const breadcrumbHome = isEn ? 'Home' : 'Trang chủ';
  const breadcrumbCategory = article.categoryName || 'Trending';
  const categoryUrl = `${article.category}.html`;

  // Update document title
  document.title = `Class6group1term127 - ${title}`;

  // Update active nav category
  document.querySelectorAll('.fashion-nav .nav-item').forEach(el => {
    if (el.getAttribute('href') === categoryUrl) {
      el.classList.add('active');
    } else if (el.getAttribute('href') !== 'index.html') {
      el.classList.remove('active');
    }
  });

  const savedComments = JSON.parse(localStorage.getItem(`comments_${article.id}`) || '[]');
  const isLiked = localStorage.getItem(`liked_${article.id}`) === 'true';

  let bodyHtml = '';
  const contentSource = (isEn && article.content_en) ? article.content_en : article.content;
  if (typeof contentSource === 'string') {
    bodyHtml = contentSource;
  } else if (Array.isArray(contentSource)) {
    bodyHtml = contentSource.map(p => {
      if (typeof p !== 'string') return '';
      let trimmed = p.trim();
      if (trimmed.startsWith('### ')) {
        return `<h3 class="article-section-heading" style="font-family:var(--font-editorial); font-size:1.45rem; font-weight:800; color:var(--color-brand-primary); margin:2rem 0 0.85rem 0;">${trimmed.replace('### ', '')}</h3>`;
      }
      if (trimmed.startsWith('## ')) {
        return `<h2 class="article-section-heading-lg" style="font-family:var(--font-editorial); font-size:1.65rem; font-weight:800; color:var(--color-brand-primary); margin:2.25rem 0 1rem 0;">${trimmed.replace('## ', '')}</h2>`;
      }
      if (trimmed.startsWith('<figure') || trimmed.startsWith('<table') || trimmed.startsWith('<div') || trimmed.startsWith('<blockquote')) {
        if (trimmed.includes('<img') && !trimmed.includes('onerror=')) {
          trimmed = trimmed.replace(/<img\\b/g, '<img onerror="handleImageError(this)"');
        }
        return trimmed;
      }
      return `<p style="margin-bottom:1.25rem; line-height:1.85; text-align:justify; font-size:1.15rem; color:var(--color-text-body);">${p}</p>`;
    }).join('');
  }

  host.innerHTML = `
    <article class="article-reading-content" style="font-size: ${currentFontSize}rem;">
      <div class="article-breadcrumb" style="display:flex; align-items:center; gap:0.5rem; font-size:0.875rem; color:var(--color-text-muted); margin-bottom:1.25rem; flex-wrap:wrap;">
        <a href="index.html" style="color:var(--color-brand-primary); font-weight:600; text-decoration:none;">${breadcrumbHome}</a>
        <span>/</span>
        <a href="${categoryUrl}" style="color:var(--color-brand-primary); font-weight:600; text-decoration:none;">${breadcrumbCategory}</a>
        <span>/</span>
        <span style="color:var(--color-brand-accent); font-weight:700;">${article.id}</span>
      </div>

      <h1 class="article-headline" style="font-family:var(--font-editorial); font-size:clamp(1.85rem, 4vw, 2.75rem); font-weight:900; line-height:1.25; margin-bottom:1rem; color:var(--color-text-headline); letter-spacing:-0.02em;">${title}</h1>
      <p class="article-sapo" style="font-family:var(--font-serif); font-size:clamp(1.1rem, 2vw, 1.3rem); line-height:1.65; color:var(--color-text-muted); margin-bottom:1.75rem; font-style:italic;">${subtitle}</p>

      <div class="article-author-strip" style="display:flex; justify-content:space-between; align-items:center; padding-bottom:1.25rem; border-bottom:1px solid var(--color-border-hairline); margin-bottom:2rem; flex-wrap:wrap; gap:1rem;">
        <div class="article-author-info" style="display:flex; align-items:center; gap:0.75rem;">
          <div class="author-avatar-small" style="width:46px; height:46px; border-radius:50%; background:var(--color-brand-primary); color:#FFF; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:1.1rem;">${article.author.charAt(0)}</div>
          <div>
            <div class="author-name-text" style="font-weight:700; color:var(--color-text-headline); font-size:1rem;">${article.author}</div>
            <div class="article-date-text" style="font-size:0.8rem; color:var(--color-text-muted); margin-top:2px;"><i class="far fa-clock"></i> ${article.date}</div>
          </div>
        </div>

        <div class="article-reading-tools" style="display:flex; align-items:center; gap:0.5rem; flex-wrap:wrap;">
          <button class="tool-btn" onclick="adjustFontSize(-0.1)" title="${isEn ? 'Decrease Font' : 'Giảm cỡ chữ'}"><i class="fas fa-font"></i> A-</button>
          <button class="tool-btn" onclick="adjustFontSize(0.1)" title="${isEn ? 'Increase Font' : 'Tăng cỡ chữ'}"><i class="fas fa-font"></i> A+</button>
          <button class="tool-btn ${isSpeaking ? 'active' : ''}" id="btnTTS" onclick="toggleTextToSpeech('${article.id}')" title="${isEn ? 'Text to Speech' : 'Nghe đọc bài báo'}">
            <i class="fas ${isSpeaking ? 'fa-pause' : 'fa-volume-up'}"></i> <span>${isSpeaking ? (isEn ? 'Pause' : 'Tạm dừng') : (isEn ? 'Listen' : 'Đọc bài báo')}</span>
          </button>
          <button class="btn-article-like ${isLiked ? 'liked' : ''}" id="likeBtn_${article.id}" onclick="toggleLikeArticle('${article.id}')" title="${isEn ? 'Like Story' : 'Thả tim bài viết'}">
            <i class="fas fa-heart"></i> <span id="likeCount_${article.id}">${article.likes + (isLiked ? 1 : 0)}</span>
          </button>
          <button class="tool-btn" onclick="shareArticle('${title.replace(/'/g, "\\\\'")}')" title="${isEn ? 'Share' : 'Chia sẻ'}"><i class="fas fa-share-alt"></i> <span>${isEn ? 'Share' : 'Chia sẻ'}</span></button>
        </div>
      </div>

      <div class="article-hero-media" style="border-radius:var(--radius-lg); overflow:hidden; margin:2rem 0; box-shadow:0 6px 24px rgba(0,0,0,0.06);">
        <img src="${article.image}" alt="${title}" style="width:100%; display:block; max-height:560px; object-fit:cover;" onerror="handleImageError(this)">
        <div class="article-media-caption" style="font-size:0.85rem; color:var(--color-text-muted); padding:0.6rem 0.5rem; font-style:italic; line-height:1.5;">${article.imageCaption || title}</div>
      </div>

      ${renderModalVideoBlock(article, isEn, title)}

      <div class="article-body-text" id="articleBodyContent" style="font-family:var(--font-body); font-size:1.15rem; line-height:1.85; color:var(--color-text-body);">
        ${bodyHtml}
        ${formatArticleSource(article, isEn)}
      </div>

      <!-- Comments Block -->
      <div class="article-comments-block" style="margin-top:3.5rem; padding-top:2rem; border-top:1px solid var(--color-border-hairline);">
        <h3 style="font-family:var(--font-editorial); font-size:1.45rem; color:var(--color-text-headline); margin-bottom:1.25rem;">
          <i class="far fa-comments" style="color:var(--color-brand-primary);"></i> ${isEn ? 'Reader Discussion' : 'Bình luận & Thảo luận'} (<span id="commentCount">${savedComments.length}</span>)
        </h3>
        
        <div class="comment-form-wrap" style="display:flex; gap:0.75rem; margin-bottom:1.5rem;">
          <input type="text" class="comment-input-field" id="newCommentInput" placeholder="${isEn ? 'Share your reflection on this story...' : 'Chia sẻ góc nhìn nhân văn của bạn về bài viết này...'}" onkeypress="if(event.key === 'Enter') submitComment('${article.id}')" style="flex-grow:1; padding:0.75rem 1rem; border:1px solid var(--color-border-hairline); border-radius:var(--radius-full); font-size:0.95rem; outline:none;">
          <button class="comment-submit-btn fashion-btn-pill" onclick="submitComment('${article.id}')" style="padding:0.75rem 1.5rem; background:var(--color-brand-primary); color:#FFF; font-weight:700; border:none; cursor:pointer;">${isEn ? 'Submit' : 'Gửi'}</button>
        </div>

        <div class="comments-list-container" id="commentsListContainer">
          ${savedComments.length === 0 ? `<p style="color:var(--color-text-muted); font-size:0.9rem; font-style:italic;">${isEn ? 'Be the first to share your heartfelt thoughts on this story.' : 'Hãy là người đầu tiên chia sẻ cảm nghĩ về bài viết này.'}</p>` : ''}
          ${savedComments.map(c => `
            <div class="comment-item-card" style="background:#FFFFFF; border:1px solid var(--color-border-hairline); border-radius:var(--radius-md); padding:0.85rem 1rem; margin-bottom:0.75rem; box-shadow:0 2px 8px rgba(0,0,0,0.03);">
              <div style="display:flex; justify-content:space-between; margin-bottom:0.35rem;">
                <strong style="color:var(--color-brand-primary); font-size:0.9rem;">${c.author}</strong>
                <span style="font-size:0.75rem; color:var(--color-text-muted);">${c.time}</span>
              </div>
              <p style="font-size:0.9rem; color:var(--color-text-body); margin:0;">${c.text}</p>
            </div>
          `).join('')}
        </div>
      </div>
    </article>
  `;

  // Render related articles
  renderRelatedArticles(article, isEn);
}
window.renderDedicatedArticlePage = renderDedicatedArticlePage;

function renderRelatedArticles(currentArt, isEn) {
  const grid = document.getElementById('relatedArticlesGrid');
  const heading = document.getElementById('relatedSectionHeading');
  const viewAll = document.getElementById('relatedViewAllText');
  const catLink = document.getElementById('relatedCategoryLink');
  if (!grid || typeof ARTICLES_DATA === 'undefined') return;

  if (heading) heading.textContent = isEn ? 'More In This Category' : 'Tin cùng chuyên mục';
  if (viewAll) viewAll.textContent = isEn ? 'View Category' : 'Xem tất cả';
  if (catLink) catLink.href = `${currentArt.category}.html`;

  const related = ARTICLES_DATA
    .filter(a => a.category === currentArt.category && a.id !== currentArt.id)
    .slice(0, 3);

  grid.innerHTML = related.map(item => {
    const rTitle = (isEn && item.title_en) ? item.title_en : item.title;
    const rExcerpt = (isEn && item.subtitle_en) ? item.subtitle_en : item.subtitle;
    const rUrl = getArticleUrl(item.id);
    return `
      <article class="fashion-article-card" onclick="window.location.href='${rUrl}'" style="cursor:pointer; background:#FFFFFF; border:1px solid var(--color-border-hairline); border-radius:var(--radius-md); overflow:hidden; display:flex; flex-direction:column;">
        <div style="aspect-ratio:16/10; overflow:hidden;">
          <img src="${item.image}" alt="${rTitle}" style="width:100%; height:100%; object-fit:cover; transition:transform 0.3s;" onmouseover="this.style.transform='scale(1.04)'" onmouseout="this.style.transform='scale(1)'" onerror="handleImageError(this)">
        </div>
        <div style="padding:1.15rem; display:flex; flex-direction:column; flex-grow:1;">
          <span style="font-size:0.725rem; font-weight:800; color:var(--color-brand-accent); letter-spacing:0.06em; text-transform:uppercase; margin-bottom:0.4rem;">${item.categoryName}</span>
          <h4 style="font-family:var(--font-editorial); font-size:1.05rem; font-weight:800; line-height:1.35; margin:0 0 0.5rem 0; color:var(--color-text-headline);">${rTitle}</h4>
          <p style="font-size:0.85rem; color:var(--color-text-muted); line-height:1.5; margin:0 0 1rem 0; flex-grow:1; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">${rExcerpt}</p>
          <span style="font-size:0.75rem; color:var(--color-brand-primary); font-weight:700;">${isEn ? 'Read Story &rarr;' : 'Đọc bài viết &rarr;'}</span>
        </div>
      </article>
    `;
  }).join('');
}
window.renderRelatedArticles = renderRelatedArticles;
"""

app_code += "\n" + dedicated_renderer

with open(APP_PATH, "w", encoding="utf-8") as f:
    f.write(app_code)
print("SUCCESS: Added renderDedicatedArticlePage and updated openArticleModal in js/app.js.")


# =====================================================================
# 3. UPDATE HEARTICLES/MADEUPARTICLE/INDEX.HTML (Clean Standalone Page)
# =====================================================================
print("3. Updating hearticles/madeuparticle/index.html to be a clean standalone page...")
with open(MADEUP_INDEX, "r", encoding="utf-8") as f:
    madeup_html = f.read()

# Update script inside madeuparticle index to render directly
old_madeup_script = """  <script>
    document.addEventListener('DOMContentLoaded', () => {
      // In this standalone route, render the article directly into the main container
      const art = ARTICLES_DATA.find(a => a.id === 'trending-1');
      if (art && typeof openArticleModal === 'function') {
        openArticleModal('trending-1');
        // Keep modal content in page view
        const modal = document.getElementById('articleReaderModal');
        if (modal) {
          modal.style.display = 'block';
          modal.style.position = 'relative';
          modal.style.zIndex = '1';
          modal.style.background = 'transparent';
        }
      }
    });
  </script>"""

new_madeup_script = """  <script>
    document.addEventListener('DOMContentLoaded', () => {
      if (typeof renderDedicatedArticlePage === 'function') {
        renderDedicatedArticlePage('trending-1');
      }
    });
  </script>"""

if old_madeup_script in madeup_html:
    madeup_html = madeup_html.replace(old_madeup_script, new_madeup_script)
    print("SUCCESS: Updated hearticles/madeuparticle script to renderDedicatedArticlePage.")

# Change id="articleModalBody" to id="standaloneArticleHost"
if 'id="articleModalBody"' in madeup_html:
    madeup_html = madeup_html.replace('id="articleModalBody"', 'id="standaloneArticleHost"')
    print("SUCCESS: Updated host ID in hearticles/madeuparticle/index.html.")

with open(MADEUP_INDEX, "w", encoding="utf-8") as f:
    f.write(madeup_html)
print("Finished updating hearticles/madeuparticle/index.html.")

print("\nALL DEDICATED ARTICLE ROUTE UPDATES COMPLETED SUCCESSFULLY!")
