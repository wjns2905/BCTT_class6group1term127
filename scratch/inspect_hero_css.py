with open('css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

classes = [
    'top-hero-3col-cluster',
    'hero-left-stream',
    'hero-center-top-post',
    'center-post-media-wrap',
    'center-post-img',
    'center-post-body',
    'center-post-title',
    'center-post-related'
]

for c in classes:
    pos = 0
    while True:
        pos = text.find('.' + c, pos)
        if pos == -1:
            break
        snippet = text[max(0, pos-20):min(len(text), pos+200)]
        print(f"=== Class .{c} ===")
        print(snippet.replace('\n', ' '))
        print()
        pos += len(c) + 1
