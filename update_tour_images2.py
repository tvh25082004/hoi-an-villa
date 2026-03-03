
import re

with open(r'd:\project\booking\sontra-villa\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Split at tour-list-container
container_start = html.find('id="tour-list-container"')
before = html[:container_start]
after_container = html[container_start:]

# Find the end of tour-list-container div (find closing </div> that matches)
# Look for the end of the tour list section - it closes before modal overlay
end_marker = '<!-- ===== TOUR DETAIL MODALS ====='
container_section_end = after_container.find(end_marker)
tour_section = after_container[:container_section_end]
rest = after_container[container_section_end:]

# All img src in the new tour cards (after the container start)
# We'll replace them based on their h3 title content or sequential order
# 
# Better approach: find each tour-card block, identify by h3 title, then replace img src

# List of (title_substring, img_filename) for each tour card in order
tour_img_assignments = [
    # OLD 5 already updated - skip them
    # NEW tours from PDF (they appear after old 5 in the container)
    # These cards were added in our replacement script and use placeholder images
    
    # From the new PDF injection (tours 6 onwards in HTML which are t01-t40 from our PDF)
    # HOI AN COOKING SCHOOL
    ("Market Tour, Basket Boat",        "tour_cooking_class.jpg"),
    ("Sidewalk Food Tour",              "tour_street_food.jpg"),
    ("Buffalo Riding, Basket Boat",     "tour_buffalo_cycling.jpg"),
    ("Basket Boat Ride &amp; Coconut",  "tour_basket_boat_coconut.jpg"),
    ("Basket Boat Ride &amp; Vietnamese Food", "tour_basket_boat_food.jpg"),
    ("Lantern Making, Market",          "tour_lantern_cooking.jpg"),
    # CU LAO CHAM
    ("Cham Island Daily Tour",          "tour_cham_daily.jpg"),
    ("Cham Island Handicraft",          "tour_cham_handicraft.jpg"),
    ("Cham Island 2 Ngày",              "tour_cham_homestay.jpg"),
    ("Cham Island Snorkeling Tour",     "tour_cham_snorkeling.jpg"),
    ("Cù Lao Chàm Try Dive",            "tour_cham_trydive.jpg"),
    ("Cù Lao Chàm Fun Dive",            "tour_cham_fundive.jpg"),
    ("Walking Underwater",              "tour_cham_walkingunder.jpg"),
    # HOI AN GREEN TRAVEL eco
    ("Cam Thanh Eco Water",             "tour_camthanh_eco.jpg"),
    ("Cam Thanh Cooking Tour",          "tour_camthanh_cooking.jpg"),
    ("Hội An City Tour – Boat",         "tour_hoian_city_boat.jpg"),
    ("Cẩm Thanh Coconut – Hội An City", "tour_hoian_lantern_night.jpg"),
    ("Bicycle Tour: Cam Thanh",         "tour_bicycle_camthanh.jpg"),
    ("Tra Que Cooking Class",           "tour_traque_cooking.jpg"),
    ("Lantern Making &amp; Farming",    "tour_lantern_farming.jpg"),
    ("Cycling, Buffalo Riding",         "tour_cycling_buffalo.jpg"),
    ("Tra Nhieu Eco Tour",              "tour_tranhieu_kimbong.jpg"),
    ("Rice Paper Noodle Making",        "tour_ricepaper_kimbong.jpg"),
    # MY SON
    ("Mỹ Sơn Sunrise Daily",            "tour_myson_sunrise.jpg"),
    ("Mỹ Sơn Sanctuary Luxury",         "tour_myson_luxury.jpg"),
    ("Mỹ Sơn Sunset Tour",              "tour_myson_sunset.jpg"),
    # RUNG DUA
    ("Tour Cơ Bản – Thuyền Thúng",      "tour_runggdua_basic.jpg"),
    ("Tour Trải Nghiệm + Quay Thúng",   "tour_runggdua_experience.jpg"),
    ("Tour Trọn Gói + Ăn Uống",         "tour_runggdua_allincl.jpg"),
    # HUE
    ("Huế City Tour",                   "tour_hue_citytour.jpg"),
    # DA NANG
    ("Bà Nà Hills Tour",                "tour_bana_fullday.jpg"),
    ("Bà Nà Hills Chiều + Cầu Rồng",   "tour_bana_dragon.jpg"),
    ("Đà Nẵng City Sites",              "tour_danang_bana_full.jpg"),
    ("Núi Khỉ – Ngũ Hành Sơn – Hội An Phố Cổ", "tour_nkhe_nhs_hoian.jpg"),
    ("Ngũ Hành Sơn – Hội An City – Thuyền", "tour_nhs_hoian_lantern.jpg"),
    ("Núi Khỉ – Ngũ Hành Sơn – Âm Phủ", "tour_nkhe_nhs_cruise.jpg"),
    ("Núi Khỉ – Ngũ Hành Sơn &amp; Mỹ Sơn", "tour_nkhe_nhs_myson.jpg"),
    ("Ngũ Hành Sơn – Núi Khỉ – Hang Âm Phủ (Buổi Sáng)", "tour_nhs_morning.jpg"),
    ("Ngũ Hành Sơn – Núi Khỉ – Hang Âm Phủ (Sunset", "tour_nhs_sunset.jpg"),
    ("Monkey Mountain",                 "tour_monkey_full.jpg"),
]

updated = 0
for title_sub, img_file in tour_img_assignments:
    # Find this card by its h3 title
    title_idx = tour_section.find(title_sub)
    if title_idx < 0:
        print(f"[MISS] {title_sub[:40]}")
        continue
    
    # Within the card block: find the img tag BEFORE the title (since img is before tour-info)
    # Extract the card block (go back from title to find start of card)
    # The structure is: ... onclick=... > tour-badge ... tour-image-container > img ... tour-info h3>title
    # So img appears BEFORE the title in the block
    card_start_from = max(0, title_idx - 600)
    card_block = tour_section[card_start_from:title_idx]
    
    # Find last img src in this block
    img_matches = list(re.finditer(r'<img\s+src="([^"]+)"', card_block))
    if not img_matches:
        print(f"[NO IMG] {title_sub[:40]}")
        continue
    
    last_img = img_matches[-1]
    old_src = last_img.group(1)
    if old_src == img_file:
        print(f"[SAME] {title_sub[:40]}")
        continue
    
    # Replace in tour_section
    abs_pos = card_start_from + last_img.start()
    old_tag = last_img.group(0)
    new_tag = f'<img src="{img_file}"'
    
    # Replace only in tour_section
    tour_section = tour_section[:card_start_from] + card_block.replace(old_tag, new_tag, 1) + tour_section[title_idx:]
    print(f"[OK] {title_sub[:40]} -> {img_file}")
    updated += 1

# Reassemble HTML 
html_new = before + tour_section + rest
with open(r'd:\project\booking\sontra-villa\index.html', 'w', encoding='utf-8') as f:
    f.write(html_new)

print(f"\nDone! {updated} tour card images updated.")
