import os

path = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

target = """  } else if (Array.isArray(contentSource)) {
    bodyHtml = article.content.map(p => {
      if (typeof p !== 'string') return '';
      const trimmed = p.trim();
      if (trimmed.startsWith('### ')) {
        return `<h3 class="article-section-heading" style="font-family:var(--font-editorial); font-size:1.35rem; font-weight:800; color:var(--color-brand-primary); margin:1.75rem 0 0.75rem 0;">${trimmed.replace('### ', '')}</h3>`;
      }
      if (trimmed.startsWith('## ')) {
        return `<h2 class="article-section-heading-lg" style="font-family:var(--font-editorial); font-size:1.55rem; font-weight:800; color:var(--color-brand-primary); margin:2rem 0 0.85rem 0;">${trimmed.replace('## ', '')}</h2>`;
      }
      if (trimmed.startsWith('<figure') || trimmed.startsWith('<table') || trimmed.startsWith('<div') || trimmed.startsWith('<blockquote')) {
        return trimmed;
      }
      return `<p style="margin-bottom:1.15rem; line-height:1.8; text-align:justify;">${p}</p>`;
    }).join('');
  }"""

replacement = """  } else if (Array.isArray(contentSource)) {
    bodyHtml = contentSource.map(p => {
      if (typeof p !== 'string') return '';
      let trimmed = p.trim();
      if (trimmed.startsWith('### ')) {
        return `<h3 class="article-section-heading" style="font-family:var(--font-editorial); font-size:1.35rem; font-weight:800; color:var(--color-brand-primary); margin:1.75rem 0 0.75rem 0;">${trimmed.replace('### ', '')}</h3>`;
      }
      if (trimmed.startsWith('## ')) {
        return `<h2 class="article-section-heading-lg" style="font-family:var(--font-editorial); font-size:1.55rem; font-weight:800; color:var(--color-brand-primary); margin:2rem 0 0.85rem 0;">${trimmed.replace('## ', '')}</h2>`;
      }
      if (trimmed.startsWith('<figure') || trimmed.startsWith('<table') || trimmed.startsWith('<div') || trimmed.startsWith('<blockquote')) {
        if (trimmed.includes('<img') && !trimmed.includes('onerror=')) {
          trimmed = trimmed.replace(/<img\\b/g, '<img onerror="handleImageError(this)"');
        }
        return trimmed;
      }
      return `<p style="margin-bottom:1.15rem; line-height:1.8; text-align:justify;">${p}</p>`;
    }).join('');
  }"""

assert target in text, "target not found in app.js"
text = text.replace(target, replacement, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("SUCCESS: Injected onerror handler into article figures.")
