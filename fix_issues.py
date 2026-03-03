"""Fix all remaining issues: broken images, Vietnamese header, and verify TOUR_DATA keys match onclick IDs"""
import re

with open(r'd:\project\booking\sontra-villa\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Vietnamese header -> English
html = html.replace('Tour Du Lịch 2026', 'Discovery Tours 2026')
html = html.replace('Trải nghiệm tuyển chọn – Hội An, Huế &amp; Đà Nẵng', 
                     'Hand-picked authentic experiences in Hoi An, Hue &amp; Da Nang')
html = html.replace('Trải nghiệm tuyển chọn – Hội An, Huế & Đà Nẵng',
                     'Hand-picked authentic experiences in Hoi An, Hue & Da Nang')

# 2. Fix broken image references - map old filenames to our downloaded files
image_fixes = {
    'ba_na_hills.png': 'tour_bana_fullday.jpg',
    'marble_mountains.png': 'tour_nkhe_nhs_hoian.jpg',
    'hai_van_pass.png': 'tour_hue_citytour.jpg',
    'hue_dmz.png': 'tour_hue_citytour.jpg',
    'countryside_cycling.png': 'tour_cycling_buffalo.jpg',
    'son_tra_peninsula.png': 'tour_monkey_full.jpg',
    'perfume_river.png': 'tour_cham_homestay.jpg',
    'fishing_village.png': 'tour_tranhieu_kimbong.jpg',
    'danang_city.png': 'tour_danang_bana_full.jpg',
    'bach_ma_park.png': 'tour_cham_fundive.jpg',
    'tra_que_village.png': 'tour_traque_cooking.jpg',
    'lantern_making.png': 'tour_lantern_cooking.jpg',
    'photo_tour.png': 'tour_camthanh_cooking.jpg',
    'spa_wellness.png': 'tour_hoian_city_boat.jpg',
    'tailoring_experience.png': 'tour_hoian_lantern_night.jpg',
    'street_food_night.png': 'tour_street_food.jpg',
    'pottery_village.png': 'tour_ricepaper_kimbong.jpg',
    'river_cruise_sunset.png': 'tour_lantern_farming.jpg',
    'water_puppet_show.png': 'tour_cycling_buffalo.jpg',
    'hue_water_park.png': 'tour_tranhieu_kimbong.jpg',
    'hue_royal_dinner.png': 'tour_ricepaper_kimbong.jpg',
    'danang_nightlife.png': 'tour_myson_sunrise.jpg',
    'danang_surfing.png': 'tour_myson_luxury.jpg',
    'danang_helicopter.png': 'tour_myson_sunset.jpg',
    'danang_golf.png': 'tour_hue_citytour.jpg',
    'golden_bridge.png': 'tour_bana_fullday.jpg',
    'hoi_an_town.png': 'tour_hoian_city_boat.jpg',
    'cooking_class.png': 'tour_cooking_class.jpg',
    'cham_island.png': 'tour_cham_snorkeling.jpg',
    'my_son.png': 'tour_myson_sunrise.jpg',
    'basket_boat.png': 'tour_basket_boat_coconut.jpg',
}

for old_img, new_img in image_fixes.items():
    count = html.count(old_img)
    if count > 0:
        html = html.replace(old_img, new_img)
        print(f"Fixed {old_img} -> {new_img} ({count} occurrences)")

# 3. Verify all TOUR_DATA keys exist
onclick_ids = re.findall(r"openTourModal\('([^']+)'\)", html)
tour_data_keys = re.findall(r"'([^']+)':\s*\{\s*\n\s*title:", html)
missing = [k for k in onclick_ids if k not in tour_data_keys]
print(f"\nonclick IDs: {len(onclick_ids)}")
print(f"TOUR_DATA keys: {len(tour_data_keys)}")
if missing:
    print(f"MISSING TOUR_DATA for: {missing}")
else:
    print("All onclick IDs have matching TOUR_DATA! ✓")

with open(r'd:\project\booking\sontra-villa\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nAll fixes applied!")
