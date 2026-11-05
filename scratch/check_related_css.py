with open('css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all occurrences of center-post-related or related-item-row or related-text-link
for term in ['center-post-related', 'related-item-row', 'related-text-link', 'hero-center-top-post']:
    print(f"=== Term: {term} ===")
    pos = 0
    while True:
        pos = text.find(term, pos)
        if pos == -1:
            break
        print(text[max(0, pos-40):min(len(text), pos+160)].replace('\n', ' '))
        print("-" * 40)
        pos += len(term) + 1
