# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/translations.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Target for vi
vi_target = """    // 12. Category Pages
    trending_desc: "Nhịp đập xu hướng, những câu chuyện thịnh hành và chuyển động văn hóa xã hội nóng hổi trích xuất từ tài nguyên chính thống [BCTT] Trending.",
    society_desc: "Những vấn đề dân sinh, chính sách tài chính du học, khủng hoảng sinh hoạt phí và các mô hình tương trợ cộng đồng văn minh trích xuất từ [BCTT] Society.",
    human_desc: "Những mảnh đời chạm đến trái tim, nghị lực phi thường và cử chỉ tử tế thắp sáng niềm tin cuộc sống trích xuất từ [BCTT] Human stories.",
    mind_desc: "Nuôi dưỡng thế giới nội tâm, nghệ thuật sống chậm, sức khỏe toàn diện và vẻ đẹp văn hóa nghệ thuật trích xuất từ [BCTT] Mind & Soul.",
    indepth_desc: "Phóng sự dài kỳ, ký sự đa phương tiện, chuyên khảo văn hóa và những góc nhìn học thuật đối ngoại sâu sắc trích xuất từ [BCTT] In-dept.",
    sidebar_top_read: '<i class="fas fa-chart-line"></i> ĐỌC NHIỀU NHẤT',
    sidebar_topics: '<i class="fas fa-tags"></i> CHỦ ĐỀ NỔI BẬT',
    btn_read_full: "Đọc bài viết đầy đủ &rarr;","""

vi_replacement = """    // 12. Category Pages
    trending_desc: "Nhịp đập xu hướng, những câu chuyện thịnh hành và chuyển động văn hóa xã hội nóng hổi trích xuất từ tài nguyên chính thống [BCTT] Trending.",
    society_desc: "Những vấn đề dân sinh, chính sách tài chính du học, khủng hoảng sinh hoạt phí và các mô hình tương trợ cộng đồng văn minh trích xuất từ [BCTT] Society.",
    human_desc: "Những mảnh đời chạm đến trái tim, nghị lực phi thường và cử chỉ tử tế thắp sáng niềm tin cuộc sống trích xuất từ [BCTT] Human stories.",
    mind_desc: "Nuôi dưỡng thế giới nội tâm, nghệ thuật sống chậm, sức khỏe toàn diện và vẻ đẹp văn hóa nghệ thuật trích xuất từ [BCTT] Mind & Soul.",
    indepth_desc: "Phóng sự dài kỳ, ký sự đa phương tiện, chuyên khảo văn hóa và những góc nhìn học thuật đối ngoại sâu sắc trích xuất từ [BCTT] In-dept.",
    sidebar_top_read: '<i class="fas fa-chart-line"></i> ĐỌC NHIỀU NHẤT',
    sidebar_topics: '<i class="fas fa-tags"></i> CHỦ ĐỀ NỔI BẬT',
    btn_read_full: "Đọc bài viết đầy đủ &rarr;",
    cat_feat_trending_kicker: "TIÊU ĐIỂM CHUYÊN MỤC · BÀI 4 TRENDING",
    cat_feat_trending_title: "Gánh mưu sinh: Hồn cốt bình dị trên từng góc phố cổ Hội An",
    cat_feat_trending_excerpt: "Hình ảnh đôi quang gánh trĩu nặng nhịp sống mưu sinh, vẻ đẹp cần lao mộc mạc và ký ức rêu phong trên từng ngõ nhỏ di sản được khắc họa xúc động qua lăng kính phóng sự VnExpress.",
    cat_feat_society_kicker: "TIÊU ĐIỂM DÂN SINH · THE GUARDIAN",
    cat_feat_society_title: "Cost of Living Crisis: Sáng kiến cộng đồng bảo toàn phẩm giá người nhận",
    cat_feat_society_excerpt: "Mô hình siêu thị cộng đồng The Vale Pantry tại Dorset (Anh) không chỉ cung cấp thực phẩm giá rẻ mà trao quyền tự chủ và phẩm giá cho các gia đình khó khăn giữa khủng hoảng chi phí sinh hoạt.",
    cat_feat_human_kicker: "CÂU CHUYỆN NGHỊ LỰC · BÀI 3 HUMAN STORIES",
    cat_feat_human_title: "“Tôi được trao cơ hội thứ hai để sống”",
    cat_feat_human_excerpt: "Hành trình tái sinh kỳ diệu của người đàn ông vượt qua ranh giới sinh tử, tìm lại mục đích sống từ lòng trắc ẩn và sự tận hiến của cộng đồng.",
    cat_feat_mind_kicker: "ÂM NHẠC & VĂN HÓA · BÁO LAO ĐỘNG",
    cat_feat_mind_title: "Sau concert Mỹ Đình, Taeyang (BigBang) liên tục nhắc đến phở và 'show tuyệt nhất'",
    cat_feat_mind_excerpt: "Giọng ca chính của BigBang bày tỏ niềm xúc động sâu sắc trước sự cuồng nhiệt của hàng chục nghìn khán giả Việt Nam, khẳng định Hà Nội là một trong những đêm diễn thăng hoa nhất trong sự nghiệp.",
    cat_feat_indepth_kicker: "KÝ SỰ VĂN HÓA · VIETNAM NEWS",
    cat_feat_indepth_title: "A Hà Nội that never stands still: Nốt hương hoa sữa và ký ức mùa thu",
    cat_feat_indepth_excerpt: "Giữa nhịp sống hiện đại hối hả, hương hoa sữa nồng nàn trên từng con phố vẫn lưu giữ hồn cốt trầm mặc, thanh lịch của Hà Nội nghìn năm văn hiến.","""

# Target for en
en_target = """    // 12. Category Pages
    trending_desc: "Trending beats, viral stories, and contemporary cultural movements curated directly from authentic [BCTT] Trending articles.",
    society_desc: "Civic realities, international student financial requirements, cost of living crises, and community mutual-aid models from [BCTT] Society.",
    human_desc: "Deeply moving human stories, extraordinary resilience, and gentle acts of kindness restoring faith in humanity from [BCTT] Human stories.",
    mind_desc: "Nourishing inner peace, the art of mindful living, holistic wellness, and cultural beauty from authentic [BCTT] Mind & Soul resources.",
    indepth_desc: "Long-form journalism, multimedia chronicles, cultural monographs, and profound academic diplomacy perspectives from [BCTT] In-dept.",
    sidebar_top_read: '<i class="fas fa-chart-line"></i> MOST READ',
    sidebar_topics: '<i class="fas fa-tags"></i> POPULAR TOPICS',
    btn_read_full: "Read Full Article &rarr;","""

en_replacement = """    // 12. Category Pages
    trending_desc: "Trending beats, viral stories, and contemporary cultural movements curated directly from authentic [BCTT] Trending articles.",
    society_desc: "Civic realities, international student financial requirements, cost of living crises, and community mutual-aid models from [BCTT] Society.",
    human_desc: "Deeply moving human stories, extraordinary resilience, and gentle acts of kindness restoring faith in humanity from [BCTT] Human stories.",
    mind_desc: "Nourishing inner peace, the art of mindful living, holistic wellness, and cultural beauty from authentic [BCTT] Mind & Soul resources.",
    indepth_desc: "Long-form journalism, multimedia chronicles, cultural monographs, and profound academic diplomacy perspectives from [BCTT] In-dept.",
    sidebar_top_read: '<i class="fas fa-chart-line"></i> MOST READ',
    sidebar_topics: '<i class="fas fa-tags"></i> POPULAR TOPICS',
    btn_read_full: "Read Full Article &rarr;",
    cat_feat_trending_kicker: "CATEGORY SPOTLIGHT · ARTICLE 4 TRENDING",
    cat_feat_trending_title: "Street Vendors: The Gentle Soul Across Hoi An Ancient Alleys",
    cat_feat_trending_excerpt: "The heavy carrying poles bearing daily livelihoods, rustic labor beauty, and mossy heritage memories across ancient alleys portrayed through VnExpress journalism.",
    cat_feat_society_kicker: "COMMUNITY SPOTLIGHT · THE GUARDIAN",
    cat_feat_society_title: "Cost of Living Crisis: Community Pantries Preserving Dignity",
    cat_feat_society_excerpt: "The Vale Pantry in Dorset provides affordable groceries while empowering families to choose with autonomy and dignity amid Britain\\'s cost-of-living hardships.",
    cat_feat_human_kicker: "INSPIRATIONAL STORY · ARTICLE 3 HUMAN STORIES",
    cat_feat_human_title: "\\\"I was given a second chance at life\\\"",
    cat_feat_human_excerpt: "The miraculous rebirth of a man who survived near-death adversity and rediscovered purpose through community compassion and devotion.",
    cat_feat_mind_kicker: "MUSIC & CULTURE · LAO DONG NEWSPAPER",
    cat_feat_mind_title: "Taeyang (BigBang) expresses deep love for pho and 'best show' at My Dinh Stadium",
    cat_feat_mind_excerpt: "BigBang lead vocalist shares heartfelt gratitude toward tens of thousands of Vietnamese fans, naming Hanoi one of the most unforgettable stages of his career.",
    cat_feat_indepth_kicker: "CULTURAL DISPATCH · VIETNAM NEWS",
    cat_feat_indepth_title: "A Hanoi that never stands still: Milk flower scent and autumn memories",
    cat_feat_indepth_excerpt: "Amid the bustling rhythm of a modern capital, the poignant scent of milk flowers along classic avenues preserves the timeless elegance and soul of thousand-year Hanoi.","""

norm_text = text.replace('\\r\\n', '\\n')
norm_vi_target = vi_target.replace('\\r\\n', '\\n')
norm_en_target = en_target.replace('\\r\\n', '\\n')

if norm_vi_target in norm_text:
    norm_text = norm_text.replace(norm_vi_target, vi_replacement)
    print("SUCCESS: vi target replaced")
else:
    print("FAIL: vi target not found")

if norm_en_target in norm_text:
    norm_text = norm_text.replace(norm_en_target, en_replacement)
    print("SUCCESS: en target replaced")
else:
    print("FAIL: en target not found")

with open('js/translations.js', 'w', encoding='utf-8') as f:
    f.write(norm_text)
print("js/translations.js updated successfully!")
