with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '.top-hero-3col-cluster' in l:
        print(f"Around line {i+1}:")
        for j in range(max(0, i-5), min(len(lines), i+80)):
            print(f"{j+1:4d}: {lines[j]}", end='')
        break
