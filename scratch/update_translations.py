import sys
sys.stdout.reconfigure(encoding='utf-8')

trans_path = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\translations.js'
with open(trans_path, 'r', encoding='utf-8') as f:
    text = f.read()

old_vi = '''    footer_desc: "Tòa soạn Tạp chí Báo điện tử Đa phương tiện • Trường Đại học Ngoại ngữ - Đại học Quốc gia Hà Nội (ULIS - VNU)",
    footer_group: "Lớp 6 - Nhóm 1 - Khóa 127 • Khoa Ngôn ngữ & Truyền thông • Tòa soạn Báo chí & Truyền thông Đa phương tiện",
    footer_copy: "&copy; 2026 HEARTICLES. Mọi quyền được bảo lưu. Xuất bản bởi Nhóm 1 Lớp 6 Khóa 127, ULIS - VNU.",'''

new_vi = '''    footer_desc: "Một tòa soạn báo chí độc lập có trụ sở tại Hà Nội, Việt Nam.",
    footer_group: "",
    footer_copy: "&copy; 2026 HEARTICLES. Mọi quyền được bảo lưu. Tòa soạn báo chí độc lập tại Hà Nội, Việt Nam.",'''

old_en = '''    footer_desc: "Multimedia Journalism & Editorial Portal • University of Languages and International Studies - VNU",
    footer_group: "Class 6 - Group 1 - Term 127 • Faculty of Linguistics & Communications • Multimedia Journalism & Publishing",
    footer_copy: "&copy; 2026 HEARTICLES. All rights reserved. Published by Group 1 Class 6 Term 127, ULIS - VNU.",'''

new_en = '''    footer_desc: "An independent news outlet based in Hanoi, Vietnam.",
    footer_group: "",
    footer_copy: "&copy; 2026 HEARTICLES. All rights reserved. • An independent news outlet based in Hanoi, Vietnam.",'''

if old_vi in text and old_en in text:
    text = text.replace(old_vi, new_vi).replace(old_en, new_en)
    with open(trans_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated translations.js successfully!")
else:
    print("Targets not found!")
