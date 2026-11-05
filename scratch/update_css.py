with open('css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

target = """.article-source-box {
  background-color: #F4ECE1;
  border: 1px solid #DFD5C6;
  border-radius: var(--radius-md);
  padding: 1.25rem 1.5rem;
  margin: 2.5rem 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
}"""

replacement = """.article-source-box {
  display: none !important;
}

/* Journalistic & Academic Source Citation at the end of each article */
.article-source-citation {
  margin-top: 2.5rem;
  padding-top: 1.25rem;
  border-top: 1px dashed rgba(84, 17, 30, 0.2);
  color: #64748B; /* Lighter than body text */
  font-size: 0.9375rem;
  line-height: 1.8;
  font-family: var(--font-body, system-ui, sans-serif);
}

.article-source-citation .citation-label {
  font-weight: 700;
  color: #475569;
}

.article-source-citation .citation-title {
  font-style: italic;
  color: #334155;
  font-family: var(--font-serif, Georgia, serif);
}

.article-source-citation .citation-url {
  color: var(--color-brand-primary, #7D1728);
  text-decoration: underline;
  text-underline-offset: 3px;
  word-break: break-all;
  transition: color 0.2s ease;
}

.article-source-citation .citation-url:hover {
  color: var(--color-brand-accent, #B83246);
}"""

assert target in text, "Target not found in css/style.css!"
text = text.replace(target, replacement)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated css/style.css with .article-source-citation styles!")
