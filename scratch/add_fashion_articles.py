import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

DATA_PATH = r"c:\Users\camka\OneDrive\Desktop\BCTT\js\data.js"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    text = f.read()

prefix = "const ARTICLES_DATA = "
suffix = ";"

json_text = text.split(prefix, 1)[1].rsplit(suffix, 1)[0].strip()
articles = json.loads(json_text)
print("Current count:", len(articles))

new_articles = [
  {
    "id": "cover-story-her",
    "category": "her",
    "categoryName": "Her",
    "title": "More Than Just a Pretty Face: Redefining Beauty in the Gen Z Era",
    "subtitle": "Why are young women still expected to fit into society's definition of beauty?",
    "author": "Ban Biên Tập Chuyên mục Her • ULIS - VNU",
    "date": "04/11/2026",
    "readTime": "6 min read",
    "sourceName": "HEARTICLES Fashion & Culture • ULIS - VNU",
    "sourceUrl": "#",
    "image": "assets/images/editorial/hd_cover_girl_portrait.jpg",
    "imageCaption": "Nét đẹp tự nhiên, tự tin và đa dạng của phụ nữ trẻ thế hệ Gen Z không còn bị ràng buộc bởi các quy chuẩn sắc đẹp truyền thống.",
    "video": "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    "isTopPost": True,
    "isBreaking": False,
    "views": 12450,
    "likes": 892,
    "tags": ["Her", "Cover Story", "Beauty", "Gen Z", "Lifestyle"],
    "content": """<p class="lead-paragraph">Tại sao phụ nữ trẻ ngày nay vẫn bị kỳ vọng phải vừa vặn với những định nghĩa sắc đẹp do xã hội đặt ra? Giữa kỷ nguyên số nơi các bộ lọc mạng xã hội liên tục tạo ra những ảo tưởng hoàn hảo, thế hệ phụ nữ Gen Z đang tiên phong viết lại chuẩn mực: Vẻ đẹp đích thực khởi nguồn từ sự thấu hiểu bản thân, lòng trắc ẩn và cá tính độc bản.</p>

<div class="editorial-pullquote">
  <blockquote>"Sắc đẹp không phải là chiếc khuôn đúc sẵn để bạn gọt giũa chính mình, mà là tấm gương phản chiếu sự tự do và sức mạnh nội tại."</blockquote>
  <cite>— Nhóm phóng viên Chuyên đề Her, ULIS - VNU</cite>
</div>

<p>Từ những buổi thảo luận văn hóa tại Trường Đại học Ngoại ngữ - ĐHQGHN cho đến các phong trào tôn vinh cơ thể tự nhiên trên mạng xã hội, các bạn trẻ đang dũng cảm nói không với sự phán xét ngoại hình (body shaming) và chủ nghĩa hoàn hảo độc hại. Họ học cách yêu những vết tàn nhang, nụ cười không góc chết và cả những ngày mỏi mệt.</p>

<p>Vẻ đẹp trong thời đại mới là sự kết hợp hài hòa giữa tri thức, bản lĩnh độc lập và tâm hồn nhân ái. Đó không chỉ là câu chuyện của thời trang hay mỹ phẩm, mà là hành trình phụ nữ khẳng định tiếng nói, quyền tự quyết và giá trị nhân văn của chính mình trong đời sống đương đại.</p>"""
  },
  {
    "id": "latest-loneliness",
    "category": "trending",
    "categoryName": "Trending",
    "title": "The Loneliness Behind the Likes",
    "subtitle": "Nghịch lý cô đơn sau hàng ngàn lượt tương tác ảo trên mạng xã hội của giới trẻ.",
    "author": "Thanh Hằng • Ban Văn hóa Số",
    "date": "03/11/2026",
    "readTime": "4 min read",
    "sourceName": "HEARTICLES Trending",
    "sourceUrl": "#",
    "image": "assets/images/editorial/hd_thumb_loneliness.jpg",
    "imageCaption": "Ánh sáng xanh từ màn hình điện thoại và khoảng trống tâm hồn trong thế giới ảo.",
    "video": "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    "isTopPost": False,
    "isBreaking": True,
    "views": 8620,
    "likes": 640,
    "tags": ["Trending", "Social Media", "Mental Health", "Youth"],
    "content": """<p class="lead-paragraph">Chúng ta đang sống trong kỷ nguyên kết nối cao nhất lịch sử nhân loại, nhưng đồng thời cũng là thế hệ cô đơn nhất. Một bức ảnh ngập tràn lượt thả tim trên Instagram không đồng nghĩa với một tâm hồn được lắng nghe và vỗ về.</p>

<p>Các chuyên gia tâm lý học cảnh báo hiện tượng 'FOMO' (sợ bị bỏ lỡ) và việc liên tục so sánh cuộc đời mình với những khoảnh khắc được chọn lọc kỹ càng của người khác đang làm xói mòn lòng tự trọng của người trẻ. Để tìm lại sự bình yên, nhiều bạn trẻ đang thực hành 'Digital Detox' — tắt thông báo, rời xa màn hình và tìm kiếm những cuộc gặp gỡ trực tiếp bằng ánh mắt và trái tim.</p>"""
  },
  {
    "id": "latest-small-acts",
    "category": "human-stories",
    "categoryName": "Human Stories",
    "title": "Small Acts, Big Changes",
    "subtitle": "Những hành động tử tế bình dị đang âm thầm thắp sáng và chữa lành cộng đồng.",
    "author": "Minh Thảo • Ban Đời sống",
    "date": "02/11/2026",
    "readTime": "5 min read",
    "sourceName": "HEARTICLES Human Stories",
    "sourceUrl": "#",
    "image": "assets/images/editorial/hd_thumb_small_acts.jpg",
    "imageCaption": "Một nhành hoa trao tay giữa phố phường Hà Nội những ngày đầu đông.",
    "video": "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    "isTopPost": False,
    "isBreaking": False,
    "views": 7430,
    "likes": 520,
    "tags": ["Human Stories", "Kindness", "Community", "Inspiration"],
    "content": """<p class="lead-paragraph">Không cần phải là một anh hùng với những chiến công vĩ đại, sự thay đổi tích cực của thế giới thường bắt đầu từ những hành động nhỏ bé nhất: Một nụ cười với người quét rác, một cốc trà nóng cho người bán hàng rong hay một nhành hoa trao tặng người xa lạ.</p>

<p>Câu chuyện về nhóm sinh viên tình nguyện ULIS mỗi sáng cuối tuần mang những bữa sáng ấm lòng cho các cụ già neo đơn là minh chứng sống động rằng: Lòng tốt có tính lan tỏa, và khi bạn gieo một hạt mầm nhân ái, cả khu rừng của niềm tin sẽ nảy lộc.</p>"""
  },
  {
    "id": "latest-hurry",
    "category": "mind-soul",
    "categoryName": "Mind & Soul",
    "title": "Why Are We Always in a Hurry?",
    "subtitle": "Tâm lý học về năng suất độc hại và nghệ thuật sống chậm giữa nhịp sống hối hả.",
    "author": "Bảo Châu • Ban Tâm lý & Sống chậm",
    "date": "01/11/2026",
    "readTime": "7 min read",
    "sourceName": "HEARTICLES Mind & Soul",
    "sourceUrl": "#",
    "image": "assets/images/editorial/thumb_sunset_exact.jpg",
    "imageCaption": "Khoảnh khắc tĩnh lặng ngắm hoàng hôn buông xuống hồ Tây sau một ngày bận rộn.",
    "video": "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    "isTopPost": False,
    "isBreaking": False,
    "views": 9150,
    "likes": 815,
    "tags": ["Mind & Soul", "Slow Living", "Mindfulness", "Wellness"],
    "content": """<p class="lead-paragraph">Tại sao chúng ta luôn có cảm giác mình đang trễ hẹn với một điều gì đó? Áp lực phải thành công trước tuổi 25, danh sách việc cần làm không bao giờ vơi và nỗi sợ đứng yên đang biến cuộc sống thành một cuộc đua kiệt sức.</p>

<p>Sống chậm (Slow Living) không phải là lười biếng hay trốn tránh trách nhiệm, mà là sự lựa chọn tỉnh thức: Chậm lại để cảm nhận từng ngụm cà phê sáng, để lắng nghe người thân nói hết một câu chuyện và để trái tim có đủ không gian hít thở giữa những bộn bề lo toan.</p>"""
  },
  {
    "id": "feature-she-definition",
    "category": "her",
    "categoryName": "Her",
    "title": "She Is Not Your Definition of Her",
    "subtitle": "A space for women to speak, question and redefine their own stories.",
    "author": "Ban Biên Tập Chuyên mục Her • ULIS - VNU",
    "date": "04/11/2026",
    "readTime": "5 min read",
    "sourceName": "HEARTICLES Her Voice",
    "sourceUrl": "#",
    "image": "assets/images/editorial/hd_her_walking.jpg",
    "imageCaption": "Mỗi bước chân của người phụ nữ tự chủ là một lời khẳng định về tự do cá nhân.",
    "video": "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    "isTopPost": False,
    "isBreaking": False,
    "views": 6820,
    "likes": 590,
    "tags": ["Her", "Women Empowerment", "Voice", "Culture"],
    "content": """<p class="lead-paragraph">Phụ nữ không phải là cái bóng trong định kiến của người khác. Dù lựa chọn cống hiến cho sự nghiệp nghiên cứu, kinh doanh, hay chọn cuộc sống bình dị bên gia đình, giá trị của họ nằm ở sự tự do lựa chọn và hạnh phúc nội tại.</p>

<p>Chuyên mục Her Voice trên HEARTICLES mở ra diễn đàn đa thanh sắc để nữ sinh viên ULIS và phụ nữ hiện đại chia sẻ những tâm tư, nỗi trăn trở và ước vọng xây dựng một xã hội tôn trọng sự bình đẳng và tình yêu thương chân thành.</p>"""
  }
]

existing_ids = {a["id"] for a in articles}
added_articles = [a for a in new_articles if a["id"] not in existing_ids]

all_articles = added_articles + articles
print("New total count:", len(all_articles))

new_js = f"""// HEART.ICLES News Portal Data
// High-Fashion Editorial Edition (Vogue / Kinfolk / Elle Aesthetic)
// Class 6 - Group 1 - Term 127 • Trường Đại học Ngoại ngữ - ĐHQGHN (ULIS - VNU)
const ARTICLES_DATA = {json.dumps(all_articles, ensure_ascii=False, indent=2)};
"""

with open(DATA_PATH, "w", encoding="utf-8") as f:
    f.write(new_js)

print("Updated js/data.js successfully with fashion editorial articles!")
