import json

with open('js/data.js', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
e = c.rfind('];') + 1
articles = json.loads(c[s:e])

# Map to update
updates = {
    'trending-8': 'assets/images/trending/image18.png',
    'mind-12': 'assets/images/mind_&_soul/image22.png',
    'society-9': 'assets/images/society/image27.jpg',
    'society-5': 'assets/images/society/image29.jpg',
    'video-7': 'assets/images/society/image34.jpg',
    'video-10': 'assets/images/society/image30.jpg'
}

for a in articles:
    if a['id'] in updates:
        a['image'] = updates[a['id']]

formatted = json.dumps(articles, ensure_ascii=False, indent=2)
new_code = c[:s] + formatted + c[e:]

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(new_code)

print("Updated image assignments for distinct visuals!")
