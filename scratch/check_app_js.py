import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Look for functions rendering articles or pagination
funcs = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', code)
print("Functions in app.js:", funcs)

# Check for renderCategoryArticles, renderArticles, etc.
for line in code.splitlines():
    if any(k in line for k in ['renderCategory', 'loadMore', 'renderArticles', 'filterByCategory', 'paginate']):
        print("  ", line.strip())
