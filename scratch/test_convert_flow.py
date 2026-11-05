import sys, os, docx, json, re

sys.stdout.reconfigure(encoding='utf-8')

from test_full_parse import parse_docx_articles

arts = parse_docx_articles('Tài nguyên/[BCTT] Mind & Soul.docx', 'mind-soul', 'mind_&_soul')
a = arts[0] # Taeyang
print(f"Article: {a['header']}")
print("Raw flow items:", len(a['flow']))

def convert_flow_to_content(flow, folder_name):
    content = []
    i = 0
    while i < len(flow):
        item = flow[i]
        itype = item[0]
        
        if itype == 'p':
            txt = item[1]
            imgs = item[2]
            
            # Check if this item has an image
            if imgs:
                # filter out tiny icons
                valid_imgs = []
                for img in imgs:
                    img_path = os.path.join('assets/images', folder_name, img)
                    if os.path.exists(img_path) and os.path.getsize(img_path) > 2000:
                        valid_imgs.append((img, img_path))
                
                caption = txt
                # If current paragraph had no caption text, check if next paragraph is caption
                if not caption and i + 1 < len(flow) and flow[i+1][0] == 'p' and not flow[i+1][2]:
                    next_txt = flow[i+1][1]
                    if any(k in next_txt.lower() for k in ['photo', 'ảnh', 'by ', 'huyền chi', 'thùy trang', 'nguồn']):
                        caption = next_txt
                        i += 1
                    elif len(next_txt) < 180 and not next_txt.endswith('.'):
                        caption = next_txt
                        i += 1
                        
                for img, img_path in valid_imgs:
                    fig_html = f'''<figure class="article-body-figure" style="margin:2rem 0; text-align:center;">
  <img src="assets/images/{folder_name}/{img}" alt="{caption or 'Article photo'}" style="max-width:100%; height:auto; border-radius:8px; box-shadow:0 4px 16px rgba(0,0,0,0.06); display:block; margin:0 auto;">
  {f'<figcaption class="article-body-figcaption" style="font-family:var(--font-sans); font-size:0.875rem; color:var(--color-text-muted); margin-top:0.6rem; font-style:italic; line-height:1.5; text-align:center;">{caption}</figcaption>' if caption else ''}
</figure>'''
                    content.append(fig_html)
                    
            elif txt:
                # Regular text or subheading or metadata
                # Ignore metadata lines like "VÂN CHI - 11:57..." or date lines if already captured
                if re.match(r'^(monday|tuesday|wednesday|thursday|friday|saturday|sunday|mon|tue|wed|thu|fri|sat|sun),', txt, re.I):
                    pass # date
                elif any(txt.lower().startswith(x) for x in ['by ', 'get vnexpress', 'link bài', 'link gốc', 'bài gốc']):
                    pass # metadata
                elif any(txt.lower().startswith(x) for x in ['photo:', '(photo', 'ảnh:']):
                    pass # orphaned caption
                elif len(txt) < 80 and not txt.endswith('.') and not txt.endswith('!') and not txt.endswith('?') and not txt.endswith('”') and not txt.endswith('"'):
                    content.append(f"### {txt}")
                else:
                    content.append(txt)
                    
        elif itype == 'tbl':
            # Check if image table or data table
            tbl_rows = item[1]
            has_table_imgs = any(any(c[1] for c in r) for r in tbl_rows)
            if has_table_imgs:
                # Image gallery / cards table
                # Usually row 0 is image, row 1 is caption
                if len(tbl_rows) >= 2:
                    imgs = [c[1] for c in tbl_rows[0] if c[1]]
                    caps = [c[0] for c in tbl_rows[1] if c[0]]
                    flat_imgs = [im for sub in imgs for im in sub]
                    for idx, img in enumerate(flat_imgs):
                        img_path = os.path.join('assets/images', folder_name, img)
                        if os.path.exists(img_path) and os.path.getsize(img_path) > 2000:
                            cap = caps[idx] if idx < len(caps) else ''
                            fig_html = f'''<figure class="article-body-figure" style="margin:2rem 0; text-align:center;">
  <img src="assets/images/{folder_name}/{img}" alt="{cap or 'Photo'}" style="max-width:100%; height:auto; border-radius:8px; box-shadow:0 4px 16px rgba(0,0,0,0.06); display:block; margin:0 auto;">
  {f'<figcaption class="article-body-figcaption" style="font-family:var(--font-sans); font-size:0.875rem; color:var(--color-text-muted); margin-top:0.6rem; font-style:italic; line-height:1.5; text-align:center;">{cap}</figcaption>' if cap else ''}
</figure>'''
                            content.append(fig_html)
            else:
                # Data table
                table_html = ['<div class="article-table-wrap" style="overflow-x:auto; margin:2rem 0;"><table class="article-data-table" style="width:100%; border-collapse:collapse; font-size:0.9rem;">']
                for ri, r in enumerate(tbl_rows):
                    table_html.append('<tr>')
                    tag = 'th' if ri == 0 or ri == 1 else 'td'
                    for c in r:
                        table_html.append(f'<{tag} style="border:1px solid #E5E5E5; padding:0.6rem 0.8rem; text-align:left;">{c[0]}</{tag}>')
                    table_html.append('</tr>')
                table_html.append('</table></div>')
                content.append("".join(table_html))
                
        i += 1
    return content

c = convert_flow_to_content(a['flow'], a['folder'])
print(f"Generated {len(c)} content items for Taeyang article:")
for item in c:
    if item.startswith('<figure'):
        print("  [FIGURE IMAGE]")
    elif item.startswith('### '):
        print(f"  [HEADING] {item}")
    else:
        print(f"  [PARAGRAPH] {item[:70]}...")
