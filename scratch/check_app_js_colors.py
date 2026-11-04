with open("js/app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines, start=1):
    if "color:" in line and ("var(--color-text-muted)" in line or "#A" in line or "#D" in line or "#E" in line or "#C" in line or "#7" in line):
        print(f"L{i}: {line.strip()}")
