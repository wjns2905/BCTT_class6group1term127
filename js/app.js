/**
 * HEARTICLES. - High-Fashion Magazine Editorial Application Core
 * Class 6 - Group 1 - Term 127
 * Trường Đại học Ngoại ngữ - Đại học Quốc gia Hà Nội (ULIS - VNU)
 * Fashion Editorial Suite (Vogue, Harper's Bazaar, Kinfolk Aesthetic)
 * 100% Authentic Articles & Images from Original Course Resources
 */

document.addEventListener('DOMContentLoaded', () => {
  initApp();
});

let currentFontSize = 1.15; // rem
let isSpeaking = false;
let speechUtterance = null;
let currentOnboardStep = 1;
let currentCategoryFilter = 'all';
let currentLanguage = localStorage.getItem('hearticles_lang') || 'en';

function initApp() {
  initLanguage();
  updateLiveDate();
  setupEventListeners();
  renderVideoHub();
  renderFashionJournal('all');
  renderCategoryPageArticles();
  renderAboutUsSection();
  setupPoll();
  initOnboarding();
  setupReadingProgressBar();
  setupNetworkStatus();
}

/* ===================================================================
   INTERNATIONALIZATION (i18n) ENGINE - VIETNAMESE & ENGLISH
   =================================================================== */
function initLanguage() {
  currentLanguage = localStorage.getItem('hearticles_lang') || 'en';
  applyLanguage(currentLanguage);
}

window.setLanguage = function(lang) {
  if (lang !== 'vi' && lang !== 'en') return;
  currentLanguage = lang;
  localStorage.setItem('hearticles_lang', lang);
  applyLanguage(lang);
};

window.toggleLanguage = function() {
  const nextLang = currentLanguage === 'vi' ? 'en' : 'vi';
  setLanguage(nextLang);
};

function applyLanguage(lang) {
  document.documentElement.lang = lang;

  // Update button active state across all header, topbar, and drawer buttons
  document.querySelectorAll('.lang-pill-btn, #btnLangVI, #btnLangEN, #drawerLangVI, #drawerLangEN').forEach(btn => {
    const targetLang = btn.getAttribute('data-lang') || (btn.id && btn.id.includes('EN') ? 'en' : 'vi');
    btn.classList.toggle('active', targetLang === lang);
  });

  // Apply translations to all data-i18n elements
  if (typeof I18N_TRANSLATIONS !== 'undefined') {
    const dict = I18N_TRANSLATIONS[lang] || I18N_TRANSLATIONS.vi;
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (dict[key]) {
        el.innerHTML = dict[key];
      }
    });

    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
      const key = el.getAttribute('data-i18n-placeholder');
      if (dict[key]) {
        el.placeholder = dict[key];
      }
    });

    document.querySelectorAll('[data-i18n-title]').forEach(el => {
      const key = el.getAttribute('data-i18n-title');
      if (dict[key]) {
        el.title = dict[key];
      }
    });
  }

  updateLiveDate();
  renderVideoHub();
  renderCategoryPageArticles();
  renderAboutUsSection();

  // Re-render open article modal if active
  const modal = document.getElementById('articleReaderModal');
  if (modal && modal.classList.contains('active')) {
    const activeArtId = modal.dataset.articleId;
    if (activeArtId) {
      openArticleModal(activeArtId);
    }
  }
}

/* ===================================================================
   DATE & TIME DISPLAY (Tabular Figures & Vietnamese Time)
   =================================================================== */
function updateLiveDate() {
  const dateEl = document.getElementById('liveDateWidget');
  if (!dateEl) return;
  const now = new Date();
  if (currentLanguage === 'en') {
    const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    const dayName = days[now.getDay()];
    const monthName = months[now.getMonth()];
    const dateStr = `${dayName}, ${monthName} ${now.getDate()}, ${now.getFullYear()} | Hanoi 26°C`;
    dateEl.innerHTML = `<i class="far fa-calendar-alt"></i> <span style="font-variant-numeric: tabular-nums;">${dateStr}</span>`;
  } else {
    const days = ['Chủ Nhật', 'Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy'];
    const dayName = days[now.getDay()];
    const dateStr = `${dayName}, ${now.getDate()} Tháng ${now.getMonth() + 1}, ${now.getFullYear()} | Hà Nội 26°C`;
    dateEl.innerHTML = `<i class="far fa-calendar-alt"></i> <span style="font-variant-numeric: tabular-nums;">${dateStr}</span>`;
  }
}

/* ===================================================================
   MULTIMEDIA & VIDEO PHÓNG SỰ HUB (5 Video Clips Requirement)
   Using Authentic Original Images as Video Thumbnails
   =================================================================== */
const VIDEO_CLIPS = [
  {
    id: "clip-1",
    category: "Trending",
    category_en: "Trending",
    title: "Phóng sự: Gánh mưu sinh và nét đẹp lao động bình dị phố cổ Hội An",
    title_en: "Documentary: Street Vendors with Shoulder Pole in Ancient Town of Hoi An",
    desc: "Hình ảnh đôi quang gánh trĩu nặng nhịp sống mưu sinh, vẻ đẹp cần lao mộc mạc và ký ức rêu phong trên từng ngõ nhỏ di sản.",
    desc_en: "The rustic beauty of vendors carrying woven baskets on shoulder poles has long been an indispensable, soulful hallmark of Hoi An.",
    url: "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    thumb: "assets/images/trending/image8.jpg",
    articleId: "trending-4"
  },
  {
    id: "clip-2",
    category: "Mind & Soul",
    category_en: "Mind & Soul",
    title: "Taeyang (BigBang) và đêm nhạc bùng nổ tại SVĐ Quốc gia Mỹ Đình",
    title_en: "BigBang's Taeyang and the Historic Concert Nights at My Dinh Stadium",
    desc: "Khoảnh khắc nam nghệ sĩ xúc động trước tình cảm nồng nhiệt của hàng vạn khán giả Thủ đô và tình yêu với ẩm thực phở Hà Nội.",
    desc_en: "The acclaimed Korean icon expressed profound gratitude to Vietnamese fans following two unforgettable anniversary nights in Hanoi.",
    url: "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    thumb: "assets/images/mind_&_soul/image2.jpg",
    articleId: "mind-1"
  },
  {
    id: "clip-3",
    category: "Human Stories",
    category_en: "Human Stories",
    title: "Những người nông dân gieo hạt mầm tri thức tại Gruver, Texas",
    title_en: "Volunteer Texas Farmers Sowing Seeds of Knowledge in Gruver, Texas",
    desc: "Câu chuyện cảm động về cộng đồng nông dân tình nguyện canh tác gây quỹ 400.000 USD học bổng mỗi năm cho học sinh nghèo vào đại học.",
    desc_en: "A tight-knit farming community volunteers land and labor, pooling harvest proceeds to fund college scholarships for local graduates.",
    url: "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    thumb: "assets/images/human_stories/image5.png",
    articleId: "human-4"
  },
  {
    id: "clip-4",
    category: "Society",
    category_en: "Society",
    title: "Chiến dịch 500 ngày đêm ADN: Trả lại danh tính cho gần 800 hài cốt liệt sĩ",
    title_en: "500-Day-and-Night Campaign: Returning Identities to Nearly 800 Fallen Soldiers",
    desc: "Hành trình thầm lặng nhưng đầy tự hào của các nhà khoa học và cơ quan chức năng vì đạo lý 'Uống nước nhớ nguồn'.",
    desc_en: "A quiet, noble journey by forensic scientists and authorities to identify fallen heroes, honoring Vietnam's ancestral gratitude.",
    url: "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    thumb: "assets/images/human_stories/image17.jpg",
    articleId: "trending-5"
  },
  {
    id: "clip-5",
    category: "About Us",
    category_en: "About Us",
    title: "HEARTICLES Manifesto: 'Stories that speak to the heart' • ULIS - VNU",
    title_en: "HEARTICLES Manifesto: 'Stories that speak to the heart' • ULIS - VNU",
    desc: "Thông điệp tôn chỉ báo chí nhân văn và hậu trường thực hiện tạp chí số từ nhóm sinh viên Lớp 6 - Nhóm 1 - Khóa 127, ULIS - VNU.",
    desc_en: "Humanistic journalism manifesto and editorial behind-the-scenes by Class 6 - Group 1 - Intake 127, ULIS - VNU.",
    url: "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    thumb: "assets/images/trending/image10.jpg",
    articleId: "about"
  }
];

function renderVideoHub() {
  const container = document.getElementById('videoHubContent');
  if (!container) return;

  const isEn = (currentLanguage === 'en');
  const mainClip = VIDEO_CLIPS[0];
  const mainTitle = (isEn && mainClip.title_en) ? mainClip.title_en : mainClip.title;
  const mainDesc = (isEn && mainClip.desc_en) ? mainClip.desc_en : mainClip.desc;
  const mainCat = (isEn && mainClip.category_en) ? mainClip.category_en : mainClip.category;

  container.innerHTML = `
    <div class="video-grid-layout">
      <div class="main-video-player-box">
        <div class="video-responsive-embed">
          <iframe id="activeVideoFrame" src="${mainClip.url}" title="${mainTitle}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
        <div class="main-video-details">
          <span class="category-tag" id="activeVideoCategory" style="color:var(--color-brand-primary); font-weight:800;">${mainCat}</span>
          <h2 class="main-video-title" id="activeVideoTitle" style="font-family:var(--font-editorial); font-size:1.5rem; margin-top:0.4rem;">${mainTitle}</h2>
          <p class="main-video-desc" id="activeVideoDesc" style="color:var(--color-text-body); font-size:0.95rem; line-height:1.6; font-weight:500;">${mainDesc}</p>
        </div>
      </div>

      <div class="video-playlist">
        ${VIDEO_CLIPS.map((clip, idx) => {
          const title = (isEn && clip.title_en) ? clip.title_en : clip.title;
          const cat = (isEn && clip.category_en) ? clip.category_en : clip.category;
          return `
            <div class="playlist-card ${idx === 0 ? 'active' : ''}" onclick="switchVideo('${clip.id}')">
              <div class="playlist-thumb-wrap">
                <img src="${clip.thumb}" alt="${title}" loading="lazy" onerror="handleImageError(this)">
                <div class="playlist-play-icon"><i class="fas fa-play"></i></div>
              </div>
              <div class="playlist-info">
                <span class="playlist-cat">${cat}</span>
                <h4 class="playlist-title">${title}</h4>
              </div>
            </div>
          `;
        }).join('')}
      </div>
    </div>
  `;
}

window.switchVideo = function(clipId) {
  const clip = VIDEO_CLIPS.find(c => c.id === clipId);
  if (!clip) return;
  const frame = document.getElementById('activeVideoFrame');
  const cat = document.getElementById('activeVideoCategory');
  const title = document.getElementById('activeVideoTitle');
  const desc = document.getElementById('activeVideoDesc');
  const isEn = (currentLanguage === 'en');

  if (frame) frame.src = clip.url;
  if (cat) cat.textContent = (isEn && clip.category_en) ? clip.category_en : clip.category;
  if (title) title.textContent = (isEn && clip.title_en) ? clip.title_en : clip.title;
  if (desc) desc.textContent = (isEn && clip.desc_en) ? clip.desc_en : clip.desc;

  document.querySelectorAll('.playlist-card').forEach(card => card.classList.remove('active'));
  event.currentTarget.classList.add('active');
};

/* ===================================================================
   THE JOURNAL (Full Curated Articles Magazine Grid)
   =================================================================== */
function renderFashionJournal(categoryKey) {
  const container = document.getElementById('fashionArticlesGrid');
  if (!container) return;

  currentCategoryFilter = categoryKey;

  let filtered = ARTICLES_DATA;
  if (categoryKey && categoryKey !== 'all') {
    filtered = ARTICLES_DATA.filter(a => a.category.toLowerCase() === categoryKey.toLowerCase());
  }

  // Update pills active state
  document.querySelectorAll('.fashion-filter-pill').forEach(pill => {
    pill.classList.remove('active');
    if (pill.getAttribute('onclick')?.includes(`'${categoryKey}'`)) {
      pill.classList.add('active');
    }
  });

  // Update navbar active state
  document.querySelectorAll('.fashion-nav .nav-item').forEach(item => {
    item.classList.remove('active');
    if (item.dataset.category === categoryKey) {
      item.classList.add('active');
    }
  });

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 4rem 1rem; color: var(--color-text-muted);">
        <i class="fas fa-feather" style="font-size: 2.5rem; color: var(--color-brand-accent); margin-bottom: 1rem;"></i>
        <h3 style="font-family: var(--font-editorial); font-size: 1.5rem; color: var(--color-text-headline);">Chưa có bài viết trong chuyên mục này</h3>
        <p style="font-size: 0.9rem; margin-top: 0.5rem;">Mời bạn chọn chuyên mục khác hoặc quay lại xem tất cả bài viết.</p>
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
}

/* ===================================================================
   STANDALONE CATEGORY PAGE ARTICLES (Multi-page Architecture)
   =================================================================== */
function renderCategoryPageArticles() {
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
}

/* ===================================================================
   NAVIGATION & CATEGORY FILTERING
   =================================================================== */
window.filterByCategory = function(categoryKey) {
  closeDrawer();
  closeArticleModal();

  if (categoryKey === 'about') {
    const aboutEl = document.getElementById('about-us');
    if (aboutEl) {
      aboutEl.scrollIntoView({ behavior: 'smooth' });
    }
    return;
  }

  renderFashionJournal(categoryKey);

  if (categoryKey !== 'all') {
    const journalEl = document.getElementById('journalSection');
    if (journalEl) {
      journalEl.scrollIntoView({ behavior: 'smooth' });
    }
  } else {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
};

/* ===================================================================
   ABOUT US SECTION (ULIS - VNU Editorial Manifesto)
   =================================================================== */
function renderAboutUsSection() {
  const container = document.getElementById('aboutUsSection');
  if (!container) return;

  const isEn = (currentLanguage === 'en');

  const manifestoTag = isEn ? '<i class="fas fa-heart"></i> EDITORIAL MANIFESTO' : '<i class="fas fa-heart"></i> TÔN CHỈ HOẠT ĐỘNG';
  const manifestoTitle = isEn ? 'HEARTICLES. E-Magazine' : 'Tạp chí Báo điện tử HEARTICLES.';
  const manifestoSubtitle = isEn ? '"Stories that speak to the heart — Where news begins with a heartbeat"' : '"Stories that speak to the heart — Nơi tin tức khởi nguồn từ nhịp đập trái tim"';

  const p1 = isEn ? `
    <strong>HEARTICLES.</strong> was founded and published by the student editorial team of <strong>Class 6 - Group 1 - Term 127</strong> at <strong>University of Languages and International Studies - Vietnam National University, Hanoi (ULIS - VNU)</strong> within the Journalism & Communication course (BCTT), aspiring to establish a multimedia news publication with haute-couture aesthetics, international standards, and boundless compassion.
  ` : `
    <strong>HEARTICLES.</strong> được sáng lập và vận hành bởi nhóm sinh viên <strong>Lớp 6 - Nhóm 1 - Khóa 127</strong> thuộc <strong>Trường Đại học Ngoại ngữ - Đại học Quốc gia Hà Nội (ULIS - VNU)</strong> trong khuôn khổ học phần Báo chí &amp; Truyền thông (BCTT), với khát vọng kiến tạo một ấn phẩm báo chí đa phương tiện mang phong cách thời trang, chuẩn mực quốc tế và tràn đầy lòng trắc ẩn.
  `;

  const p2 = isEn ? `
    Inspired by the visual design vocabulary of iconic publications like Vogue, Harper's Bazaar, and Kinfolk, as well as the editorial model of Báo Nhân Dân online, we believe authentic beauty in journalism lies not in sensationalism or clickbait, but in humanistic depth, the elegance of typography, and gentle stories that touch readers' hearts.
  ` : `
    Lấy cảm hứng từ ngôn ngữ thẩm mỹ của các tạp chí danh tiếng như Vogue, Harper's Bazaar và Kinfolk, chúng tôi tin rằng cái đẹp chân thực của báo chí không nằm ở những giật gân, câu khách, mà ở chiều sâu nhân văn, sự thanh lịch của con chữ và những câu chuyện tử tế chạm đến đáy lòng độc giả.
  `;

  const p3 = isEn ? `
    <strong>Editorial Principle:</strong> Integrity in truth, empathy in perspective, and refined aesthetics across every page.
  ` : `
    <strong>Phương châm của tòa soạn:</strong> Trung thực trong sự thật, nhân ái trong góc nhìn, và chuẩn mực thẩm mỹ trong từng trang viết.
  `;

  const logoDesc = isEn ? 'The continuous-line hand-drawn heart symbolizes boundless empathy connecting journalists with humanity and society.' : 'Biểu trưng trái tim vẽ tay liên tục (continuous line) biểu đạt tình yêu thương nối liền giữa người làm báo và cộng đồng xã hội.';

  const teamTitle = isEn ? 'Editorial Board &amp; Academic Advisory • ULIS - VNU' : 'Ban Biên Tập &amp; Cố Vấn Tòa Soạn • ULIS - VNU';
  const role1Title = isEn ? 'Faculty Advisor' : 'Giảng viên Phụ trách';
  const role1Dept = isEn ? 'Faculty of Linguistics &amp; Communication' : 'Khoa Ngôn ngữ &amp; Truyền thông';
  const role1Desc = isEn ? 'Guiding content strategy, editorial integrity, and international journalism standards.' : 'Cố vấn định hướng nội dung và nghiệp vụ báo chí đối ngoại.';

  const role2Title = isEn ? 'Class 6 - Group 1 - Term 127' : 'Lớp 6 - Nhóm 1 - Khóa 127';
  const role2Dept = isEn ? 'Editorial &amp; Content Production Board' : 'Ban Biên tập &amp; Sản xuất Nội dung';
  const role2Desc = isEn ? 'Content creation, international news curation, and field photojournalism.' : 'Sáng tạo nội dung, biên dịch báo chí quốc tế và phóng sự thực địa.';

  const role3Title = isEn ? 'Design &amp; Engineering Team' : 'Ban Thiết kế &amp; Kỹ thuật';
  const role3Dept = isEn ? 'Creative Direction &amp; Web Dev' : 'Creative Direction &amp; Web Dev';
  const role3Desc = isEn ? 'Crafting minimalist editorial design, Nielsen Norman UX, and Impeccable architecture.' : 'Phát triển giao diện chuẩn thời trang cao cấp và hệ thống Impeccable.';

  container.innerHTML = `
    <div class="about-view-wrapper" id="about-us" style="background:#FFFFFF; border:1px solid var(--color-border-hairline); border-radius:var(--radius-lg); padding:3rem 2.5rem; margin-top:3.5rem;">
      <div class="about-hero-banner" style="text-align:center; max-width:760px; margin:0 auto 2.5rem auto;">
        <span class="fashion-kicker" style="display:inline-block; margin-bottom:0.5rem;">${manifestoTag}</span>
        <h1 class="about-manifesto-title" style="font-family:var(--font-editorial); font-size:2.4rem; font-weight:800; color:var(--color-brand-primary);">${manifestoTitle}</h1>
        <p class="about-manifesto-subtitle" style="font-family:var(--font-editorial); font-style:italic; font-size:1.25rem; color:var(--color-brand-accent); margin-top:0.4rem;">
          ${manifestoSubtitle}
        </p>
      </div>

      <div class="about-story-grid" style="display:grid; grid-template-columns:1.3fr 0.9fr; gap:2.5rem; align-items:center;">
        <div class="about-story-text" style="font-size:0.95rem; line-height:1.75; color:var(--color-text-body);">
          <p style="margin-bottom:1rem;">${p1}</p>
          <p style="margin-bottom:1rem;">${p2}</p>
          <p>${p3}</p>
        </div>

        <div class="about-story-card" style="background:var(--color-surface-blush); border:1px solid #EEDBD6; border-radius:var(--radius-lg); padding:2rem; text-align:center;">
          <svg style="width:64px; height:60px; margin:0 auto 1rem auto; display:block;" viewBox="0 0 100 80" fill="none">
            <path d="M30 45 C15 32 8 20 22 10 C32 2 44 8 50 20 C56 8 68 2 78 10 C92 20 82 36 62 55 C54 62 50 67 48 68 C45 70 42 68 40 65 C34 58 26 48 30 45 Z" stroke="#591724" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M48 68 C56 72 70 75 80 70 C88 66 94 58 98 50" stroke="#BA6975" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="3 4"/>
          </svg>
          <h2 style="font-family:var(--font-editorial); font-size:1.75rem; font-style:italic; color:var(--color-brand-primary); margin-bottom:0.25rem;">HEARTICLES.</h2>
          <p style="font-size:0.875rem; font-weight:600; color:var(--color-brand-accent); margin-bottom:1rem;">Stories that speak to the heart.</p>
          <p style="font-size:0.875rem; color:var(--color-text-body); line-height:1.6; font-weight:500;">
            ${logoDesc}
          </p>
        </div>
      </div>

      <!-- Editorial Team Grid -->
      <div style="margin-top:2.5rem; padding-top:2rem; border-top:1px solid var(--color-border-hairline);">
        <h3 style="font-family:var(--font-editorial); font-size:1.35rem; color:var(--color-text-headline); margin-bottom:1.5rem; text-align:center;">
          ${teamTitle}
        </h3>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:1.25rem;">
          <div style="background:#FFFFFF; border:1px solid var(--color-border-hairline); border-radius:var(--radius-md); padding:1.25rem; text-align:center;">
            <div style="width:48px; height:48px; border-radius:50%; background:var(--color-brand-primary); color:#FFF; display:flex; align-items:center; justify-content:center; font-weight:bold; margin:0 auto 0.75rem auto;">GV</div>
            <h4 style="font-family:var(--font-serif); font-size:1rem; font-weight:700;">${role1Title}</h4>
            <p style="font-size:0.75rem; color:var(--color-brand-accent); font-weight:600;">${role1Dept}</p>
            <p style="font-size:0.8125rem; color:var(--color-text-muted); font-weight:500; margin-top:0.3rem;">${role1Desc}</p>
          </div>
          <div style="background:#FFFFFF; border:1px solid var(--color-border-hairline); border-radius:var(--radius-md); padding:1.25rem; text-align:center;">
            <div style="width:48px; height:48px; border-radius:50%; background:var(--color-brand-accent); color:#FFF; display:flex; align-items:center; justify-content:center; font-weight:bold; margin:0 auto 0.75rem auto;">N1</div>
            <h4 style="font-family:var(--font-serif); font-size:1rem; font-weight:700;">${role2Title}</h4>
            <p style="font-size:0.75rem; color:var(--color-brand-primary); font-weight:600;">${role2Dept}</p>
            <p style="font-size:0.8125rem; color:var(--color-text-muted); font-weight:500; margin-top:0.3rem;">${role2Desc}</p>
            <a href="mailto:class6group1term127@gmail.com" style="display:inline-flex; align-items:center; gap:0.35rem; margin-top:0.6rem; font-size:0.75rem; font-weight:700; color:var(--color-brand-primary); text-decoration:none; background:rgba(84,17,30,0.06); padding:4px 10px; border-radius:12px; border:1px solid rgba(84,17,30,0.12);"><i class="fas fa-envelope"></i> class6group1term127@gmail.com</a>
          </div>
          <div style="background:#FFFFFF; border:1px solid var(--color-border-hairline); border-radius:var(--radius-md); padding:1.25rem; text-align:center;">
            <div style="width:48px; height:48px; border-radius:50%; background:var(--primitive-burgundy-900); color:#FFF; display:flex; align-items:center; justify-content:center; font-weight:bold; margin:0 auto 0.75rem auto;">UI</div>
            <h4 style="font-family:var(--font-serif); font-size:1rem; font-weight:700;">${role3Title}</h4>
            <p style="font-size:0.75rem; color:var(--color-brand-accent); font-weight:600;">${role3Dept}</p>
            <p style="font-size:0.8125rem; color:var(--color-text-muted); font-weight:500; margin-top:0.3rem;">${role3Desc}</p>
          </div>
        </div>
      </div>

      <!-- Group & Course Identity Summary Box -->
      <div style="margin-top:2rem; background:rgba(84,17,30,0.03); border:1px dashed var(--color-border-hairline); border-radius:var(--radius-md); padding:1.25rem 1.75rem; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:1rem;">
        <div>
          <span style="font-size:0.75rem; font-weight:800; color:var(--color-brand-primary); letter-spacing:0.06em; text-transform:uppercase;">
            <i class="fas fa-id-card"></i> ${isEn ? 'OFFICIAL EDITORIAL & ACADEMIC ATTRIBUTION' : 'THÔNG TIN TÒA SOẠN & ĐƠN VỊ THỰC HIỆN'}
          </span>
          <p style="font-size:0.875rem; color:var(--color-text-body); margin-top:0.3rem; line-height:1.5;">
            ${isEn ? '<strong>Publication:</strong> HEARTICLES. Digital Newspaper • <strong>Curriculum:</strong> Journalism &amp; Media Studies (BCTT)' : '<strong>Ấn phẩm:</strong> Tạp chí Báo điện tử HEARTICLES. • <strong>Học phần:</strong> Báo chí &amp; Truyền thông (BCTT)'}<br>
            ${isEn ? '<strong>Author Collective:</strong> Class 6 - Group 1 - Term 127 (Faculty of Linguistics &amp; Communications, ULIS - VNU)' : '<strong>Tập thể tác giả:</strong> Lớp 6 - Nhóm 1 - Khóa 127 (Khoa Ngôn ngữ &amp; Truyền thông, Trường ĐH Ngoại ngữ - ĐHQGHN)'}
          </p>
        </div>
        <div>
          <a href="mailto:class6group1term127@gmail.com" class="academic-email-link" style="display:inline-flex; font-size:0.85rem; padding:6px 14px;">
            <i class="fas fa-paper-plane"></i> class6group1term127@gmail.com
          </a>
        </div>
      </div>
    </div>
  `;
}

window.openArticleModal = function(articleId) {
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
  }

  body.innerHTML = `
    <div class="article-reading-content" style="font-size: ${currentFontSize}rem;">
      <div class="article-breadcrumb">
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
        </div>

        <div class="comments-list-container" id="commentsListContainer">
          ${savedComments.length === 0 ? '<p style="color:var(--color-text-muted); font-size:0.875rem; font-style:italic;">Hãy là người đầu tiên chia sẻ cảm nghĩ về bài viết này.</p>' : ''}
          ${savedComments.map(c => `
            <div class="comment-item-card" style="background:white; border:1px solid var(--color-border-hairline); border-radius:var(--radius-md); padding:0.85rem 1rem; margin-bottom:0.75rem;">
              <div style="display:flex; justify-content:space-between; margin-bottom:0.35rem;">
                <strong style="color:var(--color-brand-primary); font-size:0.875rem;">${c.author}</strong>
                <span style="font-size:0.75rem; color:var(--color-text-muted);">${c.time}</span>
              </div>
              <p style="font-size:0.875rem; color:var(--color-text-body); margin:0;">${c.text}</p>
            </div>
          `).join('')}
        </div>
      </div>
    </div>
  `;

  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
};

window.closeArticleModal = function() {
  const modal = document.getElementById('articleReaderModal');
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }
  if (isSpeaking) {
    stopTextToSpeech();
  }
};

/* ===================================================================
   COMMENT & LIKE SYSTEM
   =================================================================== */
window.submitComment = function(articleId) {
  const input = document.getElementById('newCommentInput');
  if (!input || !input.value.trim()) return;

  const key = `comments_${articleId}`;
  const existing = JSON.parse(localStorage.getItem(key) || '[]');
  const now = new Date();
  const timeStr = `${now.getHours()}:${String(now.getMinutes()).padStart(2, '0')} - ${now.getDate()}/${now.getMonth() + 1}`;

  existing.unshift({
    author: 'Độc giả ULIS - VNU',
    time: timeStr,
    text: input.value.trim()
  });

  localStorage.setItem(key, JSON.stringify(existing));
  input.value = '';
  openArticleModal(articleId);
  showToast('Bình luận của bạn đã được xuất bản!', 'check');
};

window.toggleLikeArticle = function(articleId) {
  const isLiked = localStorage.getItem(`liked_${articleId}`) === 'true';
  const article = ARTICLES_DATA.find(a => a.id === articleId);
  const btn = document.getElementById(`likeBtn_${articleId}`);
  const countEl = document.getElementById(`likeCount_${articleId}`);

  if (isLiked) {
    localStorage.removeItem(`liked_${articleId}`);
    if (btn) btn.classList.remove('liked');
    if (countEl && article) countEl.textContent = article.likes;
    showToast('Đã bỏ yêu thích bài viết', 'heart-broken');
  } else {
    localStorage.setItem(`liked_${articleId}`, 'true');
    if (btn) {
      btn.classList.add('liked');
      triggerHeartBurst(btn);
    }
    if (countEl && article) countEl.textContent = article.likes + 1;
    showToast('Đã thả tim bài viết! Cảm ơn bạn.', 'heart');
  }
};

function triggerHeartBurst(element) {
  const rect = element.getBoundingClientRect();
  for (let i = 0; i < 8; i++) {
    const p = document.createElement('div');
    p.className = 'burst-particle';
    p.innerHTML = '<i class="fas fa-heart" style="color:#BA6975; font-size:12px;"></i>';
    p.style.position = 'fixed';
    p.style.left = `${rect.left + rect.width / 2}px`;
    p.style.top = `${rect.top + rect.height / 2}px`;
    p.style.pointerEvents = 'none';
    p.style.zIndex = '9999';
    p.style.transition = 'all 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
    document.body.appendChild(p);

    const angle = (i / 8) * 2 * Math.PI;
    const dist = 35 + Math.random() * 20;
    setTimeout(() => {
      p.style.transform = `translate(${Math.cos(angle) * dist}px, ${Math.sin(angle) * dist}px) scale(0)`;
      p.style.opacity = '0';
    }, 10);

    setTimeout(() => {
      p.remove();
    }, 650);
  }
}

/* ===================================================================
   TEXT TO SPEECH (Web Speech API)
   =================================================================== */
window.toggleTextToSpeech = function(articleId) {
  if (isSpeaking) {
    stopTextToSpeech();
  } else {
    startTextToSpeech(articleId);
  }
};

function startTextToSpeech(articleId) {
  const article = ARTICLES_DATA.find(a => a.id === articleId);
  if (!article || !('speechSynthesis' in window)) {
    alert(currentLanguage === 'en' ? 'Your browser does not support Web Speech API.' : 'Trình duyệt của bạn chưa hỗ trợ tính năng Web Speech API.');
    return;
  }

  window.speechSynthesis.cancel();

  const isEn = (currentLanguage === 'en');
  let plainText = '';
  const content = (isEn && article.content_en) ? article.content_en : article.content;
  if (typeof content === 'string') {
    plainText = content.replace(/<[^>]*>/g, ' ');
  } else if (Array.isArray(content)) {
    plainText = content.join(' ');
  }

  const title = (isEn && article.title_en) ? article.title_en : article.title;
  const subtitle = (isEn && article.subtitle_en) ? article.subtitle_en : article.subtitle;
  const textToRead = `${title}. ${subtitle}. ${plainText}`;
  speechUtterance = new SpeechSynthesisUtterance(textToRead);
  speechUtterance.lang = isEn ? 'en-US' : 'vi-VN';
  speechUtterance.rate = 0.95;

  speechUtterance.onstart = () => {
    isSpeaking = true;
    updateTTSButton(true);
    showToast(isEn ? 'Playing article audio...' : 'Đang phát giọng đọc bài báo...', 'volume-up');
  };

  speechUtterance.onend = () => {
    isSpeaking = false;
    updateTTSButton(false);
  };

  speechUtterance.onerror = () => {
    isSpeaking = false;
    updateTTSButton(false);
  };

  window.speechSynthesis.speak(speechUtterance);
}

function stopTextToSpeech() {
  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel();
  }
  isSpeaking = false;
  updateTTSButton(false);
}

function updateTTSButton(speaking) {
  const btn = document.getElementById('btnTTS');
  if (btn) {
    btn.innerHTML = `<i class="fas ${speaking ? 'fa-pause' : 'fa-volume-up'}"></i> ${speaking ? 'Tạm dừng' : 'Đọc bài báo'}`;
    btn.classList.toggle('active', speaking);
  }
}

window.adjustFontSize = function(delta) {
  currentFontSize = Math.min(Math.max(currentFontSize + delta, 0.95), 1.45);
  const content = document.querySelector('.article-reading-content');
  if (content) {
    content.style.fontSize = `${currentFontSize}rem`;
  }
};

window.shareArticle = function(title) {
  if (navigator.share) {
    navigator.share({
      title: title,
      text: `${title} - Đọc trên Tạp chí HEARTICLES. (ULIS - VNU)`,
      url: window.location.href
    }).catch(() => {});
  } else {
    navigator.clipboard.writeText(window.location.href);
    showToast('Đã sao chép liên kết bài viết!', 'link');
  }
};

/* ===================================================================
   SEARCH ENGINE (Instant Live Search)
   =================================================================== */
window.openSearchModal = function() {
  const modal = document.getElementById('searchModal');
  const input = document.getElementById('searchInput');
  if (modal) {
    modal.classList.add('active');
    setTimeout(() => { if (input) input.focus(); }, 100);
  }
};

window.closeSearchModal = function() {
  const modal = document.getElementById('searchModal');
  if (modal) modal.classList.remove('active');
};

window.handleSearchInput = function(query) {
  const resultsBox = document.getElementById('searchResults');
  if (!resultsBox) return;

  const trimmed = query.trim().toLowerCase();
  if (!trimmed) {
    resultsBox.innerHTML = `
      <div style="padding:1rem 0;">
        <p style="color:var(--color-text-muted); font-size:0.875rem; margin-bottom:0.75rem;">Từ khóa thịnh hành gợi ý:</p>
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem;">
          <button class="search-tag-chip" onclick="applySearchTag('Hội An')">#Hội An</button>
          <button class="search-tag-chip" onclick="applySearchTag('Taeyang')">#Taeyang</button>
          <button class="search-tag-chip" onclick="applySearchTag('Trending')">#Trending</button>
          <button class="search-tag-chip" onclick="applySearchTag('Quốc hội')">#Quốc hội</button>
          <button class="search-tag-chip" onclick="applySearchTag('ULIS')">#ULIS - VNU</button>
        </div>
      </div>
    `;
    return;
  }

  const isEn = (currentLanguage === 'en');
  const matches = ARTICLES_DATA.filter(a => {
    return a.title.toLowerCase().includes(trimmed) ||
           (a.title_en && a.title_en.toLowerCase().includes(trimmed)) ||
           a.subtitle.toLowerCase().includes(trimmed) ||
           (a.subtitle_en && a.subtitle_en.toLowerCase().includes(trimmed)) ||
           a.author.toLowerCase().includes(trimmed) ||
           a.categoryName.toLowerCase().includes(trimmed) ||
           (a.tags && a.tags.some(t => t.toLowerCase().includes(trimmed)));
  });

  if (matches.length === 0) {
    const emptyTitle = isEn ? `No articles found matching '<strong>${query}</strong>'` : `Không tìm thấy bài viết nào khớp với '<strong>${query}</strong>'`;
    const emptySub = isEn ? `Try searching by topic: <em>Trending, Society, Human Stories, Mind &amp; Soul...</em>` : `Hãy thử tìm theo tên chuyên mục: <em>Trending, Society, Human Stories, Mind &amp; Soul...</em>`;
    resultsBox.innerHTML = `
      <div style="text-align:center; padding:2rem 0; color:var(--color-text-muted);">
        <i class="fas fa-search" style="font-size:2rem; margin-bottom:0.75rem; opacity:0.5;"></i>
        <p>${emptyTitle}</p>
        <p style="font-size:0.8125rem; margin-top:0.25rem;">${emptySub}</p>
      </div>
    `;
    return;
  }

  resultsBox.innerHTML = matches.map(item => `
    <div class="search-result-item" onclick="closeSearchModal(); openArticleModal('${item.id}')" style="display:flex; gap:1rem; align-items:center; padding:0.75rem; border-bottom:1px solid var(--color-border-hairline); cursor:pointer;">
      <img src="${item.image}" alt="${item.title}" style="width:60px; height:60px; border-radius:8px; object-fit:cover;">
      <div>
        <span style="font-size:0.6875rem; color:var(--color-brand-primary); font-weight:800; text-transform:uppercase;">${item.categoryName}</span>
        <h4 style="font-family:var(--font-serif); font-size:0.95rem; font-weight:700; color:var(--color-text-headline); margin:0.15rem 0;">${highlightMatch(item.title, trimmed)}</h4>
        <span style="font-size:0.75rem; color:var(--color-text-muted);">${item.author} • ${item.readTime}</span>
      </div>
    </div>
  `).join('');
};

window.applySearchTag = function(tag) {
  const input = document.getElementById('searchInput');
  if (input) {
    input.value = tag;
    handleSearchInput(tag);
  }
};

function highlightMatch(text, query) {
  const regex = new RegExp(`(${query})`, 'gi');
  return text.replace(regex, '<mark style="background:#FCE8EC; color:#591724; font-weight:bold;">$1</mark>');
}

/* ===================================================================
   ONBOARDING SYSTEM (3-Step First-Time Walkthrough)
   =================================================================== */
function initOnboarding() {
  const hasOnboarded = localStorage.getItem('hearticles_fashion_onboarded_v2');
  if (!hasOnboarded) {
    setTimeout(() => {
      openOnboardingModal();
    }, 1200);
  }
}

window.openOnboardingModal = function() {
  const modal = document.getElementById('onboardModal');
  if (modal) {
    modal.classList.add('active');
    currentOnboardStep = 1;
    renderOnboardStep(1);
  }
};

window.closeOnboardingModal = function() {
  const modal = document.getElementById('onboardModal');
  if (modal) modal.classList.remove('active');
  localStorage.setItem('hearticles_fashion_onboarded_v2', 'true');
};

window.nextOnboardStep = function() {
  if (currentOnboardStep < 3) {
    currentOnboardStep++;
    renderOnboardStep(currentOnboardStep);
  } else {
    closeOnboardingModal();
    showToast('Chào mừng bạn đến với HEARTICLES.!', 'heart');
  }
};

function renderOnboardStep(step) {
  const dots = document.querySelectorAll('.onboard-step-dot');
  dots.forEach((dot, idx) => {
    dot.classList.toggle('active', idx === step - 1);
  });

  const content = document.getElementById('onboardStepContent');
  const btnNext = document.getElementById('onboardBtnNext');
  if (!content) return;

  if (step === 1) {
    content.innerHTML = `
      <div class="onboard-badge">BƯỚC 1 / 3 • GIỚI THIỆU</div>
      <h2 class="onboard-title">Chào mừng bạn đến với HEARTICLES.</h2>
      <p class="onboard-desc">
        Tạp chí báo điện tử đa phương tiện xuất bản bởi sinh viên <strong>Trường Đại học Ngoại ngữ - ĐHQGHN (ULIS - VNU)</strong>. Nơi tin tức khởi nguồn từ nhịp đập trái tim và lòng trắc ẩn.
      </p>
      <div class="onboard-feature-grid">
        <div class="onboard-feature-item">
          <h4><i class="fas fa-check-circle" style="color:var(--color-brand-primary);"></i> Thẩm mỹ Tạp chí Thời trang</h4>
          <p>Thiết kế tinh xảo lấy cảm hứng từ Vogue, Kinfolk với tông màu đỏ rượu ấm áp và chữ serif cổ điển.</p>
        </div>
        <div class="onboard-feature-item">
          <h4><i class="fas fa-check-circle" style="color:var(--color-brand-primary);"></i> 100% Ảnh báo chí gốc</h4>
          <p>Toàn bộ 34 bài viết và hình ảnh được trích xuất chân thực từ kho tư liệu báo chí chính thống.</p>
        </div>
      </div>
    `;
    if (btnNext) btnNext.textContent = 'Tiếp tục';
  } else if (step === 2) {
    content.innerHTML = `
      <div class="onboard-badge">BƯỚC 2 / 3 • CÁ NHÂN HÓA</div>
      <h2 class="onboard-title">Tùy biến trải nghiệm đọc</h2>
      <p class="onboard-desc">
        HEARTICLES. trang bị đầy đủ công cụ đọc báo hiện đại:
      </p>
      <div class="onboard-feature-grid">
        <div class="onboard-feature-item">
          <h4><i class="fas fa-volume-up" style="color:var(--color-brand-primary);"></i> Đọc báo tự động</h4>
          <p>Nghe bài báo rảnh tay qua công nghệ giọng đọc thông minh Web Speech API.</p>
        </div>
        <div class="onboard-feature-item">
          <h4><i class="fas fa-keyboard" style="color:var(--color-brand-primary);"></i> Phím tắt tiện lợi</h4>
          <p>Bấm phím <code>/</code> để tìm kiếm tức thì, phím <code>T</code> để phóng to chữ, <code>ESC</code> để đóng bài đọc.</p>
        </div>
      </div>
    `;
    if (btnNext) btnNext.textContent = 'Tiếp tục';
  } else {
    content.innerHTML = `
      <div class="onboard-badge">BƯỚC 3 / 3 • HOÀN TẤT</div>
      <h2 class="onboard-title">Khám phá 34 Phóng sự Đặc sắc</h2>
      <p class="onboard-desc">
        Khám phá ngay các tiêu điểm trang bìa: <strong>"Lawmakers Propose Measures"</strong>, <strong>"Gánh mưu sinh Hội An"</strong>, và ký sự <strong>"Taeyang tại concert Mỹ Đình"</strong>.
      </p>
      <div style="background:var(--color-surface-blush); border:1px dashed #EEDBD6; border-radius:12px; padding:1.25rem; margin-bottom:1.5rem; text-align:center;">
        <i class="fas fa-envelope-open-text" style="color:var(--color-brand-primary); font-size:1.75rem; margin-bottom:0.5rem;"></i>
        <p style="font-size:0.9rem; font-weight:700; color:var(--color-brand-primary);">Nhận bản tin sáng 7:00 AM mỗi ngày</p>
        <p style="font-size:0.75rem; color:var(--color-text-muted);">Bấm nút 'Subscribe' ở góc trên trang để đăng ký miễn phí.</p>
      </div>
    `;
    if (btnNext) btnNext.textContent = 'Bắt đầu trải nghiệm';
  }
}

/* ===================================================================
   READING PROGRESS BAR
   =================================================================== */
function setupReadingProgressBar() {
  window.addEventListener('scroll', () => {
    const total = document.documentElement.scrollHeight - window.innerHeight;
    if (total > 0) {
      const progress = (window.scrollY / total) * 100;
      const bar = document.getElementById('readingProgressBar');
      if (bar) bar.style.width = `${progress}%`;
    }
  }, { passive: true });
}

/* ===================================================================
   NETWORK / OFFLINE DETECTOR
   =================================================================== */
function setupNetworkStatus() {
  const banner = document.getElementById('offlineBanner');
  window.addEventListener('offline', () => {
    if (banner) banner.classList.add('active');
    showToast('Mất kết nối mạng. Bạn đang xem bản lưu ngoại tuyến.', 'wifi');
  });
  window.addEventListener('online', () => {
    if (banner) banner.classList.remove('active');
    showToast('Đã khôi phục kết nối internet.', 'wifi');
  });
}

/* ===================================================================
   TOAST NOTIFICATION ENGINE
   =================================================================== */
window.showToast = function(message, icon = 'check') {
  let toast = document.getElementById('impeccableToast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'impeccableToast';
    toast.className = 'toast-notification';
    document.body.appendChild(toast);
  }
  toast.innerHTML = `<i class="fas fa-${icon}" style="color:var(--color-brand-accent);"></i> <span>${message}</span>`;
  toast.classList.add('show');
  clearTimeout(toast.hideTimeout);
  toast.hideTimeout = setTimeout(() => {
    toast.classList.remove('show');
  }, 3200);
};

/* ===================================================================
   KEYBOARD SHORTCUTS MODAL
   =================================================================== */
window.openShortcutsModal = function() {
  const modal = document.getElementById('shortcutsModal');
  if (modal) modal.classList.add('active');
};

window.closeShortcutsModal = function() {
  const modal = document.getElementById('shortcutsModal');
  if (modal) modal.classList.remove('active');
};

/* ===================================================================
   DRAWER / OFFCANVAS MENU
   =================================================================== */
window.openDrawer = function() {
  const drawer = document.getElementById('offcanvasDrawer');
  const backdrop = document.getElementById('drawerBackdrop');
  if (drawer && backdrop) {
    drawer.classList.add('active');
    backdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
};

window.closeDrawer = function() {
  const drawer = document.getElementById('offcanvasDrawer');
  const backdrop = document.getElementById('drawerBackdrop');
  if (drawer && backdrop) {
    drawer.classList.remove('active');
    backdrop.classList.remove('active');
    document.body.style.overflow = '';
  }
};

/* ===================================================================
   SUBSCRIBE MODAL SIMULATION
   =================================================================== */
window.openSubscribeModal = function() {
  const isEn = (typeof currentLanguage !== 'undefined' && currentLanguage === 'en');
  const promptMsg = isEn 
    ? 'Enter your email to subscribe to HEARTICLES. Daily Editorial (Class 6 - Group 1 - Term 127 • ULIS - VNU):' 
    : 'Nhập địa chỉ email của bạn để nhận bản tin thời trang & nhân văn HEARTICLES. (Lớp 6 - Nhóm 1 - Khóa 127 • ULIS - VNU):';
  
  const email = prompt(promptMsg);
  if (email && email.includes('@')) {
    localStorage.setItem('hearticles_subscribed_email', email);
    const successMsg = isEn 
      ? 'Thank you! Successfully subscribed. Editorial contact: class6group1term127@gmail.com' 
      : 'Cảm ơn bạn! Đã đăng ký nhận bản tin thành công. Liên hệ tòa soạn: class6group1term127@gmail.com';
    showToast(successMsg, 'check-circle');
  } else if (email) {
    alert(isEn ? 'Please enter a valid email address.' : 'Vui lòng nhập địa chỉ email hợp lệ.');
  }
};

/* ===================================================================
   READER POLL WIDGET
   =================================================================== */
function setupPoll() {
  const container = document.getElementById('pollContainer');
  if (!container) return;
  const pollVoted = localStorage.getItem('hearticles_poll_voted');
  if (pollVoted) {
    showPollResults();
  }
}

window.votePoll = function(optionIndex) {
  localStorage.setItem('hearticles_poll_voted', optionIndex);
  showPollResults();
  showToast('Cảm ơn bạn đã đóng góp ý kiến!', 'poll');
};

function showPollResults() {
  const container = document.getElementById('pollContainer');
  if (!container) return;
  container.innerHTML = `
    <div class="poll-results-box" style="background:rgba(255,255,255,0.08); padding:1rem; border-radius:8px;">
      <div style="margin-bottom:0.75rem;">
        <div style="display:flex; justify-content:space-between; font-size:0.8125rem; margin-bottom:0.25rem;">
          <span>1. Quy hoạch tuyến phố đi bộ văn hóa</span>
          <strong>52% (1.420 phiếu)</strong>
        </div>
        <div style="background:rgba(255,255,255,0.2); height:6px; border-radius:3px; overflow:hidden;">
          <div style="background:#BA6975; width:52%; height:100%;"></div>
        </div>
      </div>
      <div style="margin-bottom:0.75rem;">
        <div style="display:flex; justify-content:space-between; font-size:0.8125rem; margin-bottom:0.25rem;">
          <span>2. Tôn vinh nét đẹp văn hóa truyền thống</span>
          <strong>34% (930 phiếu)</strong>
        </div>
        <div style="background:rgba(255,255,255,0.2); height:6px; border-radius:3px; overflow:hidden;">
          <div style="background:#E8A8B1; width:34%; height:100%;"></div>
        </div>
      </div>
      <div>
        <div style="display:flex; justify-content:space-between; font-size:0.8125rem; margin-bottom:0.25rem;">
          <span>3. Hỗ trợ sinh kế bền vững cho người nghèo</span>
          <strong>14% (385 phiếu)</strong>
        </div>
        <div style="background:rgba(255,255,255,0.2); height:6px; border-radius:3px; overflow:hidden;">
          <div style="background:#D8C0C4; width:14%; height:100%;"></div>
        </div>
      </div>
      <div style="margin-top:1rem; font-size:0.75rem; color:#FFD0D0; text-align:right;">
        <i class="fas fa-check-circle"></i> Bạn đã tham gia biểu quyết khảo sát này.
      </div>
    </div>
  `;
}

/* ===================================================================
   IMAGE ERROR HANDLER
   =================================================================== */
window.handleImageError = function(img) {
  img.onerror = null;
  img.src = 'assets/images/trending/image8.jpg';
};

/* ===================================================================
   GLOBAL EVENT LISTENERS (Keyboard shortcuts: /, ESC, ?, T)
   =================================================================== */
function setupEventListeners() {
  document.addEventListener('keydown', (e) => {
    if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) {
      if (e.key === 'Escape') {
        closeSearchModal();
      }
      return;
    }

    if (e.key === 'Escape') {
      closeArticleModal();
      closeSearchModal();
      closeDrawer();
      closeOnboardingModal();
      closeShortcutsModal();
    } else if (e.key === '/') {
      e.preventDefault();
      openSearchModal();
    } else if (e.key === '?' || (e.shiftKey && e.key === '/')) {
      e.preventDefault();
      openShortcutsModal();
    } else if (e.key === 't' || e.key === 'T') {
      adjustFontSize(currentFontSize >= 1.3 ? -0.3 : 0.15);
    }
  });
}
