import os

BASE_DIR = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127"

files = [
    'index.html',
    'trending.html',
    'society.html',
    'human-stories.html',
    'mind-soul.html',
    'in-depth.html',
    'about.html',
    'article.html',
    'hearticles/madeuparticle/index.html',
    'js/translations.js',
    'js/app.js',
    'js/data.js'
]

print("=== 1. VERIFYING NO 'BCTT' IN USER-FACING FILES ===")
total_bctt = 0
for f in files:
    path = os.path.join(BASE_DIR, f)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as fp:
        content = fp.read()
    count = content.count('BCTT')
    total_bctt += count
    if count == 0:
        print(f"PASS: {f} has 0 occurrences of BCTT")
    else:
        print(f"FAIL: {f} has {count} occurrences of BCTT!")

print(f"Total user-facing BCTT found: {total_bctt}")
assert total_bctt == 0, "BCTT found in user-facing files!"

print("\n=== 2. VERIFYING TITLES ===")
for f in ['index.html', 'trending.html', 'society.html', 'human-stories.html', 'mind-soul.html', 'in-depth.html', 'about.html', 'article.html']:
    path = os.path.join(BASE_DIR, f)
    with open(path, 'r', encoding='utf-8') as fp:
        content = fp.read()
    for line in content.split('\n'):
        if '<title' in line:
            print(f"{f} title: {line.strip()}")

print("\nVERIFICATION COMPLETED SUCCESSFULLY.")
