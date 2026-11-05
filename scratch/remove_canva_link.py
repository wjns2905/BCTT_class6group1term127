import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

html_files = [
    'index.html',
    'trending.html',
    'society.html',
    'human-stories.html',
    'mind-soul.html',
    'in-depth.html',
    'about.html'
]

pattern = re.compile(r'\s*<a\s+href="https:\/\/canva\.link\/[^"]*"\s+target="_blank"\s+rel="noopener\s+noreferrer"\s+style="color:var\(--color-brand-primary\);\s*font-weight:700;"><i\s+class="fas\s+fa-palette"><\/i>\s*Canva<\/a>', re.DOTALL)

for fpath in html_files:
    if not os.path.exists(fpath):
        print(f"File not found: {fpath}")
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, count = pattern.subn('', content)
    if count > 0:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Removed Canva link from {fpath} ({count} occurrence)")
    else:
        print(f"Pattern not found in {fpath}, checking manual string match...")
        target_str = '<a href="https://canva.link/mainguyen-ngoc-mai" target="_blank" rel="noopener noreferrer" style="color:var(--color-brand-primary); font-weight:700;"><i class="fas fa-palette"></i> Canva</a>'
        if target_str in content:
            new_content = content.replace(target_str, '')
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Replaced target_str in {fpath}")
        else:
            print(f"ERROR: Could not find target in {fpath}")

print("\nDone removing Canva link from all HTML files!")
