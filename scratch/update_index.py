import sys

with open('c:/Users/camka/OneDrive/Desktop/BCTT/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add progress bar and offline banner after <body>
t1 = '<body>'
r1 = '''<body>

  <!-- Reading Progress Bar -->
  <div class="reading-progress-bar" id="readingProgressBar"></div>

  <!-- Offline Status Banner -->
  <div class="offline-indicator-banner" id="offlineBanner">
    <i class="fas fa-wifi-slash"></i>
    <span>Chế độ ngoại tuyến: Bạn đang đọc các bài viết đã lưu đệm. Hệ thống sẽ tự động cập nhật khi có mạng.</span>
  </div>'''
if t1 in html and 'id="readingProgressBar"' not in html:
    html = html.replace(t1, r1, 1)

# 2. Add ambient canvas in hero grid
t2 = '<section class="hero-news-grid" id="mainHeroGrid">'
r2 = '''<section class="hero-news-grid" id="mainHeroGrid">
      <!-- Ambient Heartbeat Canvas -->
      <div class="ambient-canvas-wrapper">
        <canvas id="ambientHeartCanvas" class="ambient-canvas"></canvas>
      </div>'''
if t2 in html and 'id="ambientHeartCanvas"' not in html:
    html = html.replace(t2, r2, 1)

# 3. Add modals and mobile dock before script tags
t3 = '  <!-- Scripts -->\n  <script src="js/data.js"></script>'
r3 = '''  <!-- =================================================================
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
        <h3 style="font-family:var(--font-serif); font-size:1.35rem; font-weight:700; color:var(--color-text-headline);">
          <i class="fas fa-keyboard" style="color:var(--color-brand-primary); margin-right:0.5rem;"></i> Phím tắt hệ thống
        </h3>
        <button onclick="closeShortcutsModal()" style="color:var(--color-text-muted); font-size:1.25rem;" aria-label="Đóng phím tắt"><i class="fas fa-times"></i></button>
      </div>
      <div class="shortcut-row">
        <span>Mở ô tìm kiếm nhanh toàn bộ 34 bài viết</span>
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
    <a href="javascript:void(0)" class="dock-btn" onclick="openSearchModal()">
      <i class="fas fa-search"></i>
      <span>Tìm kiếm</span>
    </a>
    <a href="javascript:void(0)" class="dock-btn" onclick="filterByCategory('in-depth')">
      <i class="fas fa-book-open"></i>
      <span>In-depth</span>
    </a>
    <a href="javascript:void(0)" class="dock-btn" onclick="openDrawer()">
      <i class="fas fa-bars"></i>
      <span>Menu</span>
    </a>
  </nav>

  <!-- Scripts -->
  <script src="js/data.js"></script>'''
if t3 in html and 'id="shortcutsModal"' not in html:
    html = html.replace(t3, r3, 1)

with open('c:/Users/camka/OneDrive/Desktop/BCTT/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated index.html successfully!')
