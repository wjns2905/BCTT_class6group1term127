import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

pos = css.find('floating-heart-particle')
if pos != -1:
    print("Found in style.css at pos", pos)
    print(css[pos:pos+400])
else:
    print("floating-heart-particle NOT FOUND in style.css!")
