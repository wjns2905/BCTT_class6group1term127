import urllib.request
import sys
sys.stdout.reconfigure(encoding='utf-8')

test_url = "https://cdn-videos.vtv.vn/66349b6076cb4dee98746cf1/2026/10/28/h264/mp4/ao-dai-27533120378672986580995.mp4"
req = urllib.request.Request(test_url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
req.add_header('Referer', 'https://vietnamtoday.vtv.vn/')

try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        print("Status:", resp.status)
        print("Content-Type:", resp.headers.get('Content-Type'))
        data = resp.read(2048)
        print("Success! Read first 2KB, magic bytes:", data[:12])
except Exception as e:
    print("Error with referer:", e)
