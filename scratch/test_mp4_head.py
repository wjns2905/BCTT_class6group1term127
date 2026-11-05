import urllib.request
import sys
sys.stdout.reconfigure(encoding='utf-8')

test_url = "https://cdn-videos.vtv.vn/66349b6076cb4dee98746cf1/2026/10/28/h264/mp4/ao-dai-27533120378672986580995.mp4"
req = urllib.request.Request(test_url, method='HEAD')
req.add_header('User-Agent', 'Mozilla/5.0')

try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        print("Status:", resp.status)
        print("Content-Type:", resp.headers.get('Content-Type'))
        print("Content-Length:", resp.headers.get('Content-Length'))
        print("Accept-Ranges:", resp.headers.get('Accept-Ranges'))
        print("Access-Control-Allow-Origin:", resp.headers.get('Access-Control-Allow-Origin'))
except Exception as e:
    print("Error:", e)
