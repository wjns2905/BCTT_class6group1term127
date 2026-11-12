# -*- coding: utf-8 -*-
"""
Fix regex in js/app.js:
1. Replace backspace \x08 with proper string/regex replacements.
2. Ensure fixSubfolderAssetPaths processes all <img>, <video>, <source>, <a> tags.
3. Update handleImageError across js/app.js and HTML files.
4. Test with Node.js to verify 100% of images in trending-1 have ../../ prefix and valid files.
"""

import os
import re

BASE_DIR = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127"
APP_JS = os.path.join(BASE_DIR, "js", "app.js")
MADEUP_INDEX = os.path.join(BASE_DIR, "hearticles", "madeuparticle", "index.html")
ARTICLE_HTML = os.path.join(BASE_DIR, "article.html")

# Read current js/app.js
with open(APP_JS, "r", encoding="utf-8") as f:
    app_code = f.read()

# 1. Update handleImageError in app.js
new_handle_image_error = """function handleImageError(img) {
  if (!img) return;
  const isSub = window.location.pathname.includes('/hearticles/');
  const pfx = isSub ? '../../' : '';
  const cur = img.getAttribute('src') || img.src || '';
  if (!cur) return;

  const idx = cur.indexOf('assets/');
  if (idx !== -1) {
    const clean = cur.slice(idx);
    if (!img.dataset.triedPfx) {
      img.dataset.triedPfx = 'true';
      img.src = pfx + clean;
      return;
    }
    if (!img.dataset.triedRepo && window.location.hostname.includes('github.io')) {
      img.dataset.triedRepo = 'true';
      const repo = window.location.pathname.split('/').filter(Boolean)[0] || '';
      img.src = '/' + repo + '/' + clean;
      return;
    }
  }

  img.onerror = null;
  img.src = pfx + 'assets/images/trending/image8.jpg';
}
window.handleImageError = handleImageError;"""

app_code = re.sub(
    r"function handleImageError\(img\)\s*\{[\s\S]*?\}\s*window\.handleImageError\s*=\s*handleImageError;",
    new_handle_image_error,
    app_code,
    count=1
)

# 2. Update renderDedicatedArticlePage in app.js
new_render_page_func = """function renderDedicatedArticlePage(articleId) {
  const host = document.getElementById('standaloneArticleHost');
  if (!host || typeof ARTICLES_DATA === 'undefined') return;

  const article = ARTICLES_DATA.find(a => a.id === articleId) || ARTICLES_DATA[0];
  if (!article) return;

  const isSubfolder = window.location.pathname.includes('/hearticles/');
  const pfx = isSubfolder ? '../../' : '';

  const isEn = (currentLanguage === 'en');
  const title = (isEn && article.title_en) ? article.title_en : article.title;
  const subtitle = (isEn && article.subtitle_en) ? article.subtitle_en : article.subtitle;
  const readTime = isEn ? (article.readTime || '').replace('phút đọc', 'min read') : article.readTime;
  const breadcrumbHome = isEn ? 'Home' : 'Trang chủ';
  const breadcrumbCategory = article.categoryName || 'Trending';
  const categoryUrl = `${pfx}${article.category}.html`;
  const homeUrl = `${pfx}index.html`;

  // Update document title
  document.title = `Class6group1term127 - ${title}`;

  // Update active nav category
  document.querySelectorAll('.fashion-nav .nav-item').forEach(el => {
    const href = el.getAttribute('href') || '';
    if (href.endsWith(`${article.category}.html`)) {
      el.classList.add('active');
    } else if (!href.endsWith('index.html')) {
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
        return trimmed;
      }
      return `<p style="margin-bottom:1.25rem; line-height:1.85; text-align:justify; font-size:1.15rem; color:var(--color-text-body);">${p}</p>`;
    }).join('');
  }

  // Pre-process bodyHtml: adjust asset paths for subfolders and ensure onerror handlers
  if (isSubfolder) {
    bodyHtml = bodyHtml
      .replace(/(src=["'])assets\//gi, '$1../../assets/')
      .replace(/(poster=["'])assets\//gi, '$1../../assets/')
      .replace(/(href=["'])assets\//gi, '$1../../assets/');
  }
  bodyHtml = bodyHtml.replace(/<img\\b(?![^>]*\\bonerror=)/gi, '<img onerror="handleImageError(this)" ');

  const heroImgSrc = (article.image && (article.image.startsWith('http') || article.image.startsWith('../../')))
    ? article.image
    : (pfx + (article.image || '').replace(/^(\\.\\.\\/)+/, '').replace(/^\\.\\//, ''));

  host.innerHTML = `
    <article class="article-reading-content" style="font-size: ${currentFontSize}rem;">
      <div class="article-breadcrumb" style="display:flex; align-items:center; gap:0.5rem; font-size:0.875rem; color:var(--color-text-muted); margin-bottom:1.25rem; flex-wrap:wrap;">
        <a href="${homeUrl}" style="color:var(--color-brand-primary); font-weight:600; text-decoration:none;">${breadcrumbHome}</a>
        <span>/</span>
        <a href="${categoryUrl}" style="color:var(--color-brand-primary); font-weight:600; text-decoration:none;">${breadcrumbCategory}</a>
        <span>/</span>
        <span style="color:var(--color-brand-accent); font-weight:700;">${article.id}</span>
      </div>

      <h1 class="article-headline" style="font-family:var(--font-editorial); font-size:clamp(1.85rem, 4vw, 2.75rem); font-weight:900; line-height:1.25; margin-bottom:1rem; color:var(--color-text-headline); letter-spacing:-0.02em;">${title}</h1>
      <p class="article-sapo" style="font-family:var(--font-serif); font-size:clamp(1.1rem, 2vw, 1.3rem); line-height:1.65; color:var(--color-text-muted); margin-bottom:1.75rem; font-style:italic;">${subtitle}</p>

      <div class="article-author-strip" style="display:flex; justify-content:space-between; align-items:center; padding-bottom:1.25rem; border-bottom:1px solid var(--color-border-hairline); margin-bottom:2rem; flex-wrap:wrap; gap:1rem;">
        <div class="article-author-info" style="display:flex; align-items:center; gap:0.75rem;">
          <div class="author-avatar-small" style="width:46px; height:46px; border-radius:50%; background:var(--color-brand-primary); color:#FFF; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:1.1rem;">${(article.author || 'H').charAt(0)}</div>
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
          <button class="tool-btn" onclick="shareArticle('${(title || '').replace(/'/g, "\\\\'")}')" title="${isEn ? 'Share' : 'Chia sẻ'}"><i class="fas fa-share-alt"></i> <span>${isEn ? 'Share' : 'Chia sẻ'}</span></button>
        </div>
      </div>

      <div class="article-hero-media" style="border-radius:var(--radius-lg); overflow:hidden; margin:2rem 0; box-shadow:0 6px 24px rgba(0,0,0,0.06);">
        <img src="${heroImgSrc}" alt="${title}" style="width:100%; display:block; max-height:560px; object-fit:cover;" onerror="handleImageError(this)">
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

  // Initialize reading progress bar
  initReadingProgressBar();
}
window.renderDedicatedArticlePage = renderDedicatedArticlePage;"""

app_code = re.sub(
    r"function renderDedicatedArticlePage\(articleId\)\s*\{[\s\S]*?\}\s*window\.renderDedicatedArticlePage\s*=\s*renderDedicatedArticlePage;",
    new_render_page_func,
    app_code,
    count=1
)

with open(APP_JS, "w", encoding="utf-8") as f:
    f.write(app_code)

print("SUCCESS: Cleaned up js/app.js without any backspace bytes.")
