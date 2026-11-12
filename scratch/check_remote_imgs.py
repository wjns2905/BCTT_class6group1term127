import urllib.request

urls = [
    'https://wjns2905.github.io/BCTT_class6group1term127/assets/images/trending/ngoc_mai/passerby_kindness.jpg',
    'https://wjns2905.github.io/BCTT_class6group1term127/assets/images/trending/ngoc_mai/hat_and_jacket.jpg',
    'https://wjns2905.github.io/BCTT_class6group1term127/assets/images/trending/image8.jpg'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(u, '->', resp.status)
    except Exception as e:
        print(u, '-> ERROR:', e)
