"""
COMPLETE TOUR SECTION REWRITE
Replace tour-view HTML and TOUR_DATA entirely based on PDF.
31 tours total: 6 Cooking School (hoian), 13 Green Travel Cham+Hoian (hoian), 
3 My Son (hoian), 3 Rung Dua (hoian), 1 Hue (hue), 9 Da Nang/Ba Na (danang), 
1 Combined (danang)
"""

# ─────────────────────────────────────────────────────────────────────────────
# PART 1: All 31 tour card definitions  
# Each: (id, region, badge, img, title, desc, tags)
# ─────────────────────────────────────────────────────────────────────────────
TOURS = [
  # ── COOKING SCHOOL (hoian) ─────────────────────────────────────────────────
  ("t01","hoian","🍳 Culinary","tour_cooking_class.jpg",
   "Market Tour, Basket Boat &amp; Cooking Class",
   "Experience rural Hoi An life: morning market, coconut forest basket boat ride, and 1.5-hr cooking class with a local chef.",
   [("⏱","5 hours"),("📍","Cam Thanh"),("🍳","Cooking")]),

  ("t02","hoian","🥘 Street Food","tour_street_food.jpg",
   "Sidewalk Food Tour of Hoi An",
   "Taste 9 signature Hoi An dishes at the locals' favorite spots with an English-speaking guide. Max 6 guests.",
   [("⏱","3–4 hours"),("📍","Old Town"),("🍜","9 Dishes")]),

  ("t03","hoian","🐃 Eco","tour_buffalo_cycling.jpg",
   "Buffalo Riding, Basket Boat &amp; Cycling",
   "Cycle through rice paddies, ride a water buffalo, paddle basket boats, and enjoy a traditional local lunch.",
   [("⏱","5 hours"),("📍","Eco Village"),("🚲","Cycling")]),

  ("t04","hoian","🛶 Fun","tour_basket_boat_coconut.jpg",
   "Basket Boat Ride &amp; Coconut Tour",
   "Spin bamboo basket boats through the water coconut canals. Karaoke, crab catching, folk music — fun for all ages!",
   [("⏱","1 hour"),("📍","Coconut Forest"),("🦀","Crab Catching")]),

  ("t05","hoian","🍲 Combo","tour_basket_boat_food.jpg",
   "Basket Boat Ride &amp; Vietnamese Food",
   "Combine a basket boat ride in the historic coconut forest with a traditional Vietnamese meal at a local restaurant.",
   [("⏱","2 hours"),("📍","Coconut Forest"),("🍽️","Lunch Included")]),

  ("t06","hoian","🏮 Ultimate","tour_lantern_cooking.jpg",
   "Lantern Making, Market, Cooking &amp; Basket Boat",
   "The ultimate Hoi An experience: handmade lantern workshop, market visit, cooking class, and basket boat — all in one!",
   [("⏱","4 hours"),("📍","Old Town + Forest"),("🎨","Craft + Cook")]),

  # ── CU LAO CHAM (hoian) ───────────────────────────────────────────────────
  ("t07","hoian","⭐ POPULAR","tour_cham_daily.jpg",
   "Cham Island Daily Tour",
   "Full-day on Cham Island UNESCO Biosphere Reserve: Bai Lang village, coral snorkeling at Bai Xep, and seafood BBQ lunch.",
   [("⏱","Full Day"),("📍","Cham Island"),("🤿","Snorkeling")]),

  ("t08","hoian","🧶 Heritage","tour_cham_handicraft.jpg",
   "Cham Island Handicraft Tour",
   "Discover UNESCO-recognized traditional crafts: rattan hammock weaving, fishing net making, Banh It La Gai cake.",
   [("⏱","8:00–14:00"),("📍","Cham Island"),("🎨","Handicraft")]),

  ("t09","hoian","🏕️ Overnight","tour_cham_homestay.jpg",
   "Cham Island 2 Days 1 Night (Homestay)",
   "Stay overnight in a local island homestay. Two snorkeling sessions, island exploration, and authentic local dinners.",
   [("⏱","2D 1N"),("📍","Cham Island"),("🏕️","Homestay")]),

  ("t10","hoian","⭐ POPULAR","tour_cham_snorkeling.jpg",
   "Cham Island Snorkeling Tour",
   "Advanced snorkeling at 2 premium coral reef spots in Cham Island Marine Park. Includes Vietnamese lunch and beach time.",
   [("⏱","7:30–15:30"),("📍","Cham Island"),("🤿","2 Spots")]),

  ("t11","hoian","🌊 Try Dive","tour_cham_trydive.jpg",
   "Cú Lao Chàm Try Dive (Beginners)",
   "Scuba dive for the first time — no certification needed. 1-on-1 instructor, max depth 6–12m. Colorful coral gardens.",
   [("⏱","8:00–16:00"),("📍","Cham Island"),("🎓","No License Needed")]),

  ("t12","hoian","🎓 PADI","tour_cham_fundive.jpg",
   "Cú Lao Chàm Fun Dive (Certified)",
   "For PADI certified divers. Explore rich marine life — nudibranchs, seahorses, lionfish, reef sharks at 10–25m depth.",
   [("⏱","8:00–16:00"),("📍","Cham Island"),("🦈","10–25m Deep")]),

  ("t13","hoian","🪖 Seawalker","tour_cham_walkingunder.jpg",
   "Walking Underwater at Cham Island",
   "Walk on the ocean floor with an air-pumped helmet — no swimming skills needed. See fish and coral up close!",
   [("⏱","7:30–14:00"),("📍","Cham Island"),("🪸","No Swimming Needed")]),

  # ── GREEN TRAVEL: HOI AN & SURROUNDINGS ───────────────────────────────────
  ("t14","hoian","🌿 Eco","tour_camthanh_eco.jpg",
   "Cam Thanh Eco Water Coconut Village",
   "Explore Cam Thanh Village ecosystem — bamboo basket boat, fishing, and peaceful canal exploration under coconut palms.",
   [("⏱","2.5 hours"),("📍","Cam Thanh"),("🛶","Basket Boat")]),

  ("t15","hoian","🍳 Cooking","tour_camthanh_cooking.jpg",
   "Cam Thanh Cooking Tour",
   "Market visit, basket boat ride in Cam Thanh, and cook 5 traditional Hoi An dishes: Spring Rolls, Banh Xeo, Pho, and more.",
   [("⏱","4.5 hours"),("📍","Cam Thanh"),("🍽️","5 Dishes")]),

  ("t16","hoian","🏮 Evening","tour_hoian_city_boat.jpg",
   "Hoi An City Tour – Boat &amp; Flower Lantern",
   "Explore the Ancient Town, Japanese Bridge, Fukian Hall, then enjoy a romantic flower lantern boat ride on the Hoai River.",
   [("⏱","14:30–18:30"),("📍","Old Town"),("🚣","River Boat")]),

  ("t17","hoian","🌃 Combo","tour_hoian_lantern_night.jpg",
   "Cam Thanh Coconut – Hoi An City – Flower Lantern",
   "The complete experience: water coconut forest, Ancient Town walking tour, dinner, and evening flower lantern boat ride.",
   [("⏱","12:00–19:30"),("📍","Cam Thanh + Old Town"),("🌸","Flower Lantern")]),

  ("t18","hoian","🚲 Cycling","tour_bicycle_camthanh.jpg",
   "Bicycle Tour: Cam Thanh &amp; Tra Que",
   "Cycle through Hoi An countryside — Cam Thanh coconut forest and Tra Que organic village. Basket boat + cooking class.",
   [("⏱","5.5 hours"),("📍","Cam Thanh + Tra Que"),("🌱","Farming + Cooking")]),

  ("t19","hoian","🌱 Farm-to-Table","tour_traque_cooking.jpg",
   "Tra Que Cooking Class Tour",
   "Cooking class at Tra Que Organic Village — market visit, herb garden farming, traditional foot massage, cook 4 dishes.",
   [("⏱","4.5 hours"),("📍","Tra Que Village"),("💆","Foot Massage")]),

  ("t20","hoian","🏮 Crafts","tour_lantern_farming.jpg",
   "Lantern Making &amp; Farming at Tra Que Village",
   "Cycle through rice paddies, farm with locals at Tra Que, learn traditional Hoi An lantern making — and take your lantern home!",
   [("⏱","5.5 hours"),("📍","Tra Que Village"),("🎁","Take Home Lantern")]),

  ("t21","hoian","🐃 Adventure","tour_cycling_buffalo.jpg",
   "Cycling, Buffalo Riding – Farming &amp; Fishing",
   "Complete countryside tour — buffalo riding, traditional farming, basket boat crab catching, local home, and war history.",
   [("⏱","4.5 hours"),("📍","Cam Thanh"),("🦀","Crab Catching")]),

  ("t22","hoian","🎨 Heritage","tour_tranhieu_kimbong.jpg",
   "Tra Nhieu Eco Tour – Kim Bong Rural Village",
   "Cycling tour to Kim Bong woodworking village — traditional boat building, colorful mat weaving, basket boat at Tra Nhieu.",
   [("⏱","4.5 hours"),("📍","Kim Bong Village"),("🪵","Woodworking")]),

  ("t23","hoian","🥟 Cooking","tour_ricepaper_kimbong.jpg",
   "Rice Paper Noodle Making &amp; Cooking – Kim Bong",
   "Handmade rice paper at Kim Bong Village, then a 2-hour cooking class: 5 Vietnamese dishes including Cao Lau &amp; Grilled Fish.",
   [("⏱","4.5 hours"),("📍","Kim Bong Village"),("🍜","5 Dishes")]),

  # ── MY SON (hoian) ────────────────────────────────────────────────────────
  ("t24","hoian","🌅 Sunrise","tour_myson_sunrise.jpg",
   "My Son Sunrise Daily Tour",
   "Visit My Son UNESCO Sanctuary at sunrise — explore 7th–13th century Champa towers with an English guide. Breakfast included.",
   [("⏱","5:30–10:00"),("📍","My Son"),("🏛️","UNESCO")]),

  ("t25","hoian","✨ Luxury","tour_myson_luxury.jpg",
   "My Son Sanctuary Luxury Tour",
   "Premium My Son experience: sanctuary visit, Cham dance show, rice paper making, and wooden boat cruise down Thu Bon River.",
   [("⏱","7:30–13:30"),("📍","My Son"),("⛵","River Cruise")]),

  ("t26","hoian","🌇 Sunset","tour_myson_sunset.jpg",
   "My Son Sunset Tour",
   "Afternoon visit to My Son — Cham traditional dance, then scenic sunset boat cruise down Thu Bon River to Hoi An.",
   [("⏱","13:00–18:00"),("📍","My Son"),("🌅","Sunset Cruise")]),

  # ── RUNG DUA BAY MAU (hoian) ──────────────────────────────────────────────
  ("t27","hoian","🌿 Nature","tour_runggdua_basic.jpg",
   "Rung Dua Bay Mau – Basic Basket Boat Tour",
   "Classic basket boat experience in the stunning Bay Mau Water Coconut Forest. Perfect for families and all ages.",
   [("⏱","Flexible"),("📍","Bay Mau Forest"),("🛶","Basket Boat")]),

  ("t28","hoian","🎭 Experience","tour_runggdua_experience.jpg",
   "Rung Dua Bay Mau – Experience + Spinning",
   "Upgrade to spinning basket boat, folk fishing performance, crab catching, and local cultural shows by residents.",
   [("⏱","Flexible"),("📍","Bay Mau Forest"),("🎡","Spinning + Shows")]),

  ("t29","hoian","🍽️ All-Inclusive","tour_runggdua_allincl.jpg",
   "Rung Dua Bay Mau – All Inclusive Package",
   "The complete Bay Mau experience: all activities + a delicious set menu local meal with traditional dishes.",
   [("⏱","Flexible"),("📍","Bay Mau Forest"),("🍽️","Meal Included")]),

  # ── HUE ──────────────────────────────────────────────────────────────────
  ("t30","hue","🏯 Imperial","tour_hue_citytour.jpg",
   "Hue Imperial City Full Day Tour",
   "Full-day trip to ancient imperial Hue: cross Hai Van Pass, visit Khai Dinh Tomb, the Imperial Citadel, and Thien Mu Pagoda.",
   [("⏱","7:00–19:00"),("📍","Hue City"),("🏯","UNESCO")]),

  # ── DA NANG / BA NA HILLS ─────────────────────────────────────────────────
  ("t31","danang","🌉 Must See","tour_bana_fullday.jpg",
   "Ba Na Hills Full Day Tour",
   "Ride the world's longest cable car, cross the iconic Golden Bridge, explore French Village, Fantasy Park buffet lunch.",
   [("⏱","7:30–17:30"),("📍","Ba Na Hills"),("🚠","Cable Car")]),

  ("t32","danang","🌙 Evening","tour_bana_dragon.jpg",
   "Afternoon Ba Na Hills + Dragon Bridge at Night",
   "Ba Na Hills in the afternoon, then witness the spectacular Dragon Bridge fire &amp; water show in Da Nang city at night.",
   [("⏱","11:45–20:00"),("📍","Ba Na + Da Nang"),("🐉","Dragon Bridge")]),

  ("t33","danang","🌆 Full Day","tour_danang_bana_full.jpg",
   "Da Nang City + Ba Na Hills + Dragon Bridge (Full Day)",
   "Complete Da Nang day: Monkey Mountain, Marble Mountains, Ba Na Hills, Golden Bridge, then Dragon Bridge at night.",
   [("⏱","7:30–20:00"),("📍","Da Nang + Ba Na"),("🌉","Full Day")]),

  ("t34","danang","⛰️ Sightseeing","tour_nkhe_nhs_hoian.jpg",
   "Monkey Mountain – Marble Mountains – Hoi An Night",
   "Linh Ung Pagoda on Son Tra, Marble Mountains caves, then Hoi An Ancient Town by night with flower lantern release.",
   [("⏱","13:30–21:00"),("📍","Da Nang + Hoi An"),("🌸","Lantern Release")]),

  ("t35","danang","🏮 Cultural","tour_nhs_hoian_lantern.jpg",
   "Marble Mountains – Hoi An City – Boat &amp; Lantern",
   "Marble Mountains, Hoi An Ancient Town afternoon walk, local dinner, then flower lantern boat ride on the Hoai River.",
   [("⏱","13:30–19:00"),("📍","Da Nang + Hoi An"),("🚣","River Boat")]),

  ("t36","danang","🌃 Cruise","tour_nkhe_nhs_cruise.jpg",
   "Monkey Mountain – Marble Mountains – Da Nang Cruise",
   "Linh Ung Pagoda, Marble Mountains, Am Phu Cave, dinner, then Han River night cruise with Dragon Bridge fire show.",
   [("⏱","14:00–21:15"),("📍","Da Nang"),("⛵","Night Cruise")]),

  ("t37","danang","🏰 UNESCO","tour_nkhe_nhs_myson.jpg",
   "Monkey Mountain – Marble Mountains – My Son (Full Day)",
   "Full-day combining Da Nang's best: Linh Ung Pagoda, Marble Mountains, and My Son UNESCO Sanctuary.",
   [("⏱","7:30–18:00"),("📍","Da Nang + My Son"),("🏛️","UNESCO")]),

  ("t38","danang","🌄 Morning","tour_nhs_morning.jpg",
   "Marble Mountains – Monkey Mountain – Am Phu Cave (Morning)",
   "Half-day Da Nang highlights: Linh Ung Pagoda on Son Tra, Marble Mountains, Am Phu Cave, and Mi Quang lunch.",
   [("⏱","7:30–13:00"),("📍","Da Nang"),("🌄","Half Day")]),

  ("t39","danang","🌇 Sunset","tour_nhs_sunset.jpg",
   "Marble Mountains – Monkey Mountain – Am Phu Cave (Sunset)",
   "Afternoon version of the Da Nang highlights tour — golden sunset light over the mountain towers and caves.",
   [("⏱","14:00–18:15"),("📍","Da Nang"),("🌅","Sunset Tour")]),

  ("t40","danang","🗺️ Ultimate","tour_monkey_full.jpg",
   "Monkey Mountain – Marble Mountains – Cam Thanh – Hoi An (Full Day)",
   "The ultimate day: Son Tra, Marble Mountains, basket boat at Cam Thanh, Hoi An Ancient Town, dinner &amp; flower lantern release.",
   [("⏱","8:00–20:30"),("📍","Da Nang + Hoi An"),("🏮","Full Experience")]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PART 2: Generate tour-view HTML
# ─────────────────────────────────────────────────────────────────────────────
def make_tag(emoji, text):
    return f'<span class="rec-tag"><span>{emoji}</span> {text}</span>'

def make_card(tid, region, badge, img, title, desc, tags):
    tags_html = "".join(make_tag(e,t) for e,t in tags)
    return f'''        <div class="tour-card" data-region="{region}" onclick="openTourModal('{tid}')">
          <div class="tour-image-container">
            <img src="{img}" alt="{title}" loading="lazy" onerror="this.src='tour_hoian_city_boat.jpg'">
            <span class="rec-badge">{badge}</span>
          </div>
          <div class="tour-info">
            <h3 class="rec-title">{title}</h3>
            <p class="rec-desc">{desc}</p>
            <div class="rec-tags">{tags_html}</div>
            <p class="rec-cta">Tap for full details →</p>
          </div>
        </div>'''

cards_html = "\n".join(make_card(*t) for t in TOURS)

TOUR_VIEW_HTML = f'''    <!-- TOUR VIEW -->
    <div id="tour-view" class="fade-in" style="display: none;">
      <button class="back-btn" onclick="toggleView('main')">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 5l-7 7 7 7"/></svg>
        Go Back
      </button>

      <div class="profile">
        <h2 class="title" style="margin-top:20px;">🗺️ Discovery Tours 2026</h2>
        <p class="subtitle">Hand-picked authentic experiences in &amp; around Hoi An</p>
      </div>

      <!-- Region Filter Tabs -->
      <div class="rec-tabs" style="margin:0 16px 20px;">
        <button class="rec-tab active" onclick="filterTour('all',this)">🌏 ALL</button>
        <button class="rec-tab" onclick="filterTour('hoian',this)">🏮 Hoi An</button>
        <button class="rec-tab" onclick="filterTour('hue',this)">🏯 Hue</button>
        <button class="rec-tab" onclick="filterTour('danang',this)">🌉 Da Nang</button>
      </div>

      <!-- Tour Cards -->
      <div id="tour-list-container">
{cards_html}
      </div>
    </div>
    <!-- END TOUR VIEW -->'''

print("Generated tour-view HTML:")
print(f"  Tours: {len(TOURS)}")
print(f"  HTML length: {len(TOUR_VIEW_HTML)} chars")

# Save for inspection
with open(r'd:\project\booking\tour_view_new.html', 'w', encoding='utf-8') as f:
    f.write(TOUR_VIEW_HTML)
print("Saved to tour_view_new.html")
