import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\data.js', 'r', encoding='utf-8') as f:
    text = f.read()

queries = ["Áo dài", "trẻ em", "ARTE", "500 ngày đêm", "vĩ cầm", "Thái Nguyên", "bữa cơm", "Ốc đảo", "thể thao", "phi thường", "người cao tuổi"]
for q in queries:
    m = re.findall(rf'id:\s*["\']([^"\']+)["\'][^}}]*?title:\s*["\'][^"\']*{q}[^"\']*["\']', text, re.IGNORECASE)
    print(f"Query '{q}': ids={m}")
