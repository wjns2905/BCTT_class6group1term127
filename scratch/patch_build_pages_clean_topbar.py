# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/build_multi_pages.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Clean top-utility-right in get_header
old_utility_right = """      <div class="top-utility-right">
        <!-- Official Group Email Link -->
        <a href="mailto:class6group1term127@gmail.com" class="academic-email-link" title="Gửi thư đến Tòa soạn Lớp 6 - Nhóm 1 - Khóa 127">
          <i class="fas fa-envelope"></i> class6group1term127@gmail.com
        </a>
        <!-- Language Switcher Pill in Top Bar -->
        <div class="lang-switch-pill" role="group" aria-label="Language Selector">
          <button class="lang-pill-btn active" data-lang="vi" onclick="setLanguage('vi')">VI</button>
          <span class="lang-pill-divider">/</span>
          <button class="lang-pill-btn" data-lang="en" onclick="setLanguage('en')">EN</button>
        </div>
        <span class="date-widget" id="liveDateWidget"><i class="far fa-calendar-alt"></i> Đang tải ngày...</span>
      </div>"""

new_utility_right = """      <div class="top-utility-right">
        <span class="date-widget" id="liveDateWidget"><i class="far fa-calendar-alt"></i> Loading date...</span>
      </div>"""

# 2. Make EN active by default in header actions
old_header_actions = """        <!-- Primary language toggle button on the bar -->
        <div class="lang-switch-pill" role="group" aria-label="Language Selector">
          <button class="lang-pill-btn active" data-lang="vi" onclick="setLanguage('vi')">VI</button>
          <span class="lang-pill-divider">/</span>
          <button class="lang-pill-btn" data-lang="en" onclick="setLanguage('en')">EN</button>
        </div>"""

new_header_actions = """        <!-- Primary language toggle button on the bar (Default: EN) -->
        <div class="lang-switch-pill" role="group" aria-label="Language Selector">
          <button class="lang-pill-btn" data-lang="vi" onclick="setLanguage('vi')">VI</button>
          <span class="lang-pill-divider">/</span>
          <button class="lang-pill-btn active" data-lang="en" onclick="setLanguage('en')">EN</button>
        </div>"""

# 3. Make EN active by default in drawer
old_drawer_pill = """    <!-- Drawer Language Selector Row -->
    <div class="drawer-lang-row" style="display:flex; align-items:center; justify-content:space-between; padding:0.75rem 1rem; margin-bottom:1rem; background:rgba(255,255,255,0.06); border-radius:8px;">
      <span style="font-size:0.875rem; color:#E2D8D4; font-weight:600;"><i class="fas fa-globe" style="margin-right:0.4rem; color:var(--color-brand-accent);"></i> Ngôn ngữ / Language:</span>
      <div class="lang-switch-pill" role="group" aria-label="Language Selector">
        <button class="lang-pill-btn active" data-lang="vi" onclick="setLanguage('vi')">VI</button>
        <span class="lang-pill-divider">/</span>
        <button class="lang-pill-btn" data-lang="en" onclick="setLanguage('en')">EN</button>
      </div>
    </div>"""

new_drawer_pill = """    <!-- Drawer Language Selector Row (Default: EN) -->
    <div class="drawer-lang-row" style="display:flex; align-items:center; justify-content:space-between; padding:0.75rem 1rem; margin-bottom:1rem; background:rgba(255,255,255,0.06); border-radius:8px;">
      <span style="font-size:0.875rem; color:#E2D8D4; font-weight:600;"><i class="fas fa-globe" style="margin-right:0.4rem; color:var(--color-brand-accent);"></i> Ngôn ngữ / Language:</span>
      <div class="lang-switch-pill" role="group" aria-label="Language Selector">
        <button class="lang-pill-btn" data-lang="vi" onclick="setLanguage('vi')">VI</button>
        <span class="lang-pill-divider">/</span>
        <button class="lang-pill-btn active" data-lang="en" onclick="setLanguage('en')">EN</button>
      </div>
    </div>"""

# 4. wrap_page html lang="en"
old_wrap = '<html lang="vi">'
new_wrap = '<html lang="en">'

norm_text = text.replace('\r\n', '\n')
norm_old_util = old_utility_right.replace('\r\n', '\n')
norm_new_util = new_utility_right.replace('\r\n', '\n')
norm_old_head = old_header_actions.replace('\r\n', '\n')
norm_new_head = new_header_actions.replace('\r\n', '\n')
norm_old_draw = old_drawer_pill.replace('\r\n', '\n')
norm_new_draw = new_drawer_pill.replace('\r\n', '\n')

if norm_old_util in norm_text:
    norm_text = norm_text.replace(norm_old_util, norm_new_util)
    print("SUCCESS: Removed email and duplicate lang pill from top-utility-right!")
else:
    print("FAIL: old_utility_right not found")

if norm_old_head in norm_text:
    norm_text = norm_text.replace(norm_old_head, norm_new_head)
    print("SUCCESS: Header actions language pill defaulted to EN active!")
else:
    print("FAIL: old_header_actions not found")

if norm_old_draw in norm_text:
    norm_text = norm_text.replace(norm_old_draw, norm_new_draw)
    print("SUCCESS: Drawer language pill defaulted to EN active!")
else:
    print("FAIL: old_drawer_pill not found")

if old_wrap in norm_text:
    norm_text = norm_text.replace(old_wrap, new_wrap)
    print("SUCCESS: wrap_page updated to <html lang=\"en\">!")
else:
    print("FAIL: old_wrap not found")

with open('scratch/build_multi_pages.py', 'w', encoding='utf-8') as f:
    f.write(norm_text)
print("scratch/build_multi_pages.py updated successfully!")
