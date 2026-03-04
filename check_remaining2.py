"""
Find tours that still have old tour-image-container div and update them to gallery sliders.
Also add proper docx images where missing, or use the existing jpg as a single-image gallery.
"""
import re

html_path = r"c:\Users\TranHuy_WIN\Desktop\booking-vietnam\sontra-villa\index.html"

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find all tour-image-container usages with their context
matches = list(re.finditer(r'<div class="tour-image-container">(.*?)</div>', html, re.DOTALL))
print(f"Remaining tour-image-container occurrences: {len(matches)}")

for m in matches:
    # Show 200 chars before to find which tour
    start = max(0, m.start() - 300)
    context = html[start:m.start()]
    modal_match = re.search(r"openTourModal\('(t\d+)'\)", context)
    tour_id = modal_match.group(1) if modal_match else "?"
    img_match = re.search(r'src="([^"]+)"', m.group(0))
    img = img_match.group(1) if img_match else "?"
    print(f"  Tour {tour_id}: {img}")
