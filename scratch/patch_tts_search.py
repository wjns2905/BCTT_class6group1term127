# -*- coding: utf-8 -*-
import sys

def main():
    with open('js/app.js', 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Update startTextToSpeech to handle language
    tts_old = """function startTextToSpeech(articleId) {
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
  };"""

    tts_new = """function startTextToSpeech(articleId) {
  const article = ARTICLES_DATA.find(a => a.id === articleId);
  if (!article || !('speechSynthesis' in window)) {
    alert(currentLanguage === 'en' ? 'Your browser does not support Web Speech API.' : 'Trình duyệt của bạn chưa hỗ trợ tính năng Web Speech API.');
    return;
  }

  window.speechSynthesis.cancel();

  const isEn = (currentLanguage === 'en');
  let plainText = '';
  const content = (isEn && article.content_en) ? article.content_en : article.content;
  if (typeof content === 'string') {
    plainText = content.replace(/<[^>]*>/g, ' ');
  } else if (Array.isArray(content)) {
    plainText = content.join(' ');
  }

  const title = (isEn && article.title_en) ? article.title_en : article.title;
  const subtitle = (isEn && article.subtitle_en) ? article.subtitle_en : article.subtitle;
  const textToRead = `${title}. ${subtitle}. ${plainText}`;
  speechUtterance = new SpeechSynthesisUtterance(textToRead);
  speechUtterance.lang = isEn ? 'en-US' : 'vi-VN';
  speechUtterance.rate = 0.95;

  speechUtterance.onstart = () => {
    isSpeaking = true;
    updateTTSButton(true);
    showToast(isEn ? 'Playing article audio...' : 'Đang phát giọng đọc bài báo...', 'volume-up');
  };"""

    # 2. Update search search logic to search both vi & en and show bilingual empty message
    search_old = """  const matches = ARTICLES_DATA.filter(a => {
    return a.title.toLowerCase().includes(trimmed) ||
           a.subtitle.toLowerCase().includes(trimmed) ||
           a.author.toLowerCase().includes(trimmed) ||
           a.categoryName.toLowerCase().includes(trimmed) ||
           (a.tags && a.tags.some(t => t.toLowerCase().includes(trimmed)));
  });

  if (matches.length === 0) {
    resultsBox.innerHTML = `
      <div style="text-align:center; padding:2rem 0; color:var(--color-text-muted);">
        <i class="fas fa-search" style="font-size:2rem; margin-bottom:0.75rem; opacity:0.5;"></i>
        <p>Không tìm thấy bài viết nào khớp với '<strong>${query}</strong>'</p>
        <p style="font-size:0.8125rem; margin-top:0.25rem;">Hãy thử tìm theo tên chuyên mục: <em>Trending, Society, Human Stories, Mind &amp; Soul...</em></p>
      </div>
    `;
    return;
  }"""

    search_new = """  const isEn = (currentLanguage === 'en');
  const matches = ARTICLES_DATA.filter(a => {
    return a.title.toLowerCase().includes(trimmed) ||
           (a.title_en && a.title_en.toLowerCase().includes(trimmed)) ||
           a.subtitle.toLowerCase().includes(trimmed) ||
           (a.subtitle_en && a.subtitle_en.toLowerCase().includes(trimmed)) ||
           a.author.toLowerCase().includes(trimmed) ||
           a.categoryName.toLowerCase().includes(trimmed) ||
           (a.tags && a.tags.some(t => t.toLowerCase().includes(trimmed)));
  });

  if (matches.length === 0) {
    const emptyTitle = isEn ? `No articles found matching '<strong>${query}</strong>'` : `Không tìm thấy bài viết nào khớp với '<strong>${query}</strong>'`;
    const emptySub = isEn ? `Try searching by topic: <em>Trending, Society, Human Stories, Mind &amp; Soul...</em>` : `Hãy thử tìm theo tên chuyên mục: <em>Trending, Society, Human Stories, Mind &amp; Soul...</em>`;
    resultsBox.innerHTML = `
      <div style="text-align:center; padding:2rem 0; color:var(--color-text-muted);">
        <i class="fas fa-search" style="font-size:2rem; margin-bottom:0.75rem; opacity:0.5;"></i>
        <p>${emptyTitle}</p>
        <p style="font-size:0.8125rem; margin-top:0.25rem;">${emptySub}</p>
      </div>
    `;
    return;
  }"""

    # Normalize line endings
    norm_text = text.replace('\r\n', '\n')
    norm_tts_old = tts_old.replace('\r\n', '\n')
    norm_tts_new = tts_new.replace('\r\n', '\n')
    norm_search_old = search_old.replace('\r\n', '\n')
    norm_search_new = search_new.replace('\r\n', '\n')

    if norm_tts_old in norm_text:
        norm_text = norm_text.replace(norm_tts_old, norm_tts_new)
        print('SUCCESS: tts replaced')
    else:
        print('FAIL: tts_old not found')

    if norm_search_old in norm_text:
        norm_text = norm_text.replace(norm_search_old, norm_search_new)
        print('SUCCESS: search replaced')
    else:
        print('FAIL: search_old not found')

    with open('js/app.js', 'w', encoding='utf-8') as f:
        f.write(norm_text)
    print('js/app.js updated successfully!')

if __name__ == '__main__':
    main()
