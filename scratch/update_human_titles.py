import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
e = c.rfind('];') + 1

articles = json.loads(c[s:e])

human_updates = {
    "human-1": {
        "title": "Thấu hiểu nỗi cô đơn tuổi già: Khi những người trẻ chọn bước tới để trao đi sự lắng nghe",
        "subtitle": "Một chương trình tình nguyện kết nối hai thế hệ giúp các cụ già neo đơn tìm lại niềm vui và cảm giác được trân trọng."
    },
    "human-2": {
        "title": "Chiếc túi ân tình: Món quà nhỏ làm thay đổi cuộc đời người cựu chiến binh vô gia cư",
        "subtitle": "Từ một người lang thang mất hết niềm tin, anh đã đứng dậy và trở thành người tự tay phân phát hàng nghìn túi cứu trợ trên đường phố."
    },
    "human-3": {
        "title": "Phép màu hồi sinh của chàng trai bom đạn Iraq Qusay Hussein: 'Tôi được trao cơ hội sống thứ hai'",
        "subtitle": "Mất đi đôi mắt và khuôn mặt sau vụ nổ kinh hoàng, chàng trai trẻ đã vượt qua 50 cuộc phẫu thuật để trở thành người truyền cảm hứng sống."
    },
    "human-4": {
        "title": "Nghĩa cử hào hiệp: Những nông dân thiện nguyện gây quỹ 400.000 USD mỗi năm cho học sinh nghèo",
        "subtitle": "Cùng nhau gieo hạt, gặt hái và dành trọn lợi nhuận từ những cánh đồng ngô để tiếp sức cho con em lao động nghèo bước chân vào giảng đường."
    },
    "human-5": {
        "title": "Thầy giáo gùi chữ 20 năm qua đỉnh núi mờ sương Nam Trà My: Đôi chân trần vì nụ cười trẻ thơ",
        "title_en": "The Barefoot Teacher of Nam Tra My: 20 Years Climbing Misty Peaks to Bring Literacy to Children",
        "subtitle": "Băng rừng, lội suối, vượt qua những cơn sốt rét rừng hiểm nghèo để mang con chữ và ánh sáng tri thức đến với đồng bào vùng cao."
    },
    "human-6": {
        "title": "Hành trình 15 năm tìm con thất lạc: Phép màu từ tình thương và sự kiên trì của người cha nghèo",
        "title_en": "A Father's 15-Year Search: How Love and Unyielding Faith Reunited a Lost Son",
        "subtitle": "Đi khắp mọi miền đất nước với chiếc ba lô sờn cũ và tấm ảnh đã phai màu, người cha chưa bao giờ từ bỏ hy vọng được ôm con vào lòng."
    },
    "human-7": {
        "title": "Quán cơm 0 đồng bên cổng bệnh viện: Bữa ăn nóng hổi và nụ cười xoa dịu nỗi đau bệnh tật",
        "title_en": "The Zero-Dong Cafeteria: Free Nutritious Meals and Warm Smiles for Hospital Families",
        "subtitle": "Mỗi ngày hơn 1.000 suất ăn đầy đặn được trao tận tay những thân nhân người bệnh khó khăn, thắp lên ngọn lửa ấm áp của tình người."
    },
    "human-8": {
        "title": "Người gác rừng Cát Tiên: Cuộc chiến thầm lặng ngày đêm cứu hộ động vật hoang dã trước bẫy trộm",
        "title_en": "Guardian of Cat Tien: A Ranger's Silent Nightly Crusade Protecting Wildlife from Poachers",
        "subtitle": "Những bước chân tuần rừng không mệt mỏi tháo gỡ hàng nghìn bẫy dây thép gai, giành giật từng mạng sống của tê tê, nai vàng và khỉ mặt đỏ."
    },
    "human-9": {
        "title": "Món quà chuyển động: 1,5 triệu chiếc xe lăn trao tặng người khuyết tật tìm lại sự tự do",
        "title_en": "The Gift of Mobility: How One Nonprofit Delivered 1.5 Million Wheelchairs Worldwide",
        "subtitle": "Chiếc xe lăn địa hình bền bỉ giúp những phận đời bất hạnh tại các làng quê nghèo có thể tự mình đến trường, đi làm và làm chủ cuộc sống."
    },
    "human-10": {
        "title": "Dòng điện sáng bừng bản nghèo Bồng Lai: Niềm vui vỡ òa của đồng bào sau nhiều năm sống trong bóng tối",
        "title_en": "Stable Electricity Brings Light to Bong Lai: Mountain Hamlets Celebrate Historic Modernization",
        "subtitle": "Hơn 400 hộ dân đồng bào vùng sâu Quảng Trị đón dòng điện lưới quốc gia, giã từ ngọn đèn dầu tù mù và mở ra tương lai ấm no."
    }
}

for a in articles:
    if a['id'] in human_updates:
        u = human_updates[a['id']]
        a['title'] = u['title']
        a['subtitle'] = u['subtitle']
        if 'title_en' in u:
            a['title_en'] = u['title_en']

formatted = json.dumps(articles, ensure_ascii=False, indent=2)
new_c = c[:s] + formatted + c[e:]

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(new_c)

print("Updated human-stories titles for rich, touching emotional depth!")
