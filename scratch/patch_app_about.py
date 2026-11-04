# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos1 = text.find('function renderAboutUsSection() {')
pos2 = text.find('window.openArticleModal =', pos1)
about_old = text[pos1:pos2]

about_new = """function renderAboutUsSection() {
  const container = document.getElementById('aboutUsSection');
  if (!container) return;

  const isEn = (currentLanguage === 'en');

  const manifestoTag = isEn ? '<i class="fas fa-heart"></i> EDITORIAL MANIFESTO' : '<i class="fas fa-heart"></i> TÔN CHỈ HOẠT ĐỘNG';
  const manifestoTitle = isEn ? 'HEARTICLES. E-Magazine' : 'Tạp chí Báo điện tử HEARTICLES.';
  const manifestoSubtitle = isEn ? '"Stories that speak to the heart — Where news begins with a heartbeat"' : '"Stories that speak to the heart — Nơi tin tức khởi nguồn từ nhịp đập trái tim"';

  const p1 = isEn ? `
    <strong>HEARTICLES.</strong> was founded and published by the student editorial team of <strong>Class 6 - Group 1 - Term 127</strong> at <strong>University of Languages and International Studies - Vietnam National University, Hanoi (ULIS - VNU)</strong> within the Journalism & Communication course (BCTT), aspiring to establish a multimedia news publication with haute-couture aesthetics, international standards, and boundless compassion.
  ` : `
    <strong>HEARTICLES.</strong> được sáng lập và vận hành bởi nhóm sinh viên <strong>Lớp 6 - Nhóm 1 - Khóa 127</strong> thuộc <strong>Trường Đại học Ngoại ngữ - Đại học Quốc gia Hà Nội (ULIS - VNU)</strong> trong khuôn khổ học phần Báo chí &amp; Truyền thông (BCTT), với khát vọng kiến tạo một ấn phẩm báo chí đa phương tiện mang phong cách thời trang, chuẩn mực quốc tế và tràn đầy lòng trắc ẩn.
  `;

  const p2 = isEn ? `
    Inspired by the visual design vocabulary of iconic publications like Vogue, Harper's Bazaar, and Kinfolk, as well as the editorial model of Báo Nhân Dân online, we believe authentic beauty in journalism lies not in sensationalism or clickbait, but in humanistic depth, the elegance of typography, and gentle stories that touch readers' hearts.
  ` : `
    Lấy cảm hứng từ ngôn ngữ thẩm mỹ của các tạp chí danh tiếng như Vogue, Harper's Bazaar và Kinfolk, chúng tôi tin rằng cái đẹp chân thực của báo chí không nằm ở những giật gân, câu khách, mà ở chiều sâu nhân văn, sự thanh lịch của con chữ và những câu chuyện tử tế chạm đến đáy lòng độc giả.
  `;

  const p3 = isEn ? `
    <strong>Editorial Principle:</strong> Integrity in truth, empathy in perspective, and refined aesthetics across every page.
  ` : `
    <strong>Phương châm của tòa soạn:</strong> Trung thực trong sự thật, nhân ái trong góc nhìn, và chuẩn mực thẩm mỹ trong từng trang viết.
  `;

  const logoDesc = isEn ? 'The continuous-line hand-drawn heart symbolizes boundless empathy connecting journalists with humanity and society.' : 'Biểu trưng trái tim vẽ tay liên tục (continuous line) biểu đạt tình yêu thương nối liền giữa người làm báo và cộng đồng xã hội.';

  const teamTitle = isEn ? 'Editorial Board &amp; Academic Advisory • ULIS - VNU' : 'Ban Biên Tập &amp; Cố Vấn Tòa Soạn • ULIS - VNU';
  const role1Title = isEn ? 'Faculty Advisor' : 'Giảng viên Phụ trách';
  const role1Dept = isEn ? 'Faculty of Linguistics &amp; Communication' : 'Khoa Ngôn ngữ &amp; Truyền thông';
  const role1Desc = isEn ? 'Guiding content strategy, editorial integrity, and international journalism standards.' : 'Cố vấn định hướng nội dung và nghiệp vụ báo chí đối ngoại.';

  const role2Title = isEn ? 'Class 6 - Group 1 - Term 127' : 'Lớp 6 - Nhóm 1 - Khóa 127';
  const role2Dept = isEn ? 'Editorial &amp; Content Production Board' : 'Ban Biên tập &amp; Sản xuất Nội dung';
  const role2Desc = isEn ? 'Content creation, international news curation, and field photojournalism.' : 'Sáng tạo nội dung, biên dịch báo chí quốc tế và phóng sự thực địa.';

  const role3Title = isEn ? 'Design &amp; Engineering Team' : 'Ban Thiết kế &amp; Kỹ thuật';
  const role3Dept = isEn ? 'Creative Direction &amp; Web Dev' : 'Creative Direction &amp; Web Dev';
  const role3Desc = isEn ? 'Crafting minimalist editorial design, Nielsen Norman UX, and Impeccable architecture.' : 'Phát triển giao diện chuẩn thời trang cao cấp và hệ thống Impeccable.';

  container.innerHTML = `
    <div class="about-view-wrapper" id="about-us" style="background:#FFFFFF; border:1px solid var(--color-border-hairline); border-radius:var(--radius-lg); padding:3rem 2.5rem; margin-top:3.5rem;">
      <div class="about-hero-banner" style="text-align:center; max-width:760px; margin:0 auto 2.5rem auto;">
        <span class="fashion-kicker" style="display:inline-block; margin-bottom:0.5rem;">${manifestoTag}</span>
        <h1 class="about-manifesto-title" style="font-family:var(--font-editorial); font-size:2.4rem; font-weight:800; color:var(--color-brand-primary);">${manifestoTitle}</h1>
        <p class="about-manifesto-subtitle" style="font-family:var(--font-editorial); font-style:italic; font-size:1.25rem; color:var(--color-brand-accent); margin-top:0.4rem;">
          ${manifestoSubtitle}
        </p>
      </div>

      <div class="about-story-grid" style="display:grid; grid-template-columns:1.3fr 0.9fr; gap:2.5rem; align-items:center;">
        <div class="about-story-text" style="font-size:0.95rem; line-height:1.75; color:var(--color-text-body);">
          <p style="margin-bottom:1rem;">${p1}</p>
          <p style="margin-bottom:1rem;">${p2}</p>
          <p>${p3}</p>
        </div>

        <div class="about-story-card" style="background:var(--color-surface-blush); border:1px solid #EEDBD6; border-radius:var(--radius-lg); padding:2rem; text-align:center;">
          <svg style="width:64px; height:60px; margin:0 auto 1rem auto; display:block;" viewBox="0 0 100 80" fill="none">
            <path d="M30 45 C15 32 8 20 22 10 C32 2 44 8 50 20 C56 8 68 2 78 10 C92 20 82 36 62 55 C54 62 50 67 48 68 C45 70 42 68 40 65 C34 58 26 48 30 45 Z" stroke="#591724" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M48 68 C56 72 70 75 80 70 C88 66 94 58 98 50" stroke="#BA6975" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="3 4"/>
          </svg>
          <h2 style="font-family:var(--font-editorial); font-size:1.75rem; font-style:italic; color:var(--color-brand-primary); margin-bottom:0.25rem;">HEARTICLES.</h2>
          <p style="font-size:0.875rem; font-weight:600; color:var(--color-brand-accent); margin-bottom:1rem;">Stories that speak to the heart.</p>
          <p style="font-size:0.875rem; color:var(--color-text-body); line-height:1.6; font-weight:500;">
            ${logoDesc}
          </p>
        </div>
      </div>

      <!-- Editorial Team Grid -->
      <div style="margin-top:2.5rem; padding-top:2rem; border-top:1px solid var(--color-border-hairline);">
        <h3 style="font-family:var(--font-editorial); font-size:1.35rem; color:var(--color-text-headline); margin-bottom:1.5rem; text-align:center;">
          ${teamTitle}
        </h3>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:1.25rem;">
          <div style="background:#FFFFFF; border:1px solid var(--color-border-hairline); border-radius:var(--radius-md); padding:1.25rem; text-align:center;">
            <div style="width:48px; height:48px; border-radius:50%; background:var(--color-brand-primary); color:#FFF; display:flex; align-items:center; justify-content:center; font-weight:bold; margin:0 auto 0.75rem auto;">GV</div>
            <h4 style="font-family:var(--font-serif); font-size:1rem; font-weight:700;">${role1Title}</h4>
            <p style="font-size:0.75rem; color:var(--color-brand-accent); font-weight:600;">${role1Dept}</p>
            <p style="font-size:0.8125rem; color:var(--color-text-muted); font-weight:500; margin-top:0.3rem;">${role1Desc}</p>
          </div>
          <div style="background:#FFFFFF; border:1px solid var(--color-border-hairline); border-radius:var(--radius-md); padding:1.25rem; text-align:center;">
            <div style="width:48px; height:48px; border-radius:50%; background:var(--color-brand-accent); color:#FFF; display:flex; align-items:center; justify-content:center; font-weight:bold; margin:0 auto 0.75rem auto;">N1</div>
            <h4 style="font-family:var(--font-serif); font-size:1rem; font-weight:700;">${role2Title}</h4>
            <p style="font-size:0.75rem; color:var(--color-brand-primary); font-weight:600;">${role2Dept}</p>
            <p style="font-size:0.8125rem; color:var(--color-text-muted); font-weight:500; margin-top:0.3rem;">${role2Desc}</p>
          </div>
          <div style="background:#FFFFFF; border:1px solid var(--color-border-hairline); border-radius:var(--radius-md); padding:1.25rem; text-align:center;">
            <div style="width:48px; height:48px; border-radius:50%; background:var(--primitive-burgundy-900); color:#FFF; display:flex; align-items:center; justify-content:center; font-weight:bold; margin:0 auto 0.75rem auto;">UI</div>
            <h4 style="font-family:var(--font-serif); font-size:1rem; font-weight:700;">${role3Title}</h4>
            <p style="font-size:0.75rem; color:var(--color-brand-accent); font-weight:600;">${role3Dept}</p>
            <p style="font-size:0.8125rem; color:var(--color-text-muted); font-weight:500; margin-top:0.3rem;">${role3Desc}</p>
          </div>
        </div>
      </div>
    </div>
  `;
}

"""

text = text[:pos1] + about_new + text[pos2:]

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated renderAboutUsSection in js/app.js successfully!")
