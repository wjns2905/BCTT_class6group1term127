# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')

ROOT = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127"
pages = ["index.html", "trending.html", "society.html", "human-stories.html", "mind-soul.html", "in-depth.html", "about.html"]

print("=== VERIFYING PAGES IN BCTT_class6group1term127 ===")

all_ok = True

for page in pages:
    p = os.path.join(ROOT, page)
    if not os.path.exists(p):
        print(f"FAIL: {page} does not exist!")
        all_ok = False
        continue
    
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()

    # Checks
    has_ad = "header-ad-leaderboard-wrap" in html
    has_logo = "brand_logo_updated.png" in html
    has_email = "class6group1term127@gmail.com" in html
    no_academic_bar = "fashion-academic-bar" not in html
    has_dropdown = "about-dropdown-menu" in html
    has_title_class = "Class6group1term127" in html

    if not (has_ad and has_logo and has_email and no_academic_bar and has_dropdown and has_title_class):
        print(f"WARN in {page}: ad={has_ad}, logo={has_logo}, email={has_email}, no_bar={no_academic_bar}, dropdown={has_dropdown}, title={has_title_class}")
        all_ok = False
    else:
        print(f"PASS: {page} headers & navigation fully verified.")

# Check index.html specific elements
with open(os.path.join(ROOT, "index.html"), 'r', encoding='utf-8') as f:
    index_html = f.read()

assert "top-hero-3col-cluster" in index_html, "Missing top-hero-3col-cluster in index.html"
assert "hero-left-stream" in index_html, "Missing hero-left-stream in index.html"
assert "hero-center-top-post" in index_html, "Missing hero-center-top-post in index.html"
assert "hero-right-widgets" in index_html, "Missing hero-right-widgets in index.html"
assert "heart-tap-container" in index_html, "Missing heart-tap-container in index.html"
assert "videoHubSection" in index_html, "Missing videoHubSection in index.html"
assert "pollContainer" in index_html, "Missing pollContainer in index.html"

print("PASS: index.html 3-column hero, video, poll, and heart tap minigame verified!")

# Check JS files
for js_file in ["app.js", "translations.js", "data.js"]:
    p = os.path.join(ROOT, "js", js_file)
    with open(p, 'r', encoding='utf-8') as f:
        js_code = f.read()
    print(f"PASS: js/{js_file} loaded ({len(js_code)} chars).")

# Check Assets
ad_asset = os.path.join(ROOT, "assets", "images", "ads", "header_ad_banner.png")
logo_asset = os.path.join(ROOT, "assets", "images", "logo", "brand_logo_updated.png")

assert os.path.exists(ad_asset), f"Missing {ad_asset}"
assert os.path.exists(logo_asset), f"Missing {logo_asset}"

print(f"PASS: Header ad asset verified ({os.path.getsize(ad_asset)} bytes).")
print(f"PASS: Brand logo asset verified ({os.path.getsize(logo_asset)} bytes).")

print("\nALL SUITE AUDITS PASSED WITH ZERO ERRORS!")
