import os

target_dir = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127"

matches = []
for root, dirs, files in os.walk(target_dir):
    for f in files:
        if f.endswith(('.html', '.js', '.css', '.py', '.json', '.md')):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8') as file:
                    txt = file.read()
                    if "Desktop\\BCTT" in txt or "Desktop/BCTT" in txt:
                        # Exclude matches that are already Desktop\BCTT_class6group1term127
                        txt_replaced = txt.replace("BCTT_class6group1term127", "")
                        if "Desktop\\BCTT" in txt_replaced or "Desktop/BCTT" in txt_replaced:
                            matches.append(p)
            except Exception:
                pass

print(f"Files with old BCTT references: {len(matches)}")
for m in matches:
    print("  -", os.path.relpath(m, target_dir))
