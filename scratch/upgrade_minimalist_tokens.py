with open("css/tokens.css", "r", encoding="utf-8") as f:
    tokens = f.read()

target = """  /* Font Primitives */
  --primitive-font-editorial: 'Bodoni Moda', 'Playfair Display', Didot, 'Cinzel', serif;
  --primitive-font-headline: 'Playfair Display', 'Bodoni Moda', 'Newsreader', Georgia, serif;
  --primitive-font-body: 'Newsreader', Georgia, serif;
  --primitive-font-ui: 'Plus Jakarta Sans', 'Source Sans 3', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --primitive-font-mono: 'SFMono-Regular', Consolas, monospace;"""

replacement = """  /* Modern Minimalist Typography System (Inter & Plus Jakarta Sans) */
  --primitive-font-editorial: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --primitive-font-headline: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --primitive-font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --primitive-font-ui: 'Inter', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --primitive-font-mono: 'SFMono-Regular', Consolas, Menlo, monospace;"""

norm_tokens = tokens.replace("\r\n", "\n")
norm_target = target.replace("\r\n", "\n")
norm_rep = replacement.replace("\r\n", "\n")

if norm_target in norm_tokens:
    norm_tokens = norm_tokens.replace(norm_target, norm_rep, 1)
    with open("css/tokens.css", "w", encoding="utf-8") as f:
        f.write(norm_tokens)
    print("tokens.css upgraded to Modern Minimalist Typography!")
else:
    print("Target not found in tokens.css")
