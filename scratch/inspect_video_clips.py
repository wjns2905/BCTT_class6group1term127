import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    c = f.read()

# Find VIDEO_CLIPS definition
start = c.find('const VIDEO_CLIPS = [')
end = c.find('];', start) + 2

print(c[start:end])
