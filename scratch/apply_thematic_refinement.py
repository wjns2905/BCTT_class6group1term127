import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read current 100 articles
with open('js/data.js', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('const ARTICLES_DATA = ') + len('const ARTICLES_DATA = ')
e = c.rfind('];') + 1

articles = json.loads(c[s:e])
print(f"Loaded {len(articles)} articles.")

# Dictionary of refined titles and subtitles for the 5 categories
# We ensure every title is vibrant, tailored, and strictly matches user criteria
# 1. Trending: hot hot bùm bùm, viral, bùng nổ, kỷ lục
# 2. Society: chính sách, xã hội, cộng đồng, việc làm, hạ tầng
# 3. Human Stories: lòng nhân ái, nghị lực phi thường, chuyện đời cảm động
# 4. Mind & Soul: chữa lành, an yên, sống chậm, tâm hồn
# 5. In-Depth: sâu lắng tâm sự, ký ức, chiêm nghiệm nhân sinh, điều tra chuyên sâu

refinements = {
    # ================= TRENDING (Hot hot bùm bùm) =================
    "trending-1": {
        "title": "Cơn sốt concert sao quốc tế tại Mỹ Đình: Vé chợ đen săn lùng, sao mê mẩn nón lá và phở Việt",
        "title_en": "International Concert Mania at My Dinh: Scalper Frenzy and Stars Falling in Love with Vietnam",
        "subtitle": "Hàng chục nghìn khán giả phủ kín khán đài, tạo nên cơn sốt văn hóa bùng nổ càn quét mạng xã hội suốt tuần qua.",
        "subtitle_en": "Tens of thousands of fans packed My Dinh Stadium, sparking a viral cultural craze that swept digital media."
    },
    "trending-2": {
        "title": "Hiện tượng 'hộp mù' Art Toy và trào lưu sưu tầm gây bão: Giới trẻ chi hàng chục triệu săn lùng",
        "title_en": "The Blind Box Art Toy Phenomenon: Young Consumers Spending Millions on Viral Collectibles",
        "subtitle": "Từ các trung tâm thương mại Hà Nội đến Sài Gòn, hàng dài bạn trẻ thức xuyên đêm xếp hàng đập hộp món đồ chơi gây sốt toàn cầu.",
        "subtitle_en": "From Hanoi to Saigon malls, long queues of youth wait overnight to unbox viral designer art toys."
    },
    "trending-3": {
        "title": "Khởi nghiệp tuổi 60: Tự tay chế tác chiếc Porsche 904FF mơ ước từ thời trai trẻ gây sốt giới mê xe",
        "title_en": "Starting Fresh at 60: Handcrafting Dream Porsche 904FF Sparks Viral Adoration",
        "subtitle": "Câu chuyện người đàn ông 68 tuổi biến xưởng cơ khí thành nơi hiện thực hóa siêu xe huyền thoại thu hút hàng triệu lượt xem.",
        "subtitle_en": "The remarkable story of a 68-year-old turning a modest workshop into a haven for a legendary vintage racer."
    },
    "trending-4": {
        "title": "Gánh mưu sinh Hội An: Góc ảnh lay động triệu trái tim du khách quốc tế giữa mưa phố cổ",
        "title_en": "Street Vendors with Shoulder Pole: Viral Photo Series Captivating International Travelers",
        "subtitle": "Hình ảnh đôi quang gánh trĩu nặng nhịp sống mưu sinh rêu phong được chia sẻ rầm rộ trên các diễn đàn du lịch thế giới.",
        "subtitle_en": "Iconic imagery of street vendors under rainy heritage eaves went massively viral across global travel forums."
    },
    "trending-5": {
        "title": "Chiến dịch 500 ngày đêm: Kỳ tích khoa học ADN đưa gần 800 anh hùng liệt sĩ trở về với gia đình",
        "title_en": "500-Day-and-Night Campaign: Scientific Miracle Returning Names to Nearly 800 Fallen Heroes",
        "subtitle": "Chiến dịch ứng dụng công nghệ gen hiện đại xúc động lòng người, tạo nên bước ngoặt lịch sử trong công tác đền ơn đáp nghĩa.",
        "subtitle_en": "High-tech forensic genetics breakthrough touching the hearts of the nation in unprecedented remembrance drive."
    },
    "trending-6": {
        "title": "Vương quốc Anh tăng vọt mức chứng minh tài chính du học: Cộng đồng sinh viên quốc tế xôn xao",
        "title_en": "UK Hikes Proof-of-Funds Threshold for Students: International Community in Heated Debate",
        "subtitle": "Quy định mới áp dụng từ cuối tháng 11 nâng chi phí sinh hoạt chứng minh lên hàng trăm triệu đồng, trở thành chủ đề nóng nhất các hội du học.",
        "subtitle_en": "New regulations significantly raise financial prerequisites, igniting urgent discussions across student associations."
    },
    "trending-7": {
        "title": "Cơn bão Gen AI đổ bộ tòa soạn: Trí tuệ nhân tạo tăng tốc đưa tin nhưng liệu có thay thế được nhà báo?",
        "title_en": "The Gen AI Tidal Wave in Newsrooms: Can Algorithms Ever Replace Human Empathy?",
        "subtitle": "Các mô hình ngôn ngữ lớn đang đảo lộn quy trình sản xuất tin tức với tốc độ tính bằng giây, châm ngòi cuộc tranh luận nghề nghiệp sôi nổi.",
        "subtitle_en": "Large language models transform news desks in seconds, igniting passionate debates on the future of journalism."
    },
    "trending-8": {
        "title": "Bùng nổ trào lưu săn máy ảnh film cổ: Gen Z xếp hàng dài chờ tráng ảnh giữa lòng phố cổ",
        "title_en": "Gen Z Retro Film Craze Explodes: Youth Queuing for Analog Rolls in Hanoi's Old Quarter",
        "subtitle": "Trái ngược với sự gấp gáp của điện thoại thông minh, trải nghiệm bấm máy film cơ và chờ đợi từng khung hình đang tạo thành 'trend' cực hot.",
        "subtitle_en": "Rejecting instantaneous digital snapshots, analog film photography becomes an unstoppable lifestyle trend."
    },
    "trending-9": {
        "title": "Cà phê Robusta Việt Nam bùng nổ thế giới: Từ hạt rẻ tiền đến ngôi sao đặc sản trên bàn tiệc quốc tế",
        "title_en": "Vietnamese Robusta Revolution: From Commodity Bean to Global Specialty Coffee Star",
        "subtitle": "Làn sóng canh tác hữu cơ và lên men hảo hạng đưa hạt cà phê quê hương chiến thắng tại các cuộc thi thử nếm danh giá nhất thế giới.",
        "subtitle_en": "Premium organic fermentations elevate Vietnamese beans into the most sought-after specialty roast worldwide."
    },
    "trending-10": {
        "title": "Trào lưu 'rừng bỏ túi' trên mái cao ốc: Đô thị hóa xanh khiến cư dân thích thú check-in",
        "title_en": "Urban Pocket Forests on High-Rise Roofs: Green Living Craze Transforming Skylines",
        "subtitle": "Những ốc đảo xanh mướt giữa lưng chừng trời không chỉ hạ nhiệt tòa nhà mà còn trở thành điểm hẹn thư giãn hot nhất của giới trẻ.",
        "subtitle_en": "Emerald sky-gardens lower concrete temperatures while becoming the most sought-after urban hangout spots."
    },
    "trending-11": {
        "title": "Cẩm nang du lịch Việt Nam bùng nổ truyền thông quốc tế: Lonely Planet vinh danh top điểm đến không thể bỏ lỡ",
        "title_en": "Vietnam Travel Boom: Lonely Planet Highlights Irresistible Destinations for Global Travelers",
        "subtitle": "Từ vịnh biển thiên đường Phú Quốc, phố cổ Hội An đến đèo mây Hà Giang, hình ảnh đất nước phủ sóng khắp các trang báo du lịch thế giới.",
        "subtitle_en": "From Phu Quoc beaches to Ha Giang mountain loops, Vietnam captures the spotlight of global travel journalism."
    },
    "trending-12": {
        "title": "Làn sóng sáng tạo Gen AI tại Đông Nam Á: Giới trẻ biến truyền thuyết dân gian thành tác phẩm số triệu view",
        "title_en": "Southeast Asia Gen AI Creative Wave: Reimagining Folklore into Viral Digital Masterpieces",
        "subtitle": "Các studio trẻ kết hợp sức mạnh thuật toán với mỹ học bản địa, tạo ra những thước phim hoạt họa và bộ nhận diện khiến thế giới ngỡ ngàng.",
        "subtitle_en": "Young creative studios merge generative algorithms with cultural folklore, earning millions of global views."
    },
    "trending-13": {
        "title": "Dự án thế kỷ: Tuyến đường sắt tốc độ cao 350 km/h Bắc - Nam gây xôn xao dư luận",
        "title_en": "Project of the Century: 350 km/h North-South High-Speed Rail Stirs National Excitement",
        "subtitle": "Kế hoạch rút ngắn hành trình Hà Nội - TP.HCM xuống còn 5 giờ trở thành chủ đề nóng bỏng được chia sẻ hàng triệu lượt trên mạng xã hội.",
        "subtitle_en": "Plans to slash Hanoi-Saigon transit down to five hours spark massive public excitement and viral discussions."
    },
    "trending-14": {
        "title": "Cơn sốt cà phê lên men và ẩm thực không rác thải: Trào lưu sống xanh cực hot của giới trẻ Đà Nẵng",
        "title_en": "Zero-Waste Dining & Fermentation Craze: The Hottest Eco-Lifestyle Trend in Da Nang",
        "subtitle": "Mô hình trà vỏ cà phê và nước ép enzyme tuần hoàn thu hút đông đảo du khách trẻ trải nghiệm lối sống bền vững.",
        "subtitle_en": "Circular brewing and upcycled fruit enzymes attract waves of eco-conscious youth along the central coast."
    },
    "trending-15": {
        "title": "UNESCO vinh danh làng nghề truyền thống Việt Nam: Cơn sốt tự hào dân tộc lan tỏa mạng xã hội",
        "title_en": "UNESCO Honors Vietnamese Craft Guilds: Wave of Cultural Pride Sweeps Digital Networks",
        "subtitle": "Gốm Bát Tràng, lụa Vạn Phúc và khảm trai Chuyên Mỹ chính thức bước vào danh mục di sản sống, giới trẻ hào hứng tìm về cội nguồn.",
        "subtitle_en": "Living heritage recognition triggers widespread cultural celebration and a youth movement back to artisan roots."
    },
    "trending-16": {
        "title": "Dịch vụ công VNeID giải quyết thủ tục trong tích tắc: Cư dân mạng thích thú vì không còn cảnh xếp hàng",
        "title_en": "Smart Public Services on VNeID: Citizens Thrilled by Instant Paperwork Approvals",
        "subtitle": "Chỉ với vài thao tác chạm trên smartphone, hàng loạt thủ tục hành chính phức tạp được hoàn tất trong vài phút, người dân hào hứng khen ngợi.",
        "subtitle_en": "Administrative paperwork completed in seconds via smartphone kiosks receives overwhelming praise from citizens."
    },
    "trending-17": {
        "title": "Bùng nổ sáng tạo nông nghiệp tuần hoàn: Biến trấu và bã cà phê thành bao bì sinh học tự phân hủy cực hot",
        "title_en": "Circular Innovation Boom: Transforming Rice Husks and Coffee Pulp into Viral Eco-Packaging",
        "subtitle": "Các bạn trẻ khởi nghiệp xanh thay thế hộp xốp bằng sợi nấm và phụ phẩm nông nghiệp, nhận hàng triệu USD đầu tư công nghệ xanh.",
        "subtitle_en": "Green biotech startups replace single-use styrofoam with compostable agricultural fibers, securing major investments."
    },
    "trending-18": {
        "title": "Thương mại điện tử nông sản bùng nổ: Sầu riêng và thanh long Việt Nam phủ kín siêu thị quốc tế",
        "title_en": "Cross-Border Agri-Commerce Sensation: Vietnamese Fruits Dominating Global Supermarket Aisles",
        "subtitle": "Vận chuyển lạnh đường hàng không kết nối trực tiếp vườn cây tới bàn ăn châu Âu và Bắc Mỹ trong 48 giờ, tạo nên cơn sốt ẩm thực nhiệt đới.",
        "subtitle_en": "Cold-chain air logistics connects orchards directly to overseas consumers within 48 hours, creating viral demand."
    },
    "trending-19": {
        "title": "Thể thao điện tử (Esports) Việt Nam lập kỳ tích: Đội tuyển quốc gia giành HCV, hàng triệu fan vỡ òa",
        "title_en": "Vietnamese Esports Sensation: National Team Clinches Gold, Millions of Fans Rejoice",
        "subtitle": "Từ phòng net xập xệ đến bục vinh quang đấu trường quốc tế, game thủ Việt chứng minh đẳng cấp thể thao điện tử chuyên nghiệp đỉnh cao.",
        "subtitle_en": "From cybercafes to international podiums, Vietnamese gamers prove world-class excellence in arena athletics."
    },
    "trending-20": {
        "title": "Làn sóng âm nhạc Indie Việt gây bão: Những giai điệu mộc mạc từ phòng ngủ leo thẳng Top 1 Trending",
        "title_en": "Vietnamese Indie Music Wave Explodes: Bedroom Melodies Climbing Straight to Top 1 Trending",
        "subtitle": "Không cần phòng thu tiền tỷ hay chiêu trò PR, những ca từ chân thật và giai điệu acoustic đánh trúng tim đen thế hệ trẻ cô đơn.",
        "subtitle_en": "Stripped of over-production, raw songwriting and acoustic warmth strike an overwhelming emotional chord."
    },

    # ================= SOCIETY (Xã hội, chính sách, dân sinh, cộng đồng) =================
    "society-1": {
        "title": "Ứng phó bão giá: Các mô hình tương trợ cộng đồng và 'chợ 0 đồng' tiếp sức người lao động nghèo",
        "title_en": "Tackling the Cost of Living Crisis: Grassroots Mutual Aid Networks Supporting Low-Income Families",
        "subtitle": "Trước áp lực giá cả sinh hoạt leo thang, những bếp ăn tình thương và tủ sách cộng đồng trở thành điểm tựa vững chắc cho xóm nghèo.",
        "subtitle_en": "Amid surging inflation, community-driven free pantries and solidarity hubs provide crucial relief for working-class households."
    },
    "society-2": {
        "title": "Chuyển dịch năng lượng quốc gia: Tiềm năng điện gió ngoài khơi dẫn dắt tăng trưởng xanh của Việt Nam",
        "title_en": "National Renewable Transition: Offshore Wind Potential Powering Vietnam's Sustainable Future",
        "subtitle": "Chính phủ đẩy mạnh quy hoạch nguồn năng lượng sạch dọc bờ biển dài hơn 3.200 km, đặt mục tiêu trung hòa carbon vào năm 2050.",
        "subtitle_en": "Government accelerates green energy zoning along 3,200 km of coastline aiming for net-zero emissions by 2050."
    },
    "society-3": {
        "title": "Số hóa và bảo tồn phương ngữ các dân tộc thiểu số: Cứu di sản ngôn ngữ trước nguy cơ mai một",
        "title_en": "Digitalizing Indigenous Dialects: Safeguarding Endangered Linguistic Heritage Across the Highlands",
        "subtitle": "Các nhà nhân học và kỹ sư công nghệ phối hợp ghi âm, biên soạn từ điển số hóa cho hàng chục thứ tiếng của đồng bào miền núi.",
        "subtitle_en": "Anthropologists and software engineers compile digital phonetic archives for dozens of endangered ethnic minority tongues."
    },
    "society-4": {
        "title": "Cuộc cách mạng giao thông công cộng: Các tuyến Metro thay đổi diện mạo và văn hóa đi lại đô thị",
        "title_en": "Public Transit Revolution: Modern Metro Lines Transforming Commuter Habits in Major Cities",
        "subtitle": "Giảm thiểu ùn tắc và ô nhiễm khói bụi, thói quen đi bộ và sử dụng tàu điện ngầm đang từng bước kiến tạo lối sống văn minh.",
        "subtitle_en": "Alleviating road congestion and tailpipe smog, urban rail transit fosters a progressive, pedestrian-friendly lifestyle."
    },
    "society-5": {
        "title": "Bình đẳng giáo dục thời công nghệ: Các lớp học lập trình miễn phí trao cần câu cơm cho học sinh nghèo",
        "title_en": "Equitable Tech Education: Free Coding Academies Empowering Rural High School Students",
        "subtitle": "Dự án đưa máy tính và chuyên gia công nghệ về các vùng nông thôn hẻo lánh, mở toang cánh cửa việc làm số cho thế hệ trẻ.",
        "subtitle_en": "Initiatives delivering laptops and mentorship to countryside hamlets unlock lucrative digital career pathways."
    },
    "society-6": {
        "title": "Chùa Việt trong thời đại số: Thuyết pháp qua mạng xã hội và minh bạch công đức bằng mã QR",
        "title_en": "Vietnamese Temples in the Digital Era: Streaming Sermons and QR Code Philanthropy",
        "subtitle": "Sự thích ứng linh hoạt của các cơ sở tôn giáo giúp giáo lý từ bi lan tỏa rộng rãi tới giới trẻ và giảm thiểu tiêu cực.",
        "subtitle_en": "Thoughtful technological adaptation allows Buddhist teachings to reach modern youth while ensuring financial transparency."
    },
    "society-7": {
        "title": "Kinh tế phục hồi mạnh mẽ: GDP Việt Nam tăng trưởng 9,01%, gấp gần ba lần dự báo toàn cầu",
        "title_en": "Resilient Economic Growth: Vietnam's GDP Expands by 9.01%, Outpacing Global Forecasts",
        "subtitle": "Giải ngân đầu tư công quyết liệt và làn sóng FDI chất lượng cao tạo đòn bẩy vững chắc cho nền kinh tế trong giai đoạn then chốt.",
        "subtitle_en": "Decisive public infrastructure investments and high-value foreign manufacturing fuel robust macroeconomic expansion."
    },
    "society-8": {
        "title": "Giữ gìn tiếng Việt nơi xứ người: Hành trình kiên trì gìn giữ tiếng mẹ đẻ trong gia đình kiều bào Nam Phi",
        "title_en": "Preserving the Mother Tongue Abroad: A Vietnamese Family's Dedication in South Africa",
        "subtitle": "Dù sinh ra và lớn lên cách quê hương nửa vòng trái đất, những đứa trẻ kiều bào vẫn tự hào cất tiếng nói quê cha đất tổ trong mỗi bữa cơm.",
        "subtitle_en": "Though raised thousands of miles away, diaspora children take pride in speaking Vietnamese around the family dining table."
    },
    "society-9": {
        "title": "Chuyến xe y tế lưu động: Đưa bác sĩ chuyên khoa và thiết bị chẩn đoán cao ra tận các xã đảo tiền tiêu",
        "title_en": "Mobile Medical Vans: Delivering Specialist Healthcare and Diagnostic Equipment to Remote Islands",
        "subtitle": "Những đoàn thầy thuốc tình nguyện vượt sóng gió mang máy siêu âm, điện tim và thuốc men khám chữa bệnh miễn phí cho ngư dân.",
        "subtitle_en": "Volunteer healthcare convoys brave coastal seas to provide specialized screenings and free medicines to fishing communes."
    },
    "society-10": {
        "title": "Mô hình trường học xanh: 1.000 lớp học ứng dụng điện mặt trời và bài học thực tế về môi trường",
        "title_en": "Green Schools Movement: 1,000 Classrooms Powered by Solar Panels and Living Ecology Labs",
        "subtitle": "Học sinh được tự tay chăm sóc vườn rau hữu cơ và theo dõi sản lượng điện sạch, biến trường học thành chiếc nôi sống xanh.",
        "subtitle_en": "Pupils actively tend rooftop vegetable patches and monitor clean energy dashboards, embodying ecological stewardship."
    },
    "society-11": {
        "title": "Phổ cập ngôn ngữ ký hiệu truyền hình: Đảm bảo quyền tiếp cận thông tin bình đẳng cho người khiếm thính",
        "title_en": "Universal Sign Language Broadcasts: Ensuring Equal Information Rights for the Hearing Impaired",
        "subtitle": "Các bản tin thời sự chính luận mở rộng khung hình phiên dịch viên thủ ngữ, khẳng định cam kết không để người yếu thế bị bỏ lại phía sau.",
        "subtitle_en": "Prime-time newscasts incorporate live sign language interpretation, affirming commitments to universal civil accessibility."
    },
    "society-12": {
        "title": "Thích ứng biến đổi khí hậu: Nông dân Bến Tre chuyển đổi sinh kế thành công trước đợt hạn mặn lịch sử",
        "title_en": "Climate Adaptation in the Mekong Delta: Ben Tre Farmers Thriving Amid Historic Saline Tides",
        "subtitle": "Mô hình xen canh tôm - lúa và dừa hữu cơ chịu mặn giúp hàng nghìn hộ gia đình ven biển gia tăng thu nhập bền vững.",
        "subtitle_en": "Integrated shrimp-mangrove and organic saline-adapted crops allow coastal families to turn climate threats into prosperity."
    },
    "society-13": {
        "title": "Thư viện cộng đồng vùng cao: Những chuyến xe sách vượt đèo gieo mầm tri thức cho trẻ em bản nghèo",
        "title_en": "Highland Mobile Libraries: Books Crossing Mountain Passes to Nurture Children's Dreams",
        "subtitle": "Hơn 50 phòng đọc sách miễn phí được dựng lên tại các điểm trường xa xôi, thắp sáng ước mơ học tập của con em đồng bào dân tộc.",
        "subtitle_en": "Over fifty free library corners established in mountain hamlets illuminate the educational aspirations of ethnic youth."
    },
    "society-14": {
        "title": "Mạng lưới nhà tạm lánh cộng đồng: Lá chắn bảo vệ phụ nữ và trẻ em trước nạn bạo lực gia đình",
        "title_en": "Community Safe Havens: Protective Shelters Safeguarding Women and Children from Domestic Violence",
        "subtitle": "Cung cấp nơi ở an toàn, tư vấn tâm lý và dạy nghề miễn phí, giúp các nạn nhân tìm lại sự tự chủ và xây dựng cuộc sống mới.",
        "subtitle_en": "Providing confidential refuge, legal advocacy, and vocational training to help survivors rebuild independent, dignified lives."
    },

    # ================= MIND & SOUL (Chữa lành, an yên, tĩnh tâm, sống chậm) =================
    "mind-1": {
        "title": "Nghệ thuật thưởng thức phở Việt: Một bát nước dùng nóng hổi xoa dịu tâm hồn sau ngày dài mệt mỏi",
        "title_en": "The Soul-Soothing Art of Vietnamese Pho: How a Warm Broth Comforts a Weary Spirit",
        "subtitle": "Hương hoa hồi, quế chi và vị ngọt thanh tao của nước hầm xương từ lâu đã trở thành liệu pháp tinh thần bình dị của người Việt.",
        "subtitle_en": "Fragrant star anise, cinnamon, and rich simmered broth offer an unpretentious, deeply comforting sanctuary for the soul."
    },
    "mind-2": {
        "title": "Giải phóng bản thân qua hóa trang nghệ thuật: Khi việc thay đổi diện mạo giúp giải tỏa áp lực tâm lý",
        "title_en": "Self-Expression Through Transformative Art: Releasing Inner Burdens by Embracing Play",
        "subtitle": "Các chuyên gia tâm lý lý giải vì sao những lễ hội hóa trang sáng tạo là cơ hội tuyệt vời để rũ bỏ vỏ bọc hoàn hảo thường nhật.",
        "subtitle_en": "Psychologists explain why creative transformations allow individuals to shed rigid daily facades and rediscover inner joy."
    },
    "mind-3": {
        "title": "Lắng nghe cơ thể qua dinh dưỡng lành mạnh: So sánh sữa yến mạch và sữa bò để nuôi dưỡng thân tâm",
        "title_en": "Listening to Your Body Through Mindful Nutrition: Oat Milk vs. Dairy for Wholesome Well-Being",
        "subtitle": "Không có lựa chọn nào là hoàn hảo tuyệt đối; điều cốt lõi là thấu hiểu cơ địa và lắng nghe nhu cầu dinh dưỡng của chính mình.",
        "subtitle_en": "No single diet fits all; true wellness begins with tuning into personal digestion and honoring bodily signals."
    },
    "mind-4": {
        "title": "Nghệ thuật sống chậm (Slow Living): Ngắt kết nối với màn hình để kết nối sâu sắc với chính mình",
        "title_en": "The Art of Slow Living: Unplugging from Screens to Deeply Reconnect with Your Inner Self",
        "subtitle": "Trong thời đại thông báo nhấp nháy liên tục, sự tĩnh lặng và những buổi chiều không làm gì cả trở thành món quà xa xỉ nhất.",
        "subtitle_en": "In an era of relentless digital buzz, intentional stillness and unhurried afternoons become the ultimate form of self-care."
    },
    "mind-5": {
        "title": "Sức mạnh chữa lành của tiếng cồng chiêng: Đưa tâm thức trở về với nhịp điệu bình an cổ xưa",
        "title_en": "The Healing Resonance of Gong Culture: Returning the Mind to an Ancient Rhythm of Peace",
        "subtitle": "Tần số âm thanh trầm bổng ngân vang giữa núi rừng đại ngàn có khả năng xoa dịu hệ thần kinh và giải phóng những âu lo dồn nén.",
        "subtitle_en": "Low-frequency vibrational acoustics echoing through ancient highland forests soothe tense nervous systems and melt anxiety."
    },
    "mind-6": {
        "title": "Vệ sinh giấc ngủ thời đại số: 7 thói quen khoa học giúp bạn buông bỏ âu lo và ngủ ngon mỗi đêm",
        "title_en": "Sleep Hygiene in the Digital Age: 7 Scientific Habits to Release Worry and Rest Deeply",
        "subtitle": "Tạm biệt ánh sáng xanh, học cách hít thở chậm và thiết lập nghi thức thư giãn để chào đón một giấc ngủ sâu phục hồi năng lượng.",
        "subtitle_en": "Saying farewell to blue light, practicing diaphragmatic breathing, and creating bedtime rituals for deep restoration."
    },
    "mind-7": {
        "title": "Câu lạc bộ quyền anh của sự chữa lành: Giúp những người phụ nữ tổn thương tìm lại sức mạnh nội tâm",
        "title_en": "The Healing Boxing Ring: How Athletic Grit Empowers Abuse Survivors to Reclaim Inner Strength",
        "subtitle": "Mỗi cú đấm trên sàn tập không chỉ rèn luyện thể chất mà còn là cách giải phóng những tổn thương và tìm lại lòng tự tôn đã mất.",
        "subtitle_en": "Physical discipline on the canvas serves as a therapeutic outlet to release trauma, rebuild boundaries, and restore dignity."
    },
    "mind-8": {
        "title": "Thưởng thức ẩm thực bằng chánh niệm: Khi gia vị thảo mộc Tây Bắc đánh thức sự an lạc của giác quan",
        "title_en": "Mindful Gastronomy: How Northwest Mountain Herbs Awaken Sensory Presence and Delight",
        "subtitle": "Mùi hạt dổi, mắc khén thơm nồng hòa quyện trong từng thớ thịt nướng nhắc ta sống trọn vẹn trong khoảnh khắc hiện tại.",
        "subtitle_en": "Fragrant forest peppers and wild herbs remind diners to slow down, savor every bite, and inhabit the present moment."
    },
    "mind-9": {
        "title": "Bánh cuốn Tây Hồ 60 năm gìn giữ phong vị xưa: Một góc ẩm thực bình yên nhắc ta nhớ về bữa cơm gia đình",
        "title_en": "Tay Ho Banh Cuon Across 60 Years: A Tranquil Eatery Evoking Cherished Memories of Home",
        "subtitle": "Giữa Sài Gòn hoa lệ náo nhiệt, quán bánh cuốn mộc mạc của gia đình Michelin Bib Gourmand là nơi chốn tìm về của những tâm hồn hoài cổ.",
        "subtitle_en": "Amid Saigon's bustling streets, this multi-generational eatery offers a nostalgic sanctuary of comforting steamed rolls."
    },
    "mind-10": {
        "title": "Tắm rừng Ba Vì (Shinrin-yoku): Nghệ thuật hòa mình vào cỏ cây để xua tan mệt mỏi và âu lo đô thị",
        "title_en": "Forest Bathing in Ba Vi (Shinrin-yoku): Immersing in Woodlands to Dissolve Urban Fatigue",
        "subtitle": "Đi bộ chậm rãi dưới tán thông già, hít thở hương rừng ngai ngái và lắng nghe tiếng chim ca giúp hệ miễn dịch phục hồi mạnh mẽ.",
        "subtitle_en": "Strolling beneath towering pines, inhaling plant phytoncides, and listening to forest birds revitalizes physical vitality."
    },
    "mind-11": {
        "title": "Viết nhật ký trị liệu: Phương pháp đặt bút trút bỏ gánh nặng và làm dịu những cơn bão trong lòng",
        "title_en": "Therapeutic Journaling: Putting Pen to Paper to Unburden the Heart and Calm Inner Storms",
        "subtitle": "15 phút viết tự do không phán xét vào mỗi sáng giúp bạn gỡ rối mớ bòng bong suy nghĩ và đón nhận bản thân một cách dịu dàng.",
        "subtitle_en": "Fifteen minutes of unfiltered morning writing unravels mental knots, fostering gentle self-acceptance and clarity."
    },
    "mind-12": {
        "title": "Thiền trà Shan Tuyết trên đỉnh Chiêu Lầu Thi: Thưởng một chén trà, tìm lại một khoảng trời an yên",
        "title_en": "Shan Tuyet Tea Meditation: Sipping Silence and Finding Inner Stillness on Mountain Summits",
        "subtitle": "Hái từ những gốc chè cổ thụ hàng trăm năm tuổi ngập trong biển mây, ngụm trà ấm nóng đưa tâm hồn trở về với sự tĩnh tại tuyệt đối.",
        "subtitle_en": "Harvested from century-old wild tea trees shrouded in mist, a warm cup anchors the mind in transcendent tranquility."
    },
    "mind-13": {
        "title": "Vượt qua kiệt sức sáng tạo: Tại sao cho phép bản thân được 'rảnh rỗi' lại là chìa khóa phục hồi tâm trí",
        "title_en": "Overcoming Creative Burnout: Why Allowing Yourself to Do Nothing Restores the Mind",
        "subtitle": "Não bộ chỉ có thể kết nối những ý tưởng đột phá khi ta ngừng ép buộc bản thân chạy đua với những bảng phân công nhiệm vụ.",
        "subtitle_en": "The human brain synthesizes breakthrough ideas only when we release constant pressure and permit unstructured daydreaming."
    },
    "mind-14": {
        "title": "Âm vang đàn đá ngàn năm: Liệu pháp chữa lành tâm hồn bằng thanh âm nguyên sơ của đất trời",
        "title_en": "Acoustic Resonance of Ancient Lithophones: Primordial Sound Therapy for the Modern Soul",
        "subtitle": "Những thanh đá bazan tiền sử ngân lên giai điệu sâu thẳm, tác động vào tần số rung động của cơ thể và xoa dịu những căng thẳng sâu kín.",
        "subtitle_en": "Prehistoric basalt chime stones emit deep, primordial frequencies that harmonize bodily resonance and alleviate stress."
    },
    "mind-15": {
        "title": "Triết lý sống tối giản Danshari: Dọn dẹp không gian sống để giải phóng những vướng bận trong lòng",
        "title_en": "Danshari Minimalism: Decluttering Your Living Space to Liberate Your Mind",
        "subtitle": "Học cách buông bỏ những đồ vật không còn phục vụ cuộc sống là bước đầu tiên để tâm trí trở nên thanh thản và nhẹ nhõm.",
        "subtitle_en": "Releasing possessions that no longer serve your life is the first transformative step toward lightness and mental clarity."
    },
    "mind-16": {
        "title": "Nghệ thuật thêu tay truyền thống: Liệu pháp tĩnh tâm tìm lại sự tập trung qua từng đường kim mũi chỉ",
        "title_en": "Traditional Hand Embroidery Therapy: Restoring Inner Focus One Stitch at a Time",
        "subtitle": "Nhịp điệu đều đặn của sợi chỉ xuyên qua mặt vải lanh giúp người thực hành thoát khỏi những xao nhãng và tìm về sự bình yên trọn vẹn.",
        "subtitle_en": "The rhythmic cadence of needle and silk thread invites the sewer into a state of quiet focus and deep serenity."
    },
    "mind-17": {
        "title": "Học cách bao dung với chính mình: Thoát khỏi cái bẫy của chủ nghĩa hoàn hảo và những lời phán xét",
        "title_en": "Practicing Self-Compassion: Breaking Free from the Trap of Toxic Perfectionism",
        "subtitle": "Đối xử với bản thân bằng sự dịu dàng như đối xử với một người bạn thân là nền tảng cốt lõi của một nội lực vững vàng.",
        "subtitle_en": "Treating oneself with the same kindness offered to a dear friend forms the unbreakable foundation of true resilience."
    },

    # ================= IN-DEPTH (Sâu lắng tâm sự, tự sự, ký ức, chiêm nghiệm nhân sinh) =================
    "indepth-1": {
        "title": "Hà Nội không bao giờ ngừng chảy: Hương hoa sữa và ký ức mùa thu trôi qua những cuộc đời",
        "title_en": "A Hanoi That Never Stands Still: The Bittersweet Scent of Hoa Sua and Collective Autumn Memories",
        "subtitle": "Góc tản văn sâu lắng về những góc phố rêu phong, những mùa thu đi qua tuổi trẻ và nỗi niềm hoài niệm của những người con xa xứ.",
        "subtitle_en": "A deeply poetic essay reflecting on mossy alleys, passing autumns of youth, and nostalgic yearnings of expatriates."
    },
    "indepth-2": {
        "title": "Đối diện với căn bệnh Parkinson: Rhys Ifans và Laura Linney trải lòng về cái chết, tình yêu và sự hữu hạn",
        "title_en": "Facing Parkinson's Disease: Rhys Ifans and Laura Linney on Mortality, Love, and Grace",
        "subtitle": "Cuộc phỏng vấn thẳng thắn và xúc động đến nghẹn ngào về cách một tác phẩm nghệ thuật giúp con người dũng cảm nhìn vào đoạn kết cuộc đời.",
        "subtitle_en": "A brutally honest and touching conversation exploring how cinema helps humans confront illness and the final chapter of life."
    },
    "indepth-3": {
        "title": "Di sản kiến trúc biệt thự Pháp cổ: Ký ức đô thị trăm năm giữa dòng chảy hiện đại hóa Hà Nội",
        "title_en": "French Colonial Architectural Heritage: A Century of Urban Memory Amid Modern Expansion",
        "subtitle": "Phóng sự chuyên sâu về những mảng tường vàng bong tróc, hàng hoa sắt uốn lượn và cuộc giằng co giữa bảo tồn di sản và phát triển đô thị.",
        "subtitle_en": "An investigative monograph on weathered ochre walls, wrought-iron balconies, and the struggle between heritage and modernity."
    },
    "indepth-4": {
        "title": "Hồi sinh rừng ngập mặn Đồng bằng sông Cửu Long: Cuộc đối thoại bền bỉ giữa con người và mẹ thiên nhiên",
        "title_en": "Reviving the Mekong Delta Mangroves: A Resilient Dialogue Between Humanity and Nature",
        "subtitle": "Khảo sát thực địa đa chiều về những cánh rừng đước chắn sóng, nỗ lực phục hồi hệ sinh thái ven biển và bài học tôn trọng tự nhiên.",
        "subtitle_en": "Extensive field survey examining mangrove coastal buffers, ecological regeneration, and living in balance with tides."
    },
    "indepth-5": {
        "title": "Ký ức giấy Dó ngàn năm: Tiếng chày giã vỏ cây và nỗi niềm của những nghệ nhân già cuối cùng",
        "title_en": "The Millennium Memory of Do Paper: Echoes of Pestles and Musings of Master Artisans",
        "subtitle": "Trải lòng về một nghề truyền thống từng làm nên linh hồn văn hiến Thăng Long, nay nhọc nhằn tìm chỗ đứng trong kỷ nguyên kỹ thuật số.",
        "subtitle_en": "Reflective oral history on a craft that preserved Vietnam's ancient literature, striving to endure in the digital era."
    },
    "indepth-6": {
        "title": "Nghệ thuật dạy học bằng lòng trắc ẩn: Khi khoa học và tình thương cùng bước vào bục giảng",
        "title_en": "The Art of Educating with Compassion: When Scientific Rigor Meets Human Empathy in Classrooms",
        "subtitle": "Phân tích chuyên sâu về mô hình giáo dục cảm xúc xã hội (SEL), nơi trường học không chỉ truyền thụ kiến thức mà còn dạy trẻ cách yêu thương.",
        "subtitle_en": "Comprehensive analysis of social-emotional learning, transforming schools into incubators of empathy and mutual respect."
    },
    "indepth-7": {
        "title": "Ba con người chọn công việc bảo vệ hành tinh: Những trăn trở lặng lẽ giữa thiên nhiên hoang sơ",
        "title_en": "Three Lives Dedicated to the Earth: Quiet Solitude and Devotion in Untamed Wilderness",
        "subtitle": "Tâm sự của những chuyên gia bảo tồn động vật và nhà sinh vật học chấp nhận rời xa tiện nghi thành thị để bảo vệ sự sống cho muôn loài.",
        "subtitle_en": "Intimate profiles of conservationists who stepped away from urban comfort to defend fragile habitats and wild species."
    },
    "indepth-8": {
        "title": "Diễn viên Rory Kinnear trải lòng: Khoảng trống vô tận sau sự ra đi của người cha và hành trình tìm lại an yên",
        "title_en": "Rory Kinnear Opens His Heart: The Enduring Void of Losing a Father and Finding Peace",
        "subtitle": "Bài tâm sự sâu sắc về nỗi đau mất mát, những ký ức tuổi thơ không bao giờ phai mờ và cách nghệ thuật chữa lành những vết thương tâm hồn.",
        "subtitle_en": "A moving retrospective on parental bereavement, indelible childhood echoes, and how dramatic art mends grief."
    },
    "indepth-9": {
        "title": "Bên trong ngôi biệt thự trăm tuổi hình chữ Khẩu: Ký ức một thời vàng son của thương gia phố cổ Hàng Bè",
        "title_en": "Inside a 100-Year-Old Merchant Villa: Echoes of Hanoi's Golden Architectural Age on Hang Be",
        "subtitle": "Khảo sát kiến trúc và hồi ức của hậu duệ cụ Trương Trọng Vọng trong không gian sống lưu giữ trọn vẹn nét giao thoa văn hóa Đông - Tây.",
        "subtitle_en": "Architectural documentation and familial memoirs within a century-old residence blending Sino-French elegance."
    },
    "indepth-10": {
        "title": "Báo cáo điều tra đa tầng: Hành trình lần theo dấu vết hạt vi nhựa đe dọa nguồn sống sông ngòi Việt Nam",
        "title_en": "Multi-Layer Investigative Report: Tracking Microplastic Contamination Across Major Deltas",
        "subtitle": "Ba năm lấy mẫu phân tích trên lưu vực sông Hồng và sông Mekong gióng lên hồi chuông cảnh báo về an ninh nguồn nước và chuỗi thức ăn.",
        "subtitle_en": "Three years of environmental water sampling ringing urgent alarm bells regarding freshwater health and food chains."
    },
    "indepth-11": {
        "title": "Tiếng thoi đưa lụa Vạn Phúc: Nỗi niềm trăn trở của những người thợ dệt giữ lấy gấm hoa trước dòng đời",
        "title_en": "The Rhythm of Van Phuc Weavers: An Artisan's Longing to Preserve Heritage Silk Amid Fast Fashion",
        "subtitle": "Tâm sự của những người thợ cả dành trọn đời bên khung dệt gỗ cổ truyền, kiên cường giữ gìn hồn lụa tự nhiên giữa làn sóng sợi công nghiệp.",
        "subtitle_en": "Personal reflections of master weavers dedicating their lives to natural mulberry silk against synthetic mass production."
    },
    "indepth-12": {
        "title": "Đổi mới chăm sóc sức khỏe tâm thần tại cộng đồng: Phá bỏ bức tường định kiến để ôm lấy những nỗi đau",
        "title_en": "Community Mental Health Reform: Dismantling Stigma to Embrace Hidden Emotional Suffering",
        "subtitle": "Phóng sự chuyên sâu về sự chuyển dịch từ điều trị cách ly trong bệnh viện sang mạng lưới hỗ trợ tâm lý gần gũi ngay tại khu dân cư.",
        "subtitle_en": "An investigative look into the paradigm shift from isolated institutionalization to neighborhood-embedded counseling."
    },
    "indepth-13": {
        "title": "Giải mã bí ẩn gạch nung Mỹ Sơn: Ký ức rêu phong ngàn năm của một nền văn minh rực rỡ",
        "title_en": "Unraveling the Secrets of Cham Brick Architecture: A Thousand Years of Weathered Sanctity",
        "subtitle": "Công trình nghiên cứu khoa học phục dựng chất kết dính dầu rái cổ truyền, hé mở tài nghệ kiến trúc phi thường của người xưa.",
        "subtitle_en": "Scientific investigation uncovering ancient botanical resin binders that have held sacred sanctuary towers for twelve centuries."
    },
    "indepth-14": {
        "title": "Địa kinh tế cảng biển nước sâu và logistics đường thủy: Vận mệnh kinh tế hàng hải quốc gia",
        "title_en": "Geoeconomics of Deep-Water Seaports and Waterways: The Maritime Destiny of a Coastal Nation",
        "subtitle": "Nghiên cứu kinh tế chiến lược về cách các cụm cảng Cái Mép - Thị Vải và Lạch Huyện kết nối vận tải sà lan nội địa để nâng tầm vị thế đất nước.",
        "subtitle_en": "Strategic economic analysis of how deep-water container gateways and inland river feeders redefine national competitiveness."
    },
    "indepth-15": {
        "title": "Đạo đức trí tuệ nhân tạo trong y khoa: Điểm giao thoa giữa thuật toán chính xác và bàn tay trắc ẩn",
        "title_en": "Clinical AI Ethics: Where Algorithmic Precision Meets the Invaluable Touch of Human Empathy",
        "subtitle": "Bàn luận sâu sắc về ranh giới sinh tử nơi máy móc có thể đọc phim chụp trong một giây, nhưng chỉ có bác sĩ mới thấu hiểu ánh mắt bệnh nhân.",
        "subtitle_en": "Deep bioethical reflections on why neural networks can read scans instantly, but only human healers can comfort the suffering."
    },
    "indepth-16": {
        "title": "Ngân hàng hạt giống bản địa: Những người âm thầm gom góp nguồn gen lúa quý cứu lấy tương lai lương thực",
        "title_en": "Indigenous Seed Guardians: Silently Rescuing Heirloom Rice Genetics to Secure Future Food",
        "subtitle": "Phóng sự về hành trình xuyên rừng gom hơn 300 giống lúa cổ truyền chống chịu hạn mặn của những nhà khoa học thầm lặng.",
        "subtitle_en": "Intimate reporting on agronomists trekking remote valleys to preserve 340 heirloom climate-resilient grain varieties."
    },
    "indepth-17": {
        "title": "Tranh dân gian Đông Hồ: Hồn dân tộc lắng đọng trong màu giấy điệp và triết lý nhân sinh của người xưa",
        "title_en": "Dong Ho Folk Woodcuts: The Soul of a People Preserved in Scallop Shells and Earthy Pigments",
        "subtitle": "Khảo cứu mỹ thuật về cách những bản khắc gỗ mộc mạc lưu giữ mỹ quan, ước vọng thái bình và nếp sống thuần hậu của làng quê Bắc Bộ.",
        "subtitle_en": "Art history retrospective exploring how humble woodblocks capture rural humor, cosmological harmony, and ancestral philosophy."
    },
    "indepth-18": {
        "title": "Cuộc chiến sinh tồn của đàn voọc Cát Bà: Nỗi trăn trở giữ lại loài linh trưởng quý hiếm trước bờ vực tuyệt chủng",
        "title_en": "The Struggle for Survival of Cat Ba Langurs: Dedicated Wardens Shielding Earth's Rarest Primate",
        "subtitle": "Ghi chép từ đảo đá vôi nơi chưa đầy 90 cá thể voọc đầu vàng sinh sống, và lòng tận tụy của những người lính gác rừng kiên định.",
        "subtitle_en": "Dispatches from rugged limestone cliffs where fewer than 90 golden-headed primates cling to survival under ranger protection."
    },
    "indepth-19": {
        "title": "Ẩm thực cung đình Huế: Triết lý âm dương sâu sắc ẩn sau những mâm yến tiệc hoàng triều một thuở",
        "title_en": "Hue Imperial Gastronomy: Profound Yin-Yang Cosmological Philosophy Behind Ancient Royal Banquets",
        "subtitle": "Chuyên luận lịch sử về sự cầu kỳ, quy chuẩn lễ nghi và quan niệm 'ăn hương ăn hoa' của chốn hoàng cung xưa.",
        "subtitle_en": "Historical monograph dissecting the refined rituals, seasonal five-element balance, and aesthetics of dynasty dining."
    },
    "indepth-20": {
        "title": "Hành trình số hóa di sản Hán Nôm: Cuộc chạy đua thầm lặng với thời gian để lưu giữ linh hồn tiền nhân",
        "title_en": "Digitalizing Nom and Han Archives: A Quiet Race Against Time to Rescue Ancestral Manuscripts",
        "subtitle": "Gặp gỡ những chuyên gia phục chế đang tỉ mẩn từng trang sách cổ mối mọt, cứu hàng vạn thư tịch quý giá trước khí hậu nhiệt đới ẩm.",
        "subtitle_en": "Inside archival conservation labs where restorers painstakingly preserve crumbling parchment scrolls from tropical decay."
    }
}

# Update all matching articles in ARTICLES_DATA
updated_count = 0
for a in articles:
    if a['id'] in refinements:
        r = refinements[a['id']]
        a['title'] = r['title']
        a['title_en'] = r['title_en']
        a['subtitle'] = r['subtitle']
        a['subtitle_en'] = r['subtitle_en']
        updated_count += 1

print(f"Updated {updated_count} articles with perfect thematic titles and subtitles!")

# Format and save back to js/data.js
formatted_json = json.dumps(articles, ensure_ascii=False, indent=2)
new_code = c[:s] + formatted_json + c[e:]

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(new_code)

print("Saved updated js/data.js!")
