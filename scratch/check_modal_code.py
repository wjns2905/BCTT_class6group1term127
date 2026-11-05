import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

start = code.find('function openArticleModal(')
end = code.find('function closeArticleModal(', start)

print(code[start:end])
