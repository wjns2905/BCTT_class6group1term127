import sys

with open('js/app.js', 'r', encoding='utf-8') as f:
    c = f.read()

target = """  let bodyHtml = '';
  if (typeof article.content === 'string') {
    bodyHtml = article.content;
  } else if (Array.isArray(article.content)) {
    bodyHtml = article.content.map(p => {
      if (p.startsWith('### ')) {
        return `<h3 style="font-family:var(--font-editorial); font-size:1.35rem; font-weight:800; color:var(--color-brand-primary); margin:1.5rem 0 0.75rem 0;">${p.replace('### ', '')}</h3>`;
      }
      return `<p style="margin-bottom:1.15rem; line-height:1.8;">${p}</p>`;
    }).join('');
  }"""

replacement = """  let bodyHtml = '';
  if (typeof article.content === 'string') {
    bodyHtml = article.content;
  } else if (Array.isArray(article.content)) {
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

c_norm = c.replace('\r\n', '\n')
target_norm = target.replace('\r\n', '\n')
replacement_norm = replacement.replace('\r\n', '\n')

if target_norm in c_norm:
    c_norm = c_norm.replace(target_norm, replacement_norm, 1)
    with open('js/app.js', 'w', encoding='utf-8') as f:
        f.write(c_norm)
    print("✓ Successfully updated bodyHtml logic in js/app.js!")
else:
    print("Error: Target not found in js/app.js!")
    sys.exit(1)
