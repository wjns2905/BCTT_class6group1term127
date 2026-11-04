# -*- coding: utf-8 -*-
"""
Script to update js/translations.js with new bilingual keys
for header advertisement, 3-column top hero, heart-tap game, poll button, and about us tabs.
"""
import sys, re

def update_translations(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_vi_keys = """    // --- Update Giao Dien 2026 Additions ---
    ad_label: "QUẢNG CÁO • ADVERTISEMENT",
    stream_header_title: "TIN NỔI BẬT",
    widget_trending_title: "TRENDING • THỊNH HÀNH",
    widget_more_trending: "Xem thêm Trending &rarr;",
    widget_read_title: "MOST READ • ĐỌC NHIỀU NHẤT",
    widget_more_read: "Xem thêm Most Read &rarr;",
    poll_read_story_btn: "Đọc bài viết liên quan: Gánh mưu sinh phố cổ Hội An &rarr;",
    heart_game_title: "Nhịp Tim Gắn Kết · Stress Reliever",
    heart_game_sub: "Chạm vào trái tim để giải tỏa căng thẳng sau những giờ đọc tin tức. Mỗi nhịp chạm gửi gắm một thông điệp tích cực và tiếp thêm nguồn năng lượng chữa lành cho tâm hồn bạn!",
    heart_count_label: "nhịp đập yêu thương đã được chia sẻ",
    heart_charity_cheer: "Gửi năng lượng tương trợ đến quỹ học bổng trẻ em nghèo & vùng cao (BCTT Project).",
    about_opt_profiles: "Profiles",
    about_opt_photo: "Photo",
    about_opt_subscribe: "Subscribe",
    about_opt_mission: "Mission",
    about_tab_profiles: "Hồ Sơ Ban Biên Tập",
    about_tab_photo: "Kho Ảnh Phóng Sự Báo Chí",
    about_tab_subscribe: "Đăng Ký Nhận Bản Tin",
    about_tab_mission: "Tôn Chỉ Hoạt Động & Chuẩn Mực",
"""

    new_en_keys = """    // --- Update Giao Dien 2026 Additions ---
    ad_label: "ADVERTISEMENT • QUẢNG CÁO",
    stream_header_title: "CURATED STORIES",
    widget_trending_title: "TRENDING STORIES",
    widget_more_trending: "More Trending &rarr;",
    widget_read_title: "MOST READ STORIES",
    widget_more_read: "More Most Read &rarr;",
    poll_read_story_btn: "Read Related Story: Street Vendors of Hoi An &rarr;",
    heart_game_title: "Mindful Heart Beats · Stress Reliever",
    heart_game_sub: "Tap the pulsing heart to relieve stress after reading the news. Every gentle tap sends a wave of warmth and mindful positivity to your spirit!",
    heart_count_label: "loving heartbeats shared worldwide",
    heart_charity_cheer: "Sharing compassionate solidarity with underprivileged students & children in mountainous regions.",
    about_opt_profiles: "Profiles",
    about_opt_photo: "Photo Gallery",
    about_opt_subscribe: "Subscribe",
    about_opt_mission: "Mission & Ethics",
    about_tab_profiles: "Editorial Team & Advisors",
    about_tab_photo: "Documentary Photo Gallery",
    about_tab_subscribe: "Newsletter Subscription",
    about_tab_mission: "Mission, Ethics & Compliance",
"""

    # Check if already present
    if 'ad_label:' in content:
        print("Translations already contain ad_label, skipping append.")
        return

    # Insert into vi (before "en: {")
    en_pos = content.find('  en: {')
    if en_pos == -1:
        print("Could not find '  en: {' in translations file!")
        return

    # Find the closing brace of vi before en_pos
    last_vi_brace = content.rfind('}', 0, en_pos)
    content = content[:last_vi_brace] + new_vi_keys + content[last_vi_brace:]

    # Now find the closing brace of en (the last '}' before the final '};')
    last_en_brace = content.rfind('}', 0, content.rfind('};'))
    content = content[:last_en_brace] + new_en_keys + content[last_en_brace:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully updated translations in {filepath}!")

for p in [
    r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\translations.js',
    r'C:\Users\camka\OneDrive\Desktop\BCTT\js\translations.js'
]:
    try:
        update_translations(p)
    except Exception as e:
        print(f"Error updating {p}: {e}")
