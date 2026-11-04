# -*- coding: utf-8 -*-
import sys

app_js_path = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js"

with open(app_js_path, 'r', encoding='utf-8') as f:
    code = f.read()

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
          <h2 class="nhandan-sec-title" data-i18n="profiles_sec_title">${isEn ? 'EDITORIAL BOARD & NEWSROOM ROSTER' : 'BAN BIÊN TẬP & NHÂN SỰ TÒA SOẠN'}</h2>
          <span class="nhandan-sec-sub" data-i18n="profiles_sec_sub">${isEn ? 'Class 6 - Group 1 - Term 127 • Faculty of Linguistics & Communication • ULIS - VNU' : 'Lớp 6 - Nhóm 1 - Khóa 127 • Khoa Ngôn ngữ & Truyền thông • Trường Đại học Ngoại ngữ - ĐHQGHN'}</span>
        </div>
      </div>

      <!-- Academic Advisory Banner -->
      <div style="background:#FFF; border:1px solid var(--color-border-hairline); border-radius:12px; padding:1.5rem 1.75rem; box-shadow:0 4px 16px rgba(0,0,0,0.04); margin-bottom:1.5rem; display:flex; align-items:center; gap:1.25rem;">
        <div style="width:60px; height:60px; border-radius:50%; background:var(--color-surface-blush); color:var(--color-brand-primary); display:flex; align-items:center; justify-content:center; font-size:1.75rem; font-weight:800; flex-shrink:0;">
          <i class="fas fa-graduation-cap"></i>
        </div>
        <div>
          <h3 style="font-family:var(--font-editorial); font-size:1.2rem; font-weight:800; color:var(--color-brand-primary); margin:0 0 0.25rem 0;">
            ${isEn ? 'Academic Advisory & Faculty Supervision' : 'Hội Đồng Cố Vấn Học Thuật & Bảo Trợ Chuyên Môn'}
          </h3>
          <p style="font-size:0.875rem; color:var(--color-text-body); margin:0; line-height:1.6;">
            ${isEn ? 'Faculty of Linguistics & Communication • University of Languages and International Studies - Vietnam National University, Hanoi (ULIS - VNU). Guiding journalistic rigor, media ethics, and foreign-language publication standards.' : 'Khoa Ngôn ngữ & Truyền thông • Trường Đại học Ngoại ngữ - Đại học Quốc gia Hà Nội (ULIS - VNU). Bảo trợ định hướng chính luận, kiểm định nghiệp vụ báo chí và đạo đức truyền thông đối ngoại.'}
          </p>
        </div>
      </div>

      <!-- 5 Authentic Editorial Profiles from [BCTT] Profiles.docx -->
      <div class="profiles-grid">
        <!-- 1. Nguyễn Thị Ngọc Mai (Editor-in-Chief) -->
        <article class="profile-card">
          <div>
            <div class="profile-header-wrap">
              <div class="profile-avatar-circle">NM</div>
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
              <div class="profile-avatar-circle">HA</div>
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
              <div class="profile-avatar-circle">PA</div>
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
              <div class="profile-avatar-circle">BN</div>
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
              <div class="profile-avatar-circle">NQ</div>
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

    <!-- SECTION 4: MISSION & EDITORIAL STANDARDS (#mission) -->
    <section id="mission" style="margin-bottom: 3.5rem; scroll-margin-top: 100px;">
      <div class="nhandan-section-header">
        <div class="nhandan-sec-title-wrap">
          <span class="nhandan-sec-ribbon"></span>
          <h2 class="nhandan-sec-title" data-i18n="std_sec_title">${isEn ? 'EDITORIAL STANDARDS & CODE OF ETHICS' : 'CHUẨN MỰC XUẤT BẢN & ĐẠO ĐỨC TÒA SOẠN'}</h2>
          <span class="nhandan-sec-sub">${isEn ? 'Stories that speak to the heart — Where news begins with a heartbeat' : 'Nơi tin tức khởi nguồn từ nhịp đập trái tim và lòng trắc ẩn'}</span>
        </div>
      </div>

      <div style="background:#FFF; border:1px solid var(--color-border-hairline); border-radius:12px; padding:2rem; line-height:1.7; color:var(--color-text-body); box-shadow:0 4px 16px rgba(0,0,0,0.04);">
        <p style="font-size:1.05rem; font-family:var(--font-editorial); font-style:italic; color:var(--color-brand-primary); margin-bottom:1.25rem;">
          ${isEn ? '“Authentic beauty in digital journalism lies not in sensational clickbait, but in humanistic depth, the elegance of typography, and gentle stories that touch readers\\\' hearts.”' : '“Cái đẹp chân thực của báo chí số không nằm ở những giật gân, câu khách, mà ở chiều sâu nhân văn, sự thanh lịch của con chữ và những câu chuyện tử tế chạm đến đáy lòng độc giả.”'}
        </p>

        <p>
          ${isEn ? '<strong>HEARTICLES.</strong> is founded and developed by <strong>Class 6 - Group 1 - Term 127</strong> at the <strong>University of Languages and International Studies - Vietnam National University, Hanoi (ULIS - VNU)</strong> as the capstone publication for the Journalism & Media Communications (BCTT) curriculum.' : '<strong>HEARTICLES.</strong> được sáng lập và phát triển bởi <strong>Lớp 6 - Nhóm 1 - Khóa 127</strong> thuộc <strong>Trường Đại học Ngoại ngữ - Đại học Quốc gia Hà Nội (ULIS - VNU)</strong> như một ấn phẩm xuất bản đa phương tiện cho học phần Báo chí &amp; Truyền thông (BCTT).'}
        </p>

        <!-- 3 Pillars directly from [BCTT] Profiles.docx -->
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:1.25rem; margin:1.5rem 0;">
          <div style="background:var(--color-surface-blush); padding:1.25rem; border-radius:8px; border-left:4px solid var(--color-brand-primary);">
            <h4 style="color:var(--color-brand-primary); margin-bottom:0.4rem; font-weight:800;" data-i18n="std_accuracy_title"><i class="fas fa-check-circle"></i> ${isEn ? 'Accuracy & Objectivity' : 'Chính Xác & Khách Quan'}</h4>
            <p style="font-size:0.8125rem; margin:0;" data-i18n="std_accuracy_desc">${isEn ? 'Every publication undergoes rigorous fact-checking and cross-referencing with credible sources.' : 'Mọi tác phẩm xuất bản đều trải qua quy trình kiểm chứng sự thật nghiêm ngặt và đối chiếu đa chiều với các nguồn tin báo chí uy tín.'}</p>
          </div>
          <div style="background:var(--color-surface-blush); padding:1.25rem; border-radius:8px; border-left:4px solid var(--color-brand-primary);">
            <h4 style="color:var(--color-brand-primary); margin-bottom:0.4rem; font-weight:800;" data-i18n="std_ethics_title"><i class="fas fa-heart"></i> ${isEn ? 'Ethical Integrity' : 'Liêm Chính & Đạo Đức Nghề Báo'}</h4>
            <p style="font-size:0.8125rem; margin:0;" data-i18n="std_ethics_desc">${isEn ? 'We adhere strictly to professional journalism ethics, actively avoiding clickbait and misleading information.' : 'Chúng tôi tuân thủ nghiêm ngặt đạo đức báo chí chuyên nghiệp, chủ động bài trừ giật gân, câu view và thông tin gây hiểu lầm.'}</p>
          </div>
          <div style="background:var(--color-surface-blush); padding:1.25rem; border-radius:8px; border-left:4px solid var(--color-brand-primary);">
            <h4 style="color:var(--color-brand-primary); margin-bottom:0.4rem; font-weight:800;" data-i18n="std_ux_title"><i class="fas fa-feather"></i> ${isEn ? 'Modern Reader Experience' : 'Trải Nghiệm Độc Giả Hiện Đại'}</h4>
            <p style="font-size:0.8125rem; margin:0;" data-i18n="std_ux_desc">${isEn ? 'We leverage multimedia formats and clean design to make quality news accessible and engaging.' : 'Ứng dụng định dạng đa phương tiện và ngôn ngữ thiết kế tối giản, tinh tế để tin tức chất lượng cao tiếp cận độc giả một cách gần gũi và hấp dẫn.'}</p>
          </div>
        </div>

        <p style="font-size:0.85rem; color:var(--color-text-muted); margin-bottom:0;">
          ${isEn ? 'Official Academic Attribution: Class 6 - Group 1 - Term 127 • Faculty of Linguistics & Communication • ULIS - VNU • Hanoi, Vietnam.' : 'Thông tin pháp lý & học thuật: Lớp 6 - Nhóm 1 - Khóa 127 • Khoa Ngôn ngữ & Truyền thông • Trường Đại học Ngoại ngữ - ĐHQGHN.'}
        </p>
      </div>
    </section>
  `;
}"""

# Replace in app.js
start_marker = "function renderAboutUsSection() {"
end_marker = "function setupPoll() {"

start_pos = code.find(start_marker)
end_pos = code.find(end_marker)

if start_pos != -1 and end_pos != -1:
    code = code[:start_pos] + new_about_section + "\n\n" + code[end_pos:]
    with open(app_js_path, 'w', encoding='utf-8') as f:
        f.write(code)
    print("SUCCESS: Updated renderAboutUsSection() with authentic profiles from docx!")
else:
    print(f"ERROR: Could not locate markers in app.js! start={start_pos}, end={end_pos}")
