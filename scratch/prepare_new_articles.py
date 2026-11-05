# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

new_articles = [
    # IN-DEPTH NEW ARTICLES
    {
        "id": "indepth-6",
        "category": "in-depth",
        "categoryName": "In-Depth",
        "title": "Meet the educators using science to teach kindness",
        "title_en": "Meet the educators using science to teach kindness",
        "subtitle": "How would our world look if the next generation became leaders in kindness? These teachers are using science to help children understand what happens to our brains when we’re kind.",
        "author": "BTV Quỳnh • Positive News",
        "date": "Wednesday, November 4, 2026 - 14:15 (GMT+7)",
        "readTime": "6 min read",
        "sourceName": "Positive News",
        "sourceUrl": "https://www.positive.news/society/meet-the-educators-using-science-to-teach-kindness/",
        "image": "assets/images/in-dept/image4.jpg",
        "imageCaption": "Educators introduce the Learn Kind curriculum, exploring emotional literacy and neuroscience in classrooms.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "6.4K",
        "likes": 482,
        "tags": ["Education", "Kindness", "Neuroscience", "In-Depth"],
        "content": [
            "Science has shown that acts of kindness – such as helping someone in need, or giving to charity – improve our health, help build better relationships, and can even be contagious.",
            "Such acts promote the production of ‘feel-good’ chemicals like oxytocin, serotonin and dopamine in our brains, and possibly even give us a ‘helper’s high,’ scientists say.",
            "That’s why the charity kindness.org is keen to promote kindness, and an understanding of the science behind it, in schools. The result will be happier students and more caring classrooms, they say – and society as a whole stands to benefit.",
            "Its Learn Kind curriculum looks at the science of kindness, along with the development of skills such as self-awareness, empathy and emotional literacy. The pilot began in 2020, when it was taught in 15 countries, including the US, the UK and Thailand, reaching more than 38,500 students.",
            "Today, teachers across the globe are integrating compassionate communication and peer-led support systems, proving that emotional intelligence can be taught alongside math and literature."
        ]
    },
    {
        "id": "indepth-7",
        "category": "in-depth",
        "categoryName": "In-Depth",
        "title": "Meet three people who make a living by showing kindness to the planet",
        "title_en": "Meet three people who make a living by showing kindness to the planet",
        "subtitle": "Being kind to the planet pays, especially for these three inspiring individuals who talk to Positive News about their hands-on careers dedicated to ecological stewardship.",
        "author": "BTV Quỳnh • Positive News",
        "date": "Tuesday, November 3, 2026 - 09:30 (GMT+7)",
        "readTime": "7 min read",
        "sourceName": "Positive News",
        "sourceUrl": "https://www.positive.news/environment/three-people-who-have-jobs-in-nature/",
        "image": "assets/images/in-dept/image5.jpg",
        "imageCaption": "Carolina Pinto monitors water quality and biodiversity along London's urban river corridors.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "7.1K",
        "likes": 539,
        "tags": ["Environment", "Ecology", "Sustainability", "Careers"],
        "content": [
            "Working to protect the environment is rewarding, despite its challenges. Positive News meets three women whose careers are all about being kind to nature.",
            "### Carolina Pinto: Restoring London's Living Waters",
            "Carolina is the Brent rivers and communities officer at Thames 21, a charity that works across London to improve rivers for people and wildlife. 'I grew up by the sea in Brazil, so I always felt a connection with nature. Once I began studying environmental science at university I just fell in love with it,' she shares.",
            "Some of her work is very hands-on, such as installing large pieces of wood in the river to restore habitats for fish and other wildlife, which also helps filter the water and reduces flood risk.",
            "### Community-Driven Conservation",
            "Alongside habitat management, environmental officers collaborate with local artists, school groups, and community volunteers to turn neglected waterways into vibrant natural corridors."
        ]
    },
    {
        "id": "indepth-8",
        "category": "in-depth",
        "categoryName": "In-Depth",
        "title": "‘He’s not meant to be here’: Rory Kinnear on the ghost of his father Roy, and his brutally honest new film",
        "title_en": "‘He’s not meant to be here’: Rory Kinnear on the ghost of his father Roy, and his brutally honest new film",
        "subtitle": "The acclaimed actor speaks candidly about grief, parental memory, and turning poignant family loss into timeless cinematic art.",
        "author": "The Guardian Culture",
        "date": "Thursday, November 5, 2026 - 07:45 (GMT+7)",
        "readTime": "8 min read",
        "sourceName": "The Guardian",
        "sourceUrl": "https://www.theguardian.com/tv-and-radio/2026/nov/05/rory-kinnear-father-roy-death",
        "image": "assets/images/in-dept/image6.jpg",
        "imageCaption": "Rory Kinnear reflects on the legacy of his father, actor Roy Kinnear, and the enduring architecture of familial remembrance.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "8.9K",
        "likes": 645,
        "tags": ["Cinema", "Culture", "Memory", "Interview"],
        "content": [
            "Grief has a peculiar geometry; it bends time and reshapes how we view those who came before us. In a wide-ranging, heartfelt interview, Rory Kinnear delves into the profound loss that framed his childhood.",
            "When his father, the beloved character actor Roy Kinnear, tragically died on set in 1988, Rory was just 10 years old. The reverberations of that sudden absence have informed his creative empathy ever since.",
            "Through his new work, Kinnear refuses easy sentimentality. Instead, he explores the messy, luminous contours of remembering someone whose physical absence is permanently filled by enduring affection."
        ]
    },

    # MIND & SOUL NEW ARTICLES
    {
        "id": "mind-7",
        "category": "mind-soul",
        "categoryName": "Mind & Soul",
        "title": "The women’s boxing nights helping abuse survivors rebuild their inner strength",
        "title_en": "The women’s boxing nights helping abuse survivors rebuild their inner strength",
        "subtitle": "A new series of all-female fight nights funds free boxing classes that help women reclaim their physical autonomy and self-worth after domestic abuse.",
        "author": "BTV Quỳnh • Positive News",
        "date": "Monday, November 2, 2026 - 16:20 (GMT+7)",
        "readTime": "6 min read",
        "sourceName": "Positive News",
        "sourceUrl": "https://www.positive.news/society/the-womens-boxing-nights-helping-abuse-survivors/",
        "image": "assets/images/mind_&_soul/image13.jpg",
        "imageCaption": "Boxers at the Fight Forward programme in London train together, cultivating resilience and peer solidarity.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "5.9K",
        "likes": 472,
        "tags": ["Healing", "Boxing", "Women Empowerment", "Resilience"],
        "content": [
            "“The Fight Forward programme literally saved my life,” explains Saria, 40, raising her voice above the rhythmic percussion of gloves hitting punchbags at an east London boxing gym.",
            "Founded by former Team GB boxer Lesley Sackey, the initiative offers free training camps specifically tailored for domestic abuse survivors. Through disciplined footwork and sparring, participants rediscover their physical agency.",
            "“Doing that camp gave me the strength to fight for myself, to build confidence, and to discover a sense of self-worth that I’d never had in my life,” Saria notes.",
            "The community extends far beyond fitness: women build enduring friendships, exchanging advice and collective support in an atmosphere of radical empathy."
        ]
    },
    {
        "id": "mind-8",
        "category": "mind-soul",
        "categoryName": "Mind & Soul",
        "title": "Canadian outside skirt beef infused with Northwest Vietnamese herb marinade",
        "title_en": "Canadian outside skirt beef infused with Northwest Vietnamese herb marinade",
        "subtitle": "A delectable culinary dialogue pairing prime imported beef with fragrant mac khen, doi seeds, and pristine herbs from Vietnam's northern mountains.",
        "author": "VOV World Food Delight",
        "date": "Wednesday, November 4, 2026 - 11:00 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "VOV World",
        "sourceUrl": "https://vovworld.vn/food-delight/canadian-outside-skirt-beef-combined-with-northwest-vietnamese-herb-marinade-2468953.vov5",
        "image": "assets/images/mind_&_soul/image14.jpg",
        "imageCaption": "Chef presents pan-seared Canadian beef seasoned with Northwest forest spices and wild lime leaves.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "4.8K",
        "likes": 395,
        "tags": ["Culinary", "Gastronomy", "Culture", "Herbs"],
        "content": [
            "Culinary harmony often emerges from unlikely geographic cross-pollination. In this week's Food Delight, we explore a masterclass combining premium Canadian outside skirt beef with wild herbs from the mountainous Northwest of Vietnam.",
            "The dish highlights mac khen (wild mountain pepper) and hat doi, gently roasted and coarsely ground to release distinctive citrus-woody aromatics.",
            "Marinated briefly to let the beef's natural richness shine, the meat is flash-seared over glowing embers, producing a tender, succulent texture complemented by spicy lime dip."
        ]
    },

    # SOCIETY NEW ARTICLES
    {
        "id": "society-6",
        "category": "society",
        "categoryName": "Society",
        "title": "Vietnamese Buddhist temples embrace TikTok sermons and QR code donations",
        "title_en": "Vietnamese Buddhist temples embrace TikTok sermons and QR code donations",
        "subtitle": "From livestreaming Dharma talks to receiving cashless merit offerings via QR codes, venerable temples across Vietnam adapt compassion to the digital epoch.",
        "author": "BTV Quỳnh • VietNamNet",
        "date": "Sunday, November 1, 2026 - 15:40 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "VietNamNet",
        "sourceUrl": "https://vietnamnet.vn/en/vietnamese-buddhist-temples-embrace-tiktok-sermons-and-qr-code-donations-2570595.html",
        "image": "assets/images/society/image10.jpg",
        "imageCaption": "Monks in Da Nang utilize digital streaming devices to connect with young Buddhist followers across the nation.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "11.3K",
        "likes": 789,
        "tags": ["Digital Culture", "Buddhism", "Society", "Innovation"],
        "content": [
            "In ancient pagodas where incense smoke traditionally drifted alongside quiet chanting, a new digital hum is taking root.",
            "Monks across Hanoi, Hue, and Da Nang are setting up compact tripod cameras to broadcast short-form philosophical reflections on TikTok and YouTube Shorts, answering youth anxieties in direct, compassionate language.",
            "Alongside digital sermons, QR code plaques placed near donation boxes allow tech-savvy temple visitors to make cashless merit offerings transparently, eliminating theft and improving accounting for charity funds.",
            "“The Dharma is not static; it travels wherever people are suffering or seeking peace. In 2026, people spend hours online, so that is where spiritual reassurance must be,” explains Venerable Thich Minh."
        ]
    },
    {
        "id": "society-7",
        "category": "society",
        "categoryName": "Society",
        "title": "Vietnam's GDP grows 9.01%, nearly triple global economic forecast",
        "title_en": "Vietnam's GDP grows 9.01%, nearly triple global economic forecast",
        "subtitle": "Robust manufacturing exports, high-tech foreign investment, and burgeoning domestic tourism propel national economic expansion into double-digit projections.",
        "author": "BTV Quỳnh • VietNamNet",
        "date": "Friday, October 30, 2026 - 17:15 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "VietNamNet",
        "sourceUrl": "https://vietnamnet.vn/en/vietnam-s-gdp-grows-9-01-nearly-triple-global-forecast-2563213.html",
        "image": "assets/images/society/image11.jpg",
        "imageCaption": "High-tech semiconductor fabrication facility in Bac Ninh province operating at full global capacity.",
        "video": "",
        "isTopPost": False,
        "isBreaking": True,
        "views": "16.8K",
        "likes": 920,
        "tags": ["Economy", "GDP", "Trade", "Development"],
        "content": [
            "Vietnam's economy expanded by an astounding 9.01% in the first nine months of 2026, vastly outstripping the international average and highlighting remarkable domestic resilience.",
            "According to the General Statistics Office, industrial processing, semiconductor manufacturing, and renewable power infrastructure led the growth wave.",
            "Macroeconomic stability, contained inflation, and sweeping trade agreements have cemented Vietnam's role as a premier supply chain nexus for Southeast Asia."
        ]
    },
    {
        "id": "society-8",
        "category": "society",
        "categoryName": "Society",
        "title": "A Vietnamese voice in a South African home: Preserving mother tongue across continents",
        "title_en": "A Vietnamese voice in a South African home: Preserving mother tongue across continents",
        "subtitle": "For overseas Vietnamese families in Pretoria and Johannesburg, preserving linguistic roots and cultural identity begins at the dining table.",
        "author": "Vietnam News Cultural Bureau",
        "date": "Saturday, October 24, 2026 - 19:30 (GMT+7)",
        "readTime": "6 min read",
        "sourceName": "Vietnam News",
        "sourceUrl": "https://vietnamnews.vn/society/1803581/a-vietnamese-voice-in-a-south-african-home.html",
        "image": "assets/images/society/image23.jpg",
        "imageCaption": "Vietnamese diaspora families in South Africa gather to teach children folk songs and national history.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "6.2K",
        "likes": 465,
        "tags": ["Diaspora", "Linguistics", "Culture", "Family"],
        "content": [
            "Thousands of miles away from the bustling streets of Hanoi, the aroma of simmering nuoc mam and warm rice brings a slice of Vietnam to suburban Johannesburg.",
            "Living abroad presents unique challenges for passing down language to second-generation children. Parents establish weekend reading groups, singing folk melodies and cooking traditional dishes to keep Vietnamese heritage vibrant.",
            "“When our children speak our mother tongue, they carry a key that unlocks the memories of their grandparents and their ancestral homeland,” reflects community organizer Tran Mai."
        ]
    },

    # HUMAN STORIES NEW ARTICLES
    {
        "id": "human-9",
        "category": "human-stories",
        "categoryName": "Human Stories",
        "title": "On World Kindness Day, how one nonprofit has given the gift of mobility to 1.5 million people",
        "title_en": "On World Kindness Day, how one nonprofit has given the gift of mobility to 1.5 million people",
        "subtitle": "Free Wheelchair Mission delivers durable, cost-effective wheelchairs to people with disabilities across 95 developing countries, restoring dignity and independence.",
        "author": "BTV Quỳnh • ABC News / Good News",
        "date": "Friday, November 14, 2025 - 08:30 (GMT+7)",
        "readTime": "5 min read",
        "sourceName": "ABC News",
        "sourceUrl": "https://abcnews.com/video/127480629/",
        "image": "assets/images/human_stories/image22.jpg",
        "imageCaption": "A recipient smiles proudly upon receiving a custom-built rough-terrain wheelchair, opening up educational and livelihood opportunities.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "7.5K",
        "likes": 560,
        "tags": ["Humanity", "Philanthropy", "Mobility", "Kindness"],
        "content": [
            "For millions of individuals living with mobility impairments in rural and developing regions, everyday movement can be an insurmountable barrier.",
            "Free Wheelchair Mission has transformed over 1.5 million lives by engineering durable, low-cost wheelchairs capable of navigating rugged unpaved paths.",
            "“Mobility means renewed dignity, access to schooling, and the ability to earn an independent living,” explains CEO Nuka Hart. “Our goal is to ensure nobody is left isolated.”"
        ]
    },
    {
        "id": "human-10",
        "category": "human-stories",
        "categoryName": "Human Stories",
        "title": "Stable electricity brings light to homes in remote mountainous hamlets",
        "title_en": "Stable electricity brings light to homes in remote mountainous hamlets",
        "subtitle": "Over 400 households in Quang Tri’s Bong Lai village celebrate modern electric power, bidding farewell to smoky kerosene lamps and ushering in agricultural mechanization.",
        "author": "Nguyen Khanh Chi • Vietnam News",
        "date": "Monday, October 26, 2026 - 10:20 (GMT+7)",
        "readTime": "6 min read",
        "sourceName": "Vietnam News",
        "sourceUrl": "https://vietnamnews.vn/society/1803487/stable-electricity-brings-light-to-homes-in-remote-village.html",
        "image": "assets/images/human_stories/image23.jpg",
        "imageCaption": "Villagers in Bong Lai village gather under new electric lighting, celebrating rural infrastructure modernization.",
        "video": "",
        "isTopPost": False,
        "isBreaking": False,
        "views": "8.1K",
        "likes": 612,
        "tags": ["Infrastructure", "Rural Development", "Humanity", "Vietnam"],
        "content": [
            "In Bong Lai village, nestled in the rugged interior of Quang Tri province, dusk used to bring deep darkness and the acrid smell of burning oil lamps.",
            "Following the completion of the provincial rural electrification initiative, steady power now lights up 412 households, powering rice mills, refrigerators, and children's study desks.",
            "“Now that the electricity supply is stable, we can use appliances, preserve farm produce, and watch educational television,” smiles villager Hoang Van Thao."
        ]
    }
]

print(f"Prepared {len(new_articles)} new authentic articles from updated Word docs.")
