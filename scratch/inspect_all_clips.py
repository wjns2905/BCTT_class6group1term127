import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    code = f.read()

m = re.search(r'const\s+VIDEO_CLIPS\s*=\s*\[(.*?)\];', code, re.DOTALL)
if m:
    for clip_match in re.finditer(r'\{([^{}]+)\}', m.group(1)):
        block = clip_match.group(1)
        id_m = re.search(r'id:\s*"([^"]+)"', block)
        title_m = re.search(r'title:\s*"([^"]+)"', block)
        type_m = re.search(r'sourceType:\s*"([^"]+)"', block)
        watch_m = re.search(r'watchUrl:\s*"([^"]+)"', block)
        embed_m = re.search(r'embedUrl:\s*"([^"]+)"', block)
        print(f"ID: {id_m.group(1) if id_m else '?'}")
        print(f"  title: {title_m.group(1) if title_m else '?'}")
        print(f"  type: {type_m.group(1) if type_m else '?'}")
        print(f"  watchUrl: {watch_m.group(1) if watch_m else '?'}")
        print(f"  embedUrl: {embed_m.group(1) if embed_m else '?'}")
        print()

print("="*60)
# Check renderVideoHub and related functions
m2 = re.search(r'function\s+renderVideoHub\b.*?(?=function|\Z)', code, re.DOTALL)
if m2:
    print(m2.group(0)[:1500])
