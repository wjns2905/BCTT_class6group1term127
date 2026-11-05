import urllib.request
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

hls_url = "https://cdn.jsdelivr.net/npm/hls.js@1.5.11/dist/hls.min.js"
out_path = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\hls.min.js'

try:
    req = urllib.request.Request(hls_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=15) as resp:
        content = resp.read()
        with open(out_path, 'wb') as f:
            f.write(content)
        print(f"Successfully downloaded hls.min.js! Size: {len(content)} bytes")
except Exception as e:
    print("Download error:", e)
