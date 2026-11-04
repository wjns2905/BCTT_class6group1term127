p = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\translations.js"
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    "trong từng trang viết.'\n      // --- Update Giao Dien 2026 Additions ---",
    "trong từng trang viết.',\n      // --- Update Giao Dien 2026 Additions ---"
)

text = text.replace(
    "every published line.'\n      // --- Update Giao Dien 2026 Additions ---",
    "every published line.',\n      // --- Update Giao Dien 2026 Additions ---"
)

with open(p, 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed commas in translations.js!")
