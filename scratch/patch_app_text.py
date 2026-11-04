import sys

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

# 1. Video desc
js = js.replace(
    'style="color:var(--color-text-muted); font-size:0.9rem; line-height:1.5;">${mainClip.desc}</p>',
    'style="color:var(--color-text-body); font-size:0.95rem; line-height:1.6; font-weight:500;">${mainClip.desc}</p>'
)

# 2. About section
js = js.replace(
    'style="font-size:0.8125rem; color:var(--color-text-muted); line-height:1.5;">\n            Biểu trưng trái tim',
    'style="font-size:0.875rem; color:var(--color-text-body); line-height:1.6; font-weight:500;">\n            Biểu trưng trái tim'
)
js = js.replace(
    'style="font-size:0.75rem; color:var(--color-text-muted); margin-top:0.3rem;">Cố vấn định hướng',
    'style="font-size:0.8125rem; color:var(--color-text-muted); font-weight:500; margin-top:0.3rem;">Cố vấn định hướng'
)
js = js.replace(
    'style="font-size:0.75rem; color:var(--color-text-muted); margin-top:0.3rem;">Sáng tạo nội dung',
    'style="font-size:0.8125rem; color:var(--color-text-muted); font-weight:500; margin-top:0.3rem;">Sáng tạo nội dung'
)
js = js.replace(
    'style="font-size:0.75rem; color:var(--color-text-muted); margin-top:0.3rem;">Phát triển giao diện',
    'style="font-size:0.8125rem; color:var(--color-text-muted); font-weight:500; margin-top:0.3rem;">Phát triển giao diện'
)

# 3. Article reading modal sapo & body
js = js.replace(
    'style="font-family:var(--font-serif); font-size:1.15rem; line-height:1.6; color:var(--color-text-muted); margin-bottom:1.5rem;">${article.subtitle}</p>',
    'style="font-family:var(--font-serif); font-size:1.22rem; line-height:1.65; color:var(--color-text-body); font-weight:600; margin-bottom:1.5rem;">${article.subtitle}</p>'
)
js = js.replace(
    'style="font-size:0.75rem; color:var(--color-text-muted);">${article.date}</div>',
    'style="font-size:0.8125rem; color:var(--color-text-muted); font-weight:600;">${article.date}</div>'
)
js = js.replace(
    'style="font-size:0.8125rem; color:var(--color-text-muted); padding:0.5rem 0.25rem;">${article.imageCaption || article.title}</div>',
    'style="font-size:0.875rem; color:var(--color-text-muted); font-weight:500; font-style:italic; padding:0.6rem 0.25rem;">${article.imageCaption || article.title}</div>'
)
js = js.replace(
    'style="font-family:var(--font-body); font-size:1.125rem; line-height:1.8;">',
    'style="font-family:var(--font-body); font-size:1.18rem; line-height:1.85; color:var(--color-text-body);">'
)

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js)

print("js/app.js updated with high-contrast text styles successfully!")
