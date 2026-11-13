# -*- coding: utf-8 -*-
"""
Fix modals and drawer display bug:
Convert nonexistent .fashion-modal-backdrop and .fashion-drawer to standard
.search-modal, .onboard-modal-backdrop, .signin-modal-backdrop, .drawer-backdrop, .offcanvas-drawer
in both hearticles/madeuparticle/index.html and article.html.
Also add safety CSS rules in css/style.css.
"""

import os
import re

BASE_DIR = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127"
MADEUP_INDEX = os.path.join(BASE_DIR, "hearticles", "madeuparticle", "index.html")
ARTICLE_HTML = os.path.join(BASE_DIR, "article.html")
STYLE_CSS = os.path.join(BASE_DIR, "css", "style.css")

# 1. Standard modals markup for hearticles/madeuparticle/index.html (with ../../ paths)
madeup_modals = """  <!-- OFFCANVAS DRAWER MENU -->
  <div class="drawer-backdrop" id="drawerBackdrop" onclick="closeDrawer()"></div>
  <aside class="offcanvas-drawer" id="offcanvasDrawer" aria-label="Navigation Menu">
    <div class="drawer-header">
      <div class="brand-title" style="color:#FFF; font-family:var(--font-editorial); font-size:1.6rem; font-weight:900; letter-spacing:-0.03em;">
        HEARTICLES<span style="color:var(--color-brand-accent);">.</span>
      </div>
      <button onclick="closeDrawer()" style="color:#FFF; font-size:1.5rem;" aria-label="Close menu"><i class="fas fa-times"></i></button>
    </div>

    <!-- Drawer Language Selector Row -->
    <div class="drawer-lang-row" style="display:flex; align-items:center; justify-content:space-between; padding:0.75rem 1rem; margin-bottom:1rem; background:rgba(255,255,255,0.06); border-radius:8px;">
      <span style="font-size:0.875rem; color:#E2D8D4; font-weight:600;"><i class="fas fa-globe" style="margin-right:0.4rem; color:var(--color-brand-accent);"></i> Language:</span>
      <div class="lang-switch-pill" role="group" aria-label="Language Selector">
        <button class="lang-pill-btn" data-lang="vi" onclick="setLanguage('vi')">VI</button>
        <span class="lang-pill-divider">/</span>
        <button class="lang-pill-btn active" data-lang="en" onclick="setLanguage('en')">EN</button>
      </div>
    </div>

    <nav class="drawer-links-list">
      <a href="../../index.html" class="drawer-link" data-i18n="nav_home"><i class="fas fa-home"></i> Home</a>
      <a href="../../trending.html" class="drawer-link active" data-i18n="nav_trending"><i class="fas fa-fire"></i> Trending</a>
      <a href="../../society.html" class="drawer-link" data-i18n="nav_society"><i class="fas fa-globe-asia"></i> Society</a>
      <a href="../../human-stories.html" class="drawer-link" data-i18n="nav_human_stories"><i class="fas fa-heart"></i> Human Stories</a>
      <a href="../../mind-soul.html" class="drawer-link" data-i18n="nav_mind_soul"><i class="fas fa-spa"></i> Mind &amp; Soul</a>
      <a href="../../in-depth.html" class="drawer-link" data-i18n="nav_indepth"><i class="fas fa-feather-alt"></i> In-depth</a>
      <a href="javascript:void(0)" class="drawer-link" onclick="closeDrawer(); openSignInModal();" data-i18n="btn_signin"><i class="far fa-user-circle"></i> Đăng nhập / Sign In</a>
      <a href="../../about.html" class="drawer-link" data-i18n="nav_about"><i class="fas fa-info-circle"></i> About us</a>
    </nav>
    <div style="margin-top:auto; padding-top:1.5rem; border-top:1px solid #332B25;">
      <p style="font-size:0.8125rem; color:#E2D8D4; font-weight:600;">Faculty of English Language and Culture • ULIS - VNU • Lớp 6 - Nhóm 1 - Khóa 127:</p>
      <a href="mailto:class6group1term127@gmail.com" style="font-size:0.925rem; color:#FFFFFF; font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:0.4rem; margin-top:0.35rem;">
        <i class="fas fa-envelope" style="color:var(--color-brand-accent);"></i> class6group1term127@gmail.com
      </a>
    </div>
  </aside>

  <!-- SIGN IN MODAL -->
  <div class="signin-modal-backdrop" id="signInModal" onclick="if(event.target === this) closeSignInModal()">
    <div class="signin-modal-card">
      <button onclick="closeSignInModal()" style="position:absolute; top:1.25rem; right:1.25rem; font-size:1.25rem; color:var(--color-text-muted); cursor:pointer; background:none; border:none;" aria-label="Đóng"><i class="fas fa-times"></i></button>
      <div style="text-align:center; margin-bottom:1.5rem;">
        <div style="width:58px; height:58px; border-radius:50%; background:rgba(84,17,30,0.08); color:var(--color-brand-primary); font-size:1.85rem; display:inline-flex; align-items:center; justify-content:center; margin-bottom:0.75rem;">
          <i class="far fa-user-circle"></i>
        </div>
        <h3 style="font-family:var(--font-editorial); font-size:1.45rem; font-weight:800; color:var(--color-brand-primary);" data-i18n="signin_modal_title">Đăng Nhập Độc Giả</h3>
        <p style="font-size:0.85rem; color:var(--color-text-muted); margin-top:0.35rem;" data-i18n="signin_modal_desc">Access your reading history, saved bookmarks, and personalized notifications.</p>
      </div>
      <form onsubmit="handleSignInSubmit(event)" style="display:flex; flex-direction:column; gap:0.9rem;">
        <div>
          <label style="display:block; font-size:0.8rem; font-weight:700; color:var(--color-text-body); margin-bottom:0.3rem;" data-i18n="signin_email_label">Email hoặc Tên đăng nhập</label>
          <input type="text" id="signinEmailInput" required value="reader.ulis@vnu.edu.vn" placeholder="name@domain.com" style="width:100%; padding:0.65rem 0.9rem; border:1px solid var(--color-border-hairline); border-radius:8px; font-size:0.9rem; outline:none; box-sizing:border-box;">
        </div>
        <div>
          <label style="display:block; font-size:0.8rem; font-weight:700; color:var(--color-text-body); margin-bottom:0.3rem;" data-i18n="signin_password_label">Mật khẩu</label>
          <input type="password" required value="••••••••" placeholder="Nhập mật khẩu..." style="width:100%; padding:0.65rem 0.9rem; border:1px solid var(--color-border-hairline); border-radius:8px; font-size:0.9rem; outline:none; box-sizing:border-box;">
        </div>
        <button type="submit" class="fashion-btn-pill" style="padding:0.75rem; margin-top:0.5rem; width:100%; font-size:0.95rem; font-weight:700;" data-i18n="btn_signin">
          Đăng Nhập
        </button>
      </form>
    </div>
  </div>

  <!-- SEARCH MODAL -->
  <div class="search-modal" id="searchModal" onclick="if(event.target === this) closeSearchModal()">
    <div class="search-modal-box">
      <div class="search-input-wrap">
        <i class="fas fa-search" style="color:var(--color-brand-primary); font-size:1.25rem;"></i>
        <input type="text" class="search-input-field" id="searchInput" placeholder="Tìm kiếm bài viết, tác giả, chuyên mục..." data-i18n-placeholder="search_placeholder" oninput="handleSearchInput(this.value)">
        <button onclick="closeSearchModal()" style="font-size:1.25rem; color:var(--color-text-muted);"><i class="fas fa-times"></i></button>
      </div>
      <div class="search-results-list" id="searchResults">
        <p style="color:var(--color-text-body); font-size:0.95rem; font-weight:500;" data-i18n="search_hint">Search across 100 original verified articles...</p>
      </div>
    </div>
  </div>

  <!-- SUBSCRIBE MODAL -->
  <div class="onboard-modal-backdrop" id="subscribeModal" onclick="if(event.target === this) closeSubscribeModal()">
    <div class="onboard-card" style="text-align:center;">
      <button onclick="closeSubscribeModal()" style="position:absolute; top:1.25rem; right:1.25rem; font-size:1.25rem; color:var(--color-text-muted); cursor:pointer; background:none; border:none;" aria-label="Đóng"><i class="fas fa-times"></i></button>
      <div style="font-size:2.5rem; color:var(--color-brand-primary); margin-bottom:0.5rem;"><i class="fas fa-envelope-open-text"></i></div>
      <h3 style="font-family:var(--font-editorial); font-size:1.5rem; font-weight:800; color:var(--color-brand-primary);" data-i18n="subscribe_modal_title">Subscribe to HEARTICLES.</h3>
      <p style="font-size:0.875rem; color:var(--color-text-body); margin:0.75rem 0 1.25rem 0;" data-i18n="subscribe_modal_desc">Receive curated weekly human-interest journalism directly in your inbox every Sunday morning.</p>
      <form onsubmit="handleSubscribeSubmit(event)" style="display:flex; flex-direction:column; gap:0.75rem;">
        <input type="email" id="subscribeEmailInput" required placeholder="name@example.com" style="padding:0.75rem 1rem; border:1px solid var(--color-border-hairline); border-radius:8px; font-size:0.9rem; outline:none; box-sizing:border-box;">
        <button type="submit" id="subscribeSubmitBtn" class="fashion-btn-pill" style="padding:0.75rem; cursor:pointer; font-weight:700;" data-i18n="btn_subscribe">Subscribe</button>
      </form>
    </div>
  </div>"""

# Replace in hearticles/madeuparticle/index.html
with open(MADEUP_INDEX, "r", encoding="utf-8") as f:
    madeup_html = f.read()

# Pattern matching from <!-- Search Modal --> down to before <!-- Core Scripts -->
madeup_html = re.sub(
    r"\s*<!-- Search Modal -->[\s\S]*?<!-- Core Scripts -->",
    f"\n\n{madeup_modals}\n\n  <!-- Core Scripts -->",
    madeup_html
)

with open(MADEUP_INDEX, "w", encoding="utf-8") as f:
    f.write(madeup_html)
print("Updated hearticles/madeuparticle/index.html with standard hidden modals.")

# 2. Standard modals markup for article.html (with root paths)
article_modals = madeup_modals.replace("../../", "")

with open(ARTICLE_HTML, "r", encoding="utf-8") as f:
    art_html = f.read()

art_html = re.sub(
    r"\s*<!-- Search Modal -->[\s\S]*?<!-- Core Scripts -->",
    f"\n\n{article_modals}\n\n  <!-- Core Scripts -->",
    art_html
)

with open(ARTICLE_HTML, "w", encoding="utf-8") as f:
    f.write(art_html)
print("Updated article.html with standard hidden modals.")

# 3. Add safety fallback CSS in css/style.css
with open(STYLE_CSS, "r", encoding="utf-8") as f:
    css_content = f.read()

safety_css = """
/* ===================================================================
   SAFETY FALLBACK: ENSURE NO UNSTYLED MODALS SIT IN NORMAL FLOW
   =================================================================== */
.fashion-modal-backdrop,
.fashion-drawer-backdrop,
.fashion-drawer,
.search-modal:not(.active),
.onboard-modal-backdrop:not(.active),
.signin-modal-backdrop:not(.active),
.drawer-backdrop:not(.active) {
  display: none !important;
}
"""

if ".fashion-modal-backdrop" not in css_content:
    css_content += safety_css
    with open(STYLE_CSS, "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Appended safety modal CSS in css/style.css.")
else:
    print("Safety CSS already present in css/style.css.")

print("\nSUCCESS: All modals and drawer converted and secured.")
