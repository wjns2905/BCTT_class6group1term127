import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    c = f.read()

target = """  if (isEn) {
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
  }"""

replacement = """  if (isEn) {
    return `
      <div class="article-source-citation">
        <span class="citation-label">Original Source:</span> "<em class="citation-title">${cleanTitle}</em>", <strong>${sourceName}</strong>, by ${author}, ${formattedDate}
        <a href="${url}" target="_blank" rel="noopener noreferrer" class="citation-url" title="Open original article in new tab">
          <i class="fas fa-external-link-alt" style="margin-right: 0.35rem; font-size: 0.85rem;"></i>${url}
        </a>
      </div>
    `;
  } else {
    return `
      <div class="article-source-citation">
        <span class="citation-label">Nguồn trích dẫn gốc:</span> "<em class="citation-title">${cleanTitle}</em>", <strong>${sourceName}</strong>, tác giả ${author}, ${formattedDate}
        <a href="${url}" target="_blank" rel="noopener noreferrer" class="citation-url" title="Mở bài báo gốc trong tab mới">
          <i class="fas fa-external-link-alt" style="margin-right: 0.35rem; font-size: 0.85rem;"></i>${url}
        </a>
      </div>
    `;
  }"""

c_norm = c.replace('\r\n', '\n')
target_norm = target.replace('\r\n', '\n')
replacement_norm = replacement.replace('\r\n', '\n')

if target_norm in c_norm:
    c_norm = c_norm.replace(target_norm, replacement_norm, 1)
    with open('js/app.js', 'w', encoding='utf-8') as f:
        f.write(c_norm)
    print("Successfully updated formatArticleSource in js/app.js!")
else:
    print("Error: Target not found in js/app.js!")
    sys.exit(1)
