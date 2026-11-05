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
  updateUserAvatarState();
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
   MULTIMEDIA & VIDEO PHÓNG SỰ HUB (12 Authentic Clips from Video Journal)
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
    desc: "Hội Áo dài Việt Nam tại Phần Lan chính thức ra mắt sáng kiến mang 1.000 tà áo dài truyền thống tới quốc gia Bắc Âu qua dự án 'Ngôi nhà Áo dài', thắt chặt sợi dây kết nối thế hệ và lan tỏa tinh hoa văn hóa dân tộc.",
    desc_en: "The Vietnamese Ao Dai Association in Finland launches a landmark initiative: bringing 1,000 traditional Ao Dai to the Nordic country through the 'Ao Dai House' project, celebrating national heritage and bridging cultural generations.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/ao-dai-celebrates-vietnamese-culture-in-finland-100261028101457215.htm",
    streamUrl: "https://cdn-videos.vtv.vn/66349b6076cb4dee98746cf1/2026/10/28/h264/mp4/ao-dai-27533120378672986580995.mp4/master.m3u8",
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
    desc: "Chiến lược quốc gia về phát triển trẻ em giai đoạn 2026–2035 nhằm củng cố kỹ năng số, nâng cao năng lực tự bảo vệ và kiến tạo một môi trường mạng an toàn, lành mạnh cho thế hệ trẻ.",
    desc_en: "Viet Nam’s National Strategy on Child Development for 2026–2035 aims to strengthen children’s digital skills and create a safer, empowering digital environment for them to grow up in.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/viet-nam-tackles-gaps-in-child-online-safety-100261101165727007.htm",
    streamUrl: "https://cdn-videos.vtv.vn/66349b6076cb4dee98746cf1/2026/11/01/h264/mp4/web-an-toan-87653776369114496232065.mp4/master.m3u8",
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
    desc: "Phóng sự điều tra chuyên sâu từ hãng thông tấn ARTE.tv bóc trần mạng lưới lừa đảo xuyên biên giới qua các nền tảng mạng xã hội, giải mã tâm lý thao túng tinh vi của tội phạm công nghệ cao.",
    desc_en: "An in-depth investigative documentary from ARTE.tv exposing the dark transnational web of social media romance scams, financial manipulation, and psychological deception.",
    author: "ARTE.tv Documentary",
    watchUrl: "https://www.youtube.com/watch?v=tIqYjcHRE04",
    streamUrl: "",
    embedUrl: "https://www.youtube.com/embed/tIqYjcHRE04",
    duration: "52:10",
    thumb: "assets/images/society/image15.png",
    articleId: "video-3",
    sourceType: "youtube"
  },
  {
    id: "clip-4",
    category: "Human Stories",
    category_en: "Human Stories",
    title: "Chiến dịch 500 ngày đêm: Khi khoa học mở đường đưa các anh hùng liệt sĩ trở về",
    title_en: "500-day-and-night campaign: When science paves way to bring fallen soldiers home",
    desc: "Hành trình xúc động của các nhà khoa học và lực lượng chức năng ứng dụng công nghệ giám định ADN hiện đại để tìm kiếm, xác định danh tính và đưa hài cốt các anh hùng liệt sĩ về với quê hương.",
    desc_en: "A moving documentary chronicling the landmark scientific effort of utilizing advanced DNA identification technology to bring fallen heroes back to their families and homeland.",
    author: "Báo Tin Tức • TTXVN / Vietnam News",
    watchUrl: "https://www.youtube.com/watch?v=KDXNK3brzG0",
    streamUrl: "",
    embedUrl: "https://www.youtube.com/embed/KDXNK3brzG0",
    duration: "14:25",
    thumb: "assets/images/human-stories/image1.png",
    articleId: "video-4",
    sourceType: "youtube"
  },
  {
    id: "clip-5",
    category: "Mind & Soul",
    category_en: "Mind & Soul",
    title: "Sân khấu dành cho mọi tiếng nói: Nghệ thuật dung nạp và hòa nhập",
    title_en: "A stage for every voice",
    desc: "Đối với các nghệ sĩ khuyết tật, con đường bước lên sân khấu là hành trình vượt lên rào cản thể chất để cất lên tiếng nói chân thực, kiến tạo nên những tác phẩm kịch nghệ hòa nhập sâu sắc.",
    desc_en: "For artists with disabilities, the stage represents an empowering sanctuary where creative expression flourishes and unique perspectives take center stage through collaborative theatre.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/a-stage-for-every-voice-100261029064303631.htm",
    streamUrl: "https://cdn-videos.vtv.vn/66349b6076cb4dee98746cf1/2026/10/29/h264/mp4/yt-15014836428526926456802.mp4/master.m3u8",
    embedUrl: "",
    duration: "4:40",
    thumb: "assets/images/mind-soul/image13.png",
    articleId: "video-5",
    sourceType: "vtv"
  },
  {
    id: "clip-6",
    category: "Mind & Soul",
    category_en: "Mind & Soul",
    title: "10 năm lớp học vĩ cầm miễn phí giữa lòng công viên TP.HCM",
    title_en: "10 years of free violin lessons in park",
    desc: "Suốt một thập kỷ qua, tiếng đàn violin réo rắt dưới bóng mát công viên giữa lòng Sài Gòn đã thắp sáng niềm đam mê âm nhạc hàn lâm cho hàng trăm bạn trẻ có hoàn cảnh khó khăn.",
    desc_en: "For ten years, free violin lessons in a public park in Ho Chi Minh City have unlocked the beauty of classical music for aspiring students from all walks of life.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/10-years-of-free-violin-lessons-in-park-100261029064839361.htm",
    streamUrl: "https://cdn-videos.vtv.vn/66349b6076cb4dee98746cf1/2026/10/29/h264/mp4/yt-52403677010684809792486.mp4/master.m3u8",
    embedUrl: "",
    duration: "3:30",
    thumb: "assets/images/mind-soul/image14.png",
    articleId: "video-6",
    sourceType: "vtv"
  },
  {
    id: "clip-7",
    category: "Society",
    category_en: "Society",
    title: "Văn hóa trà Thái Nguyên thúc đẩy phát triển du lịch bền vững",
    title_en: "Thai Nguyen tea culture boosts tourism",
    desc: "Tại Lễ hội Trà Quốc tế Thái Nguyên, những trải nghiệm văn hóa ẩm thực đặc sắc đang đưa du khách đến gần hơn với những người làm trà tâm huyết, mở ra tiềm năng du lịch sinh thái nông nghiệp.",
    desc_en: "At Thai Nguyen International Tea Festival, innovative cultural encounters connect tourists with local tea growers, forging sustainable community-based tourism models.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/thai-nguyen-tea-culture-boosts-tourism-100261101042721506.htm",
    streamUrl: "https://cdn-videos.vtv.vn/66349b6076cb4dee98746cf1/2026/11/01/h264/mp4/web-thai-nguyen-47460137484532453785769.mp4/master.m3u8",
    embedUrl: "",
    duration: "4:05",
    thumb: "assets/images/society/image16.png",
    articleId: "video-7",
    sourceType: "vtv"
  },
  {
    id: "clip-8",
    category: "Human Stories",
    category_en: "Human Stories",
    title: "Người mẹ Hà Nội biến bữa cơm gia đình thành tác phẩm nghệ thuật",
    title_en: "Mother turns meals into art",
    desc: "Từ những nguyên liệu rau củ thường nhật trong gian bếp ấm cúng, người mẹ Thủ đô đã khéo léo thổi hồn thành những bức tranh ẩm thực rực rỡ sắc màu, gửi gắm tình thương yêu con vô bờ bến.",
    desc_en: "In Hanoi, a devoted mother transforms everyday household meals into whimsical culinary art, infusing daily routines with joy, warmth, and maternal affection.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/mother-turns-meals-into-art-100260710095813651.htm",
    streamUrl: "https://cdn-videos.vtv.vn/66349b6076cb4dee98746cf1/2026/07/10/h264/mp4/yt-meals-fix-59113839086671818123733.mp4/master.m3u8",
    embedUrl: "",
    duration: "3:45",
    thumb: "assets/images/human-stories/image13.png",
    articleId: "video-8",
    sourceType: "vtv"
  },
  {
    id: "clip-9",
    category: "Mind & Soul",
    category_en: "Mind & Soul",
    title: "Ốc đảo chữa lành tâm hồn hoàn toàn miễn phí tại TP. Hồ Chí Minh",
    title_en: "A healing oasis in Ho Chi Minh City",
    desc: "Một không gian thanh tịnh phi thương mại dành cho bất kỳ ai đang cảm thấy mệt mỏi, căng thẳng giữa nhịp sống đô thị gấp gáp, trao đi sự tĩnh lặng và năng lượng tích cực hoàn toàn miễn phí.",
    desc_en: "A serene community sanctuary in Ho Chi Minh City offers mindfulness, meditation, and mental health refuge entirely free of charge for urban dwellers seeking peace.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/a-healing-oasis-in-ho-chi-minh-city-100260910032153068.htm",
    streamUrl: "https://cdn-videos.vtv.vn/66349b6076cb4dee98746cf1/2026/09/10/h264/mp4/yt-33204601654543588323037.mp4/master.m3u8",
    embedUrl: "",
    duration: "4:10",
    thumb: "assets/images/mind-soul/image15.png",
    articleId: "video-9",
    sourceType: "vtv"
  },
  {
    id: "clip-10",
    category: "Society",
    category_en: "Society",
    title: "Thiết chế thể thao cộng đồng tại Hà Nội thúc đẩy lối sống năng động",
    title_en: "Community facilities promote healthier lifestyles",
    desc: "Mạng lưới máy tập thể dục ngoài trời, đường chạy bộ quanh hồ và sân chơi thể thao công cộng tại Thủ đô đang lan tỏa thói quen sống khỏe, gắn kết tình làng nghĩa xóm trong từng khu dân cư.",
    desc_en: "Outdoor community gymnasiums, lakeside running tracks, and open neighborhood sports spaces across Hanoi are cultivating energetic, healthier community lifestyles.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/community-facilities-promote-healthier-lifestyles-100261019013046705.htm",
    streamUrl: "https://cdn-videos.vtv.vn/66349b6076cb4dee98746cf1/2026/10/19/h264/mp4/4-yt-community-facilities-promote-healthier-lifestyles-92475811190434812163691.mp4/master.m3u8",
    embedUrl: "",
    duration: "3:55",
    thumb: "assets/images/society/image17.png",
    articleId: "video-10",
    sourceType: "vtv"
  },
  {
    id: "clip-11",
    category: "Human Stories",
    category_en: "Human Stories",
    title: "Những người mẹ phi thường, tình yêu phi thường thắp sáng niềm tin",
    title_en: "Extraordinary mothers, extraordinary love",
    desc: "Nhân dịp Ngày của Mẹ, phóng sự tôn vinh nghị lực phi thường và đức hy sinh lặng thầm của những người mẹ kiên cường vượt qua nghịch cảnh để chở che và ươm mầm tương lai cho con cái.",
    desc_en: "Honoring Mother’s Day, this moving feature celebrates the boundless resilience, courage, and unconditional love of mothers who overcome extraordinary odds for their children.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/extraordinary-mothers-extraordinary-love-10026051107442239.htm",
    streamUrl: "https://cdn-videos.vtv.vn/66349b6076cb4dee98746cf1/2026/05/11/h264/mp4/yt-focus-mother-fix-41166236096252430779402.mp4/master.m3u8",
    embedUrl: "",
    duration: "4:30",
    thumb: "assets/images/human-stories/image14.png",
    articleId: "video-11",
    sourceType: "vtv"
  },
  {
    id: "clip-12",
    category: "Society",
    category_en: "Society",
    title: "Người trẻ chung tay chăm sóc và mang hơi ấm tới người cao tuổi neo đơn",
    title_en: "Youth caring for the elderly",
    desc: "Hành trình định kỳ hàng tháng của những bạn trẻ tình nguyện tại TP.HCM: dọn dẹp nhà cửa, tự tay nấu từng bữa cơm nóng và lắng nghe tâm sự của các cụ già neo đơn, cô quạnh.",
    desc_en: "Monthly volunteer journeys of youth groups in Ho Chi Minh City dedicated to cleaning homes, cooking warm meals, and bringing heartfelt companionship to isolated elderly citizens.",
    author: "BTV Quỳnh • Vietnam Today / VTV",
    watchUrl: "https://vietnamtoday.vtv.vn/youth-caring-for-the-elderly-100260226123528559.htm",
    streamUrl: "https://cdn-videos.vtv.vn/66349b6076cb4dee98746cf1/2026/02/26/h264/mp4/yt-81091811841841072429889.mp4/master.m3u8",
    embedUrl: "",
    duration: "4:15",
    thumb: "assets/images/society/image18.png",
    articleId: "video-12",
    sourceType: "vtv"
  }
];

// State managed above

// Helper to attach HLS streams reliably
function attachHlsStream(streamUrl) {
  setTimeout(() => {
    const videoEl = document.getElementById('activeNativePlayer');
    if (!videoEl || !streamUrl) return;

    if (window._currentHlsInstance) {
      try { window._currentHlsInstance.destroy(); } catch (e) {}
      window._currentHlsInstance = null;
    }

    if (window.Hls && window.Hls.isSupported()) {
      const hls = new window.Hls({
        enableWorker: true,
        lowLatencyMode: false
      });
      window._currentHlsInstance = hls;
      hls.loadSource(streamUrl);
      hls.attachMedia(videoEl);
      hls.on(window.Hls.Events.MANIFEST_PARSED, function () {
        const playPromise = videoEl.play();
        if (playPromise !== undefined) {
          playPromise.catch(err => {
            console.log('Autoplay deferred until user interaction:', err);
          });
        }
      });
      hls.on(window.Hls.Events.ERROR, function (event, data) {
        if (data.fatal) {
          switch (data.type) {
            case window.Hls.ErrorTypes.NETWORK_ERROR:
              hls.startLoad();
              break;
            case window.Hls.ErrorTypes.MEDIA_ERROR:
              hls.recoverMediaError();
              break;
            default:
              hls.destroy();
              break;
          }
        }
      });
    } else if (videoEl.canPlayType('application/vnd.apple.mpegurl')) {
      videoEl.src = streamUrl;
      const playPromise = videoEl.play();
      if (playPromise !== undefined) {
        playPromise.catch(err => {
          console.log('Autoplay deferred:', err);
        });
      }
    }
  }, 40);
}

function filterVideoCategory(categoryKey) {
  currentVideoCategoryFilter = categoryKey;
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

  const isYouTube = (mainClip.sourceType === 'youtube');

  const playBtnText = isEn ? 'Play on Web' : 'Phát Trực Tiếp';
  const stopBtnText = isEn ? 'Stop Video' : 'Dừng Video';
  const watchSourceText = isYouTube 
    ? (isEn ? 'Watch on YouTube ↗' : 'Xem trên YouTube ↗')
    : (isEn ? 'VTV Vietnam Today ↗' : 'Xem trên VTV Today ↗');
  const readStoryText = isEn ? 'Read Video Story' : 'Đọc Ký Sự Phóng Sự';

  const badgeHtml = isYouTube
    ? `<span class="video-badge-pill"><i class="fab fa-youtube"></i> YOUTUBE DOCUMENTARY</span>`
    : `<span class="video-badge-pill"><i class="fas fa-broadcast-tower"></i> VTV VIETNAM TODAY • MULTIMEDIA</span>`;

  // Render direct inline player stage
  let playerStageHtml = '';
  if (isVideoPlaying) {
    if (isYouTube) {
      playerStageHtml = `
        <div class="video-responsive-embed" id="videoPlayerStageWrap">
          <iframe id="activeVideoFrame" 
            src="${mainClip.embedUrl}?autoplay=1&rel=0&modestbranding=1&playsinline=1" 
            title="${mainTitle}" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            referrerpolicy="no-referrer-when-downgrade"
            allowfullscreen>
          </iframe>
        </div>
      `;
    } else {
      playerStageHtml = `
        <div class="video-responsive-embed" id="videoPlayerStageWrap">
          <video id="activeNativePlayer" 
            controls 
            autoplay 
            playsinline 
            poster="${mainClip.thumb}"
            class="video-native-player">
          </video>
        </div>
      `;
      attachHlsStream(mainClip.streamUrl);
    }
  } else {
    playerStageHtml = `
      <div class="video-poster-stage" id="videoPlayerStageWrap" onclick="playActiveVideo('${mainClip.id}')" title="${isEn ? 'Click to play directly on web' : 'Bấm để phát video trực tiếp trên web'}">
        <img src="${mainClip.thumb}" alt="${mainTitle}" class="video-poster-img" onerror="handleImageError(this)">
        <div class="video-poster-overlay"></div>
        <div class="video-poster-top">
          ${badgeHtml}
          <span class="video-duration-tag"><i class="fas fa-clock"></i> ${mainClip.duration}</span>
        </div>
        <div class="video-play-center">
          <button class="video-play-pulse-btn" aria-label="Play Video">
            <i class="fas fa-play"></i>
          </button>
          <span class="video-play-hint">${isEn ? 'Play Directly on Web' : 'Phát Trực Tiếp Trên Web'}</span>
        </div>
      </div>
    `;
  }

  // Action Toolbar below player
  const playButtonHtml = isVideoPlaying
    ? `<button class="video-tool-btn primary" onclick="stopActiveVideo()" title="${stopBtnText}">
         <i class="fas fa-stop"></i> <span>${stopBtnText}</span>
       </button>`
    : `<button class="video-tool-btn primary" onclick="playActiveVideo('${mainClip.id}')" title="${playBtnText}">
         <i class="fas fa-play"></i> <span>${playBtnText}</span>
       </button>`;

  const sourceBtnClass = isYouTube ? 'youtube' : 'vtv';
  const sourceIconClass = isYouTube ? 'fab fa-youtube' : 'fas fa-tv';

  const actionToolbarHtml = `
    <div class="video-toolbar-strip">
      ${playButtonHtml}
      <button class="video-tool-btn story" onclick="openVideoStoryModal('${mainClip.id}')" title="${readStoryText}">
        <i class="fas fa-newspaper"></i> <span>${readStoryText}</span>
      </button>
      <a href="${mainClip.watchUrl}" target="_blank" rel="noopener noreferrer" class="video-tool-btn ${sourceBtnClass}" title="${watchSourceText}">
        <i class="${sourceIconClass}"></i> <span>${watchSourceText}</span>
      </a>
      ${isVideoPlaying ? `<span class="video-playing-indicator"><span class="video-playing-dot"></span> ${isEn ? 'LIVE PLAYING' : 'ĐANG PHÁT'}</span>` : ''}
    </div>
  `;

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
        ${playerStageHtml}
        ${actionToolbarHtml}

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
            <div class="playlist-card ${isActive ? 'active' : ''}" onclick="playActiveVideo('${clip.id}')" title="${isEn ? 'Click to play' : 'Bấm để phát trực tiếp'}">
              <div class="playlist-thumb-wrap">
                <img src="${clip.thumb}" alt="${title}" loading="lazy" onerror="handleImageError(this)">
                <div class="playlist-play-icon">
                  <i class="${isActive && isVideoPlaying ? 'fas fa-volume-up' : iconClass}"></i>
                </div>
                <span class="playlist-duration-badge">${clip.duration}</span>
              </div>
              <div class="playlist-info">
                <span class="playlist-cat">${cat}</span>
                <h4 class="playlist-title">${title}</h4>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-top:0.25rem;">
                  <span class="playlist-byline">${clip.author.split('•')[0].trim()}</span>
                  ${isActive && isVideoPlaying ? `<span style="font-size:0.7rem; color:#4ADE80; font-weight:700;"><i class="fas fa-play"></i> NOW</span>` : ''}
                </div>
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
  isVideoPlaying = true;
  renderVideoHub();

  const wrap = document.getElementById('videoPlayerStageWrap');
  if (wrap && window.innerWidth < 992) {
    wrap.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
}
window.playActiveVideo = playActiveVideo;

function stopActiveVideo() {
  if (window._currentHlsInstance) {
    try { window._currentHlsInstance.destroy(); } catch (e) {}
    window._currentHlsInstance = null;
  }
  const videoEl = document.getElementById('activeNativePlayer');
  if (videoEl) {
    videoEl.pause();
    videoEl.src = '';
  }
  isVideoPlaying = false;
  renderVideoHub();
}
window.stopActiveVideo = stopActiveVideo;

function switchVideo(clipId) {
  playActiveVideo(clipId);
}
window.switchVideo = switchVideo;

function openVideoStoryModal(clipId) {
  const clip = VIDEO_CLIPS.find(c => c.id === clipId) || VIDEO_CLIPS[0];
  const modal = document.getElementById('articleReaderModal');
  const body = document.getElementById('articleModalBody');
  if (!modal || !body) return;

  const isEn = (currentLanguage === 'en');
  const title = isEn ? (clip.title_en || clip.title) : clip.title;
  const desc = isEn ? (clip.desc_en || clip.desc) : clip.desc;
  const cat = isEn ? (clip.category_en || clip.category) : clip.category;
  const sourceName = clip.sourceType === 'youtube' ? 'YouTube / TTXVN & ARTE' : 'VTV Today / VTV';

  body.innerHTML = `
    <article class="article-detail">
      <header class="article-header">
        <div class="article-breadcrumb">
          <span>${isEn ? 'Home' : 'Trang chủ'}</span> &gt;
          <span>Multimedia Video Hub</span> &gt;
          <span style="color:var(--color-brand-primary); font-weight:700;">${cat}</span>
        </div>
        <div class="article-category-badge-wrap" style="margin-top:0.75rem;">
          <span class="category-tag">${cat}</span>
          <span style="font-size:0.8rem; background:rgba(84,17,30,0.1); color:#54111E; padding:0.25rem 0.65rem; border-radius:4px; font-weight:700; margin-left:0.5rem;">
            <i class="fas fa-video"></i> ${isEn ? 'Video Documentary' : 'Ký sự Phóng sự Video'}
          </span>
        </div>
        <h1 class="article-title" style="font-size:2rem; margin:1rem 0;">${title}</h1>
        <div class="article-meta-row" style="margin-bottom:1.5rem; color:var(--color-text-muted); font-size:0.875rem;">
          <span><i class="fas fa-user-edit"></i> ${clip.author}</span>
          <span style="margin:0 0.5rem;">•</span>
          <span><i class="fas fa-clock"></i> ${clip.duration}</span>
        </div>
      </header>
      
      <div class="article-featured-image-wrap" style="margin-bottom:2rem; border-radius:8px; overflow:hidden;">
        <img src="${clip.thumb}" alt="${title}" style="width:100%; max-height:480px; object-fit:cover; display:block;">
      </div>

      <div class="article-body-text" style="font-size:1.1rem; line-height:1.85; color:var(--color-text-body); text-align:justify;">
        <p style="font-weight:600; font-size:1.2rem; line-height:1.75; color:var(--color-text-headline); margin-bottom:1.5rem;">
          ${desc}
        </p>
        <p>
          ${isEn 
            ? 'This special multimedia phóng sự feature was produced with rigorous academic journalistic verification, capturing real voices, authentic cultural heritage, and human-centric narratives. Every frame and interview adheres to strict fact-checking standards and ethical journalism.' 
            : 'Tác phẩm phóng sự đa phương tiện đặc biệt này được thực hiện với chuẩn mực thẩm định báo chí học thuật chặt chẽ, ghi lại những thanh âm chân thực của đời sống, chiều sâu di sản văn hóa và những câu chuyện nhân văn đầy cảm xúc. Mọi thước phim và lời bộc bạch của nhân vật đều tuân thủ các nguyên tắc đạo đức báo chí và kiểm chứng đa nguồn.'}
        </p>
        <div style="margin:2rem 0; text-align:center;">
          <button onclick="closeArticleModal(); playActiveVideo('${clip.id}'); document.getElementById('multimedia-hub')?.scrollIntoView({behavior:'smooth'});" class="fashion-subscribe-btn" style="padding:0.75rem 2rem; font-size:1rem;">
            <i class="fas fa-play" style="margin-right:0.5rem;"></i> ${isEn ? 'Watch Video Inline on Web' : 'Phát Video Trực Tiếp Trên Web'}
          </button>
        </div>
      </div>

      <div class="article-source-citation" style="margin-top:2.5rem; padding:1.25rem; background:var(--color-bg-alt, #FAFAFA); border-radius:6px; border:1px solid var(--color-border-hairline);">
        <span class="citation-label" style="font-weight:700;">${isEn ? 'Official Broadcasting Source:' : 'Nguồn phát sóng chính thức:'}</span> 
        <em>${title}</em> • <strong>${sourceName}</strong>
        <a href="${clip.watchUrl}" target="_blank" rel="noopener noreferrer" class="citation-url" style="display:block; margin-top:0.4rem; color:var(--color-brand-primary);">
          <i class="fas fa-external-link-alt" style="margin-right:0.35rem;"></i>${clip.watchUrl}
        </a>
      </div>
    </article>
  `;

  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
}
window.openVideoStoryModal = openVideoStoryModal;

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
      <a href="#mission" class="about-tab-btn"><i class="fas fa-bullseye"></i> <span data-i18n="about_tab_mission">${isEn ? 'Mission, Ethics & Compliance' : 'Tôn Chỉ Hoạt Động & Chuẩn Mực'}</span></a>
      <a href="#profiles" class="about-tab-btn"><i class="fas fa-users"></i> <span data-i18n="about_tab_profiles">${isEn ? 'Editorial Profiles' : 'Hồ Sơ Ban Biên Tập'}</span></a>
      <a href="#photo" class="about-tab-btn"><i class="fas fa-camera"></i> <span data-i18n="about_tab_photo">${isEn ? 'Photojournalism Gallery' : 'Kho Ảnh Phóng Sự Báo Chí'}</span></a>
      <a href="#subscribe" class="about-tab-btn"><i class="fas fa-paper-plane"></i> <span data-i18n="about_tab_subscribe">${isEn ? 'Newsletter Subscription' : 'Đăng Ký Nhận Bản Tin'}</span></a>
    </nav>

    <!-- SECTION 1: MISSION & EDITORIAL PHILOSOPHY (#mission) -->
    <section id="mission" style="margin-bottom: 3.5rem; scroll-margin-top: 100px;">
      <div class="nhandan-section-header">
        <div class="nhandan-sec-title-wrap">
          <span class="nhandan-sec-ribbon"></span>
          <h2 class="nhandan-sec-title" data-i18n="about_mission_title">${isEn ? 'MISSION & EDITORIAL PHILOSOPHY' : 'TÔN CHỈ HOẠT ĐỘNG & TRIẾT LÝ TÒA SOẠN'}</h2>
        </div>
      </div>
      <div style="background:#FFFFFF; border:1px solid var(--color-border-hairline); border-radius:var(--radius-lg); padding:2.5rem; color:var(--color-text-body); box-shadow:var(--shadow-card, 0 4px 20px rgba(0,0,0,0.03));">
        <h3 style="font-family: var(--font-editorial, 'Playfair Display', serif); font-size: 1.65rem; font-weight: 700; color: var(--color-brand-primary, #54111E); margin-top: 0; margin-bottom: 1.25rem; letter-spacing: -0.01em;">
          ${isEn ? 'Welcome to HEARTICLES' : 'Chào Mừng Đến Với HEARTICLES'}
        </h3>
        
        <p style="margin-bottom:1.25rem; font-size:1.05rem; line-height:1.8; text-align:justify;">
          ${isEn 
            ? 'Based in Hanoi, Vietnam, HEARTICLES is an academic multimedia journalism publication born out of a simple, unwavering belief: in a world driven by rapid headlines and digital noise, true journalism must never lose its soul. Every piece we publish is built upon rigorous, multi-source verification and authentic engagement with official, credible sources, ensuring that all our reporting stands as trustworthy, accurate, and deeply reliable.' 
            : 'Đặt trụ sở tại Hà Nội, Việt Nam, HEARTICLES là ấn phẩm báo chí đa phương tiện học thuật ra đời từ một niềm tin giản dị nhưng kiên định: giữa một thế giới bị cuốn theo những dòng tít chóng vánh và sự ồn ào của kỷ nguyên số, báo chí chân chính không bao giờ được đánh mất linh hồn của mình. Mọi tác phẩm chúng tôi xuất bản đều được xây dựng trên quy trình kiểm chứng đa nguồn nghiêm ngặt và sự kết nối trực tiếp với các nguồn tin chính thống, uy tín, nhằm bảo đảm mỗi bài viết luôn trung thực, chính xác và đáng tin cậy sâu sắc.'}
        </p>

        <p style="margin-bottom:1.25rem; font-size:1.05rem; line-height:1.8; text-align:justify;">
          ${isEn 
            ? 'At HEARTICLES, our editorial heart beats for human-centric storytelling. We specialize in bringing forward stories of empathy, kindness, and unsung resilience—the quiet moments of human goodness that often go unnoticed, yet remind us of our shared humanity. Our perspective reaches far beyond borders: while we honor the timeless charm and spirit of Hanoi, our lens extends across the globe to cover diverse human experiences, vibrant cultures, local food traditions, and inspiring lifestyle narratives from every corner of the world.' 
            : 'Tại HEARTICLES, trái tim biên tập của chúng tôi luôn đập cùng những câu chuyện lấy con người làm trung tâm. Chúng tôi chuyên chở những câu chuyện về sự đồng cảm, lòng trắc ẩn và sự kiên cường thầm lặng—những khoảnh khắc tốt đẹp bình dị thường bị lãng quên nhưng nhắc nhở chúng ta về sự gắn kết nhân văn. Góc nhìn của chúng tôi vươn xa khỏi mọi biên giới: vừa tôn vinh nét đẹp vượt thời gian và tinh thần của Hà Nội, ống kính của chúng tôi vừa mở rộng ra khắp thế giới để ghi lại những trải nghiệm đa dạng, các nền văn hóa sống động, nét ẩm thực bản địa cùng những câu chuyện phong cách sống đầy cảm hứng từ mọi phương trời.'}
        </p>

        <p style="margin-bottom:1.75rem; font-size:1.05rem; line-height:1.8; text-align:justify;">
          ${isEn 
            ? 'While our storytelling is rooted in deep empathy, our reporting is firmly grounded in journalistic integrity and fully verified information. We write not just to report events, but to touch hearts, build global bridges, and foster a more thoughtful, compassionate world.' 
            : 'Nếu như cách kể chuyện của chúng tôi bắt nguồn từ sự thấu cảm sâu sắc, thì phương pháp đưa tin luôn được đặt nền móng vững chắc trên đạo đức báo chí và thông tin đã được kiểm chứng tuyệt đối. Chúng tôi cầm bút không chỉ để đưa tin về các sự kiện, mà còn để chạm tới những trái tim, xây dựng những nhịp cầu kết nối toàn cầu và nuôi dưỡng một thế giới sâu lắng, giàu lòng trắc ẩn hơn.'}
        </p>

        <div style="padding-top:1.25rem; border-top:1px dashed var(--color-border-hairline); display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:0.75rem; font-size:0.875rem; color:var(--color-text-muted);">
          <span>
            <i class="fas fa-shield-alt" style="color:var(--color-brand-primary); margin-right:0.35rem;"></i>
            ${isEn ? 'Academic Multimedia Journalism Project • ULIS - VNU • Class 6 - Group 1 - Term 127' : 'Đề án Báo chí Đa phương tiện Học thuật • ULIS - VNU • Lớp 6 - Nhóm 1 - Khóa 127'}
          </span>
          <span>
            <i class="fas fa-check-circle" style="color:#2E7D32; margin-right:0.35rem;"></i>
            ${isEn ? 'Multi-Source Fact-Checking & Journalistic Ethics Compliance' : 'Kiểm chứng đa nguồn & Tuân thủ Chuẩn mực Đạo đức Báo chí'}
          </span>
        </div>
      </div>
    </section>
<!-- SECTION 2: PROFILES (#profiles) -->
    <section id="profiles" style="margin-bottom: 3.5rem; scroll-margin-top: 100px;">
      <div class="nhandan-section-header">
        <div class="nhandan-sec-title-wrap">
          <span class="nhandan-sec-ribbon"></span>
          <h2 class="nhandan-sec-title" data-i18n="profiles_sec_title">${isEn ? 'EDITORIAL BOARD & NEWSROOM ROSTER' : 'BAN BIÊN TẬP & NHÂN SỰ TÒA SOẠN'}</h2>
          <span class="nhandan-sec-sub" data-i18n="profiles_sec_sub">${isEn ? 'Class 6 - Group 1 - Term 127 • Faculty of English Language and Culture • ULIS - VNU' : 'Lớp 6 - Nhóm 1 - Khóa 127 • Khoa Ngôn ngữ và Văn hóa các nước nói tiếng Anh (Faculty of English Language and Culture) • Trường ĐH Ngoại ngữ - ĐHQGHN'}</span>
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

    <!-- SECTION 3: PHOTOJOURNALISM MOSAIC (#photo) -->
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

    <!-- SECTION 4: NEWSLETTER SUBSCRIPTION (#subscribe) -->
    <section id="subscribe" style="margin-bottom: 2rem; scroll-margin-top: 100px;">
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
  `;

  // Highlight active tab based on hash or default to #mission
  const currentHash = window.location.hash || '#mission';
  const tabs = container.querySelectorAll('.about-tab-btn');
  tabs.forEach(tab => {
    if (tab.getAttribute('href') === currentHash) {
      tab.classList.add('active');
    } else {
      tab.classList.remove('active');
    }
    tab.addEventListener('click', function() {
      tabs.forEach(t => t.classList.remove('active'));
      this.classList.add('active');
    });
  });
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
      if (typeof p !== 'string') return '';
      const trimmed = p.trim();
      if (trimmed.startsWith('### ')) {
        return `<h3 class="article-section-heading" style="font-family:var(--font-editorial); font-size:1.35rem; font-weight:800; color:var(--color-brand-primary); margin:1.75rem 0 0.75rem 0;">${trimmed.replace('### ', '')}</h3>`;
      }
      if (trimmed.startsWith('## ')) {
        return `<h2 class="article-section-heading-lg" style="font-family:var(--font-editorial); font-size:1.55rem; font-weight:800; color:var(--color-brand-primary); margin:2rem 0 0.85rem 0;">${trimmed.replace('## ', '')}</h2>`;
      }
      if (trimmed.startsWith('<figure') || trimmed.startsWith('<table') || trimmed.startsWith('<div') || trimmed.startsWith('<blockquote')) {
        return trimmed;
      }
      return `<p style="margin-bottom:1.15rem; line-height:1.8; text-align:justify;">${p}</p>`;
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
    const card = modal.querySelector('.onboard-card');
    const isEn = (typeof currentLanguage !== 'undefined' && currentLanguage === 'en');
    if (card) {
      card.innerHTML = `
        <button onclick="closeSubscribeModal()" style="position:absolute; top:1.25rem; right:1.25rem; font-size:1.25rem; color:var(--color-text-muted); cursor:pointer; background:none; border:none;" aria-label="Đóng"><i class="fas fa-times"></i></button>
        <div style="font-size:2.5rem; color:var(--color-brand-primary); margin-bottom:0.5rem;"><i class="fas fa-envelope-open-text"></i></div>
        <h3 style="font-family:var(--font-editorial); font-size:1.5rem; font-weight:800; color:var(--color-brand-primary);" data-i18n="subscribe_modal_title">${isEn ? 'Subscribe to HEARTICLES. Sunday Edition' : 'Đăng Ký Nhận Bản Tin HEARTICLES.'}</h3>
        <p style="font-size:0.875rem; color:var(--color-text-body); margin:0.75rem 0 1.25rem 0;" data-i18n="subscribe_modal_desc">${isEn ? 'Receive curated humanistic stories and ethical journalism insights directly to your inbox every Sunday morning.' : 'Nhận tuyển tập những bài viết nhân văn sâu sắc và ký sự chạm đến trái tim vào mỗi sáng Chủ nhật.'}</p>
        <form onsubmit="handleSubscribeSubmit(event)" style="display:flex; flex-direction:column; gap:0.75rem;">
          <input type="email" id="subscribeEmailInput" required placeholder="name@example.com" style="padding:0.75rem 1rem; border:1px solid var(--color-border-hairline); border-radius:8px; font-size:0.9rem; outline:none; box-sizing:border-box;">
          <button type="submit" id="subscribeSubmitBtn" class="fashion-btn-pill" style="padding:0.75rem; cursor:pointer; font-weight:700;" data-i18n="btn_subscribe">${isEn ? 'Subscribe' : 'Đăng Ký Ngay'}</button>
        </form>
      `;
    }
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
    setTimeout(() => {
      const input = document.getElementById('subscribeEmailInput');
      if (input) input.focus();
    }, 150);
    return;
  }
}
window.openSubscribeModal = openSubscribeModal;

function closeSubscribeModal() {
  const modal = document.getElementById('subscribeModal');
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }
}
window.closeSubscribeModal = closeSubscribeModal;

function handleSubscribeSubmit(e) {
  if (e) e.preventDefault();
  const form = e ? e.target : null;
  const input = form ? form.querySelector('input[type="email"]') : document.getElementById('subscribeEmailInput');
  const email = input ? input.value.trim() : '';

  if (!email || !email.includes('@')) {
    const isEn = (typeof currentLanguage !== 'undefined' && currentLanguage === 'en');
    showToast(isEn ? 'Please enter a valid email address.' : 'Vui lòng nhập địa chỉ email hợp lệ.', 'exclamation-circle');
    return;
  }

  // Save to localStorage
  localStorage.setItem('hearticles_subscribed_email', email);

  // Success screen inside modal if modal is open
  const modal = document.getElementById('subscribeModal');
  const card = modal ? modal.querySelector('.onboard-card') : null;
  const isEn = (typeof currentLanguage !== 'undefined' && currentLanguage === 'en');

  if (card && modal.classList.contains('active')) {
    card.innerHTML = `
      <div style="font-size:3.25rem; color:#22C55E; margin-bottom:0.75rem;"><i class="fas fa-check-circle"></i></div>
      <h3 style="font-family:var(--font-editorial); font-size:1.55rem; font-weight:800; color:var(--color-brand-primary);">
        ${isEn ? 'Subscribed Successfully!' : 'Đăng Ký Nhận Bản Tin Thành Công!'}
      </h3>
      <p style="font-size:0.925rem; color:var(--color-text-body); margin:0.75rem 0 1.5rem 0; line-height:1.6;">
        ${isEn ? `Thank you! Future editions will be delivered to <strong>${email}</strong> every Sunday.` : `Cảm ơn bạn! Các ấn phẩm Chủ Nhật sẽ được gửi trực tiếp tới <strong>${email}</strong>.`}
      </p>
      <button type="button" class="fashion-btn-pill" onclick="closeSubscribeModal()" style="padding:0.75rem 2rem; font-weight:700;">
        ${isEn ? 'Close & Continue Reading' : 'Đóng & Tiếp Tục Đọc Báo'}
      </button>
    `;
  }

  // Show toast notification
  showToast(isEn ? 'Subscribed successfully! Thank you.' : 'Cảm ơn bạn! Đã đăng ký nhận bản tin thành công.', 'check-circle');

  // Also auto-close modal after 3 seconds
  setTimeout(() => {
    closeSubscribeModal();
  }, 3200);
}
window.handleSubscribeSubmit = handleSubscribeSubmit;
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
  const badgeEl = document.getElementById('heartCounterBadge');
  const msgEl = document.getElementById('heartAffirmationMsg');
  const particleContainer = document.getElementById('heartParticleContainer');
  const stageEl = btn ? btn.parentElement : null;
  if (!btn || !counterEl) return;

  let count = parseInt(localStorage.getItem('hearticles_tap_count') || '1280', 10);
  counterEl.textContent = count.toLocaleString();

  const affirmations_vi = [
    "“Hít một hơi thật sâu, thở ra nhẹ nhàng. Mọi chuyện rồi sẽ ổn thôi!”",
    "“Mỗi ngày là một khởi đầu mới với muôn vàn cơ hội tốt lành.”",
    "“Bạn đang làm rất tốt, hãy tự hào về hành trình của chính mình!”",
    "“Lòng tốt như những bông tuyết, làm đẹp mọi thứ mà nó chạm tới.”",
    "“Nụ cười của bạn hôm nay chính là món quà dành tặng cho thế giới.”",
    "“Hãy dịu dàng với bản thân, bạn xứng đáng được yêu thương và bình yên.”",
    "“Một cử chỉ tử tế nhỏ bé cũng đủ sưởi ấm cả một ngày dài.”",
    "“Trái tim bình an là khởi nguồn của mọi điều kỳ diệu.”"
  ];
  const affirmations_en = [
    "“Take a deep breath and let it go. Everything will be okay!”",
    "“Every single day is a fresh beginning filled with wonderful possibilities.”",
    "“You are doing remarkably well—be proud of your journey!”",
    "“Kindness is like snow—it beautifies everything it covers.”",
    "“Your smile today is a heartfelt gift to the entire world.”",
    "“Be gentle with yourself; you deserve love, calm, and happiness.”",
    "“A single small act of kindness can brighten an entire day.”",
    "“A peaceful heart is the wellspring of all everyday wonders.”"
  ];

  let affIdx = 0;
  let heartAudioCtx = null;

  function playHeartChime() {
    try {
      const AudioCtxClass = window.AudioContext || window.webkitAudioContext;
      if (!AudioCtxClass) return;
      if (!heartAudioCtx) heartAudioCtx = new AudioCtxClass();
      if (heartAudioCtx.state === 'suspended') {
        heartAudioCtx.resume();
      }
      const osc = heartAudioCtx.createOscillator();
      const gain = heartAudioCtx.createGain();
      osc.type = 'sine';
      // Soothing 528Hz Solfeggio frequency (Miracle tone) gently climbing to 660Hz
      const t = heartAudioCtx.currentTime;
      osc.frequency.setValueAtTime(528, t);
      osc.frequency.exponentialRampToValueAtTime(660, t + 0.15);
      gain.gain.setValueAtTime(0.2, t);
      gain.gain.exponentialRampToValueAtTime(0.001, t + 0.38);
      osc.connect(gain);
      gain.connect(heartAudioCtx.destination);
      osc.start(t);
      osc.stop(t + 0.4);
    } catch (err) {
      // Audio playback fails gracefully if autoplay restricted
    }
  }

  function burstHearts() {
    if (!particleContainer) return;
    const emojis = ['❤️', '💖', '💗', '💓', '💞', '💕', '💘', '✨', '🌸', '💝', '🎉', '🌟', '🥰', '🔥'];
    const totalParticles = 22; // Explosive radial burst!

    // Ripple Shockwave Ring
    if (stageEl) {
      const shockwave = document.createElement('div');
      shockwave.className = 'heart-shockwave';
      stageEl.appendChild(shockwave);
      setTimeout(() => shockwave.remove(), 750);

      // Floating "+1 ❤️" Floater
      const plusOne = document.createElement('div');
      plusOne.className = 'burst-plus-one';
      plusOne.innerHTML = '<i class="fas fa-heart"></i> +1';
      stageEl.appendChild(plusOne);
      setTimeout(() => plusOne.remove(), 950);
    }

    // Radial 360-degree explosion of heart particles
    for (let i = 0; i < totalParticles; i++) {
      const p = document.createElement('span');
      p.className = 'burst-heart-particle';
      p.textContent = emojis[Math.floor(Math.random() * emojis.length)];

      const angle = (i / totalParticles) * 2 * Math.PI + (Math.random() - 0.5) * 0.45;
      const distance = 65 + Math.random() * 145; // 65px to 210px fly distance
      const tx = Math.round(Math.cos(angle) * distance);
      const ty = Math.round(Math.sin(angle) * distance - 25);
      const rot = Math.round((Math.random() - 0.5) * 360);
      const scaleEnd = (0.55 + Math.random() * 0.85).toFixed(2);
      const fontSize = (1.1 + Math.random() * 1.2).toFixed(2) + 'rem';
      const duration = (0.75 + Math.random() * 0.35).toFixed(2) + 's';

      p.style.setProperty('--tx', `${tx}px`);
      p.style.setProperty('--ty', `${ty}px`);
      p.style.setProperty('--rot', `${rot}deg`);
      p.style.setProperty('--scale-end', scaleEnd);
      p.style.fontSize = fontSize;
      p.style.animationDuration = duration;

      particleContainer.appendChild(p);
      setTimeout(() => p.remove(), 1100);
    }
  }

  btn.addEventListener('click', function(e) {
    count++;
    localStorage.setItem('hearticles_tap_count', count);
    counterEl.textContent = count.toLocaleString();

    // Trigger explosive radial burst
    burstHearts();

    // Play gentle chime tone
    playHeartChime();

    // Button squash-and-stretch pop animation
    btn.classList.remove('popping');
    void btn.offsetWidth; // force DOM reflow
    btn.classList.add('popping');
    setTimeout(() => btn.classList.remove('popping'), 400);

    // Counter badge pulse pop
    if (badgeEl) {
      badgeEl.classList.remove('pop-active');
      void badgeEl.offsetWidth;
      badgeEl.classList.add('pop-active');
      setTimeout(() => badgeEl.classList.remove('pop-active'), 400);
    }

    // Affirmation quote rotation with smooth opacity fade
    if (msgEl) {
      affIdx = (affIdx + 1) % affirmations_vi.length;
      const list = (typeof currentLanguage !== 'undefined' && currentLanguage === 'en') ? affirmations_en : affirmations_vi;
      msgEl.style.opacity = '0';
      msgEl.style.transform = 'translateY(4px)';
      setTimeout(() => {
        msgEl.textContent = list[affIdx];
        msgEl.style.opacity = '1';
        msgEl.style.transform = 'translateY(0)';
      }, 140);
    }
  });
}

/* ===================================================================
   READER SIGN IN & AVATAR HANDLER
   =================================================================== */
function openSignInModal() {
  const modal = document.getElementById('signInModal');
  if (modal) {
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
}

function closeSignInModal() {
  const modal = document.getElementById('signInModal');
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }
}

function handleSignInSubmit(e) {
  if (e) e.preventDefault();
  const emailInput = document.getElementById('signInEmail');
  const email = emailInput ? emailInput.value.trim() : 'reader@ulis.vnu.edu.vn';
  localStorage.setItem('hearticles_user_logged_in', 'true');
  localStorage.setItem('hearticles_user_email', email);
  updateUserAvatarState();
  closeSignInModal();
  const isEn = typeof currentLanguage !== 'undefined' && currentLanguage === 'en';
  showToast(isEn ? 'Welcome back, ' + email.split('@')[0] + '!' : 'Chào mừng bạn quay trở lại, ' + email.split('@')[0] + '!', 'check');
}

function updateUserAvatarState() {
  const isLoggedIn = localStorage.getItem('hearticles_user_logged_in') === 'true';
  const userBtns = document.querySelectorAll('.fashion-user-btn');
  userBtns.forEach(btn => {
    if (isLoggedIn) {
      btn.classList.add('signed-in');
      btn.innerHTML = '<i class="fas fa-user-check"></i>';
      btn.title = 'Đã đăng nhập • Độc giả HEARTICLES';
    } else {
      btn.classList.remove('signed-in');
      btn.innerHTML = '<i class="far fa-user-circle"></i>';
      btn.title = 'Đăng nhập / Sign In';
    }
  });
}
