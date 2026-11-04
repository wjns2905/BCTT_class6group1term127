# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/build_multi_pages.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update academic bar in get_header
target_header = """      <div class="top-utility-right">
        <!-- Language Switcher Pill in Top Bar -->
        <div class="lang-switch-pill" role="group" aria-label="Language Selector">
          <button class="lang-pill-btn active" data-lang="vi" onclick="setLanguage('vi')">VI</button>
          <span class="lang-pill-divider">/</span>
          <button class="lang-pill-btn" data-lang="en" onclick="setLanguage('en')">EN</button>
        </div>
        <span class="date-widget" id="liveDateWidget"><i class="far fa-calendar-alt"></i> Đang tải ngày...</span>
      </div>"""

replacement_header = """      <div class="top-utility-right">
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

# 2. Update footer email link in get_footer
target_footer = """          <p style="font-size:0.85rem; color:var(--color-brand-primary); font-weight:700; margin-top:0.5rem;">
            Email: class6group1term127@gmail.com
          </p>"""

replacement_footer = """          <p style="font-size:0.875rem; color:var(--color-brand-primary); font-weight:700; margin-top:0.6rem;">
            <a href="mailto:class6group1term127@gmail.com" style="color:inherit; text-decoration:none; display:inline-flex; align-items:center; gap:0.4rem;">
              <i class="fas fa-envelope"></i> Email Tòa soạn: <strong>class6group1term127@gmail.com</strong>
            </a>
          </p>"""

# 3. Update drawer email link in get_footer
target_drawer = """    <div style="margin-top:auto; padding-top:1.5rem; border-top:1px solid #332B25;">
      <p style="font-size:0.8125rem; color:#E2D8D4; font-weight:600;">Tòa soạn ULIS - VNU:</p>
      <p style="font-size:0.925rem; color:#FFFFFF; font-weight:700;">class6group1term127@gmail.com</p>
    </div>"""

replacement_drawer = """    <div style="margin-top:auto; padding-top:1.5rem; border-top:1px solid #332B25;">
      <p style="font-size:0.8125rem; color:#E2D8D4; font-weight:600;">Tòa soạn ULIS - VNU • Lớp 6 - Nhóm 1 - Khóa 127:</p>
      <a href="mailto:class6group1term127@gmail.com" style="font-size:0.925rem; color:#FFFFFF; font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:0.4rem; margin-top:0.35rem;">
        <i class="fas fa-envelope" style="color:var(--color-brand-accent);"></i> class6group1term127@gmail.com
      </a>
    </div>"""

norm_text = text.replace('\r\n', '\n')
norm_th = target_header.replace('\r\n', '\n')
norm_rh = replacement_header.replace('\r\n', '\n')
norm_tf = target_footer.replace('\r\n', '\n')
norm_rf = replacement_footer.replace('\r\n', '\n')
norm_td = target_drawer.replace('\r\n', '\n')
norm_rd = replacement_drawer.replace('\r\n', '\n')

if norm_th in norm_text:
    norm_text = norm_text.replace(norm_th, norm_rh)
    print("SUCCESS: header email added!")
else:
    print("FAIL: target_header not found")

if norm_tf in norm_text:
    norm_text = norm_text.replace(norm_tf, norm_rf)
    print("SUCCESS: footer email updated!")
else:
    print("FAIL: target_footer not found")

if norm_td in norm_text:
    norm_text = norm_text.replace(norm_td, norm_rd)
    print("SUCCESS: drawer email updated!")
else:
    print("FAIL: target_drawer not found")

with open('scratch/build_multi_pages.py', 'w', encoding='utf-8') as f:
    f.write(norm_text)
print("build_multi_pages.py updated with email links!")
