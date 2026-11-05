import urllib.request, os

test_images = {
    'assets/images/trending/robusta_coffee_vietnam.jpg': 'https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=900&q=80',
    'assets/images/society/hanoi_metro_railway.jpg': 'https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?w=900&q=80',
    'assets/images/mind_&_soul/shan_tuyet_ancient_tea.jpg': 'https://images.unsplash.com/photo-1576092768241-dec231879fc3?w=900&q=80',
    'assets/images/in-dept/dong_ho_folk_painting.jpg': 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=900&q=80'
}

for path, url in test_images.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=15) as resp:
        content = resp.read()
    with open(path, 'wb') as f:
        f.write(content)
    print(f'Downloaded {path}: {len(content)} bytes')
