import sys

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

# Replace VIDEO_CLIPS definition with bilingual support
target_clips = """const VIDEO_CLIPS = [
  {
    id: "clip-1",
    category: "Trending",
    title: "Phóng sự: Gánh mưu sinh và nét đẹp lao động bình dị phố cổ Hội An",
    desc: "Hình ảnh đôi quang gánh trĩu nặng nhịp sống mưu sinh, vẻ đẹp cần lao mộc mạc và ký ức rêu phong trên từng ngõ nhỏ di sản.",
    url: "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    thumb: "assets/images/trending/image8.jpg",
    articleId: "trending-4"
  },
  {
    id: "clip-2",
    category: "Mind & Soul",
    title: "Taeyang (BigBang) và đêm nhạc bùng nổ tại SVĐ Quốc gia Mỹ Đình",
    desc: "Khoảnh khắc nam nghệ sĩ xúc động trước tình cảm nồng nhiệt của hàng vạn khán giả Thủ đô và tình yêu với ẩm thực phở Hà Nội.",
    url: "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    thumb: "assets/images/mind_&_soul/image2.jpg",
    articleId: "mind-1"
  },
  {
    id: "clip-3",
    category: "Human Stories",
    title: "Những người nông dân gieo hạt mầm tri thức tại Gruver, Texas",
    desc: "Câu chuyện cảm động về cộng đồng nông dân tình nguyện canh tác gây quỹ 400.000 USD học bổng mỗi năm cho học sinh nghèo vào đại học.",
    url: "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    thumb: "assets/images/human_stories/image5.png",
    articleId: "human-4"
  },
  {
    id: "clip-4",
    category: "Society",
    title: "Chiến dịch 500 ngày đêm ADN: Trả lại danh tính cho gần 800 hài cốt liệt sĩ",
    desc: "Hành trình thầm lặng nhưng đầy tự hào của các nhà khoa học và cơ quan chức năng vì đạo lý 'Uống nước nhớ nguồn'.",
    url: "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    thumb: "assets/images/human_stories/image17.jpg",
    articleId: "trending-5"
  },
  {
    id: "clip-5",
    category: "About Us",
    title: "HEARTICLES Manifesto: 'Stories that speak to the heart' • ULIS - VNU",
    desc: "Thông điệp tôn chỉ báo chí nhân văn và hậu trường thực hiện tạp chí số từ nhóm sinh viên Lớp 6 - Nhóm 1 - Khóa 127, ULIS - VNU.",
    url: "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    thumb: "assets/images/trending/image10.jpg",
    articleId: "about"
  }
];"""

rep_clips = """const VIDEO_CLIPS = [
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
];"""

# Replace initApp and add language handling
target_init = """let currentFontSize = 1.15; // rem
let isSpeaking = false;
let speechUtterance = null;
let currentOnboardStep = 1;
let currentCategoryFilter = 'all';

function initApp() {
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
}"""

rep_init = """let currentFontSize = 1.15; // rem
let isSpeaking = false;
let speechUtterance = null;
let currentOnboardStep = 1;
let currentCategoryFilter = 'all';
let currentLanguage = localStorage.getItem('hearticles_lang') || 'vi';

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
  currentLanguage = localStorage.getItem('hearticles_lang') || 'vi';
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

  // Update button active state
  document.querySelectorAll('#btnLangVI, #drawerLangVI').forEach(btn => {
    if (btn) btn.classList.toggle('active', lang === 'vi');
  });
  document.querySelectorAll('#btnLangEN, #drawerLangEN').forEach(btn => {
    if (btn) btn.classList.toggle('active', lang === 'en');
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
}"""

# Update live date for bilingual
target_date = """function updateLiveDate() {
  const dateEl = document.getElementById('liveDateWidget');
  if (!dateEl) return;
  const now = new Date();
  const days = ['Chủ Nhật', 'Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy'];
  const dayName = days[now.getDay()];
  const dateStr = `${dayName}, ${now.getDate()} Tháng ${now.getMonth() + 1}, ${now.getFullYear()} | Hà Nội 26°C`;
  dateEl.innerHTML = `<i class="far fa-calendar-alt"></i> <span style="font-variant-numeric: tabular-nums;">${dateStr}</span>`;
}"""

rep_date = """function updateLiveDate() {
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
}"""

# Update renderVideoHub for bilingual
target_videohub = """function renderVideoHub() {
  const container = document.getElementById('videoHubContent');
  if (!container) return;

  const mainClip = VIDEO_CLIPS[0];
  container.innerHTML = `
    <div class="video-grid-layout">
      <div class="main-video-player-box">
        <div class="video-responsive-embed">
          <iframe id="activeVideoFrame" src="${mainClip.url}" title="${mainClip.title}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
        <div class="main-video-details">
          <span class="category-tag" id="activeVideoCategory" style="color:var(--color-brand-primary); font-weight:800;">${mainClip.category}</span>
          <h2 class="main-video-title" id="activeVideoTitle" style="font-family:var(--font-editorial); font-size:1.5rem; margin-top:0.4rem;">${mainClip.title}</h2>
          <p class="main-video-desc" id="activeVideoDesc" style="color:var(--color-text-body); font-size:0.95rem; line-height:1.6; font-weight:500;">${mainClip.desc}</p>
        </div>
      </div>

      <div class="video-playlist">
        ${VIDEO_CLIPS.map((clip, idx) => `
          <div class="playlist-card ${idx === 0 ? 'active' : ''}" onclick="switchVideo('${clip.id}')">
            <div class="playlist-thumb-wrap">
              <img src="${clip.thumb}" alt="${clip.title}" loading="lazy" onerror="handleImageError(this)">
              <div class="playlist-play-icon"><i class="fas fa-play"></i></div>
            </div>
            <div class="playlist-info">
              <span class="playlist-cat">${clip.category}</span>
              <h4 class="playlist-title">${clip.title}</h4>
            </div>
          </div>
        `).join('')}
      </div>
    </div>
  `;
}"""

rep_videohub = """function renderVideoHub() {
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
}"""

# Update switchVideo
target_switch = """window.switchVideo = function(clipId) {
  const clip = VIDEO_CLIPS.find(c => c.id === clipId);
  if (!clip) return;
  const frame = document.getElementById('activeVideoFrame');
  const cat = document.getElementById('activeVideoCategory');
  const title = document.getElementById('activeVideoTitle');
  const desc = document.getElementById('activeVideoDesc');

  if (frame) frame.src = clip.url;
  if (cat) cat.textContent = clip.category;
  if (title) title.textContent = clip.title;
  if (desc) desc.textContent = clip.desc;

  document.querySelectorAll('.playlist-card').forEach(card => card.classList.remove('active'));
  event.currentTarget.classList.add('active');
};"""

rep_switch = """window.switchVideo = function(clipId) {
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
};"""

norm_js = js.replace("\r\n", "\n")
subs = [
    (target_clips, rep_clips),
    (target_init, rep_init),
    (target_date, rep_date),
    (target_videohub, rep_videohub),
    (target_switch, rep_switch)
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

print(f"Applied {applied}/{len(subs)} i18n core updates to js/app.js!")
