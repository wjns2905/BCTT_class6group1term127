import re

path = 'C:/Users/camka/OneDrive/Desktop/BCTT_class6group1term127/js/app.js'
with open(path, 'r', encoding='utf-8') as f:
    code = f.read()

# Helper function definitions for video modal
video_helpers = '''
function renderModalVideoBlock(article, isEn, title) {
  if (!article.video && !article.streamUrl) return '';

  // Case 1: Direct native/HLS stream URL
  if (article.streamUrl) {
    setTimeout(() => {
      attachModalHlsStream(article.streamUrl);
    }, 80);
    return `
      <div class="video-responsive-embed" style="margin-bottom: 2rem; border-radius: 12px; overflow:hidden; background:#000;">
        <video id="activeModalNativePlayer" controls playsinline poster="${article.image}" style="width:100%; max-height:480px; display:block;"></video>
      </div>
    `;
  }

  // Case 2: YouTube / External video
  const ytMatch = (article.video || '').match(/(?:embed\\/|v=|vi\\/|youtu\\.be\\/|\\/v\\/)([a-zA-Z0-9_-]{11})/);
  const ytId = ytMatch ? ytMatch[1] : '';
  const watchUrl = ytId ? `https://www.youtube.com/watch?v=${ytId}` : article.video;
  const isLocalFile = (window.location.protocol === 'file:');

  // If running locally via file://, YouTube iframe player triggers Error 153 due to lack of HTTP origin.
  // We provide a rich, interactive video showcase card with HD thumbnail, Play button, and direct watch / embed options.
  if (isLocalFile && ytId) {
    return `
      <div class="modal-video-card" style="margin-bottom: 2rem; border-radius: 12px; overflow:hidden; border: 1px solid var(--color-border-hairline); box-shadow: 0 4px 16px rgba(0,0,0,0.06); background: var(--color-canvas);">
        <div style="position:relative; aspect-ratio:16/9; background:#000; overflow:hidden;">
          <img src="https://i.ytimg.com/vi/${ytId}/hqdefault.jpg" alt="${title}" style="width:100%; height:100%; object-fit:cover; opacity:0.85;" onerror="handleImageError(this)">
          <div style="position:absolute; inset:0; background:linear-gradient(to top, rgba(0,0,0,0.78) 0%, rgba(0,0,0,0.2) 50%, rgba(0,0,0,0.45) 100%); display:flex; flex-direction:column; justify-content:space-between; padding:1.25rem;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="background:#CC181E; color:#FFF; font-size:0.75rem; font-weight:800; padding:0.25rem 0.65rem; border-radius:4px; letter-spacing:0.06em; text-transform:uppercase;">
                <i class="fab fa-youtube"></i> ${isEn ? 'FEATURED VIDEO REPORT' : 'PHÓNG SỰ VIDEO ĐẶC SẮC'}
              </span>
              <span style="background:rgba(0,0,0,0.7); color:#FFF; font-size:0.75rem; font-weight:600; padding:0.2rem 0.5rem; border-radius:4px;">
                HD 1080p
              </span>
            </div>
            <div style="text-align:center;">
              <a href="${watchUrl}" target="_blank" rel="noopener noreferrer" style="display:inline-flex; align-items:center; justify-content:center; width:64px; height:64px; border-radius:50%; background:#CC181E; color:#FFF; font-size:1.5rem; text-decoration:none; box-shadow:0 4px 18px rgba(204,24,30,0.5); transition:transform 0.2s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'" title="${isEn ? 'Watch on YouTube' : 'Xem video trên YouTube'}">
                <i class="fas fa-play" style="margin-left:3px;"></i>
              </a>
            </div>
            <div style="color:#FFF;">
              <div style="font-weight:700; font-size:1.05rem; text-shadow:0 2px 4px rgba(0,0,0,0.85);">${title}</div>
            </div>
          </div>
        </div>
        <div style="padding:1rem 1.25rem; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.75rem;">
          <div style="font-size:0.825rem; color:var(--color-text-muted);">
            <i class="fas fa-info-circle"></i> ${isEn ? 'High-definition video report from verified broadcasting source' : 'Phóng sự tài liệu độ nét cao từ kênh phát sóng chính thức'}
          </div>
          <div style="display:flex; gap:0.5rem; align-items:center;">
            <a href="${watchUrl}" target="_blank" rel="noopener noreferrer" class="fashion-btn-pill" style="background:#CC181E; color:#FFF; font-size:0.825rem; padding:0.45rem 1rem; text-decoration:none; display:inline-flex; align-items:center; gap:0.4rem; font-weight:700;">
              <i class="fab fa-youtube"></i> ${isEn ? 'Watch on YouTube ↗' : 'Xem trên YouTube ↗'}
            </a>
            <button onclick="forceEmbedModalVideo('${ytId}')" class="fashion-btn-pill" style="background:var(--color-bg-alt, #EEE); color:var(--color-text-headline); font-size:0.825rem; padding:0.45rem 0.85rem; border:none; cursor:pointer;">
              ${isEn ? 'Try Embed' : 'Thử phát nhúng'}
            </button>
          </div>
        </div>
        <div id="modalVideoEmbedSlot" style="display:none;"></div>
      </div>
    `;
  }

  // If running via HTTP/HTTPS (or non-file protocol)
  return `
    <div class="video-responsive-embed" style="margin-bottom: 2rem; border-radius: 12px; overflow:hidden;">
      <iframe src="https://www.youtube-nocookie.com/embed/${ytId}?rel=0&modestbranding=1" title="${title}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
    <div style="margin-top:-1.5rem; margin-bottom:2rem; text-align:right;">
      <a href="${watchUrl}" target="_blank" rel="noopener noreferrer" style="font-size:0.825rem; color:var(--color-brand-primary); font-weight:600; text-decoration:none; display:inline-flex; align-items:center; gap:0.35rem;">
        <i class="fab fa-youtube"></i> ${isEn ? 'Open in YouTube ↗' : 'Mở trên YouTube ↗'}
      </a>
    </div>
  `;
}
window.renderModalVideoBlock = renderModalVideoBlock;

function forceEmbedModalVideo(ytId) {
  const slot = document.getElementById('modalVideoEmbedSlot');
  if (!slot) return;
  slot.style.display = 'block';
  slot.innerHTML = `
    <div class="video-responsive-embed" style="border-radius:0 0 12px 12px; overflow:hidden;">
      <iframe src="https://www.youtube-nocookie.com/embed/${ytId}?autoplay=1&rel=0" title="Video Player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
  `;
}
window.forceEmbedModalVideo = forceEmbedModalVideo;

function attachModalHlsStream(streamUrl) {
  setTimeout(() => {
    const videoEl = document.getElementById('activeModalNativePlayer');
    if (!videoEl || !streamUrl) return;
    if (window.Hls && window.Hls.isSupported()) {
      const hls = new window.Hls();
      hls.loadSource(streamUrl);
      hls.attachMedia(videoEl);
    } else if (videoEl.canPlayType('application/vnd.apple.mpegurl')) {
      videoEl.src = streamUrl;
    }
  }, 100);
}
window.attachModalHlsStream = attachModalHlsStream;
'''

# Find the target block in openArticleModal
old_video_target = '''      ${article.video ? `
        <div class="video-responsive-embed" style="margin-bottom: 2rem; border-radius: 12px; overflow:hidden;">
          <iframe src="${article.video}" title="Video phóng sự kèm bài viết" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        </div>
      ` : ''}'''

new_video_target = '''      ${renderModalVideoBlock(article, isEn, title)}'''

if old_video_target in code:
    code = code.replace(old_video_target, new_video_target)
    print("Replaced video block in openArticleModal")
else:
    # Try regex match
    pattern = r'\$\{article\.video \? `[\s\S]*?<iframe src="\$\{article\.video\}"[\s\S]*?` : \'\'\}'
    code, count = re.subn(pattern, new_video_target, code)
    print(f"Replaced video block via regex: {count}")

# Insert helper functions before openArticleModal
if 'function renderModalVideoBlock' not in code:
    code = code.replace('function openArticleModal(articleId) {', video_helpers + '\nfunction openArticleModal(articleId) {\n')
    print("Inserted video helpers before openArticleModal")

# Update closeArticleModal to stop video playback
old_close = '''function closeArticleModal() {
  const modal = document.getElementById('articleReaderModal');
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }
  if (isSpeaking) {
    stopTextToSpeech();
  }
}'''

new_close = '''function closeArticleModal() {
  const modal = document.getElementById('articleReaderModal');
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';
    const body = document.getElementById('articleModalBody');
    if (body) {
      body.querySelectorAll('iframe, video').forEach(el => {
        try {
          if (el.tagName && el.tagName.toLowerCase() === 'video') el.pause();
          el.src = '';
        } catch (e) {}
      });
    }
  }
  if (isSpeaking) {
    stopTextToSpeech();
  }
}'''

if old_close in code:
    code = code.replace(old_close, new_close)
    print("Updated closeArticleModal successfully")

with open(path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated app.js successfully")
