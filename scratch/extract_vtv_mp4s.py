import urllib.request
import re, sys
sys.stdout.reconfigure(encoding='utf-8')

vtv_urls = [
    ("clip-1", "https://vietnamtoday.vtv.vn/ao-dai-celebrates-vietnamese-culture-in-finland-100261028101457215.htm"),
    ("clip-2", "https://vietnamtoday.vtv.vn/viet-nam-tackles-gaps-in-child-online-safety-100261101165727007.htm"),
    ("clip-5", "https://vietnamtoday.vtv.vn/a-stage-for-every-voice-100261029064303631.htm"),
    ("clip-6", "https://vietnamtoday.vtv.vn/10-years-of-free-violin-lessons-in-park-100261029064839361.htm"),
    ("clip-7", "https://vietnamtoday.vtv.vn/thai-nguyen-tea-culture-boosts-tourism-100261101042721506.htm"),
    ("clip-8", "https://vietnamtoday.vtv.vn/mother-turns-meals-into-art-100260710095813651.htm"),
    ("clip-9", "https://vietnamtoday.vtv.vn/a-healing-oasis-in-ho-chi-minh-city-100260910032153068.htm"),
    ("clip-10", "https://vietnamtoday.vtv.vn/community-facilities-promote-healthier-lifestyles-100261019013046705.htm"),
    ("clip-11", "https://vietnamtoday.vtv.vn/extraordinary-mothers-extraordinary-love-10026051107442239.htm"),
    ("clip-12", "https://vietnamtoday.vtv.vn/youth-caring-for-the-elderly-100260226123528559.htm"),
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

results = {}

for clip_id, url in vtv_urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
            # Find the primary mp4 for the article video
            # Look for player json / data-video or cdn-videos mp4
            # Usually the article's own video matches the article title or slug or appears first in the main video block
            # Let's inspect all cdn-videos mp4 in order
            mp4s = re.findall(r'(https://cdn-videos\.vtv\.vn/[^\s"\'<>]+\.mp4)', html)
            # Filter out master.m3u8 if any, keep pure .mp4
            pure_mp4s = [u for u in mp4s if not u.endswith('.m3u8')]
            print(f"[{clip_id}] Found {len(pure_mp4s)} mp4s for {url.split('/')[-1]}")
            if pure_mp4s:
                # The primary video of the article is usually the one that isn't the sidebar / footer recommendations
                # Let's see all unique ones
                seen = []
                for p in pure_mp4s:
                    if p not in seen: seen.append(p)
                print(f"  First: {seen[0]}")
                if len(seen) > 1:
                    print(f"  Others: {seen[1:3]}")
                results[clip_id] = seen[0]
            else:
                results[clip_id] = None
    except Exception as e:
        print(f"[{clip_id}] Error: {e}")
        results[clip_id] = None

print("\n--- SUMMARY OF MP4s ---")
for k, v in results.items():
    print(f"'{k}': '{v}',")
