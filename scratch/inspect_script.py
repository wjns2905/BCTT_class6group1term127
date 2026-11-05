import sys, re

sys.stdout.reconfigure(encoding='utf-8')
with open('scratch/apply_full_100_accurate_images.py', 'r', encoding='utf-8') as f:
    text = f.read()

for vid in ['video-1', 'video-2', 'video-3', 'video-5', 'video-6', 'video-7', 'video-8', 'video-9', 'video-10', 'video-11', 'video-12']:
    m = re.search(r"'" + vid + r"':\s*\{(.*?)\}", text, re.DOTALL)
    if m:
        block = m.group(1)
        img = re.search(r"'image':\s*'(.*?)'", block)
        title = re.search(r"'title':\s*'(.*?)'", block)
        print(f"{vid}: img={img.group(1) if img else None} | title={title.group(1)[:50] if title else None}")
