import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

DATA_PATH = r"c:\Users\camka\OneDrive\Desktop\BCTT\js\data.js"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    text = f.read()

prefix = "const ARTICLES_DATA = "
suffix = ";"

json_text = text.split(prefix, 1)[1].rsplit(suffix, 1)[0].strip()
articles = json.loads(json_text)

# Remove the 5 temporary placeholder articles
placeholder_ids = {'cover-story-her', 'latest-loneliness', 'latest-small-acts', 'latest-hurry', 'feature-she-definition'}
real_articles = [a for a in articles if a['id'] not in placeholder_ids]
print(f"Remaining real articles: {len(real_articles)}")

# Update specific image paths so they all point to authentic non-empty images:
for a in real_articles:
    if a['id'] == 'trending-1':
        a['image'] = 'assets/images/trending/lawmakers_lead.jpg'
        a['imageCaption'] = 'NA deputy Doan Thi Le An from Cao Bang Province speaks at the National Assembly discussion. (Photo: NDO)'
    elif a['id'] == 'trending-4':
        a['image'] = 'assets/images/trending/image8.jpg'
        a['imageCaption'] = 'A woman carrying flowers walks in the rain at the junction of Hoang Van Thu and Tran Phu Street, Hoi An.'
    elif a['id'] == 'trending-5':
        a['image'] = 'assets/images/human_stories/image17.jpg'
        a['imageCaption'] = 'Ceremony marking the transfer of samples of martyrs’ remains collected from provinces.'
    elif a['id'] == 'human-4':
        a['image'] = 'assets/images/human_stories/image7.png'
        a['imageCaption'] = 'Work on the Gruver farmland in October 2025. (Rhett Sparks)'
    elif a['id'] == 'indepth-1':
        a['image'] = 'assets/images/human_stories/image20.jpg'
        a['imageCaption'] = 'The bittersweet scent and collective memory of milk flowers (hoa sữa) along Hanoi streets.'

# Verify all images exist and are non-empty (>1000 bytes)
for a in real_articles:
    img = a['image']
    full = os.path.join(r"c:\Users\camka\OneDrive\Desktop\BCTT", img)
    if not os.path.exists(full):
        print(f"ERROR: Image not found: {img} for {a['id']}")
    else:
        sz = os.path.getsize(full)
        if sz < 1000:
            print(f"WARNING: Image too small ({sz}b): {img} for {a['id']}")

new_js = f"""// HEARTICLES. News Portal Data
// High-Fashion Editorial Edition (Vogue, Harper's Bazaar, Kinfolk Aesthetic)
// Authentic Articles & Images directly extracted from [BCTT] course resources
// Class 6 - Group 1 - Term 127 • Trường Đại học Ngoại ngữ - ĐHQGHN (ULIS - VNU)
const ARTICLES_DATA = {json.dumps(real_articles, ensure_ascii=False, indent=2)};
"""

with open(DATA_PATH, "w", encoding="utf-8") as f:
    f.write(new_js)

print("Updated js/data.js with authentic original articles and images!")
