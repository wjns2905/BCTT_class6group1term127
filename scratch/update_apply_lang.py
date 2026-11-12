import os

path = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

target = """  // Re-render open article modal if active
  const modal = document.getElementById('articleReaderModal');
  if (modal && modal.classList.contains('active')) {
    const activeArtId = modal.dataset.articleId;
    if (activeArtId) {
      openArticleModal(activeArtId);
    }
  }
}"""

replacement = """  // Re-render standalone article page if active
  const host = document.getElementById('standaloneArticleHost');
  if (host && typeof renderDedicatedArticlePage === 'function') {
    const urlParams = new URLSearchParams(window.location.search);
    const isSub = window.location.pathname.includes('/hearticles/');
    const articleId = isSub ? 'trending-1' : (urlParams.get('id') || 'trending-1');
    renderDedicatedArticlePage(articleId);
  }

  // Re-render open article modal if active (legacy fallback)
  const modal = document.getElementById('articleReaderModal');
  if (modal && modal.classList.contains('active')) {
    const activeArtId = modal.dataset.articleId;
    if (activeArtId && typeof openArticleModalLegacy === 'function') {
      openArticleModalLegacy(activeArtId);
    }
  }
}"""

assert target in text, "target not found in app.js"
text = text.replace(target, replacement, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("SUCCESS: Updated applyLanguage to re-render standalone article page on language switch.")
