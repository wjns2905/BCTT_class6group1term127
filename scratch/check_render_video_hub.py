import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

start = js.find('function renderVideoHub()')
end = js.find('function playActiveVideo(', start)
print(js[start:end])
