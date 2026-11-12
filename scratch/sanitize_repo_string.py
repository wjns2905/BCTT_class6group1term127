import os

BASE_DIR = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127"

files = [
    os.path.join(BASE_DIR, 'index.html'),
    os.path.join(BASE_DIR, 'trending.html'),
    os.path.join(BASE_DIR, 'society.html'),
    os.path.join(BASE_DIR, 'human-stories.html'),
    os.path.join(BASE_DIR, 'mind-soul.html'),
    os.path.join(BASE_DIR, 'in-depth.html'),
    os.path.join(BASE_DIR, 'about.html'),
    os.path.join(BASE_DIR, 'article.html'),
    os.path.join(BASE_DIR, 'hearticles', 'madeuparticle', 'index.html'),
    os.path.join(BASE_DIR, 'js', 'app.js'),
]

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Replace hardcoded repo path with dynamic detection
    if 'BCTT_class6group1term127' in c:
        c = c.replace(
            "img.src = '/BCTT_class6group1term127/' + cur;",
            "const repo = window.location.pathname.split('/')[1]; img.src = '/' + repo + '/' + cur;"
        )
        c = c.replace(
            "img.src = '/BCTT_class6group1term127/' + cleanPath;",
            "const repo = window.location.pathname.split('/')[1]; img.src = '/' + repo + '/' + cleanPath;"
        )
        c = c.replace(
            "window.location.pathname.startsWith('/BCTT_class6group1term127')",
            "(window.location.hostname.includes('github.io'))"
        )
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Sanitized {os.path.basename(fpath)}")

print("Done sanitizing.")
