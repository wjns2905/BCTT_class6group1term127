from PIL import Image
import sys
sys.stdout.reconfigure(encoding='utf-8')

im = Image.open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\assets\images\ads\header_ad_banner.png')
print("Image size:", im.size, "Mode:", im.mode)
