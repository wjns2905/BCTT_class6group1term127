import urllib.request
import re, sys
sys.stdout.reconfigure(encoding='utf-8')

url = "https://vietnamtoday.vtv.vn/ao-dai-celebrates-vietnamese-culture-in-finland-100261028101457215.htm"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=10) as response:
    html = response.read().decode('utf-8', errors='ignore')

# Search for "video" or "player" or "hls" or "m3u8"
for m in re.finditer(r'([^\n]{0,100}ao-dai[^\n]{0,200})', html, re.IGNORECASE):
    print(m.group(0))
    print('-'*40)
