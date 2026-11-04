# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update applyLanguage
apply_old = """function applyLanguage(lang) {
  document.documentElement.lang = lang;

  // Update button active state
  document.querySelectorAll('#btnLangVI, #drawerLangVI').forEach(btn => {
    if (btn) btn.classList.toggle('active', lang === 'vi');
  });
  document.querySelectorAll('#btnLangEN, #drawerLangEN').forEach(btn => {
    if (btn) btn.classList.toggle('active', lang === 'en');
  });"""

apply_new = """function applyLanguage(lang) {
  document.documentElement.lang = lang;

  // Update button active state across all header, topbar, and drawer buttons
  document.querySelectorAll('.lang-pill-btn, #btnLangVI, #btnLangEN, #drawerLangVI, #drawerLangEN').forEach(btn => {
    const targetLang = btn.getAttribute('data-lang') || (btn.id && btn.id.includes('EN') ? 'en' : 'vi');
    btn.classList.toggle('active', targetLang === lang);
  });"""

# 2. Update renderCategoryPageArticles
render_cat_old = """function renderCategoryPageArticles() {
  const streamContainer = document.getElementById('categoryMainStream');
  const topReadContainer = document.getElementById('sidebarTopRead');
  const legacyContainer = document.getElementById('categoryArticlesGrid');

  const currentCategory = document.body.dataset.category || '';
  if (!currentCategory) return;

  const filtered = ARTICLES_DATA.filter(a => a.category.toLowerCase() === currentCategory.toLowerCase());

  if (streamContainer) {
    if (filtered.length === 0) {
      streamContainer.innerHTML = `
        <div style="text-align: center; padding: 4rem 1rem; color: var(--color-text-muted);">
          <i class="fas fa-feather" style="font-size: 2.5rem; color: var(--color-brand-accent); margin-bottom: 1rem;"></i>
          <h3 style="font-family: var(--font-editorial); font-size: 1.5rem; color: var(--color-text-headline);">Chưa có bài viết trong chuyên mục này</h3>
        </div>
      `;
    } else {
      streamContainer.innerHTML = filtered.map(item => `
        <article class="category-stream-row" onclick="openArticleModal('${item.id}')">
          <div class="category-stream-thumb-wrap">
            <img src="${item.image}" alt="${item.title}" class="category-stream-thumb" loading="lazy" onerror="handleImageError(this)">
          </div>
          <div class="category-stream-body">
            <span style="font-size:0.725rem; font-weight:800; color:var(--color-brand-accent); letter-spacing:0.06em; text-transform:uppercase; margin-bottom:0.3rem; display:block;">${item.categoryName}</span>
            <h3 class="category-stream-title">${item.title}</h3>
            <p class="category-stream-excerpt">${item.subtitle}</p>
            <div class="category-stream-footer">
              <span><i class="far fa-user"></i> ${item.author.split('•')[0].trim()}</span>
              <span><i class="far fa-clock"></i> ${item.readTime}</span>
              <span><i class="far fa-heart"></i> ${item.likes}</span>
            </div>
          </div>
        </article>
      `).join('');
    }
  } else if (legacyContainer) {
    legacyContainer.innerHTML = filtered.map(item => `
      <article class="fashion-article-card" onclick="openArticleModal('${item.id}')">
        <div class="fashion-card-media">
          <img src="${item.image}" alt="${item.title}" class="fashion-card-img" loading="lazy" onerror="handleImageError(this)">
          <span class="fashion-card-category-tag">${item.categoryName}</span>
        </div>
        <div class="fashion-card-body">
          <h3 class="fashion-card-title">${item.title}</h3>
          <p class="fashion-card-excerpt">${item.subtitle}</p>
          <div class="fashion-card-footer">
            <span class="fashion-card-byline"><i class="far fa-user"></i> ${item.author.split('•')[0].trim()}</span>
            <div class="fashion-card-stats">
              <span><i class="far fa-clock"></i> ${item.readTime}</span>
              <span><i class="far fa-heart"></i> ${item.likes}</span>
            </div>
          </div>
        </div>
      </article>
    `).join('');
  }

  // Populate sidebar top read #1 to #5
  if (topReadContainer) {
    const topArticles = [...ARTICLES_DATA]
      .sort((a, b) => (b.likes || 0) - (a.likes || 0))
      .slice(0, 5);

    topReadContainer.innerHTML = topArticles.map((art, idx) => `
      <div class="top-read-item" onclick="openArticleModal('${art.id}')">
        <span class="top-read-num">${idx + 1}</span>
        <div>
          <span style="font-size:0.6875rem; font-weight:800; color:var(--color-brand-accent); text-transform:uppercase; display:block; margin-bottom:0.15rem;">${art.categoryName}</span>
          <h4 class="top-read-headline">${art.title}</h4>
          <span style="font-size:0.75rem; color:var(--color-text-muted); font-weight:600;"><i class="far fa-eye"></i> ${art.views || '12.4K'} lượt đọc</span>
        </div>
      </div>
    `).join('');
  }
}"""

render_cat_new = """function renderCategoryPageArticles() {
  const streamContainer = document.getElementById('categoryMainStream');
  const topReadContainer = document.getElementById('sidebarTopRead');
  const legacyContainer = document.getElementById('categoryArticlesGrid');

  const currentCategory = document.body.dataset.category || '';
  if (!currentCategory) return;

  const isEn = (currentLanguage === 'en');
  const filtered = ARTICLES_DATA.filter(a => a.category.toLowerCase() === currentCategory.toLowerCase());

  if (streamContainer) {
    if (filtered.length === 0) {
      streamContainer.innerHTML = `
        <div style="text-align: center; padding: 4rem 1rem; color: var(--color-text-muted);">
          <i class="fas fa-feather" style="font-size: 2.5rem; color: var(--color-brand-accent); margin-bottom: 1rem;"></i>
          <h3 style="font-family: var(--font-editorial); font-size: 1.5rem; color: var(--color-text-headline);">${isEn ? 'No articles available in this category' : 'Chưa có bài viết trong chuyên mục này'}</h3>
        </div>
      `;
    } else {
      streamContainer.innerHTML = filtered.map(item => {
        const title = (isEn && item.title_en) ? item.title_en : item.title;
        const excerpt = (isEn && item.subtitle_en) ? item.subtitle_en : item.subtitle;
        const readTime = isEn ? (item.readTime || '').replace('phút đọc', 'min read') : item.readTime;
        return `
        <article class="category-stream-row" onclick="openArticleModal('${item.id}')">
          <div class="category-stream-thumb-wrap">
            <img src="${item.image}" alt="${title}" class="category-stream-thumb" loading="lazy" onerror="handleImageError(this)">
          </div>
          <div class="category-stream-body">
            <span style="font-size:0.725rem; font-weight:800; color:var(--color-brand-accent); letter-spacing:0.06em; text-transform:uppercase; margin-bottom:0.3rem; display:block;">${item.categoryName}</span>
            <h3 class="category-stream-title">${title}</h3>
            <p class="category-stream-excerpt">${excerpt}</p>
            <div class="category-stream-footer">
              <span><i class="far fa-user"></i> ${item.author.split('•')[0].trim()}</span>
              <span><i class="far fa-clock"></i> ${readTime}</span>
              <span><i class="far fa-heart"></i> ${item.likes}</span>
            </div>
          </div>
        </article>
      `;
      }).join('');
    }
  } else if (legacyContainer) {
    legacyContainer.innerHTML = filtered.map(item => {
      const title = (isEn && item.title_en) ? item.title_en : item.title;
      const excerpt = (isEn && item.subtitle_en) ? item.subtitle_en : item.subtitle;
      const readTime = isEn ? (item.readTime || '').replace('phút đọc', 'min read') : item.readTime;
      return `
      <article class="fashion-article-card" onclick="openArticleModal('${item.id}')">
        <div class="fashion-card-media">
          <img src="${item.image}" alt="${title}" class="fashion-card-img" loading="lazy" onerror="handleImageError(this)">
          <span class="fashion-card-category-tag">${item.categoryName}</span>
        </div>
        <div class="fashion-card-body">
          <h3 class="fashion-card-title">${title}</h3>
          <p class="fashion-card-excerpt">${excerpt}</p>
          <div class="fashion-card-footer">
            <span class="fashion-card-byline"><i class="far fa-user"></i> ${item.author.split('•')[0].trim()}</span>
            <div class="fashion-card-stats">
              <span><i class="far fa-clock"></i> ${readTime}</span>
              <span><i class="far fa-heart"></i> ${item.likes}</span>
            </div>
          </div>
        </div>
      </article>
    `;
    }).join('');
  }

  // Populate sidebar top read #1 to #5
  if (topReadContainer) {
    const topArticles = [...ARTICLES_DATA]
      .sort((a, b) => (b.likes || 0) - (a.likes || 0))
      .slice(0, 5);

    topReadContainer.innerHTML = topArticles.map((art, idx) => {
      const artTitle = (isEn && art.title_en) ? art.title_en : art.title;
      const readLabel = isEn ? 'reads' : 'lượt đọc';
      return `
      <div class="top-read-item" onclick="openArticleModal('${art.id}')">
        <span class="top-read-num">${idx + 1}</span>
        <div>
          <span style="font-size:0.6875rem; font-weight:800; color:var(--color-brand-accent); text-transform:uppercase; display:block; margin-bottom:0.15rem;">${art.categoryName}</span>
          <h4 class="top-read-headline">${artTitle}</h4>
          <span style="font-size:0.75rem; color:var(--color-text-muted); font-weight:600;"><i class="far fa-eye"></i> ${art.views || '12.4K'} ${readLabel}</span>
        </div>
      </div>
    `;
    }).join('');
  }
}"""

norm_text = text.replace('\r\n', '\n')
norm_apply_old = apply_old.replace('\r\n', '\n')
norm_apply_new = apply_new.replace('\r\n', '\n')
norm_render_cat_old = render_cat_old.replace('\r\n', '\n')
norm_render_cat_new = render_cat_new.replace('\r\n', '\n')

if norm_apply_old in norm_text:
    norm_text = norm_text.replace(norm_apply_old, norm_apply_new)
    print("SUCCESS: applyLanguage updated!")
else:
    print("FAIL: apply_old not found")

if norm_render_cat_old in norm_text:
    norm_text = norm_text.replace(norm_render_cat_old, norm_render_cat_new)
    print("SUCCESS: renderCategoryPageArticles updated!")
else:
    print("FAIL: render_cat_old not found")

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(norm_text)
print("js/app.js updated successfully!")
