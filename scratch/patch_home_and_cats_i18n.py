# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/build_multi_pages.py', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    # Top cluster lead
    (
        '<span class="nhandan-flag-badge"><i class="fas fa-landmark"></i> TIÊU ĐIỂM BÁO CHÍ ĐỐI NGOẠI</span>',
        '<span class="nhandan-flag-badge" data-i18n="focal_badge"><i class="fas fa-landmark"></i> TIÊU ĐIỂM BÁO CHÍ ĐỐI NGOẠI</span>'
    ),
    (
        '<h1 class="lead-main-headline">\n            Lawmakers propose measures to boost development in mountainous, border regions\n          </h1>',
        '<h1 class="lead-main-headline" data-i18n="focal_lead_title">\n            Lawmakers propose measures to boost development in mountainous, border regions\n          </h1>'
    ),
    (
        '<p class="lead-sapo-text">\n            Đại biểu Quốc hội đề xuất các giải pháp đột phá nhằm phát huy thế mạnh vùng, tăng cường kết nối hạ tầng giao thông và thúc đẩy kinh tế - xã hội các tỉnh miền núi, biên giới phía Bắc.\n          </p>',
        '<p class="lead-sapo-text" data-i18n="focal_lead_sapo">\n            Đại biểu Quốc hội đề xuất các giải pháp đột phá nhằm phát huy thế mạnh vùng, tăng cường kết nối hạ tầng giao thông và thúc đẩy kinh tế - xã hội các tỉnh miền núi, biên giới phía Bắc.\n          </p>'
    ),
    (
        '<span class="lead-author-tag"><i class="far fa-user"></i> Đoàn Thị Lê An &amp; NDO</span>',
        '<span class="lead-author-tag" data-i18n="focal_lead_author"><i class="far fa-user"></i> Đoàn Thị Lê An &amp; NDO</span>'
    ),
    (
        '<span class="lead-time-tag"><i class="far fa-clock"></i> 5 min read • Báo Nhân Dân</span>',
        '<span class="lead-time-tag" data-i18n="focal_lead_meta"><i class="far fa-clock"></i> 5 min read • Báo Nhân Dân</span>'
    ),
    (
        '<span class="related-news-title">Chiến dịch 500 ngày đêm ADN: Trả lại danh tính cho gần 800 hài cốt liệt sĩ</span>',
        '<span class="related-news-title" data-i18n="focal_related_1">Chiến dịch 500 ngày đêm ADN: Trả lại danh tính cho gần 800 hài cốt liệt sĩ</span>'
    ),
    (
        '<span class="related-news-title">Trí tuệ nhân tạo trong báo chí hiện đại: Tăng tốc quy trình nhưng giữ trọn đạo đức nhân văn</span>',
        '<span class="related-news-title" data-i18n="focal_related_2">Trí tuệ nhân tạo trong báo chí hiện đại: Tăng tốc quy trình nhưng giữ trọn đạo đức nhân văn</span>'
    ),

    # Sub-lead 1
    (
        '<h3 class="sublead-title">The Kindness of Strangers: In 1989 I lost a wallet with $1,000</h3>',
        '<h3 class="sublead-title" data-i18n="sublead_title_1">The Kindness of Strangers: In 1989 I lost a wallet with $1,000</h3>'
    ),
    (
        '<p class="sublead-excerpt">Cặp vợ chồng xa lạ đã vượt qua hành trình nghìn dặm tại Australia để trao tận tay chiếc ví đánh rơi chứa toàn bộ gia tài.</p>',
        '<p class="sublead-excerpt" data-i18n="sublead_excerpt_1">Cặp vợ chồng xa lạ đã vượt qua hành trình nghìn dặm tại Australia để trao tận tay chiếc ví đánh rơi chứa toàn bộ gia tài.</p>'
    ),
    (
        '<span class="sublead-meta"><i class="far fa-clock"></i> 5 min read • The Guardian</span>',
        '<span class="sublead-meta" data-i18n="sublead_meta_1"><i class="far fa-clock"></i> 5 min read • The Guardian</span>'
    ),

    # Sub-lead 2
    (
        '<span class="sublead-cat-tag">VĂN HÓA DI SẢN</span>',
        '<span class="sublead-cat-tag" data-i18n="sublead_cat_2">VĂN HÓA DI SẢN</span>'
    ),
    (
        '<h3 class="sublead-title">Gánh mưu sinh: Hồn cốt bình dị trên từng góc phố cổ Hội An</h3>',
        '<h3 class="sublead-title" data-i18n="sublead_title_2">Gánh mưu sinh: Hồn cốt bình dị trên từng góc phố cổ Hội An</h3>'
    ),
    (
        '<p class="sublead-excerpt">Hình ảnh đôi quang gánh trĩu nặng nhịp sống mưu sinh và vẻ đẹp cần lao mộc mạc trên từng ngõ nhỏ di sản rêu phong.</p>',
        '<p class="sublead-excerpt" data-i18n="sublead_excerpt_2">Hình ảnh đôi quang gánh trĩu nặng nhịp sống mưu sinh và vẻ đẹp cần lao mộc mạc trên từng ngõ nhỏ di sản rêu phong.</p>'
    ),
    (
        '<span class="sublead-meta"><i class="far fa-clock"></i> 6 min read • VnExpress</span>',
        '<span class="sublead-meta" data-i18n="sublead_meta_2"><i class="far fa-clock"></i> 6 min read • VnExpress</span>'
    ),

    # Timeline feed
    (
        '<h2 class="timeline-widget-title">DÒNG THỜI SỰ 24/7</h2>',
        '<h2 class="timeline-widget-title" data-i18n="timeline_title">DÒNG THỜI SỰ 24/7</h2>'
    ),
    (
        '<span class="timeline-badge-today">Hôm nay</span>',
        '<span class="timeline-badge-today" data-i18n="timeline_today">Hôm nay</span>'
    ),
    (
        '<p class="timeline-headline">Cost of Living Crisis: Sáng kiến Vale Pantry bảo toàn phẩm giá người nhận</p>',
        '<p class="timeline-headline" data-i18n="timeline_item_1">Cost of Living Crisis: Sáng kiến Vale Pantry bảo toàn phẩm giá người nhận</p>'
    ),
    (
        '<p class="timeline-headline">Vương quốc Anh tăng mức chứng minh tài chính đối với du học sinh quốc tế</p>',
        '<p class="timeline-headline" data-i18n="timeline_item_2">Vương quốc Anh tăng mức chứng minh tài chính đối với du học sinh quốc tế</p>'
    ),
    (
        '<p class="timeline-headline">Taeyang (BigBang) liên tục nhắc đến phở và \'show tuyệt nhất\' tại SVĐ Mỹ Đình</p>',
        '<p class="timeline-headline" data-i18n="timeline_item_3">Taeyang (BigBang) liên tục nhắc đến phở và \'show tuyệt nhất\' tại SVĐ Mỹ Đình</p>'
    ),
    (
        '<p class="timeline-headline">A new start after 60: Ở tuổi 26 mơ về Porsche, tuổi 68 tự tay chế tạo</p>',
        '<p class="timeline-headline" data-i18n="timeline_item_4">A new start after 60: Ở tuổi 26 mơ về Porsche, tuổi 68 tự tay chế tạo</p>'
    ),
    (
        '<p class="timeline-headline">Nông dân Gruver, Texas tự nguyện canh tác gây quỹ 400.000 USD học bổng</p>',
        '<p class="timeline-headline" data-i18n="timeline_item_5">Nông dân Gruver, Texas tự nguyện canh tác gây quỹ 400.000 USD học bổng</p>'
    ),
    (
        '<a href="trending.html" class="timeline-view-all">Xem tất cả dòng sự kiện &rarr;</a>',
        '<a href="trending.html" class="timeline-view-all" data-i18n="timeline_view_all">Xem tất cả dòng sự kiện &rarr;</a>'
    ),

    # Megastory
    (
        '<span class="megastory-badge"><i class="fas fa-bolt"></i> ĐẶC BIỆT · E-MAGAZINE</span>',
        '<span class="megastory-badge" data-i18n="megastory_badge"><i class="fas fa-bolt"></i> ĐẶC BIỆT · E-MAGAZINE</span>'
    ),
    (
        '<span class="megastory-serial-tag">SỐ PHÁT HÀNH ĐẶC BIỆT</span>',
        '<span class="megastory-serial-tag" data-i18n="megastory_serial">SỐ PHÁT HÀNH ĐẶC BIỆT</span>'
    ),
    (
        '<h2 class="megastory-main-title">“Tôi được trao cơ hội thứ hai để sống”</h2>',
        '<h2 class="megastory-main-title" data-i18n="megastory_title">“Tôi được trao cơ hội thứ hai để sống”</h2>'
    ),
    (
        '<p class="megastory-sapo-text">\n            Hành trình sống sót kỳ diệu của Qusay Hussein sau vụ đánh bom thảm khốc và câu chuyện xúc động về tình thương, lòng trắc ẩn cứu rỗi cuộc đời.\n          </p>',
        '<p class="megastory-sapo-text" data-i18n="megastory_sapo">\n            Hành trình sống sót kỳ diệu của Qusay Hussein sau vụ đánh bom thảm khốc và câu chuyện xúc động về tình thương, lòng trắc ẩn cứu rỗi cuộc đời.\n          </p>'
    ),
    (
        '<button class="megastory-action-btn">Khám phá tác phẩm Megastory &rarr;</button>',
        '<button class="megastory-action-btn" data-i18n="megastory_btn">Khám phá tác phẩm Megastory &rarr;</button>'
    ),
    (
        '<span class="megastory-meta-pill"><i class="far fa-clock"></i> 8 min read • The Guardian Special</span>',
        '<span class="megastory-meta-pill" data-i18n="megastory_readtime"><i class="far fa-clock"></i> 8 min read • The Guardian Special</span>'
    ),
    (
        '<p class="megastory-caption-quote">\n            Qusay Hussein: "Nghịch cảnh không thể tước đoạt đi ánh sáng trong tâm hồn. Lòng trắc ẩn của những con người xa lạ đã tái sinh tôi một lần nữa."\n          </p>',
        '<p class="megastory-caption-quote" data-i18n="megastory_caption">\n            Qusay Hussein: "Nghịch cảnh không thể tước đoạt đi ánh sáng trong tâm hồn. Lòng trắc ẩn của những con người xa lạ đã tái sinh tôi một lần nữa."\n          </p>'
    ),

    # Society section
    (
        '<h2 class="nhandan-sec-title">XÃ HỘI &amp; ĐỜI SỐNG DÂN SINH</h2>',
        '<h2 class="nhandan-sec-title" data-i18n="society_sec_title">XÃ HỘI &amp; ĐỜI SỐNG DÂN SINH</h2>'
    ),
    (
        '<span class="nhandan-sec-sub">Chuyên đề an sinh, bình đẳng và các mô hình tương trợ cộng đồng</span>',
        '<span class="nhandan-sec-sub" data-i18n="society_sec_sub">Chuyên đề an sinh, bình đẳng và các mô hình tương trợ cộng đồng</span>'
    ),
    (
        '<a href="society.html" class="nhandan-sec-more">Chuyên mục Society &rarr;</a>',
        '<a href="society.html" class="nhandan-sec-more" data-i18n="society_sec_more">Chuyên mục Society &rarr;</a>'
    ),
    (
        '<span class="society-flag-badge"><i class="fas fa-globe-europe"></i> DÂN SINH TOÀN CẦU</span>',
        '<span class="society-flag-badge" data-i18n="society_lead_tag"><i class="fas fa-globe-europe"></i> DÂN SINH TOÀN CẦU</span>'
    ),
    (
        '<h3 class="society-main-headline">Cost of Living Crisis: Sáng kiến cộng đồng bảo toàn phẩm giá người nhận</h3>',
        '<h3 class="society-main-headline" data-i18n="society_lead_headline">Cost of Living Crisis: Sáng kiến cộng đồng bảo toàn phẩm giá người nhận</h3>'
    ),
    (
        '<p class="society-sapo-desc">Mô hình siêu thị cộng đồng The Vale Pantry tại Dorset (Anh) không chỉ cung cấp thực phẩm giá rẻ mà trao quyền tự chủ và phẩm giá cho các gia đình khó khăn giữa khủng hoảng chi phí sinh hoạt.</p>',
        '<p class="society-sapo-desc" data-i18n="society_lead_desc">Mô hình siêu thị cộng đồng The Vale Pantry tại Dorset (Anh) không chỉ cung cấp thực phẩm giá rẻ mà trao quyền tự chủ và phẩm giá cho các gia đình khó khăn giữa khủng hoảng chi phí sinh hoạt.</p>'
    ),

    # Photojournalism section
    (
        '<h2 class="photo-sec-title">PHÓNG SỰ ẢNH &amp; KHOẢNH KHẮC BÁO CHÍ</h2>',
        '<h2 class="photo-sec-title" data-i18n="photo_sec_title">PHÓNG SỰ ẢNH &amp; KHOẢNH KHẮC BÁO CHÍ</h2>'
    ),
    (
        '<span class="photo-sec-sub">Hình ảnh phóng sự chân thực trích xuất 100% từ hồ sơ tài nguyên [BCTT]</span>',
        '<span class="photo-sec-sub" data-i18n="photo_sec_sub">Hình ảnh phóng sự chân thực trích xuất 100% từ hồ sơ tài nguyên [BCTT]</span>'
    ),
    (
        '<a href="in-depth.html" class="photo-sec-more">Xem thêm phóng sự ảnh &rarr;</a>',
        '<a href="in-depth.html" class="photo-sec-more" data-i18n="photo_sec_more">Xem thêm phóng sự ảnh &rarr;</a>'
    ),
    (
        '<span class="photo-kicker">PHÓNG SỰ ĐẶC BIỆT</span>',
        '<span class="photo-kicker" data-i18n="photo_hero_kicker">PHÓNG SỰ ĐẶC BIỆT</span>'
    ),
    (
        '<h3 class="photo-hero-title">Cánh đồng nghĩa tình Texas: Nông dân gây quỹ $400.000 học bổng</h3>',
        '<h3 class="photo-hero-title" data-i18n="photo_hero_title">Cánh đồng nghĩa tình Texas: Nông dân gây quỹ $400.000 học bổng</h3>'
    ),
    (
        '<p class="photo-hero-desc">Cộng đồng nông dân Gruver, Texas tự nguyện canh tác 640 mẫu đất để trao tặng học bổng đại học cho toàn bộ thế hệ trẻ trong thị trấn.</p>',
        '<p class="photo-hero-desc" data-i18n="photo_hero_excerpt">Cộng đồng nông dân Gruver, Texas tự nguyện canh tác 640 mẫu đất để trao tặng học bổng đại học cho toàn bộ thế hệ trẻ trong thị trấn.</p>'
    ),

    # Video section
    (
        '<h2 class="nhandan-sec-title">TRUNG TÂM VIDEO &amp; ĐA PHƯƠNG TIỆN</h2>',
        '<h2 class="nhandan-sec-title" data-i18n="video_sec_title">TRUNG TÂM VIDEO &amp; ĐA PHƯƠNG TIỆN</h2>'
    ),
    (
        '<span class="video-live-badge"><i class="fas fa-broadcast-tower"></i> MULTIMEDIA HUB</span>',
        '<span class="video-live-badge" data-i18n="video_sec_badge"><i class="fas fa-broadcast-tower"></i> MULTIMEDIA HUB</span>'
    ),

    # Op-ed & Poll
    (
        '<span class="opinion-kicker">GÓC NHÌN &amp; BÌNH LUẬN CHUYÊN GIA</span>',
        '<span class="opinion-kicker" data-i18n="opinion_badge">GÓC NHÌN &amp; BÌNH LUẬN CHUYÊN GIA</span>'
    ),
    (
        '<span class="opinion-edition">SỐ THÁNG NÀY</span>',
        '<span class="opinion-edition" data-i18n="opinion_edition">SỐ THÁNG NÀY</span>'
    ),
    (
        '<h4 class="opinion-author-name">PGS. TS. Trần Đình Quân</h4>',
        '<h4 class="opinion-author-name" data-i18n="opinion_author_name">PGS. TS. Trần Đình Quân</h4>'
    ),
    (
        '<p class="opinion-author-title">Viện Nghiên cứu Truyền thông &amp; Đổi mới Báo chí</p>',
        '<p class="opinion-author-title" data-i18n="opinion_author_title">Viện Nghiên cứu Truyền thông &amp; Đổi mới Báo chí</p>'
    ),
    (
        '<span class="poll-kicker"><i class="fas fa-poll-h"></i> Ý KIẾN BẠN ĐỌC</span>',
        '<span class="poll-kicker" data-i18n="poll_badge"><i class="fas fa-poll-h"></i> Ý KIẾN BẠN ĐỌC</span>'
    ),
    (
        '<h3 class="poll-question">Theo bạn, yếu tố nào quan trọng nhất định hình một tờ báo điện tử chất lượng?</h3>',
        '<h3 class="poll-question" data-i18n="poll_question">Theo bạn, yếu tố nào quan trọng nhất định hình một tờ báo điện tử chất lượng?</h3>'
    ),

    # Culture section
    (
        '<h2 class="nhandan-sec-title">VĂN HÓA, TÂM HỒN &amp; KÝ SỰ CHUYÊN SÂU</h2>',
        '<h2 class="nhandan-sec-title" data-i18n="culture_sec_title">VĂN HÓA, TÂM HỒN &amp; KÝ SỰ CHUYÊN SÂU</h2>'
    ),
    (
        '<span class="nhandan-sec-sub">Nghệ thuật sống chậm, sức khỏe toàn diện và phóng sự dài kỳ</span>',
        '<span class="nhandan-sec-sub" data-i18n="culture_sec_sub">Nghệ thuật sống chậm, sức khỏe toàn diện và phóng sự dài kỳ</span>'
    ),
    (
        '<span class="culture-tag">ÂM NHẠC &amp; VĂN HÓA</span>',
        '<span class="culture-tag" data-i18n="culture_hero_tag">ÂM NHẠC &amp; VĂN HÓA</span>'
    ),
    (
        '<h3 class="culture-hero-title">Sau concert Mỹ Đình, Taeyang (BigBang) liên tục nhắc đến phở và \'show tuyệt nhất\'</h3>',
        '<h3 class="culture-hero-title" data-i18n="culture_hero_title">Sau concert Mỹ Đình, Taeyang (BigBang) liên tục nhắc đến phở và \'show tuyệt nhất\'</h3>'
    ),
    (
        '<p class="culture-hero-excerpt">Nam nghệ sĩ hàng đầu xứ kim chi bày tỏ tình cảm chân thành với khán giả Việt Nam sau hai đêm bùng nổ của tour diễn kỷ niệm 20 năm tại Thủ đô Hà Nội.</p>',
        '<p class="culture-hero-excerpt" data-i18n="culture_hero_excerpt">Nam nghệ sĩ hàng đầu xứ kim chi bày tỏ tình cảm chân thành với khán giả Việt Nam sau hai đêm bùng nổ của tour diễn kỷ niệm 20 năm tại Thủ đô Hà Nội.</p>'
    ),

    # Category bodies desc, kickers, titles, excerpts, buttons, sidebar
    # Trending
    (
        '<p class="category-page-desc">\n        Nhịp đập xu hướng, những câu chuyện thịnh hành và chuyển động văn hóa xã hội nóng hổi trích xuất từ tài nguyên chính thống [BCTT] Trending.\n      </p>',
        '<p class="category-page-desc" data-i18n="trending_desc">\n        Nhịp đập xu hướng, những câu chuyện thịnh hành và chuyển động văn hóa xã hội nóng hổi trích xuất từ tài nguyên chính thống [BCTT] Trending.\n      </p>'
    ),
    (
        '<span class="category-featured-kicker">TIÊU ĐIỂM CHUYÊN MỤC · BÀI 4 TRENDING</span>',
        '<span class="category-featured-kicker" data-i18n="cat_feat_trending_kicker">TIÊU ĐIỂM CHUYÊN MỤC · BÀI 4 TRENDING</span>'
    ),
    (
        '<h2 class="category-featured-title">Gánh mưu sinh: Hồn cốt bình dị trên từng góc phố cổ Hội An</h2>',
        '<h2 class="category-featured-title" data-i18n="cat_feat_trending_title">Gánh mưu sinh: Hồn cốt bình dị trên từng góc phố cổ Hội An</h2>'
    ),
    (
        '<p class="category-featured-excerpt">\n        Hình ảnh đôi quang gánh trĩu nặng nhịp sống mưu sinh, vẻ đẹp cần lao mộc mạc và ký ức rêu phong trên từng ngõ nhỏ di sản được khắc họa xúc động qua lăng kính phóng sự VnExpress.\n      </p>',
        '<p class="category-featured-excerpt" data-i18n="cat_feat_trending_excerpt">\n        Hình ảnh đôi quang gánh trĩu nặng nhịp sống mưu sinh, vẻ đẹp cần lao mộc mạc và ký ức rêu phong trên từng ngõ nhỏ di sản được khắc họa xúc động qua lăng kính phóng sự VnExpress.\n      </p>'
    ),

    # Society
    (
        '<p class="category-page-desc">\n        Những vấn đề dân sinh, chính sách tài chính du học, khủng hoảng sinh hoạt phí và các mô hình tương trợ cộng đồng văn minh trích xuất từ [BCTT] Society.\n      </p>',
        '<p class="category-page-desc" data-i18n="society_desc">\n        Những vấn đề dân sinh, chính sách tài chính du học, khủng hoảng sinh hoạt phí và các mô hình tương trợ cộng đồng văn minh trích xuất từ [BCTT] Society.\n      </p>'
    ),
    (
        '<span class="category-featured-kicker">TIÊU ĐIỂM DÂN SINH · THE GUARDIAN</span>',
        '<span class="category-featured-kicker" data-i18n="cat_feat_society_kicker">TIÊU ĐIỂM DÂN SINH · THE GUARDIAN</span>'
    ),
    (
        '<h2 class="category-featured-title">Cost of Living Crisis: Sáng kiến cộng đồng bảo toàn phẩm giá người nhận</h2>',
        '<h2 class="category-featured-title" data-i18n="cat_feat_society_title">Cost of Living Crisis: Sáng kiến cộng đồng bảo toàn phẩm giá người nhận</h2>'
    ),
    (
        '<p class="category-featured-excerpt">\n        Mô hình siêu thị cộng đồng The Vale Pantry tại Dorset (Anh) không chỉ cung cấp thực phẩm giá rẻ mà trao quyền tự chủ và phẩm giá cho các gia đình khó khăn giữa khủng hoảng chi phí sinh hoạt.\n      </p>',
        '<p class="category-featured-excerpt" data-i18n="cat_feat_society_excerpt">\n        Mô hình siêu thị cộng đồng The Vale Pantry tại Dorset (Anh) không chỉ cung cấp thực phẩm giá rẻ mà trao quyền tự chủ và phẩm giá cho các gia đình khó khăn giữa khủng hoảng chi phí sinh hoạt.\n      </p>'
    ),

    # Human Stories
    (
        '<p class="category-page-desc">\n        Những mảnh đời chạm đến trái tim, nghị lực phi thường và cử chỉ tử tế thắp sáng niềm tin cuộc sống trích xuất từ [BCTT] Human stories.\n      </p>',
        '<p class="category-page-desc" data-i18n="human_desc">\n        Những mảnh đời chạm đến trái tim, nghị lực phi thường và cử chỉ tử tế thắp sáng niềm tin cuộc sống trích xuất từ [BCTT] Human stories.\n      </p>'
    ),
    (
        '<span class="category-featured-kicker">CÂU CHUYỆN NGHỊ LỰC · BÀI 3 HUMAN STORIES</span>',
        '<span class="category-featured-kicker" data-i18n="cat_feat_human_kicker">CÂU CHUYỆN NGHỊ LỰC · BÀI 3 HUMAN STORIES</span>'
    ),
    (
        '<h2 class="category-featured-title">“Tôi được trao cơ hội thứ hai để sống”</h2>',
        '<h2 class="category-featured-title" data-i18n="cat_feat_human_title">“Tôi được trao cơ hội thứ hai để sống”</h2>'
    ),
    (
        '<p class="category-featured-excerpt">\n        Hành trình tái sinh kỳ diệu của người đàn ông vượt qua ranh giới sinh tử, tìm lại mục đích sống từ lòng trắc ẩn và sự tận hiến của cộng đồng.\n      </p>',
        '<p class="category-featured-excerpt" data-i18n="cat_feat_human_excerpt">\n        Hành trình tái sinh kỳ diệu của người đàn ông vượt qua ranh giới sinh tử, tìm lại mục đích sống từ lòng trắc ẩn và sự tận hiến của cộng đồng.\n      </p>'
    ),

    # Mind & Soul
    (
        '<p class="category-page-desc">\n        Nuôi dưỡng thế giới nội tâm, nghệ thuật sống chậm, sức khỏe toàn diện và vẻ đẹp văn hóa nghệ thuật trích xuất từ [BCTT] Mind &amp; Soul.\n      </p>',
        '<p class="category-page-desc" data-i18n="mind_desc">\n        Nuôi dưỡng thế giới nội tâm, nghệ thuật sống chậm, sức khỏe toàn diện và vẻ đẹp văn hóa nghệ thuật trích xuất từ [BCTT] Mind &amp; Soul.\n      </p>'
    ),
    (
        '<span class="category-featured-kicker">ÂM NHẠC &amp; VĂN HÓA · BÁO LAO ĐỘNG</span>',
        '<span class="category-featured-kicker" data-i18n="cat_feat_mind_kicker">ÂM NHẠC &amp; VĂN HÓA · BÁO LAO ĐỘNG</span>'
    ),
    (
        '<h2 class="category-featured-title">Sau concert Mỹ Đình, Taeyang (BigBang) liên tục nhắc đến phở và \'show tuyệt nhất\'</h2>',
        '<h2 class="category-featured-title" data-i18n="cat_feat_mind_title">Sau concert Mỹ Đình, Taeyang (BigBang) liên tục nhắc đến phở và \'show tuyệt nhất\'</h2>'
    ),
    (
        '<p class="category-featured-excerpt">\n        Giọng ca chính của BigBang bày tỏ niềm xúc động sâu sắc trước sự cuồng nhiệt của hàng chục nghìn khán giả Việt Nam, khẳng định Hà Nội là một trong những đêm diễn thăng hoa nhất trong sự nghiệp.\n      </p>',
        '<p class="category-featured-excerpt" data-i18n="cat_feat_mind_excerpt">\n        Giọng ca chính của BigBang bày tỏ niềm xúc động sâu sắc trước sự cuồng nhiệt của hàng chục nghìn khán giả Việt Nam, khẳng định Hà Nội là một trong những đêm diễn thăng hoa nhất trong sự nghiệp.\n      </p>'
    ),

    # In-depth
    (
        '<p class="category-page-desc">\n        Phóng sự dài kỳ, ký sự đa phương tiện, chuyên khảo văn hóa và những góc nhìn học thuật đối ngoại sâu sắc trích xuất từ [BCTT] In-dept.\n      </p>',
        '<p class="category-page-desc" data-i18n="indepth_desc">\n        Phóng sự dài kỳ, ký sự đa phương tiện, chuyên khảo văn hóa và những góc nhìn học thuật đối ngoại sâu sắc trích xuất từ [BCTT] In-dept.\n      </p>'
    ),
    (
        '<span class="category-featured-kicker">KÝ SỰ VĂN HÓA · VIETNAM NEWS</span>',
        '<span class="category-featured-kicker" data-i18n="cat_feat_indepth_kicker">KÝ SỰ VĂN HÓA · VIETNAM NEWS</span>'
    ),
    (
        '<h2 class="category-featured-title">A Hà Nội that never stands still: Nốt hương hoa sữa và ký ức mùa thu</h2>',
        '<h2 class="category-featured-title" data-i18n="cat_feat_indepth_title">A Hà Nội that never stands still: Nốt hương hoa sữa và ký ức mùa thu</h2>'
    ),
    (
        '<p class="category-featured-excerpt">\n        Giữa nhịp sống hiện đại hối hả, hương hoa sữa nồng nàn trên từng con phố vẫn lưu giữ hồn cốt trầm mặc, thanh lịch của Hà Nội nghìn năm văn hiến.\n      </p>',
        '<p class="category-featured-excerpt" data-i18n="cat_feat_indepth_excerpt">\n        Giữa nhịp sống hiện đại hối hả, hương hoa sữa nồng nàn trên từng con phố vẫn lưu giữ hồn cốt trầm mặc, thanh lịch của Hà Nội nghìn năm văn hiến.\n      </p>'
    ),

    # Common buttons and sidebar titles
    (
        '<button class="fashion-btn-pill">Đọc bài viết đầy đủ &rarr;</button>',
        '<button class="fashion-btn-pill" data-i18n="btn_read_full">Đọc bài viết đầy đủ &rarr;</button>'
    ),
    (
        '<h3 class="sidebar-widget-title"><i class="fas fa-chart-line"></i> ĐỌC NHIỀU NHẤT</h3>',
        '<h3 class="sidebar-widget-title" data-i18n="sidebar_top_read"><i class="fas fa-chart-line"></i> ĐỌC NHIỀU NHẤT</h3>'
    ),
    (
        '<h3 class="sidebar-widget-title"><i class="fas fa-tags"></i> CHỦ ĐỀ NỔI BẬT</h3>',
        '<h3 class="sidebar-widget-title" data-i18n="sidebar_topics"><i class="fas fa-tags"></i> CHỦ ĐỀ NỔI BẬT</h3>'
    ),

    # About Us hero desc
    (
        '<p class="category-page-desc">\n        "Where News Begins with a Heartbeat — Nơi tin tức khởi nguồn từ nhịp đập trái tim và lòng trắc ẩn."\n      </p>',
        '<p class="category-page-desc" data-i18n="about_hero_sub">\n        "Where News Begins with a Heartbeat — Nơi tin tức khởi nguồn từ nhịp đập trái tim và lòng trắc ẩn."\n      </p>'
    )
]

norm_text = text.replace('\r\n', '\n')
success_count = 0
for old, new in replacements:
    n_old = old.replace('\r\n', '\n')
    n_new = new.replace('\r\n', '\n')
    if n_old in norm_text:
        norm_text = norm_text.replace(n_old, n_new)
        success_count += 1
    else:
        print("Warning: could not find target:", n_old[:60])

print(f"Applied {success_count}/{len(replacements)} i18n replacements to body sections!")

with open('scratch/build_multi_pages.py', 'w', encoding='utf-8') as f:
    f.write(norm_text)
print("Saved scratch/build_multi_pages.py successfully!")
