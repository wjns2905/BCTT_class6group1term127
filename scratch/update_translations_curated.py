import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('js/translations.js', 'r', encoding='utf-8') as f:
    text = f.read()

# In vi:
text = text.replace(
    'stream_header_title: "TIN NỔI BẬT",',
    'stream_header_title: "TIN NỔI BẬT",\n    stream_curated_badge: "7 BÀI CHỌN LỌC",'
)

# In en:
text = text.replace(
    'stream_header_title: "CURATED STORIES",',
    'stream_header_title: "CURATED STORIES",\n    stream_curated_badge: "7 CURATED STORIES",'
)

with open('js/translations.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated translations.js with stream_curated_badge!")
