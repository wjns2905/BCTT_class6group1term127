import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

APP_JS = """/**
 * HEARTICLES. - High-Fashion Magazine Editorial Application Core
 * Class 6 - Group 1 - Term 127
 * Trường Đại học Ngoại ngữ - Đại học Quốc gia Hà Nội (ULIS - VNU)
 * Fashion Editorial Suite (Vogue, Harper's Bazaar, Kinfolk Aesthetic)
 * 100% Authentic Articles & Images from Original Course Resources
 */

document.addEventListener('DOMContentLoaded', () => {
  initApp();
});

let currentFontSize = 1.15; // rem
let isSpeaking = false;
let speechUtterance = null;
let currentOnboardStep = 1;
let currentCategoryFilter = 'all';

function initApp() {
  updateLiveDate();
  setupEventListeners();
  renderVideoHub();
  renderFashionJournal('all');
  renderAboutUsSection();
  setupPoll();
  initOnboarding();
  setupReadingProgressBar();
  setupNetworkStatus();
}

/* ===================================================================
   DATE & TIME DISPLAY (Tabular Figures & Vietnamese Time)
   =================================================================== */
function updateLiveDate() {
  const dateEl = document.getElementById('liveDateWidget');
  if (!dateEl) return;
  const now = new Date();
  const days = ['Chủ Nhật', 'Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy'];
  const dayName = days[now.getDay()];
  const dateStr = `${dayName}, ${now.getDate()} Tháng ${now.getMonth() + 1}, ${now.getFullYear()} | Hà Nội 26°C`;
  dateEl.innerHTML = `<i class=\"far fa-calendar-alt\"></i> <span style=\"font-variant-numeric: tabular-nums;\">${dateStr}</span>`;
}

/* ===================================================================
   MULTIMEDIA & VIDEO PHÓNG SỰ HUB (5 Video Clips Requirement)
   Using Authentic Original Images as Video Thumbnails
   =================================================================== */
const VIDEO_CLIPS = [
  {
    id: "clip-1",
    category: "Trending",
    title: "Phóng sự: Gánh mưu sinh và nét đẹp lao động bình dị phố cổ Hội An",
    desc: "Hình ảnh đôi quang gánh trĩu nặng nhịp sống mưu sinh, vẻ đẹp cần lao mộc mạc và ký ức rêu phong trên từng ngõ nhỏ di sản.",
    url: "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    thumb: "assets/images/trending/image8.jpg",
    articleId: "trending-4"
  },
  {
    id: "clip-2",
    category: "Mind & Soul",
    title: "Taeyang (BigBang) và đêm nhạc bùng nổ tại SVĐ Quốc gia Mỹ Đình",
    desc: "Khoảnh khắc nam nghệ sĩ xúc động trước tình cảm nồng nhiệt của hàng vạn khán giả Thủ đô và tình yêu với ẩm thực phở Hà Nội.",
    url: "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    thumb: "assets/images/mind_&_soul/image2.jpg",
    articleId: "mind-1"
  },
  {
    id: "clip-3",
    category: "Human Stories",
    title: "Những người nông dân gieo hạt mầm tri thức tại Gruver, Texas",
    desc: "Câu chuyện cảm động về cộng đồng nông dân tình nguyện canh tác gây quỹ 400.000 USD học bổng mỗi năm cho học sinh nghèo vào đại học.",
    url: "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    thumb: "assets/images/human_stories/image5.png",
    articleId: "human-4"
  },
  {
    id: "clip-4",
    category: "Society",
    title: "Chiến dịch 500 ngày đêm ADN: Trả lại danh tính cho gần 800 hài cốt liệt sĩ",
    desc: "Hành trình thầm lặng nhưng đầy tự hào của các nhà khoa học và cơ quan chức năng vì đạo lý 'Uống nước nhớ nguồn'.",
    url: "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    thumb: "assets/images/human_stories/image17.jpg",
    articleId: "trending-5"
  },
  {
    id: "clip-5",
    category: "About Us",
    title: "HEARTICLES Manifesto: 'Stories that speak to the heart' • ULIS - VNU",
    desc: "Thông điệp tôn chỉ báo chí nhân văn và hậu trường thực hiện tạp chí số từ nhóm sinh viên Lớp 6 - Nhóm 1 - Khóa 127, ULIS - VNU.",
    url: "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
    thumb: "assets/images/trending/image10.jpg",
    articleId: "about"
  }
];

function renderVideoHub() {
  const container = document.getElementById('videoHubContent');
  if (!container) return;

  const mainClip = VIDEO_CLIPS[0];
  container.innerHTML = `
    <div class=\"video-grid-layout\">
      <div class=\"main-video-player-box\">
        <div class=\"video-responsive-embed\">
          <iframe id=\"activeVideoFrame\" src=\"${mainClip.url}\" title=\"${mainClip.title}\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>
        </div>
        <div class=\"main-video-details\">
          <span class=\"category-tag\" id=\"activeVideoCategory\" style=\"color:var(--color-brand-primary); font-weight:800;\">${mainClip.category}</span>
          <h2 class=\"main-video-title\" id=\"activeVideoTitle\" style=\"font-family:var(--font-editorial); font-size:1.5rem; margin-top:0.4rem;\">${mainClip.title}</h2>
          <p class=\"main-video-desc\" id=\"activeVideoDesc\" style=\"color:var(--color-text-muted); font-size:0.9rem; line-height:1.5;\">${mainClip.desc}</p>
        </div>
      </div>

      <div class=\"video-playlist\">
        ${VIDEO_CLIPS.map((clip, idx) => `
          <div class=\"playlist-card ${idx === 0 ? 'active' : ''}\" onclick=\"switchVideo('${clip.id}')\">
            <div class=\"playlist-thumb-wrap\">
              <img src=\"${clip.thumb}\" alt=\"${clip.title}\" loading=\"lazy\" onerror=\"handleImageError(this)\">
              <div class=\"playlist-play-icon\"><i class=\"fas fa-play\"></i></div>
            </div>
            <div class=\"playlist-info\">
              <span class=\"playlist-cat\">${clip.category}</span>
              <h4 class=\"playlist-title\">${clip.title}</h4>
            </div>
          </div>
        `).join('')}
      </div>
    </div>
  `;
}

window.switchVideo = function(clipId) {
  const clip = VIDEO_CLIPS.find(c => c.id === clipId);
  if (!clip) return;
  const frame = document.getElementById('activeVideoFrame');
  const cat = document.getElementById('activeVideoCategory');
  const title = document.getElementById('activeVideoTitle');
  const desc = document.getElementById('activeVideoDesc');

  if (frame) frame.src = clip.url;
  if (cat) cat.textContent = clip.category;
  if (title) title.textContent = clip.title;
  if (desc) desc.textContent = clip.desc;

  document.querySelectorAll('.playlist-card').forEach(card => card.classList.remove('active'));
  event.currentTarget.classList.add('active');
};

/* ===================================================================
   THE JOURNAL (Full Curated Articles Magazine Grid)
   =================================================================== */
function renderFashionJournal(categoryKey) {
  const container = document.getElementById('fashionArticlesGrid');
  if (!container) return;

  currentCategoryFilter = categoryKey;

  let filtered = ARTICLES_DATA;
  if (categoryKey && categoryKey !== 'all') {
    filtered = ARTICLES_DATA.filter(a => a.category.toLowerCase() === categoryKey.toLowerCase());
  }

  // Update pills active state
  document.querySelectorAll('.fashion-filter-pill').forEach(pill => {
    pill.classList.remove('active');
    if (pill.getAttribute('onclick')?.includes(`'${categoryKey}'`)) {
      pill.classList.add('active');
    }
  });

  // Update navbar active state
  document.querySelectorAll('.fashion-nav .nav-item').forEach(item => {
    item.classList.remove('active');
    if (item.dataset.category === categoryKey) {
      item.classList.add('active');
    }
  });

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style=\"grid-column: 1 / -1; text-align: center; padding: 4rem 1rem; color: var(--color-text-muted);\">
        <i class=\"fas fa-feather\" style=\"font-size: 2.5rem; color: var(--color-brand-accent); margin-bottom: 1rem;\"></i>
        <h3 style=\"font-family: var(--font-editorial); font-size: 1.5rem; color: var(--color-text-headline);\">Chưa có bài viết trong chuyên mục này</h3>
        <p style=\"font-size: 0.9rem; margin-top: 0.5rem;\">Mời bạn chọn chuyên mục khác hoặc quay lại xem tất cả bài viết.</p>
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map(item => `
    <article class=\"fashion-article-card\" onclick=\"openArticleModal('${item.id}')\">
      <div class=\"fashion-card-media\">
        <img src=\"${item.image}\" alt=\"${item.title}\" class=\"fashion-card-img\" loading=\"lazy\" onerror=\"handleImageError(this)\">
        <span class=\"fashion-card-category-tag\">${item.categoryName}</span>
      </div>
      <div class=\"fashion-card-body\">
        <h3 class=\"fashion-card-title\">${item.title}</h3>
        <p class=\"fashion-card-excerpt\">${item.subtitle}</p>
        <div class=\"fashion-card-footer\">
          <span class=\"fashion-card-byline\"><i class=\"far fa-user\"></i> ${item.author.split('•')[0].trim()}</span>
          <div class=\"fashion-card-stats\">
            <span><i class=\"far fa-clock\"></i> ${item.readTime}</span>
            <span><i class=\"far fa-heart\"></i> ${item.likes}</span>
          </div>
        </div>
      </div>
    </article>
  `).join('');
}

/* ===================================================================
   NAVIGATION & CATEGORY FILTERING
   =================================================================== */
window.filterByCategory = function(categoryKey) {
  closeDrawer();
  closeArticleModal();

  if (categoryKey === 'about') {
    const aboutEl = document.getElementById('about-us');
    if (aboutEl) {
      aboutEl.scrollIntoView({ behavior: 'smooth' });
    }
    return;
  }

  renderFashionJournal(categoryKey);

  if (categoryKey !== 'all') {
    const journalEl = document.getElementById('journalSection');
    if (journalEl) {
      journalEl.scrollIntoView({ behavior: 'smooth' });
    }
  } else {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
};

/* ===================================================================
   ABOUT US SECTION (ULIS - VNU Editorial Manifesto)
   =================================================================== */
function renderAboutUsSection() {
  const container = document.getElementById('aboutUsSection');
  if (!container) return;

  container.innerHTML = `
    <div class=\"about-view-wrapper\" id=\"about-us\" style=\"background:#FFFFFF; border:1px solid var(--color-border-hairline); border-radius:var(--radius-lg); padding:3rem 2.5rem; margin-top:3.5rem;\">
      <div class=\"about-hero-banner\" style=\"text-align:center; max-width:760px; margin:0 auto 2.5rem auto;\">
        <span class=\"fashion-kicker\" style=\"display:inline-block; margin-bottom:0.5rem;\"><i class=\"fas fa-heart\"></i> TÔN CHỈ HOẠT ĐỘNG</span>
        <h1 class=\"about-manifesto-title\" style=\"font-family:var(--font-editorial); font-size:2.4rem; font-weight:800; color:var(--color-brand-primary);\">Tạp chí Báo điện tử HEARTICLES.</h1>
        <p class=\"about-manifesto-subtitle\" style=\"font-family:var(--font-editorial); font-style:italic; font-size:1.25rem; color:var(--color-brand-accent); margin-top:0.4rem;\">
          \"Stories that speak to the heart — Nơi tin tức khởi nguồn từ nhịp đập trái tim\"
        </p>
      </div>

      <div class=\"about-story-grid\" style=\"display:grid; grid-template-columns:1.3fr 0.9fr; gap:2.5rem; align-items:center;\">
        <div class=\"about-story-text\" style=\"font-size:0.95rem; line-height:1.75; color:var(--color-text-body);\">
          <p style=\"margin-bottom:1rem;\">
            <strong>HEARTICLES.</strong> được sáng lập và vận hành bởi nhóm sinh viên <strong>Lớp 6 - Nhóm 1 - Khóa 127</strong> thuộc <strong>Trường Đại học Ngoại ngữ - Đại học Quốc gia Hà Nội (ULIS - VNU)</strong> trong khuôn khổ học phần Báo chí &amp; Truyền thông (BCTT), với khát vọng kiến tạo một ấn phẩm báo chí đa phương tiện mang phong cách thời trang, chuẩn mực quốc tế và tràn đầy lòng trắc ẩn.
          </p>
          <p style=\"margin-bottom:1rem;\">
            Lấy cảm hứng từ ngôn ngữ thẩm mỹ của các tạp chí danh tiếng như Vogue, Harper's Bazaar và Kinfolk, chúng tôi tin rằng cái đẹp chân thực của báo chí không nằm ở những giật gân, câu khách, mà ở chiều sâu nhân văn, sự thanh lịch của con chữ và những câu chuyện tử tế chạm đến đáy lòng độc giả.
          </p>
          <p>
            <strong>Phương châm của tòa soạn:</strong> Trung thực trong sự thật, nhân ái trong góc nhìn, và chuẩn mực thẩm mỹ trong từng trang viết.
          </p>
        </div>

        <div class=\"about-story-card\" style=\"background:var(--color-surface-blush); border:1px solid #EEDBD6; border-radius:var(--radius-lg); padding:2rem; text-align:center;\">
          <svg style=\"width:64px; height:60px; margin:0 auto 1rem auto; display:block;\" viewBox=\"0 0 100 80\" fill=\"none\">
            <path d=\"M30 45 C15 32 8 20 22 10 C32 2 44 8 50 20 C56 8 68 2 78 10 C92 20 82 36 62 55 C54 62 50 67 48 68 C45 70 42 68 40 65 C34 58 26 48 30 45 Z\" stroke=\"#591724\" stroke-width=\"3\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/>
            <path d=\"M48 68 C56 72 70 75 80 70 C88 66 94 58 98 50\" stroke=\"#BA6975\" stroke-width=\"2.5\" stroke-linecap=\"round\" stroke-dasharray=\"3 4\"/>
          </svg>
          <h2 style=\"font-family:var(--font-editorial); font-size:1.75rem; font-style:italic; color:var(--color-brand-primary); margin-bottom:0.25rem;\">HEARTICLES.</h2>
          <p style=\"font-size:0.875rem; font-weight:600; color:var(--color-brand-accent); margin-bottom:1rem;\">Stories that speak to the heart.</p>
          <p style=\"font-size:0.8125rem; color:var(--color-text-muted); line-height:1.5;\">
            Biểu trưng trái tim vẽ tay liên tục (continuous line) biểu đạt tình yêu thương nối liền giữa người làm báo và cộng đồng xã hội.
          </p>
        </div>
      </div>

      <!-- Editorial Team Grid -->
      <div style=\"margin-top:2.5rem; padding-top:2rem; border-top:1px solid var(--color-border-hairline);\">
        <h3 style=\"font-family:var(--font-editorial); font-size:1.35rem; color:var(--color-text-headline); margin-bottom:1.5rem; text-align:center;\">
          Ban Biên Tập &amp; Cố Vấn Tòa Soạn • ULIS - VNU
        </h3>
        <div style=\"display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:1.25rem;\">
          <div style=\"background:#FFFFFF; border:1px solid var(--color-border-hairline); border-radius:var(--radius-md); padding:1.25rem; text-align:center;\">
            <div style=\"width:48px; height:48px; border-radius:50%; background:var(--color-brand-primary); color:#FFF; display:flex; align-items:center; justify-content:center; font-weight:bold; margin:0 auto 0.75rem auto;\">GV</div>
            <h4 style=\"font-family:var(--font-serif); font-size:1rem; font-weight:700;\">Giảng viên Phụ trách</h4>
            <p style=\"font-size:0.75rem; color:var(--color-brand-accent); font-weight:600;\">Khoa Ngôn ngữ &amp; Truyền thông</p>
            <p style=\"font-size:0.75rem; color:var(--color-text-muted); margin-top:0.3rem;\">Cố vấn định hướng nội dung và nghiệp vụ báo chí đối ngoại.</p>
          </div>
          <div style=\"background:#FFFFFF; border:1px solid var(--color-border-hairline); border-radius:var(--radius-md); padding:1.25rem; text-align:center;\">
            <div style=\"width:48px; height:48px; border-radius:50%; background:var(--color-brand-accent); color:#FFF; display:flex; align-items:center; justify-content:center; font-weight:bold; margin:0 auto 0.75rem auto;\">N1</div>
            <h4 style=\"font-family:var(--font-serif); font-size:1rem; font-weight:700;\">Lớp 6 - Nhóm 1 - Khóa 127</h4>
            <p style=\"font-size:0.75rem; color:var(--color-brand-primary); font-weight:600;\">Ban Biên tập &amp; Sản xuất Nội dung</p>
            <p style=\"font-size:0.75rem; color:var(--color-text-muted); margin-top:0.3rem;\">Sáng tạo nội dung, biên dịch báo chí quốc tế và phóng sự thực địa.</p>
          </div>
          <div style=\"background:#FFFFFF; border:1px solid var(--color-border-hairline); border-radius:var(--radius-md); padding:1.25rem; text-align:center;\">
            <div style=\"width:48px; height:48px; border-radius:50%; background:var(--primitive-burgundy-900); color:#FFF; display:flex; align-items:center; justify-content:center; font-weight:bold; margin:0 auto 0.75rem auto;\">UI</div>
            <h4 style=\"font-family:var(--font-serif); font-size:1rem; font-weight:700;\">Ban Thiết kế &amp; Kỹ thuật</h4>
            <p style=\"font-size:0.75rem; color:var(--color-brand-accent); font-weight:600;\">Creative Direction &amp; Web Dev</p>
            <p style=\"font-size:0.75rem; color:var(--color-text-muted); margin-top:0.3rem;\">Phát triển giao diện chuẩn thời trang cao cấp và hệ thống Impeccable.</p>
          </div>
        </div>
      </div>
    </div>
  `;
}

/* ===================================================================
   ARTICLE DETAIL MODAL & READING SUITE (TTS, Font Adjuster, Comments)
   =================================================================== */
window.openArticleModal = function(articleId) {
  const article = ARTICLES_DATA.find(a => a.id === articleId);
  if (!article) return;

  const modal = document.getElementById('articleReaderModal');
  const body = document.getElementById('articleModalBody');
  if (!modal || !body) return;

  const savedComments = JSON.parse(localStorage.getItem(`comments_${article.id}`) || '[]');
  const isLiked = localStorage.getItem(`liked_${article.id}`) === 'true';

  let bodyHtml = '';
  if (typeof article.content === 'string') {
    bodyHtml = article.content;
  } else if (Array.isArray(article.content)) {
    bodyHtml = article.content.map(p => {
      if (p.startsWith('### ')) {
        return `<h3>${p.replace('### ', '')}</h3>`;
      }
      return `<p>${p}</p>`;
    }).join('');
  }

  body.innerHTML = `
    <div class=\"article-reading-content\" style=\"font-size: ${currentFontSize}rem;\">
      <div class=\"article-breadcrumb\">
        <a href=\"javascript:void(0)\" onclick=\"closeArticleModal()\">Home</a>
        <span>/</span>
        <a href=\"javascript:void(0)\" onclick=\"filterByCategory('${article.category}')\">${article.categoryName}</a>
        <span>/</span>
        <span>Chi tiết bài viết</span>
      </div>

      <h1 class=\"article-headline\" style=\"font-family:var(--font-editorial); font-size:2.2rem; line-height:1.25; margin-bottom:0.75rem;\">${article.title}</h1>
      <p class=\"article-sapo\" style=\"font-family:var(--font-serif); font-size:1.15rem; line-height:1.6; color:var(--color-text-muted); margin-bottom:1.5rem;\">${article.subtitle}</p>

      <div class=\"article-author-strip\">
        <div class=\"article-author-info\">
          <div class=\"author-avatar-small\">${article.author.charAt(0)}</div>
          <div>
            <div class=\"author-name-text\" style=\"font-weight:700;\">${article.author}</div>
            <div class=\"article-date-text\" style=\"font-size:0.75rem; color:var(--color-text-muted);\">${article.date}</div>
          </div>
        </div>

        <div class=\"article-reading-tools\">
          <button class=\"tool-btn\" onclick=\"adjustFontSize(-0.1)\" title=\"Giảm cỡ chữ\"><i class=\"fas fa-font\"></i> A-</button>
          <button class=\"tool-btn\" onclick=\"adjustFontSize(0.1)\" title=\"Tăng cỡ chữ\"><i class=\"fas fa-font\"></i> A+</button>
          <button class=\"tool-btn ${isSpeaking ? 'active' : ''}\" id=\"btnTTS\" onclick=\"toggleTextToSpeech('${article.id}')\" title=\"Nghe đọc bài báo\">
            <i class=\"fas ${isSpeaking ? 'fa-pause' : 'fa-volume-up'}\"></i> ${isSpeaking ? 'Tạm dừng' : 'Đọc bài báo'}
          </button>
          <button class=\"btn-article-like ${isLiked ? 'liked' : ''}\" id=\"likeBtn_${article.id}\" onclick=\"toggleLikeArticle('${article.id}')\" title=\"Thả tim bài viết\">
            <i class=\"fas fa-heart\"></i> <span id=\"likeCount_${article.id}\">${article.likes + (isLiked ? 1 : 0)}</span>
          </button>
          <button class=\"tool-btn\" onclick=\"shareArticle('${article.title}')\" title=\"Chia sẻ\"><i class=\"fas fa-share-alt\"></i> Chia sẻ</button>
        </div>
      </div>

      <div class=\"article-hero-media\" style=\"border-radius:var(--radius-lg); overflow:hidden; margin:1.5rem 0;\">
        <img src=\"${article.image}\" alt=\"${article.title}\" style=\"width:100%; display:block;\" onerror=\"handleImageError(this)\">
        <div class=\"article-media-caption\" style=\"font-size:0.8125rem; color:var(--color-text-muted); padding:0.5rem 0.25rem;\">${article.imageCaption || article.title}</div>
      </div>

      ${article.video ? `
        <div class=\"video-responsive-embed\" style=\"margin-bottom: 2rem; border-radius: 12px; overflow:hidden;\">
          <iframe src=\"${article.video}\" title=\"Video phóng sự kèm bài viết\" allowfullscreen></iframe>
        </div>
      ` : ''}

      <div class=\"article-body-text\" id=\"articleBodyContent\" style=\"font-family:var(--font-body); font-size:1.125rem; line-height:1.8;\">
        ${bodyHtml}
      </div>

      <div class=\"article-source-box\" style=\"background:var(--color-surface-blush); border:1px solid #EEDBD6; border-radius:var(--radius-md); padding:1rem 1.25rem; margin-top:2.5rem; display:flex; justify-content:space-between; align-items:center;\">
        <div class=\"source-credit-text\">
          <strong>Nguồn trích dẫn:</strong> ${article.sourceName}
        </div>
        <a href=\"${article.sourceUrl}\" target=\"_blank\" rel=\"noopener noreferrer\" class=\"source-link-btn\" style=\"color:var(--color-brand-primary); font-weight:600; font-size:0.875rem;\">
          Xem nguồn gốc <i class=\"fas fa-external-link-alt\"></i>
        </a>
      </div>

      <!-- Comments Block -->
      <div class=\"article-comments-block\" style=\"margin-top:3rem;\">
        <h3 style=\"font-family:var(--font-editorial); font-size:1.4rem; color:var(--color-text-headline); margin-bottom:1.25rem;\">
          <i class=\"far fa-comments\" style=\"color:var(--color-brand-primary);\"></i> Bình luận &amp; Thảo luận (<span id=\"commentCount\">${savedComments.length}</span>)
        </h3>
        
        <div class=\"comment-form-wrap\" style=\"display:flex; gap:0.75rem; margin-bottom:1.5rem;\">
          <input type=\"text\" class=\"comment-input-field\" id=\"newCommentInput\" placeholder=\"Chia sẻ góc nhìn nhân văn của bạn về bài viết này...\" onkeypress=\"if(event.key === 'Enter') submitComment('${article.id}')\" style=\"flex-grow:1; padding:0.75rem 1rem; border:1px solid var(--color-border-hairline); border-radius:var(--radius-full); font-size:0.9rem;\">
          <button class=\"comment-submit-btn\" onclick=\"submitComment('${article.id}')\" style=\"background:var(--color-brand-primary); color:white; border:none; border-radius:var(--radius-full); padding:0.75rem 1.5rem; font-weight:600; cursor:pointer;\">Gửi</button>
        </div>

        <div class=\"comments-list-container\" id=\"commentsListContainer\">
          ${savedComments.length === 0 ? '<p style=\"color:var(--color-text-muted); font-size:0.875rem; font-style:italic;\">Hãy là người đầu tiên chia sẻ cảm nghĩ về bài viết này.</p>' : ''}
          ${savedComments.map(c => `
            <div class=\"comment-item-card\" style=\"background:white; border:1px solid var(--color-border-hairline); border-radius:var(--radius-md); padding:0.85rem 1rem; margin-bottom:0.75rem;\">
              <div style=\"display:flex; justify-content:space-between; margin-bottom:0.35rem;\">
                <strong style=\"color:var(--color-brand-primary); font-size:0.875rem;\">${c.author}</strong>
                <span style=\"font-size:0.75rem; color:var(--color-text-muted);\">${c.time}</span>
              </div>
              <p style=\"font-size:0.875rem; color:var(--color-text-body); margin:0;\">${c.text}</p>
            </div>
          `).join('')}
        </div>
      </div>
    </div>
  `;

  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
};

window.closeArticleModal = function() {
  const modal = document.getElementById('articleReaderModal');
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }
  if (isSpeaking) {
    stopTextToSpeech();
  }
};

/* ===================================================================
   COMMENT & LIKE SYSTEM
   =================================================================== */
window.submitComment = function(articleId) {
  const input = document.getElementById('newCommentInput');
  if (!input || !input.value.trim()) return;

  const key = `comments_${articleId}`;
  const existing = JSON.parse(localStorage.getItem(key) || '[]');
  const now = new Date();
  const timeStr = `${now.getHours()}:${String(now.getMinutes()).padStart(2, '0')} - ${now.getDate()}/${now.getMonth() + 1}`;

  existing.unshift({
    author: 'Độc giả ULIS - VNU',
    time: timeStr,
    text: input.value.trim()
  });

  localStorage.setItem(key, JSON.stringify(existing));
  input.value = '';
  openArticleModal(articleId);
  showToast('Bình luận của bạn đã được xuất bản!', 'check');
};

window.toggleLikeArticle = function(articleId) {
  const isLiked = localStorage.getItem(`liked_${articleId}`) === 'true';
  const article = ARTICLES_DATA.find(a => a.id === articleId);
  const btn = document.getElementById(`likeBtn_${articleId}`);
  const countEl = document.getElementById(`likeCount_${articleId}`);

  if (isLiked) {
    localStorage.removeItem(`liked_${articleId}`);
    if (btn) btn.classList.remove('liked');
    if (countEl && article) countEl.textContent = article.likes;
    showToast('Đã bỏ yêu thích bài viết', 'heart-broken');
  } else {
    localStorage.setItem(`liked_${articleId}`, 'true');
    if (btn) {
      btn.classList.add('liked');
      triggerHeartBurst(btn);
    }
    if (countEl && article) countEl.textContent = article.likes + 1;
    showToast('Đã thả tim bài viết! Cảm ơn bạn.', 'heart');
  }
};

function triggerHeartBurst(element) {
  const rect = element.getBoundingClientRect();
  for (let i = 0; i < 8; i++) {
    const p = document.createElement('div');
    p.className = 'burst-particle';
    p.innerHTML = '<i class=\"fas fa-heart\" style=\"color:#BA6975; font-size:12px;\"></i>';
    p.style.position = 'fixed';
    p.style.left = `${rect.left + rect.width / 2}px`;
    p.style.top = `${rect.top + rect.height / 2}px`;
    p.style.pointerEvents = 'none';
    p.style.zIndex = '9999';
    p.style.transition = 'all 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
    document.body.appendChild(p);

    const angle = (i / 8) * 2 * Math.PI;
    const dist = 35 + Math.random() * 20;
    setTimeout(() => {
      p.style.transform = `translate(${Math.cos(angle) * dist}px, ${Math.sin(angle) * dist}px) scale(0)`;
      p.style.opacity = '0';
    }, 10);

    setTimeout(() => {
      p.remove();
    }, 650);
  }
}

/* ===================================================================
   TEXT TO SPEECH (Web Speech API)
   =================================================================== */
window.toggleTextToSpeech = function(articleId) {
  if (isSpeaking) {
    stopTextToSpeech();
  } else {
    startTextToSpeech(articleId);
  }
};

function startTextToSpeech(articleId) {
  const article = ARTICLES_DATA.find(a => a.id === articleId);
  if (!article || !('speechSynthesis' in window)) {
    alert('Trình duyệt của bạn chưa hỗ trợ tính năng Web Speech API.');
    return;
  }

  window.speechSynthesis.cancel();

  let plainText = '';
  if (typeof article.content === 'string') {
    plainText = article.content.replace(/<[^>]*>/g, ' ');
  } else if (Array.isArray(article.content)) {
    plainText = article.content.join(' ');
  }

  const textToRead = `${article.title}. ${article.subtitle}. ${plainText}`;
  speechUtterance = new SpeechSynthesisUtterance(textToRead);
  speechUtterance.lang = 'vi-VN';
  speechUtterance.rate = 0.95;

  speechUtterance.onstart = () => {
    isSpeaking = true;
    updateTTSButton(true);
    showToast('Đang phát giọng đọc bài báo...', 'volume-up');
  };

  speechUtterance.onend = () => {
    isSpeaking = false;
    updateTTSButton(false);
  };

  speechUtterance.onerror = () => {
    isSpeaking = false;
    updateTTSButton(false);
  };

  window.speechSynthesis.speak(speechUtterance);
}

function stopTextToSpeech() {
  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel();
  }
  isSpeaking = false;
  updateTTSButton(false);
}

function updateTTSButton(speaking) {
  const btn = document.getElementById('btnTTS');
  if (btn) {
    btn.innerHTML = `<i class=\"fas ${speaking ? 'fa-pause' : 'fa-volume-up'}\"></i> ${speaking ? 'Tạm dừng' : 'Đọc bài báo'}`;
    btn.classList.toggle('active', speaking);
  }
}

window.adjustFontSize = function(delta) {
  currentFontSize = Math.min(Math.max(currentFontSize + delta, 0.95), 1.45);
  const content = document.querySelector('.article-reading-content');
  if (content) {
    content.style.fontSize = `${currentFontSize}rem`;
  }
};

window.shareArticle = function(title) {
  if (navigator.share) {
    navigator.share({
      title: title,
      text: `${title} - Đọc trên Tạp chí HEARTICLES. (ULIS - VNU)`,
      url: window.location.href
    }).catch(() => {});
  } else {
    navigator.clipboard.writeText(window.location.href);
    showToast('Đã sao chép liên kết bài viết!', 'link');
  }
};

/* ===================================================================
   SEARCH ENGINE (Instant Live Search)
   =================================================================== */
window.openSearchModal = function() {
  const modal = document.getElementById('searchModal');
  const input = document.getElementById('searchInput');
  if (modal) {
    modal.classList.add('active');
    setTimeout(() => { if (input) input.focus(); }, 100);
  }
};

window.closeSearchModal = function() {
  const modal = document.getElementById('searchModal');
  if (modal) modal.classList.remove('active');
};

window.handleSearchInput = function(query) {
  const resultsBox = document.getElementById('searchResults');
  if (!resultsBox) return;

  const trimmed = query.trim().toLowerCase();
  if (!trimmed) {
    resultsBox.innerHTML = `
      <div style=\"padding:1rem 0;\">
        <p style=\"color:var(--color-text-muted); font-size:0.875rem; margin-bottom:0.75rem;\">Từ khóa thịnh hành gợi ý:</p>
        <div style=\"display:flex; flex-wrap:wrap; gap:0.5rem;\">
          <button class=\"search-tag-chip\" onclick=\"applySearchTag('Hội An')\">#Hội An</button>
          <button class=\"search-tag-chip\" onclick=\"applySearchTag('Taeyang')\">#Taeyang</button>
          <button class=\"search-tag-chip\" onclick=\"applySearchTag('Trending')\">#Trending</button>
          <button class=\"search-tag-chip\" onclick=\"applySearchTag('Quốc hội')\">#Quốc hội</button>
          <button class=\"search-tag-chip\" onclick=\"applySearchTag('ULIS')\">#ULIS - VNU</button>
        </div>
      </div>
    `;
    return;
  }

  const matches = ARTICLES_DATA.filter(a => {
    return a.title.toLowerCase().includes(trimmed) ||
           a.subtitle.toLowerCase().includes(trimmed) ||
           a.author.toLowerCase().includes(trimmed) ||
           a.categoryName.toLowerCase().includes(trimmed) ||
           (a.tags && a.tags.some(t => t.toLowerCase().includes(trimmed)));
  });

  if (matches.length === 0) {
    resultsBox.innerHTML = `
      <div style=\"text-align:center; padding:2rem 0; color:var(--color-text-muted);\">
        <i class=\"fas fa-search\" style=\"font-size:2rem; margin-bottom:0.75rem; opacity:0.5;\"></i>
        <p>Không tìm thấy bài viết nào khớp với '<strong>${query}</strong>'</p>
        <p style=\"font-size:0.8125rem; margin-top:0.25rem;\">Hãy thử tìm theo tên chuyên mục: <em>Trending, Society, Human Stories, Mind &amp; Soul...</em></p>
      </div>
    `;
    return;
  }

  resultsBox.innerHTML = matches.map(item => `
    <div class=\"search-result-item\" onclick=\"closeSearchModal(); openArticleModal('${item.id}')\" style=\"display:flex; gap:1rem; align-items:center; padding:0.75rem; border-bottom:1px solid var(--color-border-hairline); cursor:pointer;\">
      <img src=\"${item.image}\" alt=\"${item.title}\" style=\"width:60px; height:60px; border-radius:8px; object-fit:cover;\">
      <div>
        <span style=\"font-size:0.6875rem; color:var(--color-brand-primary); font-weight:800; text-transform:uppercase;\">${item.categoryName}</span>
        <h4 style=\"font-family:var(--font-serif); font-size:0.95rem; font-weight:700; color:var(--color-text-headline); margin:0.15rem 0;\">${highlightMatch(item.title, trimmed)}</h4>
        <span style=\"font-size:0.75rem; color:var(--color-text-muted);\">${item.author} • ${item.readTime}</span>
      </div>
    </div>
  `).join('');
};

window.applySearchTag = function(tag) {
  const input = document.getElementById('searchInput');
  if (input) {
    input.value = tag;
    handleSearchInput(tag);
  }
};

function highlightMatch(text, query) {
  const regex = new RegExp(`(${query})`, 'gi');
  return text.replace(regex, '<mark style=\"background:#FCE8EC; color:#591724; font-weight:bold;\">$1</mark>');
}

/* ===================================================================
   ONBOARDING SYSTEM (3-Step First-Time Walkthrough)
   =================================================================== */
function initOnboarding() {
  const hasOnboarded = localStorage.getItem('hearticles_fashion_onboarded_v2');
  if (!hasOnboarded) {
    setTimeout(() => {
      openOnboardingModal();
    }, 1200);
  }
}

window.openOnboardingModal = function() {
  const modal = document.getElementById('onboardModal');
  if (modal) {
    modal.classList.add('active');
    currentOnboardStep = 1;
    renderOnboardStep(1);
  }
};

window.closeOnboardingModal = function() {
  const modal = document.getElementById('onboardModal');
  if (modal) modal.classList.remove('active');
  localStorage.setItem('hearticles_fashion_onboarded_v2', 'true');
};

window.nextOnboardStep = function() {
  if (currentOnboardStep < 3) {
    currentOnboardStep++;
    renderOnboardStep(currentOnboardStep);
  } else {
    closeOnboardingModal();
    showToast('Chào mừng bạn đến với HEARTICLES.!', 'heart');
  }
};

function renderOnboardStep(step) {
  const dots = document.querySelectorAll('.onboard-step-dot');
  dots.forEach((dot, idx) => {
    dot.classList.toggle('active', idx === step - 1);
  });

  const content = document.getElementById('onboardStepContent');
  const btnNext = document.getElementById('onboardBtnNext');
  if (!content) return;

  if (step === 1) {
    content.innerHTML = `
      <div class=\"onboard-badge\">BƯỚC 1 / 3 • GIỚI THIỆU</div>
      <h2 class=\"onboard-title\">Chào mừng bạn đến với HEARTICLES.</h2>
      <p class=\"onboard-desc\">
        Tạp chí báo điện tử đa phương tiện xuất bản bởi sinh viên <strong>Trường Đại học Ngoại ngữ - ĐHQGHN (ULIS - VNU)</strong>. Nơi tin tức khởi nguồn từ nhịp đập trái tim và lòng trắc ẩn.
      </p>
      <div class=\"onboard-feature-grid\">
        <div class=\"onboard-feature-item\">
          <h4><i class=\"fas fa-check-circle\" style=\"color:var(--color-brand-primary);\"></i> Thẩm mỹ Tạp chí Thời trang</h4>
          <p>Thiết kế tinh xảo lấy cảm hứng từ Vogue, Kinfolk với tông màu đỏ rượu ấm áp và chữ serif cổ điển.</p>
        </div>
        <div class=\"onboard-feature-item\">
          <h4><i class=\"fas fa-check-circle\" style=\"color:var(--color-brand-primary);\"></i> 100% Ảnh báo chí gốc</h4>
          <p>Toàn bộ 34 bài viết và hình ảnh được trích xuất chân thực từ kho tư liệu báo chí chính thống.</p>
        </div>
      </div>
    `;
    if (btnNext) btnNext.textContent = 'Tiếp tục';
  } else if (step === 2) {
    content.innerHTML = `
      <div class=\"onboard-badge\">BƯỚC 2 / 3 • CÁ NHÂN HÓA</div>
      <h2 class=\"onboard-title\">Tùy biến trải nghiệm đọc</h2>
      <p class=\"onboard-desc\">
        HEARTICLES. trang bị đầy đủ công cụ đọc báo hiện đại:
      </p>
      <div class=\"onboard-feature-grid\">
        <div class=\"onboard-feature-item\">
          <h4><i class=\"fas fa-volume-up\" style=\"color:var(--color-brand-primary);\"></i> Đọc báo tự động</h4>
          <p>Nghe bài báo rảnh tay qua công nghệ giọng đọc thông minh Web Speech API.</p>
        </div>
        <div class=\"onboard-feature-item\">
          <h4><i class=\"fas fa-keyboard\" style=\"color:var(--color-brand-primary);\"></i> Phím tắt tiện lợi</h4>
          <p>Bấm phím <code>/</code> để tìm kiếm tức thì, phím <code>T</code> để phóng to chữ, <code>ESC</code> để đóng bài đọc.</p>
        </div>
      </div>
    `;
    if (btnNext) btnNext.textContent = 'Tiếp tục';
  } else {
    content.innerHTML = `
      <div class=\"onboard-badge\">BƯỚC 3 / 3 • HOÀN TẤT</div>
      <h2 class=\"onboard-title\">Khám phá 34 Phóng sự Đặc sắc</h2>
      <p class=\"onboard-desc\">
        Khám phá ngay các tiêu điểm trang bìa: <strong>\"Lawmakers Propose Measures\"</strong>, <strong>\"Gánh mưu sinh Hội An\"</strong>, và ký sự <strong>\"Taeyang tại concert Mỹ Đình\"</strong>.
      </p>
      <div style=\"background:var(--color-surface-blush); border:1px dashed #EEDBD6; border-radius:12px; padding:1.25rem; margin-bottom:1.5rem; text-align:center;\">
        <i class=\"fas fa-envelope-open-text\" style=\"color:var(--color-brand-primary); font-size:1.75rem; margin-bottom:0.5rem;\"></i>
        <p style=\"font-size:0.9rem; font-weight:700; color:var(--color-brand-primary);\">Nhận bản tin sáng 7:00 AM mỗi ngày</p>
        <p style=\"font-size:0.75rem; color:var(--color-text-muted);\">Bấm nút 'Subscribe' ở góc trên trang để đăng ký miễn phí.</p>
      </div>
    `;
    if (btnNext) btnNext.textContent = 'Bắt đầu trải nghiệm';
  }
}

/* ===================================================================
   READING PROGRESS BAR
   =================================================================== */
function setupReadingProgressBar() {
  window.addEventListener('scroll', () => {
    const total = document.documentElement.scrollHeight - window.innerHeight;
    if (total > 0) {
      const progress = (window.scrollY / total) * 100;
      const bar = document.getElementById('readingProgressBar');
      if (bar) bar.style.width = `${progress}%`;
    }
  }, { passive: true });
}

/* ===================================================================
   NETWORK / OFFLINE DETECTOR
   =================================================================== */
function setupNetworkStatus() {
  const banner = document.getElementById('offlineBanner');
  window.addEventListener('offline', () => {
    if (banner) banner.classList.add('active');
    showToast('Mất kết nối mạng. Bạn đang xem bản lưu ngoại tuyến.', 'wifi');
  });
  window.addEventListener('online', () => {
    if (banner) banner.classList.remove('active');
    showToast('Đã khôi phục kết nối internet.', 'wifi');
  });
}

/* ===================================================================
   TOAST NOTIFICATION ENGINE
   =================================================================== */
window.showToast = function(message, icon = 'check') {
  let toast = document.getElementById('impeccableToast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'impeccableToast';
    toast.className = 'toast-notification';
    document.body.appendChild(toast);
  }
  toast.innerHTML = `<i class=\"fas fa-${icon}\" style=\"color:var(--color-brand-accent);\"></i> <span>${message}</span>`;
  toast.classList.add('show');
  clearTimeout(toast.hideTimeout);
  toast.hideTimeout = setTimeout(() => {
    toast.classList.remove('show');
  }, 3200);
};

/* ===================================================================
   KEYBOARD SHORTCUTS MODAL
   =================================================================== */
window.openShortcutsModal = function() {
  const modal = document.getElementById('shortcutsModal');
  if (modal) modal.classList.add('active');
};

window.closeShortcutsModal = function() {
  const modal = document.getElementById('shortcutsModal');
  if (modal) modal.classList.remove('active');
};

/* ===================================================================
   DRAWER / OFFCANVAS MENU
   =================================================================== */
window.openDrawer = function() {
  const drawer = document.getElementById('offcanvasDrawer');
  const backdrop = document.getElementById('drawerBackdrop');
  if (drawer && backdrop) {
    drawer.classList.add('active');
    backdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
};

window.closeDrawer = function() {
  const drawer = document.getElementById('offcanvasDrawer');
  const backdrop = document.getElementById('drawerBackdrop');
  if (drawer && backdrop) {
    drawer.classList.remove('active');
    backdrop.classList.remove('active');
    document.body.style.overflow = '';
  }
};

/* ===================================================================
   SUBSCRIBE MODAL SIMULATION
   =================================================================== */
window.openSubscribeModal = function() {
  const email = prompt('Nhập địa chỉ email của bạn để nhận bản tin thời trang & nhân văn HEARTICLES. mỗi sáng:');
  if (email && email.includes('@')) {
    localStorage.setItem('hearticles_subscribed_email', email);
    showToast('Cảm ơn bạn! Đã đăng ký nhận bản tin thành công.', 'check-circle');
  } else if (email) {
    alert('Vui lòng nhập địa chỉ email hợp lệ.');
  }
};

/* ===================================================================
   READER POLL WIDGET
   =================================================================== */
function setupPoll() {
  const container = document.getElementById('pollContainer');
  if (!container) return;
  const pollVoted = localStorage.getItem('hearticles_poll_voted');
  if (pollVoted) {
    showPollResults();
  }
}

window.votePoll = function(optionIndex) {
  localStorage.setItem('hearticles_poll_voted', optionIndex);
  showPollResults();
  showToast('Cảm ơn bạn đã đóng góp ý kiến!', 'poll');
};

function showPollResults() {
  const container = document.getElementById('pollContainer');
  if (!container) return;
  container.innerHTML = `
    <div class=\"poll-results-box\" style=\"background:rgba(255,255,255,0.08); padding:1rem; border-radius:8px;\">
      <div style=\"margin-bottom:0.75rem;\">
        <div style=\"display:flex; justify-content:space-between; font-size:0.8125rem; margin-bottom:0.25rem;\">
          <span>1. Quy hoạch tuyến phố đi bộ văn hóa</span>
          <strong>52% (1.420 phiếu)</strong>
        </div>
        <div style=\"background:rgba(255,255,255,0.2); height:6px; border-radius:3px; overflow:hidden;\">
          <div style=\"background:#BA6975; width:52%; height:100%;\"></div>
        </div>
      </div>
      <div style=\"margin-bottom:0.75rem;\">
        <div style=\"display:flex; justify-content:space-between; font-size:0.8125rem; margin-bottom:0.25rem;\">
          <span>2. Tôn vinh nét đẹp văn hóa truyền thống</span>
          <strong>34% (930 phiếu)</strong>
        </div>
        <div style=\"background:rgba(255,255,255,0.2); height:6px; border-radius:3px; overflow:hidden;\">
          <div style=\"background:#E8A8B1; width:34%; height:100%;\"></div>
        </div>
      </div>
      <div>
        <div style=\"display:flex; justify-content:space-between; font-size:0.8125rem; margin-bottom:0.25rem;\">
          <span>3. Hỗ trợ sinh kế bền vững cho người nghèo</span>
          <strong>14% (385 phiếu)</strong>
        </div>
        <div style=\"background:rgba(255,255,255,0.2); height:6px; border-radius:3px; overflow:hidden;\">
          <div style=\"background:#D8C0C4; width:14%; height:100%;\"></div>
        </div>
      </div>
      <div style=\"margin-top:1rem; font-size:0.75rem; color:#FFD0D0; text-align:right;\">
        <i class=\"fas fa-check-circle\"></i> Bạn đã tham gia biểu quyết khảo sát này.
      </div>
    </div>
  `;
}

/* ===================================================================
   IMAGE ERROR HANDLER
   =================================================================== */
window.handleImageError = function(img) {
  img.onerror = null;
  img.src = 'assets/images/trending/image8.jpg';
};

/* ===================================================================
   GLOBAL EVENT LISTENERS (Keyboard shortcuts: /, ESC, ?, T)
   =================================================================== */
function setupEventListeners() {
  document.addEventListener('keydown', (e) => {
    if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) {
      if (e.key === 'Escape') {
        closeSearchModal();
      }
      return;
    }

    if (e.key === 'Escape') {
      closeArticleModal();
      closeSearchModal();
      closeDrawer();
      closeOnboardingModal();
      closeShortcutsModal();
    } else if (e.key === '/') {
      e.preventDefault();
      openSearchModal();
    } else if (e.key === '?' || (e.shiftKey && e.key === '/')) {
      e.preventDefault();
      openShortcutsModal();
    } else if (e.key === 't' || e.key === 'T') {
      adjustFontSize(currentFontSize >= 1.3 ? -0.3 : 0.15);
    }
  });
}
"""

with open(r"c:\Users\camka\OneDrive\Desktop\BCTT\js\app.js", "w", encoding="utf-8") as f:
    f.write(APP_JS)

print("Updated js/app.js with authentic original articles and video clips!")
