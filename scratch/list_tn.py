import os, sys
sys.stdout.reconfigure(encoding='utf-8')

tn_dir = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\Tài nguyên'
for f in os.listdir(tn_dir):
    print(repr(f))
