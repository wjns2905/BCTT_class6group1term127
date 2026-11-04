with open("css/style.css", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines[2500:], start=2501):
    if "color:" in line and "var(--color-" not in line:
        print(f"L{i}: {line.strip()}")
