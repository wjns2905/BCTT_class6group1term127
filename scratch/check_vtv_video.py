import urllib.request
import re, sys
sys.stdout.reconfigure(encoding='utf-8')

url = "https://vietnamtoday.vtv.vn/ao-dai-celebrates-vietnamese-culture-in-finland-100261028101457215.htm"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8', errors='ignore')
        print(f"Status 200, length: {len(html)}")
        
        # Look for video tags, mp4 links, m3u8, youtube embeds, iframes
        videos = re.findall(r'(https?://[^\s"\'<>]+\.(?:mp4|m3u8)[^\s"\'<>]*)', html)
        print("Video URLs found:", len(videos), videos[:5])
        
        iframes = re.findall(r'<iframe[^>]+src=["\']([^"\']+)["\']', html)
        print("Iframes found:", len(iframes), iframes)
        
        # Look for player data
        player_matches = re.findall(r'(data-src=["\'][^"\']+["\']|type=["\']video/[^"\']+["\'])', html)
        print("Player tags:", player_matches[:5])
        
        # Check title
        m_title = re.search(r'<title>(.*?)</title>', html)
        print("Title:", m_title.group(1) if m_title else "No title")
except Exception as e:
    print("Error:", e)
