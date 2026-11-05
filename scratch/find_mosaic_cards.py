import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for aid in ['human-2', 'trending-3']:
    idx = text.find(aid)
    while idx != -1:
        print(f"=== {aid} at {idx} ===")
        print(text[max(0, idx-100):min(len(text), idx+300)])
        idx = text.find(aid, idx+1)
