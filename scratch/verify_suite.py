import os
import re

ROOT = r"c:\Users\camka\OneDrive\Desktop\BCTT"

pages = [
    ("index.html", "Home"),
    ("trending.html", "Trending"),
    ("society.html", "Society"),
    ("human-stories.html", "Human Stories"),
    ("mind-soul.html", "Mind & Soul"),
    ("in-depth.html", "In-depth"),
    ("about.html", "About Us")
]

print("=== 1. VERIFYING 7 STANDALONE PAGES ===")
all_exist = True
for page, label in pages:
    p = os.path.join(ROOT, page)
    if os.path.exists(p):
        size = os.path.getsize(p)
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Check active link
        active_match = re.search(r'<a href="([^"]+)" class="nav-item active">([^<]+)</a>', content)
        active_text = active_match.group(2) if active_match else "NONE"
        print(f"[OK] {page:18} ({size:6} bytes) -> Active tab: {active_text} (Expected: {label})")
    else:
        print(f"[ERROR] Missing file: {page}")
        all_exist = False

print("\n=== 2. VERIFYING ALL IMAGE PATHS IN DATA.JS ===")
with open(os.path.join(ROOT, "js", "data.js"), "r", encoding="utf-8") as f:
    data_js = f.read()

images = re.findall(r'"image":\s*"([^"]+)"', data_js)
print(f"Total articles in data.js: {len(images)}")
missing_images = []
empty_images = []
for img in images:
    full_img_path = os.path.join(ROOT, img.replace('/', os.sep))
    if not os.path.exists(full_img_path):
        missing_images.append(img)
    elif os.path.getsize(full_img_path) == 0:
        empty_images.append(img)

if not missing_images and not empty_images:
    print(f"[ALL OK] All {len(images)} images exist on disk and have non-zero size!")
else:
    print(f"[ERROR] Missing images: {missing_images}")
    print(f"[ERROR] Empty images: {empty_images}")

print("\n=== 3. CHECKING PROHIBITED KEYWORDS ===")
prohibited = ["Báo chí và Tuyên truyền", "AJC", "Học viện Báo chí", "placeholder", "unsplash", "via.placeholder"]
for page, _ in pages:
    p = os.path.join(ROOT, page)
    with open(p, "r", encoding="utf-8") as f:
        c = f.read()
    for word in prohibited:
        if word.lower() in c.lower():
            print(f"[WARNING] Found '{word}' in {page}")

print("\nVerification completed!")
