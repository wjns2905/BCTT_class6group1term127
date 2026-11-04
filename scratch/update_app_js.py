# -*- coding: utf-8 -*-
"""
Script to update js/app.js in BCTT_class6group1term127:
1. Add setupHeartTapWidget() and invoke in initApp().
2. Add the "Read Related Story" button in showPollResults().
3. Update renderAboutUsSection() with the 4 tabs/anchors (#profiles, #photo, #subscribe, #mission).
"""
import sys, os

app_js_path = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js"

with open(app_js_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update initApp to call setupHeartTapWidget
if 'setupHeartTapWidget();' not in code:
    code = code.replace(
        '  setupPoll();',
        '  setupPoll();\n  setupHeartTapWidget();'
    )
    print("Added setupHeartTapWidget() call to initApp().")

# 2. Add setupHeartTapWidget function if not present
heart_tap_func = """
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
"""

if 'function setupHeartTapWidget()' not in code:
    code += '\n' + heart_tap_func
    print("Appended setupHeartTapWidget() function to app.js.")

# 3. Update showPollResults to include Read Related Story button
target_poll_check = '<i class="fas fa-check-circle"></i> Bạn đã tham gia biểu quyết khảo sát này.'
if target_poll_check in code and 'poll-read-related-btn' not in code:
    replacement_poll = """<i class="fas fa-check-circle"></i> <span data-i18n="poll_voted_ack">Bạn đã tham gia biểu quyết khảo sát này.</span>
      </div>
      <div style="margin-top:1.25rem; text-align:center;">
        <button class="poll-read-related-btn" onclick="openArticleModal('trending-4')">
          <i class="fas fa-book-open"></i>
          <span data-i18n="poll_read_story_btn">Đọc bài viết liên quan: Gánh mưu sinh phố cổ Hội An &rarr;</span>
        </button>
      </div>"""
    code = code.replace(
        '<i class="fas fa-check-circle"></i> Bạn đã tham gia biểu quyết khảo sát này.\n      </div>',
        replacement_poll
    )
    print("Updated showPollResults() with Read Related Story button.")

# 4. Update renderAboutUsSection to include 4 sections (#profiles, #photo, #subscribe, #mission)
new_about_section = """function renderAboutUsSection() {
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
          <h2 class="nhandan-sec-title">${isEn ? 'EDITORIAL BOARD & ACADEMIC ADVISORY' : 'BAN BIÊN TẬP & CỐ VẤN TÒA SOẠN'}</h2>
          <span class="nhandan-sec-sub">${isEn ? 'University of Languages and International Studies - VNU (ULIS - VNU)' : 'Trường Đại học Ngoại ngữ - Đại học Quốc gia Hà Nội (ULIS - VNU)'}</span>
        </div>
      </div>

      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:1.5rem; margin-top:1.5rem;">
        <!-- Advisor Card -->
        <div style="background:#FFF; border:1px solid var(--color-border-hairline); border-radius:12px; padding:1.75rem; box-shadow:0 4px 16px rgba(0,0,0,0.04);">
          <div style="display:flex; align-items:center; gap:1rem; margin-bottom:1rem;">
            <div style="width:56px; height:56px; border-radius:50%; background:var(--color-surface-blush); color:var(--color-brand-primary); display:flex; align-items:center; justify-content:center; font-size:1.5rem; font-weight:800;">
              UL
            </div>
            <div>
              <h3 style="font-family:var(--font-editorial); font-size:1.15rem; font-weight:800; color:var(--color-brand-primary);">${isEn ? 'Academic Advisor' : 'Cố Vấn Học Thuật'}</h3>
              <p style="font-size:0.8125rem; color:var(--color-text-muted); margin:0;">${isEn ? 'Faculty of Linguistics & Communication' : 'Khoa Ngôn ngữ & Truyền thông • ULIS - VNU'}</p>
            </div>
          </div>
          <p style="font-size:0.875rem; color:var(--color-text-body); line-height:1.6; margin:0;">
            ${isEn ? 'Guiding content strategy, editorial ethics, international media standards, and journalistic compliance.' : 'Định hướng tôn chỉ nội dung, phương pháp báo chí đa phương tiện và chuẩn mực đạo đức người làm truyền thông.'}
          </p>
        </div>

        <!-- Student Group Card -->
        <div style="background:#FFF; border:1px solid var(--color-border-hairline); border-radius:12px; padding:1.75rem; box-shadow:0 4px 16px rgba(0,0,0,0.04);">
          <div style="display:flex; align-items:center; gap:1rem; margin-bottom:1rem;">
            <div style="width:56px; height:56px; border-radius:50%; background:var(--color-brand-primary); color:#FFF; display:flex; align-items:center; justify-content:center; font-size:1.5rem; font-weight:800;">
              C6
            </div>
            <div>
              <h3 style="font-family:var(--font-editorial); font-size:1.15rem; font-weight:800; color:var(--color-brand-primary);">Class 6 - Group 1 - Term 127</h3>
              <p style="font-size:0.8125rem; color:var(--color-text-muted); margin:0;">${isEn ? 'Student Editorial Team • Course: BCTT' : 'Nhóm Sinh viên Thực hiện • Học phần: BCTT'}</p>
            </div>
          </div>
          <p style="font-size:0.875rem; color:var(--color-text-body); line-height:1.6; margin:0;">
            ${isEn ? 'Researching, designing, translating, and developing the multimedia magazine HEARTICLES.' : 'Trực tiếp nghiên cứu tài nguyên, biên tập song ngữ, thiết kế mỹ thuật và lập trình toàn diện hệ thống tạp chí.'}
          </p>
          <div style="margin-top:1rem; padding-top:0.75rem; border-top:1px dashed var(--color-border-hairline); font-size:0.8125rem;">
            <a href="mailto:class6group1term127@gmail.com" style="color:var(--color-brand-primary); font-weight:700; text-decoration:none;">
              <i class="fas fa-envelope"></i> class6group1term127@gmail.com
            </a>
          </div>
        </div>
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
          <img src="assets/images/trending/image8.jpg" alt="Phố cổ Hội An" class="about-photo-img">
          <div class="about-photo-caption">
            <h4>${isEn ? 'Street Vendors in Hoi An' : 'Gánh mưu sinh phố cổ Hội An'}</h4>
            <p>${isEn ? 'VnExpress Photojournalism • Article 4 Trending' : 'Phóng sự VnExpress • Bài 4 Trending'}</p>
          </div>
        </div>

        <div class="about-photo-item" onclick="openArticleModal('human-4')">
          <img src="assets/images/human_stories/image7.png" alt="Cánh đồng nghĩa tình Texas" class="about-photo-img">
          <div class="about-photo-caption">
            <h4>${isEn ? 'Texas Volunteer Community Harvest' : 'Cánh đồng nghĩa tình Gruver, Texas'}</h4>
            <p>${isEn ? 'The Washington Post • Article 4 Human Stories' : 'The Washington Post • Bài 4 Human Stories'}</p>
          </div>
        </div>

        <div class="about-photo-item" onclick="openArticleModal('human-3')">
          <img src="assets/images/human_stories/image3.png" alt="Qusay Hussein" class="about-photo-img">
          <div class="about-photo-caption">
            <h4>${isEn ? 'Qusay Hussein: Second Chance at Life' : 'Qusay Hussein: Cơ hội thứ hai để sống'}</h4>
            <p>${isEn ? 'The Guardian • Article 3 Human Stories' : 'The Guardian • Bài 3 Human Stories'}</p>
          </div>
        </div>

        <div class="about-photo-item" onclick="openArticleModal('mind-1')">
          <img src="assets/images/mind_&_soul/image2.jpg" alt="Taeyang Mỹ Đình" class="about-photo-img">
          <div class="about-photo-caption">
            <h4>${isEn ? 'Taeyang (BigBang) Concert at My Dinh' : 'Taeyang (BigBang) tại SVĐ Mỹ Đình'}</h4>
            <p>${isEn ? 'Lao Dong Newspaper • Article 1 Mind & Soul' : 'Báo Lao Động • Bài 1 Mind & Soul'}</p>
          </div>
        </div>

        <div class="about-photo-item" onclick="openArticleModal('society-1')">
          <img src="assets/images/society/image3.jpg" alt="Vale Pantry" class="about-photo-img">
          <div class="about-photo-caption">
            <h4>${isEn ? 'The Vale Pantry Community Grocer' : 'Siêu thị cộng đồng Vale Pantry'}</h4>
            <p>${isEn ? 'The Guardian • Article 1 Society' : 'The Guardian • Bài 1 Society'}</p>
          </div>
        </div>

        <div class="about-photo-item" onclick="openArticleModal('indepth-1')">
          <img src="assets/images/human_stories/image20.jpg" alt="Hoa sữa Hà Nội" class="about-photo-img">
          <div class="about-photo-caption">
            <h4>${isEn ? 'A Hanoi That Never Stands Still' : 'Nốt hương hoa sữa và ký ức mùa thu'}</h4>
            <p>${isEn ? 'Vietnam News • Article 1 In-depth' : 'Vietnam News • Bài 1 In-depth'}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: SUBSCRIBE (#subscribe) -->
    <section id="subscribe" style="margin-bottom: 3.5rem; scroll-margin-top: 100px;">
      <div class="about-subscribe-card">
        <div style="width:64px; height:64px; border-radius:50%; background:var(--color-surface-blush); color:var(--color-brand-primary); font-size:1.75rem; display:inline-flex; align-items:center; justify-content:center; margin-bottom:1rem;">
          <i class="fas fa-paper-plane"></i>
        </div>
        <h2 style="font-family:var(--font-editorial); font-size:1.85rem; font-weight:800; color:var(--color-brand-primary); margin-bottom:0.5rem;">
          ${isEn ? 'Subscribe to HEARTICLES. Newsletter' : 'Đăng Ký Nhận Bản Tin HEARTICLES.'}
        </h2>
        <p style="font-size:0.95rem; color:var(--color-text-body); max-width:540px; margin:0 auto 1.5rem auto; line-height:1.6;">
          ${isEn ? 'Receive curated weekly editorial digests, poignant human stories, and deep cultural essays delivered straight to your inbox.' : 'Nhận tuyển tập phóng sự nhân văn sâu sắc, ký sự văn hóa và nhịp đập xã hội nổi bật được chọn lọc kỹ lưỡng mỗi sáng Chủ nhật.'}
        </p>

        <form onsubmit="event.preventDefault(); showToast(currentLanguage === 'en' ? 'Thank you for subscribing!' : 'Cảm ơn bạn đã đăng ký nhận bản tin!', 'subscribe');" style="display:flex; flex-direction:column; gap:0.75rem; max-width:440px; margin:0 auto;">
          <div style="display:flex; gap:0.5rem;">
            <input type="email" required placeholder="name@example.com" style="flex:1; padding:0.75rem 1rem; border:1px solid var(--color-border-hairline); border-radius:var(--radius-md); font-size:0.9rem; outline:none;">
            <button type="submit" class="fashion-btn-pill" style="padding:0.75rem 1.5rem; font-size:0.875rem;">
              ${isEn ? 'Subscribe' : 'Đăng ký'}
            </button>
          </div>
          <span style="font-size:0.75rem; color:var(--color-text-muted);">
            <i class="fas fa-shield-alt"></i> ${isEn ? 'No spam. Unsubscribe at any time with one click.' : 'Không spam. Hủy đăng ký bất cứ lúc nào với một cú click.'}
          </span>
        </form>
      </div>
    </section>

    <!-- SECTION 4: MISSION & ETHICS (#mission) -->
    <section id="mission" style="margin-bottom: 3.5rem; scroll-margin-top: 100px;">
      <div class="nhandan-section-header">
        <div class="nhandan-sec-title-wrap">
          <span class="nhandan-sec-ribbon"></span>
          <h2 class="nhandan-sec-title">${isEn ? 'EDITORIAL MANIFESTO & JOURNALISTIC ETHICS' : 'TÔN CHỈ HOẠT ĐỘNG & ĐẠO ĐỨC NGHỀ BÁO'}</h2>
          <span class="nhandan-sec-sub">${isEn ? 'Stories that speak to the heart — Where news begins with a heartbeat' : 'Nơi tin tức khởi nguồn từ nhịp đập trái tim và lòng trắc ẩn'}</span>
        </div>
      </div>

      <div style="background:#FFF; border:1px solid var(--color-border-hairline); border-radius:12px; padding:2rem; line-height:1.7; color:var(--color-text-body); box-shadow:0 4px 16px rgba(0,0,0,0.04);">
        <p style="font-size:1.05rem; font-family:var(--font-editorial); font-style:italic; color:var(--color-brand-primary); margin-bottom:1.25rem;">
          ${isEn ? '“Authentic beauty in digital journalism lies not in sensational clickbait, but in humanistic depth, the elegance of typography, and gentle stories that touch readers\' hearts.”' : '“Cái đẹp chân thực của báo chí số không nằm ở những giật gân, câu khách, mà ở chiều sâu nhân văn, sự thanh lịch của con chữ và những câu chuyện tử tế chạm đến đáy lòng độc giả.”'}
        </p>

        <p>
          ${isEn ? '<strong>HEARTICLES.</strong> is founded and developed by <strong>Class 6 - Group 1 - Term 127</strong> at the <strong>University of Languages and International Studies - Vietnam National University, Hanoi (ULIS - VNU)</strong> as the capstone publication for the Journalism & Media Communications (BCTT) curriculum.' : '<strong>HEARTICLES.</strong> được sáng lập và phát triển bởi <strong>Lớp 6 - Nhóm 1 - Khóa 127</strong> thuộc <strong>Trường Đại học Ngoại ngữ - Đại học Quốc gia Hà Nội (ULIS - VNU)</strong> như một ấn phẩm xuất bản đa phương tiện cho học phần Báo chí &amp; Truyền thông (BCTT).'}
        </p>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:1.25rem; margin:1.5rem 0;">
          <div style="background:var(--color-surface-blush); padding:1.25rem; border-radius:8px; border-left:4px solid var(--color-brand-primary);">
            <h4 style="color:var(--color-brand-primary); margin-bottom:0.4rem; font-weight:800;"><i class="fas fa-check-circle"></i> ${isEn ? 'Truth & Source Fidelity' : 'Tôn Trọng Sự Thật'}</h4>
            <p style="font-size:0.8125rem; margin:0;">${isEn ? '100% authentic images and stories referenced from source documents (VnExpress, The Guardian, The Washington Post, Lao Dong, NDO).' : '100% hình ảnh và tư liệu trích xuất chuẩn xác từ tài nguyên báo chí gốc.'}</p>
          </div>
          <div style="background:var(--color-surface-blush); padding:1.25rem; border-radius:8px; border-left:4px solid var(--color-brand-primary);">
            <h4 style="color:var(--color-brand-primary); margin-bottom:0.4rem; font-weight:800;"><i class="fas fa-heart"></i> ${isEn ? 'Empathy & Human Dignity' : 'Nhân Văn & Phẩm Giá'}</h4>
            <p style="font-size:0.8125rem; margin:0;">${isEn ? 'Prioritizing stories that uplift spirits, honor constructive labor, and preserve human dignity in adversity.' : 'Ưu tiên những câu chuyện thắp sáng lòng trắc ẩn, tôn vinh lao động và tôn trọng phẩm giá con người.'}</p>
          </div>
          <div style="background:var(--color-surface-blush); padding:1.25rem; border-radius:8px; border-left:4px solid var(--color-brand-primary);">
            <h4 style="color:var(--color-brand-primary); margin-bottom:0.4rem; font-weight:800;"><i class="fas fa-feather"></i> ${isEn ? 'Aesthetic Excellence' : 'Chuẩn Mực Mỹ Cảm'}</h4>
            <p style="font-size:0.8125rem; margin:0;">${isEn ? 'Harmonizing high-contrast editorial Didone/Plus Jakarta typography with Báo Nhân Dân asymmetric layout architecture.' : 'Hòa quyện vẻ đẹp xếp chữ tối giản hiện đại với kiến trúc bố cục phi đối xứng Báo Nhân Dân điện tử.'}</p>
          </div>
        </div>

        <p style="font-size:0.85rem; color:var(--color-text-muted); margin-bottom:0;">
          ${isEn ? 'Academic attribution: Class 6 - Group 1 - Term 127 • Faculty of Linguistics & Communication • ULIS - VNU • Hanoi, Vietnam.' : 'Thông tin pháp lý & học thuật: Lớp 6 - Nhóm 1 - Khóa 127 • Khoa Ngôn ngữ & Truyền thông • Trường Đại học Ngoại ngữ - ĐHQGHN.'}
        </p>
      </div>
    </section>
  `;
}"""

# Replace the existing renderAboutUsSection with new_about_section
# Find start of renderAboutUsSection
start_idx = code.find('function renderAboutUsSection() {')
if start_idx != -1:
    # Find the next function definition or end of block
    next_func_idx = code.find('\nfunction setupPoll()', start_idx)
    if next_func_idx != -1:
        code = code[:start_idx] + new_about_section + '\n\n' + code[next_func_idx:]
        print("Replaced renderAboutUsSection() with 4-tab structured implementation.")
    else:
        print("Could not find next function after renderAboutUsSection.")
else:
    print("Could not find renderAboutUsSection.")

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved updated app.js!")
