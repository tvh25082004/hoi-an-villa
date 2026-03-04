"""
Analyze the docx file to understand the order of paragraphs and images as they appear in the document.
This reads the XML directly to see when images appear relative to text.
"""
import zipfile
import xml.etree.ElementTree as ET
import re
import os

docx_path = r"c:\Users\TranHuy_WIN\Desktop\booking-vietnam\picture.docx"

ns = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'v': 'urn:schemas-microsoft-com:vml',
}

with zipfile.ZipFile(docx_path, 'r') as z:
    # Read relationships to map rId to image filenames
    with z.open('word/_rels/document.xml.rels') as f:
        rels_tree = ET.parse(f)
    rels_root = rels_tree.getroot()
    
    rId_to_img = {}
    for rel in rels_root:
        target = rel.get('Target', '')
        rId = rel.get('Id', '')
        if 'media/' in target:
            rId_to_img[rId] = os.path.basename(target)
    
    print("Relationships (rId -> image):")
    for k, v in sorted(rId_to_img.items()):
        print(f"  {k}: {v}")
    
    # Read main document
    with z.open('word/document.xml') as f:
        doc_tree = ET.parse(f)
    doc_root = doc_tree.getroot()

import os

# Walk through body children and extract text + image references in order
body = doc_root.find('.//w:body', ns)
print("\n\n=== DOCUMENT STRUCTURE (in order) ===\n")

item_index = 0
for child in body:
    tag = child.tag.split('}')[-1] if '}' in child.tag else child.tag
    
    if tag == 'p':  # paragraph
        # Get text
        texts = []
        for t in child.findall('.//w:t', ns):
            texts.append(t.text or '')
        text = ''.join(texts).strip()
        
        # Check for inline images (drawing or pict)
        images = []
        for blip in child.findall('.//a:blip', ns):
            rEmbed = blip.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
            if rEmbed and rEmbed in rId_to_img:
                images.append(rId_to_img[rEmbed])
        
        # Also check for v:imagedata
        for imgdata in child.findall('.//v:imagedata', ns):
            rId = imgdata.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
            if rId and rId in rId_to_img:
                images.append(rId_to_img[rId])
        
        if text or images:
            print(f"[Item {item_index}] TEXT: '{text}' | IMAGES: {images}")
            item_index += 1
    
    elif tag == 'tbl':  # table
        print(f"[Item {item_index}] TABLE:")
        item_index += 1
        for row_idx, row in enumerate(child.findall('.//w:tr', ns)):
            for cell_idx, cell in enumerate(row.findall('.//w:tc', ns)):
                texts = []
                for t in cell.findall('.//w:t', ns):
                    texts.append(t.text or '')
                cell_text = ''.join(texts).strip()
                
                images = []
                for blip in cell.findall('.//a:blip', ns):
                    rEmbed = blip.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                    if rEmbed and rEmbed in rId_to_img:
                        images.append(rId_to_img[rEmbed])
                
                if cell_text or images:
                    print(f"  Row {row_idx}, Col {cell_idx}: text='{cell_text[:100]}' images={images}")
