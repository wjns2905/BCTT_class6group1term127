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
let currentActiveClipId = 'clip-1';
let isVideoPlaying = false;

function initApp() {
  initLanguage();
  updateLiveDate();
  setupEventListeners();
  renderVideoHub();
  renderFashionJournal('all');
  renderCategoryPageArticles();
  renderAboutUsSection();
  syncHomepageCardsWithData(lang);
  setupPoll();
  setupHeartTapWidget();
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

function setLanguage(lang) {
  if (lang !== 'vi' && lang !== 'en') return;
  currentLanguage = lang;
  localStorage.setItem('hearticles_lang', lang);
  applyLanguage(lang);
}
window.setLanguage = setLanguage;

function toggleLanguage() {
  const nextLang = currentLanguage === 'vi' ? 'en' : 'vi';
  setLanguage(nextLang);
}
window.toggleLanguage = toggleLanguage;


function syncHomepageCardsWithData(lang) {
  if (typeof ARTICLES_DATA === 'undefined') return;
  const isEn = (lang === 'en');

  document.querySelectorAll('[onclick*="openArticleModal"]').forEach(el => {
    const match = el.getAttribute('onclick').match(/openArticleModal\(['"]([^'"]+)['"]\)/);
    if (!match) return;
    const aid = match[1];
    const art = ARTICLES_DATA.find(a => a.id === aid);
    if (!art) return;

    // 1. Sync Image src if present
    const img = el.querySelector('img');
    if (img && art.image && !img.src.endsWith(art.image)) {
      img.src = art.image;
    }

    // 2. Sync title if present and not overridden by data-i18n
    const titleEl = el.querySelector('.stream-mini-headline, .center-post-title, .widget-card-headline, .mosaic-small-title, .culture-item-title, .related-text');
    if (titleEl && !titleEl.hasAttribute('data-i18n')) {
      const chosenTitle = isEn ? (art.title_en || art.title) : (art.title || art.title_en);
      if (chosenTitle) {
        titleEl.textContent = chosenTitle;
      }
    }
  });
}
window.syncHomepageCardsWithData = syncHomepageCardsWithData;

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
  syncHomepageCardsWithData(lang);

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
   DATE & TIME DISPLAY (Tabular Figures & Vietnamese/English Time)
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
   MULTIMEDIA & VIDEO PHÓNG SỰ HUB (12 Authentic Clips from [BCTT] Video)
   Curated by Quỳnh & Class 6 Group 1 Term 127 • VTV & Documentary Features
   =================================================================== */
let currentVideoCategoryFilter = 'all';

const VIDEO_CLIPS = [
  {
    id: "clip-1",
    category: "Society",
    category_en: "Society",
    title: "Áo dài tôn vinh văn hóa Việt Nam tại Phần Lan",
    title_en: "Ao Dai Celebrates Vietnamese Culture in Finland",
    desc: "Hội Áo dài Việt Nam tại Phần Lan chính thức ra mắt sáng kiến mang 1.000 tà áo dài truyền thống tới quốc gia Bắc Âu qua dự án 'Ngôi nhà Áo dài'.",
    desc_en: "The Vietnamese Ao Dai Association in Finland launches a landmark initiative: bringing 1,000 traditional Ao Dai to the Nordic country through the 'Ao Dai House' project.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/ao-dai-celebrates-vietnamese-culture-in-finland-100261028101457215.htm",
    embedUrl: "",
    duration: "4:15",
    thumb: "assets/images/society/image13.png",
    articleId: "video-1",
    sourceType: "vtv"
  },
  {
    id: "clip-2",
    category: "Society",
    category_en: "Society",
    title: "Việt Nam giải quyết các lỗ hổng về an toàn trực tuyến cho trẻ em",
    title_en: "Vietnam Tackles Gaps in Child Online Safety",
    desc: "Chiến lược quốc gia về phát triển trẻ em giai đoạn 2026–2035 nhằm củng cố kỹ năng số và xây dựng môi trường mạng an toàn cho trẻ em.",
    desc_en: "Viet Nam’s National Strategy on Child Development for 2026–2035 aims to strengthen children’s digital skills and create a safer environment for them to grow up in.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/viet-nam-tackles-gaps-in-child-online-safety-100261101165727007.htm",
    embedUrl: "",
    duration: "3:50",
    thumb: "assets/images/society/image14.png",
    articleId: "video-2",
    sourceType: "vtv"
  },
  {
    id: "clip-3",
    category: "Society",
    category_en: "Society",
    title: "Những kẻ lừa đảo trên mạng xã hội là ai? | Phim tài liệu ARTE.tv",
    title_en: "Who Are the Social Media Fraudsters? | ARTE.tv Documentary",
    desc: "Phóng sự điều tra chuyên sâu từ ARTE.tv bóc trần những cơ chế tinh vi của các đường dây lừa đảo kỹ thuật số và thao túng tâm lý trên mạng xã hội.",
    desc_en: "ARTE.tv investigative documentary delving into the sophisticated mechanisms of modern online scams and social media deception targeting digital users worldwide.",
    author: "ARTE.tv Documentary",
    watchUrl: "https://www.youtube.com/watch?v=tIqYjcHRE04",
    embedUrl: "https://www.youtube.com/embed/tIqYjcHRE04",
    duration: "14:20",
    thumb: "assets/images/society/image2.jpg",
    articleId: "video-3",
    sourceType: "youtube"
  },
  {
    id: "clip-4",
    category: "Human Stories",
    category_en: "Human Stories",
    title: "Chiến dịch 500 ngày đêm: Khi khoa học mở đường đưa các anh hùng liệt sĩ trở về",
    title_en: "500-day-and-night campaign: When science paves way to bring fallen soldiers home",
    desc: "Hành trình thầm lặng nhưng đầy tự hào ứng dụng công nghệ giám định ADN hiện đại trả lại tên cho gần 800 hài cốt liệt sĩ vì đạo lý 'Uống nước nhớ nguồn'.",
    desc_en: "How forensic science, advanced DNA technology, and dedicated devotion bring names back to nearly 800 unidentified martyrs, fulfilling a sacred mission of national gratitude.",
    author: "VTV / Báo Nhân Dân",
    watchUrl: "https://www.youtube.com/watch?v=KDXNK3brzG0",
    embedUrl: "https://www.youtube.com/embed/KDXNK3brzG0",
    duration: "8:45",
    thumb: "assets/images/trending/image1.jpg",
    articleId: "trending-5",
    sourceType: "youtube"
  },
  {
    id: "clip-5",
    category: "Mind & Soul",
    category_en: "Mind & Soul",
    title: "Sân khấu dành cho mọi tiếng nói: Nghệ thuật dung nạp và hòa nhập",
    title_en: "A stage for every voice: Inclusive Theatre and Creative Expression",
    desc: "Đối với các nghệ sĩ khuyết tật, con đường bước lên sân khấu mang lại tiếng nói bình đẳng, nơi những câu chuyện cuộc đời được tỏa sáng bằng nghệ thuật biểu cảm.",
    desc_en: "For artists with disabilities, the path to the stage often involves a different approach to scriptwriting and rehearsals, placing collaborative creative ideas at centre stage.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/a-stage-for-every-voice-100261029064303631.htm",
    embedUrl: "",
    duration: "5:10",
    thumb: "assets/images/mind_&_soul/image6.jpg",
    articleId: "video-5",
    sourceType: "vtv"
  },
  {
    id: "clip-6",
    category: "Mind & Soul",
    category_en: "Mind & Soul",
    title: "10 năm lớp học vĩ cầm miễn phí giữa lòng công viên TP.HCM",
    title_en: "10 years of free violin lessons in park: Harmonizing Community Souls",
    desc: "Lớp học vĩ cầm miễn phí suốt một thập kỷ giữa công viên TP.HCM gieo niềm đam mê âm nhạc cổ điển vào trái tim của hàng trăm bạn trẻ và người dân.",
    desc_en: "The violin is one of the most challenging instruments to master. In Ho Chi Minh City, one community has spent a decade making musical passion accessible for all.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/10-years-of-free-violin-lessons-in-park-100261029064839361.htm",
    embedUrl: "",
    duration: "4:40",
    thumb: "assets/images/mind_&_soul/image7.jpg",
    articleId: "video-6",
    sourceType: "vtv"
  },
  {
    id: "clip-7",
    category: "Society",
    category_en: "Society",
    title: "Văn hóa trà Thái Nguyên thúc đẩy phát triển du lịch bền vững",
    title_en: "Thai Nguyen tea culture boosts tourism and community livelihoods",
    desc: "Lễ hội Trà quốc tế Thái Nguyên 2026 kết nối du khách với những người trồng chè, mở ra cơ hội phát triển du lịch nông nghiệp sinh thái đặc sắc.",
    desc_en: "At Thai Nguyen International Tea Festival 2026, innovative activities bring tourists closer to tea growers and producers, developing distinctive agritourism experiences.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/thai-nguyen-tea-culture-boosts-tourism-100261101042721506.htm",
    embedUrl: "",
    duration: "4:25",
    thumb: "assets/images/society/image34.jpg",
    articleId: "video-7",
    sourceType: "vtv"
  },
  {
    id: "clip-8",
    category: "Human Stories",
    category_en: "Human Stories",
    title: "Người mẹ Hà Nội biến bữa cơm gia đình thành tác phẩm nghệ thuật",
    title_en: "Mother turns meals into art: Creative Culinary Storytelling in Hanoi",
    desc: "Tại Hà Nội, một người mẹ khéo léo biến những nguyên liệu thường ngày thành những bức tranh ẩm thực sinh động, giúp bữa cơm thêm hào hứng và tràn ngập tình yêu thương.",
    desc_en: "For many parents, a home-cooked meal is more than just food. In Hanoi, one mother turns everyday ingredients into colourful works of art, inspiring mindful nutrition.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/mother-turns-meals-into-art-100260710095813651.htm",
    embedUrl: "",
    duration: "3:40",
    thumb: "assets/images/human_stories/image15.jpg",
    articleId: "video-8",
    sourceType: "vtv"
  },
  {
    id: "clip-9",
    category: "Mind & Soul",
    category_en: "Mind & Soul",
    title: "Ốc đảo chữa lành tâm hồn hoàn toàn miễn phí tại TP. Hồ Chí Minh",
    title_en: "A healing oasis in Ho Chi Minh City: Sanctuary for Inner Peace",
    desc: "Không gian chăm sóc sức khỏe tinh thần hoàn toàn miễn phí tại TP.HCM giúp mọi người tìm lại sự an yên và cân bằng sau những áp lực của cuộc sống hiện đại.",
    desc_en: "Mental well-being is an essential component of health. In Ho Chi Minh City, a community-based centre offers a tranquil mental spa completely free of charge.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/a-healing-oasis-in-ho-chi-minh-city-100260910032153068.htm",
    embedUrl: "",
    duration: "5:05",
    thumb: "assets/images/mind_&_soul/image18.png",
    articleId: "video-9",
    sourceType: "vtv"
  },
  {
    id: "clip-10",
    category: "Society",
    category_en: "Society",
    title: "Thiết chế thể thao cộng đồng tại Hà Nội thúc đẩy lối sống năng động",
    title_en: "Community facilities promote healthier lifestyles across Hanoi",
    desc: "Các không gian sinh hoạt, sân chơi thể thao công cộng tại Hà Nội giúp người dân mọi lứa tuổi rèn luyện sức khỏe, thắt chặt tình đoàn kết khối phố mà không tốn kém.",
    desc_en: "Staying active doesn't require expensive gym memberships. Across Hanoi, community running clubs, table tennis, and workout spaces build stronger, healthier neighborhoods.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/community-facilities-promote-healthier-lifestyles-100261019013046705.htm",
    embedUrl: "",
    duration: "4:30",
    thumb: "assets/images/society/image30.jpg",
    articleId: "video-10",
    sourceType: "vtv"
  },
  {
    id: "clip-11",
    category: "Human Stories",
    category_en: "Human Stories",
    title: "Những người mẹ phi thường, tình yêu phi thường thắp sáng niềm tin",
    title_en: "Extraordinary mothers, extraordinary love: Resilience through Adversity",
    desc: "Tôn vinh tình mẫu tử thiêng liêng và nghị lực phi thường của những người mẹ kiên cường vượt qua mọi thử thách, giông bão cuộc đời để nuôi dạy các con khôn lớn.",
    desc_en: "As Mother's Day is celebrated worldwide, people honour the boundless devotion and strength of mothers whose unique journeys require extraordinary resilience.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/extraordinary-mothers-extraordinary-love-10026051107442239.htm",
    embedUrl: "",
    duration: "5:35",
    thumb: "assets/images/human_stories/image20.jpg",
    articleId: "video-11",
    sourceType: "vtv"
  },
  {
    id: "clip-12",
    category: "Society",
    category_en: "Society",
    title: "Người trẻ chung tay chăm sóc và mang hơi ấm tới người cao tuổi neo đơn",
    title_en: "Youth caring for the elderly: Warmth and Solidarity for Solitary Seniors",
    desc: "Mỗi tháng một lần, các bạn trẻ tình nguyện viên lại cùng nhau dọn dẹp nhà cửa, nấu những bữa cơm ấm áp và trao gửi tình thân tới những cụ già neo đơn.",
    desc_en: "Once a month, a dedicated group of young volunteers gather to clean homes, prepare warm nutritious meals, and personally deliver heartfelt companionship to elderly people living alone.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/youth-caring-for-the-elderly-100260226123528559.htm",
    embedUrl: "",
    duration: "4:10",
    thumb: "assets/images/society/image18.png",
    articleId: "video-12",
    sourceType: "vtv"
  }
];

function filterVideoCategory(catKey) {
  currentVideoCategoryFilter = catKey;
  const filtered = (catKey === 'all')
    ? VIDEO_CLIPS
    : VIDEO_CLIPS.filter(c => c.category.toLowerCase() === catKey.toLowerCase());
  if (filtered.length > 0 && !filtered.some(c => c.id === currentActiveClipId)) {
    currentActiveClipId = filtered[0].id;
    isVideoPlaying = false;
  }
  renderVideoHub();
}
window.filterVideoCategory = filterVideoCategory;

function renderVideoHub() {
  const container = document.getElementById('videoHubContent');
  if (!container) return;

  const isEn = (currentLanguage === 'en');
  const mainClip = VIDEO_CLIPS.find(c => c.id === currentActiveClipId) || VIDEO_CLIPS[0];
  const mainTitle = (isEn && mainClip.title_en) ? mainClip.title_en : mainClip.title;
  const mainDesc = (isEn && mainClip.desc_en) ? mainClip.desc_en : mainClip.desc;
  const mainCat = (isEn && mainClip.category_en) ? mainClip.category_en : mainClip.category;

  const isLocalEnv = (
    window.location.protocol === 'file:' || 
    window.location.hostname === 'localhost' || 
    window.location.hostname === '127.0.0.1' || 
    !window.location.hostname
  );
  const isYouTube = (mainClip.sourceType === 'youtube' && mainClip.embedUrl);

  const playBtnText = isEn ? 'Play Video' : 'Phát Video';
  const watchYtText = isEn ? 'Watch on YouTube ↗' : 'Xem trên YouTube ↗';
  const watchVtvText = isEn ? 'Watch on VTV Today ↗' : 'Xem trên VTV Today ↗';
  const readStoryText = isEn ? 'Read Video Story' : 'Đọc Ký Sự Phóng Sự';

  const videoNotice = (isYouTube && isFileProtocol)
    ? (isEn
        ? `<div class="video-local-notice"><i class="fas fa-info-circle"></i> <span>Notice: When opening from local file (file://), YouTube security may block iframe playback. Click <strong>Watch on YouTube ↗</strong> for 100% full HD playback.</span></div>`
        : `<div class="video-local-notice"><i class="fas fa-info-circle"></i> <span>Ghi chú: Khi mở web từ tệp máy tính (file://), nếu YouTube chặn phát nhúng, bạn có thể bấm <strong>Xem trên YouTube ↗</strong> để xem trực tiếp full HD.</span></div>`)
    : '';

  const badgeHtml = isYouTube
    ? `<span class="video-badge-pill"><i class="fab fa-youtube"></i> YOUTUBE DOCUMENTARY</span>`
    : `<span class="video-badge-pill"><i class="fas fa-broadcast-tower"></i> VTV VIETNAM TODAY • MULTIMEDIA</span>`;

  const playerStageHtml = (isYouTube && isVideoPlaying)
    ? (isLocalEnv
        ? `<div class="video-poster-stage" style="cursor:default;">
             <img src="${mainClip.thumb}" alt="${mainTitle}" class="video-poster-img" onerror="handleImageError(this)">
             <div class="video-poster-overlay" style="background:rgba(20, 16, 17, 0.85);"></div>
             <div class="video-play-center" style="max-width:480px; text-align:center; padding:1.5rem;">
               <div style="font-size:2.8rem; color:#FF0000; margin-bottom:0.75rem;"><i class="fab fa-youtube"></i></div>
               <h3 style="font-family:var(--font-editorial); font-size:1.25rem; color:#FFF; margin-bottom:0.5rem;">${mainTitle}</h3>
               <p style="font-size:0.85rem; color:rgba(255,255,255,0.85); line-height:1.5; margin-bottom:1.25rem;">
                 ${isEn 
                   ? 'Opening via local file (file://): YouTube blocks inline embedding to protect origin headers (Error 153). Watch directly in crystal-clear 1080p Full HD on YouTube.' 
                   : 'Do bạn đang mở tệp trực tiếp từ máy tính (file://): YouTube kích hoạt chính sách bảo mật chặn nhúng (Lỗi 153). Mời bạn bấm nút dưới để xem trực tiếp chuẩn Full HD trên YouTube.'}
               </p>
               <div style="display:flex; justify-content:center; gap:0.75rem; flex-wrap:wrap;">
                 <a href="${mainClip.watchUrl}" target="_blank" rel="noopener noreferrer" class="fashion-btn-pill" style="background:#FF0000; color:#FFF; font-weight:700; padding:0.65rem 1.4rem; text-decoration:none; display:inline-flex; align-items:center; gap:0.5rem; border-radius:30px; box-shadow:0 4px 14px rgba(255,0,0,0.4);">
                   <i class="fab fa-youtube"></i> <span>${isEn ? 'Watch on YouTube ↗' : 'Xem ngay trên YouTube ↗'}</span>
                 </a>
                 <button onclick="isVideoPlaying=false; renderVideoHub();" class="fashion-btn-pill" style="background:rgba(255,255,255,0.15); color:#FFF; padding:0.65rem 1.2rem; border:1px solid rgba(255,255,255,0.3); border-radius:30px; cursor:pointer;">
                   ${isEn ? 'Back to Poster' : 'Quay lại bìa'}
                 </button>
               </div>
             </div>
           </div>`
        : `<div class="video-responsive-embed">
             <iframe id="activeVideoFrame" 
               src="${mainClip.embedUrl}?autoplay=1&rel=0&modestbranding=1" 
               title="${mainTitle}" 
               allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
               referrerpolicy="strict-origin-when-cross-origin" 
               allowfullscreen>
             </iframe>
           </div>`)
    : `<div class="video-poster-stage" onclick="${isYouTube ? `playActiveVideo('${mainClip.id}')` : `window.open('${mainClip.watchUrl}', '_blank')`}" title="${isEn ? (isYouTube ? 'Click to Play' : 'Click to Watch on VTV Today') : (isYouTube ? 'Nhấp để phát video' : 'Nhấp để xem trên VTV Today')}">
         <img src="${mainClip.thumb}" alt="${mainTitle}" class="video-poster-img" onerror="handleImageError(this)">
         <div class="video-poster-overlay"></div>
         <div class="video-poster-top">
           ${badgeHtml}
           <span class="video-duration-pill"><i class="far fa-clock"></i> ${mainClip.duration}</span>
         </div>
         <div class="video-play-center">
           <button class="video-play-pulse-btn" aria-label="Play Video">
             <i class="fas ${isYouTube ? 'fa-play' : 'fa-external-link-alt'}"></i>
           </button>
           <span class="video-play-hint">${isYouTube ? playBtnText : watchVtvText}</span>
         </div>
       </div>`;

  const actionToolbarHtml = isYouTube
    ? `
      <div class="video-toolbar-strip">
        <button class="video-tool-btn primary" onclick="playActiveVideo('${mainClip.id}')">
          <i class="fas fa-play"></i> <span>${playBtnText}</span>
        </button>
        <a href="${mainClip.watchUrl}" target="_blank" rel="noopener noreferrer" class="video-tool-btn youtube" title="Xem trên YouTube">
          <i class="fab fa-youtube"></i> <span>${watchYtText}</span>
        </a>
        ${mainClip.articleId ? `
        <button class="video-tool-btn story" onclick="openArticleModal('${mainClip.articleId}')">
          <i class="fas fa-newspaper"></i> <span>${readStoryText}</span>
        </button>` : ''}
      </div>`
    : `
      <div class="video-toolbar-strip">
        <a href="${mainClip.watchUrl}" target="_blank" rel="noopener noreferrer" class="video-tool-btn vtv" title="Xem trên VTV Today">
          <i class="fas fa-tv"></i> <span>${watchVtvText}</span>
        </a>
        ${mainClip.articleId ? `
        <button class="video-tool-btn story" onclick="openArticleModal('${mainClip.articleId}')">
          <i class="fas fa-newspaper"></i> <span>${readStoryText}</span>
        </button>` : ''}
      </div>`;

  // Filter Categories Pills
  const filterCategories = [
    { key: 'all', label: isEn ? 'All (12)' : 'Tất cả (12)' },
    { key: 'society', label: isEn ? 'Society (6)' : 'Xã hội (6)' },
    { key: 'human stories', label: isEn ? 'Human Stories (3)' : 'Human Stories (3)' },
    { key: 'mind & soul', label: isEn ? 'Mind & Soul (3)' : 'Mind & Soul (3)' }
  ];

  const filterBarHtml = `
    <div class="video-filter-bar">
      ${filterCategories.map(cat => {
        const isActive = (currentVideoCategoryFilter.toLowerCase() === cat.key.toLowerCase());
        return `<button class="video-filter-pill ${isActive ? 'active' : ''}" onclick="filterVideoCategory('${cat.key}')">${cat.label}</button>`;
      }).join('')}
    </div>
  `;

  // Filter playlist items
  const filteredPlaylist = (currentVideoCategoryFilter === 'all')
    ? VIDEO_CLIPS
    : VIDEO_CLIPS.filter(c => c.category.toLowerCase() === currentVideoCategoryFilter.toLowerCase());

  container.innerHTML = `
    ${filterBarHtml}
    <div class="video-grid-layout">
      <div class="main-video-player-box">
        <div id="videoPlayerStageWrap">
          ${playerStageHtml}
        </div>
        
        ${actionToolbarHtml}
        ${videoNotice}

        <div class="main-video-details">
          <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:0.5rem;">
            <span class="category-tag" id="activeVideoCategory" style="color:var(--color-brand-primary); font-weight:800; text-transform:uppercase;">${mainCat}</span>
            <span style="font-size:0.8125rem; color:var(--color-text-muted); font-weight:600;"><i class="fas fa-user-edit"></i> ${mainClip.author}</span>
          </div>
          <h2 class="main-video-title" id="activeVideoTitle" style="font-family:var(--font-editorial); font-size:1.5rem; margin-top:0.4rem;">${mainTitle}</h2>
          <p class="main-video-desc" id="activeVideoDesc" style="color:var(--color-text-body); font-size:0.95rem; line-height:1.6; font-weight:500;">${mainDesc}</p>
        </div>
      </div>

      <div class="video-playlist">
        ${filteredPlaylist.map(clip => {
          const title = (isEn && clip.title_en) ? clip.title_en : clip.title;
          const cat = (isEn && clip.category_en) ? clip.category_en : clip.category;
          const isActive = (clip.id === currentActiveClipId);
          const iconClass = clip.sourceType === 'youtube' ? 'fab fa-youtube' : 'fas fa-tv';
          return `
            <div class="playlist-card ${isActive ? 'active' : ''}" onclick="switchVideo('${clip.id}')">
              <div class="playlist-thumb-wrap">
                <img src="${clip.thumb}" alt="${title}" loading="lazy" onerror="handleImageError(this)">
                <div class="playlist-play-icon"><i class="${iconClass}"></i></div>
                <span class="playlist-duration-badge">${clip.duration}</span>
              </div>
              <div class="playlist-info">
                <span class="playlist-cat">${cat}</span>
                <h4 class="playlist-title">${title}</h4>
                <span class="playlist-byline">${clip.author.split('•')[0].trim()}</span>
              </div>
            </div>
          `;
        }).join('')}
      </div>
    </div>
  `;
}

function playActiveVideo(clipId) {
  if (clipId) currentActiveClipId = clipId;
  const clip = VIDEO_CLIPS.find(c => c.id === currentActiveClipId) || VIDEO_CLIPS[0];
  const isLocalEnv = (
    window.location.protocol === 'file:' || 
    window.location.hostname === 'localhost' || 
    window.location.hostname === '127.0.0.1' || 
    !window.location.hostname
  );

  if (clip.sourceType === 'youtube') {
    if (isLocalEnv) {
      window.open(clip.watchUrl, '_blank');
      if (typeof showToast === 'function') {
        showToast(currentLanguage === 'en' 
          ? 'Opening documentary in Full HD on YouTube' 
          : 'Đang mở phóng sự chuẩn Full HD 1080p trên YouTube', 'info');
      }
      isVideoPlaying = true;
      renderVideoHub();
      return;
    }
  }
  
  if (clip.sourceType === 'vtv') {
    window.open(clip.watchUrl, '_blank');
    return;
  }

  isVideoPlaying = true;
  renderVideoHub();
}
window.playActiveVideo = playActiveVideo;

function switchVideo(clipId) {
  currentActiveClipId = clipId;
  isVideoPlaying = false;
  renderVideoHub();
}
window.switchVideo = switchVideo;

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

  const isEn = (currentLanguage === 'en');

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 4rem 1rem; color: var(--color-text-muted);">
        <i class="fas fa-feather" style="font-size: 2.5rem; color: var(--color-brand-accent); margin-bottom: 1rem;"></i>
        <h3 style="font-family: var(--font-editorial); font-size: 1.5rem; color: var(--color-text-headline);">${isEn ? 'No articles found in this category' : 'Chưa có bài viết trong chuyên mục này'}</h3>
        <p style="font-size: 0.9rem; margin-top: 0.5rem;">${isEn ? 'Please choose another category or return to view all stories.' : 'Mời bạn chọn chuyên mục khác hoặc quay lại xem tất cả bài viết.'}</p>
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map(item => {
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
function filterByCategory(categoryKey) {
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
}
window.filterByCategory = filterByCategory;

/* ===================================================================
   ABOUT US SECTION (ULIS - VNU Editorial Manifesto & Authentic Profiles)
   =================================================================== */
function renderAboutUsSection() {
  const container = document.getElementById('aboutUsSection');
  if (!container) return;

  const isEn = (currentLanguage === 'en');

  container.innerHTML = `
    <!-- Sticky Secondary Navigation for About Us -->
    <nav class="about-tabs-nav" aria-label="About Us Navigation">
      <a href="#profiles" class="about-tab-btn"><i class="fas fa-users"></i> <span data-i18n="about_tab_profiles">${isEn ? 'Editorial Profiles' : 'Hồ Sơ Ban Biên Tập'}</span></a>
      <a href="#photo" class="about-tab-btn"><i class="fas fa-camera"></i> <span data-i18n="about_tab_photo">${isEn ? 'Photojournalism Gallery' : 'Kho Ảnh Phóng Sự Báo Chí'}</span></a>
      <a href="#subscribe" class="about-tab-btn"><i class="fas fa-paper-plane"></i> <span data-i18n="about_tab_subscribe">${isEn ? 'Newsletter Subscription' : 'Đăng Ký Nhận Bản Tin'}</span></a>
      <a href="#mission" class="about-tab-btn"><i class="fas fa-bullseye"></i> <span data-i18n="about_tab_mission">${isEn ? 'Mission, Ethics & Compliance' : 'Tôn Chỉ Hoạt Động & Chuẩn Mực'}</span></a>
    </nav>

    <!-- SECTION 1: PROFILES (#profiles) -->
    <section id="profiles" style="margin-bottom: 3.5rem; scroll-margin-top: 100px;">
      <div class="nhandan-section-header">
        <div class="nhandan-sec-title-wrap">
          <span class="nhandan-sec-ribbon"></span>
          <h2 class="nhandan-sec-title" data-i18n="profiles_sec_title">${isEn ? 'EDITORIAL BOARD & NEWSROOM ROSTER' : 'BAN BIÊN TẬP & NHÂN SỰ TÒA SOẠN'}</h2>
          <span class="nhandan-sec-sub" data-i18n="profiles_sec_sub">${isEn ? 'Class 6 - Group 1 - Term 127 • Faculty of Language & Communication, ULIS - VNU' : 'Lớp 6 - Nhóm 1 - Khóa 127 • Khoa Ngôn ngữ & Truyền thông, Trường ĐH Ngoại ngữ - ĐHQGHN'}</span>
        </div>
      </div>

      <div class="profiles-grid">
        <!-- 1. Nguyễn Thị Ngọc Mai (Editor-in-Chief) -->
        <article class="profile-card">
          <div>
            <div class="profile-header-wrap">
              <div class="profile-avatar-wrap">
                <img src="assets/images/profiles/ngoc_mai.jpg" alt="Nguyễn Thị Ngọc Mai" class="profile-avatar-img" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                <div class="profile-avatar-circle" style="display:none;">NM</div>
              </div>
              <div>
                <h3 class="profile-name-text">1. Nguyễn Thị Ngọc Mai</h3>
                <span class="profile-title-pill" data-i18n="profile_mai_title">${isEn ? 'Editor-in-Chief' : 'Tổng Biên Tập'}</span>
              </div>
            </div>
            <p class="profile-role-desc" data-i18n="profile_mai_role">
              ${isEn ? 'Sets the overall editorial direction, ensures adherence to journalistic standards, and oversees all published content across the platform.' : 'Định hướng chiến lược nội dung tổng thể của tòa soạn, đảm bảo tính chuẩn mực của đạo đức báo chí và kiểm duyệt toàn diện các ấn phẩm xuất bản trên nền tảng.'}
            </p>
          </div>
          <div>
            <a href="mailto:nguyenthiingocmaii07@email.com" class="profile-email-link" title="Gửi thư đến Tổng Biên Tập">
              <i class="fas fa-envelope"></i> <span>nguyenthiingocmaii07@email.com</span>
            </a>
          </div>
        </article>

        <!-- 2. Lê Hà Anh (Managing Editor) -->
        <article class="profile-card">
          <div>
            <div class="profile-header-wrap">
              <div class="profile-avatar-wrap">
                <img src="assets/images/profiles/ha_anh.jpg" alt="Lê Hà Anh" class="profile-avatar-img" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                <div class="profile-avatar-circle" style="display:none;">HA</div>
              </div>
              <div>
                <h3 class="profile-name-text">2. Lê Hà Anh</h3>
                <span class="profile-title-pill" data-i18n="profile_haanh_title">${isEn ? 'Managing Editor' : 'Thư Ký Tòa Soạn'}</span>
              </div>
            </div>
            <p class="profile-role-desc" data-i18n="profile_haanh_role">
              ${isEn ? 'Coordinates daily newsroom operations, manages the editorial calendar, and oversees the production workflow.' : 'Điều phối hoạt động tác nghiệp hàng ngày của tòa soạn, quản trị lịch xuất bản định kỳ và giám sát chặt chẽ quy trình sản xuất nội dung đa phương tiện.'}
            </p>
          </div>
          <div>
            <a href="mailto:bong177007@gmail.com" class="profile-email-link" title="Gửi thư đến Thư Ký Tòa Soạn">
              <i class="fas fa-envelope"></i> <span>bong177007@gmail.com</span>
            </a>
          </div>
        </article>

        <!-- 3. Bùi Phương Anh (Senior Content Editor) -->
        <article class="profile-card">
          <div>
            <div class="profile-header-wrap">
              <div class="profile-avatar-wrap">
                <img src="assets/images/profiles/phuong_anh.jpg" alt="Bùi Phương Anh" class="profile-avatar-img" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                <div class="profile-avatar-circle" style="display:none;">PA</div>
              </div>
              <div>
                <h3 class="profile-name-text">3. Bùi Phương Anh</h3>
                <span class="profile-title-pill" data-i18n="profile_phuonganh_title">${isEn ? 'Senior Content Editor' : 'Biên Tập Viên Nội Dung'}</span>
              </div>
            </div>
            <p class="profile-role-desc" data-i18n="profile_phuonganh_role">
              ${isEn ? 'Spearheads topic research, fact-checks stories, and refines written content to ensure high clarity and analytical depth.' : 'Chủ trì nghiên cứu chuyên đề, kiểm chứng sự thật đa nguồn và trau chuốt câu từ để đảm bảo độ trong sáng, sắc sảo cùng chiều sâu phân tích.'}
            </p>
          </div>
          <div>
            <a href="mailto:hamyt4141@gmail.com" class="profile-email-link" title="Gửi thư đến Biên Tập Viên Nội Dung">
              <i class="fas fa-envelope"></i> <span>hamyt4141@gmail.com</span>
            </a>
          </div>
        </article>

        <!-- 4. Bùi Bảo Ngân (Multimedia Editor) -->
        <article class="profile-card">
          <div>
            <div class="profile-header-wrap">
              <div class="profile-avatar-wrap">
                <img src="assets/images/profiles/bao_ngan.jpg" alt="Bùi Bảo Ngân" class="profile-avatar-img" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                <div class="profile-avatar-circle" style="display:none;">BN</div>
              </div>
              <div>
                <h3 class="profile-name-text">4. Bùi Bảo Ngân</h3>
                <span class="profile-title-pill" data-i18n="profile_ngan_title">${isEn ? 'Multimedia Editor' : 'Biên Tập Viên Đa Phương Tiện'}</span>
              </div>
            </div>
            <p class="profile-role-desc" data-i18n="profile_ngan_role">
              ${isEn ? 'Leads visual storytelling by designing graphics, infographics, and curation of photojournalism assets.' : 'Chỉ đạo nghệ thuật báo chí thị giác, thiết kế đồ họa tương tác, infographic và tuyển chọn các tác phẩm báo ảnh phóng sự giàu cảm xúc.'}
            </p>
          </div>
          <div>
            <a href="mailto:buibaongan90307@gmail.com" class="profile-email-link" title="Gửi thư đến Biên Tập Viên Đa Phương Tiện">
              <i class="fas fa-envelope"></i> <span>buibaongan90307@gmail.com</span>
            </a>
          </div>
        </article>

        <!-- 5. Nguyễn Như Quỳnh (Digital & Publishing Lead) -->
        <article class="profile-card">
          <div>
            <div class="profile-header-wrap">
              <div class="profile-avatar-wrap">
                <img src="assets/images/profiles/nhu_quynh.jpg" alt="Nguyễn Như Quỳnh" class="profile-avatar-img" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                <div class="profile-avatar-circle" style="display:none;">NQ</div>
              </div>
              <div>
                <h3 class="profile-name-text">5. Nguyễn Như Quỳnh</h3>
                <span class="profile-title-pill" data-i18n="profile_quynh_title">${isEn ? 'Digital & Publishing Lead' : 'Trưởng Ban Kỹ Thuật Số'}</span>
              </div>
            </div>
            <p class="profile-role-desc" data-i18n="profile_quynh_role">
              ${isEn ? 'Manages web development, optimizes digital reader experience (UX/SEO), and handles content distribution.' : 'Quản trị hệ thống web báo điện tử, tối ưu hóa trải nghiệm đọc đa thiết bị (UX/SEO) và tổ chức phát hành nội dung trên các kênh số.'}
            </p>
          </div>
          <div>
            <a href="mailto:nhuquynh.saddy0507@gmail.com" class="profile-email-link" title="Gửi thư đến Ban Kỹ Thuật Số">
              <i class="fas fa-envelope"></i> <span>nhuquynh.saddy0507@gmail.com</span>
            </a>
          </div>
        </article>
      </div>
    </section>

    <!-- SECTION 2: PHOTOJOURNALISM MOSAIC (#photo) -->
    <section id="photo" style="margin-bottom: 3.5rem; scroll-margin-top: 100px;">
      <div class="nhandan-section-header">
        <div class="nhandan-sec-title-wrap">
          <span class="nhandan-sec-ribbon"></span>
          <h2 class="nhandan-sec-title">${isEn ? 'DOCUMENTARY PHOTOJOURNALISM GALLERY' : 'KHO ẢNH PHÓNG SỰ BÁO CHÍ ĐẶC SẮC'}</h2>
          <span class="nhandan-sec-sub">${isEn ? 'Authentic documentary moments capturing human empathy and resilience' : 'Những khoảnh khắc phóng sự chân thực ghi dấu lòng trắc ẩn và nghị lực cuộc sống'}</span>
        </div>
      </div>

      <div class="about-photo-mosaic-grid">
        <div class="about-photo-item" onclick="openArticleModal('trending-4')">
          <img src="assets/images/trending/image8.jpg" alt="Phố cổ Hội An" class="about-photo-img" onerror="handleImageError(this)">
          <div class="about-photo-caption">
            <h4>${isEn ? 'Street Vendors in Hoi An' : 'Gánh mưu sinh phố cổ Hội An'}</h4>
            <p>${isEn ? 'VnExpress Photojournalism • Article 4 Trending' : 'Phóng sự VnExpress • Bài 4 Trending'}</p>
          </div>
        </div>

        <div class="about-photo-item" onclick="openArticleModal('human-4')">
          <img src="assets/images/human_stories/image7.png" alt="Cánh đồng nghĩa tình Texas" class="about-photo-img" onerror="handleImageError(this)">
          <div class="about-photo-caption">
            <h4>${isEn ? 'Texas Volunteer Community Harvest' : 'Cánh đồng nghĩa tình Gruver, Texas'}</h4>
            <p>${isEn ? 'The Washington Post • Article 4 Human Stories' : 'The Washington Post • Bài 4 Human Stories'}</p>
          </div>
        </div>

        <div class="about-photo-item" onclick="openArticleModal('human-3')">
          <img src="assets/images/human_stories/image3.png" alt="Qusay Hussein" class="about-photo-img" onerror="handleImageError(this)">
          <div class="about-photo-caption">
            <h4>${isEn ? 'Qusay Hussein: Second Chance at Life' : 'Qusay Hussein: Cơ hội thứ hai để sống'}</h4>
            <p>${isEn ? 'The Guardian • Article 3 Human Stories' : 'The Guardian • Bài 3 Human Stories'}</p>
          </div>
        </div>

        <div class="about-photo-item" onclick="openArticleModal('mind-1')">
          <img src="assets/images/mind_&_soul/image2.jpg" alt="Taeyang Mỹ Đình" class="about-photo-img" onerror="handleImageError(this)">
          <div class="about-photo-caption">
            <h4>${isEn ? 'Taeyang (BigBang) Concert at My Dinh' : 'Taeyang (BigBang) tại SVĐ Mỹ Đình'}</h4>
            <p>${isEn ? 'Lao Dong Newspaper • Article 1 Mind & Soul' : 'Báo Lao Động • Bài 1 Mind & Soul'}</p>
          </div>
        </div>

        <div class="about-photo-item" onclick="openArticleModal('society-1')">
          <img src="assets/images/society/image3.jpg" alt="Vale Pantry" class="about-photo-img" onerror="handleImageError(this)">
          <div class="about-photo-caption">
            <h4>${isEn ? 'Vale Pantry: Dignified Community Food Initiative' : 'Vale Pantry: Mô hình bảo toàn phẩm giá'}</h4>
            <p>${isEn ? 'The Guardian • Article 1 Society' : 'The Guardian • Bài 1 Society'}</p>
          </div>
        </div>

        <div class="about-photo-item" onclick="openArticleModal('trending-5')">
          <img src="assets/images/human_stories/image17.jpg" alt="Hài cốt liệt sĩ" class="about-photo-img" onerror="handleImageError(this)">
          <div class="about-photo-caption">
            <h4>${isEn ? '500-Day-and-Night Campaign: Martyrs DNA Testing' : 'Chiến dịch 500 ngày đêm ADN liệt sĩ'}</h4>
            <p>${isEn ? 'Nhan Dan Newspaper • Article 5 Trending' : 'Báo Nhân Dân • Bài 5 Trending'}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: NEWSLETTER SUBSCRIPTION (#subscribe) -->
    <section id="subscribe" style="margin-bottom: 3.5rem; scroll-margin-top: 100px;">
      <div class="about-subscribe-card">
        <i class="fas fa-paper-plane" style="font-size:2.5rem; color:var(--color-brand-primary); margin-bottom:1rem;"></i>
        <h2 style="font-family:var(--font-editorial); font-size:1.85rem; color:var(--color-brand-primary); margin-bottom:0.5rem;" data-i18n="about_sub_title">${isEn ? 'Subscribe to HEARTICLES. Sunday Edition' : 'Đăng Ký Nhận Ấn Phẩm Chủ Nhật HEARTICLES.'}</h2>
        <p style="font-size:0.95rem; color:var(--color-text-body); max-width:540px; margin:0 auto 1.5rem auto; line-height:1.6;" data-i18n="about_sub_desc">
          ${isEn ? 'Receive curated humanistic long-form stories, ethical journalism insights, and cultural essays directly to your inbox every Sunday morning.' : 'Tuyển tập những bài ký sự nhân văn sâu sắc, chuyên đề đối ngoại và phân tích xã hội chạm đến trái tim được gửi trực tiếp đến hộp thư của bạn vào mỗi sáng Chủ nhật.'}
        </p>
        <form onsubmit="event.preventDefault(); showToast(currentLanguage === 'en' ? 'Thank you for subscribing!' : 'Cảm ơn bạn đã đăng ký nhận bản tin!', 'check');" style="display:flex; max-width:480px; margin:0 auto; gap:0.5rem;">
          <input type="email" required placeholder="your.email@example.com" style="flex:1; padding:0.75rem 1.25rem; border:1px solid var(--color-border-hairline); border-radius:var(--radius-full); font-size:0.9rem; outline:none;">
          <button type="submit" class="fashion-btn-pill" style="white-space:nowrap; padding:0.75rem 1.75rem;" data-i18n="btn_subscribe">${isEn ? 'Subscribe' : 'Đăng Ký'}</button>
        </form>
      </div>
    </section>

    <!-- SECTION 4: MISSION & COMPLIANCE (#mission) -->
    <section id="mission" style="margin-bottom: 2rem; scroll-margin-top: 100px;">
      <div class="nhandan-section-header">
        <div class="nhandan-sec-title-wrap">
          <span class="nhandan-sec-ribbon"></span>
          <h2 class="nhandan-sec-title" data-i18n="about_mission_title">${isEn ? 'MISSION, JOURNALISTIC ETHICS & COMPLIANCE' : 'TÔN CHỈ HOẠT ĐỘNG, ĐẠO ĐỨC & CHUẨN MỰC BÁO CHÍ'}</h2>
        </div>
      </div>
      <div style="background:#FFFFFF; border:1px solid var(--color-border-hairline); border-radius:var(--radius-lg); padding:2rem; line-height:1.75; color:var(--color-text-body);">
        <p style="margin-bottom:1rem;">
          <strong>HEARTICLES.</strong> ${isEn ? 'is an academic multimedia journalism publication developed by Class 6 - Group 1 - Term 127 under the Faculty of Language & Communication, University of Languages and International Studies, Vietnam National University (ULIS - VNU).' : 'là ấn phẩm báo chí điện tử đa phương tiện học thuật được nghiên cứu và phát triển bởi tập thể sinh viên Lớp 6 - Nhóm 1 - Khóa 127, Khoa Ngôn ngữ & Truyền thông, Trường Đại học Ngoại ngữ - Đại học Quốc gia Hà Nội (ULIS - VNU).'}
        </p>
        <p style="margin-bottom:1rem;">
          ${isEn ? 'Our editorial philosophy is anchored in the belief that modern journalism must uphold humanistic values, strict multi-source verification, and empathetic storytelling that uplifts vulnerable communities.' : 'Tôn chỉ hoạt động của chúng tôi kiên định với sứ mệnh: báo chí hiện đại phải đặt lòng nhân ái và tính trung thực lên hàng đầu, kiểm chứng nguồn tin đa chiều nghiêm ngặt và lan tỏa những câu chuyện lay động trái tim hướng tới cộng đồng.'}
        </p>
        <p style="margin:0; font-size:0.875rem; color:var(--color-text-muted);">
          <i class="fas fa-shield-alt" style="color:var(--color-brand-primary); margin-right:0.35rem;"></i>
          ${isEn ? 'Strict compliance with the Press Law of the Socialist Republic of Vietnam, ULIS - VNU Academic Research Regulations, and Nielsen Norman Group UX Accessibility Guidelines.' : 'Tuân thủ nghiêm ngặt Luật Báo chí nước Cộng hòa Xã hội Chủ nghĩa Việt Nam, Quy chế Nghiên cứu Khoa học Sinh viên ĐHQGHN và tiêu chuẩn công nghệ khả năng tiếp cận Nielsen Norman UX.'}
        </p>
      </div>
    </section>
  `;
}

/* ===================================================================
   ARTICLE DETAIL MODAL & READING SUITE (Bilingual, TTS, Zoom, Like)
   =================================================================== */
function formatArticleSource(article, isEn) {
  if (!article) return '';

  const rawTitle = isEn 
    ? (article.title_en || article.title || '') 
    : (article.title || article.title_en || '');
  const cleanTitle = rawTitle.replace(/^["'“”‘’]|["'“”‘’]$/g, '').trim();

  // Clean author name
  let author = (article.author || '').split('•')[0].trim();
  if (author.endsWith(' & NDO')) author = author.replace(' & NDO', '');
  if (!author) author = isEn ? 'Editorial Staff' : 'Ban biên tập';

  const sourceName = article.sourceName || (isEn ? 'HEARTICLES. Editorial' : 'Tòa soạn HEARTICLES.');

  // Date formatting
  let rawDate = (article.date || '').split(' - ')[0].trim();
  rawDate = rawDate.replace(/^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),\s*/i, '');

  const monthsMap = {
    'January': 'tháng 1', 'February': 'tháng 2', 'March': 'tháng 3',
    'April': 'tháng 4', 'May': 'tháng 5', 'June': 'tháng 6',
    'July': 'tháng 7', 'August': 'tháng 8', 'September': 'tháng 9',
    'October': 'tháng 10', 'November': 'tháng 11', 'December': 'tháng 12'
  };

  let formattedDate = rawDate;
  if (!isEn) {
    const match = rawDate.match(/([A-Za-z]+)\s+(\d{1,2}),?\s+(\d{4})/);
    if (match) {
      const monthVi = monthsMap[match[1]] || match[1];
      formattedDate = `ngày ${match[2]} ${monthVi} năm ${match[3]}`;
    }
  }

  const url = article.sourceUrl || '#';

  if (isEn) {
    return `
      <div class="article-source-citation">
        <span class="citation-label">Source:</span> "<em class="citation-title">${cleanTitle}</em>", ${sourceName}, by ${author}, ${formattedDate}, 
        <a href="${url}" target="_blank" rel="noopener noreferrer" class="citation-url">${url}</a>
      </div>
    `;
  } else {
    return `
      <div class="article-source-citation">
        <span class="citation-label">Source:</span> "<em class="citation-title">${cleanTitle}</em>", ${sourceName}, viết bởi ${author}, ${formattedDate}, 
        <a href="${url}" target="_blank" rel="noopener noreferrer" class="citation-url">${url}</a>
      </div>
    `;
  }
}
window.formatArticleSource = formatArticleSource;

function openArticleModal(articleId) {
  const article = ARTICLES_DATA.find(a => a.id === articleId);
  if (!article) return;

  const modal = document.getElementById('articleReaderModal');
  const body = document.getElementById('articleModalBody');
  if (!modal || !body) return;

  modal.dataset.articleId = articleId;

  const isEn = (currentLanguage === 'en');
  const title = (isEn && article.title_en) ? article.title_en : article.title;
  const subtitle = (isEn && article.subtitle_en) ? article.subtitle_en : article.subtitle;
  const readTime = isEn ? (article.readTime || '').replace('phút đọc', 'min read') : article.readTime;
  const breadcrumbHome = isEn ? 'Home' : 'Trang chủ';
  const breadcrumbDetail = isEn ? 'Article Detail' : 'Chi tiết bài viết';

  const savedComments = JSON.parse(localStorage.getItem(`comments_${article.id}`) || '[]');
  const isLiked = localStorage.getItem(`liked_${article.id}`) === 'true';

  let bodyHtml = '';
  if (typeof article.content === 'string') {
    bodyHtml = article.content;
  } else if (Array.isArray(article.content)) {
    bodyHtml = article.content.map(p => {
      if (p.startsWith('### ')) {
        return `<h3 style="font-family:var(--font-editorial); font-size:1.35rem; font-weight:800; color:var(--color-brand-primary); margin:1.5rem 0 0.75rem 0;">${p.replace('### ', '')}</h3>`;
      }
      return `<p style="margin-bottom:1.15rem; line-height:1.8;">${p}</p>`;
    }).join('');
  }

  body.innerHTML = `
    <div class="article-reading-content" style="font-size: ${currentFontSize}rem;">
      <div class="article-breadcrumb" style="display:flex; align-items:center; gap:0.5rem; font-size:0.8125rem; color:var(--color-text-muted); margin-bottom:1rem;">
        <a href="javascript:void(0)" onclick="closeArticleModal()" style="color:var(--color-brand-primary); font-weight:600;">${breadcrumbHome}</a>
        <span>/</span>
        <a href="javascript:void(0)" onclick="filterByCategory('${article.category}')" style="color:var(--color-brand-primary); font-weight:600;">${article.categoryName}</a>
        <span>/</span>
        <span>${breadcrumbDetail}</span>
      </div>

      <h1 class="article-headline" style="font-family:var(--font-editorial); font-size:2.2rem; font-weight:800; line-height:1.25; margin-bottom:0.75rem; color:var(--color-text-headline);">${title}</h1>
      <p class="article-sapo" style="font-family:var(--font-serif); font-size:1.15rem; line-height:1.6; color:var(--color-text-muted); margin-bottom:1.5rem;">${subtitle}</p>

      <div class="article-author-strip" style="display:flex; justify-content:space-between; align-items:center; padding-bottom:1rem; border-bottom:1px solid var(--color-border-hairline); margin-bottom:1.5rem; flex-wrap:wrap; gap:1rem;">
        <div class="article-author-info" style="display:flex; align-items:center; gap:0.75rem;">
          <div class="author-avatar-small" style="width:42px; height:42px; border-radius:50%; background:var(--color-brand-primary); color:#FFF; display:flex; align-items:center; justify-content:center; font-weight:bold;">${article.author.charAt(0)}</div>
          <div>
            <div class="author-name-text" style="font-weight:700; color:var(--color-text-headline);">${article.author}</div>
            <div class="article-date-text" style="font-size:0.75rem; color:var(--color-text-muted);"><i class="far fa-clock"></i> ${article.date}</div>
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
          <button class="tool-btn" onclick="shareArticle('${title.replace(/'/g, "\\'")}')" title="${isEn ? 'Share' : 'Chia sẻ'}"><i class="fas fa-share-alt"></i> <span>${isEn ? 'Share' : 'Chia sẻ'}</span></button>
        </div>
      </div>

      <div class="article-hero-media" style="border-radius:var(--radius-lg); overflow:hidden; margin:1.5rem 0;">
        <img src="${article.image}" alt="${title}" style="width:100%; display:block; max-height:540px; object-fit:cover;" onerror="handleImageError(this)">
        <div class="article-media-caption" style="font-size:0.8125rem; color:var(--color-text-muted); padding:0.5rem 0.25rem; font-style:italic;">${article.imageCaption || title}</div>
      </div>

      ${article.video ? `
        <div class="video-responsive-embed" style="margin-bottom: 2rem; border-radius: 12px; overflow:hidden;">
          <iframe src="${article.video}" title="Video phóng sự kèm bài viết" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        </div>
      ` : ''}

      <div class="article-body-text" id="articleBodyContent" style="font-family:var(--font-body); font-size:1.125rem; line-height:1.8; color:var(--color-text-body);">
        ${bodyHtml}
        ${formatArticleSource(article, isEn)}
      </div>

      <!-- Comments Block -->
      <div class="article-comments-block" style="margin-top:3rem;">
        <h3 style="font-family:var(--font-editorial); font-size:1.4rem; color:var(--color-text-headline); margin-bottom:1.25rem;">
          <i class="far fa-comments" style="color:var(--color-brand-primary);"></i> ${isEn ? 'Reader Discussion' : 'Bình luận & Thảo luận'} (<span id="commentCount">${savedComments.length}</span>)
        </h3>
        
        <div class="comment-form-wrap" style="display:flex; gap:0.75rem; margin-bottom:1.5rem;">
          <input type="text" class="comment-input-field" id="newCommentInput" placeholder="${isEn ? 'Share your humanistic reflection on this story...' : 'Chia sẻ góc nhìn nhân văn của bạn về bài viết này...'}" onkeypress="if(event.key === 'Enter') submitComment('${article.id}')" style="flex-grow:1; padding:0.75rem 1rem; border:1px solid var(--color-border-hairline); border-radius:var(--radius-full); font-size:0.9rem; outline:none;">
          <button class="comment-submit-btn fashion-btn-pill" onclick="submitComment('${article.id}')" style="padding:0.75rem 1.5rem;">${isEn ? 'Submit' : 'Gửi'}</button>
        </div>

        <div class="comments-list-container" id="commentsListContainer">
          ${savedComments.length === 0 ? `<p style="color:var(--color-text-muted); font-size:0.875rem; font-style:italic;">${isEn ? 'Be the first to share your heartfelt thoughts on this story.' : 'Hãy là người đầu tiên chia sẻ cảm nghĩ về bài viết này.'}</p>` : ''}
          ${savedComments.map(c => `
            <div class="comment-item-card" style="background:#FFFFFF; border:1px solid var(--color-border-hairline); border-radius:var(--radius-md); padding:0.85rem 1rem; margin-bottom:0.75rem;">
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
}
window.openArticleModal = openArticleModal;

function closeArticleModal() {
  const modal = document.getElementById('articleReaderModal');
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }
  if (isSpeaking) {
    stopTextToSpeech();
  }
}
window.closeArticleModal = closeArticleModal;

/* ===================================================================
   COMMENT & LIKE SYSTEM
   =================================================================== */
function submitComment(articleId) {
  const input = document.getElementById('newCommentInput');
  if (!input || !input.value.trim()) return;

  const key = `comments_${articleId}`;
  const existing = JSON.parse(localStorage.getItem(key) || '[]');
  const now = new Date();
  const timeStr = `${now.getHours()}:${String(now.getMinutes()).padStart(2, '0')} - ${now.getDate()}/${now.getMonth() + 1}`;

  existing.unshift({
    author: (currentLanguage === 'en') ? 'ULIS - VNU Reader' : 'Độc giả ULIS - VNU',
    time: timeStr,
    text: input.value.trim()
  });

  localStorage.setItem(key, JSON.stringify(existing));
  input.value = '';
  openArticleModal(articleId);
  showToast(currentLanguage === 'en' ? 'Your reflection has been posted!' : 'Bình luận của bạn đã được xuất bản!', 'check');
}
window.submitComment = submitComment;

function toggleLikeArticle(articleId) {
  const isLiked = localStorage.getItem(`liked_${articleId}`) === 'true';
  const article = ARTICLES_DATA.find(a => a.id === articleId);
  const btn = document.getElementById(`likeBtn_${articleId}`);
  const countEl = document.getElementById(`likeCount_${articleId}`);

  if (isLiked) {
    localStorage.removeItem(`liked_${articleId}`);
    if (btn) btn.classList.remove('liked');
    if (countEl && article) countEl.textContent = article.likes;
    showToast(currentLanguage === 'en' ? 'Removed bookmark' : 'Đã bỏ yêu thích bài viết', 'heart-broken');
  } else {
    localStorage.setItem(`liked_${articleId}`, 'true');
    if (btn) {
      btn.classList.add('liked');
      triggerHeartBurst(btn);
    }
    if (countEl && article) countEl.textContent = article.likes + 1;
    showToast(currentLanguage === 'en' ? 'Heart sent to this story!' : 'Đã thả tim bài viết! Cảm ơn bạn.', 'heart');
  }
}
window.toggleLikeArticle = toggleLikeArticle;

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
function toggleTextToSpeech(articleId) {
  if (isSpeaking) {
    stopTextToSpeech();
  } else {
    startTextToSpeech(articleId);
  }
}
window.toggleTextToSpeech = toggleTextToSpeech;

function startTextToSpeech(articleId) {
  const article = ARTICLES_DATA.find(a => a.id === articleId);
  if (!article || !('speechSynthesis' in window)) {
    alert(currentLanguage === 'en' ? 'Web Speech API is not supported in this browser.' : 'Trình duyệt của bạn chưa hỗ trợ tính năng Web Speech API.');
    return;
  }

  window.speechSynthesis.cancel();

  const isEn = (currentLanguage === 'en');
  const title = (isEn && article.title_en) ? article.title_en : article.title;
  const subtitle = (isEn && article.subtitle_en) ? article.subtitle_en : article.subtitle;

  let plainText = '';
  if (typeof article.content === 'string') {
    plainText = article.content.replace(/<[^>]*>/g, ' ');
  } else if (Array.isArray(article.content)) {
    plainText = article.content.join(' ');
  }

  const textToRead = `${title}. ${subtitle}. ${plainText}`;
  speechUtterance = new SpeechSynthesisUtterance(textToRead);
  speechUtterance.lang = isEn ? 'en-US' : 'vi-VN';
  speechUtterance.rate = 0.95;

  speechUtterance.onstart = () => {
    isSpeaking = true;
    updateTTSButton(true);
    showToast(isEn ? 'Playing audio article...' : 'Đang phát giọng đọc bài báo...', 'volume-up');
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
    const isEn = (currentLanguage === 'en');
    btn.innerHTML = `<i class="fas ${speaking ? 'fa-pause' : 'fa-volume-up'}"></i> <span>${speaking ? (isEn ? 'Pause' : 'Tạm dừng') : (isEn ? 'Listen' : 'Đọc bài báo')}</span>`;
    btn.classList.toggle('active', speaking);
  }
}

function adjustFontSize(delta) {
  currentFontSize = Math.min(Math.max(currentFontSize + delta, 0.95), 1.45);
  const content = document.querySelector('.article-reading-content');
  if (content) {
    content.style.fontSize = `${currentFontSize}rem`;
  }
}
window.adjustFontSize = adjustFontSize;

function shareArticle(title) {
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
}
window.shareArticle = shareArticle;

/* ===================================================================
   SEARCH ENGINE (Instant Live Search)
   =================================================================== */
function openSearchModal() {
  const modal = document.getElementById('searchModal');
  const input = document.getElementById('searchInput');
  if (modal) {
    modal.classList.add('active');
    setTimeout(() => { if (input) input.focus(); }, 100);
  }
}
window.openSearchModal = openSearchModal;

function closeSearchModal() {
  const modal = document.getElementById('searchModal');
  if (modal) modal.classList.remove('active');
}
window.closeSearchModal = closeSearchModal;

function handleSearchInput(query) {
  const resultsBox = document.getElementById('searchResults');
  if (!resultsBox) return;

  const isEn = (currentLanguage === 'en');
  const trimmed = query.trim().toLowerCase();
  if (!trimmed) {
    resultsBox.innerHTML = `
      <div style="padding:1rem 0;">
        <p style="color:var(--color-text-muted); font-size:0.875rem; margin-bottom:0.75rem;">${isEn ? 'Trending suggestion tags:' : 'Từ khóa thịnh hành gợi ý:'}</p>
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem;">
          <button class="search-tag-chip" onclick="applySearchTag('Hội An')">#Hội An</button>
          <button class="search-tag-chip" onclick="applySearchTag('Taeyang')">#Taeyang</button>
          <button class="search-tag-chip" onclick="applySearchTag('Trending')">#Trending</button>
          <button class="search-tag-chip" onclick="applySearchTag('Lawmakers')">#Lawmakers</button>
          <button class="search-tag-chip" onclick="applySearchTag('ULIS')">#ULIS - VNU</button>
        </div>
      </div>
    `;
    return;
  }

  const matches = ARTICLES_DATA.filter(a => {
    const title = (a.title || '') + ' ' + (a.title_en || '');
    const subtitle = (a.subtitle || '') + ' ' + (a.subtitle_en || '');
    return title.toLowerCase().includes(trimmed) ||
           subtitle.toLowerCase().includes(trimmed) ||
           a.author.toLowerCase().includes(trimmed) ||
           a.categoryName.toLowerCase().includes(trimmed) ||
           (a.tags && a.tags.some(t => t.toLowerCase().includes(trimmed)));
  });

  if (matches.length === 0) {
    resultsBox.innerHTML = `
      <div style="text-align:center; padding:2rem 0; color:var(--color-text-muted);">
        <i class="fas fa-search" style="font-size:2rem; margin-bottom:0.75rem; opacity:0.5;"></i>
        <p>${isEn ? 'No stories found matching' : 'Không tìm thấy bài viết nào khớp với'} '<strong>${query}</strong>'</p>
        <p style="font-size:0.8125rem; margin-top:0.25rem;">${isEn ? 'Try searching by category name: Trending, Society, Human Stories, Mind & Soul...' : 'Hãy thử tìm theo tên chuyên mục: Trending, Society, Human Stories, Mind & Soul...'}</p>
      </div>
    `;
    return;
  }

  resultsBox.innerHTML = matches.map(item => {
    const artTitle = (isEn && item.title_en) ? item.title_en : item.title;
    return `
    <div class="search-result-item" onclick="closeSearchModal(); openArticleModal('${item.id}')" style="display:flex; gap:1rem; align-items:center; padding:0.75rem; border-bottom:1px solid var(--color-border-hairline); cursor:pointer;">
      <img src="${item.image}" alt="${artTitle}" style="width:60px; height:60px; border-radius:8px; object-fit:cover;" onerror="handleImageError(this)">
      <div>
        <span style="font-size:0.6875rem; color:var(--color-brand-primary); font-weight:800; text-transform:uppercase;">${item.categoryName}</span>
        <h4 style="font-family:var(--font-serif); font-size:0.95rem; font-weight:700; color:var(--color-text-headline); margin:0.15rem 0;">${highlightMatch(artTitle, trimmed)}</h4>
        <span style="font-size:0.75rem; color:var(--color-text-muted);">${item.author} • ${item.readTime}</span>
      </div>
    </div>
  `;
  }).join('');
}
window.handleSearchInput = handleSearchInput;

function applySearchTag(tag) {
  const input = document.getElementById('searchInput');
  if (input) {
    input.value = tag;
    handleSearchInput(tag);
  }
}
window.applySearchTag = applySearchTag;

function highlightMatch(text, query) {
  const regex = new RegExp(`(${query})`, 'gi');
  return text.replace(regex, '<mark style="background:#FCE8EC; color:#591724; font-weight:bold;">$1</mark>');
}

/* ===================================================================
   ONBOARDING SYSTEM (3-Step First-Time Walkthrough)
   =================================================================== */
function initOnboarding() {
  const hasOnboarded = localStorage.getItem('hearticles_onboarded_flag');
  if (!hasOnboarded) {
    // Only auto-show if desired or keep ready
  }
}

function openOnboardingModal() {
  const modal = document.getElementById('onboardModal');
  if (modal) {
    modal.classList.add('active');
    currentOnboardStep = 1;
    renderOnboardStep(1);
  }
}
window.openOnboardingModal = openOnboardingModal;

function closeOnboardingModal() {
  const modal = document.getElementById('onboardModal');
  if (modal) modal.classList.remove('active');
  localStorage.setItem('hearticles_onboarded_flag', 'true');
}
window.closeOnboardingModal = closeOnboardingModal;

function nextOnboardStep() {
  if (currentOnboardStep < 3) {
    currentOnboardStep++;
    renderOnboardStep(currentOnboardStep);
  } else {
    closeOnboardingModal();
    showToast(currentLanguage === 'en' ? 'Welcome to HEARTICLES.!' : 'Chào mừng bạn đến với HEARTICLES.!', 'heart');
  }
}
window.nextOnboardStep = nextOnboardStep;

function renderOnboardStep(step) {
  const dots = document.querySelectorAll('.onboard-step-dot');
  dots.forEach((dot, idx) => {
    dot.classList.toggle('active', idx === step - 1);
  });

  const content = document.getElementById('onboardStepContent');
  const btnNext = document.getElementById('onboardBtnNext');
  if (!content) return;

  const isEn = (currentLanguage === 'en');

  if (step === 1) {
    content.innerHTML = `
      <div class="onboard-badge">${isEn ? 'STEP 1 / 3 • WELCOME' : 'BƯỚC 1 / 3 • GIỚI THIỆU'}</div>
      <h2 class="onboard-title">HEARTICLES<span style="color:var(--color-brand-accent);">.</span></h2>
      <p class="onboard-desc">
        ${isEn ? 'High-fashion editorial news platform published by Class 6 - Group 1 - Term 127 at ULIS - VNU. Where news begins with a heartbeat.' : 'Tạp chí báo điện tử đa phương tiện xuất bản bởi sinh viên Trường Đại học Ngoại ngữ - ĐHQGHN (ULIS - VNU). Nơi tin tức khởi nguồn từ nhịp đập trái tim.'}
      </p>
    `;
    if (btnNext) btnNext.textContent = isEn ? 'Next' : 'Tiếp tục';
  } else if (step === 2) {
    content.innerHTML = `
      <div class="onboard-badge">${isEn ? 'STEP 2 / 3 • FEATURES' : 'BƯỚC 2 / 3 • TÍNH NĂNG'}</div>
      <h2 class="onboard-title">${isEn ? 'Smart Reading Suite' : 'Bộ công cụ đọc báo thông minh'}</h2>
      <p class="onboard-desc">
        ${isEn ? 'Includes Text-to-Speech audio reader, font zoom, fast keyboard shortcuts (/ to search, ESC to close), and bilingual support.' : 'Hỗ trợ đọc báo tự động qua giọng nói Web Speech, thu phóng cỡ chữ, phím tắt nhanh (/ để tìm kiếm) và song ngữ.'}
      </p>
    `;
    if (btnNext) btnNext.textContent = isEn ? 'Next' : 'Tiếp tục';
  } else {
    content.innerHTML = `
      <div class="onboard-badge">${isEn ? 'STEP 3 / 3 • READY' : 'BƯỚC 3 / 3 • BẮT ĐẦU'}</div>
      <h2 class="onboard-title">${isEn ? 'Authentic Stories' : '34 Phóng sự Báo chí'}</h2>
      <p class="onboard-desc">
        ${isEn ? '100% authentic articles and original photojournalism from The Guardian, Báo Nhân Dân, VnExpress, and more.' : '100% tác phẩm phóng sự và hình ảnh báo chí chân thực từ các nguồn báo chí uy tín chính thống.'}
      </p>
    `;
    if (btnNext) btnNext.textContent = isEn ? 'Start Exploring' : 'Bắt đầu trải nghiệm';
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
    showToast(currentLanguage === 'en' ? 'Offline mode enabled. Showing cached articles.' : 'Mất kết nối mạng. Bạn đang xem bản lưu ngoại tuyến.', 'wifi');
  });
  window.addEventListener('online', () => {
    if (banner) banner.classList.remove('active');
    showToast(currentLanguage === 'en' ? 'Internet connection restored.' : 'Đã khôi phục kết nối internet.', 'wifi');
  });
}

/* ===================================================================
   TOAST NOTIFICATION ENGINE
   =================================================================== */
function showToast(message, icon = 'check') {
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
}
window.showToast = showToast;

/* ===================================================================
   KEYBOARD SHORTCUTS MODAL
   =================================================================== */
function openShortcutsModal() {
  const modal = document.getElementById('shortcutsModal');
  if (modal) modal.classList.add('active');
}
window.openShortcutsModal = openShortcutsModal;

function closeShortcutsModal() {
  const modal = document.getElementById('shortcutsModal');
  if (modal) modal.classList.remove('active');
}
window.closeShortcutsModal = closeShortcutsModal;

/* ===================================================================
   DRAWER / OFFCANVAS MENU
   =================================================================== */
function openDrawer() {
  const drawer = document.getElementById('offcanvasDrawer');
  const backdrop = document.getElementById('drawerBackdrop');
  if (drawer && backdrop) {
    drawer.classList.add('active');
    backdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
}
window.openDrawer = openDrawer;

function closeDrawer() {
  const drawer = document.getElementById('offcanvasDrawer');
  const backdrop = document.getElementById('drawerBackdrop');
  if (drawer && backdrop) {
    drawer.classList.remove('active');
    backdrop.classList.remove('active');
    document.body.style.overflow = '';
  }
}
window.closeDrawer = closeDrawer;

/* ===================================================================
   SUBSCRIBE MODAL SIMULATION
   =================================================================== */
function openSubscribeModal() {
  const modal = document.getElementById('subscribeModal');
  if (modal) {
    modal.classList.add('active');
    return;
  }
  const isEn = (currentLanguage === 'en');
  const email = prompt(isEn ? 'Enter your email address to receive HEARTICLES. Sunday Edition:' : 'Nhập địa chỉ email của bạn để nhận bản tin thời trang & nhân văn HEARTICLES. mỗi sáng:');
  if (email && email.includes('@')) {
    localStorage.setItem('hearticles_subscribed_email', email);
    showToast(isEn ? 'Subscribed successfully! Thank you.' : 'Cảm ơn bạn! Đã đăng ký nhận bản tin thành công.', 'check-circle');
  } else if (email) {
    alert(isEn ? 'Please enter a valid email address.' : 'Vui lòng nhập địa chỉ email hợp lệ.');
  }
}
window.openSubscribeModal = openSubscribeModal;

function closeSubscribeModal() {
  const modal = document.getElementById('subscribeModal');
  if (modal) modal.classList.remove('active');
}
window.closeSubscribeModal = closeSubscribeModal;

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

function votePoll(optionIndex) {
  localStorage.setItem('hearticles_poll_voted', optionIndex);
  showPollResults();
  showToast(currentLanguage === 'en' ? 'Thank you for casting your vote!' : 'Cảm ơn bạn đã đóng góp ý kiến!', 'poll');
}
window.votePoll = votePoll;

function showPollResults() {
  const container = document.getElementById('pollContainer');
  if (!container) return;
  const isEn = (currentLanguage === 'en');
  container.innerHTML = `
    <div class="poll-results-box" style="background:rgba(255,255,255,0.08); padding:1rem; border-radius:8px;">
      <div style="margin-bottom:0.75rem;">
        <div style="display:flex; justify-content:space-between; font-size:0.8125rem; margin-bottom:0.25rem;">
          <span>${isEn ? '1. Pedestrian heritage zone planning' : '1. Quy hoạch tuyến phố đi bộ văn hóa'}</span>
          <strong>52% (1,420 ${isEn ? 'votes' : 'phiếu'})</strong>
        </div>
        <div style="background:rgba(255,255,255,0.2); height:6px; border-radius:3px; overflow:hidden;">
          <div style="background:#BA6975; width:52%; height:100%;"></div>
        </div>
      </div>
      <div style="margin-bottom:0.75rem;">
        <div style="display:flex; justify-content:space-between; font-size:0.8125rem; margin-bottom:0.25rem;">
          <span>${isEn ? '2. Honoring traditional craft heritage' : '2. Tôn vinh nét đẹp văn hóa truyền thống'}</span>
          <strong>34% (930 ${isEn ? 'votes' : 'phiếu'})</strong>
        </div>
        <div style="background:rgba(255,255,255,0.2); height:6px; border-radius:3px; overflow:hidden;">
          <div style="background:#E8A8B1; width:34%; height:100%;"></div>
        </div>
      </div>
      <div>
        <div style="display:flex; justify-content:space-between; font-size:0.8125rem; margin-bottom:0.25rem;">
          <span>${isEn ? '3. Sustainable livelihood support' : '3. Hỗ trợ sinh kế bền vững cho người nghèo'}</span>
          <strong>14% (385 ${isEn ? 'votes' : 'phiếu'})</strong>
        </div>
        <div style="background:rgba(255,255,255,0.2); height:6px; border-radius:3px; overflow:hidden;">
          <div style="background:#D8C0C4; width:14%; height:100%;"></div>
        </div>
      </div>
      <div style="margin-top:1rem; font-size:0.75rem; color:#FFD0D0; text-align:right;">
        <i class="fas fa-check-circle"></i> ${isEn ? 'You have voted in this survey.' : 'Bạn đã tham gia biểu quyết khảo sát này.'}
      </div>
    </div>
  `;
}

/* ===================================================================
   IMAGE ERROR HANDLER
   =================================================================== */
function handleImageError(img) {
  img.onerror = null;
  img.src = 'assets/images/trending/image8.jpg';
}
window.handleImageError = handleImageError;

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
      closeSubscribeModal();
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

/* ===================================================================
   HEART TAP & STRESS RELIEVER MINIGAME ENGINE
   =================================================================== */
function setupHeartTapWidget() {
  const btn = document.getElementById('heartTapBtn');
  const counterEl = document.getElementById('heartCountNumber');
  const msgEl = document.getElementById('heartAffirmationMsg');
  const particleContainer = document.getElementById('heartParticleContainer');
  if (!btn || !counterEl) return;

  let count = parseInt(localStorage.getItem('hearticles_tap_count') || '1280', 10);
  counterEl.textContent = count.toLocaleString();

  const affirmations_vi = [
    "“Hít một hơi thật sâu, thở ra nhẹ nhàng. Mọi chuyện rồi sẽ ổn thôi!”",
    "“Mỗi ngày là một khởi đầu mới với muôn vàn cơ hội tốt lành.”",
    "“Bạn đang làm rất tốt, hãy tự hào về hành trình của chính mình!”",
    "“Lòng tốt như những bông tuyết, làm đẹp mọi thứ mà nó chạm tới.”",
    "“Nụ cười của bạn hôm nay chính là món quà dành tặng cho thế giới.”",
    "“Hãy dịu dàng với bản thân, bạn xứng đáng được yêu thương và bình yên.”"
  ];
  const affirmations_en = [
    "“Take a deep breath and let it go. Everything will be okay!”",
    "“Every single day is a fresh beginning filled with wonderful possibilities.”",
    "“You are doing remarkably well—be proud of your journey!”",
    "“Kindness is like snow—it beautifies everything it covers.”",
    "“Your smile today is a heartfelt gift to the entire world.”",
    "“Be gentle with yourself; you deserve love, calm, and happiness.”"
  ];

  let affIdx = 0;

  btn.addEventListener('click', function(e) {
    count++;
    localStorage.setItem('hearticles_tap_count', count);
    counterEl.textContent = count.toLocaleString();

    // Floating heart particle animation
    if (particleContainer) {
      const heart = document.createElement('span');
      heart.className = 'floating-heart-particle';
      const emojis = ['❤️', '💖', '✨', '🌸', '💫'];
      heart.textContent = emojis[Math.floor(Math.random() * emojis.length)];
      heart.style.left = (Math.random() * 40 - 20) + 'px';
      heart.style.top = '-10px';
      particleContainer.appendChild(heart);
      setTimeout(() => heart.remove(), 1200);
    }

    // Affirmation rotation
    affIdx = (affIdx + 1) % affirmations_vi.length;
    if (msgEl) {
      const list = (currentLanguage === 'en') ? affirmations_en : affirmations_vi;
      msgEl.textContent = list[affIdx];
    }

    // Gentle tactile spring bounce
    btn.style.transform = 'scale(1.2) rotate(' + (Math.random() * 10 - 5) + 'deg)';
    setTimeout(() => { btn.style.transform = ''; }, 150);
  });
}
