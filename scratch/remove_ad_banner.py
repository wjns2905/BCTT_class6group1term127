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

pattern = re.compile(
    r'\s*<!--\s*=+\s*1\.\s*HEADER LEADERBOARD ADVERTISEMENT.*?-->\s*<div class="header-ad-leaderboard-wrap">.*?</div>\s*</div>',
    re.DOTALL
)

for fpath in html_files:
    if not os.path.exists(fpath):
        print(f"File not found: {fpath}")
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, count = pattern.subn('\n', content)
    if count > 0:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Removed Header Advertisement from {fpath} ({count} occurrence)")
    else:
        # Fallback substring search
        start_idx = content.find('<div class="header-ad-leaderboard-wrap">')
        if start_idx != -1:
            end_div_1 = content.find('</div>', start_idx)
            end_div_2 = content.find('</div>', end_div_1 + 6)
            end_idx = end_div_2 + 6
            # Also find comment before start_idx
            comment_start = content.rfind('<!--', 0, start_idx)
            if comment_start != -1 and 'HEADER LEADERBOARD' in content[comment_start:start_idx]:
                start_idx = comment_start
            new_content = content[:start_idx] + content[end_idx:]
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Removed Header Advertisement (fallback) from {fpath}")
        else:
            print(f"Warning: header-ad-leaderboard-wrap not found in {fpath}")

print("\nFinished removing advertisement banners!")
