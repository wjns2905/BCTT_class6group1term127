import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

pos_start = js.find('function renderAboutUsSection()')
pos_end = js.find('/* ===================================================================\n   ARTICLE DETAIL MODAL', pos_start)

about_body = js[pos_start:pos_end]

# Find markers
p1 = about_body.find('<!-- SECTION 1: PROFILES (#profiles) -->')
p2 = about_body.find('<!-- SECTION 2: PHOTOJOURNALISM MOSAIC (#photo) -->')
p3 = about_body.find('<!-- SECTION 3: NEWSLETTER SUBSCRIPTION (#subscribe) -->')
p4 = about_body.find('<!-- SECTION 4: MISSION & EDITORIAL PHILOSOPHY (#mission) -->')

# End of section 4 is before the closing template literal
p4_end = about_body.rfind('  `;\n}')
if p4_end == -1:
    p4_end = about_body.rfind('`;')

header_block = about_body[:p1]
profiles_block = about_body[p1:p2]
photo_block = about_body[p2:p3]
subscribe_block = about_body[p3:p4]
mission_block = about_body[p4:p4_end]
tail_block = about_body[p4_end:]

# Reorder nav buttons in header_block
old_nav = """    <nav class="about-tabs-nav" aria-label="About Us Navigation">
      <a href="#profiles" class="about-tab-btn"><i class="fas fa-users"></i> <span data-i18n="about_tab_profiles">${isEn ? 'Editorial Profiles' : 'Hồ Sơ Ban Biên Tập'}</span></a>
      <a href="#photo" class="about-tab-btn"><i class="fas fa-camera"></i> <span data-i18n="about_tab_photo">${isEn ? 'Photojournalism Gallery' : 'Kho Ảnh Phóng Sự Báo Chí'}</span></a>
      <a href="#subscribe" class="about-tab-btn"><i class="fas fa-paper-plane"></i> <span data-i18n="about_tab_subscribe">${isEn ? 'Newsletter Subscription' : 'Đăng Ký Nhận Bản Tin'}</span></a>
      <a href="#mission" class="about-tab-btn"><i class="fas fa-bullseye"></i> <span data-i18n="about_tab_mission">${isEn ? 'Mission, Ethics & Compliance' : 'Tôn Chỉ Hoạt Động & Chuẩn Mực'}</span></a>
    </nav>"""

new_nav = """    <nav class="about-tabs-nav" aria-label="About Us Navigation">
      <a href="#mission" class="about-tab-btn"><i class="fas fa-bullseye"></i> <span data-i18n="about_tab_mission">${isEn ? 'Mission, Ethics & Compliance' : 'Tôn Chỉ Hoạt Động & Chuẩn Mực'}</span></a>
      <a href="#profiles" class="about-tab-btn"><i class="fas fa-users"></i> <span data-i18n="about_tab_profiles">${isEn ? 'Editorial Profiles' : 'Hồ Sơ Ban Biên Tập'}</span></a>
      <a href="#photo" class="about-tab-btn"><i class="fas fa-camera"></i> <span data-i18n="about_tab_photo">${isEn ? 'Photojournalism Gallery' : 'Kho Ảnh Phóng Sự Báo Chí'}</span></a>
      <a href="#subscribe" class="about-tab-btn"><i class="fas fa-paper-plane"></i> <span data-i18n="about_tab_subscribe">${isEn ? 'Newsletter Subscription' : 'Đăng Ký Nhận Bản Tin'}</span></a>
    </nav>"""

header_block = header_block.replace(old_nav, new_nav)

# Adjust section comments / margins
# Mission becomes Section 1
mission_block_mod = mission_block.replace(
    '<!-- SECTION 4: MISSION & EDITORIAL PHILOSOPHY (#mission) -->',
    '<!-- SECTION 1: MISSION & EDITORIAL PHILOSOPHY (#mission) -->'
).replace(
    '<section id="mission" style="margin-bottom: 2rem; scroll-margin-top: 100px;">',
    '<section id="mission" style="margin-bottom: 3.5rem; scroll-margin-top: 100px;">'
)

# Profiles becomes Section 2
profiles_block_mod = profiles_block.replace(
    '<!-- SECTION 1: PROFILES (#profiles) -->',
    '<!-- SECTION 2: PROFILES (#profiles) -->'
)

# Photo becomes Section 3
photo_block_mod = photo_block.replace(
    '<!-- SECTION 2: PHOTOJOURNALISM MOSAIC (#photo) -->',
    '<!-- SECTION 3: PHOTOJOURNALISM MOSAIC (#photo) -->'
)

# Subscribe becomes Section 4
subscribe_block_mod = subscribe_block.replace(
    '<!-- SECTION 3: NEWSLETTER SUBSCRIPTION (#subscribe) -->',
    '<!-- SECTION 4: NEWSLETTER SUBSCRIPTION (#subscribe) -->'
).replace(
    '<section id="subscribe" style="margin-bottom: 3.5rem; scroll-margin-top: 100px;">',
    '<section id="subscribe" style="margin-bottom: 2rem; scroll-margin-top: 100px;">'
)

new_about_body = header_block + mission_block_mod + profiles_block_mod + photo_block_mod + subscribe_block_mod + tail_block

new_js = js[:pos_start] + new_about_body + js[pos_end:]

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'w', encoding='utf-8') as f:
    f.write(new_js)

print("Updated js/app.js successfully!")
