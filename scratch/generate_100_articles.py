import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read existing data.js
with open('js/data.js', 'r', encoding='utf-8') as f:
    orig_code = f.read()

s = orig_code.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
e = orig_code.rfind('];') + 1

existing_articles = json.loads(orig_code[s:e])
existing_dict = {a['id']: a for a in existing_articles}
print(f"Existing articles in data.js: {len(existing_dict)}")

# Now define 15 new articles to reach exactly 100 (3 for each category)
new_15 = [
    # --- TRENDING (3 new: trending-18, trending-19, trending-20) ---
    {
        "id": "trending-18",
        "category": "trending",
        "categoryName": "Trending",
        "title": "Thương mại điện tử nông sản vươn ra toàn cầu: Trái sầu riêng và thanh long Việt Nam trên kệ siêu thị quốc tế",
        "title_en": "Cross-Border Agri-Commerce: Vietnamese Specialty Fruits Winning Global Supermarkets",
        "subtitle": "Direct-to-consumer cold chain logistics and cross-border digital marketplaces enable tropical fruit cooperatives to reach overseas tables within 48 hours.",
        "author": "Thu Huyen • Vietnam Agri-Trade",
        "date": "Thursday, November 5, 2026 - 10:15 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "Vietnam Agriculture Review",
        "sourceUrl": "https://nongnghiep.vn/thuong-mai-dien-tu-nong-san-xuat-khau-trai-cay-viet",
        "image": "",  # will be assigned uniquely
        "imageCaption": "Vietnamese specialty dragon fruit and durian packaged with digital traceability QR tags for international export.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "17.4K",
        "likes": 810,
        "tags": ["Agri-Commerce", "Export", "Tropical Fruits", "Innovation"],
        "content": [
            "Vietnamese premium agricultural products are undergoing a digital export renaissance, bypassing traditional intermediary layers through direct-to-retail cold chain distribution.",
            "From Tien Giang to Dak Lak, cooperative farmers utilize blockchain-verified traceability tags, assuring consumers in Tokyo, Seoul, and Paris of strict organic pesticide-free standards.",
            "“Connecting our orchards directly to international logistics platforms has doubled farmgate incomes while establishing pride in Vietnamese agricultural excellence,” shares cooperative director Nguyen Van Binh."
        ]
    },
    {
        "id": "trending-19",
        "category": "trending",
        "categoryName": "Trending",
        "title": "Thể thao điện tử (Esports) và làn sóng định danh nghề nghiệp cho người trẻ",
        "title_en": "The Professionalization of Vietnamese Esports: From Passion to Career",
        "subtitle": "With international championship victories and dedicated university academic tracks, competitive gaming is established as a legitimate creative and athletic career path.",
        "author": "Quang Minh • Youth Tech Review",
        "date": "Wednesday, November 4, 2026 - 16:50 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "GameK / Kenh14",
        "sourceUrl": "https://gamek.vn/esports-viet-nam-dinh-danh-nghe-nghiep-chuyen-nghiep",
        "image": "",
        "imageCaption": "Professional Vietnamese esports athletes competing under arena spotlights during regional finals.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "25.8K",
        "likes": 1340,
        "tags": ["Esports", "Youth Culture", "Gaming", "Digital Career"],
        "content": [
            "Once dismissed as an unproductive adolescent pastime, esports has matured into a multi-million-dollar industry in Vietnam, complete with sports science nutritionists, tactical analysts, and legal agents.",
            "Vietnamese national teams have secured gold medals at regional athletic games, while universities now offer specialized degrees in digital sports management and broadcast production.",
            "“Professional gaming demands rigorous discipline, physical endurance, and instantaneous split-second communication,” explains head coach Le Hoang."
        ]
    },
    {
        "id": "trending-20",
        "category": "trending",
        "categoryName": "Trending",
        "title": "Làn sóng âm nhạc Indie Việt: Những giai điệu mộc mạc chạm đến trái tim thế hệ trẻ",
        "title_en": "The Boom of Indie Music: Acoustic Rawness Captivating Youth across Vietnam",
        "subtitle": "Independent singer-songwriters are dominating streaming platforms with introspective lyrics, lo-fi bedroom production, and sincere vulnerability.",
        "author": "Thanh Hang • Contemporary Sound",
        "date": "Tuesday, November 3, 2026 - 20:10 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "Lao Dong Tre",
        "sourceUrl": "https://laodongtre.vn/am-nhac-indie-viet-chinh-phuc-gioi-tre",
        "image": "",
        "imageCaption": "Independent singer-songwriter performing an acoustic set in a cozy Hanoi listening room.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "29.2K",
        "likes": 1620,
        "tags": ["Indie Music", "Gen Z", "Art & Culture", "Storytelling"],
        "content": [
            "Rejecting over-commercialized formulaic pop, Vietnam's vibrant indie music scene has captured the collective emotional frequency of youth navigating urban alienation and modern romance.",
            "Equipped with simple guitars, vintage synthesisers, and genuine songwriting, artists record tracks in home bedrooms that resonate with millions on digital streaming charts.",
            "“In a fast-paced hyperconnected society, people crave unfiltered honesty,” says independent producer Vu Nam. “Indie music provides a safe harbor for unspoken emotions.”"
        ]
    },

    # --- SOCIETY (3 new: society-12, society-13, society-14) ---
    {
        "id": "society-12",
        "category": "society",
        "categoryName": "Society",
        "title": "Mô hình sinh kế thích ứng hạn mặn cho nông dân ven biển Bến Tre",
        "title_en": "Saline-Adapted Livelihoods: How Ben Tre Farmers Thrive with Giant River Prawns and Brackish Crops",
        "subtitle": "Instead of fighting rising sea tides, coastal agriculturalists are turning seasonal salinity into an economic boon through integrated shrimp-mangrove and organic date farming.",
        "author": "Vinh Thuan • Tuoi Tre Mekong",
        "date": "Wednesday, November 4, 2026 - 08:30 (GMT+7)",
        "readTime": "6 min read",
        "sourceName": "Tuổi Trẻ Đồng Bằng",
        "sourceUrl": "https://tuoitre.vn/nong-dan-ben-tre-chuyen-doi-sinh-ke-thich-ung-han-man",
        "image": "",
        "imageCaption": "Farmers tending certified organic shrimp-mangrove polyculture ponds in Ba Tri district.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "13.6K",
        "likes": 590,
        "tags": ["Mekong Delta", "Climate Adaptation", "Aquaculture", "Sustainability"],
        "content": [
            "In Ben Tre province, where freshwater shortages and saline intrusion once brought heartbreak during the dry season, farmers are embracing flexible adaptive agronomy.",
            "By alternating between salt-tolerant rice during the monsoon and black tiger shrimp during brackish months, household earnings have surged while eliminating chemical pesticide use.",
            "“We no longer curse the saltwater; we have learned to dance with the natural rhythms of the river delta,” says veteran farmer Vo Van Ut."
        ]
    },
    {
        "id": "society-13",
        "category": "society",
        "categoryName": "Society",
        "title": "Thư viện cộng đồng vùng cao: Những cuốn sách vượt đèo nuôi dưỡng ước mơ con trẻ",
        "title_en": "Mountain Pass Libraries: Mobile Reading Hubs Nurturing Highland Children's Dreams",
        "subtitle": "Volunteer educators strap book crates to motorbikes to establish 50 solar-powered reading rooms across isolated villages in Ha Giang, Son La, and Cao Bang.",
        "author": "Nguyen Hai Yen • Giao Duc Cong Dong",
        "date": "Monday, November 2, 2026 - 15:20 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "Giáo Dục Cộng Đồng",
        "sourceUrl": "https://giaoduc.net.vn/thu-vien-sach-vung-cao-gieo-uoc-mo-tre-em-ban-ngheo",
        "image": "",
        "imageCaption": "Ethnic Hmong and Dao children eagerly reading illustrated scientific encyclopedias in a village library.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "16.8K",
        "likes": 790,
        "tags": ["Reading Culture", "Highlands", "Education", "Volunteering"],
        "content": [
            "Across jagged mountain passes where internet connectivity remains sporadic, a grassroots initiative called 'Books on Stilt Houses' is igniting a passion for lifelong learning.",
            "Over 100,000 beautifully illustrated picture books, bilingual folk tales, and introductory science manuals have been transported directly to hamlet community centers.",
            "“When a child opens a book, mountain boundaries dissolve,” notes volunteer coordinator Tran Thi Mai. “They begin to imagine themselves as astronomers, doctors, and explorers.”"
        ]
    },
    {
        "id": "society-14",
        "category": "society",
        "categoryName": "Society",
        "title": "Mạng lưới nhà tạm lánh cộng đồng: Lá chắn bảo vệ phụ nữ và trẻ em trước bạo lực",
        "title_en": "Safe Havens: Community Safe Houses Protecting Women and Vulnerable Children",
        "subtitle": "A nationwide coalition of confidential safe homes provides holistic legal aid, trauma therapy, and vocational retraining for survivors of domestic violence.",
        "author": "Le Thu Trang • Phu Nu Viet Nam",
        "date": "Friday, October 30, 2026 - 17:30 (GMT+7)",
        "readTime": "6 min read",
        "sourceName": "Báo Phụ Nữ Việt Nam",
        "sourceUrl": "https://phunuvietnam.vn/nha-tam-lanh-la-chan-an-toan-cho-phu-nu-va-tre-em",
        "image": "",
        "imageCaption": "Counselors offering warm psychosocial support in a tranquil, confidential shelter setting.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "18.3K",
        "likes": 920,
        "tags": ["Women Rights", "Social Protection", "Community", "Empathy"],
        "content": [
            "For women and children escaping domestic abuse, finding an immediate, secure sanctuary can mean the difference between life and tragedy.",
            "Community safe shelters operated in partnership with the Vietnam Women's Union offer discreet emergency accommodation, legal accompaniment, and trauma-informed psychological counseling.",
            "Crucially, residents receive microfinance grants and vocational apprenticeships in baking, tailoring, and digital marketing, enabling them to establish independent, self-determined livelihoods."
        ]
    },

    # --- HUMAN STORIES (3 new: human-16, human-17, human-18) ---
    {
        "id": "human-16",
        "category": "human-stories",
        "categoryName": "Human Stories",
        "title": "Chuyến xe cứu thương 0 đồng của người tài xế cựu binh miền Tây",
        "title_en": "The Zero-Dong Ambulance: Veteran Driver’s 12-Year Mission Rushing Patients to Emergency Rooms",
        "subtitle": "Selling his family farm plot to purchase an equipped medical transport van, 65-year-old Hai Cong drives round-the-clock emergency hospital transfers completely free of charge.",
        "author": "Thach Thao • Tien Phong",
        "date": "Wednesday, November 4, 2026 - 21:00 (GMT+7)",
        "readTime": "6 min read",
        "sourceName": "Báo Tiền Phong",
        "sourceUrl": "https://tienphong.vn/chuyen-xe-cuu-thuong-0-dong-nguoi-tai-xe-mien-tay",
        "image": "",
        "imageCaption": "Veteran Hai Cong inspecting his ambulance vehicle before a midnight emergency call.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "28.4K",
        "likes": 1890,
        "tags": ["Compassion", "Volunteering", "Mekong Delta", "Heroes in Life"],
        "content": [
            "In rural Cho Gao district, everyone keeps Uncle Hai Cong’s mobile number taped to their refrigerator. When emergencies strike at 3 a.m., his siren is heard within minutes.",
            "Over twelve years, Hai Cong has completed over 3,200 emergency runs, ferrying laboring mothers, accident victims, and stroke patients to provincial hospitals in My Tho and Ho Chi Minh City.",
            "He adamantly refuses compensation or fuel reimbursement: 'When people are fighting for breath, humanity cannot be measured in money. As long as my eyes can see the road, I will drive.'"
        ]
    },
    {
        "id": "human-17",
        "category": "human-stories",
        "categoryName": "Human Stories",
        "title": "Cặp vợ chồng U70 và hành trình hiến đất mở đường, dựng trường cho trẻ em nghèo",
        "title_en": "The Generous Octogenarians Donating Family Land to Build Mountain Classrooms",
        "subtitle": "In the remote foothills of Quang Ngai, elder couple Vo Van Sanh and Nguyen Thi Sen donated 5,000 square meters of ancestral farmland to construct a kindergarten and concrete access bridge.",
        "author": "Bao Binh • Dan Tri",
        "date": "Monday, November 2, 2026 - 11:45 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "Dân Trí",
        "sourceUrl": "https://dantri.com.vn/tam-long-nhan-ai/cap-vo-chong-gia-hien-dat-xay-truong-cho-tre",
        "image": "",
        "imageCaption": "Grandpa Sanh and Grandma Sen smiling warmly outside the colorful kindergarten built on their donated land.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "21.0K",
        "likes": 1470,
        "tags": ["Philanthropy", "Grandparents", "Kindness", "Education"],
        "content": [
            "When local authorities struggled to find land to construct a safe kindergarten away from monsoon landslide zones, grandpa Vo Van Sanh gathered his children and grandchildren for a family council.",
            "Together, the family unanimously agreed to donate 5,000 square meters of fertile cinnamon and acacia land—worth billions of dong—to the village community.",
            "“Wealth comes and goes, but educated children will lift our entire village out of hardship,” says 78-year-old Sanh with a radiant smile."
        ]
    },
    {
        "id": "human-18",
        "category": "human-stories",
        "categoryName": "Human Stories",
        "title": "Nghị lực của cô gái bại não trở thành dịch giả sách truyền cảm hứng",
        "title_en": "Cerebral Palsy Scholar Translating Inspirational Books to Empower Youth",
        "subtitle": "Typing with a single functional index finger on an adapted keyboard, Tran Thi Mai Lan has translated 15 bestselling psychological titles, proving resilience conquers physical limitations.",
        "author": "Hoang Yen • Phu Nu Online",
        "date": "Friday, October 30, 2026 - 14:10 (GMT+7)",
        "readTime": "6 min read",
        "sourceName": "Phụ Nữ Online",
        "sourceUrl": "https://phunuonline.com.vn/nghi-luc-co-gai-bai-nao-tro-thanh-dich-gia-sach",
        "image": "",
        "imageCaption": "Translator Mai Lan typing with dedicated focus at her custom-designed workspace.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "24.9K",
        "likes": 1720,
        "tags": ["Inspiration", "Resilience", "Literature", "Never Give Up"],
        "content": [
            "Diagnosed with congenital spastic cerebral palsy at birth, doctors warned that Mai Lan might never sit upright or speak articulate sentences.",
            "With her mother's steadfast devotion and her own unyielding curiosity, Lan taught herself English by listening to audiobooks, painstakingly tapping out letters one by one.",
            "Today, Lan is one of the most respected translators of inspirational and therapeutic psychology literature in Vietnam, using her royalty earnings to fund wheelchairs for disabled children."
        ]
    },

    # --- MIND & SOUL (3 new: mind-15, mind-16, mind-17) ---
    {
        "id": "mind-15",
        "category": "mind-soul",
        "categoryName": "Mind & Soul",
        "title": "Triết lý sống tối giản Danshari trong không gian căn hộ đô thị nhỏ",
        "title_en": "Danshari Minimalism: Finding Spacious Serenity in Compact Urban Studios",
        "subtitle": "By paring down possessions to only those that spark genuine utility and joy, young urbanites are transforming tiny 35-square-meter apartments into zen havens.",
        "author": "Minh Chau • Living Well",
        "date": "Thursday, November 5, 2026 - 09:00 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "Tạp chí Kiến Trúc & Đời Sống",
        "sourceUrl": "https://kientrucdoisong.vn/triet-ly-danshari-trong-can-ho-nho-do-thi",
        "image": "",
        "imageCaption": "A minimalist living studio with uncluttered wooden surfaces and tranquil indoor greenery.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "16.1K",
        "likes": 840,
        "tags": ["Minimalism", "Danshari", "Slow Living", "Inner Peace"],
        "content": [
            "In dense metropolises where square footage is scarce, emotional claustrophobia often mirrors physical clutter.",
            "The Danshari philosophy (Dan = Refuse, Sha = Dispose, Ri = Separate) encourages letting go of consumerist accumulation, creating breathable physical and mental space.",
            "“When you strip away what is unnecessary, what truly matters—peace of mind, meaningful connection, and stillness—finally has room to breathe,” reflects minimalist architect Le Thuy."
        ]
    },
    {
        "id": "mind-16",
        "category": "mind-soul",
        "categoryName": "Mind & Soul",
        "title": "Nghệ thuật thêu tay truyền thống: Liệu pháp thiền tịnh phục hồi cảm xúc",
        "title_en": "Hand Embroidery Therapy: The Calming Cadence of Thread, Needle, and Breath",
        "subtitle": "Drawing thousands of desk-bound office workers into weekend craft ateliers, needlework offers an unplugged flow state that alleviates chronic digital anxiety.",
        "author": "An Nhien • Mindful Crafts",
        "date": "Tuesday, November 3, 2026 - 18:20 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "Tạp chí Văn Hóa & Nghệ Thuật",
        "sourceUrl": "https://vanhoanghethuat.vn/theu-tay-truyen-thong-lieu-phap-chua-lanh",
        "image": "",
        "imageCaption": "Artisan carefully guiding silk embroidery thread through fine linen fabric on an embroidery hoop.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "14.9K",
        "likes": 730,
        "tags": ["Embroidery", "Mindfulness", "Art Therapy", "Handicrafts"],
        "content": [
            "The repetitive, rhythmic pull of silk thread through taut linen requires singular, gentle attention, naturally anchoring wandering minds in the immediate physical present.",
            "Psychologists liken traditional embroidery to tactile meditation: each stitch represents an intentional breath, gently slowing heart rates and soothing nervous exhaustion.",
            "“In a world of instant dopamine and fleeting clicks, watching a lotus flower bloom slowly beneath your fingertips over weeks is deeply therapeutic,” says workshop founder Pham Lan."
        ]
    },
    {
        "id": "mind-17",
        "category": "mind-soul",
        "categoryName": "Mind & Soul",
        "title": "Học cách bao dung với chính mình: Thoát khỏi cái bẫy chủ nghĩa hoàn hảo",
        "title_en": "Self-Compassion in High-Pressure Times: Breaking the Trap of Toxic Perfectionism",
        "subtitle": "Behavioral psychologists explain why treating oneself with the same kindness offered to a dear friend builds true emotional resilience and lasting success.",
        "author": "Dr. Ha My • Psychology & Well-being",
        "date": "Sunday, November 1, 2026 - 10:00 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "Tâm Lý Học Đời Sống",
        "sourceUrl": "https://tamlyhoc.vn/bao-dung-chinh-minh-thoat-bay-chu-nghia-hoan-hao",
        "image": "",
        "imageCaption": "A person sitting quietly in nature, practicing gentle mindful self-acceptance.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "19.7K",
        "likes": 1050,
        "tags": ["Self Compassion", "Mental Wellness", "Personal Growth", "Psychology"],
        "content": [
            "Modern professionals often operate under an internal tyrant, harshly criticizing every perceived shortcoming or minor career setback.",
            "Research demonstrates that self-criticism triggers physiological threat responses, increasing anxiety and cognitive paralysis, whereas self-compassion fosters genuine grit.",
            "Allowing oneself to make mistakes without questioning personal worth is not complacency; it is the fundamental cornerstone of healthy psychological endurance."
        ]
    },

    # --- IN-DEPTH (3 new: indepth-18, indepth-19, indepth-20) ---
    {
        "id": "indepth-18",
        "category": "in-depth",
        "categoryName": "In-Depth",
        "title": "Bảo tồn đàn voọc Cát Bà: Cuộc chiến sinh thái giữ loài linh trưởng quý hiếm bậc nhất thế giới",
        "title_en": "The Cat Ba Langur Conservation Crusade: Protecting Earth's Rarest Primate",
        "subtitle": "With fewer than 90 individuals surviving on rugged limestone islands, a dedicated team of Vietnamese rangers and international primatologists fights to avert extinction.",
        "author": "Doan Xuan Tung • Wildlife Conservation",
        "date": "Wednesday, November 4, 2026 - 13:00 (GMT+7)",
        "readTime": "8 min read",
        "sourceName": "Vietnam Journal of Primatology",
        "sourceUrl": "https://conservation.org.vn/cat-ba-langur-conservation-crusade",
        "image": "",
        "imageCaption": "Golden-headed Cat Ba langur perched gracefully on sheer limestone karst cliffs.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "22.7K",
        "likes": 1130,
        "tags": ["Wildlife Conservation", "Cat Ba", "Biodiversity", "Endangered Species"],
        "content": [
            "Perched on sheer vertical cliffs rising out of the emerald waters of Lan Ha Bay, the golden-headed Cat Ba langur (Trachypithecus poliocephalus) is one of the world's most critically endangered mammals.",
            "Decades of habitat fragmentation and poaching reduced the population to just 40 individuals in the early 2000s, triggering an extraordinary multi-agency conservation rescue mission.",
            "Through community guardian patrols, anti-snare sweeps, and strictly protected karst corridors, the population has rebounded to 88 individuals, representing a beacon of hope for global biodiversity conservation."
        ]
    },
    {
        "id": "indepth-19",
        "category": "in-depth",
        "categoryName": "In-Depth",
        "title": "Nghệ thuật ẩm thực cung đình Huế: Lịch sử, triết lý âm dương và nghi lễ hoàng gia",
        "title_en": "Hue Royal Culinary Art: History, Yin-Yang Gastronomy, and Palace Banquets",
        "subtitle": "An exhaustive historical monograph exploring the strict culinary rituals, seasonal ingredients, and aesthetic philosophies that defined Nguyen Dynasty banquet feasts.",
        "author": "Historian Tran Duc Anh Son • Imperial Studies",
        "date": "Monday, November 2, 2026 - 17:00 (GMT+7)",
        "readTime": "8 min read",
        "sourceName": "Hue Historical Review",
        "sourceUrl": "https://tapchisonghuong.com.vn/nghe-thuat-am-thuc-cung-dinh-hue",
        "image": "",
        "imageCaption": "Intricately carved royal dragon fruit centerpiece and porcelain banquet dishes of imperial Hue.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "27.1K",
        "likes": 1390,
        "tags": ["Hue Imperial", "Culinary Heritage", "History", "Gastronomy"],
        "content": [
            "In imperial Hue, cooking was elevated into a metaphysical art form governed by royal protocol, aesthetic symmetry, and the fundamental five-element (Ngũ hành) harmony.",
            "Palace cooks (Đội Thượng Thiện) sourced the finest regional delicacies across the realm, from bird's nest and lotus seeds of Tinh Tam Lake to rare sea cucumber and green sticky rice.",
            "Preserving these authentic imperial banquet recipes today requires not only culinary skill, but a profound understanding of historical etiquette and seasonal cosmological balance."
        ]
    },
    {
        "id": "indepth-20",
        "category": "in-depth",
        "categoryName": "In-Depth",
        "title": "Hành trình số hóa di sản Hán Nôm: Cứu hàng vạn tài liệu cổ trước sự bào mòn của thời gian",
        "title_en": "Digitalizing Nom and Han Archives: Rescuing Vietnam’s Ancient Manuscripts from Decay",
        "subtitle": "Equipped with multispectral optical scanners and machine learning OCR, scholars and archivists are racing against tropical humidity to preserve fragile parchment scrolls.",
        "author": "Dr. Nguyen Quang Thang • Institute of Han-Nom Studies",
        "date": "Saturday, October 31, 2026 - 15:40 (GMT+7)",
        "readTime": "7 min read",
        "sourceName": "Institute of Han-Nom Studies",
        "sourceUrl": "https://hannom.org.vn/so-hoa-di-san-han-nom-cuu-tai-lieu-co",
        "image": "",
        "imageCaption": "Archivists utilizing cold-light overhead scanners to digitize fragile woodblock printed manuscripts.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "20.4K",
        "likes": 1020,
        "tags": ["Han-Nom", "Digital Archiving", "Ancient Manuscripts", "Cultural Heritage"],
        "content": [
            "Deep in library vaults across Vietnam and overseas collections lie hundreds of thousands of royal decrees, medical treatises, village genealogies, and epic poetry penned in ancient Han-Nom script.",
            "In tropical monsoon humidity, insect pests and acid paper decay present constant perils to these irreplaceable parchment records.",
            "Using advanced contactless multispectral imaging and deep-learning character recognition, an international consortium has made over 20,000 ancient volumes publicly accessible to scholars worldwide."
        ]
    }
]

print(f"Defined {len(new_15)} new articles!")
