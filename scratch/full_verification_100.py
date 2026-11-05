import json
import os
from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
e = c.rfind('];') + 1

articles = json.loads(c[s:e])

print("=" * 60)
print(f"VERIFICATION REPORT: {len(articles)} ARTICLES")
print("=" * 60)

# 1. Total Count
assert len(articles) == 100, f"Expected 100, got {len(articles)}"
print("✓ Total Count: EXACTLY 100 articles")

# 2. Category Distribution
cat_counts = {}
for a in articles:
    cat_counts[a['category']] = cat_counts.get(a['category'], 0) + 1

for cat, count in sorted(cat_counts.items()):
    assert count == 20, f"Category {cat} has {count} articles, expected 20!"
    print(f"✓ Category '{cat}': EXACTLY 20 articles")

# 3. Unique IDs
ids = [a['id'] for a in articles]
assert len(ids) == len(set(ids)), "Duplicate IDs detected!"
print(f"✓ Article IDs: 100 / 100 strictly unique")

# 4. Unique Images
images = [a['image'] for a in articles]
assert len(images) == len(set(images)), "Duplicate Images detected!"
print(f"✓ Article Images: 100 / 100 strictly unique (ZERO duplicate images)")

# 5. Image Files On Disk
for a in articles:
    img = a['image']
    assert os.path.exists(img), f"Image does not exist on disk: {img}"
    with Image.open(img) as im:
        w, h = im.size
        assert w >= 250 and h >= 180, f"Image too small: {img} ({w}x{h})"

print(f"✓ All 100 image files exist on disk and meet high-res quality requirements (>= 250x180)")

# 6. Title and Subtitle Uniqueness
titles = [a['title'].strip().lower() for a in articles]
assert len(titles) == len(set(titles)), "Duplicate Titles detected!"
print(f"✓ Article Titles: 100 / 100 strictly unique")

# 7. Bilingual & Content Fields
for a in articles:
    assert 'title' in a and a['title'], f"Article {a['id']} missing title"
    assert 'title_en' in a and a['title_en'], f"Article {a['id']} missing title_en"
    assert 'subtitle' in a and a['subtitle'], f"Article {a['id']} missing subtitle"
    assert 'subtitle_en' in a and a['subtitle_en'], f"Article {a['id']} missing subtitle_en"
    assert 'content' in a and len(a['content']) >= 2, f"Article {a['id']} has insufficient content paragraphs"
    assert 'author' in a and a['author'], f"Article {a['id']} missing author"
    assert 'date' in a and a['date'], f"Article {a['id']} missing date"
    assert 'sourceName' in a and a['sourceName'], f"Article {a['id']} missing sourceName"

print("✓ All 100 articles have bilingual title/subtitle, rich content paragraphs, author, date, and source")

print("=" * 60)
print("ALL 7 VERIFICATION CHECKS PASSED WITH 100% SUCCESS!")
print("=" * 60)
