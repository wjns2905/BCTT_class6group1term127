import urllib.request
import sys
sys.stdout.reconfigure(encoding='utf-8')

urls = [
    ("Facebook", "https://www.facebook.com/share/1US9HuksEu/?mibextid=wwXIfr"),
    ("Instagram", "https://www.instagram.com/hearticles.news"),
    ("Instagram QR", "https://www.instagram.com/hearticles.news?vrfl=MTZybHZncnU2aDZobw%3D%3D&utm_source=qr"),
    ("X", "https://x.com/hearticles_news?s=11"),
    ("X plain", "https://x.com/hearticles_news"),
    ("Twitter plain", "https://twitter.com/hearticles_news")
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for name, url in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"[{name}] {resp.status} -> Final URL: {resp.url}")
    except urllib.error.HTTPError as e:
        print(f"[{name}] HTTP Error: {e.code} for {url}")
    except Exception as e:
        print(f"[{name}] Error: {e}")
