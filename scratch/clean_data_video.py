import re

path = 'C:/Users/camka/OneDrive/Desktop/BCTT_class6group1term127/js/data.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# List of article IDs where video was erroneously added and should be cleared
# Only human-3 and video-3 should keep video
to_clear_ids = [
    'trending-1',
    'human-1',
    'human-2',
    'mind-1',
    'society-1',
    'indepth-1',
    'human-5',
    'mind-5',
    'indepth-3',
    'indepth-5'
]

# We can parse or replace accurately
for art_id in to_clear_ids:
    # Match the article block starting with "id": "art_id" up to "video": "..."
    # Replace "video": "https://www.youtube.com/embed/8t07V5aCcME" with "video": ""
    pattern = rf'("id":\s*"{art_id}"[\s\S]*?"video":\s*)"https://www\.youtube\.com/embed/8t07V5aCcME"'
    content, count = re.subn(pattern, r'\1""', content, count=1)
    print(f'Cleared video for {art_id}: {count} replacements')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated data.js successfully.')
