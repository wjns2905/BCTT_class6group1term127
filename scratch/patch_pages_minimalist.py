with open("scratch/build_multi_pages.py", "r", encoding="utf-8") as f:
    code = f.read()

old_fonts = """  <!-- High-Fashion Editorial Typography: Bodoni Moda, Playfair Display, Plus Jakarta Sans, Newsreader -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900&family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400;1,6..72,600&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">"""

new_fonts = """  <!-- Modern Minimalist Editorial Typography: Plus Jakarta Sans (Headlines/Display) & Inter (Body/UI) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600;1,700&display=swap" rel="stylesheet">"""

code = code.replace(old_fonts, new_fonts)

# Update drawer title
code = code.replace(
    'style="color:#FFF; font-family:var(--font-editorial); font-size:1.6rem; font-style:italic;"',
    'style="color:#FFF; font-family:var(--font-editorial); font-size:1.6rem; font-weight:900; letter-spacing:-0.03em;"'
)

with open("scratch/build_multi_pages.py", "w", encoding="utf-8") as f:
    f.write(code)

print("scratch/build_multi_pages.py updated with Minimalist Typography links!")
