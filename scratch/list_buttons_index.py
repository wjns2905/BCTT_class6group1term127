import sys, re

sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'<[a-zA-Z0-9]+[^>]+(?:class|style)="[^"]*(?:pill|btn|button|subscribe)[^"]*"[^>]*>.*?</[a-zA-Z0-9]+>', text, re.DOTALL)
print(f"Total elements: {len(matches)}")
for m in matches:
    # replace newlines
    one_line = ' '.join(m.split())
    print("  ", one_line[:120])
