import json

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
end = text.rfind('];') + 1
articles = json.loads(text[start:end])

t1 = next(a for a in articles if a['id'] == 'trending-1')
print("Image cover:", t1['image'])
print("Content snippets with img:")
for p in t1['content']:
    if '<img' in p:
        print(p)
