import sys

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

# Replace openArticleModal
old_modal_start = """window.openArticleModal = function(articleId) {
  const article = ARTICLES_DATA.find(a => a.id === articleId);
  if (!article) return;

  const modal = document.getElementById('articleReaderModal');
  const body = document.getElementById('articleModalBody');
  if (!modal || !body) return;

  const savedComments = JSON.parse(localStorage.getItem(`comments_${article.id}`) || '[]');
  const isLiked = localStorage.getItem(`liked_${article.id}`) === 'true';

  let bodyHtml = '';
  if (typeof article.content === 'string') {
    bodyHtml = article.content;
  } else if (Array.isArray(article.content)) {
    bodyHtml = article.content.map(p => {
      if (p.startsWith('### ')) {
        return `<h3>${p.replace('### ', '')}</h3>`;
      }
      return `<p>${p}</p>`;
    }).join('');
  }"""

new_modal_start = """window.openArticleModal = function(articleId) {
  const article = ARTICLES_DATA.find(a => a.id === articleId);
  if (!article) return;

  const modal = document.getElementById('articleReaderModal');
  const body = document.getElementById('articleModalBody');
  if (!modal || !body) return;

  modal.dataset.articleId = articleId;
  const isEn = (currentLanguage === 'en');
  const title = (isEn && article.title_en) ? article.title_en : article.title;
  const subtitle = (isEn && article.subtitle_en) ? article.subtitle_en : article.subtitle;
  const savedComments = JSON.parse(localStorage.getItem(`comments_${article.id}`) || '[]');
  const isLiked = localStorage.getItem(`liked_${article.id}`) === 'true';

  let content = article.content;
  if (isEn && article.content_en) {
    content = article.content_en;
  }

  let bodyHtml = '';
  if (typeof content === 'string') {
    bodyHtml = content;
  } else if (Array.isArray(content)) {
    bodyHtml = content.map(p => {
      if (p.startsWith('### ')) {
        return `<h3>${p.replace('### ', '')}</h3>`;
      }
      return `<p>${p}</p>`;
    }).join('');
  }"""

# Replace modal inner content
old_modal_inner = """      <div class="article-breadcrumb">
        <a href="javascript:void(0)" onclick="closeArticleModal()">Home</a>
        <span>/</span>
        <a href="javascript:void(0)" onclick="filterByCategory('${article.category}')">${article.categoryName}</a>
        <span>/</span>
        <span>Chi tiết bài viết</span>
      </div>

      <h1 class="article-headline" style="font-family:var(--font-editorial); font-size:2.2rem; line-height:1.25; margin-bottom:0.75rem;">${article.title}</h1>
      <p class="article-sapo" style="font-family:var(--font-serif); font-size:1.22rem; line-height:1.65; color:var(--color-text-body); font-weight:600; margin-bottom:1.5rem;">${article.subtitle}</p>

      <div class="article-author-strip">
        <div class="article-author-info">
          <div class="author-avatar-small">${article.author.charAt(0)}</div>
          <div>
            <div class="author-name-text" style="font-weight:700;">${article.author}</div>
            <div class="article-date-text" style="font-size:0.8125rem; color:var(--color-text-muted); font-weight:600;">${article.date}</div>
          </div>
        </div>

        <div class="article-reading-tools">
          <button class="tool-btn" onclick="adjustFontSize(-0.1)" title="Giảm cỡ chữ"><i class="fas fa-font"></i> A-</button>
          <button class="tool-btn" onclick="adjustFontSize(0.1)" title="Tăng cỡ chữ"><i class="fas fa-font"></i> A+</button>
          <button class="tool-btn ${isSpeaking ? 'active' : ''}" id="btnTTS" onclick="toggleTextToSpeech('${article.id}')" title="Nghe đọc bài báo">
            <i class="fas ${isSpeaking ? 'fa-pause' : 'fa-volume-up'}"></i> ${isSpeaking ? 'Tạm dừng' : 'Đọc bài báo'}
          </button>
          <button class="btn-article-like ${isLiked ? 'liked' : ''}" id="likeBtn_${article.id}" onclick="toggleLikeArticle('${article.id}')" title="Thả tim bài viết">
            <i class="fas fa-heart"></i> <span id="likeCount_${article.id}">${article.likes + (isLiked ? 1 : 0)}</span>
          </button>
          <button class="tool-btn" onclick="shareArticle('${article.title}')" title="Chia sẻ"><i class="fas fa-share-alt"></i> Chia sẻ</button>
        </div>
      </div>

      <div class="article-hero-media" style="border-radius:var(--radius-lg); overflow:hidden; margin:1.5rem 0;">
        <img src="${article.image}" alt="${article.title}" style="width:100%; display:block;" onerror="handleImageError(this)">
        <div class="article-media-caption" style="font-size:0.875rem; color:var(--color-text-muted); font-weight:500; font-style:italic; padding:0.6rem 0.25rem;">${article.imageCaption || article.title}</div>
      </div>

      ${article.video ? `
        <div class="video-responsive-embed" style="margin-bottom: 2rem; border-radius: 12px; overflow:hidden;">
          <iframe src="${article.video}" title="Video phóng sự kèm bài viết" allowfullscreen></iframe>
        </div>
      ` : ''}

      <div class="article-body-text" id="articleBodyContent" style="font-family:var(--font-body); font-size:1.18rem; line-height:1.85; color:var(--color-text-body);">
        ${bodyHtml}
      </div>

      <div class="article-source-box" style="background:var(--color-surface-blush); border:1px solid #EEDBD6; border-radius:var(--radius-md); padding:1rem 1.25rem; margin-top:2.5rem; display:flex; justify-content:space-between; align-items:center;">
        <div class="source-credit-text">
          <strong>Nguồn trích dẫn:</strong> ${article.sourceName}
        </div>
        <a href="${article.sourceUrl}" target="_blank" rel="noopener noreferrer" class="source-link-btn" style="color:var(--color-brand-primary); font-weight:600; font-size:0.875rem;">
          Xem nguồn gốc <i class="fas fa-external-link-alt"></i>
        </a>
      </div>

      <!-- Comments Block -->
      <div class="article-comments-block" style="margin-top:3rem;">
        <h3 style="font-family:var(--font-editorial); font-size:1.4rem; color:var(--color-text-headline); margin-bottom:1.25rem;">
          <i class="far fa-comments" style="color:var(--color-brand-primary);"></i> Bình luận &amp; Thảo luận (<span id="commentCount">${savedComments.length}</span>)
        </h3>
        
        <div class="comment-form-wrap" style="display:flex; gap:0.75rem; margin-bottom:1.5rem;">
          <input type="text" class="comment-input-field" id="newCommentInput" placeholder="Chia sẻ góc nhìn nhân văn của bạn về bài viết này..." onkeypress="if(event.key === 'Enter') submitComment('${article.id}')" style="flex-grow:1; padding:0.75rem 1rem; border:1px solid var(--color-border-hairline); border-radius:var(--radius-full); font-size:0.9rem;">
          <button class="comment-submit-btn" onclick="submitComment('${article.id}')" style="background:var(--color-brand-primary); color:white; border:none; border-radius:var(--radius-full); padding:0.75rem 1.5rem; font-weight:600; cursor:pointer;">Gửi</button>
        </div>"""

new_modal_inner = """      <div class="article-breadcrumb">
        <a href="javascript:void(0)" onclick="closeArticleModal()">Home</a>
        <span>/</span>
        <a href="javascript:void(0)" onclick="filterByCategory('${article.category}')">${article.categoryName}</a>
        <span>/</span>
        <span>${isEn ? 'Article Details' : 'Chi tiết bài viết'}</span>
      </div>

      <h1 class="article-headline" style="font-family:var(--font-editorial); font-size:2.2rem; line-height:1.25; margin-bottom:0.75rem;">${title}</h1>
      <p class="article-sapo" style="font-family:var(--font-sans); font-size:1.22rem; line-height:1.65; color:var(--color-text-body); font-weight:600; margin-bottom:1.5rem;">${subtitle}</p>

      <div class="article-author-strip">
        <div class="article-author-info">
          <div class="author-avatar-small">${article.author.charAt(0)}</div>
          <div>
            <div class="author-name-text" style="font-weight:700;">${article.author}</div>
            <div class="article-date-text" style="font-size:0.8125rem; color:var(--color-text-muted); font-weight:600;">${article.date}</div>
          </div>
        </div>

        <div class="article-reading-tools">
          <button class="tool-btn" onclick="adjustFontSize(-0.1)" title="${isEn ? 'Decrease text size' : 'Giảm cỡ chữ'}"><i class="fas fa-font"></i> A-</button>
          <button class="tool-btn" onclick="adjustFontSize(0.1)" title="${isEn ? 'Increase text size' : 'Tăng cỡ chữ'}"><i class="fas fa-font"></i> A+</button>
          <button class="tool-btn ${isSpeaking ? 'active' : ''}" id="btnTTS" onclick="toggleTextToSpeech('${article.id}')" title="${isEn ? 'Listen to Article' : 'Nghe đọc bài báo'}">
            <i class="fas ${isSpeaking ? 'fa-pause' : 'fa-volume-up'}"></i> ${isSpeaking ? (isEn ? 'Pause' : 'Tạm dừng') : (isEn ? 'Listen to Article' : 'Đọc bài báo')}
          </button>
          <button class="btn-article-like ${isLiked ? 'liked' : ''}" id="likeBtn_${article.id}" onclick="toggleLikeArticle('${article.id}')" title="${isEn ? 'Like this article' : 'Thả tim bài viết'}">
            <i class="fas fa-heart"></i> <span id="likeCount_${article.id}">${article.likes + (isLiked ? 1 : 0)}</span>
          </button>
          <button class="tool-btn" onclick="shareArticle('${title}')" title="${isEn ? 'Share' : 'Chia sẻ'}"><i class="fas fa-share-alt"></i> ${isEn ? 'Share' : 'Chia sẻ'}</button>
        </div>
      </div>

      <div class="article-hero-media" style="border-radius:var(--radius-lg); overflow:hidden; margin:1.5rem 0;">
        <img src="${article.image}" alt="${title}" style="width:100%; display:block;" onerror="handleImageError(this)">
        <div class="article-media-caption" style="font-size:0.875rem; color:var(--color-text-muted); font-weight:500; font-style:italic; padding:0.6rem 0.25rem;">${article.imageCaption || title}</div>
      </div>

      ${article.video ? `
        <div class="video-responsive-embed" style="margin-bottom: 2rem; border-radius: 12px; overflow:hidden;">
          <iframe src="${article.video}" title="${title}" allowfullscreen></iframe>
        </div>
      ` : ''}

      <div class="article-body-text" id="articleBodyContent" style="font-family:var(--font-body); font-size:1.15rem; line-height:1.8; color:var(--color-text-body);">
        ${bodyHtml}
      </div>

      <div class="article-source-box" style="background:var(--color-surface-blush); border:1px solid #EEDBD6; border-radius:var(--radius-md); padding:1rem 1.25rem; margin-top:2.5rem; display:flex; justify-content:space-between; align-items:center;">
        <div class="source-credit-text">
          <strong>${isEn ? 'Source citation:' : 'Nguồn trích dẫn:'}</strong> ${article.sourceName}
        </div>
        <a href="${article.sourceUrl}" target="_blank" rel="noopener noreferrer" class="source-link-btn" style="color:var(--color-brand-primary); font-weight:600; font-size:0.875rem;">
          ${isEn ? 'View Original Source' : 'Xem nguồn gốc'} <i class="fas fa-external-link-alt"></i>
        </a>
      </div>

      <!-- Comments Block -->
      <div class="article-comments-block" style="margin-top:3rem;">
        <h3 style="font-family:var(--font-editorial); font-size:1.4rem; color:var(--color-text-headline); margin-bottom:1.25rem;">
          <i class="far fa-comments" style="color:var(--color-brand-primary);"></i> ${isEn ? 'Comments & Discussion' : 'Bình luận & Thảo luận'} (<span id="commentCount">${savedComments.length}</span>)
        </h3>
        
        <div class="comment-form-wrap" style="display:flex; gap:0.75rem; margin-bottom:1.5rem;">
          <input type="text" class="comment-input-field" id="newCommentInput" placeholder="${isEn ? 'Share your constructive reflection on this story...' : 'Chia sẻ góc nhìn nhân văn của bạn về bài viết này...'}" onkeypress="if(event.key === 'Enter') submitComment('${article.id}')" style="flex-grow:1; padding:0.75rem 1rem; border:1px solid var(--color-border-hairline); border-radius:var(--radius-full); font-size:0.9rem;">
          <button class="comment-submit-btn" onclick="submitComment('${article.id}')" style="background:var(--color-brand-primary); color:white; border:none; border-radius:var(--radius-full); padding:0.75rem 1.5rem; font-weight:600; cursor:pointer;">${isEn ? 'Post' : 'Gửi'}</button>
        </div>"""

# Replace TTS
old_tts = """window.toggleTextToSpeech = function(articleId) {
  if (isSpeaking) {
    window.speechSynthesis.cancel();
    isSpeaking = false;
    updateTTSButton(false);
    return;
  }

  const article = ARTICLES_DATA.find(a => a.id === articleId);
  if (!article) return;

  const fullText = `${article.title}. ${article.subtitle}. ${Array.isArray(article.content) ? article.content.join('. ') : article.content}`.replace(/### /g, '');

  speechUtterance = new SpeechSynthesisUtterance(fullText);
  speechUtterance.lang = 'vi-VN';
  speechUtterance.rate = 1.0;

  speechUtterance.onend = () => {
    isSpeaking = false;
    updateTTSButton(false);
  };
  speechUtterance.onerror = () => {
    isSpeaking = false;
    updateTTSButton(false);
  };

  window.speechSynthesis.speak(speechUtterance);
  isSpeaking = true;
  updateTTSButton(true);
};"""

new_tts = """window.toggleTextToSpeech = function(articleId) {
  if (isSpeaking) {
    window.speechSynthesis.cancel();
    isSpeaking = false;
    updateTTSButton(false);
    return;
  }

  const article = ARTICLES_DATA.find(a => a.id === articleId);
  if (!article) return;

  const isEn = (currentLanguage === 'en');
  const title = (isEn && article.title_en) ? article.title_en : article.title;
  const subtitle = (isEn && article.subtitle_en) ? article.subtitle_en : article.subtitle;
  let content = article.content;
  if (isEn && article.content_en) {
    content = article.content_en;
  }

  const fullText = `${title}. ${subtitle}. ${Array.isArray(content) ? content.join('. ') : content}`.replace(/### /g, '');

  speechUtterance = new SpeechSynthesisUtterance(fullText);
  speechUtterance.lang = isEn ? 'en-US' : 'vi-VN';
  speechUtterance.rate = 1.0;

  speechUtterance.onend = () => {
    isSpeaking = false;
    updateTTSButton(false);
  };
  speechUtterance.onerror = () => {
    isSpeaking = false;
    updateTTSButton(false);
  };

  window.speechSynthesis.speak(speechUtterance);
  isSpeaking = true;
  updateTTSButton(true);
};

function updateTTSButton(speaking) {
  const btn = document.getElementById('btnTTS');
  if (!btn) return;
  const isEn = (currentLanguage === 'en');
  if (speaking) {
    btn.classList.add('active');
    btn.innerHTML = `<i class="fas fa-pause"></i> ${isEn ? 'Pause' : 'Tạm dừng'}`;
  } else {
    btn.classList.remove('active');
    btn.innerHTML = `<i class="fas fa-volume-up"></i> ${isEn ? 'Listen to Article' : 'Đọc bài báo'}`;
  }
}"""

# Update search results for bilingual
old_search = """  if (results.length === 0) {
    container.innerHTML = `<p style="color:var(--color-text-muted); font-size:0.9rem; padding:1rem 0;">Không tìm thấy bài viết nào phù hợp với từ khóa "${query}".</p>`;
    return;
  }"""

new_search = """  const isEn = (currentLanguage === 'en');
  if (results.length === 0) {
    container.innerHTML = `<p style="color:var(--color-text-muted); font-size:0.9rem; padding:1rem 0;">${isEn ? `No stories found matching "${query}".` : `Không tìm thấy bài viết nào phù hợp với từ khóa "${query}".`}</p>`;
    return;
  }"""

norm_js = js.replace("\r\n", "\n")
subs = [
    (old_modal_start, new_modal_start),
    (old_modal_inner, new_modal_inner),
    (old_tts, new_tts),
    (old_search, new_search)
]

applied = 0
for t, r in subs:
    nt = t.replace("\r\n", "\n")
    nr = r.replace("\r\n", "\n")
    if nt in norm_js:
        norm_js = norm_js.replace(nt, nr, 1)
        applied += 1
    else:
        print(f"FAILED on block: {t[:40]}...")

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(norm_js)

print(f"Applied {applied}/{len(subs)} modal/TTS bilingual updates to js/app.js!")
