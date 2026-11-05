import sys, re

sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all openArticleModal calls in index.html
matches = re.findall(r"openArticleModal\('([^']+)'\)", text)
print(f"Total openArticleModal in index.html: {len(matches)}")
print("IDs:", matches)

# Find all <img> src inside index.html
imgs = re.findall(r'<img[^>]+src="([^"]+)"[^>]*>', text)
print(f"Total images in index.html: {len(imgs)}")
for img in imgs:
    if 'assets/images' in img:
        print("  ", img)
