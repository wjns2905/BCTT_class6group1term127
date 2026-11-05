import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replacement block for VIDEO_CLIPS down to before renderFashionJournal
replacement_code = '''const VIDEO_CLIPS = [
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

let currentActiveClipId = 'clip-1';
let isVideoPlaying = false;

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
'''

# Find the exact span to replace in js
start_marker = 'const VIDEO_CLIPS = ['
end_marker = '/* ===================================================================\n   THE JOURNAL (Full Curated Articles Magazine Grid)'

start_pos = js.find(start_marker)
end_pos = js.find(end_marker)

if start_pos == -1 or end_pos == -1:
    print(f"Error: markers not found. start={start_pos}, end={end_pos}")
    sys.exit(1)

new_js = js[:start_pos] + replacement_code + '\n' + js[end_pos:]

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'w', encoding='utf-8') as f:
    f.write(new_js)

print("Updated js/app.js successfully!")
