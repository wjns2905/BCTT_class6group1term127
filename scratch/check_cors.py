import urllib.request
import sys
sys.stdout.reconfigure(encoding='utf-8')

test_m3u8 = "https://cdn-videos.vtv.vn/66349b6076cb4dee98746cf1/2026/10/28/h264/mp4/ao-dai-27533120378672986580995.mp4/master.m3u8"
req = urllib.request.Request(test_m3u8)
req.add_header('User-Agent', 'Mozilla/5.0')
req.add_header('Origin', 'http://localhost:3000')

try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        print("Status:", resp.status)
        for k, v in resp.headers.items():
            if 'access-control' in k.lower():
                print(f"{k}: {v}")
except Exception as e:
    print("Error:", e)
