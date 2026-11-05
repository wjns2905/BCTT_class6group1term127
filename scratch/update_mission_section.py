import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

app_path = 'js/app.js'
with open(app_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Pattern for section 4: mission
old_mission_section_regex = r'(<!-- SECTION 4: MISSION & COMPLIANCE \(#mission\) -->\s*<section id="mission"[\s\S]*?<\/section>)'

new_mission_section = """<!-- SECTION 4: MISSION & EDITORIAL PHILOSOPHY (#mission) -->
    <section id="mission" style="margin-bottom: 2rem; scroll-margin-top: 100px;">
      <div class="nhandan-section-header">
        <div class="nhandan-sec-title-wrap">
          <span class="nhandan-sec-ribbon"></span>
          <h2 class="nhandan-sec-title" data-i18n="about_mission_title">${isEn ? 'MISSION & EDITORIAL PHILOSOPHY' : 'TÔN CHỈ HOẠT ĐỘNG & TRIẾT LÝ TÒA SOẠN'}</h2>
        </div>
      </div>
      <div style="background:#FFFFFF; border:1px solid var(--color-border-hairline); border-radius:var(--radius-lg); padding:2.5rem; color:var(--color-text-body); box-shadow:var(--shadow-card, 0 4px 20px rgba(0,0,0,0.03));">
        <h3 style="font-family: var(--font-editorial, 'Playfair Display', serif); font-size: 1.65rem; font-weight: 700; color: var(--color-brand-primary, #54111E); margin-top: 0; margin-bottom: 1.25rem; letter-spacing: -0.01em;">
          ${isEn ? 'Welcome to HEARTICLES' : 'Chào Mừng Đến Với HEARTICLES'}
        </h3>
        
        <p style="margin-bottom:1.25rem; font-size:1.05rem; line-height:1.8; text-align:justify;">
          ${isEn 
            ? 'Based in Hanoi, Vietnam, HEARTICLES is an academic multimedia journalism publication born out of a simple, unwavering belief: in a world driven by rapid headlines and digital noise, true journalism must never lose its soul. Every piece we publish is built upon rigorous, multi-source verification and authentic engagement with official, credible sources, ensuring that all our reporting stands as trustworthy, accurate, and deeply reliable.' 
            : 'Đặt trụ sở tại Hà Nội, Việt Nam, HEARTICLES là ấn phẩm báo chí đa phương tiện học thuật ra đời từ một niềm tin giản dị nhưng kiên định: giữa một thế giới bị cuốn theo những dòng tít chóng vánh và sự ồn ào của kỷ nguyên số, báo chí chân chính không bao giờ được đánh mất linh hồn của mình. Mọi tác phẩm chúng tôi xuất bản đều được xây dựng trên quy trình kiểm chứng đa nguồn nghiêm ngặt và sự kết nối trực tiếp với các nguồn tin chính thống, uy tín, nhằm bảo đảm mỗi bài viết luôn trung thực, chính xác và đáng tin cậy sâu sắc.'}
        </p>

        <p style="margin-bottom:1.25rem; font-size:1.05rem; line-height:1.8; text-align:justify;">
          ${isEn 
            ? 'At HEARTICLES, our editorial heart beats for human-centric storytelling. We specialize in bringing forward stories of empathy, kindness, and unsung resilience—the quiet moments of human goodness that often go unnoticed, yet remind us of our shared humanity. Our perspective reaches far beyond borders: while we honor the timeless charm and spirit of Hanoi, our lens extends across the globe to cover diverse human experiences, vibrant cultures, local food traditions, and inspiring lifestyle narratives from every corner of the world.' 
            : 'Tại HEARTICLES, trái tim biên tập của chúng tôi luôn đập cùng những câu chuyện lấy con người làm trung tâm. Chúng tôi chuyên chở những câu chuyện về sự đồng cảm, lòng trắc ẩn và sự kiên cường thầm lặng—những khoảnh khắc tốt đẹp bình dị thường bị lãng quên nhưng nhắc nhở chúng ta về sự gắn kết nhân văn. Góc nhìn của chúng tôi vươn xa khỏi mọi biên giới: vừa tôn vinh nét đẹp vượt thời gian và tinh thần của Hà Nội, ống kính của chúng tôi vừa mở rộng ra khắp thế giới để ghi lại những trải nghiệm đa dạng, các nền văn hóa sống động, nét ẩm thực bản địa cùng những câu chuyện phong cách sống đầy cảm hứng từ mọi phương trời.'}
        </p>

        <p style="margin-bottom:1.75rem; font-size:1.05rem; line-height:1.8; text-align:justify;">
          ${isEn 
            ? 'While our storytelling is rooted in deep empathy, our reporting is firmly grounded in journalistic integrity and fully verified information. We write not just to report events, but to touch hearts, build global bridges, and foster a more thoughtful, compassionate world.' 
            : 'Nếu như cách kể chuyện của chúng tôi bắt nguồn từ sự thấu cảm sâu sắc, thì phương pháp đưa tin luôn được đặt nền móng vững chắc trên đạo đức báo chí và thông tin đã được kiểm chứng tuyệt đối. Chúng tôi cầm bút không chỉ để đưa tin về các sự kiện, mà còn để chạm tới những trái tim, xây dựng những nhịp cầu kết nối toàn cầu và nuôi dưỡng một thế giới sâu lắng, giàu lòng trắc ẩn hơn.'}
        </p>

        <div style="padding-top:1.25rem; border-top:1px dashed var(--color-border-hairline); display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:0.75rem; font-size:0.875rem; color:var(--color-text-muted);">
          <span>
            <i class="fas fa-shield-alt" style="color:var(--color-brand-primary); margin-right:0.35rem;"></i>
            ${isEn ? 'Academic Multimedia Journalism Project • ULIS - VNU • Class 6 - Group 1 - Term 127' : 'Đề án Báo chí Đa phương tiện Học thuật • ULIS - VNU • Lớp 6 - Nhóm 1 - Khóa 127'}
          </span>
          <span>
            <i class="fas fa-check-circle" style="color:#2E7D32; margin-right:0.35rem;"></i>
            ${isEn ? 'Multi-Source Fact-Checking & Journalistic Ethics Compliance' : 'Kiểm chứng đa nguồn & Tuân thủ Chuẩn mực Đạo đức Báo chí'}
          </span>
        </div>
      </div>
    </section>"""

if not re.search(old_mission_section_regex, app_js):
    print("Error: Could not find old mission section in js/app.js!")
    sys.exit(1)

new_app_js = re.sub(old_mission_section_regex, new_mission_section, app_js, count=1)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(new_app_js)

print("✓ Updated section #mission in js/app.js!")

# Now update js/translations.js
trans_path = 'js/translations.js'
with open(trans_path, 'r', encoding='utf-8') as f:
    trans_js = f.read()

# Update VI dictionary
vi_replacements = {
    'about_mission_title': 'TÔN CHỈ HOẠT ĐỘNG & TRIẾT LÝ TÒA SOẠN',
    'about_manifesto_title': 'Chào Mừng Đến Với HEARTICLES',
    'about_text_p1': 'Đặt trụ sở tại Hà Nội, Việt Nam, HEARTICLES là ấn phẩm báo chí đa phương tiện học thuật ra đời từ một niềm tin giản dị nhưng kiên định: giữa một thế giới bị cuốn theo những dòng tít chóng vánh và sự ồn ào của kỷ nguyên số, báo chí chân chính không bao giờ được đánh mất linh hồn của mình. Mọi tác phẩm chúng tôi xuất bản đều được xây dựng trên quy trình kiểm chứng đa nguồn nghiêm ngặt và sự kết nối trực tiếp với các nguồn tin chính thống, uy tín, nhằm bảo đảm mỗi bài viết luôn trung thực, chính xác và đáng tin cậy sâu sắc.',
    'about_text_p2': 'Tại HEARTICLES, trái tim biên tập của chúng tôi luôn đập cùng những câu chuyện lấy con người làm trung tâm. Chúng tôi chuyên chở những câu chuyện về sự đồng cảm, lòng trắc ẩn và sự kiên cường thầm lặng—những khoảnh khắc tốt đẹp bình dị thường bị lãng quên nhưng nhắc nhở chúng ta về sự gắn kết nhân văn. Góc nhìn của chúng tôi vươn xa khỏi mọi biên giới: vừa tôn vinh nét đẹp vượt thời gian và tinh thần của Hà Nội, ống kính của chúng tôi vừa mở rộng ra khắp thế giới để ghi lại những trải nghiệm đa dạng, các nền văn hóa sống động, nét ẩm thực bản địa cùng những câu chuyện phong cách sống đầy cảm hứng từ mọi phương trời.',
    'about_text_p3': 'Nếu như cách kể chuyện của chúng tôi bắt nguồn từ sự thấu cảm sâu sắc, thì phương pháp đưa tin luôn được đặt nền móng vững chắc trên đạo đức báo chí và thông tin đã được kiểm chứng tuyệt đối. Chúng tôi cầm bút không chỉ để đưa tin về các sự kiện, mà còn để chạm tới những trái tim, xây dựng những nhịp cầu kết nối toàn cầu và nuôi dưỡng một thế giới sâu lắng, giàu lòng trắc ẩn hơn.'
}

# Update EN dictionary
en_replacements = {
    'about_mission_title': 'MISSION & EDITORIAL PHILOSOPHY',
    'about_manifesto_title': 'Welcome to HEARTICLES',
    'about_text_p1': 'Based in Hanoi, Vietnam, HEARTICLES is an academic multimedia journalism publication born out of a simple, unwavering belief: in a world driven by rapid headlines and digital noise, true journalism must never lose its soul. Every piece we publish is built upon rigorous, multi-source verification and authentic engagement with official, credible sources, ensuring that all our reporting stands as trustworthy, accurate, and deeply reliable.',
    'about_text_p2': 'At HEARTICLES, our editorial heart beats for human-centric storytelling. We specialize in bringing forward stories of empathy, kindness, and unsung resilience—the quiet moments of human goodness that often go unnoticed, yet remind us of our shared humanity. Our perspective reaches far beyond borders: while we honor the timeless charm and spirit of Hanoi, our lens extends across the globe to cover diverse human experiences, vibrant cultures, local food traditions, and inspiring lifestyle narratives from every corner of the world.',
    'about_text_p3': 'While our storytelling is rooted in deep empathy, our reporting is firmly grounded in journalistic integrity and fully verified information. We write not just to report events, but to touch hearts, build global bridges, and foster a more thoughtful, compassionate world.'
}

# Replace in trans_js
for k, v in vi_replacements.items():
    if f'{k}:' in trans_js:
        trans_js = re.sub(rf'{k}:\s*["\'].*?["\'],', f'{k}: "{v}",', trans_js, count=1)
    else:
        # insert before about_manifesto_title
        trans_js = trans_js.replace('about_manifesto_title:', f'{k}: "{v}",\n    about_manifesto_title:')

for k, v in en_replacements.items():
    pattern = rf'({k}:\s*["\'].*?["\'],)'
    matches = list(re.finditer(pattern, trans_js))
    if len(matches) >= 2:
        # second match is in EN section
        m = matches[1]
        trans_js = trans_js[:m.start()] + f'{k}: "{v}",' + trans_js[m.end():]
    elif len(matches) == 1 and k == 'about_mission_title':
        # add to EN section before about_manifesto_title in EN
        parts = trans_js.split('en: {')
        if len(parts) == 2:
            parts[1] = parts[1].replace('about_manifesto_title:', f'{k}: "{v}",\n    about_manifesto_title:', 1)
            trans_js = 'en: {'.join(parts)

with open(trans_path, 'w', encoding='utf-8') as f:
    f.write(trans_js)

print("✓ Updated js/translations.js!")
