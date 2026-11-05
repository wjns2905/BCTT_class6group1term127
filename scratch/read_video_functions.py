import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# find from renderVideoHub to end of playActiveVideo
start = code.find('function renderVideoHub()')
end = code.find('function openArticleModal(', start)
print(code[start:end])
