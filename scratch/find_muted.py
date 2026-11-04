with open("css/style.css", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines[2500:], start=2501):
    if "var(--color-text-muted)" in line or "var(--color-brand-accent)" in line:
        print(f"L{i}: {line.strip()}")
