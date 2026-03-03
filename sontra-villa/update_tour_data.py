
import re
import json

html_path = r"d:\project\booking\sontra-villa\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Images
danang_imgs = [f"picture/danang_{i}.jpg" for i in range(1, 11)]
hoian_imgs = [f"picture/hoian_{i}.jpg" for i in range(1, 11)]

# Map IDs to regions based on the file content or manual mapping
# From previous observation:
# t27-t35, t37 are Danang
# t36 is Hue
# Others are Hoian

# Instead of hardcoding, let's parse the TOUR_DATA keys and their "region" field
# TOUR_DATA = { 'id': { "region": "..." } }

def update_tour_data(match):
    json_text = "{" + match.group(1) + "}"
    # This might be tricky if it's not valid JSON (e.g. JS object literal)
    # But TOUR_DATA looks very JSON-like.
    
    # Let's try to extract the entries one by one using regex instead of json.loads
    # entries look like 't01': { ... },
    entries = re.findall(r"'(\w+)':\s*({.*?}),?\n", json_text, re.DOTALL)
    
    dn_idx = 0
    ha_idx = 0
    
    new_entries = []
    for tour_id, data_str in entries:
        # data_str is a JS object string
        region_match = re.search(r'"region":\s*"([^"]+)"', data_str)
        if not region_match:
            new_entries.append(f"    '{tour_id}': {data_str},")
            continue
            
        region = region_match.group(1)
        if region == 'danang':
            img = danang_imgs[dn_idx % len(danang_imgs)]
            dn_idx += 1
            new_data_str = re.sub(r'"image":\s*"[^"]+"', f'"image": "{img}"', data_str)
            new_entries.append(f"    '{tour_id}': {new_data_str},")
        elif region == 'hoian':
            img = hoian_imgs[ha_idx % len(hoian_imgs)]
            ha_idx += 1
            new_data_str = re.sub(r'"image":\s*"[^"]+"', f'"image": "{img}"', data_str)
            new_entries.append(f"    '{tour_id}': {new_data_str},")
        else:
            new_entries.append(f"    '{tour_id}': {data_str},")
            
    return "const TOUR_DATA = {\n" + "\n".join(new_entries) + "\n  };"

# Find TOUR_DATA block
pattern = r"const TOUR_DATA = \{(.*?)\};"
new_content = re.sub(pattern, update_tour_data, content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated TOUR_DATA successfully.")
