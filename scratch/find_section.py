import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for term in ['500-day-and-night', 'MOST READ', 'TOP 3', 'A new start after 60', 'hero', 'grid', 'editorial-mosaic', 'home-grid', 'magazine']:
    if term in text:
        print(f"Found '{term}' in index.html")
        # Find line number
        for i, line in enumerate(text.splitlines()):
            if term.lower() in line.lower():
                print(f"   Line {i+1}: {line.strip()[:100]}")
                break
