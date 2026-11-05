import urllib.request
import sys
sys.stdout.reconfigure(encoding='utf-8')

chunk_url = "https://cdn-videos.vtv.vn/66349b6076cb4dee98746cf1/2026/10/28/h264/mp4/ao-dai-27533120378672986580995.mp4/index-f3-v1-a1.m3u8"
req = urllib.request.Request(chunk_url)
req.add_header('User-Agent', 'Mozilla/5.0')
req.add_header('Origin', 'null')

try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        print("Status:", resp.status)
        content = resp.read().decode('utf-8')
        print("Subplaylist:\n", content[:300])
        first_ts = [l for l in content.splitlines() if l.endswith('.ts')][0]
        ts_url = f"https://cdn-videos.vtv.vn/66349b6076cb4dee98746cf1/2026/10/28/h264/mp4/ao-dai-27533120378672986580995.mp4/{first_ts}"
        print("First TS URL:", ts_url)
        
        req_ts = urllib.request.Request(ts_url)
        req_ts.add_header('User-Agent', 'Mozilla/5.0')
        with urllib.request.urlopen(req_ts, timeout=10) as resp_ts:
            print("TS Status:", resp_ts.status, "Length:", resp_ts.headers.get('Content-Length'))
            print("TS CORS:", resp_ts.headers.get('Access-Control-Allow-Origin'))
except Exception as e:
    print("Error:", e)
