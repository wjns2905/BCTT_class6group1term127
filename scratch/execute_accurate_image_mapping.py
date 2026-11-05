import sys, json, re, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

# The exact 1-to-1 mapping of Article ID -> (Image Path, Title_VI, Title_EN, Subtitle_VI, Subtitle_EN)
# Ensuring docx articles have their true authentic docx photos and titles!
EXACT_MAPPING = {
    # ================= TRENDING =================
    'trending-1': {
        'image': 'assets/images/trending/lawmakers_lead.jpg',
        'title': 'Đại biểu Quốc hội đề xuất các giải pháp đột phá phát triển kinh tế vùng miền núi, biên giới',
        'title_en': 'Lawmakers propose measures to boost development in mountainous, border regions',
        'sourceUrl': 'https://en.nhandan.vn/lawmakers-propose-measures-to-boost-development-in-mountainous-border-regions-post168532.html',
        'sourceName': 'Báo Nhân Dân'
    },
    'trending-2': {
        'image': 'assets/images/trending/image2.jpg',
        'title': 'Lòng tốt của người lạ: Năm 1989 tôi đánh rơi chiếc ví có 1.000 USD và hành trình tìm lại khó tin',
        'title_en': 'The Kindness of Strangers: In 1989 I lost a wallet with $1,000 in it. A couple went to incredible lengths to return it',
        'sourceUrl': 'https://www.theguardian.com/lifeandstyle/2026/nov/02/kindness-of-strangers-lost-wallet-cash-returned-couple',
        'sourceName': 'The Guardian'
    },
    'trending-3': {
        'image': 'assets/images/trending/image3.jpg',
        'title': 'Khởi nghiệp tuổi 60: Ở tuổi 26 mơ về Porsche, tuổi 68 tự tay chế tạo chiếc 904FF',
        'title_en': 'A new start after 60: At 26, I saw my dream Porsche. At 68, I built one from scratch',
        'sourceUrl': 'https://www.theguardian.com/lifeandstyle/2026/nov/02/a-new-start-after-60-at-26-i-saw-my-dream-porsche-at-68-i-built-one-from-scratch',
        'sourceName': 'The Guardian'
    },
    'trending-4': {
        'image': 'assets/images/trending/image8.jpg',
        'title': 'Gánh mưu sinh: Hồn cốt bình dị trên từng góc phố cổ Hội An',
        'title_en': 'Street Vendors with Shoulder Pole: A Timeless Hallmark of Hoi An Ancient Town',
        'sourceUrl': 'https://e.vnexpress.net/news/travel/places/street-vendors-with-shoulder-pole-a-familiar-sight-in-vietnam-s-old-town-4099491.html',
        'sourceName': 'VnExpress International'
    },
    'trending-5': {
        'image': 'assets/images/trending/image1.jpg',
        'title': 'Chiến dịch 500 ngày đêm ADN: Trả lại danh tính cho gần 800 hài cốt liệt sĩ',
        'title_en': '500-day-and-night campaign: DNA testing results returned for nearly 800 fallen soldiers',
        'sourceUrl': 'https://en.nhandan.vn/500-day-and-night-campaign-dna-testing-results-returned-for-nearly-800-samples-of-martyrs-remains-post167905.html',
        'sourceName': 'Báo Nhân Dân'
    },
    'trending-6': {
        'image': 'assets/images/trending/image15.jpg',
        'title': 'Vương quốc Anh tăng mức chứng minh tài chính đối với du học sinh',
        'title_en': 'UK to hike proof-of-funds requirement for international students',
        'sourceUrl': 'https://e.vnexpress.net/news/news/education/uk-to-hike-proof-of-funds-requirement-for-international-students-from-nov-30-5139725.html',
        'sourceName': 'VnExpress International'
    },
    'trending-7': {
        'image': 'assets/images/trending/ai_newsroom_journalism.jpg',
        'title': 'Trí tuệ nhân tạo trong báo chí hiện đại: Tăng tốc quy trình nhưng giữ trọn đạo đức nhân văn',
        'title_en': 'AI in modern journalism: Enhancing reporting speed while preserving human empathy and ethics'
    },
    'trending-8': {
        'image': 'assets/images/trending/vintage_film_camera.jpg',
        'title': 'Bùng nổ trào lưu săn máy ảnh film cổ: Gen Z tìm lại vẻ đẹp hoài niệm của nhiếp ảnh tương tự',
        'title_en': 'Resurgence of Vintage Film Cameras: Gen Z Embracing Analogue Nostalgia'
    },
    'trending-9': {
        'image': 'assets/images/trending/robusta_coffee_vietnam.jpg',
        'title': 'Cà phê Robusta Việt Nam bùng nổ thế giới: Từ hạt rẻ tiền đến làn sóng đặc sản triệu đô',
        'title_en': 'Vietnamese Robusta Coffee Goes Global: From Cheap Commodity to Specialty Craze'
    },
    'trending-10': {
        'image': 'assets/images/trending/rooftop_pocket_forest.jpg',
        'title': 'Trào lưu 'rừng bỏ túi' trên mái cao ốc: Đô thị hóa xanh giữa những khối bê tông chọc trời',
        'title_en': 'Urban Pocket Forests on High-Rise Rooftops: Rewilding Concrete Jungles'
    },
    'trending-11': {
        'image': 'assets/images/trending/art_toy_blind_box.jpg',
        'title': 'Hiện tượng 'hộp mù' Art Toy và trào lưu sưu tầm gây bão: Giới trẻ chi hàng chục triệu săn lùng',
        'title_en': 'The Blind Box Art Toy Phenomenon: Young Consumers Spending Millions on Viral Collectibles'
    },
    'trending-12': {
        'image': 'assets/images/trending/heritage_train_travel.jpg',
        'title': 'Làn sóng du lịch 'chữa lành' bằng tàu hỏa Bắc - Nam: Ngắm trọn vẻ đẹp di sản dải đất hình chữ S',
        'title_en': 'Healing Journey by Heritage Train: Rediscovering Vietnam’s Scenic Splendors on Slow Rails'
    },
    'trending-13': {
        'image': 'assets/images/trending/military_history_museum.jpg',
        'title': 'Bảo tàng Lịch sử Quân sự Việt Nam mới: Hiện tượng văn hóa thu hút hàng vạn bạn trẻ mỗi ngày',
        'title_en': 'New Vietnam Military History Museum: Cultural Phenomenon Drawing Thousands Daily'
    },
    'trending-14': {
        'image': 'assets/images/trending/vietnamese_heritage_attire.jpg',
        'title': 'Trào lưu cổ phục Việt bùng nổ trên mạng xã hội: Giới trẻ tự hào diện Nhật Bình, áo ngũ thân',
        'title_en': 'Traditional Vietnamese Attire Goes Viral: Youth Reviving Historic Nhat Binh Garments'
    },
    'trending-15': {
        'image': 'assets/images/trending/electric_vehicle_green.jpg',
        'title': 'Xe điện 'Made in Vietnam' vươn ra biển lớn: Dấu ấn công nghệ xanh trên thị trường quốc tế',
        'title_en': 'Made-in-Vietnam Electric Vehicles Expanding Globally: Sustainable Mobility Innovation'
    },
    'trending-16': {
        'image': 'assets/images/trending/hanoi_street_food.jpg',
        'title': 'Cơn sốt ẩm thực đường phố Hà Nội: Phở cuốn và bánh tôm hồ Tây chinh phục giới sành ăn quốc tế',
        'title_en': 'Hanoi Street Food Renaissance: Pho Cuon and West Lake Shrimp Cakes Captivate Global Foodies'
    },
    'trending-17': {
        'image': 'assets/images/trending/podcast_healing_audio.jpg',
        'title': 'Podcast và xu hướng 'nghe chữa lành': Giới trẻ đô thị tìm lại sự an yên giữa bộn bề công nghệ',
        'title_en': 'Therapeutic Podcasting Trend: Urban Youth Seeking Inner Solace Through Mindful Audio'
    },
    'trending-18': {
        'image': 'assets/images/trending/agricultural_ecommerce.jpg',
        'title': 'Thương mại điện tử nông sản bùng nổ: Nông dân livestream bán hàng triệu đơn nông sản tươi',
        'title_en': 'Agricultural Livestream E-Commerce Surge: Vietnamese Farmers Selling Direct to Global Homes'
    },
    'trending-19': {
        'image': 'assets/images/trending/esports_championship.jpg',
        'title': 'Thể thao điện tử (Esports) Việt Nam lập kỳ tích: Đội tuyển trẻ khẳng định vị thế trên đấu trường châu lục',
        'title_en': 'Vietnamese Esports Team Clinches Historic Continental Victory in Thrilling Finals'
    },
    'trending-20': {
        'image': 'assets/images/trending/indie_music_acoustic.jpg',
        'title': 'Làn sóng âm nhạc Indie Việt: Những giai điệu mộc mạc chạm đến triệu trái tim người trẻ',
        'title_en': 'The Acoustic Vietnamese Indie Wave: Raw Melodies Resonating with Millions of Youth'
    },

    # ================= SOCIETY =================
    'society-1': {
        'image': 'assets/images/society/image3.jpg',
        'title': 'Ứng phó bão giá: Các mô hình tương trợ cộng đồng và 'chợ 0 đồng' tiếp sức người nghèo',
        'title_en': 'Cost of Living Crisis: Inspiring Grassroots Responses That Empower Communities',
        'sourceUrl': 'https://www.positive.news/society/cost-of-living-crisis-refreshing-responses/',
        'sourceName': 'Positive News'
    },
    'society-2': {
        'image': 'assets/images/society/offshore_wind_energy.jpg',
        'title': 'Chuyển dịch năng lượng quốc gia: Tiềm năng điện gió ngoài khơi dẫn lối tương lai xanh',
        'title_en': 'National Energy Transition: Offshore Wind Power Illuminating Vietnam’s Net-Zero Horizon'
    },
    'society-3': {
        'image': 'assets/images/society/ethnic_minority_heritage.jpg',
        'title': 'Số hóa và bảo tồn phương ngữ các dân tộc thiểu số: Cứu lấy tiếng mẹ đẻ trước nguy cơ mai một',
        'title_en': 'Digitizing and Preserving Indigenous Dialects: Saving Mother Tongues from Extinction'
    },
    'society-4': {
        'image': 'assets/images/society/hanoi_metro_railway.jpg',
        'title': 'Cuộc cách mạng giao thông công cộng: Các tuyến Metro thay đổi thói quen di chuyển đô thị',
        'title_en': 'Public Transit Revolution: Elevated Urban Metro Transforming Commuting Culture'
    },
    'society-5': {
        'image': 'assets/images/society/rural_kids_coding_class.jpg',
        'title': 'Bình đẳng giáo dục thời công nghệ: Các lớp học lập trình miễn phí cho trẻ em vùng sâu, vùng xa',
        'title_en': 'Bridging the Digital Divide: Free Programming Classrooms for Underprivileged Rural Children'
    },
    'society-6': {
        'image': 'assets/images/society/image7.png',
        'title': 'Chùa Việt thời 4.0: Giảng pháp qua TikTok và cúng dường qua mã QR tiện ích',
        'title_en': 'Vietnamese Buddhist temples embrace TikTok sermons and QR code donations',
        'sourceUrl': 'https://vietnamnet.vn/en/vietnamese-buddhist-temples-embrace-tiktok-sermons-and-qr-code-donations-2570595.html',
        'sourceName': 'VietnamNet'
    },
    'society-7': {
        'image': 'assets/images/society/image11.jpg',
        'title': 'Kinh tế Việt Nam bứt phá ngoạn mục: Tăng trưởng GDP 9.01% gần gấp ba dự báo toàn cầu',
        'title_en': 'Vietnam's GDP grows 9.01%, nearly triple global forecast',
        'sourceUrl': 'https://vietnamnet.vn/en/vietnam-s-gdp-grows-9-01-nearly-triple-global-forecast-2563213.html',
        'sourceName': 'VietnamNet'
    },
    'society-8': {
        'image': 'assets/images/society/image24.jpg',
        'title': 'Tiếng Việt trong ngôi nhà Nam Phi: Hành trình người mẹ truyền lửa cội nguồn nơi đất khách',
        'title_en': 'A Vietnamese voice in a South African home',
        'sourceUrl': 'https://vietnamnews.vn/society/1803581/a-vietnamese-voice-in-a-south-african-home.html',
        'sourceName': 'Vietnam News'
    },
    'society-9': {
        'image': 'assets/images/society/image28.jpg',
        'title': 'Cẩm nang cho du khách lần đầu đến Việt Nam: Từ phố cổ Hà Nội đến bãi biển Phú Quốc',
        'title_en': 'Vietnam for first-timers, beach lovers and nightlife seekers: Where to go?',
        'sourceUrl': 'https://news.tuoitre.vn/vietnam-for-first-timers-beach-lovers-and-nightlife-seekers-where-to-go-103261022142743028.htm',
        'sourceName': 'Tuổi Trẻ News'
    },
    'society-10': {
        'image': 'assets/images/society/image31.jpg',
        'title': 'Bên trong ngôi biệt thự trăm tuổi hình chữ Khẩu của đại gia phố cổ Hàng Bè',
        'title_en': 'Inside Hanoi tycoon’s 100-year-old villa in the Old Quarter',
        'sourceUrl': 'https://e.vnexpress.net/photo/trend/inside-hanoi-tycoons-100-year-old-villa-in-the-old-quarter-5140151.html',
        'sourceName': 'VnExpress International'
    },
    'society-11': {
        'image': 'assets/images/society/telemedicine_remote_doctor.jpg',
        'title': 'Chuyển đổi số y tế cơ sở: Bác sĩ vùng cao chẩn đoán bệnh từ xa qua hệ thống Telemedicine',
        'title_en': 'Primary Healthcare Digitalization: Remote Highland Clinics Connected via Telemedicine'
    },
    'society-12': {
        'image': 'assets/images/society/mekong_saline_adaptation.jpg',
        'title': 'Thích ứng biến đổi khí hậu: Nông dân Bến Tre chuyển đổi sinh kế thành công trước đợt hạn mặn lịch sử',
        'title_en': 'Climate Adaptation in the Mekong Delta: Ben Tre Farmers Thriving Amid Historic Saline Tides'
    },
    'society-13': {
        'image': 'assets/images/society/highland_mobile_library.jpg',
        'title': 'Thư viện cộng đồng vùng cao: Những chuyến xe sách vượt đèo gieo mầm tri thức cho trẻ em bản nghèo',
        'title_en': 'Highland Mobile Libraries: Books Crossing Mountain Passes to Nurture Children\'s Dreams'
    },
    'society-14': {
        'image': 'assets/images/society/community_safe_shelter.jpg',
        'title': 'Mạng lưới nhà tạm lánh cộng đồng: Lá chắn bảo vệ phụ nữ và trẻ em trước nạn bạo lực gia đình',
        'title_en': 'Community Safe Havens: Protective Shelters Safeguarding Women and Children from Domestic Violence'
    },
    'society-15': {
        'image': 'assets/images/society/vietnamese_ao_dai_finland.jpg',
        'title': 'Áo dài tôn vinh văn hóa Việt Nam tại Phần Lan qua sáng kiến 'Ngôi nhà Áo dài'',
        'title_en': 'Ao Dai Celebrates Vietnamese Culture in Finland Through the Landmark \'Ao Dai House\' Project'
    },
    'society-16': {
        'image': 'assets/images/society/child_online_safety.jpg',
        'title': 'Việt Nam giải quyết các lỗ hổng về an toàn trực tuyến cho trẻ em trong chiến lược số quốc gia',
        'title_en': 'Vietnam Tackles Critical Gaps in Child Online Safety Across National Digital Frameworks'
    },
    'society-17': {
        'image': 'assets/images/society/thai_nguyen_tea_hills.jpg',
        'title': 'Văn hóa trà Thái Nguyên thúc đẩy phát triển du lịch sinh thái nông nghiệp bền vững',
        'title_en': 'Thai Nguyen Tea Culture Driving Sustainable Agritourism and Highland Prosperity'
    },
    'society-18': {
        'image': 'assets/images/society/hanoi_community_fitness.jpg',
        'title': 'Thiết chế thể thao cộng đồng tại Hà Nội: Thúc đẩy lối sống năng động và gắn kết khối phố',
        'title_en': 'Community Public Facilities Fostering Active Living and Civic Solidarity Across Hanoi'
    },
    'society-19': {
        'image': 'assets/images/society/youth_caring_elderly.jpg',
        'title': 'Người trẻ chung tay chăm sóc và mang hơi ấm tới người cao tuổi neo đơn giữa lòng đô thị',
        'title_en': 'Youth Volunteers Bringing Warmth and Compassionate Care to Solitary Urban Seniors'
    },
    'society-20': {
        'image': 'assets/images/society/waste_sorting_recycling.jpg',
        'title': 'Chiến dịch phân loại rác tại nguồn: Người dân đô thị chung tay vì một Việt Nam xanh',
        'title_en': 'Source-Separated Waste Sorting Campaign: Urban Citizens Uniting for a Greener Vietnam'
    },

    # ================= HUMAN STORIES =================
    'human-1': {
        'image': 'assets/images/human_stories/image1.jpg',
        'title': 'Thấu hiểu nỗi cô đơn tuổi già: Khi những người trẻ chọn bước tới để trao đi sự lắng nghe',
        'title_en': '\'I wanted to make a change knowing older people suffer from loneliness\'',
        'sourceUrl': 'https://www.theguardian.com/voluntary-sector-network/2018/jun/04/volunteering-older-people-loneliness-isolation',
        'sourceName': 'The Guardian'
    },
    'human-2': {
        'image': 'assets/images/human_stories/image11.jpg',
        'title': 'Chiếc túi ân tình: Món quà nhỏ làm thay đổi cuộc đời người cựu chiến binh vô gia cư',
        'title_en': 'Kindness Bag Changes Homeless Vet\'s Life, Now He Delivers Them on LA Streets',
        'sourceUrl': 'https://www.goodnewsnetwork.org/kindness-bag-changes-homeless-vets-life/',
        'sourceName': 'Good News Network'
    },
    'human-3': {
        'image': 'assets/images/human_stories/image3.png',
        'title': 'Phép màu hồi sinh của chàng trai bom đạn Iraq Qusay Hussein: 'Tôi được trao cơ hội sống thứ hai'',
        'title_en': '“I was given a second chance”: Qusay Hussein\'s miraculous survival and journey of hope',
        'sourceUrl': 'https://www.theguardian.com/lifeandstyle/2019/nov/03/i-was-given-a-second-chance-six-amazing-people-describe-their-life-changes',
        'sourceName': 'The Guardian / MSF'
    },
    'human-4': {
        'image': 'assets/images/human_stories/image7.png',
        'title': 'Nghĩa cử hào hiệp: Những nông dân thiện nguyện gây quỹ 400.000 USD mỗi năm cho học sinh nghèo',
        'title_en': 'These volunteer farmers raise $400,000 each year for teens going to college',
        'sourceUrl': 'https://www.washingtonpost.com/lifestyle/2023/11/02/gruver-farm-scholarship-texas/',
        'sourceName': 'The Washington Post'
    },
    'human-5': {
        'image': 'assets/images/human_stories/mountain_teacher_trail.jpg',
        'title': 'Thầy giáo cõng chữ lên đỉnh Ngọc Linh: 15 năm kiên trì thắp sáng tương lai học trò vùng cao',
        'title_en': 'Carrying Literacy up Mount Ngoc Linh: A Highland Teacher\'s 15-Year Devotion to Mountain Children'
    },
    'human-6': {
        'image': 'assets/images/human_stories/emotional_family_reunion.jpg',
        'title': 'Hành trình 15 năm tìm con thất lạc: Phép màu từ tình thương và mạng xã hội',
        'title_en': 'A Mother\'s 15-Year Search for Her Lost Son: A Heartbreaking Miracle of Unfailing Love'
    },
    'human-7': {
        'image': 'assets/images/human_stories/charity_soup_kitchen.jpg',
        'title': 'Quán cơm 0 đồng bên cổng bệnh viện: Bữa ăn nóng hổi và điểm tựa ấm áp cho bệnh nhân nghèo',
        'title_en': 'The Zero-Dong Charity Kitchen: Free Warm Meals Fueling Hope for Impoverished Patients'
    },
    'human-8': {
        'image': 'assets/images/human_stories/forest_ranger_patrol.jpg',
        'title': 'Người gác rừng Cát Tiên: Cuộc chiến thầm lặng ngày đêm bảo vệ lá phổi xanh của Tổ quốc',
        'title_en': 'The Silent Guardians of Cat Tien: Rangers Risking Lives to Shield Ancient Primeval Forests'
    },
    'human-9': {
        'image': 'assets/images/human_stories/image22.jpg',
        'title': 'Món quà vận động cho 1,5 triệu mảnh đời: Hành trình thắp sáng tự do cho người khuyết tật nghèo',
        'title_en': 'On World Kindness Day, how one nonprofit has given the gift of mobility to 1.5 million people',
        'sourceUrl': 'https://abcnews.com/video/127480629/',
        'sourceName': 'ABC News'
    },
    'human-10': {
        'image': 'assets/images/human_stories/image26.jpg',
        'title': 'Ánh sáng điện lưới về bản xa: Hơn 1.500 đồng bào dân tộc thiểu số đổi đời',
        'title_en': 'Stable electricity brings light to homes in remote village',
        'sourceUrl': 'https://vietnamnews.vn/society/1803487/stable-electricity-brings-light-to-homes-in-remote-village.html',
        'sourceName': 'Vietnam News'
    },
    'human-11': {
        'image': 'assets/images/human_stories/creative_culinary_bento.jpg',
        'title': 'Người mẹ Hà Nội biến bữa cơm gia đình thành tác phẩm nghệ thuật truyền cảm hứng',
        'title_en': 'Mother Turns Meals into Art: Creative Culinary Storytelling Inspiring Hanoi Families'
    },
    'human-12': {
        'image': 'assets/images/human_stories/extraordinary_mother_love.jpg',
        'title': 'Những người mẹ phi thường, tình yêu phi thường: Vượt giông bão cuộc đời nuôi con khôn lớn',
        'title_en': 'Extraordinary Mothers, Extraordinary Love: Boundless Resilience in the Face of Life\'s Tempest'
    },
    'human-13': {
        'image': 'assets/images/human_stories/disabled_mentor_teaching.jpg',
        'title': 'Thầy giáo khuyết tật thắp lửa lập trình cho hàng trăm bạn trẻ khó khăn',
        'title_en': 'Paralyzed Coding Mentor Empowering Hundreds of Underprivileged Youth to Code Their Futures'
    },
    'human-14': {
        'image': 'assets/images/human_stories/flood_rescue_volunteers.jpg',
        'title': 'Đội thuyền cứu hộ của những ngư dân miền Trung: Băng qua tâm lũ dữ cứu người',
        'title_en': 'The Fisherman Flotilla of Central Vietnam: Braving Raging Floodwaters to Rescue Stranded Lives'
    },
    'human-15': {
        'image': 'assets/images/human_stories/night_street_classroom.jpg',
        'title': 'Lớp học chữ miễn phí dưới ánh đèn đường: 18 năm gieo hy vọng cho trẻ em lao động nghèo',
        'title_en': 'Free Sidewalk Evening School: 18 Years Sowing Seeds of Hope for Child Laborers in the City'
    },
    'human-16': {
        'image': 'assets/images/human_stories/free_volunteer_ambulance.jpg',
        'title': 'Chuyến xe cứu thương 0 đồng của người tài xế cựu binh miền Tây',
        'title_en': 'The Zero-Dong Ambulance: Veteran Driver’s 12-Year Mission Rushing Patients to Emergency Rooms'
    },
    'human-17': {
        'image': 'assets/images/human_stories/elderly_land_donors.jpg',
        'title': 'Cặp vợ chồng U70 và hành trình hiến đất mở đường, dựng trường cho trẻ em nghèo',
        'title_en': 'The Generous Octogenarians Donating Family Land to Build Mountain Classrooms'
    },
    'human-18': {
        'image': 'assets/images/human_stories/cerebral_palsy_scholar.jpg',
        'title': 'Nghị lực của cô gái bại não trở thành dịch giả sách truyền cảm hứng',
        'title_en': 'Cerebral Palsy Scholar Translating Inspirational Books to Empower Youth'
    },
    'human-19': {
        'image': 'assets/images/human_stories/heirloom_rice_engineer.jpg',
        'title': 'Chàng kỹ sư bỏ phố về làng tái sinh giống lúa cổ bản địa của ông cha',
        'title_en': 'Agronomist Leaves Corporate City Life to Revive Ancient Ancestral Heirloom Rice Grains'
    },
    'human-20': {
        'image': 'assets/images/human_stories/elderly_bike_repair.jpg',
        'title': 'Bà lão 80 tuổi vá xe miễn phí cho sinh viên và người lao động nghèo trên phố Hà Nội',
        'title_en': '80-Year-Old Grandma Repairing Bicycles for Free to Aid Struggling Students and Laborers'
    },

    # ================= MIND & SOUL =================
    'mind-1': {
        'image': 'assets/images/mind_&_soul/image2.jpg',
        'title': 'Sau concert Mỹ Đình, Taeyang (BigBang) liên tục nhắc đến phở và 'show tuyệt nhất'',
        'title_en': 'After My Dinh concert, BigBang\'s Taeyang praises Vietnamese pho and calls it \'the best show\'',
        'sourceUrl': 'https://news.laodong.vn/van-hoa-giai-tri/sau-concert-my-dinh-taeyang-bigbang-lien-tuc-nhac-den-pho-va-show-tuyet-voi-nhat-1791777.ldo',
        'sourceName': 'Báo Lao Động'
    },
    'mind-2': {
        'image': 'assets/images/mind_&_soul/image5.jpg',
        'title': 'Megan Thee Stallion: Biến hóa huyền ảo mùa Halloween và câu chuyện chữa lành qua sáng tạo',
        'title_en': 'The story behind Megan Thee Stallion’s elaborately spooky Halloween costume',
        'sourceUrl': 'https://edition.cnn.com/2026/11/01/entertainment/megan-thee-stallion-halloween-costume',
        'sourceName': 'CNN'
    },
    'mind-3': {
        'image': 'assets/images/mind_&_soul/image9.jpg',
        'title': 'So sánh dinh dưỡng giữa sữa yến mạch và sữa bò: Lợi ích và những lưu ý cho sức khỏe',
        'title_en': 'Oat vs. dairy milk: Nutrition, benefits, and downsides',
        'sourceUrl': 'https://www.health.harvard.edu/diet-and-nutrition/oat-vs-dairy-milk-nutrition-benefits-and-downsides',
        'sourceName': 'Harvard Health'
    },
    'mind-4': {
        'image': 'assets/images/mind_&_soul/slow_living_peace.jpg',
        'title': 'Nghệ thuật sống chậm (Slow Living): Ngắt kết nối với màn hình để tìm lại sự an yên đích thực',
        'title_en': 'The Art of Slow Living: Disconnecting from Screens to Reclaim Mindful Serenity'
    },
    'mind-5': {
        'image': 'assets/images/mind_&_soul/tay_nguyen_gong_ceremony.jpg',
        'title': 'Sức mạnh chữa lành của tiếng cồng chiêng: Đưa tâm thức hòa nhịp cùng đại ngàn Tây Nguyên',
        'title_en': 'Healing Resonance of Sacred Gongs: Aligning the Spirit with the Whispering Central Highlands'
    },
    'mind-6': {
        'image': 'assets/images/mind_&_soul/park_violin_community.jpg',
        'title': '10 năm lớp học vĩ cầm miễn phí giữa lòng công viên TP.HCM: Gieo nốt nhạc bình an',
        'title_en': '10 Years of Free Violin Lessons in the Park: Harmonizing Community Souls in Ho Chi Minh City'
    },
    'mind-7': {
        'image': 'assets/images/mind_&_soul/healing_oasis_sanctuary.jpg',
        'title': 'Ốc đảo chữa lành tâm hồn hoàn toàn miễn phí tại TP. Hồ Chí Minh: Nơi trú ẩn bình an',
        'title_en': 'A Healing Oasis in Ho Chi Minh City: A Sanctuary for Inner Peace Open to All'
    },
    'mind-8': {
        'image': 'assets/images/mind_&_soul/inclusive_theatre_stage.jpg',
        'title': 'Sân khấu dành cho mọi tiếng nói: Nghệ thuật biểu cảm dung nạp và hòa nhập cộng đồng',
        'title_en': 'A Stage for Every Voice: Inclusive Theatre and Creative Expression Uplifting the Disabled'
    },
    'mind-9': {
        'image': 'assets/images/mind_&_soul/steamed_banh_cuon_delight.jpg',
        'title': 'Bánh cuốn Tây Hồ 60 năm gìn giữ phong vị xưa: Một góc ẩm thực tinh tế nuôi dưỡng hoài niệm',
        'title_en': 'Michelin-Honored Saigon Eatery Serves Banh Cuon with an Unbroken Touch of Tradition'
    },
    'mind-10': {
        'image': 'assets/images/mind_&_soul/shinrin_yoku_forest_bath.jpg',
        'title': 'Tắm rừng Ba Vì (Shinrin-yoku): Nghệ thuật hòa mình vào thiên nhiên thanh lọc tâm trí',
        'title_en': 'Ba Vi Forest Bathing (Shinrin-yoku): Immersing in Pristine Greenery to Purify the Weary Mind'
    },
    'mind-11': {
        'image': 'assets/images/mind_&_soul/therapeutic_journaling.jpg',
        'title': 'Viết nhật ký trị liệu: Phương pháp đặt bút trút bỏ gánh nặng tinh thần và kết nối nội tâm',
        'title_en': 'Therapeutic Journaling: Writing Down Thoughts to Release Emotional Burdens and Heal'
    },
    'mind-12': {
        'image': 'assets/images/mind_&_soul/shan_tuyet_ancient_tea.jpg',
        'title': 'Thiền trà Shan Tuyết trên đỉnh Chiêu Lầu Thi: Thưởng một chén trà, buông vạn nỗi ưu phiền',
        'title_en': 'Shan Tuyet Tea Meditation on Chieu Lau Thi Peak: Sip Solace, Release Worldly Turmoil'
    },
    'mind-13': {
        'image': 'assets/images/mind_&_soul/creative_rest_recovery.jpg',
        'title': 'Vượt qua kiệt sức sáng tạo: Tại sao cho phép bản thân được nghỉ ngơi là một đặc ân cần thiết',
        'title_en': 'Overcoming Creative Burnout: Why Granting Yourself Stillness Is an Essential Sacred Act'
    },
    'mind-14': {
        'image': 'assets/images/mind_&_soul/ancient_lithophone_stones.jpg',
        'title': 'Âm vang đàn đá ngàn năm: Liệu pháp chữa lành tâm hồn bằng tần số âm thanh cổ xưa',
        'title_en': 'Echoes of Ancient Lithophones: Sound Therapy Vibrations from Millennia-Old Musical Stones'
    },
    'mind-15': {
        'image': 'assets/images/mind_&_soul/danshari_minimalism.jpg',
        'title': 'Triết lý sống tối giản Danshari: Dọn dẹp không gian sống để giải phóng những vướng bận trong lòng',
        'title_en': 'Danshari Minimalism: Decluttering Your Physical Space to Liberate Your Inner Mind'
    },
    'mind-16': {
        'image': 'assets/images/mind_&_soul/hand_embroidery_art.jpg',
        'title': 'Nghệ thuật thêu tay truyền thống: Liệu pháp tĩnh tâm tìm lại sự tập trung qua từng đường kim mũi chỉ',
        'title_en': 'Traditional Hand Embroidery Therapy: Restoring Inner Focus One Mindful Stitch at a Time'
    },
    'mind-17': {
        'image': 'assets/images/mind_&_soul/self_compassion_peace.jpg',
        'title': 'Học cách bao dung với chính mình: Thoát khỏi cái bẫy của chủ nghĩa hoàn hảo và những lời phán xét',
        'title_en': 'Practicing Self-Compassion: Breaking Free from the Toxic Trap of Unrelenting Perfectionism'
    },
    'mind-18': {
        'image': 'assets/images/mind_&_soul/mindful_pottery_wheel.jpg',
        'title': 'Nghệ thuật gốm vuốt tay: Cảm nhận sự gắn kết với đất mẹ qua từng chuyển động của đôi bàn tay',
        'title_en': 'Mindful Hand-Thrown Pottery: Feeling Deep Oneness with Earth on the Spinning Wheel'
    },
    'mind-19': {
        'image': 'assets/images/mind_&_soul/aromatherapy_natural_scent.jpg',
        'title': 'Chữa lành bằng hương thơm tự nhiên: Liệu pháp tinh dầu trầm hương và hoa bưởi thanh khiết',
        'title_en': 'Aromatherapy with Native Scents: Calming the Nervous System with Agarwood and Pomelo Blossoms'
    },
    'mind-20': {
        'image': 'assets/images/mind_&_soul/image13.jpg',
        'title': 'Đêm đấm bốc của những người phụ nữ từng bị bạo hành: Nơi lấy lại tự tin và sức mạnh bản thân',
        'title_en': 'The women\'s boxing nights helping abuse survivors reclaim courage and dignity',
        'sourceUrl': 'https://www.positive.news/society/the-womens-boxing-nights-helping-abuse-survivors/',
        'sourceName': 'Positive News'
    },

    # ================= IN-DEPTH =================
    'indepth-1': {
        'image': 'assets/images/in-dept/image2.jpg',
        'title': 'Hà Nội không bao giờ ngừng chảy: Hương hoa sữa và ký ức rêu phong giữa dòng đời hối hả',
        'title_en': 'A Hà Nội that never stands still',
        'sourceUrl': 'https://vietnamnews.vn/talk-around-town/1802722/a-ha-noi-that-never-stands-still.html',
        'sourceName': 'Vietnam News'
    },
    'indepth-2': {
        'image': 'assets/images/in-dept/image1.jpg',
        'title': 'Đối diện với căn bệnh Parkinson: Rhys Ifans và Laura Linney chia sẻ về nghệ thuật và lòng dũng cảm',
        'title_en': 'Rhys Ifans and Laura Linney on Parkinson’s: Acting, Humor, and Defying Vulnerability',
        'sourceUrl': 'https://www.theguardian.com/film/2026/nov/02/rhys-ifans-laura-linney-onwards-sideways-film-interview-parkinsons-paul-mayhew-archer',
        'sourceName': 'The Guardian'
    },
    'indepth-3': {
        'image': 'assets/images/in-dept/image3.jpg',
        'title': 'Những nhà giáo dục dùng khoa học dạy lòng trắc ẩn: Khi sự tử tế trở thành môn học chính khóa',
        'title_en': 'Meet the educators using science to teach kindness',
        'sourceUrl': 'https://www.positive.news/society/meet-the-educators-using-science-to-teach-kindness/',
        'sourceName': 'Positive News'
    },
    'indepth-4': {
        'image': 'assets/images/in-dept/image4.jpg',
        'title': 'Ba con người chọn gắn đời mình với thiên nhiên hoang dã: Sứ mệnh bảo vệ sự sống hành tinh',
        'title_en': 'Three people who have jobs in nature: Devoted Custodians of Planetary Life',
        'sourceUrl': 'https://www.positive.news/environment/three-people-who-have-jobs-in-nature/',
        'sourceName': 'Positive News'
    },
    'indepth-5': {
        'image': 'assets/images/in-dept/image8.jpg',
        'title': 'Rory Kinnear và nỗi đau mất cha: Nghệ thuật giúp tôi hàn gắn vết thương sau bi kịch cuộc đời',
        'title_en': 'Rory Kinnear on father Roy\'s death: Grief, Memory, and the Catharsis of Performance',
        'sourceUrl': 'https://www.theguardian.com/tv-and-radio/2026/nov/05/rory-kinnear-father-roy-death',
        'sourceName': 'The Guardian'
    },
    'indepth-6': {
        'image': 'assets/images/mind_&_soul/image14.jpg',
        'title': 'Bò nướng tảng Canada ướp mắc khén Tây Bắc: Giao thoa tinh tế giữa hai nền văn hóa ẩm thực',
        'title_en': 'Canadian ‘outside skirt’ beef combined with Northwest Vietnamese herb marinade',
        'sourceUrl': 'https://vovworld.vn/food-delight/canadian-outside-skirt-beef-combined-with-northwest-vietnamese-herb-marinade-2468953.vov5',
        'sourceName': 'VOV World'
    },
    'indepth-7': {
        'image': 'assets/images/in-dept/hanoi_french_colonial_villa.jpg',
        'title': 'Di sản kiến trúc biệt thự Pháp cổ Hà Nội: Hành trình bảo tồn ký ức đô thị trăm năm',
        'title_en': 'Hanoi’s French Colonial Architectural Heritage: Preserving Centuries of Urban Memory'
    },
    'indepth-8': {
        'image': 'assets/images/in-dept/vietnamese_ceramic_master.jpg',
        'title': 'Gốm cổ Chu Đậu và Bát Tràng: Khát vọng đưa tinh hoa đất Việt vươn tầm nghệ thuật thế giới',
        'title_en': 'Chu Dau and Bat Trang Ceramics: Lifting Vietnamese Clay Artistry to Global Prominence'
    },
    'indepth-9': {
        'image': 'assets/images/in-dept/can_gio_mangrove_forest.jpg',
        'title': 'Hồi sinh rừng ngập mặn Cần Giờ: Cuộc đại kiến tạo lá chắn xanh che chở thành phố phương Nam',
        'title_en': 'Revitalizing Can Gio Mangroves: The Epic Biosphere Shield Defending Southern Megacity'
    },
    'indepth-10': {
        'image': 'assets/images/in-dept/cyber_fraud_investigation.jpg',
        'title': 'Báo cáo điều tra đa tầng: Hành trình lần theo dấu vết các đường dây lừa đảo xuyên biên giới',
        'title_en': 'Multi-Tier Investigative Dossier: Tracing Transnational Cyber Fraud Syndicates'
    },
    'indepth-11': {
        'image': 'assets/images/in-dept/van_phuc_silk_weaving.jpg',
        'title': 'Tiếng thoi đưa lụa Vạn Phúc: Nỗi niềm trăn trở của những nghệ nhân giữ hồn lụa Việt ngàn năm',
        'title_en': 'Rhythm of Van Phuc Looms: Masters Safeguarding a Millennial Heritage of Pure Silk'
    },
    'indepth-12': {
        'image': 'assets/images/in-dept/community_mental_health_circle.jpg',
        'title': 'Đổi mới chăm sóc sức khỏe tâm thần tại cộng đồng: Phá bỏ định kiến và mở rộng vòng tay thấu cảm',
        'title_en': 'Reinventing Community Mental Health: Dismantling Stigma Through Inclusive Empathy'
    },
    'indepth-13': {
        'image': 'assets/images/in-dept/my_son_cham_sanctuary.jpg',
        'title': 'Giải mã bí ẩn gạch nung Mỹ Sơn: Ký ức rêu phong ngàn năm của vương triều Champa cổ',
        'title_en': 'Deciphering the Mystery of My Son Bricks: Millennial Memories of the Ancient Champa Realm'
    },
    'indepth-14': {
        'image': 'assets/images/in-dept/deepwater_container_port.jpg',
        'title': 'Địa kinh tế cảng biển nước sâu và logistics đường thủy: Đòn bẩy đưa Việt Nam thành trung tâm trung chuyển',
        'title_en': 'Deepwater Transshipment Geoeconomics: Positioning Vietnam as a Premier Maritime Hub'
    },
    'indepth-15': {
        'image': 'assets/images/in-dept/medical_ai_robotics.jpg',
        'title': 'Đạo đức trí tuệ nhân tạo trong y khoa: Điểm giao thoa giữa thuật toán chính xác và lương tâm người thầy thuốc',
        'title_en': 'Ethics of Artificial Intelligence in Medicine: Where Algorithmic Precision Meets Hippocratic Conscience'
    },
    'indepth-16': {
        'image': 'assets/images/in-dept/heirloom_seed_bank.jpg',
        'title': 'Ngân hàng hạt giống bản địa: Những người âm thầm gom góp tương lai lương thực của quốc gia',
        'title_en': 'Indigenous Heirloom Seed Banks: Quiet Custodians Safeguarding National Food Sovereignty'
    },
    'indepth-17': {
        'image': 'assets/images/in-dept/dong_ho_folk_painting.jpg',
        'title': 'Tranh dân gian Đông Hồ: Hồn dân tộc lắng đọng trong màu điệp, giấy dó và những nét khắc mộc mạc',
        'title_en': 'Dong Ho Woodblock Folk Art: The National Soul Etched on Scallop-Shell Paper'
    },
    'indepth-18': {
        'image': 'assets/images/in-dept/cat_ba_langur_conservation.jpg',
        'title': 'Cuộc chiến sinh tồn của đàn voọc Cát Bà: Nỗi trăn trở giữ lại loài linh trưởng quý hiếm trước bờ vực tuyệt chủng',
        'title_en': 'The Struggle for Survival of Cat Ba Langurs: Dedicated Wardens Shielding Earth\'s Rarest Primate'
    },
    'indepth-19': {
        'image': 'assets/images/in-dept/hue_imperial_gastronomy.jpg',
        'title': 'Ẩm thực cung đình Huế: Triết lý âm dương sâu sắc ẩn sau những mâm yến tiệc hoàng triều một thuở',
        'title_en': 'Hue Imperial Gastronomy: Profound Yin-Yang Cosmological Philosophy Behind Ancient Royal Banquets'
    },
    'indepth-20': {
        'image': 'assets/images/in-dept/han_nom_digital_archive.jpg',
        'title': 'Hành trình số hóa di sản Hán Nôm: Cuộc chạy đua thầm lặng với thời gian để lưu giữ linh hồn tiền nhân',
        'title_en': 'Digitalizing Nom and Han Archives: A Quiet Race Against Time to Rescue Ancestral Manuscripts'
    }
}

# Update js/data.js
with open('js/data.js', 'r', encoding='utf-8') as f:
    js_text = f.read()

m = re.search(r'const ARTICLES_DATA = (\[[\s\S]*?\]);\s*(?:window\.|\n\w|\Z)', js_text)
if not m:
    print('Error: ARTICLES_DATA not found in js/data.js')
    sys.exit(1)

articles = json.loads(m.group(1))
print(f'Total articles in file: {len(articles)}')

updated_count = 0
for a in articles:
    aid = a.get('id')
    if aid in EXACT_MAPPING:
        mapping = EXACT_MAPPING[aid]
        for k, v in mapping.items():
            a[k] = v
        updated_count += 1

print(f'Updated {updated_count} articles with exact thematic mapping!')

new_json = json.dumps(articles, ensure_ascii=False, indent=2)
new_js_text = js_text[:m.start(1)] + new_json + js_text[m.end(1):]

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(new_js_text)

print('Successfully written updated articles to js/data.js!')
