
import re

html_path = r"d:\project\booking\sontra-villa\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Helper to avoid duplicates by rotating
danang_imgs = [f"picture/danang_{i}.jpg" for i in range(1, 11)]
hoian_imgs = [f"picture/hoian_{i}.jpg" for i in range(1, 11)]

dn_idx = 0
ha_idx = 0

def tour_replacer(match):
    global dn_idx, ha_idx
    card_html = match.group(0)
    region_match = re.search(r'data-region="([^"]+)"', card_html)
    if not region_match:
        return card_html
    
    region = region_match.group(1)
    
    if region == 'danang':
        img = danang_imgs[dn_idx % len(danang_imgs)]
        dn_idx += 1
        # Replace img src inside this card
        card_html = re.sub(r'src="[^"]+"', f'src="{img}"', card_html)
    elif region == 'hoian':
        img = hoian_imgs[ha_idx % len(hoian_imgs)]
        ha_idx += 1
        # Replace img src inside this card
        card_html = re.sub(r'src="[^"]+"', f'src="{img}"', card_html)
        
    return card_html

# We need to find the tour cards. They look like <div class="tour-card ..."> ... </div>
# Due to potentially nested tags, we'll try to find by blocks.
# A tour-card block ends with </div> and the next one starts or it's the end of container.
# However, re.DOTALL is needed.

# Let's use a more robust regex for the tour card blocks.
# Matches: <div class="tour-card ..."> [content] </div>
# Note: This might be tricky if there are nested divs. 
# But in the provided index.html snippet, tour-card structure is simple.

new_content = re.sub(r'<div class="tour-card[^"]*"[^>]*>.*?</div>\s+</div>', tour_replacer, content, flags=re.DOTALL)
# Wait, the closing pattern is a bit different in some cases.
# Let's try to match from <div class="tour-card" to the next </div> that matches the card end.
# Actually, the snippet shows:
# <div class="tour-card ...">
#   ...
#   <div class="tour-card-click-hint">...</div>
# </div>

pattern = r'(<div class="tour-card[^>]*>.*?<div class="tour-card-click-hint">.*?</div>\s*</div>)'
new_content = re.sub(pattern, tour_replacer, content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Updated {dn_idx} Da Nang cards and {ha_idx} Hoi An cards.")
