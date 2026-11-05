import sys, json, re, os
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

# The Master 100-Article Accurate Mapping
# Key = Article ID in js/data.js
MASTER_100_MAP = {
    # ----------------- TRENDING (20) -----------------
    'trending-1': {
        'image': 'assets/images/trending/lawmakers_lead.jpg',
        'title': 'Đại biểu Quốc hội đề xuất các giải pháp đột phá phát triển kinh tế vùng miền núi, biên giới',
        'title_en': 'Lawmakers propose measures to boost development in mountainous, border regions',
        'subtitle': 'Tập trung đầu tư hạ tầng giao thông kết nối, phát huy thế mạnh nông lâm sản đặc thù và nâng cao sinh kế bền vững cho đồng bào các tỉnh miền núi phía Bắc.',
        'subtitle_en': 'Focusing on transport infrastructure connectivity, leveraging indigenous agro-forestry strengths, and elevating sustainable livelihoods in northern border provinces.',
        'sourceUrl': 'https://en.nhandan.vn/lawmakers-propose-measures-to-boost-development-in-mountainous-border-regions-post168532.html',
        'sourceName': 'Báo Nhân Dân'
    },
    'trending-2': {
        'image': 'assets/images/trending/image2.jpg',
        'title': 'Lòng tốt của người lạ: Năm 1989 tôi đánh rơi chiếc ví có 1.000 USD và hành trình tìm lại khó tin',
        'title_en': 'The Kindness of Strangers: In 1989 I lost a wallet with $1,000 in it. A couple went to incredible lengths to return it',
        'subtitle': 'Câu chuyện cảm động về đôi vợ chồng xa lạ đã kiên trì lần theo từng manh mối suốt nhiều tuần để trao tận tay người mất số tiền dành dụm cả năm trời.',
        'subtitle_en': 'A deeply touching story of a stranger couple who painstakingly traced clues for weeks to return a year\'s savings to its rightful owner.',
        'sourceUrl': 'https://www.theguardian.com/lifeandstyle/2026/nov/02/kindness-of-strangers-lost-wallet-cash-returned-couple',
        'sourceName': 'The Guardian'
    },
    'trending-3': {
        'image': 'assets/images/trending/image3.jpg',
        'title': 'Khởi nghiệp tuổi 60: Ở tuổi 26 mơ về Porsche, tuổi 68 tự tay chế tạo chiếc 904FF',
        'title_en': 'A new start after 60: At 26, I saw my dream Porsche. At 68, I built one from scratch',
        'subtitle': 'Hành trình bền bỉ suốt 8 năm của một người thợ cơ khí nghỉ hưu biến giấc mơ thanh xuân thành hiện thực bằng đôi bàn tay tài hoa và đam mê bất tận.',
        'subtitle_en': 'An eight-year labor of love by a retired mechanic turning a youthful dream into reality through artisanal craftsmanship and enduring passion.',
        'sourceUrl': 'https://www.theguardian.com/lifeandstyle/2026/nov/02/a-new-start-after-60-at-26-i-saw-my-dream-porsche-at-68-i-built-one-from-scratch',
        'sourceName': 'The Guardian'
    },
    'trending-4': {
        'image': 'assets/images/trending/image8.jpg',
        'title': 'Gánh mưu sinh: Hồn cốt bình dị trên từng góc phố cổ Hội An',
        'title_en': 'Street Vendors with Shoulder Pole: A Timeless Hallmark of Hoi An Ancient Town',
        'subtitle': 'Hình ảnh đôi quang gánh trĩu nặng nhịp sống mưu sinh, vẻ đẹp cần lao mộc mạc và ký ức rêu phong trên từng ngõ nhỏ di sản níu chân du khách quốc tế.',
        'subtitle_en': 'The rustic beauty of vendors carrying woven baskets on shoulder poles has long been an indispensable, soulful hallmark of the ancient town.',
        'sourceUrl': 'https://e.vnexpress.net/news/travel/places/street-vendors-with-shoulder-pole-a-familiar-sight-in-vietnam-s-old-town-4099491.html',
        'sourceName': 'VnExpress International'
    },
    'trending-5': {
        'image': 'assets/images/trending/image1.jpg',
        'title': 'Chiến dịch 500 ngày đêm ADN: Trả lại danh tính cho gần 800 hài cốt liệt sĩ',
        'title_en': '500-day-and-night campaign: DNA testing results returned for nearly 800 fallen soldiers',
        'subtitle': 'Hành trình thầm lặng nhưng đầy tự hào ứng dụng công nghệ giám định ADN hiện đại trả lại tên cho các anh hùng dân tộc vì đạo lý Uống nước nhớ nguồn.',
        'subtitle_en': 'How forensic science, advanced DNA technology, and dedicated devotion bring names back to nearly 800 unidentified martyrs, fulfilling a sacred mission.',
        'sourceUrl': 'https://en.nhandan.vn/500-day-and-night-campaign-dna-testing-results-returned-for-nearly-800-samples-of-martyrs-remains-post167905.html',
        'sourceName': 'Báo Nhân Dân'
    },
    'trending-6': {
        'image': 'assets/images/trending/image15.jpg',
        'title': 'Vương quốc Anh tăng mức chứng minh tài chính đối với du học sinh',
        'title_en': 'UK to hike proof-of-funds requirement for international students',
        'subtitle': 'Quy định tài chính mới có hiệu lực từ cuối tháng 11 yêu cầu du học sinh quốc tế phải chứng minh số dư sinh hoạt phí cao hơn đáng kể khi xin thị thực.',
        'subtitle_en': 'New visa rules taking effect in late November require international students to demonstrate substantially higher living funds.',
        'sourceUrl': 'https://e.vnexpress.net/news/news/education/uk-to-hike-proof-of-funds-requirement-for-international-students-from-nov-30-5139725.html',
        'sourceName': 'VnExpress International'
    },
    'trending-7': {
        'image': 'assets/images/trending/ai_newsroom_journalism.jpg',
        'title': 'Trí tuệ nhân tạo trong báo chí hiện đại: Tăng tốc quy trình nhưng giữ trọn đạo đức nhân văn',
        'title_en': 'AI in modern journalism: Enhancing reporting speed while preserving human empathy and ethics',
        'subtitle': 'Các tòa soạn hàng đầu ứng dụng AI tổng hợp dữ liệu thời gian thực nhưng kiên quyết đặt chuẩn mực kiểm chứng và lương tâm nhà báo làm kim chỉ nam.',
        'subtitle_en': 'Leading newsrooms leverage real-time data automation while rigorously upholding multi-source fact-checking and ethical empathy.'
    },
    'trending-8': {
        'image': 'assets/images/trending/vintage_film_camera.jpg',
        'title': 'Bùng nổ trào lưu săn máy ảnh film cổ: Gen Z tìm lại vẻ đẹp hoài niệm của nhiếp ảnh tương tự',
        'title_en': 'Resurgence of Vintage Film Cameras: Gen Z Embracing Analogue Nostalgia',
        'subtitle': 'Những cuộn film 35mm và tiếng trập cơ học mang lại sự kiên nhẫn, xúc cảm chân thật giữa kỷ nguyên chụp ảnh số hàng loạt và bộ lọc ảo.',
        'subtitle_en': 'Mechanical shutters and 35mm rolls inspire patience and tangible authenticity amid an era of ephemeral digital filters.'
    },
    'trending-9': {
        'image': 'assets/images/trending/robusta_coffee_vietnam.jpg',
        'title': 'Cà phê Robusta Việt Nam bùng nổ thế giới: Từ hạt rẻ tiền đến làn sóng đặc sản triệu đô',
        'title_en': 'Vietnamese Robusta Coffee Goes Global: From Cheap Commodity to Specialty Craze',
        'subtitle': 'Nỗ lực nâng cấp quy trình thu hái chín 100% và lên men yếm khí giúp cà phê hạt Robusta Tây Nguyên chinh phục giới sành cà phê quốc tế.',
        'subtitle_en': 'Ripe harvesting and anaerobic fermentation elevate Central Highlands Robusta beans into international specialty prominence.'
    },
    'trending-10': {
        'image': 'assets/images/trending/rooftop_pocket_forest.jpg',
        'title': 'Trào lưu \'rừng bỏ túi\' trên mái cao ốc: Đô thị hóa xanh giữa những khối bê tông chọc trời',
        'title_en': 'Urban Pocket Forests on High-Rise Rooftops: Rewilding Concrete Jungles',
        'subtitle': 'Các khu vườn sinh thái thu nhỏ trên tầng thượng giúp hạ nhiệt tòa nhà, thanh lọc không khí và mang thiên nhiên vào đời sống cư dân phố thị.',
        'subtitle_en': 'Sky gardens cool buildings, purify smog, and bring biodiversity into dense metropolitan skylines.'
    },
    'trending-11': {
        'image': 'assets/images/trending/art_toy_blind_box.jpg',
        'title': 'Hiện tượng \'hộp mù\' Art Toy và trào lưu sưu tầm gây bão: Giới trẻ chi hàng chục triệu săn lùng',
        'title_en': 'The Blind Box Art Toy Phenomenon: Young Consumers Spending Millions on Viral Collectibles',
        'subtitle': 'Cảm giác hồi hộp khi bóc seal cùng giá trị thẩm mỹ của các tác phẩm đồ chơi nghệ thuật tạo nên cơn sốt văn hóa thị giác bùng nổ.',
        'subtitle_en': 'The thrill of mystery unboxing combined with designer artistry sparks a vibrant pop-culture phenomenon among urban youth.'
    },
    'trending-12': {
        'image': 'assets/images/trending/heritage_train_travel.jpg',
        'title': 'Làn sóng du lịch \'chữa lành\' bằng tàu hỏa Bắc - Nam: Ngắm trọn vẻ đẹp di sản dải đất hình chữ S',
        'title_en': 'Healing Journey by Heritage Train: Rediscovering Vietnam’s Scenic Splendors on Slow Rails',
        'subtitle': 'Những chuyến tàu chạy dọc eo biển miền Trung và đèo Hải Vân mở ra trải nghiệm du lịch chậm, kết nối tâm hồn với thiên nhiên hùng vĩ.',
        'subtitle_en': 'Scenic coastal railway routes through mountain passes offer a restorative slow-travel escape reconnecting passengers with nature.'
    },
    'trending-13': {
        'image': 'assets/images/trending/military_history_museum.jpg',
        'title': 'Bảo tàng Lịch sử Quân sự Việt Nam mới: Hiện tượng văn hóa thu hút hàng vạn bạn trẻ mỗi ngày',
        'title_en': 'New Vietnam Military History Museum: Cultural Phenomenon Drawing Thousands Daily',
        'subtitle': 'Không gian trưng bày hoành tráng kết hợp công nghệ tương tác 3D đưa lịch sử hào hùng của dân tộc chạm đến trái tim thế hệ trẻ.',
        'subtitle_en': 'Grand architectural exhibits combined with immersive 3D technology bring national heroic history alive for younger generations.'
    },
    'trending-14': {
        'image': 'assets/images/trending/vietnamese_heritage_attire.jpg',
        'title': 'Trào lưu cổ phục Việt bùng nổ trên mạng xã hội: Giới trẻ tự hào diện Nhật Bình, áo ngũ thân',
        'title_en': 'Traditional Vietnamese Attire Goes Viral: Youth Reviving Historic Nhat Binh Garments',
        'subtitle': 'Sự phục hưng của những tà áo truyền thống thời Nguyễn trong các lễ hội và bộ ảnh nghệ thuật thể hiện lòng tự hào văn hóa sâu sắc.',
        'subtitle_en': 'The revival of historic Nguyen dynasty garments in modern celebrations reflects a profound surge in cultural pride.'
    },
    'trending-15': {
        'image': 'assets/images/trending/electric_vehicle_green.jpg',
        'title': 'Xe điện \'Made in Vietnam\' vươn ra biển lớn: Dấu ấn công nghệ xanh trên thị trường quốc tế',
        'title_en': 'Made-in-Vietnam Electric Vehicles Expanding Globally: Sustainable Mobility Innovation',
        'subtitle': 'Bước chuyển mình mạnh mẽ của ngành công nghiệp ô tô nội địa khẳng định vị thế công nghệ và cam kết phát thải ròng bằng 0.',
        'subtitle_en': 'Domestic automotive innovation expands abroad, driving green technological competence and net-zero commitments.'
    },
    'trending-16': {
        'image': 'assets/images/trending/hanoi_street_food.jpg',
        'title': 'Cơn sốt ẩm thực đường phố Hà Nội: Phở cuốn và bánh tôm hồ Tây chinh phục giới sành ăn quốc tế',
        'title_en': 'Hanoi Street Food Renaissance: Pho Cuon and West Lake Shrimp Cakes Captivate Global Foodies',
        'subtitle': 'Sự tươi mát của rau thơm, nước chấm chua ngọt tinh tế và hương vị truyền thống đưa ẩm thực Thủ đô tỏa sáng trên bản đồ thế giới.',
        'subtitle_en': 'Fresh herbs, delicate sweet-sour dipping broths, and authentic flavors position Hanoi culinary street culture on the global stage.'
    },
    'trending-17': {
        'image': 'assets/images/trending/podcast_healing_audio.jpg',
        'title': 'Podcast và xu hướng \'nghe chữa lành\': Giới trẻ đô thị tìm lại sự an yên giữa bộn bề công nghệ',
        'title_en': 'Therapeutic Podcasting Trend: Urban Youth Seeking Inner Solace Through Mindful Audio',
        'subtitle': 'Những giọng đọc truyền cảm, giai điệu mộc mạc và câu chuyện chân thành trở thành liều thuốc tinh thần xoa dịu áp lực thường nhật.',
        'subtitle_en': 'Intimate audio narrations and heartfelt storytelling offer a calming sanctuary against fast-paced daily screen exhaustion.'
    },
    'trending-18': {
        'image': 'assets/images/trending/agricultural_ecommerce.jpg',
        'title': 'Thương mại điện tử nông sản bùng nổ: Nông dân livestream bán hàng triệu đơn nông sản tươi',
        'title_en': 'Agricultural Livestream E-Commerce Surge: Vietnamese Farmers Selling Direct to Global Homes',
        'subtitle': 'Ứng dụng chuyển đổi số giúp xóa nhòa ranh giới trung gian, đưa đặc sản miệt vườn đến thẳng bàn ăn người tiêu dùng trong và ngoài nước.',
        'subtitle_en': 'Digital platforms eliminate intermediaries, connecting orchard harvests directly with urban and international consumers.'
    },
    'trending-19': {
        'image': 'assets/images/trending/esports_championship.jpg',
        'title': 'Thể thao điện tử (Esports) Việt Nam lập kỳ tích: Đội tuyển trẻ khẳng định vị thế trên đấu trường châu lục',
        'title_en': 'Vietnamese Esports Team Clinches Historic Continental Victory in Thrilling Finals',
        'subtitle': 'Chiến thuật thông minh, tinh thần kỷ luật thép và sự phối hợp ăn ý đem lại tấm huy chương danh giá cho nền thể thao điện tử nước nhà.',
        'subtitle_en': 'Sharp strategic execution, disciplined preparation, and teamwork secure a prestigious international esports championship title.'
    },
    'trending-20': {
        'image': 'assets/images/trending/indie_music_acoustic.jpg',
        'title': 'Làn sóng âm nhạc Indie Việt: Những giai điệu mộc mạc chạm đến triệu trái tim người trẻ',
        'title_en': 'The Acoustic Vietnamese Indie Wave: Raw Melodies Resonating with Millions of Youth',
        'subtitle': 'Không cần phòng thu hào nhoáng hay chiêu trò PR, những ca từ chân phương cất lên từ phòng trọ lại tạo nên sức lan tỏa mãnh liệt.',
        'subtitle_en': 'Unfiltered lyrics and simple acoustic chords recorded in dorm rooms spark immense emotional resonance among millions.'
    },

    # ----------------- SOCIETY (20) -----------------
    'society-1': {
        'image': 'assets/images/society/image3.jpg',
        'title': 'Ứng phó bão giá: Các mô hình tương trợ cộng đồng và \'chợ 0 đồng\' tiếp sức người nghèo',
        'title_en': 'Cost of Living Crisis: Inspiring Grassroots Responses That Empower Communities',
        'subtitle': 'Sáng kiến tiệm tạp hóa Vale Pantry tại Anh và các phiên chợ nhân ái trao quyền lựa chọn thực phẩm, gìn giữ phẩm giá cho người nhận.',
        'subtitle_en': 'Innovative grocery models like the Vale Pantry empower low-income families by preserving human dignity and choice.',
        'sourceUrl': 'https://www.positive.news/society/cost-of-living-crisis-refreshing-responses/',
        'sourceName': 'Positive News'
    },
    'society-2': {
        'image': 'assets/images/society/offshore_wind_energy.jpg',
        'title': 'Chuyển dịch năng lượng quốc gia: Tiềm năng điện gió ngoài khơi dẫn lối tương lai xanh',
        'title_en': 'National Energy Transition: Offshore Wind Power Illuminating Vietnam’s Net-Zero Horizon',
        'subtitle': 'Vùng biển dài hơn 3.260 km mở ra nguồn năng lượng tái tạo dồi dào, giảm thiểu phụ thuộc nhiên liệu hóa thạch và bảo vệ khí hậu.',
        'subtitle_en': 'A vast 3,260-kilometer coastline provides boundless offshore wind potential, accelerating decarbonization goals.'
    },
    'society-3': {
        'image': 'assets/images/society/ethnic_minority_heritage.jpg',
        'title': 'Số hóa và bảo tồn phương ngữ các dân tộc thiểu số: Cứu lấy tiếng mẹ đẻ trước nguy cơ mai một',
        'title_en': 'Digitizing and Preserving Indigenous Dialects: Saving Mother Tongues from Extinction',
        'subtitle': 'Các chuyên gia ngôn ngữ học và thanh niên bản địa cùng xây dựng kho dữ liệu âm thanh số để lưu giữ ký ức văn hóa sống động.',
        'subtitle_en': 'Linguists and indigenous youths build comprehensive digital audio corpora to preserve oral traditions and ancestral tongues.'
    },
    'society-4': {
        'image': 'assets/images/society/hanoi_metro_railway.jpg',
        'title': 'Cuộc cách mạng giao thông công cộng: Các tuyến Metro thay đổi thói quen di chuyển đô thị',
        'title_en': 'Public Transit Revolution: Elevated Urban Metro Transforming Commuting Culture',
        'subtitle': 'Tàu điện trên cao giúp giảm tải ùn tắc giao thông, hạn chế khí thải carbon và kiến tạo lối sống văn minh, chuẩn giờ giấc cho cư dân.',
        'subtitle_en': 'Rapid transit rail eases road congestion, slashes urban carbon emissions, and nurtures punctual commuting habits.'
    },
    'society-5': {
        'image': 'assets/images/society/rural_kids_coding_class.jpg',
        'title': 'Bình đẳng giáo dục thời công nghệ: Các lớp học lập trình miễn phí cho trẻ em vùng sâu, vùng xa',
        'title_en': 'Bridging the Digital Divide: Free Programming Classrooms for Underprivileged Rural Children',
        'subtitle': 'Những chiếc máy tính cũ được phục hồi mang tri thức số và niềm tin vào tương lai đến với học sinh nghèo trên mọi nẻo đường.',
        'subtitle_en': 'Refurbished computers and dedicated volunteers bring digital literacy and hope to underserved mountain classrooms.'
    },
    'video-1': {
        'image': 'assets/images/society/vietnamese_ao_dai_finland.jpg',
        'title': 'Áo dài tôn vinh văn hóa Việt Nam tại Phần Lan qua sáng kiến \'Ngôi nhà Áo dài\'',
        'title_en': 'Ao Dai Celebrates Vietnamese Culture in Finland Through the Landmark \'Ao Dai House\' Project',
        'subtitle': 'Hội Áo dài Việt Nam tại Phần Lan chính thức ra mắt sáng kiến mang 1.000 tà áo dài truyền thống tới quốc gia Bắc Âu.',
        'subtitle_en': 'The Vietnamese Ao Dai Association in Finland brings 1,000 traditional Ao Dai to Nordic friends, celebrating heritage.',
        'sourceUrl': 'https://vietnamtoday.vtv.vn/ao-dai-celebrates-vietnamese-culture-in-finland-100261028101457215.htm',
        'sourceName': 'VTV Vietnam Today'
    },
    'video-2': {
        'image': 'assets/images/society/child_online_safety.jpg',
        'title': 'Việt Nam giải quyết các lỗ hổng về an toàn trực tuyến cho trẻ em trong chiến lược số quốc gia',
        'title_en': 'Vietnam Tackles Critical Gaps in Child Online Safety Across National Digital Frameworks',
        'subtitle': 'Chiến lược quốc gia về phát triển trẻ em giai đoạn 2026–2035 nhằm củng cố kỹ năng số và xây dựng môi trường mạng lành mạnh.',
        'subtitle_en': 'Vietnam\'s National Strategy on Child Development reinforces digital literacy and constructs safe online environments.',
        'sourceUrl': 'https://vietnamtoday.vtv.vn/viet-nam-tackles-gaps-in-child-online-safety-100261101165727007.htm',
        'sourceName': 'VTV Vietnam Today'
    },
    'video-3': {
        'image': 'assets/images/society/arte_social_fraud_doc.jpg',
        'title': 'Những kẻ lừa đảo trên mạng xã hội là ai? | Phim tài liệu ARTE.tv',
        'title_en': 'Who Are the Social Media Fraudsters? | ARTE.tv Documentary',
        'subtitle': 'Phóng sự điều tra chuyên sâu từ ARTE.tv bóc trần những cơ chế tinh vi của các đường dây lừa đảo kỹ thuật số và thao túng tâm lý.',
        'subtitle_en': 'ARTE.tv investigative documentary delving into the sophisticated mechanisms of modern online scams and psychological manipulation.',
        'sourceUrl': 'https://www.youtube.com/watch?v=tIqYjcHRE04',
        'sourceName': 'ARTE.tv Documentary'
    },
    'video-7': {
        'image': 'assets/images/society/thai_nguyen_tea_hills.jpg',
        'title': 'Văn hóa trà Thái Nguyên thúc đẩy phát triển du lịch sinh thái nông nghiệp bền vững',
        'title_en': 'Thai Nguyen Tea Culture Driving Sustainable Agritourism and Highland Prosperity',
        'subtitle': 'Lễ hội Trà quốc tế Thái Nguyên kết nối du khách với những người trồng chè, mở ra cơ hội phát triển du lịch nông nghiệp đặc sắc.',
        'subtitle_en': 'International tea festivals connect travelers with growers, unlocking distinctive sustainable agritourism experiences.',
        'sourceUrl': 'https://vietnamtoday.vtv.vn/thai-nguyen-tea-culture-boosts-tourism-100261101042721506.htm',
        'sourceName': 'VTV Vietnam Today'
    },
    'video-10': {
        'image': 'assets/images/society/hanoi_community_fitness.jpg',
        'title': 'Thiết chế thể thao cộng đồng tại Hà Nội: Thúc đẩy lối sống năng động và gắn kết khối phố',
        'title_en': 'Community Public Facilities Fostering Active Living and Civic Solidarity Across Hanoi',
        'subtitle': 'Các không gian sinh hoạt, sân chơi thể thao công cộng giúp người dân mọi lứa tuổi rèn luyện sức khỏe mà không tốn kém.',
        'subtitle_en': 'Accessible outdoor fitness parks across neighborhoods enable residents to stay healthy, active, and united.',
        'sourceUrl': 'https://vietnamtoday.vtv.vn/community-facilities-promote-healthier-lifestyles-100261019013046705.htm',
        'sourceName': 'VTV Vietnam Today'
    },
    'video-12': {
        'image': 'assets/images/society/youth_caring_elderly.jpg',
        'title': 'Người trẻ chung tay chăm sóc và mang hơi ấm tới người cao tuổi neo đơn giữa lòng đô thị',
        'title_en': 'Youth Volunteers Bringing Warmth and Compassionate Care to Solitary Urban Seniors',
        'subtitle': 'Mỗi tháng một lần, các bạn trẻ tình nguyện lại cùng nhau dọn dẹp nhà cửa, nấu những bữa cơm ấm áp và bầu bạn cùng các cụ già.',
        'subtitle_en': 'Young volunteers dedicate weekends to cleaning homes, cooking warm meals, and comforting solitary seniors.',
        'sourceUrl': 'https://vietnamtoday.vtv.vn/youth-caring-for-the-elderly-100260226123528559.htm',
        'sourceName': 'VTV Vietnam Today'
    },
    'society-6': {
        'image': 'assets/images/society/image7.png',
        'title': 'Chùa Việt thời 4.0: Giảng pháp qua TikTok và cúng dường qua mã QR tiện ích',
        'title_en': 'Vietnamese Buddhist temples embrace TikTok sermons and QR code donations',
        'subtitle': 'Sự dung hòa giữa giáo lý từ bi ngàn năm và công nghệ hiện đại giúp đạo Phật tiếp cận gần gũi hơn với giới trẻ.',
        'subtitle_en': 'Bridging millennial Buddhist wisdom with digital accessibility brings compassionate ethics closer to younger seekers.',
        'sourceUrl': 'https://vietnamnet.vn/en/vietnamese-buddhist-temples-embrace-tiktok-sermons-and-qr-code-donations-2570595.html',
        'sourceName': 'VietnamNet'
    },
    'society-7': {
        'image': 'assets/images/society/image11.jpg',
        'title': 'Kinh tế Việt Nam bứt phá ngoạn mục: Tăng trưởng GDP 9.01% gần gấp ba dự báo toàn cầu',
        'title_en': 'Vietnam\'s GDP grows 9.01%, nearly triple global forecast',
        'subtitle': 'Sức bật từ xuất khẩu, vốn đầu tư FDI kỷ lục và công nghiệp chế biến chế tạo đưa Việt Nam trở thành điểm sáng kinh tế thế giới.',
        'subtitle_en': 'Robust export rebound and record FDI inflows position Vietnam as a resilient economic beacon.',
        'sourceUrl': 'https://vietnamnet.vn/en/vietnam-s-gdp-grows-9-01-nearly-triple-global-forecast-2563213.html',
        'sourceName': 'VietnamNet'
    },
    'society-8': {
        'image': 'assets/images/society/image24.jpg',
        'title': 'Tiếng Việt trong ngôi nhà Nam Phi: Hành trình người mẹ truyền lửa cội nguồn nơi đất khách',
        'title_en': 'A Vietnamese voice in a South African home',
        'subtitle': 'Nỗ lực không ngừng nghỉ gìn giữ tiếng mẹ đẻ và bản sắc quê hương cho thế hệ con cháu sinh ra và lớn lên tại châu Phi xa xôi.',
        'subtitle_en': 'A mother\'s tireless devotion teaching her children mother tongue and heritage far away in South Africa.',
        'sourceUrl': 'https://vietnamnews.vn/society/1803581/a-vietnamese-voice-in-a-south-african-home.html',
        'sourceName': 'Vietnam News'
    },
    'society-9': {
        'image': 'assets/images/society/image28.jpg',
        'title': 'Cẩm nang cho du khách lần đầu đến Việt Nam: Từ phố cổ Hà Nội đến bãi biển Phú Quốc',
        'title_en': 'Vietnam for first-timers, beach lovers and nightlife seekers: Where to go?',
        'subtitle': 'Những gợi ý hành trình đặc sắc khám phá chiều sâu lịch sử Thủ đô, ẩm thực phong phú và bờ biển ngọc ngà phương Nam.',
        'subtitle_en': 'Curated travel highlights revealing centuries of rich history, world-renowned street food, and emerald beaches.',
        'sourceUrl': 'https://news.tuoitre.vn/vietnam-for-first-timers-beach-lovers-and-nightlife-seekers-where-to-go-103261022142743028.htm',
        'sourceName': 'Tuổi Trẻ News'
    },
    'society-10': {
        'image': 'assets/images/society/image31.jpg',
        'title': 'Bên trong ngôi biệt thự trăm tuổi hình chữ Khẩu của đại gia phố cổ Hàng Bè',
        'title_en': 'Inside Hanoi tycoon’s 100-year-old villa in the Old Quarter',
        'subtitle': 'Công trình kiến trúc độc bản kết hợp nét thanh lịch Đông Dương và phong thủy truyền thống gìn giữ ký ức vàng son Thăng Long.',
        'subtitle_en': 'An extraordinary historic residence harmonizing Indochinese refinement with traditional feng shui in the Old Quarter.',
        'sourceUrl': 'https://e.vnexpress.net/photo/trend/inside-hanoi-tycoons-100-year-old-villa-in-the-old-quarter-5140151.html',
        'sourceName': 'VnExpress International'
    },
    'society-11': {
        'image': 'assets/images/society/telemedicine_remote_doctor.jpg',
        'title': 'Chuyển đổi số y tế cơ sở: Bác sĩ vùng cao chẩn đoán bệnh từ xa qua hệ thống Telemedicine',
        'title_en': 'Primary Healthcare Digitalization: Remote Highland Clinics Connected via Telemedicine',
        'subtitle': 'Sự kết nối trực tuyến với các bệnh viện tuyến trung ương giúp cứu sống kịp thời nhiều ca bệnh hiểm nghèo tại các bản làng xa xôi.',
        'subtitle_en': 'High-speed remote clinical connections with central medical institutes save critical lives in isolated mountain communes.'
    },
    'society-12': {
        'image': 'assets/images/society/mekong_saline_adaptation.jpg',
        'title': 'Thích ứng biến đổi khí hậu: Nông dân Bến Tre chuyển đổi sinh kế thành công trước đợt hạn mặn lịch sử',
        'title_en': 'Climate Adaptation in the Mekong Delta: Ben Tre Farmers Thriving Amid Historic Saline Tides',
        'subtitle': 'Mô hình xen canh tôm - lúa và vườn cây ăn trái thích ứng mặn giúp nông dân làm giàu bền vững trên chính mảnh đất quê hương.',
        'subtitle_en': 'Saline-resilient crop rotation and shrimp-rice systems turn climate headwinds into sustainable local prosperity.'
    },
    'society-13': {
        'image': 'assets/images/society/highland_mobile_library.jpg',
        'title': 'Thư viện cộng đồng vùng cao: Những chuyến xe sách vượt đèo gieo mầm tri thức cho trẻ em bản nghèo',
        'title_en': 'Highland Mobile Libraries: Books Crossing Mountain Passes to Nurture Children\'s Dreams',
        'subtitle': 'Hàng nghìn đầu sách tranh, truyện thiếu nhi và kiến thức khoa học được đưa đến tận tay các em nhỏ vùng biên giới.',
        'subtitle_en': 'Thousands of illustrated storybooks and science encyclopedias delivered to eager children along border frontiers.'
    },
    'society-14': {
        'image': 'assets/images/society/community_safe_shelter.jpg',
        'title': 'Mạng lưới nhà tạm lánh cộng đồng: Lá chắn bảo vệ phụ nữ và trẻ em trước nạn bạo lực gia đình',
        'title_en': 'Community Safe Havens: Protective Shelters Safeguarding Women and Children from Domestic Violence',
        'subtitle': 'Nơi cung cấp chốn ở an toàn, tư vấn tâm lý và hỗ trợ pháp lý miễn phí, giúp các nạn nhân tìm lại cuộc đời tự chủ và hạnh phúc.',
        'subtitle_en': 'Offering emergency refuge, psychological support, and legal advocacy to guide survivors toward dignity and healing.'
    },

    # ----------------- HUMAN STORIES (20) -----------------
    'human-1': {
        'image': 'assets/images/human_stories/image1.jpg',
        'title': 'Thấu hiểu nỗi cô đơn tuổi già: Khi những người trẻ chọn bước tới để trao đi sự lắng nghe',
        'title_en': '\'I wanted to make a change knowing older people suffer from loneliness\'',
        'subtitle': 'Những buổi chiều trò chuyện giản dị bên tách trà giúp xua tan sự trống trải của những người già sống một mình trong thành phố lớn.',
        'subtitle_en': 'Compassionate volunteering projects where young people listen, comfort, and stand alongside isolated seniors.',
        'sourceUrl': 'https://www.theguardian.com/voluntary-sector-network/2018/jun/04/volunteering-older-people-loneliness-isolation',
        'sourceName': 'The Guardian'
    },
    'human-2': {
        'image': 'assets/images/human_stories/image11.jpg',
        'title': 'Chiếc túi ân tình: Món quà nhỏ làm thay đổi cuộc đời người cựu chiến binh vô gia cư',
        'title_en': 'Kindness Bag Changes Homeless Vet\'s Life, Now He Delivers Them on LA Streets',
        'subtitle': 'Một chiếc túi chứa vật phẩm thiết yếu và thông điệp động viên đã thắp lại ngọn lửa hy vọng, giúp anh làm lại cuộc đời và giúp đỡ người khác.',
        'subtitle_en': 'A simple care package with hygiene essentials and heartfelt notes sparks a former homeless veteran\'s mission.',
        'sourceUrl': 'https://www.goodnewsnetwork.org/kindness-bag-changes-homeless-vets-life/',
        'sourceName': 'Good News Network'
    },
    'human-3': {
        'image': 'assets/images/human_stories/image3.png',
        'title': 'Phép màu hồi sinh của chàng trai bom đạn Iraq Qusay Hussein: \'Tôi được trao cơ hội sống thứ hai\'',
        'title_en': '“I was given a second chance”: Qusay Hussein\'s miraculous survival and journey of hope',
        'subtitle': 'Mất đi đôi mắt và khuôn mặt sau vụ đánh bom thảm khốc, Qusay kiên cường vượt qua 50 cuộc phẫu thuật để trở thành diễn giả truyền cảm hứng.',
        'subtitle_en': 'Surviving devastating suicide blast injuries and blindness, Qusay Hussein endures 50 surgeries to become an inspirational speaker.',
        'sourceUrl': 'https://www.theguardian.com/lifeandstyle/2019/nov/03/i-was-given-a-second-chance-six-amazing-people-describe-their-life-changes',
        'sourceName': 'The Guardian / MSF'
    },
    'human-4': {
        'image': 'assets/images/human_stories/image7.png',
        'title': 'Nghĩa cử hào hiệp: Những nông dân thiện nguyện gây quỹ 400.000 USD mỗi năm cho học sinh nghèo',
        'title_en': 'These volunteer farmers raise $400,000 each year for teens going to college',
        'subtitle': 'Tại thị trấn Gruver, Texas, toàn bộ cộng đồng nông dân chung tay canh tác 360 mẫu đất nông nghiệp để mọi học sinh tốt nghiệp đều có học bổng đại học.',
        'subtitle_en': 'In Gruver, Texas, an entire farming town pools labor and land across 360 acres so every graduating senior affords college.',
        'sourceUrl': 'https://www.washingtonpost.com/lifestyle/2023/11/02/gruver-farm-scholarship-texas/',
        'sourceName': 'The Washington Post'
    },
    'human-5': {
        'image': 'assets/images/human_stories/mountain_teacher_trail.jpg',
        'title': 'Thầy giáo cõng chữ lên đỉnh Ngọc Linh: 15 năm kiên trì thắp sáng tương lai học trò vùng cao',
        'title_en': 'Carrying Literacy up Mount Ngoc Linh: A Highland Teacher\'s 15-Year Devotion to Mountain Children',
        'subtitle': 'Băng qua những cung đường sạt lở mùa mưa bão, thầy giáo trẻ cắm bản mang con chữ và tình thương sưởi ấm những đôi chân trần trên núi.',
        'subtitle_en': 'Trekking treacherous muddy slopes during monsoon floods to bring education and warmth to barefoot highland pupils.'
    },
    'human-6': {
        'image': 'assets/images/human_stories/emotional_family_reunion.jpg',
        'title': 'Hành trình 15 năm tìm con thất lạc: Phép màu từ tình thương và mạng xã hội',
        'title_en': 'A Mother\'s 15-Year Search for Her Lost Son: A Heartbreaking Miracle of Unfailing Love',
        'subtitle': 'Không một ngày nào người mẹ thôi hy vọng, và điều kỳ diệu đã đến khi tấm ảnh đăng trên mạng xã hội kết nối lại hai số phận.',
        'subtitle_en': 'Never losing hope for a single day, an agonizing search ends in tears of joy when a social media post reconnects family.'
    },
    'human-7': {
        'image': 'assets/images/human_stories/charity_soup_kitchen.jpg',
        'title': 'Quán cơm 0 đồng bên cổng bệnh viện: Bữa ăn nóng hổi và điểm tựa ấm áp cho bệnh nhân nghèo',
        'title_en': 'The Zero-Dong Charity Kitchen: Free Warm Meals Fueling Hope for Impoverished Patients',
        'subtitle': 'Mỗi trưa, hàng trăm suất cơm thơm ngon, đủ chất được trao tận tay những gia đình đang gồng mình chống chọi với bạo bệnh.',
        'subtitle_en': 'Hundreds of steaming, nutritious lunches handed daily to exhausted relatives battling critical illnesses.'
    },
    'human-8': {
        'image': 'assets/images/human_stories/forest_ranger_patrol.jpg',
        'title': 'Người gác rừng Cát Tiên: Cuộc chiến thầm lặng ngày đêm bảo vệ lá phổi xanh của Tổ quốc',
        'title_en': 'The Silent Guardians of Cat Tien: Rangers Risking Lives to Shield Ancient Primeval Forests',
        'subtitle': 'Đối mặt với hiểm nguy giữa rừng thiêng nước độc, những người kiểm lâm kiên gan giữ trọn từng gốc cây cổ thụ và đàn thú quý.',
        'subtitle_en': 'Facing poachers and harsh wilderness to fiercely protect millennial trees and endangered wildlife biodiversity.'
    },
    'video-8': {
        'image': 'assets/images/human_stories/creative_culinary_bento.jpg',
        'title': 'Người mẹ Hà Nội biến bữa cơm gia đình thành tác phẩm nghệ thuật truyền cảm hứng',
        'title_en': 'Mother Turns Meals into Art: Creative Culinary Storytelling Inspiring Hanoi Families',
        'subtitle': 'Bằng nguyên liệu rau củ mộc mạc, chị khéo léo tạo hình những bức tranh ẩm thực sinh động, giúp các con hào hứng ăn uống lành mạnh.',
        'subtitle_en': 'Transforming everyday ingredients into colorful visual art, inspiring mindful nutrition and joyful family bonding.',
        'sourceUrl': 'https://vietnamtoday.vtv.vn/mother-turns-meals-into-art-100260710095813651.htm',
        'sourceName': 'VTV Vietnam Today'
    },
    'video-11': {
        'image': 'assets/images/human_stories/extraordinary_mother_love.jpg',
        'title': 'Những người mẹ phi thường, tình yêu phi thường: Vượt giông bão cuộc đời nuôi con khôn lớn',
        'title_en': 'Extraordinary Mothers, Extraordinary Love: Boundless Resilience in the Face of Life\'s Tempest',
        'subtitle': 'Tôn vinh tình mẫu tử thiêng liêng và nghị lực phi thường của những người mẹ kiên cường vượt qua mọi nghịch cảnh bệnh tật.',
        'subtitle_en': 'Honoring the boundless devotion and strength of mothers whose unique journeys require extraordinary resilience.',
        'sourceUrl': 'https://vietnamtoday.vtv.vn/extraordinary-mothers-extraordinary-love-10026051107442239.htm',
        'sourceName': 'VTV Vietnam Today'
    },
    'human-9': {
        'image': 'assets/images/human_stories/image22.jpg',
        'title': 'Món quà vận động cho 1,5 triệu mảnh đời: Hành trình thắp sáng tự do cho người khuyết tật nghèo',
        'title_en': 'On World Kindness Day, how one nonprofit has given the gift of mobility to 1.5 million people',
        'subtitle': 'Tổ chức phi lợi nhuận Free Wheelchair Mission đã trao tặng 1,5 triệu chiếc xe lăn tại 95 quốc gia, giúp những người bại liệt tự chủ cuộc sống.',
        'subtitle_en': 'Free Wheelchair Mission delivers 1.5 million wheelchairs across 95 nations, restoring freedom, mobility, and dignity.',
        'sourceUrl': 'https://abcnews.com/video/127480629/',
        'sourceName': 'ABC News'
    },
    'human-10': {
        'image': 'assets/images/human_stories/image26.jpg',
        'title': 'Ánh sáng điện lưới về bản xa: Hơn 1.500 đồng bào dân tộc thiểu số đổi đời',
        'title_en': 'Stable electricity brings light to homes in remote village',
        'subtitle': 'Dự án đưa điện lưới quốc gia vượt đèo dốc về với hơn 400 hộ dân bản nghèo thắp sáng ước mơ học hành và phát triển kinh tế gia đình.',
        'subtitle_en': 'Extending the national electric grid across rugged gorges transforms over 400 households in isolated mountain hamlets.',
        'sourceUrl': 'https://vietnamnews.vn/society/1803487/stable-electricity-brings-light-to-homes-in-remote-village.html',
        'sourceName': 'Vietnam News'
    },
    'human-11': {
        'image': 'assets/images/human_stories/disabled_mentor_teaching.jpg',
        'title': 'Thầy giáo khuyết tật thắp lửa lập trình cho hàng trăm bạn trẻ khó khăn',
        'title_en': 'Paralyzed Coding Mentor Empowering Hundreds of Underprivileged Youth to Code Their Futures',
        'subtitle': 'Vượt lên nghịch cảnh ngồi xe lăn, anh mở lớp dạy lập trình miễn phí giúp học sinh nghèo có việc làm ổn định trong ngành công nghệ.',
        'subtitle_en': 'Teaching free software engineering skills from a wheelchair, opening pathways into tech for disadvantaged youths.'
    },
    'human-12': {
        'image': 'assets/images/human_stories/flood_rescue_volunteers.jpg',
        'title': 'Đội thuyền cứu hộ của những ngư dân miền Trung: Băng qua tâm lũ dữ cứu người',
        'title_en': 'The Fisherman Flotilla of Central Vietnam: Braving Raging Floodwaters to Rescue Stranded Lives',
        'subtitle': 'Không quản ngại hiểm nguy, những ngư dân biển chất cano lên xe tải lao vào tâm lũ cứu sống hàng trăm người già và trẻ nhỏ mắc kẹt.',
        'subtitle_en': 'Coastal fishermen haul motorboats inland into raging flood torrents, rescuing hundreds trapped on submerged roofs.'
    },
    'human-13': {
        'image': 'assets/images/human_stories/night_street_classroom.jpg',
        'title': 'Lớp học chữ miễn phí dưới ánh đèn đường: 18 năm gieo hy vọng cho trẻ em lao động nghèo',
        'title_en': 'Free Sidewalk Evening School: 18 Years Sowing Seeds of Hope for Child Laborers in the City',
        'subtitle': 'Sau một ngày mưu sinh bán vé số, nhặt ve chai, những đứa trẻ nghèo lại quây quần bên góc bảng con để học từng con chữ, phép tính.',
        'subtitle_en': 'After selling lottery tickets by day, underprivileged street children gather under streetlights to learn reading.'
    },
    'human-14': {
        'image': 'assets/images/human_stories/free_volunteer_ambulance.jpg',
        'title': 'Chuyến xe cứu thương 0 đồng của người tài xế cựu binh miền Tây',
        'title_en': 'The Zero-Dong Ambulance: Veteran Driver’s 12-Year Mission Rushing Patients to Emergency Rooms',
        'subtitle': 'Bất kể nửa đêm hay mưa bão, hễ nghe chuông điện thoại là ông lại nổ máy chở bệnh nhân nghèo lên bệnh viện tuyến trên kịp thời.',
        'subtitle_en': 'On call day and night through monsoons, an elderly veteran rushes destitute emergency patients to hospitals for free.'
    },
    'human-15': {
        'image': 'assets/images/human_stories/elderly_land_donors.jpg',
        'title': 'Cặp vợ chồng U70 và hành trình hiến đất mở đường, dựng trường cho trẻ em nghèo',
        'title_en': 'The Generous Octogenarians Donating Family Land to Build Mountain Classrooms',
        'subtitle': 'Từ bỏ mảnh đất hương hỏa trị giá bạc tỷ, hai ông bà chỉ mong các cháu nhỏ trong bản có con đường nhựa và ngôi trường khang trang.',
        'subtitle_en': 'Gifting prime ancestral land worth fortunes so local highland pupils could have a paved road and brick school.'
    },
    'human-16': {
        'image': 'assets/images/human_stories/cerebral_palsy_scholar.jpg',
        'title': 'Nghị lực của cô gái bại não trở thành dịch giả sách truyền cảm hứng',
        'title_en': 'Cerebral Palsy Scholar Translating Inspirational Books to Empower Youth',
        'subtitle': 'Chỉ cử động được hai ngón tay, cô kiên trì gõ từng ký tự suốt nhiều năm để cho ra đời những cuốn sách gieo niềm tin vào cuộc sống.',
        'subtitle_en': 'Typing letter by letter with only two movable fingers, she translates uplifting international literature.'
    },
    'human-17': {
        'image': 'assets/images/human_stories/heirloom_rice_engineer.jpg',
        'title': 'Chàng kỹ sư bỏ phố về làng tái sinh giống lúa cổ bản địa của ông cha',
        'title_en': 'Agronomist Leaves Corporate City Life to Revive Ancient Ancestral Heirloom Rice Grains',
        'subtitle': 'Hành trình lặn lội tìm lại những hạt giống lúa nương thuần chủng thơm nức, khôi phục phương thức canh tác hữu cơ bền vững.',
        'subtitle_en': 'Rescuing pure heirloom mountain paddy seeds, proving ecological organic cultivation preserves biodiversity.'
    },
    'human-18': {
        'image': 'assets/images/human_stories/elderly_bike_repair.jpg',
        'title': 'Bà lão 80 tuổi vá xe miễn phí cho sinh viên và người lao động nghèo trên phố Hà Nội',
        'title_en': '80-Year-Old Grandma Repairing Bicycles for Free to Aid Struggling Students and Laborers',
        'subtitle': 'Bên góc ngã tư rợp bóng xà cừ, chiếc bơm tay và hộp vá xe của bà lão đã sưởi ấm biết bao chuyến xe mưu sinh nhọc nhằn.',
        'subtitle_en': 'With worn hands and a hand-pump on a shaded street corner, an 80-year-old fixes tires for struggling poor workers.'
    },

    # ----------------- MIND & SOUL (20) -----------------
    'mind-1': {
        'image': 'assets/images/mind_&_soul/image2.jpg',
        'title': 'Sau concert Mỹ Đình, Taeyang (BigBang) liên tục nhắc đến phở và \'show tuyệt nhất\'',
        'title_en': 'After My Dinh concert, BigBang\'s Taeyang praises Vietnamese pho and calls it \'the best show\'',
        'subtitle': 'Giọng ca chính của BigBang chia sẻ tình yêu nồng nhiệt với ẩm thực Việt và xúc động trước tình cảm chân thành của hàng chục nghìn khán giả.',
        'subtitle_en': 'BigBang\'s main vocalist expresses heartfelt gratitude for Vietnamese fans and celebrates pho culinary comfort.',
        'sourceUrl': 'https://news.laodong.vn/van-hoa-giai-tri/sau-concert-my-dinh-taeyang-bigbang-lien-tuc-nhac-den-pho-va-show-tuyet-voi-nhat-1791777.ldo',
        'sourceName': 'Báo Lao Động'
    },
    'mind-2': {
        'image': 'assets/images/mind_&_soul/image5.jpg',
        'title': 'Megan Thee Stallion: Biến hóa huyền ảo mùa Halloween và câu chuyện chữa lành qua sáng tạo',
        'title_en': 'The story behind Megan Thee Stallion’s elaborately spooky Halloween costume',
        'subtitle': 'Nghệ thuật hóa trang không chỉ là vẻ bề ngoài mà còn là cách người nghệ sĩ giải phóng năng lượng sáng tạo và tìm lại sự tự tin.',
        'subtitle_en': 'Elaborate costume design becomes a transformative medium for creative catharsis and reclaiming self-confidence.',
        'sourceUrl': 'https://edition.cnn.com/2026/11/01/entertainment/megan-thee-stallion-halloween-costume',
        'sourceName': 'CNN'
    },
    'mind-3': {
        'image': 'assets/images/mind_&_soul/image9.jpg',
        'title': 'So sánh dinh dưỡng giữa sữa yến mạch và sữa bò: Lợi ích và những lưu ý cho sức khỏe',
        'title_en': 'Oat vs. dairy milk: Nutrition, benefits, and downsides',
        'subtitle': 'Phân tích khoa học từ chuyên gia dinh dưỡng Harvard giúp bạn lắng nghe cơ thể để lựa chọn nguồn dinh dưỡng phù hợp nhất.',
        'subtitle_en': 'Rigorous nutritional insights from Harvard Health guiding mindful dietary choices for body wellness.',
        'sourceUrl': 'https://www.health.harvard.edu/diet-and-nutrition/oat-vs-dairy-milk-nutrition-benefits-and-downsides',
        'sourceName': 'Harvard Health'
    },
    'mind-4': {
        'image': 'assets/images/mind_&_soul/slow_living_peace.jpg',
        'title': 'Nghệ thuật sống chậm (Slow Living): Ngắt kết nối với màn hình để tìm lại sự an yên đích thực',
        'title_en': 'The Art of Slow Living: Disconnecting from Screens to Reclaim Mindful Serenity',
        'subtitle': 'Một buổi sáng không điện thoại, chỉ có trang sách giấy và làn gió mát bên hiên nhà giúp phục hồi năng lượng tinh thần kỳ diệu.',
        'subtitle_en': 'Screen-free morning stillness, a printed novel, and fresh air restore depleted inner vitality.'
    },
    'mind-5': {
        'image': 'assets/images/mind_&_soul/tay_nguyen_gong_ceremony.jpg',
        'title': 'Sức mạnh chữa lành của tiếng cồng chiêng: Đưa tâm thức hòa nhịp cùng đại ngàn Tây Nguyên',
        'title_en': 'Healing Resonance of Sacred Gongs: Aligning the Spirit with the Whispering Central Highlands',
        'subtitle': 'Tần số âm thanh vang vọng từ những chiếc chiêng đồng cổ bên bếp lửa nhà rông xua tan lo âu và kết nối con người với vũ trụ.',
        'subtitle_en': 'Acoustic resonance from bronze gongs around communal fires dissolves modern anxieties, grounding the soul in nature.'
    },
    'mind-6': {
        'image': 'assets/images/mind_&_soul/park_violin_community.jpg',
        'title': '10 năm lớp học vĩ cầm miễn phí giữa lòng công viên TP.HCM: Gieo nốt nhạc bình an',
        'title_en': '10 Years of Free Violin Lessons in the Park: Harmonizing Community Souls in Ho Chi Minh City',
        'subtitle': 'Tiếng đàn réo rắt dưới bóng cây râm mát mở ra không gian văn hóa nghệ thuật đại chúng, đưa âm nhạc cổ điển đến gần mọi người.',
        'subtitle_en': 'String melodies floating beneath canopy trees democratize classical music, offering community solace.'
    },
    'video-5': {
        'image': 'assets/images/mind_&_soul/inclusive_theatre_stage.jpg',
        'title': 'Sân khấu dành cho mọi tiếng nói: Nghệ thuật biểu cảm dung nạp và hòa nhập cộng đồng',
        'title_en': 'A Stage for Every Voice: Inclusive Theatre and Creative Expression Uplifting the Disabled',
        'subtitle': 'Đối với các nghệ sĩ khuyết tật, con đường bước lên sân khấu mang lại tiếng nói bình đẳng, nơi cảm xúc được thăng hoa trọn vẹn.',
        'subtitle_en': 'Inclusive theatrical production places collaborative artistic empowerment and disabled talent centre stage.',
        'sourceUrl': 'https://vietnamtoday.vtv.vn/a-stage-for-every-voice-100261029064303631.htm',
        'sourceName': 'VTV Vietnam Today'
    },
    'video-6': {
        'image': 'assets/images/mind_&_soul/image7.jpg',
        'title': '10 năm lớp học vĩ cầm miễn phí giữa lòng công viên TP.HCM: Phóng sự VTV',
        'title_en': '10 years of free violin lessons in park: Harmonizing Community Souls',
        'subtitle': 'Lớp học vĩ cầm miễn phí suốt một thập kỷ giữa công viên TP.HCM gieo niềm đam mê âm nhạc cổ điển vào trái tim của hàng trăm bạn trẻ.',
        'subtitle_en': 'A decade of bringing free violin coaching to open city parks proves music is a universal healing language.',
        'sourceUrl': 'https://vietnamtoday.vtv.vn/10-years-of-free-violin-lessons-in-park-100261029064839361.htm',
        'sourceName': 'VTV Vietnam Today'
    },
    'video-9': {
        'image': 'assets/images/mind_&_soul/healing_oasis_sanctuary.jpg',
        'title': 'Ốc đảo chữa lành tâm hồn hoàn toàn miễn phí tại TP. Hồ Chí Minh: Nơi trú ẩn bình an',
        'title_en': 'A Healing Oasis in Ho Chi Minh City: A Sanctuary for Inner Peace Open to All',
        'subtitle': 'Không gian chăm sóc sức khỏe tinh thần hoàn toàn miễn phí tại TP.HCM giúp mọi người tìm lại sự an yên và cân bằng sau những áp lực.',
        'subtitle_en': 'A community-based mindfulness centre offering tranquil mental spa retreats completely free of charge.',
        'sourceUrl': 'https://vietnamtoday.vtv.vn/a-healing-oasis-in-ho-chi-minh-city-100260910032153068.htm',
        'sourceName': 'VTV Vietnam Today'
    },
    'mind-7': {
        'image': 'assets/images/mind_&_soul/steamed_banh_cuon_delight.jpg',
        'title': 'Bánh cuốn Tây Hồ 60 năm gìn giữ phong vị xưa: Một góc ẩm thực tinh tế nuôi dưỡng hoài niệm',
        'title_en': 'Michelin-Honored Saigon Eatery Serves Banh Cuon with an Unbroken Touch of Tradition',
        'subtitle': 'Từng lớp bánh mỏng mướt tráng tay, hành phi thơm nức và chén nước mắm thanh tao gợi nhớ ký ức bữa sáng ấm áp bên người thân.',
        'subtitle_en': 'Delicate hand-steamed rice rolls sprinkled with golden fried shallots evoke warm nostalgic breakfast memories.',
        'sourceUrl': 'https://vietnamnet.vn/en/michelin-honored-saigon-eatery-serves-banh-cuon-with-a-touch-of-tradition-2566799.html',
        'sourceName': 'VietnamNet'
    },
    'mind-8': {
        'image': 'assets/images/mind_&_soul/shinrin_yoku_forest_bath.jpg',
        'title': 'Tắm rừng Ba Vì (Shinrin-yoku): Nghệ thuật hòa mình vào thiên nhiên thanh lọc tâm trí',
        'title_en': 'Ba Vi Forest Bathing (Shinrin-yoku): Immersing in Pristine Greenery to Purify the Weary Mind',
        'subtitle': 'Hít thở hợp chất phytoncide tự nhiên tỏa ra từ rừng thông giúp giảm hormone căng thẳng cortisol và tái tạo hệ miễn dịch.',
        'subtitle_en': 'Inhaling natural tree phytoncides deep in mountain pine woods dramatically reduces stress hormone cortisol.'
    },
    'mind-9': {
        'image': 'assets/images/mind_&_soul/therapeutic_journaling.jpg',
        'title': 'Viết nhật ký trị liệu: Phương pháp đặt bút trút bỏ gánh nặng tinh thần và kết nối nội tâm',
        'title_en': 'Therapeutic Journaling: Writing Down Thoughts to Release Emotional Burdens and Heal',
        'subtitle': 'Khi cảm xúc tiêu cực được gọi tên trên trang giấy trắng, tâm trí sẽ tự tìm lại trật tự và sự thấu suốt nhẹ nhõm.',
        'subtitle_en': 'Naming raw emotions on blank paper untangles cognitive rumination and restores emotional clarity.'
    },
    'mind-10': {
        'image': 'assets/images/mind_&_soul/shan_tuyet_ancient_tea.jpg',
        'title': 'Thiền trà Shan Tuyết trên đỉnh Chiêu Lầu Thi: Thưởng một chén trà, buông vạn nỗi ưu phiền',
        'title_en': 'Shan Tuyet Tea Meditation on Chieu Lau Thi Peak: Sip Solace, Release Worldly Turmoil',
        'subtitle': 'Hương vị chát dịu, hậu ngọt sâu của búp trà tuyết cổ thụ hàng trăm năm tuổi đưa người thưởng thức về với thực tại an nhiên.',
        'subtitle_en': 'Centuries-old wild mountain tea buds brewed in misty heights anchor the soul in calm presence.'
    },
    'mind-11': {
        'image': 'assets/images/mind_&_soul/creative_rest_recovery.jpg',
        'title': 'Vượt qua kiệt sức sáng tạo: Tại sao cho phép bản thân được nghỉ ngơi là một đặc ân cần thiết',
        'title_en': 'Overcoming Creative Burnout: Why Granting Yourself Stillness Is an Essential Sacred Act',
        'subtitle': 'Ngưng tạo áp lực phải luôn năng suất; đôi khi sự im lặng và những ngày lười biếng lại là mảnh đất ươm mầm cho ý tưởng vĩ đại.',
        'subtitle_en': 'Relinquishing toxic productivity traps; intentional stillness provides fertile ground for genuine creative rebirth.'
    },
    'mind-12': {
        'image': 'assets/images/mind_&_soul/ancient_lithophone_stones.jpg',
        'title': 'Âm vang đàn đá ngàn năm: Liệu pháp chữa lành tâm hồn bằng tần số âm thanh cổ xưa',
        'title_en': 'Echoes of Ancient Lithophones: Sound Therapy Vibrations from Millennia-Old Musical Stones',
        'subtitle': 'Những phiến đá trầm tích ngàn năm tuổi khi được gõ lên tạo ra rung động âm thanh nguyên thủy có khả năng điều hòa sóng não.',
        'subtitle_en': 'Primordial sound vibrations resonating from ancient resonant stone bars restore harmonic brainwave states.'
    },
    'mind-13': {
        'image': 'assets/images/mind_&_soul/danshari_minimalism.jpg',
        'title': 'Triết lý sống tối giản Danshari: Dọn dẹp không gian sống để giải phóng những vướng bận trong lòng',
        'title_en': 'Danshari Minimalism: Decluttering Your Physical Space to Liberate Your Inner Mind',
        'subtitle': 'Học cách từ bỏ những đồ vật không còn hữu ích là bài học sâu sắc để buông xả những chấp niệm và gánh nặng quá khứ.',
        'subtitle_en': 'Letting go of redundant physical clutter mirrors a profound internal release of emotional attachments.'
    },
    'mind-14': {
        'image': 'assets/images/mind_&_soul/hand_embroidery_art.jpg',
        'title': 'Nghệ thuật thêu tay truyền thống: Liệu pháp tĩnh tâm tìm lại sự tập trung qua từng đường kim mũi chỉ',
        'title_en': 'Traditional Hand Embroidery Therapy: Restoring Inner Focus One Mindful Stitch at a Time',
        'subtitle': 'Chuyển động nhịp nhàng của mũi kim luồn qua sợi chỉ màu sắc tạo nên trạng thái thiền định tự nhiên, xua tan căng thẳng.',
        'subtitle_en': 'Rhythmic hand stitching through silk canvas triggers deep active meditation, gently dissolving anxiety.'
    },
    'mind-15': {
        'image': 'assets/images/mind_&_soul/self_compassion_peace.jpg',
        'title': 'Học cách bao dung với chính mình: Thoát khỏi cái bẫy của chủ nghĩa hoàn hảo và những lời phán xét',
        'title_en': 'Practicing Self-Compassion: Breaking Free from the Toxic Trap of Unrelenting Perfectionism',
        'subtitle': 'Thay vì tự trách móc những sai lầm, hãy đối xử với bản thân bằng sự dịu dàng như cách bạn an ủi một người bạn thân thiết.',
        'subtitle_en': 'Replacing punitive internal self-criticism with gentle empathy, treating yourself as your dearest companion.'
    },
    'mind-16': {
        'image': 'assets/images/mind_&_soul/mindful_pottery_wheel.jpg',
        'title': 'Nghệ thuật gốm vuốt tay: Cảm nhận sự gắn kết với đất mẹ qua từng chuyển động của đôi bàn tay',
        'title_en': 'Mindful Hand-Thrown Pottery: Feeling Deep Oneness with Earth on the Spinning Wheel',
        'subtitle': 'Cảm giác chạm vào thớ đất sét ẩm mịn và nắn vuốt từng đường cong giúp tâm trí buông bỏ suy nghĩ vẩn vơ, neo chặt vào hiện tại.',
        'subtitle_en': 'Tactile immersion in cool spinning clay grounds wandering thoughts firmly in physical presence.'
    },
    'mind-17': {
        'image': 'assets/images/mind_&_soul/aromatherapy_natural_scent.jpg',
        'title': 'Chữa lành bằng hương thơm tự nhiên: Liệu pháp tinh dầu trầm hương và hoa bưởi thanh khiết',
        'title_en': 'Aromatherapy with Native Scents: Calming the Nervous System with Agarwood and Pomelo Blossoms',
        'subtitle': 'Hương thơm mộc mạc của hoa cỏ quê nhà kích hoạt khứu giác, xoa dịu hệ thần kinh và đưa giấc ngủ về trong êm đềm.',
        'subtitle_en': 'Natural ancestral scents of pomelo blossoms and agarwood soothe overstimulated nervous systems into deep sleep.'
    },
    'mind-20': {
        'image': 'assets/images/mind_&_soul/image13.jpg',
        'title': 'Đêm đấm bốc của những người phụ nữ từng bị bạo hành: Nơi lấy lại tự tin và sức mạnh bản thân',
        'title_en': 'The women\'s boxing nights helping abuse survivors reclaim courage and dignity',
        'subtitle': 'Trên võ đài, những cú đấm dứt khoát không phải để tấn công mà để giải phóng nỗi sợ hãi, khơi dậy ý chí kiên cường ẩn sâu bên trong.',
        'subtitle_en': 'Inside the boxing ring, survivors release trauma and fear, forging physical empowerment and renewed dignity.',
        'sourceUrl': 'https://www.positive.news/society/the-womens-boxing-nights-helping-abuse-survivors/',
        'sourceName': 'Positive News'
    },

    # ----------------- IN-DEPTH (20) -----------------
    'indepth-1': {
        'image': 'assets/images/in-dept/image2.jpg',
        'title': 'Hà Nội không bao giờ ngừng chảy: Hương hoa sữa và ký ức rêu phong giữa dòng đời hối hả',
        'title_en': 'A Hà Nội that never stands still',
        'subtitle': 'Tản văn sâu lắng về một Thủ đô giao thoa giữa nhịp sống hiện đại hối hả và những góc phố rêu phong tĩnh lặng đọng hương kỷ niệm.',
        'subtitle_en': 'An evocative essay capturing the timeless rhythm of Hanoi where modernity blends seamlessly with ancient lanes.',
        'sourceUrl': 'https://vietnamnews.vn/talk-around-town/1802722/a-ha-noi-that-never-stands-still.html',
        'sourceName': 'Vietnam News'
    },
    'indepth-2': {
        'image': 'assets/images/in-dept/image1.jpg',
        'title': 'Đối diện với căn bệnh Parkinson: Rhys Ifans và Laura Linney chia sẻ về nghệ thuật và lòng dũng cảm',
        'title_en': 'Rhys Ifans and Laura Linney on Parkinson’s: Acting, Humor, and Defying Vulnerability',
        'subtitle': 'Cuộc phỏng vấn độc quyền hé lộ cách hai diễn viên tài danh dùng sân khấu để phơi bày sự mong manh của số phận với lòng trắc ẩn.',
        'subtitle_en': 'An exclusive interview on how transformative theatre embraces physical vulnerability and Parkinson\'s with courage.',
        'sourceUrl': 'https://www.theguardian.com/film/2026/nov/02/rhys-ifans-laura-linney-onwards-sideways-film-interview-parkinsons-paul-mayhew-archer',
        'sourceName': 'The Guardian'
    },
    'indepth-3': {
        'image': 'assets/images/in-dept/image3.jpg',
        'title': 'Những nhà giáo dục dùng khoa học dạy lòng trắc ẩn: Khi sự tử tế trở thành môn học chính khóa',
        'title_en': 'Meet the educators using science to teach kindness',
        'subtitle': 'Các nghiên cứu thần kinh học chứng minh rằng lòng vị tha có thể rèn luyện như một khối cơ, giúp trẻ em xây dựng khả năng thấu cảm.',
        'subtitle_en': 'Neuroscience proves empathy is an trainable cognitive skill, transforming school culture through proactive kindness.',
        'sourceUrl': 'https://www.positive.news/society/meet-the-educators-using-science-to-teach-kindness/',
        'sourceName': 'Positive News'
    },
    'indepth-4': {
        'image': 'assets/images/in-dept/image4.jpg',
        'title': 'Ba con người chọn gắn đời mình với thiên nhiên hoang dã: Sứ mệnh bảo vệ sự sống hành tinh',
        'title_en': 'Three people who have jobs in nature: Devoted Custodians of Planetary Life',
        'subtitle': 'Từ đáy đại dương đến đỉnh núi cao, những chuyên gia bảo tồn thầm lặng cống hiến tuổi xuân để giữ lại màu xanh cho muôn loài.',
        'subtitle_en': 'Dedicated conservationists share what it truly means to devote life to restoring natural ecosystems.',
        'sourceUrl': 'https://www.positive.news/environment/three-people-who-have-jobs-in-nature/',
        'sourceName': 'Positive News'
    },
    'indepth-5': {
        'image': 'assets/images/in-dept/image8.jpg',
        'title': 'Rory Kinnear và nỗi đau mất cha: Nghệ thuật giúp tôi hàn gắn vết thương sau bi kịch cuộc đời',
        'title_en': 'Rory Kinnear on father Roy\'s death: Grief, Memory, and the Catharsis of Performance',
        'subtitle': 'Những dòng tâm sự gan ruột của nam diễn viên gạo cội về cách chuyển hóa nỗi mất mát to lớn thành sức mạnh nội tâm trên sân khấu.',
        'subtitle_en': 'A profound personal essay on channeling raw childhood grief into emotional truth and artistic authenticity.',
        'sourceUrl': 'https://www.theguardian.com/tv-and-radio/2026/nov/05/rory-kinnear-father-roy-death',
        'sourceName': 'The Guardian'
    },
    'indepth-6': {
        'image': 'assets/images/mind_&_soul/image14.jpg',
        'title': 'Bò nướng tảng Canada ướp mắc khén Tây Bắc: Giao thoa tinh tế giữa hai nền văn hóa ẩm thực',
        'title_en': 'Canadian ‘outside skirt’ beef combined with Northwest Vietnamese herb marinade',
        'subtitle': 'Sự kết hợp độc đáo giữa thớ thịt bò thượng hạng Bắc Mỹ và hạt mắc khén thơm nồng từ đại ngàn Tây Bắc tạo nên bản hòa tấu hương vị.',
        'subtitle_en': 'An innovative cross-cultural dish pairing premium Canadian beef cut with fragrant wild mac khen herbs.',
        'sourceUrl': 'https://vovworld.vn/food-delight/canadian-outside-skirt-beef-combined-with-northwest-vietnamese-herb-marinade-2468953.vov5',
        'sourceName': 'VOV World'
    },
    'indepth-7': {
        'image': 'assets/images/in-dept/hanoi_french_colonial_villa.jpg',
        'title': 'Di sản kiến trúc biệt thự Pháp cổ Hà Nội: Hành trình bảo tồn ký ức đô thị trăm năm',
        'title_en': 'Hanoi’s French Colonial Architectural Heritage: Preserving Centuries of Urban Memory',
        'subtitle': 'Những bức tường vàng rêu phong và mái ngói cổ kính là chứng nhân sống động cho sự giao thoa văn hóa Đông Dương đầy mê hoặc.',
        'subtitle_en': 'Historic yellow facades and shuttered windows bear testament to a century of fascinating Indochinese architecture.'
    },
    'indepth-8': {
        'image': 'assets/images/in-dept/vietnamese_ceramic_master.jpg',
        'title': 'Gốm cổ Chu Đậu và Bát Tràng: Khát vọng đưa tinh hoa đất Việt vươn tầm nghệ thuật thế giới',
        'title_en': 'Chu Dau and Bat Trang Ceramics: Lifting Vietnamese Clay Artistry to Global Prominence',
        'subtitle': 'Từng nét vẽ lam chàm thanh tao trên men tro trấu là sự kết tinh của tài hoa, kiên nhẫn và lòng tự tôn văn hóa dân tộc.',
        'subtitle_en': 'Cobalt brushstrokes on natural rice-husk glazes embody centuries of artisanal mastery and national cultural pride.'
    },
    'indepth-9': {
        'image': 'assets/images/in-dept/can_gio_mangrove_forest.jpg',
        'title': 'Hồi sinh rừng ngập mặn Cần Giờ: Cuộc đại kiến tạo lá chắn xanh che chở thành phố phương Nam',
        'title_en': 'Revitalizing Can Gio Mangroves: The Epic Biosphere Shield Defending Southern Megacity',
        'subtitle': 'Từ một vùng đất chết vì bom đạn và chất độc hóa học, bàn tay con người đã kiên trì hồi sinh khu dự trữ sinh quyển thế giới xanh ngút ngàn.',
        'subtitle_en': 'From defoliated wartime wasteland to a UNESCO world biosphere reserve shielding Ho Chi Minh City from tidal surges.'
    },
    'indepth-10': {
        'image': 'assets/images/in-dept/cyber_fraud_investigation.jpg',
        'title': 'Báo cáo điều tra đa tầng: Hành trình lần theo dấu vết các đường dây lừa đảo xuyên biên giới',
        'title_en': 'Multi-Tier Investigative Dossier: Tracing Transnational Cyber Fraud Syndicates',
        'subtitle': 'Vạch trần những thủ đoạn thao túng tâm lý tinh vi, các \'trại cày tiền\' công nghệ cao và cuộc chiến cam go bảo vệ tài sản công dân.',
        'subtitle_en': 'Unmasking psychological entrapment techniques and dark digital infrastructure run by transnational criminal networks.'
    },
    'indepth-11': {
        'image': 'assets/images/in-dept/van_phuc_silk_weaving.jpg',
        'title': 'Tiếng thoi đưa lụa Vạn Phúc: Nỗi niềm trăn trở của những nghệ nhân giữ hồn lụa Việt ngàn năm',
        'title_en': 'Rhythm of Van Phuc Looms: Masters Safeguarding a Millennial Heritage of Pure Silk',
        'subtitle': 'Giữa cơn lốc sợi tổng hợp công nghiệp giá rẻ, các nghệ nhân làng lụa vẫn miệt mài bên khung cửi cổ để dệt nên những dải mây óng ả.',
        'subtitle_en': 'Amid cheap synthetic imports, heritage weavers preserve antique wooden looms to produce shimmering mulberry silk.'
    },
    'indepth-12': {
        'image': 'assets/images/in-dept/community_mental_health_circle.jpg',
        'title': 'Đổi mới chăm sóc sức khỏe tâm thần tại cộng đồng: Phá bỏ định kiến và mở rộng vòng tay thấu cảm',
        'title_en': 'Reinventing Community Mental Health: Dismantling Stigma Through Inclusive Empathy',
        'subtitle': 'Mô hình nhóm hỗ trợ ngang hàng tại các khu dân cư giúp người trầm cảm, rối loạn âu lo được lắng nghe và điều trị kịp thời.',
        'subtitle_en': 'Grassroots peer-support networks dismantle societal shame, offering accessible early intervention for depression.'
    },
    'indepth-13': {
        'image': 'assets/images/in-dept/my_son_cham_sanctuary.jpg',
        'title': 'Giải mã bí ẩn gạch nung Mỹ Sơn: Ký ức rêu phong ngàn năm của vương triều Champa cổ',
        'title_en': 'Deciphering the Mystery of My Son Bricks: Millennial Memories of the Ancient Champa Realm',
        'subtitle': 'Kỹ thuật nung gạch và kết dính bằng nhựa thực vật độc nhất vô nhị vẫn là thách thức hấp dẫn đối với các nhà khoa học đương đại.',
        'subtitle_en': 'Mortarless vegetable-resin brick bonding techniques continue to intrigue archaeological scientists worldwide.'
    },
    'indepth-14': {
        'image': 'assets/images/in-dept/deepwater_container_port.jpg',
        'title': 'Địa kinh tế cảng biển nước sâu và logistics đường thủy: Đòn bẩy đưa Việt Nam thành trung tâm trung chuyển',
        'title_en': 'Deepwater Transshipment Geoeconomics: Positioning Vietnam as a Premier Maritime Hub',
        'subtitle': 'Hệ thống cảng Cái Mép - Thị Vải đón những siêu tàu mẹ quốc tế, khẳng định vai trò mắt xích chiến lược trong chuỗi cung ứng toàn cầu.',
        'subtitle_en': 'Deepwater terminals accommodating mega-containerships anchor Vietnam firmly as a vital node in global shipping.'
    },
    'indepth-15': {
        'image': 'assets/images/in-dept/medical_ai_robotics.jpg',
        'title': 'Đạo đức trí tuệ nhân tạo trong y khoa: Điểm giao thoa giữa thuật toán chính xác và lương tâm người thầy thuốc',
        'title_en': 'Ethics of Artificial Intelligence in Medicine: Where Algorithmic Precision Meets Hippocratic Conscience',
        'subtitle': 'Dù AI có thể đọc phim X-quang trong tích tắc, sự đồng cảm và trách nhiệm đạo đức của bác sĩ vẫn là giá trị không thể thay thế.',
        'subtitle_en': 'While neural networks diagnose in seconds, physician empathy and moral accountability remain utterly irreplaceable.'
    },
    'indepth-16': {
        'image': 'assets/images/in-dept/heirloom_seed_bank.jpg',
        'title': 'Ngân hàng hạt giống bản địa: Những người âm thầm gom góp tương lai lương thực của quốc gia',
        'title_en': 'Indigenous Heirloom Seed Banks: Quiet Custodians Safeguarding National Food Sovereignty',
        'subtitle': 'Những mẫu hạt lúa, ngô, đỗ cổ truyền được bảo quản lạnh cẩn mật là chìa khóa thích ứng với các dịch bệnh và biến đổi khí hậu mai sau.',
        'subtitle_en': 'Preserving native germplasm in cryogenic vaults safeguards resilient genetics against future climate crises.'
    },
    'indepth-17': {
        'image': 'assets/images/in-dept/dong_ho_folk_painting.jpg',
        'title': 'Tranh dân gian Đông Hồ: Hồn dân tộc lắng đọng trong màu điệp, giấy dó và những nét khắc mộc mạc',
        'title_en': 'Dong Ho Woodblock Folk Art: The National Soul Etched on Scallop-Shell Paper',
        'subtitle': 'Màu đen từ than rơm nếp, màu vàng từ hoa hòe và ánh điệp lấp lánh phản chiếu bức tranh đời sống tâm hồn mộc mạc của người Việt.',
        'subtitle_en': 'Natural pigments from straw charcoal, gardenia pods, and crushed scallop shells portray Vietnamese folk philosophy.'
    },
    'indepth-18': {
        'image': 'assets/images/in-dept/cat_ba_langur_conservation.jpg',
        'title': 'Cuộc chiến sinh tồn của đàn voọc Cát Bà: Nỗi trăn trở giữ lại loài linh trưởng quý hiếm trước bờ vực tuyệt chủng',
        'title_en': 'The Struggle for Survival of Cat Ba Langurs: Dedicated Wardens Shielding Earth\'s Rarest Primate',
        'subtitle': 'Chỉ còn chưa đầy 80 cá thể trên những vách đá vôi dựng đứng giữa vịnh, mỗi sự chào đời của voọc con là niềm hạnh phúc vỡ òa.',
        'subtitle_en': 'Fewer than 80 individuals survive on limestone sea cliffs; every newborn langur marks an emotional triumph for wardens.'
    },
    'indepth-19': {
        'image': 'assets/images/in-dept/hue_imperial_gastronomy.jpg',
        'title': 'Ẩm thực cung đình Huế: Triết lý âm dương sâu sắc ẩn sau những mâm yến tiệc hoàng triều một thuở',
        'title_en': 'Hue Imperial Gastronomy: Profound Yin-Yang Cosmological Philosophy Behind Ancient Royal Banquets',
        'subtitle': 'Từng món ăn dâng vua không chỉ là đỉnh cao nghệ thuật thị giác mà còn là bài thuốc điều hòa ngũ tạng theo y lý cổ truyền phương Đông.',
        'subtitle_en': 'Dynastic royal banquets fused exquisite visual sculpting with sophisticated nutritional balance.'
    },
    'indepth-20': {
        'image': 'assets/images/in-dept/han_nom_digital_archive.jpg',
        'title': 'Hành trình số hóa di sản Hán Nôm: Cuộc chạy đua thầm lặng với thời gian để lưu giữ linh hồn tiền nhân',
        'title_en': 'Digitalizing Nom and Han Archives: A Quiet Race Against Time to Rescue Ancestral Manuscripts',
        'subtitle': 'Từng trang sách dó mục mòn, từng sắc phong cổ được lau chùi cẩn trọng và quét ảnh độ phân giải cao để trường tồn cùng năm tháng.',
        'subtitle_en': 'Delicate centuries-old manuscripts cleansed and captured in ultra-high resolution to defy decay and time.'
    }
}

# 1. Load data
with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const ARTICLES_DATA = (\[[\s\S]*?\]);\s*(?:window\.|\n\w|\Z)', text)
articles = json.loads(m.group(1))

print(f"Total articles in file: {len(articles)}")
print(f"Total mappings prepared: {len(MASTER_100_MAP)}")

# 2. Apply master mapping
applied = 0
for a in articles:
    aid = a.get('id')
    if aid in MASTER_100_MAP:
        mapping = MASTER_100_MAP[aid]
        for k, v in mapping.items():
            a[k] = v
        applied += 1
    else:
        print(f"WARNING: No mapping for article ID {aid}")

print(f"Applied mapping to {applied} / {len(articles)} articles!")

# 3. Verify all image files exist and are unique
assigned_images = [a['image'] for a in articles]
unique_images = set(assigned_images)
print(f"Total assigned images: {len(assigned_images)}")
print(f"Unique images count: {len(unique_images)}")

if len(assigned_images) != len(unique_images):
    print("ERROR: Duplicate images found!")
    from collections import Counter
    c = Counter(assigned_images)
    for img, count in c.items():
        if count > 1:
            print(f"  Duplicate ({count}x): {img}")
    sys.exit(1)

# Check all images on disk
missing_files = []
for a in articles:
    p = a['image']
    if not os.path.exists(p):
        missing_files.append((a['id'], p))
    else:
        if os.path.getsize(p) < 5000:
            print(f"WARNING: File too small ({os.path.getsize(p)} bytes): {p}")

if missing_files:
    print(f"ERROR: {len(missing_files)} image files missing on disk!")
    for aid, p in missing_files:
        print(f"  [{aid}] -> {p}")
    sys.exit(1)

print("✓ All 100 images exist on disk and are 100% unique!")

# 4. Write back to js/data.js
new_json = json.dumps(articles, ensure_ascii=False, indent=2)
new_js_text = text[:m.start(1)] + new_json + text[m.end(1):]

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(new_js_text)

print("SUCCESS: js/data.js has been completely updated and verified!")
