import re
with open(r'c:\Users\TranHuy_WIN\Desktop\booking-vietnam\sontra-villa\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find tours still using old tour-image-container (not gallery)
old_pattern = re.findall(r"openTourModal\('(t\d+)'\).*?<div class=\"tour-image-container\">.*?src=\"([^\"]+)\"", html, re.DOTALL)
print('Tours still using old image container:')
for tour_id, img_src in old_pattern:
    print(f'  {tour_id}: {img_src}')
print(f'\nTotal: {len(old_pattern)}')
