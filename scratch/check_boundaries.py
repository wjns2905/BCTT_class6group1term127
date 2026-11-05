import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

print("BEFORE clips:")
print(js[5950:6123])
print("\n" + "="*50 + "\nAFTER play/switch:")
print(js[28500:28750])
