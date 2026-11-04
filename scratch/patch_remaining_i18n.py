# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/build_multi_pages.py', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    # Megastory
    (
        '<span class="megastory-pill-gold"><i class="fas fa-award"></i> ĐẶC BIỆT · E-MAGAZINE</span>',
        '<span class="megastory-pill-gold" data-i18n="megastory_badge"><i class="fas fa-award"></i> ĐẶC BIỆT · E-MAGAZINE</span>'
    ),
    (
        '<span class="megastory-serial-no">SỐ PHÁT HÀNH ĐẶC BIỆT</span>',
        '<span class="megastory-serial-no" data-i18n="megastory_serial">SỐ PHÁT HÀNH ĐẶC BIỆT</span>'
    ),
    (
        '<h2 class="megastory-title">\n            “Tôi được trao cơ hội thứ hai để sống.”\n          </h2>',
        '<h2 class="megastory-title" data-i18n="megastory_title">\n            “Tôi được trao cơ hội thứ hai để sống.”\n          </h2>'
    ),
    (
        '<p class="megastory-sapo">\n            Hành trình sống sót kỳ diệu của Qusay Hussein sau vụ đánh bom thảm khốc và câu chuyện tái sinh phi thường giữa nghịch cảnh cùng 5 nhân vật quả cảm trên khắp thế giới.\n          </p>',
        '<p class="megastory-sapo" data-i18n="megastory_sapo">\n            Hành trình sống sót kỳ diệu của Qusay Hussein sau vụ đánh bom thảm khốc và câu chuyện tái sinh phi thường giữa nghịch cảnh cùng 5 nhân vật quả cảm trên khắp thế giới.\n          </p>'
    ),
    (
        '<button class="btn-megastory-action" onclick="event.stopPropagation(); openArticleModal(\'human-3\');">\n              Khám phá tác phẩm Megastory <i class="fas fa-arrow-right"></i>\n            </button>',
        '<button class="btn-megastory-action" onclick="event.stopPropagation(); openArticleModal(\'human-3\');" data-i18n="megastory_btn">\n              Khám phá tác phẩm Megastory <i class="fas fa-arrow-right"></i>\n            </button>'
    ),
    (
        '<span class="megastory-readtime">8 min read • The Guardian Special</span>',
        '<span class="megastory-readtime" data-i18n="megastory_readtime">8 min read • The Guardian Special</span>'
    ),
    (
        '<span>Qusay Hussein: "Nghịch cảnh không thể tước đoạt đi ánh sáng trong tâm hồn."</span>',
        '<span data-i18n="megastory_caption">Qusay Hussein: "Nghịch cảnh không thể tước đoạt đi ánh sáng trong tâm hồn."</span>'
    ),

    # Society section
    (
        '<h2 class="nhandan-sec-title">XÃ HỘI &amp; DÂN SINH</h2>',
        '<h2 class="nhandan-sec-title" data-i18n="society_sec_title">XÃ HỘI &amp; DÂN SINH</h2>'
    ),
    (
        '<span class="society-lead-tag">DÂN SINH TOÀN CẦU</span>',
        '<span class="society-lead-tag" data-i18n="society_lead_tag">DÂN SINH TOÀN CẦU</span>'
    ),
    (
        '<h3 class="society-lead-headline">Cost of Living Crisis: Sáng kiến cộng đồng bảo toàn phẩm giá người nhận</h3>',
        '<h3 class="society-lead-headline" data-i18n="society_lead_headline">Cost of Living Crisis: Sáng kiến cộng đồng bảo toàn phẩm giá người nhận</h3>'
    ),
    (
        '<p class="society-lead-desc">Mô hình siêu thị cộng đồng Vale Pantry và dự án trao tặng 3 triệu đôi giày cho trẻ em nghèo mở ra định nghĩa mới về lòng hảo tâm: Cho đi mà không làm tổn thương lòng tự trọng.</p>',
        '<p class="society-lead-desc" data-i18n="society_lead_desc">Mô hình siêu thị cộng đồng Vale Pantry và dự án trao tặng 3 triệu đôi giày cho trẻ em nghèo mở ra định nghĩa mới về lòng hảo tâm: Cho đi mà không làm tổn thương lòng tự trọng.</p>'
    ),
    (
        '<h4 class="society-mini-title">Vương quốc Anh tăng mức chứng minh tài chính đối với du học sinh quốc tế</h4>',
        '<h4 class="society-mini-title" data-i18n="society_mini_title_1">Vương quốc Anh tăng mức chứng minh tài chính đối với du học sinh quốc tế</h4>'
    ),
    (
        '<h4 class="society-mini-title">Chuyển dịch năng lượng tái tạo: Tiềm năng điện gió ngoài khơi dẫn lối tương lai</h4>',
        '<h4 class="society-mini-title" data-i18n="society_mini_title_2">Chuyển dịch năng lượng tái tạo: Tiềm năng điện gió ngoài khơi dẫn lối tương lai</h4>'
    ),

    # Photojournalism section
    (
        '<h2 class="nhandan-sec-title">PHÓNG SỰ ẢNH · NHỮNG CÂU CHUYỆN CHẠM ĐẾN TRÁI TIM</h2>',
        '<h2 class="nhandan-sec-title" data-i18n="photo_sec_title">PHÓNG SỰ ẢNH · NHỮNG CÂU CHUYỆN CHẠM ĐẾN TRÁI TIM</h2>'
    ),
    (
        '<span class="nhandan-sec-sub">Ống kính phóng sự ghi lại khoảnh khắc nhân văn và lòng quả cảm</span>',
        '<span class="nhandan-sec-sub" data-i18n="photo_sec_sub">Ống kính phóng sự ghi lại khoảnh khắc nhân văn và lòng quả cảm</span>'
    ),
    (
        '<a href="human-stories.html" class="nhandan-sec-more">Chuyên mục Human Stories &rarr;</a>',
        '<a href="human-stories.html" class="nhandan-sec-more" data-i18n="photo_sec_more">Chuyên mục Human Stories &rarr;</a>'
    ),
    (
        '<span class="mosaic-kicker"><i class="fas fa-camera"></i> PHÓNG SỰ ĐẶC BIỆT</span>',
        '<span class="mosaic-kicker" data-i18n="photo_hero_kicker"><i class="fas fa-camera"></i> PHÓNG SỰ ĐẶC BIỆT</span>'
    ),
    (
        '<h3 class="mosaic-title">Cánh đồng nghĩa tình Texas: Nông dân gây quỹ $400.000 mỗi năm cho học trò nghèo</h3>',
        '<h3 class="mosaic-title" data-i18n="photo_hero_title">Cánh đồng nghĩa tình Texas: Nông dân gây quỹ $400.000 mỗi năm cho học trò nghèo</h3>'
    ),
    (
        '<p class="mosaic-excerpt">Cộng đồng người làm nông tại Gruver, Texas tự nguyện canh tác và dành toàn bộ lợi nhuận làm học bổng giúp học sinh nghèo bước chân vào cổng trường đại học.</p>',
        '<p class="mosaic-excerpt" data-i18n="photo_hero_excerpt">Cộng đồng người làm nông tại Gruver, Texas tự nguyện canh tác và dành toàn bộ lợi nhuận làm học bổng giúp học sinh nghèo bước chân vào cổng trường đại học.</p>'
    ),
    (
        '<h4 class="mosaic-small-title">Loraine Coleman: Bữa ăn ấm áp xóa tan sự cô đơn của người già</h4>',
        '<h4 class="mosaic-small-title" data-i18n="photo_small_title_1">Loraine Coleman: Bữa ăn ấm áp xóa tan sự cô đơn của người già</h4>'
    ),
    (
        '<h4 class="mosaic-small-title">Kindness Bag cứu vớt cuộc đời cựu chiến binh và hành trình trao gửi yêu thương</h4>',
        '<h4 class="mosaic-small-title" data-i18n="photo_small_title_2">Kindness Bag cứu vớt cuộc đời cựu chiến binh và hành trình trao gửi yêu thương</h4>'
    ),

    # Video hub
    (
        '<h2 class="video-hub-title"><i class="fas fa-play-circle" style="color:var(--color-brand-primary);"></i> TRUYỀN HÌNH ĐA PHƯƠNG TIỆN</h2>',
        '<h2 class="video-hub-title" data-i18n="video_sec_title"><i class="fas fa-play-circle" style="color:var(--color-brand-primary);"></i> TRUYỀN HÌNH ĐA PHƯƠNG TIỆN</h2>'
    ),
    (
        '<span class="video-hub-badge">5 Chuyên đề video phóng sự chuẩn truyền hình</span>',
        '<span class="video-hub-badge" data-i18n="video_sec_badge">5 Chuyên đề video phóng sự chuẩn truyền hình</span>'
    ),

    # Op-ed & Poll
    (
        '<span class="opinion-badge"><i class="fas fa-feather-alt"></i> BÌNH LUẬN &amp; XÃ LUẬN</span>',
        '<span class="opinion-badge" data-i18n="opinion_badge"><i class="fas fa-feather-alt"></i> BÌNH LUẬN &amp; XÃ LUẬN</span>'
    ),
    (
        '<span class="opinion-edition">Ấn phẩm BCTT • ULIS - VNU</span>',
        '<span class="opinion-edition" data-i18n="opinion_edition">Ấn phẩm BCTT • ULIS - VNU</span>'
    ),
    (
        '<h3 class="opinion-author-name">Cố vấn Học thuật Khoa Ngôn ngữ &amp; Truyền thông</h3>',
        '<h3 class="opinion-author-name" data-i18n="opinion_author_name">Cố vấn Học thuật Khoa Ngôn ngữ &amp; Truyền thông</h3>'
    ),
    (
        '<p class="opinion-author-title">Trường Đại học Ngoại ngữ - ĐHQGHN</p>',
        '<p class="opinion-author-title" data-i18n="opinion_author_title">Trường Đại học Ngoại ngữ - ĐHQGHN</p>'
    ),
    (
        '<blockquote class="opinion-quote">\n            “Báo chí chân chính trong kỷ nguyên số không đo lường sức ảnh hưởng bằng tốc độ giật gân, mà bằng chiều sâu nhân văn và khả năng thắp sáng lòng trắc ẩn trong tâm hồn công chúng.”\n          </blockquote>',
        '<blockquote class="opinion-quote" data-i18n="opinion_quote">\n            “Báo chí chân chính trong kỷ nguyên số không đo lường sức ảnh hưởng bằng tốc độ giật gân, mà bằng chiều sâu nhân văn và khả năng thắp sáng lòng trắc ẩn trong tâm hồn công chúng.”\n          </blockquote>'
    ),
    (
        '<p class="opinion-note">Trích chuyên luận: <em>Đạo đức báo chí và sứ mệnh phụng sự xã hội của thế hệ người làm truyền thông mới</em>.</p>',
        '<p class="opinion-note" data-i18n="opinion_note">Trích chuyên luận: <em>Đạo đức báo chí và sứ mệnh phụng sự xã hội của thế hệ người làm truyền thông mới</em>.</p>'
    ),
    (
        '<div class="poll-badge"><i class="fas fa-poll"></i> THĂM DÒ Ý KIẾN BẠN ĐỌC</div>',
        '<div class="poll-badge" data-i18n="poll_badge"><i class="fas fa-poll"></i> THĂM DÒ Ý KIẾN BẠN ĐỌC</div>'
    ),
    (
        '<h3 class="poll-question">Theo bạn, các đô thị di sản như Hà Nội và Hội An nên quản lý và bảo tồn nét đẹp văn hóa gánh hàng rong như thế nào?</h3>',
        '<h3 class="poll-question" data-i18n="poll_question">Theo bạn, các đô thị di sản như Hà Nội và Hội An nên quản lý và bảo tồn nét đẹp văn hóa gánh hàng rong như thế nào?</h3>'
    ),
    (
        '<span>1. Quy hoạch các tuyến phố đi bộ văn hóa dành riêng</span>',
        '<span data-i18n="poll_opt_1">1. Quy hoạch các tuyến phố đi bộ văn hóa dành riêng</span>'
    ),
    (
        '<span>2. Tôn vinh nét đẹp văn hóa truyền thống bình dị</span>',
        '<span data-i18n="poll_opt_2">2. Tôn vinh nét đẹp văn hóa truyền thống bình dị</span>'
    ),
    (
        '<span>3. Hỗ trợ sinh kế bền vững cho người lao động nghèo</span>',
        '<span data-i18n="poll_opt_3">3. Hỗ trợ sinh kế bền vững cho người lao động nghèo</span>'
    ),

    # Featured card 3 (Human Stories)
    (
        '<h2 class="category-featured-title">“Tôi được trao cơ hội thứ hai để sống” — Qusay Hussein</h2>',
        '<h2 class="category-featured-title" data-i18n="cat_feat_human_title">“Tôi được trao cơ hội thứ hai để sống” — Qusay Hussein</h2>'
    ),

    # Featured card excerpts
    (
        '<p class="category-featured-excerpt">\n          Hình ảnh đôi quang gánh trĩu nặng nhịp sống mưu sinh, vẻ đẹp cần lao mộc mạc và ký ức rêu phong trên từng ngõ nhỏ di sản được khắc họa xúc động qua lăng kính phóng sự VnExpress.\n        </p>',
        '<p class="category-featured-excerpt" data-i18n="cat_feat_trending_excerpt">\n          Hình ảnh đôi quang gánh trĩu nặng nhịp sống mưu sinh, vẻ đẹp cần lao mộc mạc và ký ức rêu phong trên từng ngõ nhỏ di sản được khắc họa xúc động qua lăng kính phóng sự VnExpress.\n        </p>'
    ),
    (
        '<p class="category-featured-excerpt">\n          Mô hình siêu thị cộng đồng Vale Pantry và dự án trao tặng 3 triệu đôi giày cho trẻ em nghèo mở ra định nghĩa mới về lòng hảo tâm: Cho đi mà không làm tổn thương lòng tự trọng.\n        </p>',
        '<p class="category-featured-excerpt" data-i18n="cat_feat_society_excerpt">\n          Mô hình siêu thị cộng đồng Vale Pantry và dự án trao tặng 3 triệu đôi giày cho trẻ em nghèo mở ra định nghĩa mới về lòng hảo tâm: Cho đi mà không làm tổn thương lòng tự trọng.\n        </p>'
    ),
    (
        '<p class="category-featured-excerpt">\n          Sống sót kỳ diệu sau vụ đánh bom thảm khốc và mất đi thị lực, Qusay Hussein cùng 5 nhân vật phi thường chia sẻ khoảnh khắc sinh tử đã thay đổi cuộc đời họ mãi mãi.\n        </p>',
        '<p class="category-featured-excerpt" data-i18n="cat_feat_human_excerpt">\n          Sống sót kỳ diệu sau vụ đánh bom thảm khốc và mất đi thị lực, Qusay Hussein cùng 5 nhân vật phi thường chia sẻ khoảnh khắc sinh tử đã thay đổi cuộc đời họ mãi mãi.\n        </p>'
    ),
    (
        '<p class="category-featured-excerpt">\n          Nam nghệ sĩ hàng đầu xứ kim chi bày tỏ tình cảm chân thành với khán giả Việt Nam sau hai đêm bùng nổ của tour diễn kỷ niệm 20 năm tại Hà Nội.\n        </p>',
        '<p class="category-featured-excerpt" data-i18n="cat_feat_mind_excerpt">\n          Nam nghệ sĩ hàng đầu xứ kim chi bày tỏ tình cảm chân thành với khán giả Việt Nam sau hai đêm bùng nổ của tour diễn kỷ niệm 20 năm tại Hà Nội.\n        </p>'
    ),
    (
        '<p class="category-featured-excerpt">\n          Hương hoa sữa nồng nàn tháng Mười không chỉ là câu chuyện yêu hay ghét một mùi hương, mà là tấm gương phản chiếu nhịp thở của một Hà Nội không bao giờ ngừng chuyển động.\n        </p>',
        '<p class="category-featured-excerpt" data-i18n="cat_feat_indepth_excerpt">\n          Hương hoa sữa nồng nàn tháng Mười không chỉ là câu chuyện yêu hay ghét một mùi hương, mà là tấm gương phản chiếu nhịp thở của một Hà Nội không bao giờ ngừng chuyển động.\n        </p>'
    )
]

norm_text = text.replace('\r\n', '\n')
success = 0
for old, new in replacements:
    n_old = old.replace('\r\n', '\n')
    n_new = new.replace('\r\n', '\n')
    if n_old in norm_text:
        norm_text = norm_text.replace(n_old, n_new)
        success += 1
    else:
        print("Missing target:", repr(n_old[:60]))

print(f"Applied {success}/{len(replacements)} replacements!")

with open('scratch/build_multi_pages.py', 'w', encoding='utf-8') as f:
    f.write(norm_text)
print("Updated scratch/build_multi_pages.py successfully!")
