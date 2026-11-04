import docx
import zipfile
import xml.etree.ElementTree as ET
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT = r"c:\Users\camka\OneDrive\Desktop\BCTT\Tài nguyên"

def analyze_doc_images(fn):
    docx_path = os.path.join(ROOT, fn)
    doc = docx.Document(docx_path)
    print(f"\n==========================================")
    print(f"MAPPING IMAGES FOR: {fn}")
    print(f"==========================================")
    
    # Open docx as zip to inspect document.xml and rels
    with zipfile.ZipFile(docx_path, 'r') as z:
        # Load rels to map rId to image filename
        rels_xml = z.read('word/_rels/document.xml.rels')
        rels_tree = ET.fromstring(rels_xml)
        rid_map = {}
        for rel in rels_tree:
            rid = rel.attrib.get('Id')
            target = rel.attrib.get('Target')
            if target and 'media/' in target:
                rid_map[rid] = os.path.basename(target)
                
        # Parse document.xml to see which paragraph has which rId
        doc_xml = z.read('word/document.xml')
        doc_tree = ET.fromstring(doc_xml)
        
        # Walk through body elements
        # w:p paragraphs
        ns = {
            'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
            'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
            'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
        }
        
        body = doc_tree.find('w:body', ns)
        current_article = "Start"
        article_images = {}
        
        for p in body.findall('w:p', ns):
            # Get text
            texts = [t.text for t in p.findall('.//w:t', ns) if t.text]
            p_text = "".join(texts).strip()
            
            # Check if this paragraph is a title or link
            if p_text and any(k in p_text.lower() for k in ['http://', 'https://', 'link gốc', 'link bài', 'bài gốc']):
                current_article = p_text[:60]
                if current_article not in article_images:
                    article_images[current_article] = []
            elif p_text and len(p_text) > 15 and current_article == "Start":
                current_article = p_text[:60]
                article_images[current_article] = []
                
            # Find drawings/blips
            for blip in p.findall('.//a:blip', ns):
                embed_id = blip.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                if embed_id and embed_id in rid_map:
                    img_name = rid_map[embed_id]
                    if current_article not in article_images:
                        article_images[current_article] = []
                    article_images[current_article].append(img_name)
                    print(f"Found image {img_name} in article: '{current_article}' (text nearby: '{p_text[:40]}')")

for f in ['[BCTT] Trending.docx', '[BCTT] Society.docx', '[BCTT] Human stories.docx', '[BCTT] Mind & Soul.docx', '[BCTT] In-dept.docx']:
    analyze_doc_images(f)
