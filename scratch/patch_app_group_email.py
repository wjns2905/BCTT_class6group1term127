# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update team card role2 in renderAboutUsSection
old_role2_block = """            <h4 style="font-family:var(--font-serif); font-size:1rem; font-weight:700;">${role2Title}</h4>
            <p style="font-size:0.75rem; color:var(--color-brand-primary); font-weight:600;">${role2Dept}</p>
            <p style="font-size:0.8125rem; color:var(--color-text-muted); font-weight:500; margin-top:0.3rem;">${role2Desc}</p>
          </div>"""

new_role2_block = """            <h4 style="font-family:var(--font-serif); font-size:1rem; font-weight:700;">${role2Title}</h4>
            <p style="font-size:0.75rem; color:var(--color-brand-primary); font-weight:600;">${role2Dept}</p>
            <p style="font-size:0.8125rem; color:var(--color-text-muted); font-weight:500; margin-top:0.3rem;">${role2Desc}</p>
            <a href="mailto:class6group1term127@gmail.com" style="display:inline-flex; align-items:center; gap:0.35rem; margin-top:0.6rem; font-size:0.75rem; font-weight:700; color:var(--color-brand-primary); text-decoration:none; background:rgba(84,17,30,0.06); padding:4px 10px; border-radius:12px; border:1px solid rgba(84,17,30,0.12);"><i class="fas fa-envelope"></i> class6group1term127@gmail.com</a>
          </div>"""

# 2. Add identity box before the last </div> in about section
old_about_end = """        </div>
      </div>
    </div>
  `;
}"""

new_about_end = """        </div>
      </div>

      <!-- Group & Course Identity Summary Box -->
      <div style="margin-top:2rem; background:rgba(84,17,30,0.03); border:1px dashed var(--color-border-hairline); border-radius:var(--radius-md); padding:1.25rem 1.75rem; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:1rem;">
        <div>
          <span style="font-size:0.75rem; font-weight:800; color:var(--color-brand-primary); letter-spacing:0.06em; text-transform:uppercase;">
            <i class="fas fa-id-card"></i> ${isEn ? 'OFFICIAL EDITORIAL & ACADEMIC ATTRIBUTION' : 'THÔNG TIN TÒA SOẠN & ĐƠN VỊ THỰC HIỆN'}
          </span>
          <p style="font-size:0.875rem; color:var(--color-text-body); margin-top:0.3rem; line-height:1.5;">
            ${isEn ? '<strong>Publication:</strong> HEARTICLES. Digital Newspaper • <strong>Curriculum:</strong> Journalism &amp; Media Studies (BCTT)' : '<strong>Ấn phẩm:</strong> Tạp chí Báo điện tử HEARTICLES. • <strong>Học phần:</strong> Báo chí &amp; Truyền thông (BCTT)'}<br>
            ${isEn ? '<strong>Author Collective:</strong> Class 6 - Group 1 - Term 127 (Faculty of Linguistics &amp; Communications, ULIS - VNU)' : '<strong>Tập thể tác giả:</strong> Lớp 6 - Nhóm 1 - Khóa 127 (Khoa Ngôn ngữ &amp; Truyền thông, Trường ĐH Ngoại ngữ - ĐHQGHN)'}
          </p>
        </div>
        <div>
          <a href="mailto:class6group1term127@gmail.com" class="academic-email-link" style="display:inline-flex; font-size:0.85rem; padding:6px 14px;">
            <i class="fas fa-paper-plane"></i> class6group1term127@gmail.com
          </a>
        </div>
      </div>
    </div>
  `;
}"""

# 3. Update openSubscribeModal
old_sub = """window.openSubscribeModal = function() {
  const email = prompt('Nhập địa chỉ email của bạn để nhận bản tin thời trang & nhân văn HEARTICLES. mỗi sáng:');
  if (email && email.includes('@')) {
    localStorage.setItem('hearticles_subscribed_email', email);
    showToast('Cảm ơn bạn! Đã đăng ký nhận bản tin thành công.', 'check-circle');
  } else if (email) {
    alert('Vui lòng nhập địa chỉ email hợp lệ.');
  }
};"""

new_sub = """window.openSubscribeModal = function() {
  const isEn = (typeof currentLanguage !== 'undefined' && currentLanguage === 'en');
  const promptMsg = isEn 
    ? 'Enter your email to subscribe to HEARTICLES. Daily Editorial (Class 6 - Group 1 - Term 127 • ULIS - VNU):' 
    : 'Nhập địa chỉ email của bạn để nhận bản tin thời trang & nhân văn HEARTICLES. (Lớp 6 - Nhóm 1 - Khóa 127 • ULIS - VNU):';
  
  const email = prompt(promptMsg);
  if (email && email.includes('@')) {
    localStorage.setItem('hearticles_subscribed_email', email);
    const successMsg = isEn 
      ? 'Thank you! Successfully subscribed. Editorial contact: class6group1term127@gmail.com' 
      : 'Cảm ơn bạn! Đã đăng ký nhận bản tin thành công. Liên hệ tòa soạn: class6group1term127@gmail.com';
    showToast(successMsg, 'check-circle');
  } else if (email) {
    alert(isEn ? 'Please enter a valid email address.' : 'Vui lòng nhập địa chỉ email hợp lệ.');
  }
};"""

norm_text = text.replace('\r\n', '\n')
norm_old_role2 = old_role2_block.replace('\r\n', '\n')
norm_new_role2 = new_role2_block.replace('\r\n', '\n')
norm_old_about_end = old_about_end.replace('\r\n', '\n')
norm_new_about_end = new_about_end.replace('\r\n', '\n')
norm_old_sub = old_sub.replace('\r\n', '\n')
norm_new_sub = new_sub.replace('\r\n', '\n')

if norm_old_role2 in norm_text:
    norm_text = norm_text.replace(norm_old_role2, norm_new_role2)
    print("SUCCESS: role2 team card updated with email!")
else:
    print("FAIL: old_role2_block not found")

if norm_old_about_end in norm_text:
    norm_text = norm_text.replace(norm_old_about_end, norm_new_about_end)
    print("SUCCESS: about us identity box added!")
else:
    print("FAIL: old_about_end not found")

if norm_old_sub in norm_text:
    norm_text = norm_text.replace(norm_old_sub, norm_new_sub)
    print("SUCCESS: openSubscribeModal updated with group info and email!")
else:
    print("FAIL: old_sub not found")

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(norm_text)
print("js/app.js updated successfully!")
