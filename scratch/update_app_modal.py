import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Define formatArticleSource right before function openArticleModal
helper_fn = """function formatArticleSource(article, isEn) {
  if (!article) return '';

  const rawTitle = isEn 
    ? (article.title_en || article.title || '') 
    : (article.title || article.title_en || '');
  const cleanTitle = rawTitle.replace(/^["'“”‘’]|["'“”‘’]$/g, '').trim();

  // Clean author name
  let author = (article.author || '').split('•')[0].trim();
  if (author.endsWith(' & NDO')) author = author.replace(' & NDO', '');
  if (!author) author = isEn ? 'Editorial Staff' : 'Ban biên tập';

  const sourceName = article.sourceName || (isEn ? 'HEARTICLES. Editorial' : 'Tòa soạn HEARTICLES.');

  // Date formatting
  let rawDate = (article.date || '').split(' - ')[0].trim();
  rawDate = rawDate.replace(/^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),\\s*/i, '');

  const monthsMap = {
    'January': 'tháng 1', 'February': 'tháng 2', 'March': 'tháng 3',
    'April': 'tháng 4', 'May': 'tháng 5', 'June': 'tháng 6',
    'July': 'tháng 7', 'August': 'tháng 8', 'September': 'tháng 9',
    'October': 'tháng 10', 'November': 'tháng 11', 'December': 'tháng 12'
  };

  let formattedDate = rawDate;
  if (!isEn) {
    const match = rawDate.match(/([A-Za-z]+)\\s+(\\d{1,2}),?\\s+(\\d{4})/);
    if (match) {
      const monthVi = monthsMap[match[1]] || match[1];
      formattedDate = `ngày ${match[2]} ${monthVi} năm ${match[3]}`;
    }
  }

  const url = article.sourceUrl || '#';

  if (isEn) {
    return `
      <div class="article-source-citation">
        <span class="citation-label">Source:</span> "<em class="citation-title">${cleanTitle}</em>", ${sourceName}, by ${author}, ${formattedDate}, 
        <a href="${url}" target="_blank" rel="noopener noreferrer" class="citation-url">${url}</a>
      </div>
    `;
  } else {
    return `
      <div class="article-source-citation">
        <span class="citation-label">Source:</span> "<em class="citation-title">${cleanTitle}</em>", ${sourceName}, viết bởi ${author}, ${formattedDate}, 
        <a href="${url}" target="_blank" rel="noopener noreferrer" class="citation-url">${url}</a>
      </div>
    `;
  }
}
window.formatArticleSource = formatArticleSource;

"""

target_modal_header = """/* ===================================================================
   ARTICLE DETAIL MODAL & READING SUITE (Bilingual, TTS, Zoom, Like)
   =================================================================== */
function openArticleModal(articleId) {"""

assert target_modal_header in text, "Target modal header not found!"
text = text.replace(target_modal_header, f"""/* ===================================================================
   ARTICLE DETAIL MODAL & READING SUITE (Bilingual, TTS, Zoom, Like)
   =================================================================== */
{helper_fn}function openArticleModal(articleId) {{""")

# 2. Update modal body HTML to include formatArticleSource and remove old article-source-box
target_body_block = """      <div class="article-body-text" id="articleBodyContent" style="font-family:var(--font-body); font-size:1.125rem; line-height:1.8; color:var(--color-text-body);">
        ${bodyHtml}
      </div>

      <div class="article-source-box" style="background:var(--color-surface-blush, #FBF3F4); border:1px solid rgba(84,17,30,0.12); border-radius:var(--radius-md); padding:1rem 1.25rem; margin-top:2.5rem; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem;">
        <div class="source-credit-text" style="font-size:0.875rem;">
          <strong>${isEn ? 'Source Attribution:' : 'Nguồn trích dẫn:'}</strong> ${article.sourceName}
        </div>
        <a href="${article.sourceUrl}" target="_blank" rel="noopener noreferrer" class="source-link-btn" style="color:var(--color-brand-primary); font-weight:700; font-size:0.875rem; text-decoration:none;">
          ${isEn ? 'Original Article' : 'Xem nguồn gốc'} <i class="fas fa-external-link-alt"></i>
        </a>
      </div>"""

replacement_body_block = """      <div class="article-body-text" id="articleBodyContent" style="font-family:var(--font-body); font-size:1.125rem; line-height:1.8; color:var(--color-text-body);">
        ${bodyHtml}
        ${formatArticleSource(article, isEn)}
      </div>"""

assert target_body_block in text, "Target body block not found!"
text = text.replace(target_body_block, replacement_body_block)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated js/app.js with formatArticleSource in modal!")
