import glob, os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

root = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127'

ad_markup = """  <!-- =================================================================
       1. HEADER LEADERBOARD ADVERTISEMENT (IELTS FIGHTER BANNER)
       ================================================================= -->
  <div class="header-ad-leaderboard-wrap">
    <div class="container" style="display:flex; flex-direction:column; align-items:center;">
      <span class="ad-label-strip" data-i18n="ad_label">ADVERTISEMENT • QUẢNG CÁO</span>
      <a href="https://ielts-fighter.com" target="_blank" rel="noopener noreferrer" class="header-ad-link" title="IELTS Fighter - Đột phá điểm số">
        <img src="assets/images/ads/header_ad_banner.png" alt="IELTS Fighter Leaderboard Ad" class="header-ad-banner-img">
      </a>
    </div>
  </div>

  """

footer_target_pattern = re.compile(
    r'<p class="fashion-footer-desc"[^>]*>.*?</p>\s*'
    r'<p class="fashion-footer-group"[^>]*>.*?</p>\s*'
    r'<div style="display:flex; gap:1\.25rem; margin-top:0\.75rem; font-size:0\.875rem;">.*?</div>\s*'
    r'<p style="font-size:0\.875rem; color:var\(--color-brand-primary\); font-weight:700; margin-top:0\.6rem;">\s*'
    r'<a href="mailto:class6group1term127@gmail\.com"[^>]*>\s*'
    r'<i class="fas fa-envelope"></i> Email Tòa soạn: <strong>class6group1term127@gmail\.com</strong>\s*'
    r'</a>\s*'
    r'</p>',
    re.DOTALL
)

footer_replacement = """<p class="fashion-footer-desc" data-i18n="footer_desc">An independent news outlet based in Hanoi, Vietnam.</p>
          <div class="fashion-footer-socials" style="display:flex; flex-wrap:wrap; gap:0.75rem; margin-top:0.85rem; align-items:center;">
            <a href="https://www.facebook.com/people/Hearticles/61595901793120/" target="_blank" rel="noopener noreferrer" class="social-pill-btn fb" title="Facebook - HEARTICLES">
              <i class="fab fa-facebook"></i> <span>Facebook</span>
            </a>
            <a href="https://www.instagram.com/hearticles.news/" target="_blank" rel="noopener noreferrer" class="social-pill-btn ig" title="Instagram - @hearticles.news">
              <i class="fab fa-instagram"></i> <span>Instagram</span>
            </a>
            <a href="https://x.com/hearticles_news" target="_blank" rel="noopener noreferrer" class="social-pill-btn tw" title="X (Twitter) - @hearticles_news">
              <i class="fab fa-x-twitter"></i> <span>X (Twitter)</span>
            </a>
          </div>
          <p style="font-size:0.875rem; color:var(--color-brand-primary); font-weight:700; margin-top:0.75rem;">
            <a href="mailto:class6group1term127@gmail.com" style="color:inherit; text-decoration:none; display:inline-flex; align-items:center; gap:0.4rem;">
              <i class="fas fa-envelope"></i> Email: <strong>class6group1term127@gmail.com</strong>
            </a>
          </p>"""

copy_old = '<span data-i18n="footer_copy">&copy; 2026 HEARTICLES. Mọi quyền được bảo lưu. Xuất bản bởi Nhóm 1 Lớp 6 Khóa 127, ULIS - VNU.</span>'
copy_new = '<span data-i18n="footer_copy">&copy; 2026 HEARTICLES. All rights reserved. • An independent news outlet based in Hanoi, Vietnam.</span>'

drawer_socials_markup = """      <div class="drawer-socials" style="margin-top:auto; padding-top:1.5rem; border-top:1px solid rgba(255,255,255,0.12); display:flex; align-items:center; gap:0.75rem;">
        <span style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.08em; color:rgba(255,255,255,0.5);">Follow us:</span>
        <a href="https://www.facebook.com/people/Hearticles/61595901793120/" target="_blank" rel="noopener noreferrer" class="drawer-social-link" title="Facebook"><i class="fab fa-facebook"></i></a>
        <a href="https://www.instagram.com/hearticles.news/" target="_blank" rel="noopener noreferrer" class="drawer-social-link" title="Instagram"><i class="fab fa-instagram"></i></a>
        <a href="https://x.com/hearticles_news" target="_blank" rel="noopener noreferrer" class="drawer-social-link" title="X (Twitter)"><i class="fab fa-x-twitter"></i></a>
      </div>
    </aside>"""

for fpath in glob.glob(os.path.join(root, '*.html')):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add IELTS banner if not present
    if 'header-ad-leaderboard-wrap' not in html:
        # insert right before <div class="fashion-masthead-hero">
        target_masthead = '<div class="fashion-masthead-hero">'
        if target_masthead in html:
            html = html.replace(target_masthead, ad_markup + target_masthead, 1)
            print("Added IELTS ad to:", os.path.basename(fpath))

    # 2. Update footer
    if footer_target_pattern.search(html):
        html = footer_target_pattern.sub(footer_replacement, html)
        print("Updated footer in:", os.path.basename(fpath))
    else:
        print("Footer pattern not matched in:", os.path.basename(fpath))

    if copy_old in html:
        html = html.replace(copy_old, copy_new)
        print("Updated footer_copy in:", os.path.basename(fpath))

    # 3. Add drawer socials if not present
    if 'drawer-socials' not in html and '</aside>' in html:
        html = html.replace('</aside>', drawer_socials_markup, 1)
        print("Added drawer socials to:", os.path.basename(fpath))

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)

print("HTML updates completed!")
