with open("scratch/build_multi_pages.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update podcast box text colors
code = code.replace(
    'style="font-size:0.875rem; color:#E5D0D0; line-height:1.5;"',
    'style="font-size:0.925rem; color:#FFFFFF; line-height:1.6; font-weight:500;"'
)
code = code.replace(
    'style="font-size:0.75rem; color:#D3C0C0;"',
    'style="font-size:0.8125rem; color:#FFFFFF; font-weight:700;"'
)

# 2. Update drawer text colors
code = code.replace(
    'style="font-size:0.75rem; color:#A99F94;"',
    'style="font-size:0.8125rem; color:#E2D8D4; font-weight:600;"'
)
code = code.replace(
    'style="font-size:0.875rem; color:#FFB3B3; font-weight:600;"',
    'style="font-size:0.925rem; color:#FFFFFF; font-weight:700;"'
)

# 3. Update search modal placeholder message
code = code.replace(
    'style="color:var(--color-text-muted); font-size:0.9rem;"',
    'style="color:var(--color-text-body); font-size:0.95rem; font-weight:500;"'
)

with open("scratch/build_multi_pages.py", "w", encoding="utf-8") as f:
    f.write(code)

print("scratch/build_multi_pages.py updated!")
