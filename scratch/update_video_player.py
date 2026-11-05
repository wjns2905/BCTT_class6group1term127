# -*- coding: utf-8 -*-
import sys

app_js_path = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js"

with open(app_js_path, "r", encoding="utf-8") as f:
    js = f.read()

# Replace playerStageHtml
target_stage = """  const playerStageHtml = (isYouTube && isVideoPlaying)
    ? `<div class="video-responsive-embed">
         <iframe id="activeVideoFrame" 
           src="${mainClip.embedUrl}?autoplay=1&rel=0&modestbranding=1" 
           title="${mainTitle}" 
           allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
           referrerpolicy="strict-origin-when-cross-origin" 
           allowfullscreen>
         </iframe>
       </div>`
    : `<div class="video-poster-stage" onclick="${isYouTube ? `playActiveVideo('${mainClip.id}')` : `window.open('${mainClip.watchUrl}', '_blank')`}" title="${isEn ? (isYouTube ? 'Click to Play' : 'Click to Watch on VTV Today') : (isYouTube ? 'Nhấp để phát video' : 'Nhấp để xem trên VTV Today')}">"""

rep_stage = """  const playerStageHtml = (isYouTube && isVideoPlaying)
    ? (isFileProtocol
        ? `<div class="video-poster-stage" style="cursor:default;">
             <img src="${mainClip.thumb}" alt="${mainTitle}" class="video-poster-img" onerror="handleImageError(this)">
             <div class="video-poster-overlay" style="background:rgba(20, 16, 17, 0.85);"></div>
             <div class="video-play-center" style="max-width:480px; text-align:center; padding:1.5rem;">
               <div style="font-size:2.8rem; color:#FF0000; margin-bottom:0.75rem;"><i class="fab fa-youtube"></i></div>
               <h3 style="font-family:var(--font-editorial); font-size:1.25rem; color:#FFF; margin-bottom:0.5rem;">${mainTitle}</h3>
               <p style="font-size:0.85rem; color:rgba(255,255,255,0.85); line-height:1.5; margin-bottom:1.25rem;">
                 ${isEn 
                   ? 'Opening via local file (file://): YouTube blocks inline embedding to protect origin headers (Error 153). Watch directly in crystal-clear 1080p Full HD on YouTube.' 
                   : 'Do bạn đang mở tệp trực tiếp từ máy tính (file://): YouTube kích hoạt chính sách bảo mật chặn nhúng (Lỗi 153). Mời bạn bấm nút dưới để xem trực tiếp chuẩn Full HD trên YouTube.'}
               </p>
               <div style="display:flex; justify-content:center; gap:0.75rem; flex-wrap:wrap;">
                 <a href="${mainClip.watchUrl}" target="_blank" rel="noopener noreferrer" class="fashion-btn-pill" style="background:#FF0000; color:#FFF; font-weight:700; padding:0.65rem 1.4rem; text-decoration:none; display:inline-flex; align-items:center; gap:0.5rem; border-radius:30px; box-shadow:0 4px 14px rgba(255,0,0,0.4);">
                   <i class="fab fa-youtube"></i> <span>${isEn ? 'Watch on YouTube ↗' : 'Xem ngay trên YouTube ↗'}</span>
                 </a>
                 <button onclick="isVideoPlaying=false; renderVideoHub();" class="fashion-btn-pill" style="background:rgba(255,255,255,0.15); color:#FFF; padding:0.65rem 1.2rem; border:1px solid rgba(255,255,255,0.3); border-radius:30px; cursor:pointer;">
                   ${isEn ? 'Back to Poster' : 'Quay lại bìa'}
                 </button>
               </div>
             </div>
           </div>`
        : `<div class="video-responsive-embed">
             <iframe id="activeVideoFrame" 
               src="${mainClip.embedUrl}?autoplay=1&rel=0&modestbranding=1" 
               title="${mainTitle}" 
               allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
               referrerpolicy="strict-origin-when-cross-origin" 
               allowfullscreen>
             </iframe>
           </div>`)
    : `<div class="video-poster-stage" onclick="${isYouTube ? `playActiveVideo('${mainClip.id}')` : `window.open('${mainClip.watchUrl}', '_blank')`}" title="${isEn ? (isYouTube ? 'Click to Play' : 'Click to Watch on VTV Today') : (isYouTube ? 'Nhấp để phát video' : 'Nhấp để xem trên VTV Today')}">"""

# Replace playActiveVideo
target_play = """function playActiveVideo(clipId) {
  if (clipId) currentActiveClipId = clipId;
  isVideoPlaying = true;
  renderVideoHub();
}"""

rep_play = """function playActiveVideo(clipId) {
  if (clipId) currentActiveClipId = clipId;
  const clip = VIDEO_CLIPS.find(c => c.id === currentActiveClipId) || VIDEO_CLIPS[0];
  const isFileProtocol = (window.location.protocol === 'file:' || !window.location.protocol.startsWith('http'));

  if (clip.sourceType === 'youtube' && isFileProtocol) {
    window.open(clip.watchUrl, '_blank');
    if (typeof showToast === 'function') {
      showToast(currentLanguage === 'en' 
        ? 'Opening video on YouTube in Full HD (local file mode)' 
        : 'Đang mở video Full HD trên YouTube (chế độ tệp cục bộ)', 'info');
    }
    isVideoPlaying = true;
    renderVideoHub();
    return;
  }
  
  if (clip.sourceType === 'vtv') {
    window.open(clip.watchUrl, '_blank');
    return;
  }

  isVideoPlaying = true;
  renderVideoHub();
}"""

if target_stage in js:
    js = js.replace(target_stage, rep_stage)
    print("Successfully replaced playerStageHtml")
else:
    print("Warning: target_stage not found directly, checking normalization")

if target_play in js:
    js = js.replace(target_play, rep_play)
    print("Successfully replaced playActiveVideo")
else:
    print("Warning: target_play not found directly, checking normalization")

with open(app_js_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Saved updated js/app.js")
