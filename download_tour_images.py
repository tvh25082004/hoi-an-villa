
import urllib.request
import os
import time

SAVE_DIR = r"d:\project\booking\sontra-villa"

# Map: filename -> Unsplash direct image URL (landscape, relevant to tour)
images = {
    # HOI AN COOKING SCHOOL tours
    "tour_cooking_class.jpg":       "https://images.unsplash.com/photo-1604908177453-7462950a6a3b?w=800&q=80",
    "tour_street_food.jpg":         "https://images.unsplash.com/photo-1559410545-0bdcd187e0a6?w=800&q=80",
    "tour_buffalo_cycling.jpg":     "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80",
    "tour_basket_boat_coconut.jpg": "https://images.unsplash.com/photo-1567529692333-de9fd6772897?w=800&q=80",
    "tour_basket_boat_food.jpg":    "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?w=800&q=80",
    "tour_lantern_cooking.jpg":     "https://images.unsplash.com/photo-1528360983277-13d401cdc186?w=800&q=80",

    # CU LAO CHAM tours
    "tour_cham_daily.jpg":          "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=800&q=80",
    "tour_cham_handicraft.jpg":     "https://images.unsplash.com/photo-1519582272560-66a2f43b3a2d?w=800&q=80",
    "tour_cham_homestay.jpg":       "https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?w=800&q=80",
    "tour_cham_snorkeling.jpg":     "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=800&q=80",
    "tour_cham_trydive.jpg":        "https://images.unsplash.com/photo-1682687220509-61b8a906ca19?w=800&q=80",
    "tour_cham_fundive.jpg":        "https://images.unsplash.com/photo-1549880338-65ddcdfd017b?w=800&q=80",
    "tour_cham_walkingunder.jpg":   "https://images.unsplash.com/photo-1560275619-4662e36fa65c?w=800&q=80",

    # HOI AN GREEN TRAVEL - Villages/Eco
    "tour_camthanh_eco.jpg":        "https://images.unsplash.com/photo-1567529692333-de9fd6772897?w=800&q=80",
    "tour_camthanh_cooking.jpg":    "https://images.unsplash.com/photo-1604908177453-7462950a6a3b?w=800&q=80",
    "tour_hoian_city_boat.jpg":     "https://images.unsplash.com/photo-1528360983277-13d401cdc186?w=800&q=80",
    "tour_hoian_lantern_night.jpg": "https://images.unsplash.com/photo-1528360983277-13d401cdc186?w=800&q=80",
    "tour_bicycle_camthanh.jpg":    "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80",
    "tour_traque_cooking.jpg":      "https://images.unsplash.com/photo-1604908177453-7462950a6a3b?w=800&q=80",
    "tour_lantern_farming.jpg":     "https://images.unsplash.com/photo-1519582272560-66a2f43b3a2d?w=800&q=80",
    "tour_cycling_buffalo.jpg":     "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80",
    "tour_tranhieu_kimbong.jpg":    "https://images.unsplash.com/photo-1519582272560-66a2f43b3a2d?w=800&q=80",
    "tour_ricepaper_kimbong.jpg":   "https://images.unsplash.com/photo-1604908177453-7462950a6a3b?w=800&q=80",

    # MY SON
    "tour_myson_sunrise.jpg":       "https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=800&q=80",
    "tour_myson_luxury.jpg":        "https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=800&q=80",
    "tour_myson_sunset.jpg":        "https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=800&q=80",

    # RUNG DUA BAY MAU
    "tour_runggdua_basic.jpg":      "https://images.unsplash.com/photo-1567529692333-de9fd6772897?w=800&q=80",
    "tour_runggdua_experience.jpg": "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?w=800&q=80",
    "tour_runggdua_allincl.jpg":    "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?w=800&q=80",

    # HUE
    "tour_hue_citytour.jpg":        "https://images.unsplash.com/photo-1583417319070-4a69db38a482?w=800&q=80",

    # DA NANG / BA NA HILLS
    "tour_bana_fullday.jpg":        "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80",
    "tour_bana_dragon.jpg":         "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=800&q=80",
    "tour_danang_bana_full.jpg":    "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80",
    "tour_nkhe_nhs_hoian.jpg":      "https://images.unsplash.com/photo-1551524164-687a55dd1126?w=800&q=80",
    "tour_nhs_hoian_lantern.jpg":   "https://images.unsplash.com/photo-1528360983277-13d401cdc186?w=800&q=80",
    "tour_nkhe_nhs_cruise.jpg":     "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=800&q=80",
    "tour_nkhe_nhs_myson.jpg":      "https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=800&q=80",
    "tour_nhs_morning.jpg":         "https://images.unsplash.com/photo-1551524164-687a55dd1126?w=800&q=80",
    "tour_nhs_sunset.jpg":          "https://images.unsplash.com/photo-1551524164-687a55dd1126?w=800&q=80",
    "tour_monkey_full.jpg":         "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80",
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

ok = 0
fail = 0
for fname, url in images.items():
    fpath = os.path.join(SAVE_DIR, fname)
    if os.path.exists(fpath):
        print(f"[SKIP] {fname} already exists")
        ok += 1
        continue
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        with open(fpath, 'wb') as f:
            f.write(data)
        print(f"[OK] {fname} ({len(data)//1024}KB)")
        ok += 1
        time.sleep(0.3)
    except Exception as e:
        print(f"[FAIL] {fname}: {e}")
        fail += 1

print(f"\nDone: {ok} success, {fail} failed")
