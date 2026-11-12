import os
import json
import re

base = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127"

with open(os.path.join(base, 'js', 'data.js'), 'r', encoding='utf-8') as f:
    text = f.read().strip()

# find first [ and last ]
start = text.find('[')
end = text.rfind(']')
data = json.loads(text[start:end+1])

art = [a for a in data if a['id'] == 'trending-1'][0]

print('Article 1 hero image:', art['image'])
hero_path = os.path.join(base, art['image'].replace('/', os.sep))
print('Hero exists on disk:', os.path.isfile(hero_path))

imgs = re.findall(r'src=["\']([^"\']+)["\']', ''.join(art['content']))
for img in imgs:
    img_path = os.path.join(base, img.replace('/', os.sep))
    exists = os.path.isfile(img_path)
    print('Content img:', img, 'Exists:', exists)
    if exists:
        d, b = os.path.split(img_path)
        actual = os.listdir(d)
        print('  Exact casing match:', b in actual)
    else:
        print('  MISSING FILE!')
