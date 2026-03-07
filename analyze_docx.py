import sys, os
sys.stdout.reconfigure(encoding='utf-8')
from docx import Document
from docx.oxml.ns import qn
import lxml.etree as etree

doc = Document(r'c:\Users\TranHuy_WIN\Desktop\booking-vietnam\DaNang_HoiAn_Experience_Guide.docx')

# We need to walk through the document body elements in ORDER
# to correlate text headings with images

body = doc.element.body
elem_index = 0
img_counter = 0

print("=== FULL DOCUMENT STRUCTURE ===\n")

for elem in body:
    tag = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag
    
    if tag == 'p':
        # It's a paragraph - get text
        text = ''.join(r.text or '' for r in elem.findall('.//' + qn('w:t')))
        
        # Check for images inside this paragraph
        blips = elem.findall('.//' + qn('a:blip'))
        rIds = [b.get(qn('r:embed')) for b in blips if b.get(qn('r:embed'))]
        
        if text.strip():
            print(f"TEXT: {text.strip()[:100]}")
        
        if rIds:
            for rId in rIds:
                img_counter += 1
                # Get the actual part
                part = doc.part.related_parts.get(rId)
                filename = os.path.basename(part.partname) if part else rId
                print(f"  → IMAGE #{img_counter}: rId={rId}, file={filename}")
    
    elif tag == 'tbl':
        # Table - check cells for text and images
        print(f"[TABLE]")
        for row in elem.findall('.//' + qn('w:tr')):
            for cell in row.findall('.//' + qn('w:tc')):
                cell_text = ''.join(t.text or '' for t in cell.findall('.//' + qn('w:t')))
                blips = cell.findall('.//' + qn('a:blip'))
                rIds = [b.get(qn('r:embed')) for b in blips if b.get(qn('r:embed'))]
                if cell_text.strip():
                    print(f"  CELL TEXT: {cell_text.strip()[:80]}")
                if rIds:
                    for rId in rIds:
                        img_counter += 1
                        part = doc.part.related_parts.get(rId)
                        filename = os.path.basename(part.partname) if part else rId
                        print(f"    → IMAGE #{img_counter}: rId={rId}, file={filename}")

print(f"\n=== TOTAL IMAGES FOUND: {img_counter} ===")
