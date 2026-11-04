# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/build_multi_pages.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update get_header to include language selector on bar and data-i18n
head_old = """def get_header(active_key):
    nav_items = [
        ("index.html", "all", "Home"),
        ("trending.html", "trending", "Trending"),
        ("society.html", "society", "Society"),
        ("human-stories.html", "human-stories", "Human Stories"),
        ("mind-soul.html", "mind-soul", "Mind & Soul"),
        ("in-depth.html", "in-depth", "In-depth"),
        ("about.html", "about", "About Us")
    ]
    
    nav_html = ""
    for href, key, label in nav_items:
        is_active = "active" if key == active_key else ""
        nav_html += f'        <a href="{href}" class="nav-item {is_active}">{label}</a>\\n'

    return f\"\"\"  <!-- Reading Progress Bar -->
  <div class="reading-progress-bar" id="readingProgressBar"></div>

  <!-- Offline Status Banner -->
  <div class="offline-indicator-banner" id="offlineBanner">
    <i class="fas fa-wifi-slash"></i>
    <span>Chế độ ngoại tuyến: Bạn đang đọc các bài viết đã lưu đệm. Hệ thống sẽ tự động cập nhật khi có mạng.</span>
  </div>

  <!-- =================================================================
       1. ACADEMIC ATTRIBUTION & UTILITY BAR (ULIS - VNU)
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
       2. BRAND MASTHEAD (HIGH-CONTRAST EDITORIAL HEADER)
       ================================================================= -->
  <header class="fashion-header">
    <div class="container fashion-header-container">
      <!-- 1. Brand Logo: HEARTICLES. with Didone Italic & Dot -->
      <a href="index.html" class="fashion-brand-logo">
        HEARTICLES<span class="fashion-brand-period">.</span>
      </a>

      <!-- 2. Minimalist Fashion Navigation with Active Burgundy Underline -->
      <nav class="fashion-nav" aria-label="Thanh điều hướng tạp chí">
{nav_html}      </nav>

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
\"\"\""""

head_new = """def get_header(active_key):
    nav_items = [
        ("index.html", "all", "Home", "nav_home"),
        ("trending.html", "trending", "Trending", "nav_trending"),
        ("society.html", "society", "Society", "nav_society"),
        ("human-stories.html", "human-stories", "Human Stories", "nav_human_stories"),
        ("mind-soul.html", "mind-soul", "Mind & Soul", "nav_mind_soul"),
        ("in-depth.html", "in-depth", "In-depth", "nav_indepth"),
        ("about.html", "about", "About Us", "nav_about")
    ]
    
    nav_html = ""
    for href, key, label, i18n_key in nav_items:
        is_active = "active" if key == active_key else ""
        nav_html += f'        <a href="{href}" class="nav-item {is_active}" data-i18n="{i18n_key}">{label}</a>\\n'

    return f\"\"\"  <!-- Reading Progress Bar -->
  <div class="reading-progress-bar" id="readingProgressBar"></div>

  <!-- Offline Status Banner -->
  <div class="offline-indicator-banner" id="offlineBanner" data-i18n="offline_banner">
    <i class="fas fa-wifi-slash"></i>
    <span>Chế độ ngoại tuyến: Bạn đang đọc các bài viết đã lưu đệm. Hệ thống sẽ tự động cập nhật khi có mạng.</span>
  </div>

  <!-- =================================================================
       1. ACADEMIC ATTRIBUTION & UTILITY BAR (ULIS - VNU)
       ================================================================= -->
  <div class="fashion-academic-bar">
    <div class="container fashion-academic-container">
      <div class="academic-tag-pill" data-i18n="academic_text">
        <i class="fas fa-graduation-cap"></i>
        <span>Trường Đại học Ngoại ngữ - Đại học Quốc gia Hà Nội (ULIS - VNU) • Lớp 6 - Nhóm 1 - Khóa 127 • BCTT</span>
      </div>
      <div class="top-utility-right">
        <!-- Language Switcher Pill in Top Bar -->
        <div class="lang-switch-pill" role="group" aria-label="Language Selector">
          <button class="lang-pill-btn active" data-lang="vi" onclick="setLanguage('vi')">VI</button>
          <span class="lang-pill-divider">/</span>
          <button class="lang-pill-btn" data-lang="en" onclick="setLanguage('en')">EN</button>
        </div>
        <span class="date-widget" id="liveDateWidget"><i class="far fa-calendar-alt"></i> Đang tải ngày...</span>
      </div>
    </div>
  </div>

  <!-- =================================================================
       2. BRAND MASTHEAD (HIGH-CONTRAST EDITORIAL HEADER)
       ================================================================= -->
  <header class="fashion-header">
    <div class="container fashion-header-container">
      <!-- 1. Brand Logo: HEARTICLES. with Didone Italic & Dot -->
      <a href="index.html" class="fashion-brand-logo">
        HEARTICLES<span class="fashion-brand-period">.</span>
      </a>

      <!-- 2. Minimalist Fashion Navigation with Active Burgundy Underline -->
      <nav class="fashion-nav" aria-label="Thanh điều hướng tạp chí">
{nav_html}      </nav>

      <!-- 3. Actions: Language Switcher, Search, Subscribe Pill, Mobile Drawer Toggle -->
      <div class="fashion-header-actions">
        <!-- Primary language toggle button on the bar -->
        <div class="lang-switch-pill" role="group" aria-label="Language Selector">
          <button class="lang-pill-btn active" data-lang="vi" onclick="setLanguage('vi')">VI</button>
          <span class="lang-pill-divider">/</span>
          <button class="lang-pill-btn" data-lang="en" onclick="setLanguage('en')">EN</button>
        </div>
        <button class="fashion-search-btn" onclick="openSearchModal()" title="Tìm kiếm bài viết (/)" aria-label="Tìm kiếm" data-i18n-title="search_tooltip">
          <i class="fas fa-search"></i>
        </button>
        <button class="fashion-subscribe-btn" onclick="openSubscribeModal()" title="Đăng ký nhận bản tin" data-i18n="btn_subscribe">
          Subscribe
        </button>
        <button class="fashion-hamburger-btn" onclick="openDrawer()" aria-label="Mở menu chuyển trang">
          <i class="fas fa-bars"></i>
        </button>
      </div>
    </div>
  </header>
\"\"\""""

# 2. Update get_footer to include translations.js and drawer language selector
foot_old = """  <!-- OFFCANVAS DRAWER MENU -->
  <div class="drawer-backdrop" id="drawerBackdrop" onclick="closeDrawer()"></div>
  <aside class="offcanvas-drawer" id="offcanvasDrawer" aria-label="Menu mở rộng">
    <div class="drawer-header">
      <div class="brand-title" style="color:#FFF; font-family:var(--font-editorial); font-size:1.6rem; font-weight:900; letter-spacing:-0.03em;">
        HEARTICLES<span style="color:var(--color-brand-accent);">.</span>
      </div>
      <button onclick="closeDrawer()" style="color:#FFF; font-size:1.5rem;" aria-label="Đóng menu"><i class="fas fa-times"></i></button>
    </div>
    <nav class="drawer-links-list">
      <a href="index.html" class="drawer-link"><i class="fas fa-home"></i> Home</a>
      <a href="trending.html" class="drawer-link"><i class="fas fa-fire"></i> Trending</a>
      <a href="society.html" class="drawer-link"><i class="fas fa-globe-asia"></i> Society</a>
      <a href="human-stories.html" class="drawer-link"><i class="fas fa-heart"></i> Human Stories</a>
      <a href="mind-soul.html" class="drawer-link"><i class="fas fa-spa"></i> Mind &amp; Soul</a>
      <a href="in-depth.html" class="drawer-link"><i class="fas fa-feather-alt"></i> In-depth</a>
      <a href="about.html" class="drawer-link"><i class="fas fa-info-circle"></i> About us</a>
    </nav>
    <div style="margin-top:auto; padding-top:1.5rem; border-top:1px solid #332B25;">
      <p style="font-size:0.8125rem; color:#E2D8D4; font-weight:600;">Tòa soạn ULIS - VNU:</p>
      <p style="font-size:0.925rem; color:#FFFFFF; font-weight:700;">class6group1term127@gmail.com</p>
    </div>
  </aside>"""

foot_new = """  <!-- OFFCANVAS DRAWER MENU -->
  <div class="drawer-backdrop" id="drawerBackdrop" onclick="closeDrawer()"></div>
  <aside class="offcanvas-drawer" id="offcanvasDrawer" aria-label="Menu mở rộng">
    <div class="drawer-header">
      <div class="brand-title" style="color:#FFF; font-family:var(--font-editorial); font-size:1.6rem; font-weight:900; letter-spacing:-0.03em;">
        HEARTICLES<span style="color:var(--color-brand-accent);">.</span>
      </div>
      <button onclick="closeDrawer()" style="color:#FFF; font-size:1.5rem;" aria-label="Đóng menu"><i class="fas fa-times"></i></button>
    </div>

    <!-- Drawer Language Selector Row -->
    <div class="drawer-lang-row" style="display:flex; align-items:center; justify-content:space-between; padding:0.75rem 1rem; margin-bottom:1rem; background:rgba(255,255,255,0.06); border-radius:8px;">
      <span style="font-size:0.875rem; color:#E2D8D4; font-weight:600;"><i class="fas fa-globe" style="margin-right:0.4rem; color:var(--color-brand-accent);"></i> Ngôn ngữ / Language:</span>
      <div class="lang-switch-pill" role="group" aria-label="Language Selector">
        <button class="lang-pill-btn active" data-lang="vi" onclick="setLanguage('vi')">VI</button>
        <span class="lang-pill-divider">/</span>
        <button class="lang-pill-btn" data-lang="en" onclick="setLanguage('en')">EN</button>
      </div>
    </div>

    <nav class="drawer-links-list">
      <a href="index.html" class="drawer-link" data-i18n="nav_home"><i class="fas fa-home"></i> Home</a>
      <a href="trending.html" class="drawer-link" data-i18n="nav_trending"><i class="fas fa-fire"></i> Trending</a>
      <a href="society.html" class="drawer-link" data-i18n="nav_society"><i class="fas fa-globe-asia"></i> Society</a>
      <a href="human-stories.html" class="drawer-link" data-i18n="nav_human_stories"><i class="fas fa-heart"></i> Human Stories</a>
      <a href="mind-soul.html" class="drawer-link" data-i18n="nav_mind_soul"><i class="fas fa-spa"></i> Mind &amp; Soul</a>
      <a href="in-depth.html" class="drawer-link" data-i18n="nav_indepth"><i class="fas fa-feather-alt"></i> In-depth</a>
      <a href="about.html" class="drawer-link" data-i18n="nav_about"><i class="fas fa-info-circle"></i> About us</a>
    </nav>
    <div style="margin-top:auto; padding-top:1.5rem; border-top:1px solid #332B25;">
      <p style="font-size:0.8125rem; color:#E2D8D4; font-weight:600;">Tòa soạn ULIS - VNU:</p>
      <p style="font-size:0.925rem; color:#FFFFFF; font-weight:700;">class6group1term127@gmail.com</p>
    </div>
  </aside>"""

# 3. Update footer scripts
scripts_old = """  <!-- Scripts -->
  <script src="js/data.js"></script>
  <script src="js/app.js"></script>"""

scripts_new = """  <!-- Scripts: translations.js loaded first -->
  <script src="js/translations.js"></script>
  <script src="js/data.js"></script>
  <script src="js/app.js"></script>"""

# 4. Update footer paragraphs
footer_p_old = """        <div class="fashion-footer-brand">
          <span class="fashion-footer-logo">HEARTICLES<span class="fashion-brand-period">.</span></span>
          <p class="fashion-footer-desc">Tòa soạn Tạp chí Báo điện tử Đa phương tiện • Trường Đại học Ngoại ngữ - Đại học Quốc gia Hà Nội (ULIS - VNU)</p>
          <p class="fashion-footer-group">Lớp 6 - Nhóm 1 - Khóa 127 • Khoa Ngôn ngữ &amp; Truyền thông • Học phần Báo chí &amp; Truyền thông (BCTT)</p>"""

footer_p_new = """        <div class="fashion-footer-brand">
          <span class="fashion-footer-logo">HEARTICLES<span class="fashion-brand-period">.</span></span>
          <p class="fashion-footer-desc" data-i18n="footer_desc">Tòa soạn Tạp chí Báo điện tử Đa phương tiện • Trường Đại học Ngoại ngữ - Đại học Quốc gia Hà Nội (ULIS - VNU)</p>
          <p class="fashion-footer-group" data-i18n="footer_group">Lớp 6 - Nhóm 1 - Khóa 127 • Khoa Ngôn ngữ &amp; Truyền thông • Học phần Báo chí &amp; Truyền thông (BCTT)</p>"""

footer_bot_old = """      <div class="fashion-footer-bottom">
        <span>&copy; 2026 HEARTICLES. Mọi quyền được bảo lưu. Xuất bản bởi Nhóm 1 Lớp 6 Khóa 127, ULIS - VNU.</span>
        <span>Mô hình tòa soạn Báo Nhân Dân điện tử (nhandan.vn) kết hợp tiêu chuẩn Nielsen Norman UX.</span>
      </div>"""

footer_bot_new = """      <div class="fashion-footer-bottom">
        <span data-i18n="footer_copy">&copy; 2026 HEARTICLES. Mọi quyền được bảo lưu. Xuất bản bởi Nhóm 1 Lớp 6 Khóa 127, ULIS - VNU.</span>
        <span data-i18n="footer_model">Mô hình tòa soạn Báo Nhân Dân điện tử (nhandan.vn) kết hợp tiêu chuẩn Nielsen Norman UX.</span>
      </div>"""

# 5. Update search input
search_in_old = """<input type="text" class="search-input-field" id="searchInput" placeholder="Tìm kiếm bài viết, tác giả, chuyên mục..." oninput="handleSearchInput(this.value)">"""
search_in_new = """<input type="text" class="search-input-field" id="searchInput" placeholder="Tìm kiếm bài viết, tác giả, chuyên mục..." data-i18n-placeholder="search_placeholder" oninput="handleSearchInput(this.value)">"""

# 6. Update shortcuts modal
short_old = """      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.25rem;">
        <h3 style="font-family:var(--font-editorial); font-size:1.35rem; font-weight:700; color:var(--color-text-headline);">
          <i class="fas fa-keyboard" style="color:var(--color-brand-primary); margin-right:0.5rem;"></i> Phím tắt hệ thống
        </h3>
        <button onclick="closeShortcutsModal()" style="color:var(--color-text-muted); font-size:1.25rem;" aria-label="Đóng phím tắt"><i class="fas fa-times"></i></button>
      </div>
      <div class="shortcut-row">
        <span>Mở ô tìm kiếm nhanh</span>
        <kbd class="shortcut-key">/</kbd>
      </div>
      <div class="shortcut-row">
        <span>Đóng bài đọc / Đóng hộp thoại</span>
        <kbd class="shortcut-key">ESC</kbd>
      </div>
      <div class="shortcut-row">
        <span>Tăng / Giảm cỡ chữ đọc bài (Zoom Text)</span>
        <kbd class="shortcut-key">T</kbd>
      </div>
      <div class="shortcut-row">
        <span>Xem bảng danh sách phím tắt</span>
        <kbd class="shortcut-key">?</kbd>
      </div>"""

short_new = """      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.25rem;">
        <h3 style="font-family:var(--font-editorial); font-size:1.35rem; font-weight:700; color:var(--color-text-headline);" data-i18n="shortcuts_title">
          <i class="fas fa-keyboard" style="color:var(--color-brand-primary); margin-right:0.5rem;"></i> Phím tắt hệ thống
        </h3>
        <button onclick="closeShortcutsModal()" style="color:var(--color-text-muted); font-size:1.25rem;" aria-label="Đóng phím tắt"><i class="fas fa-times"></i></button>
      </div>
      <div class="shortcut-row">
        <span data-i18n="shortcut_search">Mở ô tìm kiếm nhanh</span>
        <kbd class="shortcut-key">/</kbd>
      </div>
      <div class="shortcut-row">
        <span data-i18n="shortcut_esc">Đóng bài đọc / Đóng hộp thoại</span>
        <kbd class="shortcut-key">ESC</kbd>
      </div>
      <div class="shortcut-row">
        <span data-i18n="shortcut_zoom">Tăng / Giảm cỡ chữ đọc bài (Zoom Text)</span>
        <kbd class="shortcut-key">T</kbd>
      </div>
      <div class="shortcut-row">
        <span data-i18n="shortcut_help">Xem bảng danh sách phím tắt</span>
        <kbd class="shortcut-key">?</kbd>
      </div>"""

norm_text = text.replace('\r\n', '\n')
replacements = [
    (head_old, head_new, "get_header"),
    (foot_old, foot_new, "drawer_lang"),
    (scripts_old, scripts_new, "scripts_translations"),
    (footer_p_old, footer_p_new, "footer_p"),
    (footer_bot_old, footer_bot_new, "footer_bot"),
    (search_in_old, search_in_new, "search_input"),
    (short_old, short_new, "shortcuts")
]

for old, new, tag in replacements:
    n_old = old.replace('\r\n', '\n')
    n_new = new.replace('\r\n', '\n')
    if n_old in norm_text:
        norm_text = norm_text.replace(n_old, n_new)
        print(f"SUCCESS: {tag} replaced!")
    else:
        print(f"FAIL: {tag} not found")

with open('scratch/build_multi_pages.py', 'w', encoding='utf-8') as f:
    f.write(norm_text)
print("Updated scratch/build_multi_pages.py base templates!")
