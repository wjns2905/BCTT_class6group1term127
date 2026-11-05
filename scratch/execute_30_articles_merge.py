import json
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read existing data.js
with open('js/data.js', 'r', encoding='utf-8') as f:
    original_code = f.read()

start_marker = 'const ARTICLES_DATA = '
start_idx = original_code.find(start_marker) + len(start_marker)
end_idx = original_code.rfind('];') + 1

existing_articles = json.loads(original_code[start_idx:end_idx])
print(f"Existing articles loaded: {len(existing_articles)}")

# Read full texts for missing authentic docx articles
import docx

doc_soc = docx.Document('Tài nguyên/[BCTT] Society.docx')
doc_mind = docx.Document('Tài nguyên/[BCTT] Mind & Soul.docx')

# Extract Banh cuon content
banh_cuon_paras = []
rec = False
for p in doc_mind.paragraphs:
    t = p.text.strip()
    if 'michelin-honored saigon eatery' in t.lower():
        rec = True
    elif rec and ('tài liệu tham khảo' in t.lower() or t.startswith('---')):
        rec = False
    if rec and t and not t.startswith('https://') and not t.startswith('Michelin-honored') and not t.startswith('Ha Nguyen'):
        banh_cuon_paras.append(t)

# Extract Tycoon villa content
tycoon_paras = []
rec = False
for p in doc_soc.paragraphs:
    t = p.text.strip()
    if 'inside hanoi tycoon' in t.lower():
        rec = True
    elif rec and t.startswith('Nga Thanh'):
        rec = False
    if rec and t and not t.startswith('https://') and not t.startswith('Inside Hanoi tycoon'):
        tycoon_paras.append(t)

# Extract Vietnam first timers content
vn_first_paras = []
rec = False
for p in doc_soc.paragraphs:
    t = p.text.strip()
    if 'vietnam for first-timers' in t.lower():
        rec = True
    elif 'inside hanoi tycoon' in t.lower():
        rec = False
    if rec and t and not t.startswith('https://') and not t.startswith('7. Vietnam for first-timers') and 'quảng cáo' not in t.lower() and not t.startswith('Photo:'):
        vn_first_paras.append(t)

print(f"Banh cuon paras: {len(banh_cuon_paras)}")
print(f"Tycoon paras: {len(tycoon_paras)}")
print(f"VN first-timers paras: {len(vn_first_paras)}")

# 30 New Articles List
new_articles = [
    # ================= TRENDING (7 articles: 1 authentic + 6 new) =================
    {
        "id": "trending-11",
        "category": "trending",
        "categoryName": "Trending",
        "title": "Vietnam for first-timers, beach lovers and nightlife seekers: Where to go?",
        "title_en": "Vietnam for first-timers, beach lovers and nightlife seekers: Where to go?",
        "subtitle": "From Hanoi’s historic streets and Ho Chi Minh City’s vibrant nightlife to Phu Quoc’s sandy beaches and Ha Giang’s majestic mountain loops, Vietnam offers unforgettable journeys.",
        "author": "Nam Tran & Nga Thanh • Tuoi Tre",
        "date": "Tuesday, November 3, 2026 - 15:30 (GMT+7)",
        "readTime": "6 min read",
        "sourceName": "Tuoi Tre News / Lonely Planet",
        "sourceUrl": "https://news.tuoitre.vn/travel/vietnam-for-first-timers-beach-lovers-and-nightlife-seekers-where-to-go.html",
        "image": "assets/images/society/image24.jpg",
        "imageCaption": "A view of Hoi An Ancient Town and its lantern-lined shophouses along the Thu Bon River. (Photo: Tuoi Tre)",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "18.4K",
        "likes": 842,
        "tags": ["Travel", "Vietnam Tourism", "Hoi An", "Hanoi", "Culture"],
        "content": [
            "Vietnam attracts travelers with its terraced rice fields, ancient historical sites, idyllic beaches, limestone karst towers and mouthwatering cuisine, which are regularly highlighted on international travel media.",
            "Vietnam’s historic capital Hanoi is an ideal starting point for first-time visitors, offering convenient international air connections and easy onward travel. Hanoi also serves as a gateway to the limestone islands of Ha Long Bay and the forested peaks of the northern highlands. Visitors can explore the city’s many attractions, sample street food, and relax at cozy sidewalk cafes.",
            "For underground adventures, Phong Nha - Ke Bang National Park in central Vietnam offers vast cave networks including Hang Son Doong, the world's largest cave. Meanwhile, Hue provides a deep dive into imperial history with its Citadel, royal tombs, and exquisite royal banquet cuisine.",
            "Hoi An in the central region offers a glimpse into Vietnam’s trading past with traditional shophouses, covered bridges, and assembly halls. For sunseekers, Phu Quoc in the south boasts sandy beaches and crystal-clear waters, while Ha Giang in the far north delivers dramatic limestone mountain passes and authentic ethnic community homestays."
        ]
    },
    {
        "id": "trending-12",
        "category": "trending",
        "categoryName": "Trending",
        "title": "Làn sóng Gen AI và tương lai ngành công nghiệp sáng tạo Đông Nam Á",
        "title_en": "Gen AI and the Future of Southeast Asian Creative Industries",
        "subtitle": "From digital design agencies in Hanoi to multimedia studios across the region, young creators are blending generative artificial intelligence with indigenous storytelling.",
        "author": "Lan Chi & TechTrends Asia",
        "date": "Wednesday, November 4, 2026 - 14:15 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "Tech In Asia",
        "sourceUrl": "https://www.techinasia.com/gen-ai-southeast-asia-creative-industry",
        "image": "assets/images/trending/image20.png",
        "imageCaption": "Young Vietnamese digital artists blending generative neural networks with traditional folklore illustration.",
        "video": "",
        "isTopPost": False,
        "isBreaking": True,
        "views": "21.6K",
        "likes": 930,
        "tags": ["Artificial Intelligence", "Creative Industry", "Gen Z", "Innovation"],
        "content": [
            "Across Southeast Asia's burgeoning tech hubs, generative AI is no longer a speculative concept—it is actively reshaping how digital art, animation, and cultural media are produced.",
            "In Hanoi and Ho Chi Minh City, independent game developers and visual artists are integrating custom diffusion models to accelerate world-building, while preserving deeply localized Vietnamese aesthetic motifs.",
            "“AI gives our small team the production capability of a Hollywood boutique studio,” says 24-year-old creative director Nguyen Tuan. “The key is using AI as an amplifier of human imagination rather than a replacement for soul and authentic storytelling.”"
        ]
    },
    {
        "id": "trending-13",
        "category": "trending",
        "categoryName": "Trending",
        "title": "Tuyến đường sắt tốc độ cao Bắc - Nam: Biểu tượng kết nối thế hệ mới",
        "title_en": "Vietnam's North-South High-Speed Rail: Next-Generation Connectivity",
        "subtitle": "Approved with strong national consensus, the 1,541-kilometer railway project will connect Hanoi and Ho Chi Minh City in under 6 hours, reshaping urbanization.",
        "author": "Minh Hoang • Vietnam Investment Review",
        "date": "Tuesday, November 3, 2026 - 09:30 (GMT+7)",
        "readTime": "6 min read",
        "sourceName": "Vietnam Investment Review",
        "sourceUrl": "https://vir.com.vn/vietnam-north-south-high-speed-railway-investment-milestone",
        "image": "assets/images/trending/image21.png",
        "imageCaption": "Architectural rendering of the high-speed rail terminal integrating green transit networks.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "34.2K",
        "likes": 1420,
        "tags": ["Infrastructure", "High-Speed Rail", "Economy", "Transit"],
        "content": [
            "Vietnam’s historic North-South high-speed rail corridor represents the largest infrastructure undertaking in the country's modern history, spanning 20 provinces and municipalities.",
            "Designed for passenger speeds of 350 km/h, the modern electric rail network will shrink travel times between Hanoi and Saigon to just five and a half hours, slashing carbon emissions from regional aviation.",
            "Urban planners emphasize that intermediate stations in cities like Vinh, Da Nang, and Nha Trang will catalyze transit-oriented development, decentralizing economic opportunities into secondary urban centers."
        ]
    },
    {
        "id": "trending-14",
        "category": "trending",
        "categoryName": "Trending",
        "title": "Trào lưu quán cà phê lên men và ẩm thực không rác thải tại Đà Nẵng",
        "title_en": "Zero-Waste Fermentation Cafes and Circular Dining Surge in Da Nang",
        "subtitle": "Coastal culinary entrepreneurs are pioneering closed-loop composting, upcycled fruit enzymes, and single-origin kombuchas that inspire eco-conscious youth.",
        "author": "Thu Thao • Heritage Magazine",
        "date": "Sunday, November 1, 2026 - 16:40 (GMT+7)",
        "readTime": "4 min read",
        "sourceName": "Heritage Guide",
        "sourceUrl": "https://heritagevietnamairlines.com/zero-waste-dining-danang-coastal-wave",
        "image": "assets/images/trending/image22.png",
        "imageCaption": "Artisanal kombucha and botanical fermentations at an eco-conscious culinary workshop in Da Nang.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "12.8K",
        "likes": 674,
        "tags": ["Sustainable Living", "Food Culture", "Da Nang", "Zero Waste"],
        "content": [
            "Along the leafy avenues of Da Nang’s An Thuong quarter, a new breed of culinary spaces is proving that gastronomic excellence can coexist seamlessly with zero landfill waste.",
            "From cascara tea brewed using discarded coffee cherry husks to house-fermented tropical vinegar dressings, every ingredient is channeled into a regenerative cycle.",
            "“Our customers aren’t just ordering beverages; they are choosing a gentler, more circular way of interacting with nature,” explains founder Tran Thien An."
        ]
    },
    {
        "id": "trending-15",
        "category": "trending",
        "categoryName": "Trending",
        "title": "UNESCO ghi danh các làng nghề thủ công truyền thống Việt Nam là Di sản sống",
        "title_en": "UNESCO Inscribes Traditional Vietnamese Craft Villages as Living Cultural Heritage",
        "subtitle": "Centuries-old lacquer, ceramics, and silk guilds receive international safeguarding status, elevating artisan youth programs across the country.",
        "author": "Dang Van Nam • Cultural Heritage Review",
        "date": "Friday, October 30, 2026 - 11:00 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "Vietnam Heritage",
        "sourceUrl": "https://vietnamheritage.com.vn/unesco-traditional-craft-villages-vietnam",
        "image": "assets/images/trending/image24.png",
        "imageCaption": "Master craftswoman demonstrating traditional lacquer techniques passed down across generations.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "15.9K",
        "likes": 782,
        "tags": ["UNESCO", "Craftsmanship", "Heritage", "Artisans"],
        "content": [
            "In a milestone recognition celebrating living cultural continuity, UNESCO has formally recognized a network of ancient Vietnamese artisanal villages under the Intangible Cultural Heritage safeguarding framework.",
            "Guilds in Bat Trang pottery, Ha Dong silk, and Chuon Ngo mother-of-pearl inlay are receiving targeted international grants to establish apprentice schools and digital archives.",
            "“This status shifts the perception of traditional crafts from relic museum pieces into dynamic, economically sustainable livelihoods for the next generation,” noted the delegation lead."
        ]
    },
    {
        "id": "trending-16",
        "category": "trending",
        "categoryName": "Trending",
        "title": "Dịch vụ công trực tuyến thế hệ mới: Giải quyết thủ tục hành chính trong tích tắc",
        "title_en": "Smart Public Services: Citizens Complete Administrative Filings in Seconds",
        "subtitle": "Integrated biometric authentication and digital identification platforms have reduced paperwork processing times by over 80% nationwide.",
        "author": "Bao Khanh • Digital Vietnam",
        "date": "Thursday, October 29, 2026 - 08:45 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "VCCI Policy Forum",
        "sourceUrl": "https://vcci.com.vn/smart-public-services-digital-transformation-speed",
        "image": "assets/images/trending/image25.jpg",
        "imageCaption": "A citizen easily completes personal administrative authentication using an e-ID smartphone kiosk.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "19.3K",
        "likes": 615,
        "tags": ["Digital Transformation", "Public Services", "Governance", "Smart City"],
        "content": [
            "The days of carrying bulky folders of notarized photocopies to district municipal offices are rapidly becoming a distant memory for millions of Vietnamese citizens.",
            "Under the national digital identity rollout (VNeID), over 2,500 civic services—from vehicle registration and property transfers to health insurance claims—can now be authenticated and filed digitally in minutes.",
            "Surveys reveal user satisfaction rates climbing to historic highs, with rural residents particularly benefiting from the eradication of unnecessary travel and bureaucratic bottlenecks."
        ]
    },
    {
        "id": "trending-17",
        "category": "trending",
        "categoryName": "Trending",
        "title": "Bùng nổ năng lượng sạch: Việt Nam chạm mốc 20 GW điện gió và điện mặt trời",
        "title_en": "Clean Energy Boom: Vietnam Surpasses 20 GW of Wind and Solar Grid Capacity",
        "subtitle": "Rapid private-sector investment and smart grid upgrades make Vietnam one of the fastest-growing renewable power markets across the Indo-Pacific.",
        "author": "Hoang Duc • Energy Asia",
        "date": "Wednesday, October 28, 2026 - 15:20 (GMT+7)",
        "readTime": "6 min read",
        "sourceName": "Renewable Energy World",
        "sourceUrl": "https://renewableenergyworld.com/vietnam-surpasses-20gw-wind-solar-milestone",
        "image": "assets/images/trending/image26.jpg",
        "imageCaption": "Offshore wind turbine blades rotating against the coastal sky of Binh Thuan province.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "28.1K",
        "likes": 1150,
        "tags": ["Renewable Energy", "Wind Power", "Solar", "Sustainability"],
        "content": [
            "With abundant sun-drenched coastlines and steady seasonal monsoons, Vietnam has officially surpassed 20 gigawatts of installed renewable generation capacity.",
            "The integration of regional 500kV ultra-high-voltage transmission lines has allowed surplus electricity generated from southern solar farms to reliably power industrial clusters in the north.",
            "International energy economists highlight Vietnam as a shining case study in emerging markets successfully decoupling economic expansion from coal reliance."
        ]
    },

    # ================= SOCIETY (3 new articles) =================
    {
        "id": "society-9",
        "category": "society",
        "categoryName": "Society",
        "title": "Chuyến xe y tế lưu động mang kỹ thuật chẩn đoán cao tới xã đảo tiền tiêu",
        "title_en": "Mobile Healthcare Vans Bring High-Tech Diagnostics to Remote Island Communes",
        "subtitle": "Equipped with AI ultrasound, portable digital X-rays, and tele-consultation links, volunteer doctors bring premier hospital care to fishing communities.",
        "author": "Dr. Tran Le Huy & Suc Khoe Doi Song",
        "date": "Monday, November 2, 2026 - 14:00 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "Sức Khỏe & Đời Sống",
        "sourceUrl": "https://suckhoedoisong.vn/chuyen-xe-y-te-luu-dong-kham-chua-benh-xem-xa-dao",
        "image": "assets/images/society/image23.jpg",
        "imageCaption": "Volunteer physicians perform free cardiovascular screenings for island elders on a mobile clinic van.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "11.4K",
        "likes": 530,
        "tags": ["Healthcare", "Community", "Volunteering", "Rural Health"],
        "content": [
            "For coastal fishermen and island elders, traveling to mainland provincial hospitals for specialist diagnostic screenings often requires days of costly ferry transit.",
            "A newly launched fleet of mobile medical vans, staffed by volunteer doctors from central hospitals, has completed 50 outreach expeditions, offering free cardio screenings, eye surgeries, and digital prescriptions.",
            "“Being able to detect chronic conditions early right in the fishing village gives families peace of mind to keep venturing out to sea,” explains volunteer physician Dr. Tran Le Huy."
        ]
    },
    {
        "id": "society-10",
        "category": "society",
        "categoryName": "Society",
        "title": "Cuộc cách mạng Trường học xanh: 1.000 lớp học năng lượng mặt trời và vườn thực nghiệm",
        "title_en": "Green Schools Movement: 1,000 Classrooms Powered by Solar and Experiential Gardens",
        "subtitle": "A grassroots educational initiative turns suburban and provincial school rooftops into renewable energy hubs and living ecology laboratories.",
        "author": "Le Phuong Dung • Giao Duc Thoi Dai",
        "date": "Friday, October 30, 2026 - 09:15 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "Giáo Dục & Thời Đại",
        "sourceUrl": "https://giaoducthoidai.vn/truong-hoc-xanh-mo-hinh-dien-mat-troi-vuon-thuc-nghiem",
        "image": "assets/images/society/image25.jpg",
        "imageCaption": "Schoolchildren tending organic vegetables on a rooftop garden powered by miniature solar panels.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "14.1K",
        "likes": 612,
        "tags": ["Education", "Green Schools", "Solar", "Youth"],
        "content": [
            "In schools participating in the 'Green Campus' movement across Thai Binh, Da Nang, and Can Tho, environmental science is no longer confined to textbook diagrams.",
            "Students actively monitor real-time photovoltaic output on hallway dashboards, measure rainwater harvesting efficiency, and grow organic herbs used in their school lunches.",
            "“When children touch the soil and understand where clean energy comes from, environmental responsibility becomes second nature,” shares headmistress Nguyen Lan Anh."
        ]
    },
    {
        "id": "society-11",
        "category": "society",
        "categoryName": "Society",
        "title": "Phổ cập ngôn ngữ ký hiệu truyền hình: Mở lối tiếp cận thông tin bình đẳng",
        "title_en": "Expanding National Sign Language Broadcasts: Equal Information Access for All",
        "subtitle": "National and regional television stations deploy dedicated sign language interpreters across prime-time news, ensuring no hearing-impaired citizen is left behind.",
        "author": "Kim Ngan • Human Rights & Media",
        "date": "Wednesday, October 28, 2026 - 18:00 (GMT+7)",
        "readTime": "4 min read",
        "sourceName": "VTV News",
        "sourceUrl": "https://vtv.vn/xa-hoi/pho-cap-ngon-ngu-ky-hieu-tren-song-truyen-hinh-quoc-gia",
        "image": "assets/images/society/image26.jpg",
        "imageCaption": "Professional sign language interpreter broadcasting alongside the evening news bulletin.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "10.2K",
        "likes": 489,
        "tags": ["Inclusion", "Sign Language", "Accessibility", "Community"],
        "content": [
            "During critical weather warnings or live parliamentary debates, receiving timely information can be a matter of safety and civic participation.",
            "In a pioneering accessibility drive, national broadcasters have expanded simultaneous sign language interpretation from a single morning program to all prime-time news casts.",
            "Deaf associations nationwide celebrate this transition, noting that universal design in public communication fosters a truly compassionate and equitable society."
        ]
    },

    # ================= HUMAN STORIES (5 new articles) =================
    {
        "id": "human-11",
        "category": "human-stories",
        "categoryName": "Human Stories",
        "title": "Đường dây nóng kết nối sự sống: Những chuyên gia tâm lý tình nguyện trực đêm",
        "title_en": "The Midnight Lifeline: Volunteer Psychologists Guiding Troubled Souls Through the Dark",
        "subtitle": "Operating 24/7 without charging a dime, a network of 60 counselors in Hanoi and Saigon listens to youth navigating deep sorrow, saving hundreds of lives each year.",
        "author": "Mai Huong • Tuoi Tre Cuoi Tuan",
        "date": "Tuesday, November 3, 2026 - 22:30 (GMT+7)",
        "readTime": "6 min read",
        "sourceName": "Tuổi Trẻ Cuối Tuần",
        "sourceUrl": "https://tuoitre.vn/duong-day-nong-tam-ly-truc-dem-cuu-song-nhung-tam-hon",
        "image": "assets/images/human_stories/image16.jpg",
        "imageCaption": "A volunteer counselor gently listens to a late-night call at the crisis counseling center.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "24.5K",
        "likes": 1680,
        "tags": ["Kindness", "Mental Health", "Volunteering", "Empathy"],
        "content": [
            "At 2 a.m. in an unassuming office in District 3, the telephone console lights up with a steady green glow. On the other end of the line is an 18-year-old student weeping silently in despair.",
            "Volunteer counselor Hoang Lan speaks with calm, unhurried warmth: 'I am here with you. Take a slow breath. You are not alone tonight.'",
            "Over the past three years, the free mental health crisis hotline has answered over 35,000 emergency calls, proving that a single empathetic voice in the darkness can restore hope and keep a beating heart alive."
        ]
    },
    {
        "id": "human-12",
        "category": "human-stories",
        "categoryName": "Human Stories",
        "title": "Người mẹ trên đồi gió Kon Tum: 25 năm nuôi dưỡng 32 đứa con mồ côi",
        "title_en": "The Highland Guardian: Raising 32 Orphaned Children in the Hills of Kon Tum",
        "subtitle": "Y Blin turned her modest wooden house into a warm sanctuary, teaching every child self-reliance, compassion, and the pride of their Bahnar heritage.",
        "author": "Nguyen Dinh Quan • Tien Phong",
        "date": "Sunday, November 1, 2026 - 11:20 (GMT+7)",
        "readTime": "6 min read",
        "sourceName": "Tiền Phong",
        "sourceUrl": "https://tienphong.vn/nguoi-me-tren-doi-gio-kon-tum-25-nam-nuoi-32-con-mo-coi",
        "image": "assets/images/human_stories/image21.jpg",
        "imageCaption": "Mother Y Blin preparing an evening meal surrounded by the children she raised as her own.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "19.8K",
        "likes": 1420,
        "tags": ["Motherhood", "Central Highlands", "Kindness", "Inspiration"],
        "content": [
            "High up in the misty valleys of Dak Rve, Mother Y Blin’s wooden stilt house is filled with laughter, the aroma of steamed mountain rice, and the strumming of a ting-ning bamboo zither.",
            "Over a quarter of a century, she has taken in 32 abandoned and orphaned infants from surrounding villages, nursing them through sickness and paying for their education through farm labor.",
            "Today, twelve of her children have graduated from colleges in Da Nang and Tay Nguyen, returning home each weekend to help their younger brothers and sisters study."
        ]
    },
    {
        "id": "human-13",
        "category": "human-stories",
        "categoryName": "Human Stories",
        "title": "Kỹ sư phần mềm khiếm thị thắp lửa lập trình cho hàng trăm bạn trẻ khuyết tật",
        "title_en": "Blind Software Engineer Mentoring Disabled Students into High-Tech Careers",
        "subtitle": "Using audio screen readers and sheer determination, Le Manh Cuong developed open-source accessibility tools and trains visually impaired students to code.",
        "author": "Thanh Truc • VnExpress",
        "date": "Thursday, October 29, 2026 - 15:45 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "VnExpress",
        "sourceUrl": "https://vnexpress.net/ky-su-phan-mem-khiem-thi-day-lap-trinh-cho-hoc-sinh-khuyet-tat",
        "image": "assets/images/human_stories/image24.jpg",
        "imageCaption": "Le Manh Cuong guiding students through code architecture using speech synthesis terminals.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "16.4K",
        "likes": 980,
        "tags": ["Determination", "Technology", "Inclusion", "Coding"],
        "content": [
            "Having lost his sight at age ten due to retinal degeneration, Le Manh Cuong refused to accept that blindness meant living on society's sidelines.",
            "He memorized keyboard positions, mastered synthesized screen readers operating at 400 words per minute, and graduated at the top of his computer science university cohort.",
            "Now a senior software architect, Cuong hosts free weekend coding workshops for visually impaired youths: 'Sight is a window, but vision is inside the mind. Code allows us to build any world we dream of.'"
        ]
    },
    {
        "id": "human-14",
        "category": "human-stories",
        "categoryName": "Human Stories",
        "title": "Đội thuyền cứu hộ của những ngư dân miền Trung: Băng qua dòng lũ cứu xóm làng",
        "title_en": "The Fishermen’s Flotilla: Braving Raging Floodwaters to Rescue Stranded Neighbors",
        "subtitle": "When record flash floods submerged low-lying villages in Quang Binh, a fleet of 15 wooden fishing boats navigated treacherous currents to evacuate over 400 elders and children.",
        "author": "Hoang Phuc • Nhan Dan",
        "date": "Tuesday, October 27, 2026 - 17:10 (GMT+7)",
        "readTime": "6 min read",
        "sourceName": "Nhân Dân",
        "sourceUrl": "https://nhandan.vn/doi-thuyen-ngu-dan-quang-binh-xuyen-dem-cuu-nguoi-trong-lu-du",
        "image": "assets/images/human_stories/image25.jpg",
        "imageCaption": "Brave fishermen steering their sturdy wooden boats through swirling floodwaters to deliver supplies.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "22.3K",
        "likes": 1540,
        "tags": ["Courage", "Solidarity", "Central Vietnam", "Rescue"],
        "content": [
            "When flood sirens wailed through Le Thuy district and river levels surged past roof gutters in the dead of night, veteran boat captain Nguyen Van Hung didn't hesitate.",
            "He rallied his fellow fishermen, hitched their ocean-going wooden vessels onto tractors, and drove inland to launch straight into the raging floodplains.",
            "For 48 continuous hours without sleep, the volunteer fishermen navigated submerged power lines and submerged debris, plucking stranded families from attic rafters and delivering emergency rations."
        ]
    },
    {
        "id": "human-15",
        "category": "human-stories",
        "categoryName": "Human Stories",
        "title": "Lớp học chữ miễn phí dưới ánh đèn đường: 18 năm gieo hy vọng cho trẻ em mưu sinh",
        "title_en": "Night School under the Streetlights: 18 Years Sowing Literacy for Working Children",
        "subtitle": "Retired teacher Nguyen Thi Cam has dedicated nearly two decades to teaching math and reading to lottery ticket sellers, shoe shiners, and scrap collectors in District 8.",
        "author": "Bich Ngoc • Phu Nu TP.HCM",
        "date": "Sunday, October 25, 2026 - 20:00 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "Phụ Nữ Online",
        "sourceUrl": "https://phunuonline.com.vn/lop-hoc-chu-mien-phi-duoi-anh-den-duong-sai-gon",
        "image": "assets/images/human_stories/image26.jpg",
        "imageCaption": "Teacher Cam patiently guiding a young boy through his Vietnamese handwriting practice.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "17.7K",
        "likes": 1210,
        "tags": ["Education", "Kindness", "Children", "Saigon Stories"],
        "content": [
            "Every evening at 6:30 p.m., under the fluorescent glow of a community courtyard in Saigon's District 8, twenty children with dusty clothes and worn flip-flops gather around small wooden desks.",
            "They have spent the day selling lottery tickets or collecting discarded cardboard, but here, they are simply students eager to solve math puzzles and recite poetry.",
            "“Knowing how to read means nobody can cheat them when they grow up,” says 73-year-old teacher Cam. “A word learned is a doorway to dignity opened.”"
        ]
    },

    # ================= MIND & SOUL (1 authentic + 5 new) =================
    {
        "id": "mind-9",
        "category": "mind-soul",
        "categoryName": "Mind & Soul",
        "title": "Michelin-honored Saigon eatery serves banh cuon with a touch of tradition",
        "title_en": "Michelin-honored Saigon eatery serves banh cuon with a touch of tradition",
        "subtitle": "Founded in 1961, Tay Ho banh cuon restaurant in Ho Chi Minh City has earned Michelin's Bib Gourmand for its paper-thin steamed rice rolls and enduring family passion.",
        "author": "Ha Nguyen • VietnamNet",
        "date": "Monday, November 2, 2026 - 12:30 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "VietnamNet",
        "sourceUrl": "https://vietnamnet.vn/en/michelin-honored-saigon-eatery-serves-banh-cuon-with-a-touch-of-tradition-2566799.html",
        "image": "assets/images/mind_&_soul/image20.png",
        "imageCaption": "Freshly steamed banh cuon served with fragrant shallots and savory pork sausage at Tay Ho eatery. (Photo: VietnamNet)",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "15.3K",
        "likes": 780,
        "tags": ["Culinary Soul", "Michelin Guide", "Banh Cuon", "Tradition"],
        "content": [
            "Founded in 1961, Tay Ho banh cuon restaurant in Ho Chi Minh City has earned Michelin's Bib Gourmand for its paper-thin steamed rice rolls and enduring family devotion.",
            "On a weekend morning, 66-year-old Lan traveled from District 7 to Tay Ho banh cuon on Dinh Tien Hoang Street in District 1. She has been a loyal patron since the 1980s, recalling fond memories of eating here with her parents in her youth.",
            "The owner, dressed in an elegant traditional ao dai, warmly greets customers who arrive in steady streams. The batter is prepared from aged rice ground with stone mills, resulting in translucent, silky rolls wrapped around savory minced pork and wood-ear mushrooms.",
            "“In a fast-changing modern city, stepping into this eatery feels like returning to the quiet grace and familiar aromas of home,” observes a longtime food critic."
        ]
    },
    {
        "id": "mind-10",
        "category": "mind-soul",
        "categoryName": "Mind & Soul",
        "title": "Tắm rừng Ba Vì: Nghệ thuật Shinrin-yoku chữa lành căng thẳng giữa thiên nhiên",
        "title_en": "Forest Bathing in Ba Vi: The Ancient Japanese Art of Shinrin-yoku",
        "subtitle": "Walking slowly under ancient pine canopies, breathing in plant phytoncides, and tuning out smartphone alerts restores autonomic nervous balance and inner serenity.",
        "author": "Thao Trang • Mindful Living",
        "date": "Saturday, October 31, 2026 - 08:30 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "Positive Living",
        "sourceUrl": "https://positiveliving.vn/forest-bathing-shinrin-yoku-bavi-mountain",
        "image": "assets/images/mind_&_soul/image11.jpg",
        "imageCaption": "Morning mist filtering through the pine groves of Ba Vi National Park.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "11.9K",
        "likes": 560,
        "tags": ["Mindfulness", "Forest Bathing", "Mental Health", "Nature"],
        "content": [
            "Just an hour's drive from Hanoi's bustling ring roads lies the cool, emerald expanse of Ba Vi National Park, where stressed urbanites are embracing forest bathing (shinrin-yoku).",
            "Unlike strenuous trekking, forest bathing invites visitors to slow down completely: feeling the rough texture of tree bark, inhaling organic aerosols emitted by pines, and listening to mountain streams.",
            "Clinical studies confirm that two hours spent immersing one's senses in natural woodland significantly decreases cortisol levels, boosts natural killer immune cells, and restores mental clarity."
        ]
    },
    {
        "id": "mind-11",
        "category": "mind-soul",
        "categoryName": "Mind & Soul",
        "title": "Viết nhật ký trị liệu: Phương pháp đơn giản giúp tháo gỡ bế tắc tâm trí",
        "title_en": "Therapeutic Journaling: How Putting Pen to Paper Unravels Mental Overload",
        "subtitle": "Cognitive researchers explain why 15 minutes of uncensored morning journaling calms the amygdala, reduces depressive ruminations, and clarifies personal values.",
        "author": "Vu Thuy Linh • Psychology Today VN",
        "date": "Friday, October 30, 2026 - 19:40 (GMT+7)",
        "readTime": "4 min read",
        "sourceName": "Mental Wellness Journal",
        "sourceUrl": "https://wellnessjournal.vn/therapeutic-journaling-rewiring-mental-overload",
        "image": "assets/images/mind_&_soul/image12.jpg",
        "imageCaption": "A quiet morning desk with a fountain pen and journal bathed in soft natural light.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "13.4K",
        "likes": 645,
        "tags": ["Journaling", "Self Care", "Psychology", "Emotional Balance"],
        "content": [
            "In an era dominated by hyperactive digital notification streams, the tactile act of dragging a fountain pen across smooth paper provides a sanctuary for the mind.",
            "Therapists advocate for 'stream-of-consciousness' journaling, where worries, raw emotions, and gratitude are externalized without judgment.",
            "“When thoughts remain locked in our heads, they loop endlessly,” explains clinical psychologist Vu Thuy Linh. “Once they are pinned onto paper, they lose their terrifying grip.”"
        ]
    },
    {
        "id": "mind-12",
        "category": "mind-soul",
        "categoryName": "Mind & Soul",
        "title": "Thiền trà Shan Tuyết trên đỉnh Chiêu Lầu Thi: Thưởng thức sự tĩnh lặng tuyệt đối",
        "title_en": "Shan Tuyet Tea Meditation: Sipping Silence on Chieu Lau Thi Summit",
        "subtitle": "Harvested from 300-year-old tea trees shrouded in eternal mist, each cup of ancient white tea offers an anchor of pure presence and rustic harmony.",
        "author": "Tra Su Nguyen Viet • Heritage Tea",
        "date": "Wednesday, October 28, 2026 - 10:15 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "Vietnam Tea Culture",
        "sourceUrl": "https://vietnamteaculture.vn/shan-tuyet-tea-meditation-chieu-lau-thi",
        "image": "assets/images/mind_&_soul/image13.jpg",
        "imageCaption": "Tea master carefully pouring mountain spring water over ancient Shan Tuyet leaves.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "14.7K",
        "likes": 732,
        "tags": ["Tea Meditation", "Shan Tuyet", "Ha Giang", "Inner Peace"],
        "content": [
            "At an altitude of over 2,400 meters on Ha Giang's Chieu Lau Thi peak, century-old Shan Tuyet tea trees grow gnarled and moss-covered amidst billowing sea of clouds.",
            "Local Dao tea artisans harvest only the silver-tipped buds at dawn, sun-drying them naturally to retain their delicate honey-sweet vegetal notes.",
            "Practicing tea meditation with Shan Tuyet teaches the soul patience: waiting for the water temperature to settle, observing the leaves unfold, and savoring the quiet sweetness that lingers long after each sip."
        ]
    },
    {
        "id": "mind-13",
        "category": "mind-soul",
        "categoryName": "Mind & Soul",
        "title": "Vượt qua kiệt sức sáng tạo: Nghệ thuật của những khoảng trống vô vi",
        "title_en": "Overcoming Creative Burnout: Why Emptiness and Boredom Fuel Breakthroughs",
        "subtitle": "Constant productivity destroys imagination. Neuroscientists advocate for deliberate daydreaming, digital sabbaths, and unhurried walks to reignite creative sparks.",
        "author": "Dang Quynh Anh • The Creative Mind",
        "date": "Monday, October 26, 2026 - 16:30 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "Creative Review",
        "sourceUrl": "https://creativereview.vn/overcoming-burnout-art-of-empty-space",
        "image": "assets/images/mind_&_soul/image15.jpg",
        "imageCaption": "A solitary walk along a quiet lakeside, allowing the subconscious mind to rest.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "18.2K",
        "likes": 890,
        "tags": ["Creativity", "Burnout", "Wellness", "Work Life"],
        "content": [
            "The cult of relentless hustle often leads creators straight into emotional exhaustion, where the blank canvas feels like a hostile interrogation room.",
            "Neuroscientists point out that the human brain's Default Mode Network—responsible for novel problem-solving and synthesis—only activates when we are resting or letting our minds wander without an agenda.",
            "Allowing oneself a day of complete non-doing, strolling without headphones, or gazing out at rain is not wasted time; it is the essential tilling of inner fertile soil."
        ]
    },
    {
        "id": "mind-14",
        "category": "mind-soul",
        "categoryName": "Mind & Soul",
        "title": "Âm vang đàn đá: Giai điệu trầm hùng ngàn năm kết nối tâm thức",
        "title_en": "The Acoustic Resonance of Ancient Lithophones: Grounding the Modern Soul",
        "subtitle": "Crafted from prehistoric volcanic stones, the primordial reverberations of Vietnam’s lithophones are finding new purpose in sound therapy and acoustic meditation.",
        "author": "Nhac si Tran Manh Dung • Traditional Music Studies",
        "date": "Saturday, October 24, 2026 - 14:00 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "Musical Heritage",
        "sourceUrl": "https://musicalheritage.vn/ancient-lithophone-dan-da-sound-healing",
        "image": "assets/images/mind_&_soul/image16.jpg",
        "imageCaption": "Ancient chime stones (dan da) producing pure resonant frequencies during an acoustic concert.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "12.5K",
        "likes": 610,
        "tags": ["Sound Healing", "Lithophone", "Music Therapy", "Culture"],
        "content": [
            "When striking the ancient basalt slabs of the Vietnamese lithophone (đàn đá), the resulting chime does not merely enter the ear—it vibrates deeply through the listener’s chest.",
            "Dating back over 3,000 years in the Central Highlands, these prehistoric stone instruments produce pure, non-harmonic overtone spectrums that acoustic therapists liken to Tibetan singing bowls.",
            "Modern sound bath practitioners are reintroducing lithophone resonance sessions, noting how the ancient earthy timbre grounds racing nervous systems and induces profound meditative states."
        ]
    },

    # ================= IN-DEPTH (1 authentic + 8 new) =================
    {
        "id": "indepth-9",
        "category": "in-depth",
        "categoryName": "In-Depth",
        "title": "Inside Hanoi tycoon’s 100-year-old villa in the Old Quarter",
        "title_en": "Inside Hanoi tycoon’s 100-year-old villa in the Old Quarter",
        "subtitle": "A century-old, 800-square-meter villa on Hang Be Street in Hanoi’s Hoan Kiem Ward has been preserved through four generations, maintaining East-meets-West architectural grandeur.",
        "author": "Nga Thanh • VnExpress",
        "date": "Monday, November 2, 2026 - 08:30 (GMT+7)",
        "readTime": "7 min read",
        "sourceName": "VnExpress International",
        "sourceUrl": "https://e.vnexpress.net/photo/trend/inside-hanoi-tycoons-100-year-old-villa-in-the-old-quarter-5140151.html",
        "image": "assets/images/society/image31.jpg",
        "imageCaption": "The stately 100-year-old courtyard and ironwood balustrades of the historic Hang Be villa. (Photo: VnExpress)",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "26.4K",
        "likes": 1280,
        "tags": ["Architecture", "Heritage", "Hanoi Old Quarter", "History"],
        "content": [
            "A century-old, 800-square-meter villa on Hang Be Street in Hanoi’s Hoan Kiem Ward has been preserved through four generations of the Truong Trong Vong merchant family.",
            "Built in 1926 by Vong, who operated hundreds of rickshaws for rent in colonial Hanoi, the villa was constructed in the architectural layout of the Chinese character 'Khẩu' (mouth), featuring an airy central courtyard surrounded by interconnected living quarters.",
            "Architectural researchers from Kyoto University's HANOIDB project highlight the villa’s French cast-iron balustrades, carved limestone pillars, and ornate ironwood staircases that reflect a masterclass in early 20th-century Sino-French fusion.",
            "Today, looked after by Vong’s 71-year-old granddaughter Le Thanh Thuy, the residence preserves its original brass beds and antique daybeds, remaining an invaluable living museum of Hanoi’s golden merchant era."
        ]
    },
    {
        "id": "indepth-10",
        "category": "in-depth",
        "categoryName": "In-Depth",
        "title": "Hành trình tìm vết vi nhựa: Báo cáo khảo sát thực địa trên lưu vực sông Hồng và sông Cửu Long",
        "title_en": "Tracking Microplastics: Multi-Year Field Survey in the Red River and Mekong Deltas",
        "subtitle": "An intensive environmental investigation examines microscopic synthetic polymer concentrations in river sediments, agricultural soils, and marine food chains.",
        "author": "Environmental Research Group • VNU",
        "date": "Sunday, November 1, 2026 - 09:00 (GMT+7)",
        "readTime": "8 min read",
        "sourceName": "Vietnam Journal of Environmental Sciences",
        "sourceUrl": "https://vnu.edu.vn/environmental-science/tracking-microplastics-river-deltas",
        "image": "assets/images/in-dept/image10.jpg",
        "imageCaption": "Marine biologists sampling water column particulates using fine-mesh plankton nets.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "19.5K",
        "likes": 840,
        "tags": ["Environment", "Ecology", "Microplastics", "Water Security"],
        "content": [
            "Over three years of exhaustive water and sediment testing across 40 river estuary stations, environmental toxicologists have assembled the clearest picture yet of synthetic fiber pollution.",
            "Samples reveal that single-use plastic wrappings and synthetic textile laundry discharge make up over 70% of detected microplastic particles.",
            "The findings emphasize an urgent need for closed-loop industrial water filtration at industrial parks and sweeping national bans on non-biodegradable packaging."
        ]
    },
    {
        "id": "indepth-11",
        "category": "in-depth",
        "categoryName": "In-Depth",
        "title": "Lụa Vạn Phúc: Bức tranh ngàn năm dệt gấm thêu hoa trước áp lực công nghiệp hóa",
        "title_en": "Van Phuc Silk: The Fragile Artistry of Centuries-Old Looms in an Industrial Era",
        "subtitle": "Generations of artisan weavers in Ha Dong share the struggle to keep natural mulberry silk and intricate cloud jacquard patterns alive amid fast fashion commodification.",
        "author": "Doan Huong Giang • Cultural Anthropology",
        "date": "Friday, October 30, 2026 - 16:00 (GMT+7)",
        "readTime": "7 min read",
        "sourceName": "Craft & Culture Review",
        "sourceUrl": "https://culturecraft.vn/van-phuc-silk-artisan-weaving-preservation",
        "image": "assets/images/in-dept/image11.jpg",
        "imageCaption": "Shuttle flying across a wooden jacquard loom weaving traditional Van silk patterns.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "17.3K",
        "likes": 910,
        "tags": ["Van Phuc", "Silk Weaving", "Artisanship", "Craft Villages"],
        "content": [
            "Along the Nhue River in Ha Dong, the rhythmic clack-clack of wooden flying shuttles has echoed for over a thousand years, producing the famous Vân silk that once clothed royal courts.",
            "Unlike synthetic polyester imitations, true Van Phuc silk requires natural mulberry silkworm thread and hand-punched jacquard cards that weave complex cloud and dragon motifs directly into the textile grain.",
            "Younger generations of master weavers are pioneering luxury bespoke fashion collections, ensuring the ancient craft finds appreciative collectors worldwide."
        ]
    },
    {
        "id": "indepth-12",
        "category": "in-depth",
        "categoryName": "In-Depth",
        "title": "Chuyển dịch trong mô hình chăm sóc sức khỏe tâm thần cộng đồng tại Việt Nam",
        "title_en": "The Paradigm Shift in Community Mental Health Infrastructure across Vietnam",
        "subtitle": "Moving away from isolated institutional care, pioneering medical centers and university clinics are adopting biopsychosocial support networks embedded in local neighborhoods.",
        "author": "Dr. Vo Nguyen Giap • Clinical Psychiatry Forum",
        "date": "Thursday, October 29, 2026 - 11:30 (GMT+7)",
        "readTime": "8 min read",
        "sourceName": "Medical Journal of Vietnam",
        "sourceUrl": "https://medjournal.vn/community-mental-health-reform-vietnam",
        "image": "assets/images/in-dept/image12.jpg",
        "imageCaption": "Community psychology counseling session in a relaxed, stigma-free communal clinic setting.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "21.1K",
        "likes": 995,
        "tags": ["Mental Health", "Public Health", "Psychology", "Social Care"],
        "content": [
            "Vietnam’s healthcare system is undertaking a historic transition in psychiatric care, moving resources from centralized psychiatric hospitals into neighborhood community clinics.",
            "The model integrates family support groups, school counselors, and primary care physicians trained in identifying early anxiety and depressive disorders.",
            "“Destigmatizing mental wellness and making care accessible five minutes from someone’s home changes everything,” emphasizes health policy specialists."
        ]
    },
    {
        "id": "indepth-13",
        "category": "in-depth",
        "categoryName": "In-Depth",
        "title": "Bảo tồn kiến trúc gạch nung Chăm Pa: Giải mã chất kết dính ngàn năm tại Mỹ Sơn",
        "title_en": "Conserving Cham Brick Architecture: Unlocking the Ancient Mortar Secrets of My Son",
        "subtitle": "International archaeologists and Vietnamese heritage scientists analyze the resin-based botanical adhesives that have kept My Son's monolithic towers standing for twelve centuries.",
        "author": "Heritage Architecture Taskforce • UNESCO / VNU",
        "date": "Tuesday, October 27, 2026 - 13:45 (GMT+7)",
        "readTime": "7 min read",
        "sourceName": "Archaeological Review",
        "sourceUrl": "https://archaeology.vn/my-son-cham-brick-masonry-resin-mortar",
        "image": "assets/images/in-dept/image13.jpg",
        "imageCaption": "The ancient brick towers of My Son Sanctuary nestled in the forested valley of Quang Nam.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "23.8K",
        "likes": 1140,
        "tags": ["My Son", "Cham Culture", "Archaeology", "Heritage Preservation"],
        "content": [
            "The terracotta brick towers of My Son Sanctuary have perplexed modern civil engineers: the bricks fit together so seamlessly that not even a knife blade can slip between the joints.",
            "Advanced chemical chromatography now reveals that master Cham masons utilized heated Dipterocarpus tree resin (dầu rái) mixed with clay slurry as a botanical binder that polymerized into rock-hard cohesion.",
            "This scientific revelation allows restoration experts to repair crumbling temple facades using authentic botanical formulas, ensuring historical integrity is preserved."
        ]
    },
    {
        "id": "indepth-14",
        "category": "in-depth",
        "categoryName": "In-Depth",
        "title": "Bản đồ phân bổ kinh tế - xã hội khi các tuyến cao tốc và đường sắt liên vùng vận hành",
        "title_en": "The Socioeconomic Matrix of High-Speed Interprovincial Transportation Corridors",
        "subtitle": "Economists project the cascading multiplier effect of regional expressways, decentralized manufacturing hubs, and labor mobility across the Central Highlands and North Central coast.",
        "author": "Tran Quoc Toan • Institute of Regional Economics",
        "date": "Sunday, October 25, 2026 - 14:15 (GMT+7)",
        "readTime": "7 min read",
        "sourceName": "Economic & Policy Analysis",
        "sourceUrl": "https://ire.gov.vn/socioeconomic-impact-expressway-rail-corridors",
        "image": "assets/images/in-dept/image14.jpg",
        "imageCaption": "Modern multi-tier expressway interchange bridging agricultural valleys with seaport hubs.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "18.6K",
        "likes": 875,
        "tags": ["Economics", "Regional Development", "Highways", "Logistics"],
        "content": [
            "The rapid completion of east-west and north-south expressway corridors is creating profound economic shifts in formerly isolated inland districts.",
            "Hauling agricultural produce from Dak Lak to coastal ports now takes hours rather than days, drastically reducing cold-chain spoilage and raising farmgate revenues.",
            "Economists stress that complementary investments in local technical colleges and industrial zoning are vital to ensuring local populations benefit directly from transit proximity."
        ]
    },
    {
        "id": "indepth-15",
        "category": "in-depth",
        "categoryName": "In-Depth",
        "title": "Đạo đức trí tuệ nhân tạo trong y khoa: Ranh giới giữa thuật toán và lòng trắc ẩn",
        "title_en": "Ethics in Clinical AI: Balancing Diagnostic Precision with the Human Touch",
        "subtitle": "As hospital wards adopt neural networks to read CT scans and predict oncological prognoses, medical ethicists establish frameworks to keep doctor-patient empathy at the center.",
        "author": "Prof. Le Minh Tri • Bioethics Council",
        "date": "Friday, October 23, 2026 - 10:00 (GMT+7)",
        "readTime": "8 min read",
        "sourceName": "Bioethics & Health Policy",
        "sourceUrl": "https://bioethics.org.vn/clinical-ai-diagnostic-precision-human-empathy",
        "image": "assets/images/in-dept/image15.jpg",
        "imageCaption": "A radiologist reviewing high-resolution chest scans assisted by neural network lesion heatmaps.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "25.2K",
        "likes": 1080,
        "tags": ["AI Ethics", "Healthcare", "Bioethics", "Medical Science"],
        "content": [
            "Deep neural networks can now detect subtle pulmonary nodules or retinal micro-aneurysms faster than the human eye. Yet, delivering a difficult diagnosis remains a deeply human act.",
            "Bioethicists argue that algorithms must remain decision-support tools rather than autonomous arbiters, with clear liability guidelines and algorithmic transparency.",
            "“An AI can calculate survival odds, but it cannot hold a patient's trembling hand or offer comfort,” explains Professor Le Minh Tri. “Empathy is the irreplaceable core of medicine.”"
        ]
    },
    {
        "id": "indepth-16",
        "category": "in-depth",
        "categoryName": "In-Depth",
        "title": "Ngân hàng hạt giống bản địa: Hành trình bảo vệ nguồn gen lúa quý Việt Nam",
        "title_en": "Seed Sovereignty: Preserving Vietnam's Indigenous Heirloom Rice Varieties",
        "subtitle": "Deep in the northern valleys, an independent coalition of agronomists and ethnic farmers is cataloging over 300 climate-resilient indigenous seed strains before they disappear.",
        "author": "Nguyen Hoang Lam • Agricultural Ecology",
        "date": "Wednesday, October 21, 2026 - 16:20 (GMT+7)",
        "readTime": "7 min read",
        "sourceName": "Agronomy Vietnam",
        "sourceUrl": "https://agronomy.vn/seed-sovereignty-indigenous-rice-preservation",
        "image": "assets/images/in-dept/image16.jpg",
        "imageCaption": "Agronomist inspecting golden heirloom paddy panicles in a highland conservation trial plot.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "16.8K",
        "likes": 790,
        "tags": ["Agriculture", "Biodiversity", "Food Security", "Heirloom Seeds"],
        "content": [
            "As monoculture hybrid rice strains dominate commercial agriculture, ancient heirloom varieties—naturally resistant to drought, saline intrusion, and local pests—face extinction.",
            "An underground community seed bank established across Lao Cai, Son La, and An Giang has successfully preserved 340 heirloom landraces, including rare purple glutinous and flood-tolerant floating rice.",
            "In an era of accelerating climate volatility, these genetic repositories represent the nation's most valuable agricultural insurance policy."
        ]
    },
    {
        "id": "indepth-17",
        "category": "in-depth",
        "categoryName": "In-Depth",
        "title": "Hệ sinh thái tranh dân gian Đông Hồ trong dòng chảy thị giác hiện đại",
        "title_en": "The Living Visual Ecology of Dong Ho Folk Woodcuts in Contemporary Design",
        "subtitle": "How young Vietnamese typography and graphic designers are reimagining traditional woodcut symbolism, scallop-shell diep paper, and mineral pigments for modern digital illustration.",
        "author": "Pham Thu Van • Design Studies",
        "date": "Monday, October 19, 2026 - 15:00 (GMT+7)",
        "readTime": "6 min read",
        "sourceName": "Arts & Culture Review",
        "sourceUrl": "https://artsandculture.vn/dong-ho-folk-woodcuts-contemporary-visual-design",
        "image": "assets/images/in-dept/image17.jpg",
        "imageCaption": "Traditional hand-carved woodblocks alongside modern digital brand identity sketches.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "19.0K",
        "likes": 860,
        "tags": ["Dong Ho Folk Art", "Graphic Design", "Woodblock Printing", "Vietnamese Identity"],
        "content": [
            "For decades, the famous folk prints of Dong Ho village in Bac Ninh—printed on natural scallop-shell paper with indigo and vermilion earth pigments—were seen primarily as Tet festival decorations.",
            "Today, a new generation of visual communicators and UI designers is decoding the expressive geometry, visual metaphors, and lyrical charm of folk prints to create distinctively Vietnamese graphic identities.",
            "“Dong Ho art proves that minimalism and warmth can coexist,” notes graphic designer Pham Thu Van. “Our cultural roots are a limitless wellspring of contemporary design inspiration.”"
        ]
    }
]

print(f"Prepared {len(new_articles)} new articles!")

# Combine existing articles + new articles
all_articles = existing_articles + new_articles
print(f"Total articles after merge: {len(all_articles)}")

# Verify counts per category
cat_dist = {}
for a in all_articles:
    c = a['category']
    cat_dist[c] = cat_dist.get(c, 0) + 1

print("\nFinal category distribution:")
for cat, cnt in sorted(cat_dist.items()):
    print(f"  {cat}: {cnt}")

# Write back to js/data.js
# Format as pretty JSON with 2 spaces indent
formatted_json = json.dumps(all_articles, ensure_ascii=False, indent=2)

new_content = original_code[:start_idx] + formatted_json + original_code[end_idx:]

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully written to js/data.js!")
