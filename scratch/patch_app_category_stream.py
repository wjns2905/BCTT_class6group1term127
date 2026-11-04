with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

target = """function renderCategoryPageArticles() {
  const container = document.getElementById('categoryArticlesGrid');
  if (!container) return;

  const currentCategory = document.body.dataset.category || '';
  if (!currentCategory) return;

  const filtered = ARTICLES_DATA.filter(a => a.category.toLowerCase() === currentCategory.toLowerCase());

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 4rem 1rem; color: var(--color-text-muted);">
        <i class="fas fa-feather" style="font-size: 2.5rem; color: var(--color-brand-accent); margin-bottom: 1rem;"></i>
        <h3 style="font-family: var(--font-editorial); font-size: 1.5rem; color: var(--color-text-headline);">Chưa có bài viết trong chuyên mục này</h3>
        <p style="font-size: 0.9rem; margin-top: 0.5rem;">Các bài viết mới sẽ sớm được cập nhật.</p>
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map(item => `
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
}"""

replacement = """function renderCategoryPageArticles() {
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

norm_js = js.replace("\r\n", "\n")
norm_target = target.replace("\r\n", "\n")
norm_rep = replacement.replace("\r\n", "\n")

if norm_target in norm_js:
    norm_js = norm_js.replace(norm_target, norm_rep, 1)
    with open("js/app.js", "w", encoding="utf-8") as f:
        f.write(norm_js)
    print("js/app.js updated successfully with asymmetric category stream & top-read sidebar!")
else:
    print("Could not match renderCategoryPageArticles in js/app.js")
