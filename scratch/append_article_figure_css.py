import sys

css_rules = """

/* ===================================================================
   ARTICLE BODY MEDIA & INLINE FIGURES (Full Editorial Fidelity)
   =================================================================== */
.article-body-figure {
  margin: 2.25rem 0 !important;
  text-align: center;
  display: block;
  clear: both;
}
.article-body-figure img {
  max-width: 100%;
  height: auto;
  border-radius: var(--radius-md, 8px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.07);
  display: block;
  margin: 0 auto;
  transition: transform var(--duration-fast, 0.2s) ease;
}
.article-body-figure img:hover {
  transform: scale(1.01);
}
.article-body-figcaption {
  font-family: var(--font-sans, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif);
  font-size: 0.875rem;
  color: var(--color-text-muted, #666);
  margin-top: 0.65rem;
  font-style: italic;
  line-height: 1.5;
  text-align: center;
  padding: 0 1rem;
}
.article-table-wrap {
  overflow-x: auto;
  margin: 2rem 0;
  border-radius: var(--radius-md, 8px);
  border: 1px solid var(--color-border-hairline, #E5E5E5);
}
.article-data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}
.article-data-table th,
.article-data-table td {
  padding: 0.65rem 0.85rem;
  border: 1px solid var(--color-border-hairline, #E5E5E5);
  text-align: left;
}
.article-data-table th {
  background-color: rgba(84, 17, 30, 0.05);
  font-weight: 700;
  color: var(--color-brand-primary, #54111E);
}
"""

with open('css/style.css', 'r', encoding='utf-8') as f:
    c = f.read()

if '.article-body-figure' not in c:
    with open('css/style.css', 'a', encoding='utf-8') as f:
        f.write(css_rules)
    print("Appended article figure styles to css/style.css")
else:
    print("Styles already present.")
