import json
import os
from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read existing data.js
with open('js/data.js', 'r', encoding='utf-8') as f:
    orig_code = f.read()

s = orig_code.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
e = orig_code.rfind('];') + 1

articles_85 = json.loads(orig_code[s:e])
print(f"Loaded {len(articles_85)} existing articles.")

# Import new 15
import importlib.util
spec = importlib.util.spec_from_file_location("gen", "scratch/generate_100_articles.py")
gen_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen_mod)
new_15 = gen_mod.new_15
print(f"Loaded {len(new_15)} new articles.")

# Combine into 100 articles
all_articles = articles_85 + new_15
print(f"Total articles combined: {len(all_articles)}")

# Refine trending-17 to eliminate renewable energy overlap with society-2
for a in all_articles:
    if a['id'] == 'trending-17':
        a['title'] = "Đổi mới sáng tạo trong nông nghiệp tuần hoàn: Biến phụ phẩm lúa gạo và cà phê thành bao bì sinh học tự phân hủy"
        a['title_en'] = "Circular Agriculture: Upcycling Rice Husks and Coffee Byproducts into Biodegradable Packaging"
        a['subtitle'] = "Pioneering biotech startups in the Mekong Delta and Central Highlands are replacing single-use styrofoam with compostable plant-fiber materials."
        a['subtitle_en'] = "Pioneering biotech startups in the Mekong Delta and Central Highlands are replacing single-use styrofoam with compostable plant-fiber materials."
        a['tags'] = ["Circular Economy", "Biotech", "Sustainability", "Innovation"]
        a['content'] = [
            "In an agricultural powerhouse generating tens of millions of tons of rice husks, bagasse, and coffee pulp annually, Vietnamese green entrepreneurs are transforming organic waste into high-value packaging.",
            "Using thermo-compression and fungal mycelium binding, local facilities produce takeaway boxes and shock-absorbent logistics padding that decompose naturally in soil within 90 days.",
            "“Waste is simply a raw material whose value has not yet been unlocked,” says 28-year-old circular design pioneer Nguyen Thi Thao."
        ]
    elif a['id'] == 'indepth-14':
        a['title'] = "Địa kinh tế chuỗi cung ứng cảng biển nước sâu và logistics đường thủy nội địa"
        a['title_en'] = "Geoeconomics of Deep-Water Seaports and Inland Waterway Maritime Logistics Corridors"
        a['subtitle'] = "An exhaustive regional study analyzing how Cai Mep-Thi Vai and Lach Huyen deep-sea hubs are integrating with river barge networks to slash export logistics costs."
        a['subtitle_en'] = "An exhaustive regional study analyzing how Cai Mep-Thi Vai and Lach Huyen deep-sea hubs are integrating with river barge networks to slash export logistics costs."
        a['tags'] = ["Maritime Logistics", "Deep-Sea Ports", "Supply Chain", "Geoeconomics"]
        a['content'] = [
            "With Vietnam sitting astride one of the busiest maritime trade arteries in the world, the strategic expansion of deep-water container terminals has altered Southeast Asian logistics architecture.",
            "Direct maritime routes connecting Cai Mep-Thi Vai to the US West Coast and Northern Europe have eliminated costly transshipment stopovers in regional hubs, cutting transit times by over a week.",
            "Economists underscore that synchronizing deep-water port operations with low-emission inland river barge feeder routes is essential to maintaining national export competitiveness."
        ]

# Group by category
by_cat = {
    'trending': [],
    'society': [],
    'human-stories': [],
    'mind-soul': [],
    'in-depth': []
}

for a in all_articles:
    by_cat[a['category']].append(a)

for c, arts in by_cat.items():
    print(f"Category '{c}': {len(arts)} articles")
    assert len(arts) == 20, f"Category {c} has {len(arts)} articles, expected 20!"

# Valid image helper
def get_valid_images(folder):
    res = []
    for f in sorted(os.listdir(folder)):
        p = f"{folder}/{f}".replace('\\', '/')
        if p.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            try:
                with Image.open(p) as im:
                    w, h = im.size
                    if w >= 250 and h >= 180 and 'logo' not in p.lower() and 'ads' not in p.lower() and 'profiles' not in p.lower():
                        res.append(p)
            except:
                pass
    return res

trending_pool = get_valid_images('assets/images/trending')
society_pool = get_valid_images('assets/images/society')
human_pool = get_valid_images('assets/images/human_stories')
mind_pool = get_valid_images('assets/images/mind_&_soul')
indepth_pool = get_valid_images('assets/images/in-dept')
editorial_pool = get_valid_images('assets/images/editorial')
notes_pool = get_valid_images('assets/images/note_giao_diện')

print(f"Pool sizes: Trending={len(trending_pool)}, Society={len(society_pool)}, Human={len(human_pool)}, Mind={len(mind_pool)}, Indepth={len(indepth_pool)}, Editorial={len(editorial_pool)}, Notes={len(notes_pool)}")

# Prepare 20 distinct images for TRENDING:
# Preserving authentic images:
# trending-1 -> assets/images/trending/lawmakers_lead.jpg
# trending-2 -> assets/images/trending/image2.jpg
# trending-3 -> assets/images/trending/image3.jpg
# trending-4 -> assets/images/trending/image8.jpg
# trending-5 -> assets/images/trending/image1.jpg
# trending-6 -> assets/images/trending/image15.jpg
# trending-11 -> assets/images/society/image24.jpg (Hoi An photo)
# Now we need 13 more unique images from trending_pool:
trending_fixed = {
    'trending-1': 'assets/images/trending/lawmakers_lead.jpg',
    'trending-2': 'assets/images/trending/image2.jpg',
    'trending-3': 'assets/images/trending/image3.jpg',
    'trending-4': 'assets/images/trending/image8.jpg',
    'trending-5': 'assets/images/trending/image1.jpg',
    'trending-6': 'assets/images/trending/image15.jpg',
    'trending-11': 'assets/images/society/image24.jpg',
}

# Collect used images so far
assigned_images = set(trending_fixed.values())

# Fill remaining trending articles from trending_pool
for a in by_cat['trending']:
    if a['id'] in trending_fixed:
        a['image'] = trending_fixed[a['id']]
    else:
        # find unused in trending_pool
        chosen = None
        for img in trending_pool:
            if img not in assigned_images:
                chosen = img
                break
        assert chosen is not None, "Out of trending images!"
        a['image'] = chosen
        assigned_images.add(chosen)

# Prepare 20 distinct images for SOCIETY:
# Authentic images:
# society-1 -> assets/images/society/image3.jpg
# society-6 -> assets/images/society/image10.jpg
# society-7 -> assets/images/society/image11.jpg
# society-8 -> assets/images/society/image23.jpg
# video-1 -> assets/images/society/image13.png
# video-2 -> assets/images/society/image14.png
# video-3 -> assets/images/society/image2.jpg
# video-7 -> assets/images/society/image34.jpg
# video-10 -> assets/images/society/image30.jpg
# video-12 -> assets/images/society/image18.png
society_fixed = {
    'society-1': 'assets/images/society/image3.jpg',
    'society-6': 'assets/images/society/image10.jpg',
    'society-7': 'assets/images/society/image11.jpg',
    'society-8': 'assets/images/society/image23.jpg',
    'video-1': 'assets/images/society/image13.png',
    'video-2': 'assets/images/society/image14.png',
    'video-3': 'assets/images/society/image2.jpg',
    'video-7': 'assets/images/society/image34.jpg',
    'video-10': 'assets/images/society/image30.jpg',
    'video-12': 'assets/images/society/image18.png',
}
for img in society_fixed.values():
    assert img not in assigned_images, f"Conflict with {img}!"
    assigned_images.add(img)

for a in by_cat['society']:
    if a['id'] in society_fixed:
        a['image'] = society_fixed[a['id']]
    else:
        chosen = None
        for img in society_pool:
            if img not in assigned_images:
                chosen = img
                break
        assert chosen is not None, "Out of society images!"
        a['image'] = chosen
        assigned_images.add(chosen)

# Prepare 20 distinct images for HUMAN STORIES:
# Authentic images:
# human-1 -> assets/images/human_stories/image1.jpg
# human-2 -> assets/images/human_stories/image11.jpg
# human-3 -> assets/images/human_stories/image3.png
# human-4 -> assets/images/human_stories/image7.png
# human-9 -> assets/images/human_stories/image22.jpg
# human-10 -> assets/images/human_stories/image23.jpg
# video-8 -> assets/images/human_stories/image15.jpg
# video-11 -> assets/images/human_stories/image20.jpg
human_fixed = {
    'human-1': 'assets/images/human_stories/image1.jpg',
    'human-2': 'assets/images/human_stories/image11.jpg',
    'human-3': 'assets/images/human_stories/image3.png',
    'human-4': 'assets/images/human_stories/image7.png',
    'human-9': 'assets/images/human_stories/image22.jpg',
    'human-10': 'assets/images/human_stories/image23.jpg',
    'video-8': 'assets/images/human_stories/image15.jpg',
    'video-11': 'assets/images/human_stories/image20.jpg',
}
for img in human_fixed.values():
    assert img not in assigned_images, f"Conflict with {img}!"
    assigned_images.add(img)

for a in by_cat['human-stories']:
    if a['id'] in human_fixed:
        a['image'] = human_fixed[a['id']]
    else:
        chosen = None
        for img in human_pool:
            if img not in assigned_images:
                chosen = img
                break
        assert chosen is not None, "Out of human stories images!"
        a['image'] = chosen
        assigned_images.add(chosen)

# Prepare 20 distinct images for MIND & SOUL:
# Authentic images:
# mind-1 -> assets/images/mind_&_soul/image2.jpg
# mind-2 -> assets/images/mind_&_soul/image5.jpg
# mind-3 -> assets/images/mind_&_soul/image9.jpg
# mind-7 -> assets/images/mind_&_soul/image13.jpg
# mind-8 -> assets/images/mind_&_soul/image14.jpg
# mind-9 -> assets/images/mind_&_soul/image20.png
# video-5 -> assets/images/mind_&_soul/image6.jpg
# video-6 -> assets/images/mind_&_soul/image7.jpg
# video-9 -> assets/images/mind_&_soul/image18.png
mind_fixed = {
    'mind-1': 'assets/images/mind_&_soul/image2.jpg',
    'mind-2': 'assets/images/mind_&_soul/image5.jpg',
    'mind-3': 'assets/images/mind_&_soul/image9.jpg',
    'mind-7': 'assets/images/mind_&_soul/image13.jpg',
    'mind-8': 'assets/images/mind_&_soul/image14.jpg',
    'mind-9': 'assets/images/mind_&_soul/image20.png',
    'video-5': 'assets/images/mind_&_soul/image6.jpg',
    'video-6': 'assets/images/mind_&_soul/image7.jpg',
    'video-9': 'assets/images/mind_&_soul/image18.png',
}
for img in mind_fixed.values():
    assert img not in assigned_images, f"Conflict with {img}!"
    assigned_images.add(img)

mind_combined_pool = mind_pool + notes_pool
for a in by_cat['mind-soul']:
    if a['id'] in mind_fixed:
        a['image'] = mind_fixed[a['id']]
    else:
        chosen = None
        for img in mind_combined_pool:
            if img not in assigned_images:
                chosen = img
                break
        assert chosen is not None, "Out of mind & soul images!"
        a['image'] = chosen
        assigned_images.add(chosen)

# Prepare 20 distinct images for IN-DEPTH:
# Authentic images:
# indepth-1 -> assets/images/in-dept/image2.jpg
# indepth-2 -> assets/images/in-dept/image1.jpg
# indepth-6 -> assets/images/in-dept/image4.jpg
# indepth-7 -> assets/images/in-dept/image5.jpg
# indepth-8 -> assets/images/in-dept/image6.jpg
# indepth-9 -> assets/images/society/image31.jpg (Tycoon villa)
indepth_fixed = {
    'indepth-1': 'assets/images/in-dept/image2.jpg',
    'indepth-2': 'assets/images/in-dept/image1.jpg',
    'indepth-6': 'assets/images/in-dept/image4.jpg',
    'indepth-7': 'assets/images/in-dept/image5.jpg',
    'indepth-8': 'assets/images/in-dept/image6.jpg',
    'indepth-9': 'assets/images/society/image31.jpg',
}
for img in indepth_fixed.values():
    assert img not in assigned_images, f"Conflict with {img}!"
    assigned_images.add(img)

indepth_combined_pool = indepth_pool + editorial_pool
for a in by_cat['in-depth']:
    if a['id'] in indepth_fixed:
        a['image'] = indepth_fixed[a['id']]
    else:
        chosen = None
        for img in indepth_combined_pool:
            if img not in assigned_images:
                chosen = img
                break
        assert chosen is not None, "Out of in-depth images!"
        a['image'] = chosen
        assigned_images.add(chosen)

# Final validation of all 100 articles:
print("\n" + "="*50)
print("FINAL AUDIT:")
print(f"Total articles: {len(all_articles)}")
all_ids = [a['id'] for a in all_articles]
all_images = [a['image'] for a in all_articles]

print(f"Unique IDs: {len(set(all_ids))} / 100")
print(f"Unique Images: {len(set(all_images))} / 100")

assert len(all_ids) == 100, "Must be exactly 100 IDs"
assert len(set(all_ids)) == 100, "IDs must be strictly unique"
assert len(all_images) == 100, "Must be exactly 100 Images"
assert len(set(all_images)) == 100, "IMAGES MUST BE STRICTLY UNIQUE - ZERO DUPLICATES!"

# Check that 100% of images exist on disk and have w>=250, h>=180
for img in all_images:
    assert os.path.exists(img), f"Image does not exist: {img}"
    with Image.open(img) as im:
        w, h = im.size
        assert w >= 250 and h >= 180, f"Image {img} too small: {w}x{h}"

print("SUCCESS: 100% OF ALL 100 ARTICLES HAVE DISTINCT, VALID, HIGH-RES IMAGES!")

# Write to js/data.js
formatted_json = json.dumps(all_articles, ensure_ascii=False, indent=2)
new_data_code = orig_code[:s] + formatted_json + orig_code[e:]

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(new_data_code)

print("Saved js/data.js!")

# Update VIDEO_CLIPS thumbnails in js/app.js to match each video article's image!
with open('js/app.js', 'r', encoding='utf-8') as f:
    app_code = f.read()

# Build map of articleId -> image
art_img_map = {a['id']: a['image'] for a in all_articles}

# Find VIDEO_CLIPS in app.js
video_clips_start = app_code.find('const VIDEO_CLIPS = [')
video_clips_end = app_code.find('];', video_clips_start) + 2

clips_json_str = app_code[video_clips_start + len('const VIDEO_CLIPS = '):video_clips_end - 1].strip()
# Use python regex or evaluation
import re
# For each clip in VIDEO_CLIPS, ensure thumb matches art_img_map[articleId]
for a in all_articles:
    if a['id'].startswith('video-') or a['id'] == 'trending-5':
        img = a['image']
        # replace thumb: "..." before articleId: "a['id']"
        pattern = r'(thumb:\s*["\'])([^"\']+)(["\'],\s*articleId:\s*["\']' + re.escape(a['id']) + r'["\'])'
        app_code = re.sub(pattern, r'\g<1>' + img + r'\g<3>', app_code)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(app_code)

print("Updated VIDEO_CLIPS thumbnails in js/app.js!")
