
import re

with open(r'd:\project\booking\sontra-villa\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Map tour modal ID -> image file
# These are the existing 5 old tours + new ones need img updates in tour cards

# Old tours still in HTML use old images - update them by tour card content matching
# New tours from PDF injection use placeholder images - update them

replacements = [
    # OLD TOUR CARDS (by onclick ID)
    # Tour 1 old: cham-snorkeling -> use cham_daily
    ("openTourModal('cham-snorkeling')", "CHAM_SNORKELING"),
    ("openTourModal('basket-boat')",     "BASKET_BOAT"),
    ("openTourModal('bana-hills')",      "BANA_HILLS"),
    ("openTourModal('hoian-city')",      "HOIAN_CITY"),
    ("openTourModal('my-son')",          "MY_SON"),
    # New tours by ID
    ("openTourModal('t01')",  "T01"),
    ("openTourModal('t02')",  "T02"),
    ("openTourModal('t03')",  "T03"),
    ("openTourModal('t04')",  "T04"),
    ("openTourModal('t05')",  "T05"),
    ("openTourModal('t06')",  "T06"),
    ("openTourModal('t07')",  "T07"),
    ("openTourModal('t08')",  "T08"),
    ("openTourModal('t09')",  "T09"),
    ("openTourModal('t10')",  "T10"),
    ("openTourModal('t11')",  "T11"),
    ("openTourModal('t12')",  "T12"),
    ("openTourModal('t13')",  "T13"),
    ("openTourModal('t14')",  "T14"),
    ("openTourModal('t15')",  "T15"),
    ("openTourModal('t16')",  "T16"),
    ("openTourModal('t17')",  "T17"),
    ("openTourModal('t18')",  "T18"),
    ("openTourModal('t19')",  "T19"),
    ("openTourModal('t20')",  "T20"),
    ("openTourModal('t21')",  "T21"),
    ("openTourModal('t22')",  "T22"),
    ("openTourModal('t23')",  "T23"),
    ("openTourModal('t24')",  "T24"),
    ("openTourModal('t25')",  "T25"),
    ("openTourModal('t26')",  "T26"),
    ("openTourModal('t27')",  "T27"),
    ("openTourModal('t28')",  "T28"),
    ("openTourModal('t29')",  "T29"),
    ("openTourModal('t30')",  "T30"),
    ("openTourModal('t31')",  "T31"),
    ("openTourModal('t32')",  "T32"),
    ("openTourModal('t33')",  "T33"),
    ("openTourModal('t34')",  "T34"),
    ("openTourModal('t35')",  "T35"),
    ("openTourModal('t36')",  "T36"),
    ("openTourModal('t37')",  "T37"),
    ("openTourModal('t38')",  "T38"),
    ("openTourModal('t39')",  "T39"),
    ("openTourModal('t40')",  "T40"),
]

# Image mapping per tour
img_map = {
    "CHAM_SNORKELING": "tour_cham_snorkeling.jpg",
    "BASKET_BOAT":     "tour_basket_boat_coconut.jpg",
    "BANA_HILLS":      "tour_bana_fullday.jpg",
    "HOIAN_CITY":      "tour_hoian_city_boat.jpg",
    "MY_SON":          "tour_myson_sunrise.jpg",
    "T01": "tour_cooking_class.jpg",
    "T02": "tour_street_food.jpg",
    "T03": "tour_buffalo_cycling.jpg",
    "T04": "tour_basket_boat_coconut.jpg",
    "T05": "tour_basket_boat_food.jpg",
    "T06": "tour_lantern_cooking.jpg",
    "T07": "tour_cham_daily.jpg",
    "T08": "tour_cham_handicraft.jpg",
    "T09": "tour_cham_homestay.jpg",
    "T10": "tour_cham_snorkeling.jpg",
    "T11": "tour_cham_trydive.jpg",
    "T12": "tour_cham_fundive.jpg",
    "T13": "tour_cham_walkingunder.jpg",
    "T14": "tour_camthanh_eco.jpg",
    "T15": "tour_camthanh_cooking.jpg",
    "T16": "tour_hoian_city_boat.jpg",
    "T17": "tour_hoian_lantern_night.jpg",
    "T18": "tour_bicycle_camthanh.jpg",
    "T19": "tour_traque_cooking.jpg",
    "T20": "tour_lantern_farming.jpg",
    "T21": "tour_cycling_buffalo.jpg",
    "T22": "tour_tranhieu_kimbong.jpg",
    "T23": "tour_ricepaper_kimbong.jpg",
    "T24": "tour_myson_sunrise.jpg",
    "T25": "tour_myson_luxury.jpg",
    "T26": "tour_myson_sunset.jpg",
    "T27": "tour_runggdua_basic.jpg",
    "T28": "tour_runggdua_experience.jpg",
    "T29": "tour_runggdua_allincl.jpg",
    "T30": "tour_hue_citytour.jpg",
    "T31": "tour_bana_fullday.jpg",
    "T32": "tour_bana_dragon.jpg",
    "T33": "tour_danang_bana_full.jpg",
    "T34": "tour_nkhe_nhs_hoian.jpg",
    "T35": "tour_nhs_hoian_lantern.jpg",
    "T36": "tour_nkhe_nhs_cruise.jpg",
    "T37": "tour_nkhe_nhs_myson.jpg",
    "T38": "tour_nhs_morning.jpg",
    "T39": "tour_nhs_sunset.jpg",
    "T40": "tour_monkey_full.jpg",
}

def replace_img_in_card(html, onclick_str, key):
    img_file = img_map[key]
    # Find the tour card div containing this onclick, then replace its img src
    # Pattern: find the card block, replace img src inside it
    # We'll use a simple split approach
    parts = html.split(onclick_str)
    if len(parts) < 2:
        print(f"NOT FOUND: {onclick_str}")
        return html
    
    # The img tag is inside the tour-image-container div in this card
    # It appears AFTER onclick in the card's next 200 chars... 
    # Actually the card div is opened BEFORE onclick, so we need the img after onclick
    after = parts[1]
    # Find first <img src="... 
    img_match = re.search(r'<img\s+src="([^"]+)"', after)
    if not img_match:
        print(f"IMG NOT FOUND after: {onclick_str}")
        return html
    old_src = img_match.group(1)
    new_after = after.replace(img_match.group(0), f'<img src="{img_file}"', 1)
    result = onclick_str.join([parts[0], new_after])
    print(f"[OK] {key}: {old_src} -> {img_file}")
    return result

for onclick_str, key in replacements:
    html = replace_img_in_card(html, onclick_str, key)

with open(r'd:\project\booking\sontra-villa\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nDone! HTML updated.")
