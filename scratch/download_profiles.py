# -*- coding: utf-8 -*-
import os
import sys
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')

profiles = [
    ("ngoc_mai", "12iBmOhoAJ7vhARNzZ8taAwKWj3olLZ58", "Nguyễn Thị Ngọc Mai"),
    ("ha_anh", "199Ap6dDfLulOwq0vUsz0kkwhN5m_Km5D", "Lê Hà Anh"),
    ("phuong_anh", "14mmsv4JL3SxAuxv9g_PuZpRJ-rp4Q-b2", "Bùi Phương Anh"),
    ("bao_ngan", "1nK19NJdpzaiFkY1Xpv-pKfL1Kwk_XXKv", "Bùi Bảo Ngân"),
    ("nhu_quynh", "1wQKS64eBLfWUowReSuBclJEVzu0C2go2", "Nguyễn Như Quỳnh")
]

out_dir = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\assets\images\profiles"
os.makedirs(out_dir, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def download_file(file_id, filename_base):
    # Try multiple direct download URLs
    urls = [
        f"https://drive.usercontent.google.com/download?id={file_id}&export=download",
        f"https://drive.google.com/uc?export=download&id={file_id}",
        f"https://lh3.googleusercontent.com/d/{file_id}"
    ]
    
    for url in urls:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read()
                content_type = resp.headers.get('Content-Type', '')
                print(f"URL: {url} -> Content-Type: {content_type}, Size: {len(content)} bytes")
                
                # Check if it's an image
                if 'image' in content_type or len(content) > 10000:
                    ext = ".jpg"
                    if "png" in content_type or content.startswith(b'\x89PNG'):
                        ext = ".png"
                    elif "jpeg" in content_type or "jpg" in content_type or content.startswith(b'\xff\xd8'):
                        ext = ".jpg"
                    elif "webp" in content_type or b'WEBP' in content[:16]:
                        ext = ".webp"
                    elif "heic" in content_type or b'ftypheic' in content[:16]:
                        ext = ".heic"
                    
                    target = os.path.join(out_dir, f"{filename_base}{ext}")
                    with open(target, 'wb') as f:
                        f.write(content)
                    print(f"==> Successfully saved {target} ({len(content)} bytes)")
                    return f"assets/images/profiles/{filename_base}{ext}"
                else:
                    print(f"Skipping: Response is not image data (likely html confirmation: {content[:200]})")
        except Exception as e:
            print(f"Failed {url}: {e}")
    return None

results = {}
for key, fid, name in profiles:
    print(f"\nDownloading profile photo for {name} ({key})...")
    saved_path = download_file(fid, key)
    results[key] = saved_path

print("\nFinal Results:")
for k, v in results.items():
    print(f"  {k}: {v}")
