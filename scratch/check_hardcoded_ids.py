import os
import re

files_to_check = ['index.html', 'trending.html', 'society.html', 'human-stories.html', 'mind-soul.html', 'in-depth.html', 'about.html', 'js/app.js']

for f in files_to_check:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
        # Find occurrences of trending-, society-, human-, mind-, indepth-, video-
        matches = re.findall(r'(?:trending|society|human|mind|indepth|video)-\d+', content)
        if matches:
            print(f"In {f}: {sorted(set(matches))}")
