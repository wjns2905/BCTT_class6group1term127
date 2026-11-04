p = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js"
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("readers' hearts", "readers\\' hearts")

with open(p, 'w', encoding='utf-8') as f:
    f.write(text)

print("Apostrophe fixed successfully!")
