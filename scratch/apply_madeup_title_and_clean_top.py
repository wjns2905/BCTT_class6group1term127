# -*- coding: utf-8 -*-
"""
Apply user request:
1. Prepend "[Made-up article] " to the title of trending-1 in VI and EN.
2. Remove top hero image and top video from the beginning of trending-1.
"""

import os
import re

BASE_DIR = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127"
DATA_JS = os.path.join(BASE_DIR, "js", "data.js")
TRANS_JS = os.path.join(BASE_DIR, "js", "translations.js")
APP_JS = os.path.join(BASE_DIR, "js", "app.js")
MADEUP_INDEX = os.path.join(BASE_DIR, "hearticles", "madeuparticle", "index.html")
INDEX_HTML = os.path.join(BASE_DIR, "index.html")
TRENDING_HTML = os.path.join(BASE_DIR, "trending.html")

# 1. Update js/data.js
with open(DATA_JS, "r", encoding="utf-8") as f:
    data_content = f.read()

# Replace title and title_en for trending-1
old_title_vi = '"title": "Cô gái say rượu ngã gục trên ghế, bất ngờ nhận được sự giúp đỡ “đặc biệt” từ người qua đường",'
new_title_vi = '"title": "[Made-up article] Cô gái say rượu ngã gục trên ghế, bất ngờ nhận được sự giúp đỡ “đặc biệt” từ người qua đường",'
old_title_en = '"title_en": "Drunk Girl Collapses on Park Bench, Unexpectedly Receives \'Special\' Kindness from Strangers",'
new_title_en = '"title_en": "[Made-up article] Drunk Girl Collapses on Park Bench, Unexpectedly Receives \'Special\' Kindness from Strangers",'

data_content = data_content.replace(old_title_vi, new_title_vi)
data_content = data_content.replace(old_title_en, new_title_en)

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(data_content)
print("Updated js/data.js with [Made-up article] prefix.")

# 2. Update js/translations.js
with open(TRANS_JS, "r", encoding="utf-8") as f:
    trans_content = f.read()

trans_content = trans_content.replace(
    'focal_lead_title: "Cô gái say rượu ngã gục trên ghế, bất ngờ nhận được sự giúp đỡ “đặc biệt” từ người qua đường",',
    'focal_lead_title: "[Made-up article] Cô gái say rượu ngã gục trên ghế, bất ngờ nhận được sự giúp đỡ “đặc biệt” từ người qua đường",'
)
trans_content = trans_content.replace(
    'cat_feat_trending_title: "Cô gái say rượu ngã gục trên ghế, bất ngờ nhận được sự giúp đỡ “đặc biệt” từ người qua đường",',
    'cat_feat_trending_title: "[Made-up article] Cô gái say rượu ngã gục trên ghế, bất ngờ nhận được sự giúp đỡ “đặc biệt” từ người qua đường",'
)
trans_content = trans_content.replace(
    'focal_lead_title: "Drunk Girl Collapses on Park Bench, Unexpectedly Receives \'Special\' Kindness from Strangers",',
    'focal_lead_title: "[Made-up article] Drunk Girl Collapses on Park Bench, Unexpectedly Receives \'Special\' Kindness from Strangers",'
)
trans_content = trans_content.replace(
    'cat_feat_trending_title: "Drunk Girl Collapses on Park Bench, Unexpectedly Receives \'Special\' Kindness from Strangers",',
    'cat_feat_trending_title: "[Made-up article] Drunk Girl Collapses on Park Bench, Unexpectedly Receives \'Special\' Kindness from Strangers",'
)

with open(TRANS_JS, "w", encoding="utf-8") as f:
    f.write(trans_content)
print("Updated js/translations.js with [Made-up article] prefix.")

# 3. Update index.html and trending.html
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    idx_content = f.read()

idx_content = idx_content.replace(
    "Drunk Girl Collapses on Park Bench, Unexpectedly Receives 'Special' Kindness from Strangers",
    "[Made-up article] Drunk Girl Collapses on Park Bench, Unexpectedly Receives 'Special' Kindness from Strangers"
)
with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(idx_content)
print("Updated index.html.")

with open(TRENDING_HTML, "r", encoding="utf-8") as f:
    tre_content = f.read()

tre_content = tre_content.replace(
    "Drunk Girl Collapses on Park Bench, Unexpectedly Receives 'Special' Kindness from Strangers",
    "[Made-up article] Drunk Girl Collapses on Park Bench, Unexpectedly Receives 'Special' Kindness from Strangers"
)
with open(TRENDING_HTML, "w", encoding="utf-8") as f:
    f.write(tre_content)
print("Updated trending.html.")

# 4. Update js/app.js to remove top hero image and video for trending-1
with open(APP_JS, "r", encoding="utf-8") as f:
    app_content = f.read()

old_host_inner = """      <div class="article-hero-media" style="border-radius:var(--radius-lg); overflow:hidden; margin:2rem 0; box-shadow:0 6px 24px rgba(0,0,0,0.06);">
        <img src="${heroImgSrc}" alt="${title}" style="width:100%; display:block; max-height:560px; object-fit:cover;" onerror="handleImageError(this)">
        <div class="article-media-caption" style="font-size:0.85rem; color:var(--color-text-muted); padding:0.6rem 0.5rem; font-style:italic; line-height:1.5;">${article.imageCaption || title}</div>
      </div>

      ${renderModalVideoBlock(article, isEn, title)}"""

new_host_inner = """      ${(article.id === 'trending-1') ? '' : `
      <div class="article-hero-media" style="border-radius:var(--radius-lg); overflow:hidden; margin:2rem 0; box-shadow:0 6px 24px rgba(0,0,0,0.06);">
        <img src="${heroImgSrc}" alt="${title}" style="width:100%; display:block; max-height:560px; object-fit:cover;" onerror="handleImageError(this)">
        <div class="article-media-caption" style="font-size:0.85rem; color:var(--color-text-muted); padding:0.6rem 0.5rem; font-style:italic; line-height:1.5;">${article.imageCaption || title}</div>
      </div>

      ${renderModalVideoBlock(article, isEn, title)}
      `}"""

if old_host_inner in app_content:
    app_content = app_content.replace(old_host_inner, new_host_inner)
    print("Replaced top media block in js/app.js.")
else:
    print("WARNING: Could not find exact old_host_inner in js/app.js!")

with open(APP_JS, "w", encoding="utf-8") as f:
    f.write(app_content)

# 5. Update hearticles/madeuparticle/index.html
with open(MADEUP_INDEX, "r", encoding="utf-8") as f:
    madeup_content = f.read()

# Update title and meta in hearticles/madeuparticle/index.html
madeup_content = madeup_content.replace(
    "<title>Class6group1term127 - Drunk Girl Collapses on Park Bench</title>",
    "<title>Class6group1term127 - [Made-up article] Drunk Girl Collapses on Park Bench</title>"
)
madeup_content = madeup_content.replace(
    '<meta name="description" content="Hot Paper: Drunk Girl Collapses on Park Bench, Unexpectedly Receives \'Special\' Kindness from Strangers - HEARTICLES. Magazine">',
    '<meta name="description" content="Hot Paper: [Made-up article] Drunk Girl Collapses on Park Bench, Unexpectedly Receives \'Special\' Kindness from Strangers - HEARTICLES. Magazine">'
)
madeup_content = madeup_content.replace(
    '<meta property="og:title" content="Drunk Girl Collapses on Park Bench, Unexpectedly Receives \'Special\' Kindness from Strangers">',
    '<meta property="og:title" content="[Made-up article] Drunk Girl Collapses on Park Bench, Unexpectedly Receives \'Special\' Kindness from Strangers">'
)

# Update headline in pre-rendered body
madeup_content = madeup_content.replace(
    '<h1 class="article-headline" style="font-family:var(--font-editorial); font-size:clamp(1.85rem, 4vw, 2.75rem); font-weight:900; line-height:1.25; margin-bottom:1rem; color:var(--color-text-headline); letter-spacing:-0.02em;">Cô gái say rượu ngã gục trên ghế, bất ngờ nhận được sự giúp đỡ “đặc biệt” từ người qua đường</h1>',
    '<h1 class="article-headline" style="font-family:var(--font-editorial); font-size:clamp(1.85rem, 4vw, 2.75rem); font-weight:900; line-height:1.25; margin-bottom:1rem; color:var(--color-text-headline); letter-spacing:-0.02em;">[Made-up article] Cô gái say rượu ngã gục trên ghế, bất ngờ nhận được sự giúp đỡ “đặc biệt” từ người qua đường</h1>'
)

# Remove the top hero media and top CCTV video block in hearticles/madeuparticle/index.html
old_pre_media = """        <div class="article-hero-media" style="border-radius:var(--radius-lg); overflow:hidden; margin:2rem 0; box-shadow:0 6px 24px rgba(0,0,0,0.06);">
          <img src="../../assets/images/trending/ngoc_mai/hat_and_jacket.jpg" alt="Cô gái say rượu ngã gục trên ghế" style="width:100%; display:block; max-height:560px; object-fit:cover;" onerror="handleImageError(this)">
          <div class="article-media-caption" style="font-size:0.85rem; color:var(--color-text-muted); padding:0.6rem 0.5rem; font-style:italic; line-height:1.5;">Hình ảnh chiếc mũ có tiền lẻ và chiếc áo khoác đắp ấm trong câu chuyện của Ngọc Mãi. (Nguồn: Nhân vật cung cấp)</div>
        </div>

        <!-- CCTV Video Player -->
        <div class="video-responsive-embed" style="margin-bottom: 2rem; border-radius: 12px; overflow:hidden; background:#000; box-shadow: 0 4px 18px rgba(0,0,0,0.14);">
          <video id="activeModalNativePlayer" controls playsinline poster="../../assets/images/trending/ngoc_mai/hat_and_jacket.jpg" preload="metadata" style="width:100%; max-height:500px; display:block; margin:0 auto; background:#000;">
            <source src="../../assets/videos/cctv_ulus_park_kindness.mp4" type="video/mp4">
            Trình duyệt của bạn không hỗ trợ video HTML5.
          </video>
          <div style="background:#161616; color:#E0E0E0; padding:0.65rem 1rem; font-size:0.8125rem; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; border-top:1px solid #282828;">
            <span><i class="fas fa-video" style="color:var(--color-brand-accent, #80182A);"></i> Camera an ninh khu vực: Toàn bộ video trích xuất ghi lại sự việc lòng tốt của người qua đường.</span>
            <span style="background:rgba(255,255,255,0.12); padding:2px 8px; border-radius:4px; font-size:0.75rem; font-weight:700;">1080p MP4</span>
          </div>
        </div>"""

if old_pre_media in madeup_content:
    madeup_content = madeup_content.replace(old_pre_media, "")
    print("Removed top hero media & top CCTV video from hearticles/madeuparticle/index.html.")
else:
    print("WARNING: Could not find old_pre_media in hearticles/madeuparticle/index.html!")

with open(MADEUP_INDEX, "w", encoding="utf-8") as f:
    f.write(madeup_content)

print("\nSUCCESS: All files updated.")
