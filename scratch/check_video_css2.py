import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

print("Contains video-native-player:", ".video-native-player" in css)
print("Contains video inside embed:", "video-responsive-embed video" in css)
