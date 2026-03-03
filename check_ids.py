import re
with open(r'd:\project\booking\sontra-villa\index.html','r',encoding='utf-8') as f:
    html=f.read()
ids = re.findall(r"openTourModal\('([^']+)'\)", html)
print('Tour card onclick IDs:', ids)
print('Count:', len(ids))
keys = re.findall(r"'([^']+)':\s*\{\s*\n\s*title:", html)
print('TOUR_DATA keys:', keys)
print('Keys count:', len(keys))
