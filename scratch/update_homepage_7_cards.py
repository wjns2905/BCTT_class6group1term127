import sys, re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace badge 6 -> 7
html = html.replace(
    '<span style="font-size:0.75rem; color:var(--color-text-muted); font-weight:700;">6 BÀI CHỌN LỌC</span>',
    '<span style="font-size:0.75rem; color:var(--color-text-muted); font-weight:700;" data-i18n="stream_curated_badge">7 BÀI CHỌN LỌC</span>'
)

# Replace trending-5 image in hero stream
html = html.replace(
    '<img src="assets/images/human_stories/image17.jpg" alt="Chiến dịch 500 ngày đêm ADN" class="stream-thumb-img" onerror="handleImageError(this)">',
    '<img src="assets/images/trending/image1.jpg" alt="Chiến dịch 500 ngày đêm ADN" class="stream-thumb-img" onerror="handleImageError(this)">'
)

# Replace human-5 image in hero stream (fixes Hoi An vendor image!)
html = html.replace(
    '<img src="assets/images/human_stories/image13.jpg" alt="Thầy giáo Nam Trà My" class="stream-thumb-img" onerror="handleImageError(this)">',
    '<img src="assets/images/human_stories/mountain_teacher_trail.jpg" alt="Thầy giáo Nam Trà My" class="stream-thumb-img" onerror="handleImageError(this)">'
)

# Replace human-2 image in mosaic
html = html.replace(
    '<img src="assets/images/human_stories/image2.jpg" alt="Kindness Bag" class="mosaic-small-img" onerror="handleImageError(this)">',
    '<img src="assets/images/human_stories/image11.jpg" alt="Kindness Bag" class="mosaic-small-img" onerror="handleImageError(this)">'
)

# Replace trending-3 image in widget and culture list
html = html.replace(
    '<img src="assets/images/trending/image4.jpg" alt="Porsche 904FF" class="widget-card-thumb" onerror="handleImageError(this)">',
    '<img src="assets/images/trending/image3.jpg" alt="Porsche 904FF" class="widget-card-thumb" onerror="handleImageError(this)">'
)
html = html.replace(
    '<img src="assets/images/trending/image4.jpg" alt="Porsche 904FF" class="culture-thumb-img" onerror="handleImageError(this)">',
    '<img src="assets/images/trending/image3.jpg" alt="Porsche 904FF" class="culture-thumb-img" onerror="handleImageError(this)">'
)

# Replace indepth-1 image in culture list
html = html.replace(
    '<img src="assets/images/human_stories/image20.jpg" alt="Hoa sữa Hà Nội" class="culture-thumb-img" onerror="handleImageError(this)">',
    '<img src="assets/images/in-dept/image2.jpg" alt="Hoa sữa Hà Nội" class="culture-thumb-img" onerror="handleImageError(this)">'
)

# Add 7th item into hero-left-stream right after society-1
card_6_target = """        <!-- 6. Society 1: Vale Pantry -->
        <article class="stream-card-mini" onclick="openArticleModal('society-1')">
          <img src="assets/images/society/image3.jpg" alt="Vale Pantry" class="stream-thumb-img" onerror="handleImageError(this)">
          <div class="stream-mini-body">
            <span class="stream-mini-cat">SOCIETY</span>
            <h4 class="stream-mini-headline">Cost of Living Crisis: Sáng kiến Vale Pantry bảo toàn phẩm giá người nhận</h4>
            <span class="stream-mini-time"><i class="far fa-clock"></i> 6 min read • The Guardian</span>
          </div>
        </article>"""

card_7_addition = """        <!-- 6. Society 1: Vale Pantry -->
        <article class="stream-card-mini" onclick="openArticleModal('society-1')">
          <img src="assets/images/society/image3.jpg" alt="Vale Pantry" class="stream-thumb-img" onerror="handleImageError(this)">
          <div class="stream-mini-body">
            <span class="stream-mini-cat">SOCIETY</span>
            <h4 class="stream-mini-headline">Cost of Living Crisis: Sáng kiến Vale Pantry bảo toàn phẩm giá người nhận</h4>
            <span class="stream-mini-time"><i class="far fa-clock"></i> 6 min read • The Guardian</span>
          </div>
        </article>

        <!-- 7. In-depth 3: Dạy lòng trắc ẩn bằng khoa học -->
        <article class="stream-card-mini" onclick="openArticleModal('indepth-3')">
          <img src="assets/images/in-dept/image3.jpg" alt="Dạy lòng trắc ẩn bằng khoa học" class="stream-thumb-img" onerror="handleImageError(this)">
          <div class="stream-mini-body">
            <span class="stream-mini-cat">IN-DEPTH</span>
            <h4 class="stream-mini-headline">Những nhà giáo dục dùng khoa học dạy lòng trắc ẩn: Khi sự tử tế là môn chính khóa</h4>
            <span class="stream-mini-time"><i class="far fa-clock"></i> 7 min read • Positive News</span>
          </div>
        </article>"""

if card_6_target in html:
    html = html.replace(card_6_target, card_7_addition)
    print("✓ Added 7th article (indepth-3) to hero-left-stream!")
else:
    # Try CRLF
    card_6_crlf = card_6_target.replace('\n', '\r\n')
    card_7_crlf = card_7_addition.replace('\n', '\r\n')
    if card_6_crlf in html:
        html = html.replace(card_6_crlf, card_7_crlf)
        print("✓ Added 7th article (CRLF) to hero-left-stream!")
    else:
        print("ERROR: card_6_target not found in index.html!")
        sys.exit(1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Saved updated index.html successfully!")
