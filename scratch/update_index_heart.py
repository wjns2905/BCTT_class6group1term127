import sys
sys.stdout.reconfigure(encoding='utf-8')

index_path = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_section = """<section class="heart-tap-container" id="heartTapSection">
      <div class="heart-tap-header">
        <h2 class="heart-tap-title" data-i18n="heart_game_title"><i class="fas fa-heartbeat" style="color:var(--color-brand-primary);"></i> Nhịp Tim Gắn Kết · Stress Reliever</h2>
        <p class="heart-tap-subtitle" data-i18n="heart_game_sub">
          Chạm vào trái tim để giải tỏa căng thẳng sau những giờ đọc tin tức. Mỗi nhịp chạm gửi gắm một thông điệp tích cực và tiếp thêm nguồn năng lượng chữa lành cho tâm hồn bạn!
        </p>
      </div>

      <div style="position:relative; display:inline-block; margin:1rem 0;">
        <button class="heart-btn-circle" id="heartTapBtn" aria-label="Tap Heart">
          <i class="fas fa-heart"></i>
        </button>
        <div id="heartParticleContainer" style="position:absolute; inset:0; pointer-events:none;"></div>
      </div>

      <div>
        <div class="heart-counter-badge" id="heartCounterBadge">
          <i class="fas fa-sparkles"></i> <span id="heartCountNumber">1,280</span> <span data-i18n="heart_count_label">nhịp đập yêu thương đã được chia sẻ</span>
        </div>
        <p class="heart-affirmation-msg" id="heartAffirmationMsg">
          “Hít một hơi thật sâu, thở ra nhẹ nhàng. Mọi chuyện rồi sẽ ổn thôi!”
        </p>
      </div>

      <div style="margin-top:1.25rem; font-size:0.8rem; color:var(--color-text-muted); display:inline-flex; align-items:center; gap:0.4rem; background:rgba(84, 17, 30, 0.04); padding:0.4rem 1rem; border-radius:var(--radius-full);">
        <i class="fas fa-hand-holding-heart" style="color:var(--color-brand-primary);"></i>
        <span data-i18n="heart_charity_cheer">Gửi năng lượng tương trợ đến quỹ học bổng trẻ em nghèo &amp; vùng cao .</span>
      </div>
    </section>"""

new_section = """<section class="heart-tap-container" id="heartTapSection">
      <div class="heart-tap-header">
        <h2 class="heart-tap-title" data-i18n="heart_game_title"><i class="fas fa-heartbeat" style="color:var(--color-brand-primary);"></i> Nhịp Tim Gắn Kết · Stress Reliever</h2>
        <p class="heart-tap-subtitle" data-i18n="heart_game_sub">
          Chạm vào trái tim để giải tỏa căng thẳng sau những giờ đọc tin tức. Mỗi nhịp chạm gửi gắm một thông điệp tích cực và tiếp thêm nguồn năng lượng chữa lành cho tâm hồn bạn!
        </p>
      </div>

      <div class="heart-tap-stage" style="position:relative; display:inline-flex; align-items:center; justify-content:center; margin:1.5rem 0;">
        <button class="heart-btn-circle" id="heartTapBtn" aria-label="Tap Heart" title="Chạm để bắn tung tóe trái tim!">
          <i class="fas fa-heart"></i>
        </button>
        <div id="heartParticleContainer" class="heart-particles-canvas" style="position:absolute; top:50%; left:50%; width:0; height:0; pointer-events:none; z-index:100;"></div>
      </div>

      <div>
        <div class="heart-counter-badge" id="heartCounterBadge">
          <i class="fas fa-sparkles"></i> <span id="heartCountNumber">1,280</span> <span data-i18n="heart_count_label">nhịp đập yêu thương đã được chia sẻ</span>
        </div>
        <p class="heart-affirmation-msg" id="heartAffirmationMsg">
          “Hít một hơi thật sâu, thở ra nhẹ nhàng. Mọi chuyện rồi sẽ ổn thôi!”
        </p>
      </div>
    </section>"""

if old_section in html:
    html = html.replace(old_section, new_section)
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated index.html heart section successfully!")
else:
    print("old_section not found directly!")
