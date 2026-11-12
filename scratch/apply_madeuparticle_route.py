# -*- coding: utf-8 -*-
"""
Script to set article link to /hearticles/madeuparticle:
1. Update js/data.js (sourceUrl, url, canonicalUrl, slug)
2. Update js/app.js (URL pushState on modal open/close, shareArticle link, formatArticleSource, initApp deep link router)
3. Create hearticles/madeuparticle/index.html standalone page
"""

import os
import json
import re

BASE_DIR = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127"
DATA_PATH = os.path.join(BASE_DIR, "js", "data.js")
APP_PATH = os.path.join(BASE_DIR, "js", "app.js")
TRANS_PATH = os.path.join(BASE_DIR, "js", "translations.js")
MADEUP_DIR = os.path.join(BASE_DIR, "hearticles", "madeuparticle")
MADEUP_INDEX = os.path.join(MADEUP_DIR, "index.html")

# =====================================================================
# 1. UPDATE JS/DATA.JS
# =====================================================================
print("1. Updating js/data.js...")
with open(DATA_PATH, "r", encoding="utf-8") as f:
    text = f.read()

start_marker = "const ARTICLES_DATA = "
start_idx = text.find(start_marker) + len(start_marker)
end_idx = text.rfind("];") + 1
articles = json.loads(text[start_idx:end_idx])

for a in articles:
    if a.get("id") == "trending-1":
        a["sourceUrl"] = "/hearticles/madeuparticle"
        a["url"] = "/hearticles/madeuparticle"
        a["canonicalUrl"] = "/hearticles/madeuparticle"
        a["slug"] = "hearticles/madeuparticle"
        break

new_json_str = json.dumps(articles, ensure_ascii=False, indent=2)
new_text = text[:start_idx] + new_json_str + text[end_idx:]

with open(DATA_PATH, "w", encoding="utf-8") as f:
    f.write(new_text)
print("SUCCESS: Updated trending-1 in js/data.js with /hearticles/madeuparticle.")

# =====================================================================
# 2. UPDATE JS/APP.JS
# =====================================================================
print("2. Updating js/app.js...")
with open(APP_PATH, "r", encoding="utf-8") as f:
    app_code = f.read()

# 2.1 Update formatArticleSource to display clean article link
old_source_format = """  const url = article.sourceUrl || '#';

  if (isEn) {
    return `
      <div class="article-source-citation">
        <span class="citation-label">Original Source:</span> "<em class="citation-title">${cleanTitle}</em>", <strong>${sourceName}</strong>, by ${author}, ${formattedDate}
        <a href="${url}" target="_blank" rel="noopener noreferrer" class="citation-url" title="Open original article in new tab">
          <i class="fas fa-external-link-alt" style="margin-right: 0.35rem; font-size: 0.85rem;"></i>${url}
        </a>
      </div>
    `;
  } else {
    return `
      <div class="article-source-citation">
        <span class="citation-label">Nguồn trích dẫn gốc:</span> "<em class="citation-title">${cleanTitle}</em>", <strong>${sourceName}</strong>, tác giả ${author}, ${formattedDate}
        <a href="${url}" target="_blank" rel="noopener noreferrer" class="citation-url" title="Mở bài báo gốc trong tab mới">
          <i class="fas fa-external-link-alt" style="margin-right: 0.35rem; font-size: 0.85rem;"></i>${url}
        </a>
      </div>
    `;
  }"""

new_source_format = """  const url = article.sourceUrl || '#';
  const isInternalLink = url.startsWith('/');
  const linkLabel = isEn ? (isInternalLink ? 'Article Link:' : 'Original Source:') : (isInternalLink ? 'Đường dẫn bài báo:' : 'Nguồn trích dẫn gốc:');
  const linkIcon = isInternalLink ? 'fa-link' : 'fa-external-link-alt';
  const linkTarget = isInternalLink ? '' : 'target="_blank" rel="noopener noreferrer"';

  if (isEn) {
    return `
      <div class="article-source-citation">
        <span class="citation-label">${linkLabel}</span> "<em class="citation-title">${cleanTitle}</em>", <strong>${sourceName}</strong>, by ${author}, ${formattedDate}
        <a href="${url}" ${linkTarget} class="citation-url" title="${isInternalLink ? 'Direct Article Link' : 'Open original article in new tab'}">
          <i class="fas ${linkIcon}" style="margin-right: 0.35rem; font-size: 0.85rem;"></i>${url}
        </a>
      </div>
    `;
  } else {
    return `
      <div class="article-source-citation">
        <span class="citation-label">${linkLabel}</span> "<em class="citation-title">${cleanTitle}</em>", <strong>${sourceName}</strong>, tác giả ${author}, ${formattedDate}
        <a href="${url}" ${linkTarget} class="citation-url" title="${isInternalLink ? 'Đường dẫn trực tiếp bài báo' : 'Mở bài báo gốc trong tab mới'}">
          <i class="fas ${linkIcon}" style="margin-right: 0.35rem; font-size: 0.85rem;"></i>${url}
        </a>
      </div>
    `;
  }"""

if old_source_format in app_code:
    app_code = app_code.replace(old_source_format, new_source_format)
    print("SUCCESS: Updated formatArticleSource to support internal /hearticles/madeuparticle links.")

# 2.2 Update openArticleModal to update URL and history
old_modal_activate = """  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
}
window.openArticleModal = openArticleModal;"""

new_modal_activate = """  modal.classList.add('active');
  document.body.style.overflow = 'hidden';

  // URL Routing: update URL to /hearticles/madeuparticle for trending-1
  try {
    const articleUrl = (article.url || article.sourceUrl);
    if (articleUrl && articleUrl.startsWith('/')) {
      if (window.location.protocol === 'file:') {
        window.location.hash = articleUrl.replace(/^\\//, '');
      } else {
        history.pushState({ articleId: article.id }, '', articleUrl);
      }
    }
  } catch (e) {}
}
window.openArticleModal = openArticleModal;"""

if old_modal_activate in app_code:
    app_code = app_code.replace(old_modal_activate, new_modal_activate)
    print("SUCCESS: Added URL history routing to openArticleModal.")

# 2.3 Update closeArticleModal to reset URL
old_close_modal = """function closeArticleModal() {
  const modal = document.getElementById('articleReaderModal');
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';"""

new_close_modal = """function closeArticleModal() {
  const modal = document.getElementById('articleReaderModal');
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';

    // Revert URL when closing modal
    try {
      if (window.location.hash.includes('madeuparticle')) {
        history.pushState(null, '', window.location.pathname);
      } else if (window.location.pathname.includes('/hearticles/madeuparticle')) {
        history.pushState(null, '', 'index.html');
      }
    } catch (e) {}"""

if old_close_modal in app_code:
    app_code = app_code.replace(old_close_modal, new_close_modal)
    print("SUCCESS: Added URL reset to closeArticleModal.")

# 2.4 Update shareArticle to share /hearticles/madeuparticle
old_share = """function shareArticle(title) {
  if (navigator.share) {
    navigator.share({
      title: title,
      text: `${title} - HEARTICLES. (ULIS - VNU)`,
      url: window.location.href
    }).catch(() => {});
  } else {
    navigator.clipboard.writeText(window.location.href);
    showToast(currentLanguage === 'en' ? 'Article link copied!' : 'Đã sao chép liên kết bài viết!', 'link');
  }
}"""

new_share = """function shareArticle(title) {
  const modal = document.getElementById('articleReaderModal');
  let targetUrl = window.location.href;
  if (modal && modal.dataset.articleId === 'trending-1') {
    targetUrl = (window.location.origin && window.location.origin !== 'null')
      ? `${window.location.origin}/hearticles/madeuparticle`
      : '/hearticles/madeuparticle';
  }

  if (navigator.share) {
    navigator.share({
      title: title,
      text: `${title} - HEARTICLES. (ULIS - VNU)`,
      url: targetUrl
    }).catch(() => {});
  } else {
    navigator.clipboard.writeText(targetUrl);
    showToast(currentLanguage === 'en' ? `Article link copied: ${targetUrl}` : `Đã sao chép liên kết: ${targetUrl}`, 'link');
  }
}"""

if old_share in app_code:
    app_code = app_code.replace(old_share, new_share)
    print("SUCCESS: Updated shareArticle to share /hearticles/madeuparticle.")

# 2.5 Add route checker on initApp
if "checkInitialArticleRoute" not in app_code:
    route_check_func = """
/* ===================================================================
   DEEP LINK ROUTE CHECKER (/hearticles/madeuparticle)
   =================================================================== */
function checkInitialArticleRoute() {
  const path = window.location.pathname.toLowerCase();
  const hash = window.location.hash.toLowerCase();
  if (path.includes('madeuparticle') || hash.includes('madeuparticle')) {
    setTimeout(() => {
      openArticleModal('trending-1');
    }, 150);
  }
}
"""
    app_code += "\n" + route_check_func
    # Call inside initApp
    app_code = app_code.replace("setupStickyHeader();", "setupStickyHeader();\n  checkInitialArticleRoute();")
    print("SUCCESS: Added checkInitialArticleRoute to initApp.")

with open(APP_PATH, "w", encoding="utf-8") as f:
    f.write(app_code)
print("Finished updating js/app.js.")


# =====================================================================
# 3. CREATE STANDALONE ROUTE: hearticles/madeuparticle/index.html
# =====================================================================
print("3. Creating hearticles/madeuparticle/index.html...")
os.makedirs(MADEUP_DIR, exist_ok=True)

standalone_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Class6group1term127 - Drunk Girl Collapses on Park Bench</title>
  <meta name="description" content="Hot Paper: Drunk Girl Collapses on Park Bench, Unexpectedly Receives 'Special' Kindness from Strangers - HEARTICLES. Magazine">
  <link rel="canonical" href="/hearticles/madeuparticle">
  <link rel="icon" type="image/svg+xml" href="../../assets/images/logo/heart-logo.svg">
  
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
      img.onerror = null;
      img.src = '../../assets/images/trending/ngoc_mai/hat_and_jacket.jpg';
    }
  </script>
  <link rel="stylesheet" href="../../css/tokens.css">
  <link rel="stylesheet" href="../../css/style.css">
  <meta name="application-name" content="Class6group1term127">
  <meta property="og:site_name" content="Class6group1term127">
  <meta property="og:url" content="/hearticles/madeuparticle">
  <meta property="og:title" content="Drunk Girl Collapses on Park Bench, Unexpectedly Receives 'Special' Kindness from Strangers">
  <meta property="og:image" content="../../assets/images/trending/ngoc_mai/hat_and_jacket.jpg">
</head>
<body data-category="trending">
  <!-- Reading Progress Bar -->
  <div class="reading-progress-bar" id="readingProgressBar"></div>

  <!-- Editorial Sticky Header -->
  <header class="fashion-header">
    <div class="container fashion-header-container">
      <a href="../../index.html" class="fashion-mobile-brand" aria-label="HEARTICLES. - Home">HEARTICLES.</a>
      <nav class="fashion-nav" aria-label="Navigation">
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
        <button class="fashion-search-btn" onclick="openSearchModal()" title="Search" aria-label="Search"><i class="fas fa-search"></i></button>
        <button class="fashion-subscribe-btn" onclick="openSubscribeModal()" title="Subscribe">Subscribe</button>
        <button class="fashion-user-btn" id="headerUserBtn" onclick="openSignInModal()" title="Sign In"><i class="far fa-user-circle"></i></button>
        <button class="fashion-hamburger-btn" onclick="openDrawer()" aria-label="Menu"><i class="fas fa-bars"></i></button>
      </div>
    </div>
  </header>

  <!-- Main Article Body -->
  <main class="container" style="flex-grow:1; max-width:960px; margin:2.5rem auto; padding:0 1rem;">
    <div class="article-breadcrumb" style="display:flex; align-items:center; gap:0.5rem; font-size:0.875rem; color:var(--color-text-muted); margin-bottom:1.25rem;">
      <a href="../../index.html" style="color:var(--color-brand-primary); font-weight:600; text-decoration:none;">Home</a>
      <span>/</span>
      <a href="../../trending.html" style="color:var(--color-brand-primary); font-weight:600; text-decoration:none;">Trending</a>
      <span>/</span>
      <span style="color:var(--color-brand-accent); font-weight:700;">/hearticles/madeuparticle</span>
    </div>

    <!-- Article Reader Container -->
    <div id="articleModalBody"></div>
  </main>

  <!-- Footer -->
  <footer class="fashion-footer" style="margin-top:4rem; border-top:1px solid var(--color-border-hairline); padding:2rem 0; text-align:center; color:var(--color-text-muted); font-size:0.875rem;">
    <div class="container">
      <p style="margin:0 0 0.5rem 0; font-weight:700; color:var(--color-brand-primary); font-family:var(--font-editorial); font-size:1.25rem;">HEARTICLES.</p>
      <p style="margin:0;">Class6group1term127 • Faculty of English Language and Culture • ULIS - VNU</p>
      <p style="margin:0.25rem 0 0 0; font-size:0.8rem;">Canonical Link: <a href="/hearticles/madeuparticle" style="color:var(--color-brand-accent);">/hearticles/madeuparticle</a></p>
    </div>
  </footer>

  <!-- Core Scripts -->
  <script src="../../js/data.js"></script>
  <script src="../../js/translations.js"></script>
  <script src="../../js/app.js"></script>
  <script>
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
  </script>
</body>
</html>
"""

with open(MADEUP_INDEX, "w", encoding="utf-8") as f:
    f.write(standalone_html)
print("SUCCESS: Created hearticles/madeuparticle/index.html.")

print("\nALL URL UPDATES COMPLETED SUCCESSFULLY!")
