import re
import sys

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    def r(match):
        pre, title, mid, old_img, post = match.groups()
        t = title.lower()
        if "cham island" in t or "snorkeling" in t or "dive" in t or "underwater" in t or "cù lao chàm" in t:
            img = "cham_island_signature.png"
        elif "my son" in t or "mỹ sơn" in t:
            img = "myson_signature.png"
        elif "hue" in t or "hai van" in t or "huế" in t:
            img = "hue_signature.png"
        elif "dragon" in t or "cruise" in t or "night tour" in t or "thuyền" in t and "đà nẵng" in t:
            img = "danang_dragon_signature.png"
        elif "marble" in t or "monkey" in t or "hell cave" in t or "ngũ hành" in t:
            img = "danang_marble_signature.png"
        elif "ba na" in t or "golden bridge" in t or "bà nà" in t:
            img = "danang_signature.png"
        elif "cooking" in t or "food" in t or "market" in t or "rice paper" in t:
            img = "hoian_cooking_signature.png"
        elif "eco" in t or "basket boat" in t or "buffalo" in t or "farming" in t or "tra n" in t \
            or "tra que" in t or "kim bong" in t or "coconut" in t or "bicycle" in t or "cycling" in t or "cẩm thanh" in t:
            img = "hoian_eco_signature.png"
        elif "hoi an" in t or "city tour" in t or "lantern" in t or "phố cổ" in t:
            img = "hoian_signature.png"
        else:
            if "danang_signature" in old_img or "hue_signature" in old_img or "hoian_signature" in old_img:
                img = old_img
            else:
                img = "hoian_signature.png"
        return f'{pre}{title}{mid}{img}{post}'

    pattern = r'("title"\s*:\s*")(.*?)(".*?\"image\"\s*:\s*\")(.*?)(\")'
    new_content = re.sub(pattern, r, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

process_file(r'd:\project\booking\build_tours_part1.py')
process_file(r'd:\project\booking\build_tours_part2.py')
print("Successfully mapped 40 tours to new signature images.")
