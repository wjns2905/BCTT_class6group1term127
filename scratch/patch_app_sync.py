import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

sync_func = """
function syncHomepageCardsWithData(lang) {
  if (typeof ARTICLES_DATA === 'undefined') return;
  const isEn = (lang === 'en');

  document.querySelectorAll('[onclick*="openArticleModal"]').forEach(el => {
    const match = el.getAttribute('onclick').match(/openArticleModal\\(['"]([^'"]+)['"]\\)/);
    if (!match) return;
    const aid = match[1];
    const art = ARTICLES_DATA.find(a => a.id === aid);
    if (!art) return;

    // 1. Sync Image src if present
    const img = el.querySelector('img');
    if (img && art.image && !img.src.endsWith(art.image)) {
      img.src = art.image;
    }

    // 2. Sync title if present and not overridden by data-i18n
    const titleEl = el.querySelector('.stream-mini-headline, .center-post-title, .widget-card-headline, .mosaic-small-title, .culture-item-title, .related-text');
    if (titleEl && !titleEl.hasAttribute('data-i18n')) {
      const chosenTitle = isEn ? (art.title_en || art.title) : (art.title || art.title_en);
      if (chosenTitle) {
        titleEl.textContent = chosenTitle;
      }
    }
  });
}
window.syncHomepageCardsWithData = syncHomepageCardsWithData;
"""

target = "  renderAboutUsSection();"
replacement = "  renderAboutUsSection();\n  syncHomepageCardsWithData(lang);"

if target in text:
    text = text.replace(target, replacement)
    # Add function before applyLanguage
    text = text.replace("function applyLanguage(lang) {", sync_func + "\nfunction applyLanguage(lang) {")
    with open('js/app.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("✓ Added syncHomepageCardsWithData to js/app.js!")
else:
    print("ERROR: Target string not found in js/app.js!")
    sys.exit(1)
