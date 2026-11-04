import json
import re

with open("js/data.js", "r", encoding="utf-8") as f:
    text = f.read()

m = re.search(r'const ARTICLES_DATA\s*=\s*(\[\s*\{.*\}\s*\]);', text, re.DOTALL)
articles = json.loads(m.group(1))

for a in articles:
    if a['id'] == 'mind-1':
        a['title_en'] = "After Hanoi concert, BigBang's Taeyang praises Vietnamese pho and calls it 'the best show'"
        a['subtitle_en'] = "The acclaimed BigBang icon expressed profound gratitude and boundless excitement for Vietnamese fans following two historic anniversary concert nights at My Dinh National Stadium."
        a['content_en'] = [
            "The BIGBANG 2026–2027 World Tour in Hanoi took place over two exhilarating nights at My Dinh National Stadium, drawing tens of thousands of passionate fans from across Vietnam and Southeast Asia.",
            "Celebrating the group's 20th anniversary milestone, members G-Dragon, Taeyang, and Daesung reunited on stage, delivering explosive vocal performances and heartfelt interactions that deeply moved the audience.",
            "On October 29, BigBang's main vocalist shared behind-the-scenes clips and reflections on his official social media channels, continuously praising traditional Vietnamese pho and calling Hanoi 'one of the greatest crowds we have ever performed for.'",
            "Cultural commentators emphasized that the concert's remarkable success reflects Vietnam's growing prominence as a vibrant international hub for world-class cultural and musical exchanges."
        ]
    elif a['id'] == 'trending-4':
        a['title_en'] = "Street Vendors with Shoulder Pole: A Timeless Hallmark of Livelihood in Hoi An"
        a['subtitle_en'] = "The rustic beauty of vendors carrying woven baskets on shoulder poles has long been an indispensable, soulful hallmark of the ancient heritage town."
    elif a['id'] == 'indepth-1':
        a['title_en'] = "A Hanoi that never stands still: The bittersweet scent and collective memory of milk flowers"
        a['subtitle_en'] = "The debate over milkwood flowers is not merely about loving or loathing a fragrance; it is about how a thousand-year-old capital preserves its soul amid rapid urbanization."

new_js = f"// HEARTICLES. News Portal Data\n// Modern Minimalist Bilingual Edition (VI / EN)\n// Authentic Articles & Images directly extracted from [BCTT] course resources\n// Class 6 - Group 1 - Term 127 • Trường Đại học Ngoại ngữ - ĐHQGHN (ULIS - VNU)\nconst ARTICLES_DATA = {json.dumps(articles, ensure_ascii=False, indent=2)};\n"

with open("js/data.js", "w", encoding="utf-8") as f:
    f.write(new_js)

print("js/data.js updated with English fields for all articles!")
