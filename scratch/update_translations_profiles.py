import sys

p = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\translations.js"

with open(p, 'r', encoding='utf-8') as f:
    content = f.read()

new_vi = """    // --- Member Profiles (from [BCTT] Profiles.docx) ---
    profiles_sec_title: "BAN BIÊN TẬP & NHÂN SỰ TÒA SOẠN",
    profiles_sec_sub: "Lớp 6 - Nhóm 1 - Khóa 127 • Khoa Ngôn ngữ & Truyền thông • Trường Đại học Ngoại ngữ - ĐHQGHN",
    profile_mai_title: "Tổng Biên Tập (Editor-in-Chief)",
    profile_mai_role: "Định hướng chiến lược nội dung tổng thể của tòa soạn, đảm bảo tính chuẩn mực của đạo đức báo chí và kiểm duyệt toàn diện các ấn phẩm xuất bản trên nền tảng.",
    profile_haanh_title: "Thư Ký Tòa Soạn (Managing Editor)",
    profile_haanh_role: "Điều phối hoạt động tác nghiệp hàng ngày của tòa soạn, quản trị lịch xuất bản định kỳ và giám sát chặt chẽ quy trình sản xuất nội dung đa phương tiện.",
    profile_phuonganh_title: "Biên Tập Viên Nội Dung Cao Cấp (Senior Content Editor)",
    profile_phuonganh_role: "Chủ trì nghiên cứu chuyên đề, kiểm chứng sự thật đa nguồn và trau chuốt câu từ để đảm bảo độ trong sáng, sắc sảo cùng chiều sâu phân tích.",
    profile_ngan_title: "Biên Tập Viên Đa Phương Tiện (Multimedia Editor)",
    profile_ngan_role: "Chỉ đạo nghệ thuật báo chí thị giác, thiết kế đồ họa tương tác, infographic và tuyển chọn các tác phẩm báo ảnh phóng sự giàu cảm xúc.",
    profile_quynh_title: "Trưởng Ban Kỹ Thuật Số & Xuất Bản (Digital & Publishing Lead)",
    profile_quynh_role: "Quản trị hệ thống web báo điện tử, tối ưu hóa trải nghiệm đọc đa thiết bị (UX/SEO) và tổ chức phát hành nội dung trên các kênh số.",
    std_sec_title: "CHUẨN MỰC XUẤT BẢN & ĐẠO ĐỨC TÒA SOẠN",
    std_accuracy_title: "Chính Xác & Khách Quan (Accuracy & Objectivity)",
    std_accuracy_desc: "Mọi tác phẩm xuất bản đều trải qua quy trình kiểm chứng sự thật nghiêm ngặt và đối chiếu đa chiều với các nguồn tin báo chí uy tín.",
    std_ethics_title: "Liêm Chính & Đạo Đức Nghề Báo (Ethical Integrity)",
    std_ethics_desc: "Chúng tôi tuân thủ nghiêm ngặt đạo đức báo chí chuyên nghiệp, chủ động bài trừ giật gân, câu view và thông tin gây hiểu lầm.",
    std_ux_title: "Trải Nghiệm Độc Giả Hiện Đại (Modern Reader Experience)",
    std_ux_desc: "Ứng dụng định dạng đa phương tiện và ngôn ngữ thiết kế tối giản, tinh tế để tin tức chất lượng cao tiếp cận độc giả một cách gần gũi và hấp dẫn.",
"""

new_en = """    // --- Member Profiles (from [BCTT] Profiles.docx) ---
    profiles_sec_title: "EDITORIAL BOARD & NEWSROOM ROSTER",
    profiles_sec_sub: "Class 6 - Group 1 - Term 127 • Faculty of Linguistics & Communication • ULIS - VNU",
    profile_mai_title: "Editor-in-Chief",
    profile_mai_role: "Sets the overall editorial direction, ensures adherence to journalistic standards, and oversees all published content across the platform.",
    profile_haanh_title: "Managing Editor",
    profile_haanh_role: "Coordinates daily newsroom operations, manages the editorial calendar, and oversees the production workflow.",
    profile_phuonganh_title: "Senior Content Editor",
    profile_phuonganh_role: "Spearheads topic research, fact-checks stories, and refines written content to ensure high clarity and analytical depth.",
    profile_ngan_title: "Multimedia Editor",
    profile_ngan_role: "Leads visual storytelling by designing graphics, infographics, and curation of photojournalism assets.",
    profile_quynh_title: "Digital & Publishing Lead",
    profile_quynh_role: "Manages web development, optimizes digital reader experience (UX/SEO), and handles content distribution.",
    std_sec_title: "EDITORIAL STANDARDS & CODE OF ETHICS",
    std_accuracy_title: "Accuracy & Objectivity",
    std_accuracy_desc: "Every publication undergoes rigorous fact-checking and cross-referencing with credible sources.",
    std_ethics_title: "Ethical Integrity",
    std_ethics_desc: "We adhere strictly to professional journalism ethics, actively avoiding clickbait and misleading information.",
    std_ux_title: "Modern Reader Experience",
    std_ux_desc: "We leverage multimedia formats and clean design to make quality news accessible and engaging.",
"""

if 'profile_mai_title' not in content:
    # Insert in vi
    en_pos = content.find('  en: {')
    last_vi_brace = content.rfind('}', 0, en_pos)
    content = content[:last_vi_brace] + new_vi + content[last_vi_brace:]

    # Insert in en
    last_en_brace = content.rfind('}', 0, content.rfind('};'))
    content = content[:last_en_brace] + new_en + content[last_en_brace:]

    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Added profiles and standards translations!")
else:
    print("Profiles translations already present.")
