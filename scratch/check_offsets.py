import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Locate VIDEO_CLIPS to the start of openArticleModal
clips_start = js.find('const VIDEO_CLIPS = [')
render_start = js.find('function renderVideoHub()')
play_start = js.find('function playActiveVideo(')
article_modal_start = js.find('function formatArticleSource(')

print(f"clips_start: {clips_start}")
print(f"render_start: {render_start}")
print(f"play_start: {play_start}")
print(f"article_modal_start: {article_modal_start}")
