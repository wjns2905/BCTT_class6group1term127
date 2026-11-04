with open("js/app.js", "r", encoding="utf-8") as f:
    code = f.read()

target1 = """function initApp() {
  updateLiveDate();
  setupEventListeners();
  renderVideoHub();
  renderFashionJournal('all');
  renderAboutUsSection();"""

replacement1 = """function initApp() {
  updateLiveDate();
  setupEventListeners();
  renderVideoHub();
  renderFashionJournal('all');
  renderCategoryPageArticles();
  renderAboutUsSection();"""

target2 = """  container.innerHTML = filtered.map(item => `
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

replacement2 = """  container.innerHTML = filtered.map(item => `
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

/* ===================================================================
   STANDALONE CATEGORY PAGE ARTICLES (Multi-page Architecture)
   =================================================================== */
function renderCategoryPageArticles() {
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

# Normalize newlines for replacement
norm_code = code.replace("\r\n", "\n")
norm_target1 = target1.replace("\r\n", "\n")
norm_replacement1 = replacement1.replace("\r\n", "\n")
norm_target2 = target2.replace("\r\n", "\n")
norm_replacement2 = replacement2.replace("\r\n", "\n")

if norm_target1 in norm_code and norm_target2 in norm_code:
    norm_code = norm_code.replace(norm_target1, norm_replacement1, 1)
    norm_code = norm_code.replace(norm_target2, norm_replacement2, 1)
    with open("js/app.js", "w", encoding="utf-8") as f:
        f.write(norm_code)
    print("js/app.js updated successfully with renderCategoryPageArticles!")
else:
    print("Could not match target blocks in js/app.js")
