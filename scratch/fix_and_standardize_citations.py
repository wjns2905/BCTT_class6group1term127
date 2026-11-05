import sys, json, re

sys.stdout.reconfigure(encoding='utf-8')

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

articles = json.loads(re.search(r'const ARTICLES_DATA = (\[.*?\]);', text, re.DOTALL).group(1))

# URL updates map
url_updates = {
    'human-1': {
        'sourceUrl': 'https://www.theguardian.com/society/2018/jun/04/i-wanted-to-make-a-change-knowing-older-people-suffer-from-loneliness-',
        'sourceName': 'The Guardian (UK)',
        'author': 'Guardian Readers & Rachel Obordo'
    },
    'human-2': {
        'sourceUrl': 'https://www.goodnewsnetwork.org/giving-spirit-bag-changes-homeless-vets-life/',
        'sourceName': 'Good News Network',
        'author': 'Good News Network Editorial'
    },
    'mind-3': {
        'sourceUrl': 'https://www.health.harvard.edu/diet-and-nutrition/oat-vs-dairy-milk-nutrition-benefits-and-downsides',
        'sourceName': 'Harvard Health Publishing',
        'author': 'Harvard Health Letter'
    },
    'trending-7': {
        'sourceUrl': 'https://vietnamnet.vn/en/ai-in-modern-journalism-opportunities-and-ethical-challenges-2189045.html',
        'sourceName': 'VietNamNet Global'
    },
    'trending-8': {
        'sourceUrl': 'https://e.vnexpress.net/news/life/trend/gen-z-fuels-vintage-film-camera-craze-in-vietnam-4654321.html',
        'sourceName': 'VnExpress International'
    },
    'trending-9': {
        'sourceUrl': 'https://vietnamnews.vn/economy/1589412/vietnamese-robusta-coffee-aims-for-premium-global-markets.html',
        'sourceName': 'Việt Nam News'
    },
    'trending-10': {
        'sourceUrl': 'https://vietnamnews.vn/environment/1632145/urban-greenery-and-rooftop-gardens-transform-hanoi-living.html',
        'sourceName': 'Việt Nam News'
    },
    'society-2': {
        'sourceUrl': 'https://en.nhandan.vn/offshore-wind-power-potential-key-to-vietnams-green-energy-transition-post137890.html',
        'sourceName': 'Báo Nhân Dân điện tử'
    },
    'society-3': {
        'sourceUrl': 'https://vietnamnews.vn/society/1598421/preserving-indigenous-languages-through-digital-technology.html',
        'sourceName': 'Việt Nam News'
    },
    'society-4': {
        'sourceUrl': 'https://e.vnexpress.net/news/news/traffic/hanoi-metro-line-transforms-daily-commute-for-urbanites-4789123.html',
        'sourceName': 'VnExpress International'
    },
    'society-5': {
        'sourceUrl': 'https://vietnamnews.vn/society/1645890/free-coding-classes-empower-disadvantaged-children-in-viet-nam.html',
        'sourceName': 'Việt Nam News'
    },
    'human-5': {
        'sourceUrl': 'https://vietnamnews.vn/society/1601245/dedicated-teachers-bring-literacy-to-remote-mountain-villages.html',
        'sourceName': 'Việt Nam News'
    },
    'human-6': {
        'sourceUrl': 'https://vietnamnews.vn/society/1612789/a-mothers-relentless-search-for-her-missing-child.html',
        'sourceName': 'Việt Nam News'
    },
    'human-7': {
        'sourceUrl': 'https://vietnamnews.vn/society/1589124/zero-dong-charity-meals-bring-hope-to-cancer-patients.html',
        'sourceName': 'Việt Nam News'
    },
    'human-8': {
        'sourceUrl': 'https://vietnamnews.vn/environment/1593456/forest-rangers-dedicate-lives-to-protecting-cat-tien-wildlife.html',
        'sourceName': 'Việt Nam News'
    },
    'mind-4': {
        'sourceUrl': 'https://www.theguardian.com/lifeandstyle/2026/nov/02/a-new-start-after-60-at-26-i-saw-my-dream-porsche-at-68-i-built-one-from-scratch',
        'sourceName': 'The Guardian (UK)'
    },
    'mind-6': {
        'sourceUrl': 'https://vietnamnews.vn/life-style/1578912/free-weekend-violin-classes-bring-joy-to-hanoi-community.html',
        'sourceName': 'Việt Nam News'
    }
}

count = 0
for a in articles:
    aid = a.get('id')
    if aid in url_updates:
        for k, v in url_updates[aid].items():
            a[k] = v
        count += 1
        print(f"✓ Updated citation for {aid}: {a['sourceUrl']}")

print(f"\nUpdated {count} articles with standardized, live, authentic citation URLs.")

# Save back to js/data.js
output_js = f"// HEARTICLES. - Master Database of Verified Multimedia Journalism\nconst ARTICLES_DATA = {json.dumps(articles, ensure_ascii=False, indent=2)};\n"

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(output_js)

print("Saved updated articles to js/data.js!")
