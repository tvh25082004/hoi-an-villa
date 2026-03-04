"""
Update remaining 8 tours that still use tour-image-container.
Convert them to gallery sliders too (1 or more images).
"""
import re

html_path = r"c:\Users\TranHuy_WIN\Desktop\booking-vietnam\sontra-villa\index.html"

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

def build_gallery_html(tour_id, images):
    """Build swipeable gallery HTML for tour card."""
    slides = ''
    for img in images:
        slides += f'<div class="tg-slide"><img src="{img}" alt="Tour Photo" loading="lazy"></div>\n              '
    
    arrows = ''
    dots_html = ''
    if len(images) > 1:
        dots = ''.join(
            f'<span class="tg-dot{"  tg-active" if i == 0 else ""}"></span>'
            for i in range(len(images))
        )
        arrows = f'''
              <button class="tg-arrow tg-prev" onclick="tgPrev(event, this)" aria-label="prev">&#8249;</button>
              <button class="tg-arrow tg-next" onclick="tgNext(event, this)" aria-label="next">&#8250;</button>
              <div class="tg-dots">{dots}</div>'''
    
    return f'''<div class="tour-gallery" id="tg-{tour_id}">
              <div class="tg-track">
              {slides}</div>{arrows}
            </div>'''

# Image assignments for remaining tours
REMAINING_TOURS = {
    # Da Nang tours - use existing danang jpgs as single images (they look great already)
    't27': ['picture/danang_1.jpg'],   # Ba Na Hills / Golden Bridge
    't28': ['picture/danang_2.jpg'],   # Ba Na Hills + Dragon Bridge Night
    't29': ['picture/danang_3.jpg'],   # Da Nang Scenic + Ba Na Hills
    't31': ['picture/docx_monkey1.png', 'picture/docx_monkey2.png'],  # Marble Mt + Monkey Mt + Hoi An River - use monkey/marble docx images
    't36': ['hue_signature_1772543822350.png'],  # Hue tour - keep signature img
    't37': ['picture/danang_10.jpg'],  # Full Day Da Nang + Hoi An + Coconut
    # Hoi An tours
    't02': ['picture/hoian_6.jpg'],    # Street Food Tour
    't16': ['picture/hoian_3.jpg'],    # Hoi An Old Town tours
}

def replace_old_container(html, tour_id, gallery_html):
    """Replace tour-image-container for the given tour."""
    # Find the tour's openTourModal call
    start_marker = f"openTourModal('{tour_id}')"
    pos = html.find(start_marker)
    if pos == -1:
        print(f"  *** Not found: {tour_id}")
        return html
    
    # Find the nearest tour-image-container after that position
    img_start = html.find('<div class="tour-image-container">', pos)
    if img_start == -1:
        print(f"  *** No image container for {tour_id}")
        return html
    
    img_end = html.find('</div>', img_start) + len('</div>')
    old = html[img_start:img_end]
    html = html[:img_start] + gallery_html + html[img_end:]
    print(f"  Updated {tour_id}: {len(old)} -> {len(gallery_html)} chars")
    return html

total = 0
for tour_id, images in REMAINING_TOURS.items():
    gallery = build_gallery_html(tour_id, images)
    new_html = replace_old_container(html, tour_id, gallery)
    if new_html != html:
        total += 1
    html = new_html

print(f"\nTotal updated: {total}")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML written!")
