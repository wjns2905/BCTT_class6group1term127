with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

print("CSS matches for center-post:")
for line in css.splitlines():
    if 'center-post' in line:
        print("  ", line[:100])

print("\nJS matches for center-post or focal_lead:")
for line in js.splitlines():
    if 'center-post' in line or 'focal_lead' in line or 'hero-center' in line:
        print("  ", line[:100])
