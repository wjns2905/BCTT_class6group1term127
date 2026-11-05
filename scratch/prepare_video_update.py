import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Let's inspect around VIDEO_CLIPS start and end
idx_clips = js.find('const VIDEO_CLIPS = [')
idx_render = js.find('function renderVideoHub()')
idx_play = js.find('function playActiveVideo(')
idx_journal = js.find('function renderFashionJournal(')

print(f"Indices: clips={idx_clips}, render={idx_render}, play={idx_play}, journal={idx_journal}")
