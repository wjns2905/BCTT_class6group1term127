# -*- coding: utf-8 -*-
"""
Fix hearticles/madeuparticle/index.html and ensure article.html works flawlessly.
"""

import os

BASE_DIR = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127"
MADEUP_INDEX = os.path.join(BASE_DIR, "hearticles", "madeuparticle", "index.html")
ARTICLE_HTML = os.path.join(BASE_DIR, "article.html")
APP_JS = os.path.join(BASE_DIR, "js", "app.js")

# 1. Update hearticles/madeuparticle/index.html:
# Remove <base href="../../"> which caused double relative path resolution (404s on CSS/JS).
# Use exact same full layout as article.html but with ../../ paths.
madeup_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Class6group1term127 - Drunk Girl Collapses on Park Bench</title>
  <meta name="description" content="Hot Paper: Drunk Girl Collapses on Park Bench, Unexpectedly Receives 'Special' Kindness from Strangers - HEARTICLES. Magazine">
  <link rel="canonical" href="/hearticles/madeuparticle">
  <link rel="icon" type="image/svg+xml" href="../../assets/images/logo/heart-logo.svg">
  
  <!-- Typography: Plus Jakarta Sans & Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600;1,700&display=swap" rel="stylesheet">
  
  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  
  <!-- Main Stylesheets -->
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <script>
    function handleImageError(img) {
      if (!img) return;
      const cur = img.getAttribute('src') || '';
      if (!img.dataset.triedFallback) {
        img.dataset.triedFallback = 'true';
        if (cur.startsWith('assets/')) {
          img.src = '../../' + cur;
          return;
        }
      }
      img.onerror = null;
      img.src = '../../assets/images/trending/image8.jpg';
    }
  </script>
  <link rel="stylesheet" href="../../css/tokens.css">
  <link rel="stylesheet" href="../../css/style.css">
  <meta name="application-name" content="Class6group1term127">
  <meta property="og:site_name" content="Class6group1term127">
</head>
<body data-category="trending">
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
        <img src="../../assets/images/ads/header_ad_banner.png" alt="British Council IELTS One Skill Retake Leaderboard Ad" class="header-ad-banner-img" width="1444" height="378">
      </a>
    </div>
  </div>

  <!-- Brand Masthead Hero -->
  <div class="fashion-masthead-hero">
    <div class="container masthead-hero-inner">
      <a href="../../index.html" class="fashion-brand-logo-masthead" aria-label="HEARTICLES. - Where News Begins with a Heartbeat">
        <img src="../../assets/images/logo/brand_logo_updated.png" alt="HEARTICLES. - Where News Begins with a Heartbeat" class="fashion-brand-logo-fullsize">
      </a>
    </div>
  </div>

  <!-- Sticky Categories Header Navigation -->
  <header class="fashion-header">
    <div class="container fashion-header-container">
      <a href="../../index.html" class="fashion-mobile-brand" aria-label="HEARTICLES. - Home">HEARTICLES.</a>
      <nav class="fashion-nav" aria-label="Thanh điều hướng tạp chí">
        <a href="../../index.html" class="nav-item">Home</a>
        <a href="../../trending.html" class="nav-item active">Trending</a>
        <a href="../../society.html" class="nav-item">Society</a>
        <a href="../../human-stories.html" class="nav-item">Human Stories</a>
        <a href="../../mind-soul.html" class="nav-item">Mind & Soul</a>
        <a href="../../in-depth.html" class="nav-item">In-depth</a>
        <a href="../../about.html" class="nav-item">About Us</a>
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
      <!-- Article injected dynamically via renderDedicatedArticlePage('trending-1') -->
    </div>

    <!-- Related Articles Section -->
    <section class="article-related-section" id="articleRelatedSection" style="margin-top:4rem; padding-top:2.5rem; border-top:1px solid var(--color-border-hairline);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem;">
        <h3 style="font-family:var(--font-editorial); font-size:1.45rem; font-weight:800; color:var(--color-brand-primary); margin:0;">
          <i class="fas fa-newspaper" style="margin-right:0.5rem;"></i>
          <span id="relatedSectionHeading">Tin cùng chuyên mục</span>
        </h3>
        <a id="relatedCategoryLink" href="../../trending.html" style="font-size:0.875rem; font-weight:700; color:var(--color-brand-accent); text-decoration:none;">
          <span id="relatedViewAllText">Xem tất cả</span> &rarr;
        </a>
      </div>
      <div id="relatedArticlesGrid" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:1.5rem;"></div>
    </section>
  </main>

  <!-- Footer -->
  <footer class="fashion-footer">
    <div class="container">
      <div class="footer-grid-top">
        <div class="footer-col-brand">
          <a href="../../index.html" class="footer-brand-logo">HEARTICLES.</a>
          <p class="footer-brand-tagline">Where News Begins with a Heartbeat.</p>
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

  <!-- Mobile Drawer -->
  <div class="fashion-drawer-backdrop" id="fashionDrawerBackdrop" onclick="closeDrawer()"></div>
  <aside class="fashion-drawer" id="fashionDrawer">
    <div class="drawer-header">
      <span class="drawer-brand">HEARTICLES.</span>
      <button class="drawer-close-btn" onclick="closeDrawer()"><i class="fas fa-times"></i></button>
    </div>
    <nav class="drawer-nav">
      <a href="../../index.html" class="drawer-nav-item">Home</a>
      <a href="../../trending.html" class="drawer-nav-item">Trending</a>
      <a href="../../society.html" class="drawer-nav-item">Society</a>
      <a href="../../human-stories.html" class="drawer-nav-item">Human Stories</a>
      <a href="../../mind-soul.html" class="drawer-nav-item">Mind & Soul</a>
      <a href="../../in-depth.html" class="drawer-nav-item">In-depth</a>
      <a href="../../about.html" class="drawer-nav-item">About Us</a>
    </nav>
  </aside>

  <!-- Core Scripts -->
  <script src="../../js/data.js"></script>
  <script src="../../js/translations.js"></script>
  <script src="../../js/app.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      if (typeof renderDedicatedArticlePage === 'function') {
        renderDedicatedArticlePage('trending-1');
      }
    });
  </script>
</body>
</html>
"""

with open(MADEUP_INDEX, "w", encoding="utf-8") as f:
    f.write(madeup_html)
print("SUCCESS: Rewrote hearticles/madeuparticle/index.html with full layout and correct relative paths.")

# 2. Update getArticleUrl in js/app.js:
# Ensure getArticleUrl always returns a valid, working, direct URL
with open(APP_JS, "r", encoding="utf-8") as f:
    app_text = f.read()

target_url_func = """function getArticleUrl(articleId) {
  if (articleId === 'trending-1') {
    const isSub = window.location.pathname.includes('/hearticles/');
    return isSub ? 'index.html' : 'hearticles/madeuparticle/index.html';
  }
  const isSub = window.location.pathname.includes('/hearticles/');
  const prefix = isSub ? '../../' : '';
  return `${prefix}article.html?id=${encodeURIComponent(articleId)}`;
}"""

replacement_url_func = """function getArticleUrl(articleId) {
  const isSub = window.location.pathname.includes('/hearticles/');
  if (articleId === 'trending-1') {
    return isSub ? 'index.html' : 'hearticles/madeuparticle/index.html';
  }
  const prefix = isSub ? '../../' : '';
  return `${prefix}article.html?id=${encodeURIComponent(articleId)}`;
}"""

if target_url_func in app_text:
    app_text = app_text.replace(target_url_func, replacement_url_func)
    with open(APP_JS, "w", encoding="utf-8") as f:
        f.write(app_text)
    print("SUCCESS: Verified getArticleUrl in app.js.")

print("\nFix script completed.")
