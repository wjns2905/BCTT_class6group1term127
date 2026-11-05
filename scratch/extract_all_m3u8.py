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

streams = {}

for clip_id, url in vtv_urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Extract data-vid
            m_vid = re.search(r'data-vid=["\']?(https://[^\s"\'<>]+master\.m3u8)', html)
            if not m_vid:
                m_vid = re.search(r'(https://cdn-videos\.vtv\.vn/[^\s"\'<>]+master\.m3u8)', html)
            
            if m_vid:
                streams[clip_id] = m_vid.group(1)
                print(f"{clip_id}: {m_vid.group(1)}")
            else:
                # check any m3u8
                all_m3u8 = re.findall(r'(https://[^\s"\'<>]+\.m3u8)', html)
                print(f"{clip_id}: No direct master.m3u8, all found: {all_m3u8}")
                if all_m3u8:
                    streams[clip_id] = all_m3u8[0]
    except Exception as e:
        print(f"Error {clip_id}: {e}")

print("\n--- RESULTS DICT ---")
for k, v in streams.items():
    print(f'"{k}": "{v}",')
