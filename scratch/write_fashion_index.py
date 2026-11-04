import sys

sys.stdout.reconfigure(encoding='utf-8')

HTML_CONTENT = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HEARTICLES. — Stories that speak to the heart | Tạp chí Báo điện tử Đa phương tiện</title>
  <meta name="description" content="HEARTICLES. - Tạp chí báo điện tử đa phương tiện chất lượng cao theo phong cách Vogue, Kinfolk, Elle. Phát triển bởi sinh viên ULIS - VNU. Nơi tin tức khởi nguồn từ nhịp đập trái tim.">
  <link rel="icon" type="image/svg+xml" href="assets/images/logo/heart-logo.svg">
  
  <!-- High-Fashion Typography: Bodoni Moda, Playfair Display, Plus Jakarta Sans, Newsreader -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900&family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400;1,6..72,600&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  
  <!-- Main Stylesheet -->
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <!-- Reading Progress Bar -->
  <div class="reading-progress-bar" id="readingProgressBar"></div>

  <!-- Offline Status Banner -->
  <div class="offline-indicator-banner" id="offlineBanner">
    <i class="fas fa-wifi-slash"></i>
    <span>Chế độ ngoại tuyến: Bạn đang đọc các bài viết đã lưu đệm. Hệ thống sẽ tự động cập nhật khi có mạng.</span>
  </div>

  <!-- =================================================================
       1. ACADEMIC ATTRIBUTION & UTILITY BAR
       ================================================================= -->
  <div class="fashion-academic-bar">
    <div class="container fashion-academic-container">
      <div class="academic-tag-pill">
        <i class="fas fa-graduation-cap"></i>
        <span>Trường Đại học Ngoại ngữ - Đại học Quốc gia Hà Nội (ULIS - VNU) • Lớp 6 - Nhóm 1 - Khóa 127 • BCTT</span>
      </div>
      <div class="top-utility-right">
        <span class="date-widget" id="liveDateWidget"><i class="far fa-calendar-alt"></i> Đang tải ngày...</span>
      </div>
    </div>
  </div>

  <!-- =================================================================
       2. BRAND MASTHEAD (HIGH-FASHION EDITORIAL HEADER)
       ================================================================= -->
  <header class="fashion-header">
    <div class="container fashion-header-container">
      <!-- 1. Brand Logo: HEARTICLES. with Didone Italic & Dot -->
      <a href="javascript:void(0)" class="fashion-brand-logo" onclick="filterByCategory('all')">
        HEARTICLES<span class="fashion-brand-period">.</span>
      </a>

      <!-- 2. Minimalist Fashion Navigation -->
      <nav class="fashion-nav" aria-label="Thanh điều hướng tạp chí">
        <a href="javascript:void(0)" class="nav-item active" data-category="all" onclick="filterByCategory('all')">Home</a>
        <a href="javascript:void(0)" class="nav-item" data-category="trending" onclick="filterByCategory('trending')">Trending</a>
        <a href="javascript:void(0)" class="nav-item nav-item-her" data-category="her" onclick="filterByCategory('her')">
          Her <span class="nav-badge-dot"></span>
        </a>
        <a href="javascript:void(0)" class="nav-item" data-category="society" onclick="filterByCategory('society')">Society</a>
        <a href="javascript:void(0)" class="nav-item" data-category="mind-soul" onclick="filterByCategory('mind-soul')">Mind &amp; Soul</a>
        <a href="javascript:void(0)" class="nav-item" data-category="human-stories" onclick="filterByCategory('human-stories')">Human Stories</a>
        <a href="#about-us" class="nav-item" data-category="about">About Us</a>
      </nav>

      <!-- 3. Actions: Search, Subscribe Pill, Mobile Drawer Toggle -->
      <div class="fashion-header-actions">
        <button class="fashion-search-btn" onclick="openSearchModal()" title="Tìm kiếm bài viết (/)" aria-label="Tìm kiếm">
          <i class="fas fa-search"></i>
        </button>
        <button class="fashion-subscribe-btn" onclick="openSubscribeModal()" title="Đăng ký nhận bản tin">
          Subscribe
        </button>
        <button class="fashion-hamburger-btn" onclick="openDrawer()" aria-label="Mở menu chuyển trang">
          <i class="fas fa-bars"></i>
        </button>
      </div>
    </div>
  </header>

  <!-- =================================================================
       MAIN CONTENT CONTAINER
       ================================================================= -->
  <main class="container" style="flex-grow: 1;">

    <!-- ===============================================================
         3. HERO BENTO GRID: COVER STORY + THE LATEST
         Directly matching the official fashion magazine mockup
         =============================================================== -->
    <section class="fashion-hero-grid">
      <!-- Left: Giant Cover Story Card -->
      <article class="fashion-cover-card" onclick="openArticleModal('cover-story-her')">
        <div class="fashion-cover-text">
          <div class="fashion-kicker-row">
            <span class="fashion-kicker">COVER STORY · HER</span>
            <svg class="fashion-doodle-heart" viewBox="0 0 32 30" fill="none">
              <path d="M16 26C15 25 3 17 3 9C3 4.5 6.5 2 10.5 2C13.5 2 15 3.5 16 5.5C17 3.5 18.5 2 21.5 2C25.5 2 29 4.5 29 9C29 17 17 25 16 26Z" stroke="#BA6975" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <h1 class="fashion-headline">
            More Than Just<br>
            a Pretty Face:<br>
            <span class="fashion-italic">Redefining Beauty in the Gen Z Era</span>
          </h1>
          <p class="fashion-excerpt">
            Why are young women still expected to fit into society's definition of beauty?
          </p>
          <div class="fashion-action-row">
            <button class="fashion-btn-pill" onclick="event.stopPropagation(); openArticleModal('cover-story-her');">
              Read the story &rarr;
            </button>
            <span class="fashion-meta-pill">6 min read</span>
          </div>
        </div>
        <div class="fashion-cover-media">
          <img src="assets/images/editorial/hd_cover_girl_portrait.jpg" alt="More Than Just a Pretty Face" class="fashion-cover-image">
        </div>
      </article>

      <!-- Right: THE LATEST. Column -->
      <aside class="fashion-latest-card">
        <div class="fashion-latest-header">
          <h2 class="fashion-latest-title">THE LATEST.</h2>
          <a href="javascript:void(0)" onclick="filterByCategory('all')" class="fashion-view-all">View all &rarr;</a>
        </div>
        <div class="fashion-latest-list">
          <!-- Item 1: Trending -->
          <div class="fashion-latest-item" onclick="openArticleModal('latest-loneliness')">
            <div class="latest-thumb-wrap">
              <img src="assets/images/editorial/hd_thumb_loneliness.jpg" alt="The Loneliness Behind the Likes" class="latest-thumb-img">
            </div>
            <div class="latest-content">
              <span class="latest-kicker">TRENDING</span>
              <h3 class="latest-title">The Loneliness Behind the Likes</h3>
              <span class="latest-meta">4 min read</span>
            </div>
          </div>
          <!-- Item 2: Human Stories -->
          <div class="fashion-latest-item" onclick="openArticleModal('latest-small-acts')">
            <div class="latest-thumb-wrap">
              <img src="assets/images/editorial/hd_thumb_small_acts.jpg" alt="Small Acts, Big Changes" class="latest-thumb-img">
            </div>
            <div class="latest-content">
              <span class="latest-kicker">HUMAN STORIES</span>
              <h3 class="latest-title">Small Acts, Big Changes</h3>
              <span class="latest-meta">5 min read</span>
            </div>
          </div>
          <!-- Item 3: Mind & Soul -->
          <div class="fashion-latest-item" onclick="openArticleModal('latest-hurry')">
            <div class="latest-thumb-wrap">
              <img src="assets/images/editorial/thumb_sunset_exact.jpg" alt="Why Are We Always in a Hurry?" class="latest-thumb-img">
            </div>
            <div class="latest-content">
              <span class="latest-kicker">MIND &amp; SOUL</span>
              <h3 class="latest-title">Why Are We Always in a Hurry?</h3>
              <span class="latest-meta">7 min read</span>
            </div>
          </div>
        </div>
      </aside>
    </section>

    <!-- ===============================================================
         4. SECONDARY CURATED BENTO ROW (3 FEATURE CARDS)
         =============================================================== -->
    <section class="fashion-feature-row">
      <!-- Card 1: WHAT'S THE BUZZ? -->
      <div class="fashion-bento-card bento-buzz" onclick="filterByCategory('trending')">
        <div class="bento-text">
          <span class="bento-kicker">WHAT'S THE BUZZ?</span>
          <p class="bento-sub">The conversations everyone is having right now.</p>
        </div>
        <div class="bento-media">
          <img src="assets/images/editorial/hd_buzz_girls.jpg" alt="What's the buzz?" class="bento-img">
        </div>
      </div>

      <!-- Card 2: HER VOICE. HER STORY. -->
      <div class="fashion-bento-card bento-her-voice" onclick="openArticleModal('feature-she-definition')">
        <div class="bento-text">
          <span class="bento-kicker">HER VOICE. HER STORY.</span>
          <h3 class="bento-headline">She Is Not Your Definition of Her.</h3>
          <p class="bento-excerpt">A space for women to speak, question and redefine their own stories.</p>
          <a href="javascript:void(0)" class="bento-arrow-link" onclick="event.stopPropagation(); filterByCategory('her');">
            EXPLORE HER &rarr;
          </a>
        </div>
        <div class="bento-media">
          <img src="assets/images/editorial/hd_her_walking.jpg" alt="Her Voice Her Story" class="bento-img-square">
        </div>
      </div>

      <!-- Card 3: A LITTLE MORE HUMAN. -->
      <div class="fashion-bento-card bento-human" onclick="filterByCategory('human-stories')">
        <div class="bento-text">
          <span class="bento-kicker">A LITTLE MORE HUMAN.</span>
          <h3 class="bento-headline">The World Needs More Kindness.</h3>
          <svg class="bento-doodle-heart" viewBox="0 0 32 30" fill="none">
            <path d="M16 26C15 25 3 17 3 9C3 4.5 6.5 2 10.5 2C13.5 2 15 3.5 16 5.5C17 3.5 18.5 2 21.5 2C25.5 2 29 4.5 29 9C29 17 17 25 16 26Z" stroke="#BA6975" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <div class="bento-media">
          <img src="assets/images/editorial/hd_human_cat.jpg" alt="The World Needs More Kindness" class="bento-img">
        </div>
      </div>
    </section>

    <!-- ===============================================================
         5. MULTIMEDIA & VIDEO PHÓNG SỰ HUB (5 Video Clips Requirement)
         =============================================================== -->
    <section class="video-hub-section" id="videoHubSection">
      <div class="video-hub-header">
        <h2 class="video-hub-title"><i class="fas fa-play-circle" style="color:var(--color-brand-primary);"></i> MULTIMEDIA &amp; VIDEO HUB</h2>
        <span class="video-hub-badge">5 Chuyên đề video phóng sự đa phương tiện</span>
      </div>
      <div id="videoHubContent">
        <!-- Rendered dynamically by app.js -->
      </div>
    </section>

    <!-- ===============================================================
         6. THE EDITORIAL JOURNAL (Full 39-Article Curated Magazine Grid)
         =============================================================== -->
    <section class="fashion-journal-section" id="journalSection">
      <div class="fashion-section-divider">
        <div class="fashion-section-title-wrap">
          <h2 class="fashion-section-main-title">THE JOURNAL.</h2>
          <span class="fashion-section-sub">Tuyển tập phóng sự và bài viết đa chiều</span>
        </div>
        <div class="fashion-filter-pills" id="categoryFilterPills">
          <button class="fashion-filter-pill active" onclick="filterByCategory('all')">✦ Tất cả bài viết</button>
          <button class="fashion-filter-pill" onclick="filterByCategory('trending')">Trending</button>
          <button class="fashion-filter-pill" onclick="filterByCategory('her')">Her (Phụ nữ &amp; Bản sắc)</button>
          <button class="fashion-filter-pill" onclick="filterByCategory('society')">Society</button>
          <button class="fashion-filter-pill" onclick="filterByCategory('mind-soul')">Mind &amp; Soul</button>
          <button class="fashion-filter-pill" onclick="filterByCategory('human-stories')">Human Stories</button>
          <button class="fashion-filter-pill" onclick="filterByCategory('in-depth')">In-depth</button>
        </div>
      </div>

      <!-- Articles Grid rendered by app.js -->
      <div class="fashion-articles-grid" id="fashionArticlesGrid">
        <!-- Injected dynamically by app.js -->
      </div>
    </section>

    <!-- ===============================================================
         7. INTERACTIVE POLL & RADIO BÁO NÓI
         =============================================================== -->
    <section class="interactive-feature-strip">
      <!-- Interactive Reader Poll -->
      <div class="poll-box">
        <div class="poll-badge"><i class="fas fa-poll"></i> GÓC NHÌN BẠN ĐỌC</div>
        <h3 class="poll-question">Theo bạn, các trường đại học và cơ quan truyền thông nên tôn vinh và khuyến khích tiếng nói của nữ giới trẻ như thế nào để kiến tạo một xã hội nhân văn, bình đẳng?</h3>
        <div class="poll-options" id="pollContainer">
          <button class="poll-option-btn" onclick="votePoll(1)">
            <span>1. Tạo nhiều diễn đàn văn hóa và học thuật chuyên sâu</span>
            <i class="far fa-circle"></i>
          </button>
          <button class="poll-option-btn" onclick="votePoll(2)">
            <span>2. Tôn vinh vẻ đẹp trí tuệ, lòng trắc ẩn và cá tính độc bản</span>
            <i class="far fa-circle"></i>
          </button>
          <button class="poll-option-btn" onclick="votePoll(3)">
            <span>3. Xây dựng môi trường bình đẳng không phán xét ngoại hình</span>
            <i class="far fa-circle"></i>
          </button>
        </div>
      </div>

      <!-- Audio Podcast Box -->
      <div class="podcast-box">
        <div>
          <span class="podcast-header-tag"><i class="fas fa-podcast"></i> RADIO BÁO NÓI</span>
          <h3 class="podcast-title">Tạp chí Radio: "Nơi lòng tốt bắt đầu từ những người xa lạ"</h3>
          <p style="font-size:0.875rem; color:#E5D0D0; line-height:1.5;">Số phát thanh đặc biệt tuần này phát sóng câu chuyện chiếc ví đánh rơi 1.000 USD và hành trình trả lại nghìn dặm tại nước Úc.</p>
        </div>
        <div class="podcast-player-control">
          <button class="btn-podcast-play" onclick="alert('Đang phát số Radio Podcast tuần này...')"><i class="fas fa-play"></i></button>
          <div class="podcast-progress-bar">
            <div class="podcast-progress-fill"></div>
          </div>
          <span style="font-size:0.75rem; color:#D3C0C0;">14:28 / 32:00</span>
        </div>
      </div>
    </section>

    <!-- ===============================================================
         8. ABOUT US SECTION (ULIS - VNU Editorial Manifesto)
         =============================================================== -->
    <div id="aboutUsSection">
      <!-- Rendered by app.js -->
    </div>
  </main>

  <!-- =================================================================
       9. HIGH-FASHION EDITORIAL FOOTER WITH SKETCH HEART
       ================================================================= -->
  <footer class="fashion-footer">
    <div class="container">
      <div class="fashion-footer-container">
        <div class="fashion-footer-brand">
          <span class="fashion-footer-logo">HEARTICLES<span class="fashion-brand-period">.</span></span>
          <p class="fashion-footer-desc">Tòa soạn Tạp chí Báo điện tử Đa phương tiện • Trường Đại học Ngoại ngữ - Đại học Quốc gia Hà Nội (ULIS - VNU)</p>
          <p class="fashion-footer-group">Lớp 6 - Nhóm 1 - Khóa 127 • Khoa Ngôn ngữ &amp; Truyền thông • Học phần Báo chí &amp; Truyền thông (BCTT)</p>
          <p style="font-size:0.8125rem; color:var(--color-brand-primary); font-weight:600; margin-top:0.4rem;">
            class6group1term127@gmail.com
          </p>
        </div>
        <div class="fashion-footer-slogan-wrap">
          <svg class="fashion-slogan-heart" viewBox="0 0 100 80" fill="none">
            <path d="M30 45 C15 32 8 20 22 10 C32 2 44 8 50 20 C56 8 68 2 78 10 C92 20 82 36 62 55 C54 62 50 67 48 68 C45 70 42 68 40 65 C34 58 26 48 30 45 Z" stroke="#591724" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M48 68 C56 72 70 75 80 70 C88 66 94 58 98 50" stroke="#BA6975" stroke-width="2" stroke-linecap="round" stroke-dasharray="3 4"/>
          </svg>
          <span class="fashion-slogan-text">Stories that speak to the heart.</span>
        </div>
      </div>
      <div class="fashion-footer-bottom">
        <span>&copy; 2026 HEARTICLES. Mọi quyền được bảo lưu. Xuất bản bởi Nhóm 1 Lớp 6 Khóa 127, ULIS - VNU.</span>
        <span>Thiết kế theo quy chuẩn Vogue, Kinfolk &amp; Nielsen Norman UX.</span>
      </div>
    </div>
  </footer>

  <!-- =================================================================
       10. OFFCANVAS DRAWER MENU (Mobile Menu)
       ================================================================= -->
  <div class="drawer-backdrop" id="drawerBackdrop" onclick="closeDrawer()"></div>
  <aside class="offcanvas-drawer" id="offcanvasDrawer" aria-label="Menu mở rộng">
    <div class="drawer-header">
      <div class="brand-title" style="color:#FFF; font-family:var(--font-editorial); font-size:1.6rem; font-style:italic;">
        HEARTICLES<span style="color:var(--color-brand-accent);">.</span>
      </div>
      <button onclick="closeDrawer()" style="color:#FFF; font-size:1.5rem;" aria-label="Đóng menu"><i class="fas fa-times"></i></button>
    </div>
    <nav class="drawer-links-list">
      <a href="javascript:void(0)" class="drawer-link" onclick="filterByCategory('all')"><i class="fas fa-home"></i> Home</a>
      <a href="javascript:void(0)" class="drawer-link" onclick="filterByCategory('trending')"><i class="fas fa-fire"></i> Trending</a>
      <a href="javascript:void(0)" class="drawer-link" onclick="filterByCategory('her')"><i class="fas fa-venus"></i> Her (Phụ nữ &amp; Bản sắc)</a>
      <a href="javascript:void(0)" class="drawer-link" onclick="filterByCategory('society')"><i class="fas fa-globe-asia"></i> Society</a>
      <a href="javascript:void(0)" class="drawer-link" onclick="filterByCategory('mind-soul')"><i class="fas fa-spa"></i> Mind &amp; Soul</a>
      <a href="javascript:void(0)" class="drawer-link" onclick="filterByCategory('human-stories')"><i class="fas fa-heart"></i> Human Stories</a>
      <a href="javascript:void(0)" class="drawer-link" onclick="filterByCategory('in-depth')"><i class="fas fa-feather-alt"></i> In-depth</a>
      <a href="javascript:void(0)" class="drawer-link" onclick="filterByCategory('about')"><i class="fas fa-info-circle"></i> About us</a>
    </nav>
    <div style="margin-top:auto; padding-top:1.5rem; border-top:1px solid #332B25;">
      <p style="font-size:0.75rem; color:#A99F94;">Tòa soạn ULIS - VNU:</p>
      <p style="font-size:0.875rem; color:#FFB3B3; font-weight:600;">class6group1term127@gmail.com</p>
    </div>
  </aside>

  <!-- =================================================================
       11. ARTICLE READER MODAL (Full Reading Suite with TTS)
       ================================================================= -->
  <div class="article-modal-backdrop" id="articleReaderModal">
    <div class="article-modal-container">
      <button class="article-modal-close-btn" onclick="closeArticleModal()" aria-label="Đóng bài viết">
        <i class="fas fa-times"></i>
      </button>
      <div id="articleModalBody">
        <!-- Injected dynamically by app.js -->
      </div>
    </div>
  </div>

  <!-- =================================================================
       12. SEARCH MODAL (Instant Live Search)
       ================================================================= -->
  <div class="search-modal" id="searchModal" onclick="if(event.target === this) closeSearchModal()">
    <div class="search-modal-box">
      <div class="search-input-wrap">
        <i class="fas fa-search" style="color:var(--color-brand-primary); font-size:1.25rem;"></i>
        <input type="text" class="search-input-field" id="searchInput" placeholder="Tìm kiếm bài viết, tác giả, chuyên mục..." oninput="handleSearchInput(this.value)">
        <button onclick="closeSearchModal()" style="font-size:1.25rem; color:var(--color-text-muted);"><i class="fas fa-times"></i></button>
      </div>
      <div class="search-results-list" id="searchResults">
        <p style="color:var(--color-text-muted); font-size:0.9rem;">Nhập từ khóa để tìm kiếm trong 39+ bài viết...</p>
      </div>
    </div>
  </div>

  <!-- =================================================================
       13. ONBOARDING MODAL (3-Step First-Time Reader Walkthrough)
       ================================================================= -->
  <div class="onboard-modal-backdrop" id="onboardModal" onclick="if(event.target === this) closeOnboardingModal()">
    <div class="onboard-card">
      <div class="onboard-steps-progress">
        <span class="onboard-step-dot active"></span>
        <span class="onboard-step-dot"></span>
        <span class="onboard-step-dot"></span>
      </div>
      <div id="onboardStepContent">
        <!-- Rendered dynamically by app.js -->
      </div>
      <div class="onboard-action-row">
        <button class="btn-text-skip" onclick="closeOnboardingModal()">Bỏ qua</button>
        <button class="btn-onboard-next" id="onboardBtnNext" onclick="nextOnboardStep()">Tiếp tục</button>
      </div>
    </div>
  </div>

  <!-- =================================================================
       14. KEYBOARD SHORTCUTS MODAL
       ================================================================= -->
  <div class="shortcuts-modal" id="shortcutsModal" onclick="if(event.target === this) closeShortcutsModal()">
    <div class="shortcuts-card">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.25rem;">
        <h3 style="font-family:var(--font-editorial); font-size:1.35rem; font-weight:700; color:var(--color-text-headline);">
          <i class="fas fa-keyboard" style="color:var(--color-brand-primary); margin-right:0.5rem;"></i> Phím tắt hệ thống
        </h3>
        <button onclick="closeShortcutsModal()" style="color:var(--color-text-muted); font-size:1.25rem;" aria-label="Đóng phím tắt"><i class="fas fa-times"></i></button>
      </div>
      <div class="shortcut-row">
        <span>Mở ô tìm kiếm nhanh trong toàn bộ 39 bài viết</span>
        <kbd class="shortcut-key">/</kbd>
      </div>
      <div class="shortcut-row">
        <span>Đóng bài đọc / Đóng hộp thoại đang mở</span>
        <kbd class="shortcut-key">ESC</kbd>
      </div>
      <div class="shortcut-row">
        <span>Tăng / Giảm cỡ chữ đọc bài (Zoom Text)</span>
        <kbd class="shortcut-key">T</kbd>
      </div>
      <div class="shortcut-row">
        <span>Xem bảng danh sách phím tắt</span>
        <kbd class="shortcut-key">?</kbd>
      </div>
      <div style="margin-top:1.25rem; font-size:0.75rem; color:var(--color-text-muted); text-align:center;">
        Nhấn <kbd class="shortcut-key">ESC</kbd> hoặc click ra ngoài để đóng.
      </div>
    </div>
  </div>

  <!-- =================================================================
       15. MOBILE BOTTOM DOCK (Mobile < 768px Touch Navigation)
       ================================================================= -->
  <nav class="mobile-bottom-dock" aria-label="Điều hướng nhanh trên di động">
    <a href="javascript:void(0)" class="dock-btn" onclick="filterByCategory('all')">
      <i class="fas fa-home"></i>
      <span>Trang chủ</span>
    </a>
    <a href="javascript:void(0)" class="dock-btn" onclick="filterByCategory('trending')">
      <i class="fas fa-fire"></i>
      <span>Trending</span>
    </a>
    <a href="javascript:void(0)" class="dock-btn" onclick="filterByCategory('her')">
      <i class="fas fa-venus"></i>
      <span>Her</span>
    </a>
    <a href="javascript:void(0)" class="dock-btn" onclick="openSearchModal()">
      <i class="fas fa-search"></i>
      <span>Tìm kiếm</span>
    </a>
    <a href="javascript:void(0)" class="dock-btn" onclick="openDrawer()">
      <i class="fas fa-bars"></i>
      <span>Menu</span>
    </a>
  </nav>

  <!-- Scripts -->
  <script src="js/data.js"></script>
  <script src="js/app.js"></script>
</body>
</html>
"""

with open(r"c:\Users\camka\OneDrive\Desktop\BCTT\index.html", "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print("index.html written successfully with Fashion Magazine structure!")
