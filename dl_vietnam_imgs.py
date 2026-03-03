
import urllib.request, os, time, sys

SAVE_DIR = r"d:\project\booking\sontra-villa"

# Vietnam-specific images from Unsplash with proper Vietnam location queries
images = {
    # HOI AN - Cooking / Food
    "tour_cooking_class.jpg":       "https://images.unsplash.com/photo-1600565193348-f74bd3c7ccdf?w=800&q=85",  # Vietnam cooking class
    "tour_street_food.jpg":         "https://images.unsplash.com/photo-1559134197-3dca50e2c36c?w=800&q=85",  # Hoi An street food
    # HOI AN - Activities
    "tour_buffalo_cycling.jpg":     "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=800&q=85",  # Vietnam rice field cycling
    "tour_basket_boat_coconut.jpg": "https://images.unsplash.com/photo-1568798248271-2c3bef9b40d1?w=800&q=85",  # basket boat Hoi An
    "tour_basket_boat_food.jpg":    "https://images.unsplash.com/photo-1528360983277-13d401cdc186?w=800&q=85",  # Hoi An lanterns / boat
    "tour_lantern_cooking.jpg":     "https://images.unsplash.com/photo-1557800636-894a64c1696f?w=800&q=85",  # Hoi An lanterns
    # CU LAO CHAM - Island
    "tour_cham_daily.jpg":          "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=800&q=85",  # Vietnam island
    "tour_cham_handicraft.jpg":     "https://images.unsplash.com/photo-1519582272560-66a2f43b3a2d?w=800&q=85",  # Vietnam handicraft
    "tour_cham_homestay.jpg":       "https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?w=800&q=85",  # island homestay
    "tour_cham_snorkeling.jpg":     "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=800&q=85",  # Vietnam snorkeling
    "tour_cham_trydive.jpg":        "https://images.unsplash.com/photo-1682687220945-922198770e60?w=800&q=85",  # scuba diving
    "tour_cham_fundive.jpg":        "https://images.unsplash.com/photo-1504214208698-ea1916a2195a?w=800&q=85",  # coral reef dive
    "tour_cham_walkingunder.jpg":   "https://images.unsplash.com/photo-1559560853-2e7d8ccfb2e5?w=800&q=85",  # underwater walking
    # ECO / VILLAGE tours Hoi An
    "tour_camthanh_eco.jpg":        "https://images.unsplash.com/photo-1568798248271-2c3bef9b40d1?w=800&q=85",  # basket boat coconut forest
    "tour_camthanh_cooking.jpg":    "https://images.unsplash.com/photo-1600565193348-f74bd3c7ccdf?w=800&q=85",  # cooking class
    "tour_hoian_city_boat.jpg":     "https://images.unsplash.com/photo-1557800636-894a64c1696f?w=800&q=85",  # Hoi An lanterns river
    "tour_hoian_lantern_night.jpg": "https://images.unsplash.com/photo-1528360983277-13d401cdc186?w=800&q=85",  # Hoi An night lanterns
    "tour_bicycle_camthanh.jpg":    "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=85",  # Vietnam cycling
    "tour_traque_cooking.jpg":      "https://images.unsplash.com/photo-1600565193348-f74bd3c7ccdf?w=800&q=85",  # Vietnam cooking
    "tour_lantern_farming.jpg":     "https://images.unsplash.com/photo-1519582272560-66a2f43b3a2d?w=800&q=85",  # Vietnam farming
    "tour_cycling_buffalo.jpg":     "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?w=800&q=85",  # Vietnam buffalo
    "tour_tranhieu_kimbong.jpg":    "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=800&q=85",  # Vietnam village
    "tour_ricepaper_kimbong.jpg":   "https://images.unsplash.com/photo-1519582272560-66a2f43b3a2d?w=800&q=85",  # Vietnam crafts
    # MY SON - ruins
    "tour_myson_sunrise.jpg":       "https://images.unsplash.com/photo-1538688525198-9b88f6f53126?w=800&q=85",  # My Son Sanctuary
    "tour_myson_luxury.jpg":        "https://images.unsplash.com/photo-1559134197-3dca50e2c36c?w=800&q=85",  # My Son ruins
    "tour_myson_sunset.jpg":        "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&q=85",  # Vietnam sunset landscape
    # RUNG DUA BAY MAU
    "tour_runggdua_basic.jpg":      "https://images.unsplash.com/photo-1568798248271-2c3bef9b40d1?w=800&q=85",
    "tour_runggdua_experience.jpg": "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=800&q=85",
    "tour_runggdua_allincl.jpg":    "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?w=800&q=85",
    # HUE - Imperial city
    "tour_hue_citytour.jpg":        "https://images.unsplash.com/photo-1583417319070-4a69db38a482?w=800&q=85",  # Hue Imperial city
    # DA NANG - Ba Na Hills, Golden Bridge
    "tour_bana_fullday.jpg":        "https://images.unsplash.com/photo-1542332213-31c7bd98044e?w=800&q=85",  # Golden Bridge Ba Na
    "tour_bana_dragon.jpg":         "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=800&q=85",  # Dragon Bridge Da Nang
    "tour_danang_bana_full.jpg":    "https://images.unsplash.com/photo-1542332213-31c7bd98044e?w=800&q=85",  # Ba Na Hills
    "tour_nkhe_nhs_hoian.jpg":      "https://images.unsplash.com/photo-1551524164-687a55dd1126?w=800&q=85",  # Marble Mountains
    "tour_nhs_hoian_lantern.jpg":   "https://images.unsplash.com/photo-1557800636-894a64c1696f?w=800&q=85",  # Hoi An
    "tour_nkhe_nhs_cruise.jpg":     "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=800&q=85",  # Da Nang river night
    "tour_nkhe_nhs_myson.jpg":      "https://images.unsplash.com/photo-1538688525198-9b88f6f53126?w=800&q=85",  # My Son
    "tour_nhs_morning.jpg":         "https://images.unsplash.com/photo-1551524164-687a55dd1126?w=800&q=85",  # Marble Mountains morning
    "tour_nhs_sunset.jpg":          "https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=800&q=85",  # Vietnam sunset
    "tour_monkey_full.jpg":         "https://images.unsplash.com/photo-1542332213-31c7bd98044e?w=800&q=85",  # Da Nang
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
ok = fail = 0
for fname, url in images.items():
    fpath = os.path.join(SAVE_DIR, fname)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
        with open(fpath, 'wb') as f:
            f.write(data)
        sys.stdout.buffer.write(f"[OK] {fname} ({len(data)//1024}KB)\n".encode('utf-8'))
        sys.stdout.buffer.flush()
        ok += 1
        time.sleep(0.2)
    except Exception as e:
        sys.stdout.buffer.write(f"[FAIL] {fname}: {e}\n".encode('utf-8'))
        sys.stdout.buffer.flush()
        fail += 1

sys.stdout.buffer.write(f"\nDone: {ok} OK, {fail} FAIL\n".encode('utf-8'))
