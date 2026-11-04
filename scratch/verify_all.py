import os
import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

ROOT = r"c:\Users\camka\OneDrive\Desktop\BCTT"

def test_dom_elements():
    print("=== TEST 1: DOM Elements in index.html ===")
    with open(os.path.join(ROOT, "index.html"), "r", encoding="utf-8") as f:
        html = f.read()

    expected_ids = [
        "readingProgressBar", "offlineBanner",
        "onboardModal", "shortcutsModal",
        "videoHubContent", "aboutUsSection", "articleReaderModal",
        "articleModalBody", "searchModal", "searchResults", "liveDateWidget",
        "drawerBackdrop", "offcanvasDrawer", "fashionArticlesGrid"
    ]

    missing = [id_name for id_name in expected_ids if f'id="{id_name}"' not in html]
    if missing:
        print(f"FAILED: Missing IDs: {missing}")
        return False
    print(f"PASSED: All {len(expected_ids)} critical DOM elements exist in index.html.")
    return True

def test_no_ajc():
    print("\n=== TEST 2: Zero AJC Mentions (Must be ULIS - VNU) ===")
    files = ["index.html", "js/app.js", "js/data.js", "css/style.css", "css/tokens.css", "PRODUCT.md", "DESIGN.md", "README.md"]
    banned_patterns = ["Báo chí và Tuyên truyền", "Báo chí & Tuyên truyền", "AJC", "Học viện BCTT"]
    violations = []

    for file_rel in files:
        file_path = os.path.join(ROOT, file_rel)
        if not os.path.exists(file_path):
            continue
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        for pat in banned_patterns:
            if pat.lower() in content.lower():
                violations.append((file_rel, pat))

    if violations:
        print(f"FAILED: Banned terms found: {violations}")
        return False
    print("PASSED: 0 references to Academy of Journalism. ULIS - VNU confirmed as sole institution.")
    return True

def test_articles_and_images():
    print("\n=== TEST 3: Articles Data and Asset Integrity ===")
    with open(os.path.join(ROOT, "js", "data.js"), "r", encoding="utf-8") as f:
        text = f.read()

    json_text = text.split("const ARTICLES_DATA = ", 1)[1].rsplit(";", 1)[0].strip()
    articles = json.loads(json_text)
    print(f"Loaded {len(articles)} articles from data.js")

    missing_images = []
    found_images = 0
    for a in articles:
        img_rel = a.get("image")
        if img_rel:
            full_path = os.path.join(ROOT, img_rel.replace("/", os.sep))
            if not os.path.exists(full_path):
                missing_images.append((a["id"], img_rel))
            else:
                found_images += 1

    if missing_images:
        print(f"FAILED: Missing images: {missing_images}")
        return False
    print(f"PASSED: All {found_images} article images verified physically on disk.")
    return True

def test_font_stacks():
    print("\n=== TEST 4: High-Fashion Typography ===")
    with open(os.path.join(ROOT, "css", "tokens.css"), "r", encoding="utf-8") as f:
        tokens = f.read()
    with open(os.path.join(ROOT, "css", "style.css"), "r", encoding="utf-8") as f:
        css = f.read()

    assert "Bodoni Moda" in tokens or "Bodoni Moda" in css, "Bodoni Moda missing"
    assert "Playfair Display" in tokens or "Playfair Display" in css, "Playfair Display missing"
    assert "Plus Jakarta Sans" in tokens or "Plus Jakarta Sans" in css, "Plus Jakarta Sans missing"
    print("PASSED: Bodoni Moda, Playfair Display, and Plus Jakarta Sans verified.")
    return True

def main():
    t1 = test_dom_elements()
    t2 = test_no_ajc()
    t3 = test_articles_and_images()
    t4 = test_font_stacks()

    if all([t1, t2, t3, t4]):
        print("\n========================================================")
        print("ALL VERIFICATION SUITES PASSED PERFECTLY FOR FASHION SUITE!")
        print("========================================================")
    else:
        print("\nSome tests failed!")

if __name__ == "__main__":
    main()
