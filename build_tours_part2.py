import json

TOURS = {}

# 21-40
TOURS['t21'] = {
    "title": "Cycling, Water Buffalo Riding – Farming & Fishing", "badge": "🚲 Village", "region": "hoian", "image": "hoian_eco_signature.png",
    "desc_card": "A comprehensive bicycle tour: ride to Cam Thanh village, meet farmers, ride a buffalo, paddle a basket boat to catch crabs, and learn about local history.",
    "highlights": ["🚲 Cycling", "🐃 Buffalo Riding", "🛶 Basket Boat", "🎣 Crab Catching", "👨‍🌾 Farming", "🍽️ Lunch"],
    "itinerary": [
        {"time": "08:30 / 14:00", "title": "Hotel Pickup", "desc": "Cycle from hotel to Cam Thanh."},
        {"time": "09:00 / 14:30", "title": "Meet Farmers", "desc": "Plough the field, plant rice, ride and feed water buffalos."},
        {"time": "10:00 / 15:30", "title": "Fisherman's Home", "desc": "Enjoy coconut jam and tea at a local home."},
        {"time": "10:30 / 16:00", "title": "Coconut Forest", "desc": "Basket boat ride, fishing, catching crabs."},
        {"time": "11:30 / 17:00", "title": "Local Lunch", "desc": "Lunch at local home, learn to make rice milk and Banh Xeo."},
        {"time": "13:00 / 18:30", "title": "Hotel Drop-off", "desc": "Return to your hotel."}
    ],
    "included": [{"ok": True, "text": "Hotel pickup"}, {"ok": True, "text": "Lunch/Dinner"}, {"ok": True, "text": "Guide"}, {"ok": True, "text": "Basket boat & bike"}, {"ok": True, "text": "Entrance tickets"}],
    "meta": [("⏱", "4.5 hours"), ("📍", "Cam Thanh"), ("🐃", "Buffalo")], "notes": "Min 2 guests."
}

TOURS['t22'] = {
    "title": "Tra Nhieu Eco Tour – Kim Bong Rural Village", "badge": "🛶 Eco", "region": "hoian", "image": "hoian_signature.png",
    "desc_card": "Bicycle tour to explore the traditional Kim Bong Carpentry village, see colorful sleep mat weaving, and paddle a basket boat in Tra Nhieu palm forest.",
    "highlights": ["🪚 Kim Bong Woodcraft", "🧶 Mat Weaving", "🚲 Cycling", "🛶 Basket Boat", "🌿 Tra Nhieu Forest", "🍽️ Lunch"],
    "itinerary": [
        {"time": "08:30 / 13:30", "title": "Hotel Pickup", "desc": "Cycle to Kim Bong Carpentry Village."},
        {"time": "09:00 / 14:00", "title": "Kim Bong Village", "desc": "Discover the art of traditional shipbuilding and wood carving."},
        {"time": "09:45 / 14:45", "title": "Mat Weaving", "desc": "Learn how locals weave colorful traditional sleeping mats."},
        {"time": "10:30 / 15:30", "title": "Tra Nhieu Village", "desc": "Cycle through massive rice paddies to Tra Nhieu palm forest."},
        {"time": "11:00 / 16:00", "title": "Basket Boat", "desc": "Paddle a basket boat through the water coconut canals."},
        {"time": "12:00 / 17:00", "title": "Lunch", "desc": "Local lunch."},
        {"time": "13:00 / 18:00", "title": "Hotel Drop-off", "desc": "Return to Hoi An."}
    ],
    "included": [{"ok": True, "text": "Bicycle"}, {"ok": True, "text": "Basket boat"}, {"ok": True, "text": "Guide"}, {"ok": True, "text": "Entrance tickets"}, {"ok": True, "text": "Lunch & water"}],
    "meta": [("⏱", "Afternoon"), ("📍", "Tra Nhieu & Kim Bong"), ("🛶", "Eco")], "notes": ""
}

TOURS['t23'] = {
    "title": "Rice Paper Making & Cooking at Kim Bong", "badge": "🍳 Cooking", "region": "hoian", "image": "hoian_signature.png",
    "desc_card": "Experience traditional handmade rice paper making at Kim Bong village and join a cooking class to prepare 5 traditional Hoi An dishes.",
    "highlights": ["🥞 Rice Paper Making", "👨‍🍳 5-Dish Cooking", "🍆 Grilled Eggplant", "🍜 Cao Lau", "🍌 Caramel Banana", "🍽️ Lunch"],
    "itinerary": [
        {"time": "08:15 / 13:30", "title": "Hotel Pickup", "desc": "Pick up at hotel."},
        {"time": "08:45 / 14:00", "title": "Kim Bong Village", "desc": "Transfer to Kim Bong Carpentry Village."},
        {"time": "09:15 / 14:30", "title": "Rice Paper craft", "desc": "Learn to make traditional handmade rice paper."},
        {"time": "10:15 / 15:30", "title": "2-Hour Cooking Class", "desc": "Cook: Vietnamese Salad, Chicken Cao Lau, Mushroom Banh Xeo, Charcoal Grilled Eggplant, Caramel Banana."},
        {"time": "12:15 / 17:30", "title": "Lunch/Dinner", "desc": "Enjoy your cooked meal."},
        {"time": "13:00 / 18:00", "title": "Hotel Drop-off", "desc": "Return to hotel."}
    ],
    "included": [{"ok": True, "text": "Transport (car/motorcycle)"}, {"ok": True, "text": "Guide & Entrance tickets"}, {"ok": True, "text": "Lunch & cooking class"}],
    "meta": [("⏱", "4.5 hours"), ("📍", "Kim Bong"), ("🍽️", "Cooking")], "notes": "Min 2 guests."
}

TOURS['t24'] = {
    "title": "My Son Sunrise Daily Tour", "badge": "🌅 Sunrise", "region": "hoian", "image": "hoian_signature.png",
    "desc_card": "Beat the crowds and the heat by visiting the My Son Sanctuary at dawn. Explore the 4th-century Hindu temples and enjoy a local breakfast.",
    "highlights": ["🌅 Best Light for Photos", "🏛️ UNESCO World Heritage", "⛩️ Ancient Cham Temples", "🍜 Breakfast Mi Quang", "🌄 Morning Quiet", "📸 Photography"],
    "itinerary": [
        {"time": "05:00-05:20", "title": "Hotel Pickup", "desc": "Pick up at Hoi An hotel."},
        {"time": "06:00", "title": "Arrive at My Son", "desc": "Take electric buggy to the ruins."},
        {"time": "06:15", "title": "My Son Exploration", "desc": "2-hour guided walking tour among the 4th-13th century Cham pa Hindu temple ruins in the cool morning air."},
        {"time": "08:30", "title": "Local Breakfast", "desc": "Enjoy famous Mi Quang noodles for breakfast at a local restaurant."},
        {"time": "09:00", "title": "Return", "desc": "Drive back to Hoi An."},
        {"time": "10:00", "title": "Hotel Drop-off", "desc": "Return to your hotel."}
    ],
    "included": [{"ok": True, "text": "Hotel pickup & drop-off"}, {"ok": True, "text": "Electric buggy inside My Son"}, {"ok": True, "text": "English guide"}, {"ok": True, "text": "My Son entrance ticket"}, {"ok": True, "text": "Breakfast & water"}],
    "meta": [("⏱", "5:30–10:00"), ("📍", "My Son"), ("🌅", "Sunrise")], "notes": "Min 2, Max 10 guests."
}

TOURS['t25'] = { # OLD: my-son
    "title": "My Son Sanctuary Discovery", "badge": "🏛️ History", "region": "hoian", "image": "hoian_signature.png",
    "desc_card": "Journey to the spiritual heart of the Champa Kingdom. Explore ancient Hindu temples nestled in a lush valley with an expert guide.",
    "highlights": ["🏛️ UNESCO Heritage", "🎭 Cham Dance", "⛩️ Hindu Temples", "🥞 Rice Paper Making", "🚣 River Boat Return", "🌾 Countryside Views"],
    "itinerary": [
        {"time": "07:30", "title": "Hotel Pickup", "desc": "Pick up at your hotel."},
        {"time": "09:00", "title": "My Son Sanctuary", "desc": "Explore the majestic Champa Kingdom ruins and enjoy a traditional Cham Apsara dance performance."},
        {"time": "11:15", "title": "Rice Paper Experience", "desc": "Learn to make rice paper at a local home."},
        {"time": "11:45", "title": "Lunch", "desc": "Enjoy lunch at a local restaurant."},
        {"time": "12:30", "title": "Thu Bon River Cruise", "desc": "Return to Hoi An via a scenic wooden boat cruise on the Thu Bon River."},
        {"time": "13:30", "title": "Hotel Drop-off", "desc": "Return to your hotel."}
    ],
    "included": [{"ok": True, "text": "Hotel pickup/drop-off"}, {"ok": True, "text": "Buggy & wooden boat"}, {"ok": True, "text": "Guide"}, {"ok": True, "text": "Entrance tickets"}, {"ok": True, "text": "Lunch & water"}],
    "meta": [("⏱", "7:30–13:30"), ("📍", "Duy Xuyen"), ("🏛️", "Classic")], "notes": "Min 1, Max 12 guests."
}

TOURS['t26'] = {
    "title": "My Son Sunset Tour", "badge": "🌇 Sunset", "region": "hoian", "image": "hoian_signature.png",
    "desc_card": "Visit My Son Sanctuary in the afternoon, catch the traditional Cham dance, and enjoy a breathtaking sunset boat cruise back to Hoi An.",
    "highlights": ["🌅 Sunset Views", "🎭 Cham Dance", "🏛️ Ancient Ruins", "🚣 River Cruise", "🥖 Banh Mi", "📸 Photos"],
    "itinerary": [
        {"time": "13:00", "title": "Hotel Pickup", "desc": "Pick up from hotel."},
        {"time": "15:00", "title": "Explore My Son", "desc": "2-hour tour of the sanctuary's ruins, landscapes, and watch the traditional Cham performance."},
        {"time": "17:00", "title": "Thu Bon River Cruise", "desc": "Board a wooden boat and cruise back toward Hoi An while enjoying the sunset."},
        {"time": "18:00", "title": "Hotel Drop-off", "desc": "Return to hotel."}
    ],
    "included": [{"ok": True, "text": "Hotel pickup/drop-off"}, {"ok": True, "text": "Buggy & wooden boat"}, {"ok": True, "text": "Guide"}, {"ok": True, "text": "Entrance ticket"}, {"ok": True, "text": "Vietnamese Banh Mi"}, {"ok": True, "text": "Water"}],
    "meta": [("⏱", "13:00–18:00"), ("📍", "My Son"), ("🌅", "Sunset")], "notes": "Min 1, Max 12 guests."
}

TOURS['t27'] = {  # OLD: bana-hills
    "title": "Ba Na Hills & Golden Bridge", "badge": "✨ Must See", "region": "danang", "image": "danang_signature_1772543844660.png",
    "desc_card": "Ride the world's longest cable car to the iconic 'Hands of God' bridge. Explore the French Village and enjoy panoramic mountain views.",
    "highlights": ["🚠 Cable Car", "🌉 Golden Bridge", "🇫🇷 French Village", "🎠 Fantasy Park", "🍽️ Buffet Lunch", "🌸 French Gardens"],
    "itinerary": [
        {"time": "07:30", "title": "Hotel Pickup", "desc": "Depart from hotel in Hoi An/Da Nang."},
        {"time": "09:00", "title": "Cable Car", "desc": "Dream Stream Cable Car — longest single-track cable car."},
        {"time": "10:00", "title": "Golden Bridge & Gardens", "desc": "Golden Bridge, Le Jardin D'amour, Linh Ung Pagoda."},
        {"time": "11:30", "title": "French Village", "desc": "Cable car #2 to the French Village, Campanile, Shrine, Carnival show."},
        {"time": "12:30", "title": "Buffet Lunch", "desc": "Lava Train to Moon Castle, enjoy Buffet Lunch."},
        {"time": "14:00", "title": "Fantasy Park", "desc": "Free time for Fantasy Park indoor rides (90+ games)."},
        {"time": "15:00", "title": "Descend", "desc": "Take cable car down."},
        {"time": "16:45", "title": "Hotel Drop-off", "desc": "Return to your hotel."}
    ],
    "included": [{"ok": True, "text": "Hotel pickup (Hoi An/Da Nang)"}, {"ok": True, "text": "Guide"}, {"ok": True, "text": "Cable car round-trip"}, {"ok": True, "text": "Fantasy Park, Golden Bridge, Le Jardin, Funicular tickets"}, {"ok": True, "text": "Buffet Lunch"}],
    "meta": [("⏱", "7:30–17:30"), ("📍", "Ba Na Hills"), ("🚠", "Full Day")], "notes": ""
}

TOURS['t28'] = {
    "title": "Afternoon Ba Na Hills & Dragon Bridge at Night", "badge": "🌌 Night Tour", "region": "danang", "image": "hoian_signature.png",
    "desc_card": "An epic combo: Ba Na Hills Golden Bridge in the afternoon, followed by dinner in Da Nang and the famous Dragon Bridge fire-breathing show at night.",
    "highlights": ["🌉 Golden Bridge sunset", "🚠 Cable Car", "🇫🇷 French Village", "🐉 Dragon Bridge Show", "🔥 Fire & Water Jets", "🍽️ Dinner"],
    "itinerary": [
        {"time": "12:30", "title": "Hotel Pickup", "desc": "Pick up at hotel."},
        {"time": "14:00", "title": "Ba Na Hills", "desc": "Cable car ascent, Golden Bridge, Le Jardin D'amour, French Village."},
        {"time": "15:30", "title": "Moon Kingdom", "desc": "Lava train to Helios Waterfall, Time Gate, Moon Kingdom, and Fantasy Park."},
        {"time": "17:00", "title": "Descend", "desc": "Take cable car back down."},
        {"time": "18:45", "title": "Local Dinner", "desc": "Dinner at a local restaurant in Da Nang."},
        {"time": "19:15", "title": "Dragon Bridge", "desc": "Watch the famous Da Nang Dragon Bridge breath fire and water (Fri, Sat, Sun)."},
        {"time": "20:00", "title": "Hotel Drop-off", "desc": "Return to Hoi An/Da Nang hotel."}
    ],
    "included": [{"ok": True, "text": "Transport 2-ways"}, {"ok": True, "text": "Guide"}, {"ok": True, "text": "Cable car tickets"}, {"ok": True, "text": "Dinner"}, {"ok": True, "text": "All Ba Na entrance fees"}],
    "meta": [("⏱", "12:30–20:00"), ("📍", "Da Nang"), ("🐉", "Night Tour")], "notes": "Dragon bridge fire show typically acts on weekends."
}

TOURS['t29'] = {
    "title": "Da Nang City Sites & Ba Na Hills (Full Day)", "badge": "🚐 Mega Combo", "region": "danang", "image": "hoian_signature.png",
    "desc_card": "The ultimate Da Nang tour: Marble Mountains, Son Tra Peninsula (Monkey Mountain), Ba Na Hills Golden Bridge, and Dragon Bridge at night.",
    "highlights": ["🐵 Monkey Mountain", "⛰️ Marble Mountains", "🌉 Golden Bridge", "🎟️ Fantasy Park", "🐉 Dragon Bridge", "🍜 2 Meals"],
    "itinerary": [
        {"time": "07:30", "title": "Hotel Pickup", "desc": "Pick up at hotel."},
        {"time": "08:30", "title": "Monkey Mountain", "desc": "Visit Linh Ung Pagoda and the giant 67m Lady Buddha statue."},
        {"time": "09:30", "title": "Marble Mountains", "desc": "Explore Huyen Khong Cave, Tang Chon Cave, and Am Phu Cave."},
        {"time": "11:45", "title": "Lunch", "desc": "Mi Quang light lunch at a restaurant."},
        {"time": "13:00", "title": "Ba Na Hills", "desc": "Cable car, Golden Bridge, French Village, Fantasy Park."},
        {"time": "17:00", "title": "Descend", "desc": "Take cable car back down."},
        {"time": "18:30", "title": "Dinner", "desc": "Dinner in Da Nang city."},
        {"time": "19:00", "title": "Dragon Bridge", "desc": "Watch the Dragon Bridge display."},
        {"time": "20:00", "title": "Hotel Drop-off", "desc": "Return to Hoi An."}
    ],
    "included": [{"ok": True, "text": "Transport"}, {"ok": True, "text": "Guide"}, {"ok": True, "text": "Cable car, Marble Mt & Am Phu tickets"}, {"ok": True, "text": "Lunch & Dinner"}],
    "meta": [("⏱", "7:30–20:00"), ("📍", "Da Nang"), ("⛰️", "Mountains")], "notes": ""
}

TOURS['t30'] = {
    "title": "Monkey Mountain, Marble Mountains & Hoi An Night", "badge": "✨ Highlights", "region": "danang", "image": "hoian_signature.png",
    "desc_card": "Afternoon trip from Da Nang to Son Tra Peninsula, Marble Mountains caves, then head to Hoi An Ancient Town for dinner and a flower lantern boat ride.",
    "highlights": ["🐵 Monkey Mountain", "⛰️ Marble Mountains", "🏮 Hoi An Old Town", "🛍️ Night Market", "🍜 Local Dinner", "🌸 Lantern Boat"],
    "itinerary": [
        {"time": "13:30", "title": "Hotel Pickup", "desc": "Pick up at hotel."},
        {"time": "14:30", "title": "Monkey Mountain", "desc": "Visit Linh Ung Pagoda, Lady Buddha statue."},
        {"time": "15:30", "title": "Marble Mountains", "desc": "Explore Tang Chon Cave, Non Nuoc Stone Carving Village."},
        {"time": "17:00", "title": "Hoi An Ancient Town", "desc": "Japanese Bridge, Ancient House, Fukian Assembly Hall."},
        {"time": "18:00", "title": "Hoi An Night Market", "desc": "Stroll Nguyen Hoang night market, lantern street, Hoai River."},
        {"time": "18:30", "title": "Dinner", "desc": "Enjoy Hoi An specialty dinner."},
        {"time": "20:00", "title": "Hotel Drop-off", "desc": "Return to hotel."}
    ],
    "included": [{"ok": True, "text": "Transport"}, {"ok": True, "text": "Guide"}, {"ok": True, "text": "Entrance tickets"}, {"ok": True, "text": "Dinner"}, {"ok": True, "text": "Water"}],
    "meta": [("⏱", "13:30–21:00"), ("📍", "Da Nang -> Hoi An"), ("🏮", "Night")], "notes": ""
}

TOURS['t31'] = {
    "title": "Marble Mountains, Hoi An City & River Boat", "badge": "🛶 Combo", "region": "danang", "image": "hoian_signature.png",
    "desc_card": "Explore the mystical cave temples of Marble Mountains before heading to Hoi An's glowing old town for dinner and a flower lantern release.",
    "highlights": ["⛰️ Marble Caves", "🗿 Stone Carving Village", "🏮 Ancient Town", "🍜 Hoi An Dinner", "🚣 River Boat", "🌸 Flower Lantern"],
    "itinerary": [
        {"time": "13:30", "title": "Hotel Pickup", "desc": "Pick up in Da Nang."},
        {"time": "14:00", "title": "Marble Mountains", "desc": "Explore Huyen Khong/Tang Chon caves and stone carving village."},
        {"time": "15:00", "title": "Hoi An Ancient Town", "desc": "Fukian Assembly Hall, Phung Hung House, Tan Ky, Japanese Bridge."},
        {"time": "17:00", "title": "Dinner", "desc": "Taste Hoi An specialty dishes."},
        {"time": "18:00", "title": "Boat & Flower Lantern", "desc": "Take a boat ride on Hoai River and release a lantern."},
        {"time": "19:30", "title": "Hotel Drop-off", "desc": "Return to Da Nang hotel."}
    ],
    "included": [{"ok": True, "text": "Hotel pickup Da Nang"}, {"ok": True, "text": "Guide & Tickets"}, {"ok": True, "text": "Hoi An Dinner"}, {"ok": True, "text": "River boat & lantern"}],
    "meta": [("⏱", "13:30–19:00"), ("📍", "Danang -> Hoian"), ("🏮", "Romance")], "notes": ""
}

TOURS['t32'] = {
    "title": "Monkey Mountain, Marble Mt, Hell Cave & River Cruise", "badge": "🚢 Cruise", "region": "danang", "image": "hoian_signature.png",
    "desc_card": "Visit the highlights of Da Nang: Lady Buddha, Marble Mountains, the fascinating 'Hell Cave' (Am Phu), ending with a Han River night cruise.",
    "highlights": ["🐵 Monkey Mountain", "⛰️ Hell Cave", "🚢 Han River Cruise", "🌆 Da Nang Night Skyline", "🐉 Dragon Bridge", "🍽️ Dinner"],
    "itinerary": [
        {"time": "14:00", "title": "Hotel Pickup", "desc": "Pick up in Da Nang."},
        {"time": "14:40", "title": "Monkey Mountain", "desc": "Visit Linh Ung Pagoda & Lady Buddha."},
        {"time": "15:40", "title": "Marble Mountains", "desc": "Explore the challenging 'Hell Cave' (Am Phu Cave)."},
        {"time": "17:30", "title": "Dinner", "desc": "Local restaurant in Da Nang."},
        {"time": "19:00", "title": "Han River Cruise", "desc": "Enjoy a night cruise on the Han River, admire the illuminated bridges and skyline."},
        {"time": "21:00", "title": "Dragon Bridge", "desc": "Watch the Dragon Bridge breath fire (weekends only)."},
        {"time": "21:30", "title": "Hotel Drop-off", "desc": "Return to hotel."}
    ],
    "included": [{"ok": True, "text": "Transport (100km)"}, {"ok": True, "text": "Marble Mt & Hell Cave tickets"}, {"ok": True, "text": "Han River Cruise ticket"}, {"ok": True, "text": "Dinner + Drinks"}, {"ok": True, "text": "Guide"}],
    "meta": [("⏱", "14:00–21:15"), ("📍", "Da Nang"), ("🚢", "Night Skyline")], "notes": ""
}


TOURS['t33'] = {
    "title": "Monkey Mountain, Marble Mt & My Son Sanctuary", "badge": "🏺 Heritage", "region": "danang", "image": "hoian_signature.png",
    "desc_card": "A full-day journey spanning Da Nang's natural landmarks and the ancient Champa ruins of My Son, plus a local rice paper making class.",
    "highlights": ["🐵 Monkey Mountain", "⛰️ Marble Caves", "🏛️ My Son UNESCO", "💃 Apsara Dance", "🥞 Rice Paper Making", "🍽️ 2 Meals included"],
    "itinerary": [
        {"time": "07:30", "title": "Hotel Pickup", "desc": "Pick up in Hoi An/Da Nang."},
        {"time": "08:30", "title": "Monkey Mountain", "desc": "Linh Ung Pagoda."},
        {"time": "09:30", "title": "Marble Mountains", "desc": "Explore Huyen Khong, Tang Chon, and Hell Cave."},
        {"time": "12:00", "title": "Lunch", "desc": "Lunch at a restaurant."},
        {"time": "13:00", "title": "Drive to My Son", "desc": "Travel to My Son Sanctuary."},
        {"time": "14:45", "title": "My Son Ruins", "desc": "2-hour tour of Cham culture, Apsara dance performance."},
        {"time": "17:00", "title": "Rice Paper Craft", "desc": "Learn to make rice paper at a local home."},
        {"time": "17:30", "title": "Dinner", "desc": "Dinner cooked by local family."},
        {"time": "18:45", "title": "Hotel Drop-off", "desc": "Return to Da Nang/Hoi An."}
    ],
    "included": [{"ok": True, "text": "Transport (190km)"}, {"ok": True, "text": "Guide"}, {"ok": True, "text": "All entrance tickets"}, {"ok": True, "text": "Lunch & Dinner"}, {"ok": True, "text": "Rice paper class"}],
    "meta": [("⏱", "7:30–18:00"), ("📍", "Da Nang & Duy Xuyen"), ("🏛️", "Full Day")], "notes": ""
}

TOURS['t34'] = {
    "title": "Marble Mountains, Monkey Mt & Hell Cave (Morning)", "badge": "⛰️ Core", "region": "danang", "image": "hoian_signature.png",
    "desc_card": "A half-day morning tour covering Da Nang's top three mystical sites: Lady Buddha, Marble Mountains summit, and the sprawling Hell Cave.",
    "highlights": ["🐵 Lady Buddha 67m", "⛰️ Marble Summit", "🕳️ Hell Cave (Am Phu)", "🍜 Mi Quang Lunch", "📸 Photos", "🏃 Active Trip"],
    "itinerary": [
        {"time": "07:30", "title": "Hotel Pickup", "desc": "Pick up in Da Nang/Hoi An."},
        {"time": "08:30", "title": "Monkey Mountain", "desc": "Linh Ung Pagoda and sweeping ocean views."},
        {"time": "09:30", "title": "Marble Mountains", "desc": "Mountain climbing (optional elevator/cable car). Visit Huyen Khong & Tang Chon caves."},
        {"time": "10:30", "title": "Hell Cave", "desc": "Explore Am Phu Cave with its depictions of the afterlife."},
        {"time": "11:45", "title": "Lunch", "desc": "Enjoy Mi Quang local noodles."},
        {"time": "13:00", "title": "Hotel Drop-off", "desc": "Return to your hotel."}
    ],
    "included": [{"ok": True, "text": "Transport"}, {"ok": True, "text": "Guide"}, {"ok": True, "text": "Entrance tickets"}, {"ok": True, "text": "Lunch (Mi Quang)"}],
    "meta": [("⏱", "7:30–13:00"), ("📍", "Da Nang"), ("⛰️", "Morning")], "notes": ""
}

TOURS['t35'] = {
    "title": "Marble Mountains, Monkey Mt & Hell Cave (Sunset)", "badge": "🌇 Magic", "region": "danang", "image": "danang_signature_1772543844660.png",
    "desc_card": "The afternoon version of Da Nang's core tour — witness the golden sunset light filtering down through the caves of Marble Mountains.",
    "highlights": ["🌅 Golden Sunset Views", "🐵 Monkey Mountain", "🕳️ Hell Cave", "⛰️ Mountain Echoes", "⛩️ Pagodas", "📸 Great Light"],
    "itinerary": [
        {"time": "14:00", "title": "Hotel Pickup", "desc": "Pick up from your Da Nang hotel."},
        {"time": "14:40", "title": "Monkey Mountain", "desc": "Visit Linh Ung Pagoda under beautiful afternoon light."},
        {"time": "15:40", "title": "Marble Mountains", "desc": "Explore caves and panoramic viewpoints."},
        {"time": "16:40", "title": "Hell Cave", "desc": "Descend into Am Phu Cave."},
        {"time": "17:45", "title": "Hotel Drop-off", "desc": "Return to your hotel."}
    ],
    "included": [{"ok": True, "text": "Transport (90km)"}, {"ok": True, "text": "Marble Mt & Am Phu tickets"}, {"ok": True, "text": "English Guide"}, {"ok": True, "text": "Water"}],
    "meta": [("⏱", "14:00–18:15"), ("📍", "Da Nang"), ("🌄", "Sunset")], "notes": ""
}

TOURS['t36'] = {
    "title": "Hue Imperial City Tour via Hai Van Pass", "badge": "👑 Royal", "region": "hue", "image": "hue_signature_1772543822350.png",
    "desc_card": "A majestic full-day journey to the ancient capital. Cross the stunning Hai Van Pass, visit the royal Khai Dinh Tomb, the grand Imperial Citadel, and Thien Mu Pagoda.",
    "highlights": ["⛰️ Hai Van Pass", "👑 Imperial Citadel", "🏺 Khai Dinh Tomb", "⛩️ Thien Mu Pagoda", "🌊 Lap An Lagoon", "🍽️ Royal Cuisine Lunch"],
    "itinerary": [
        {"time": "07:00", "title": "Hotel Pickup", "desc": "Pick up in Hoi An (7:00) or Da Nang (8:00)."},
        {"time": "09:00", "title": "Hai Van Pass & Lang Co", "desc": "Drive over Hai Van Pass for epic views. Photo stop at Lap An Lagoon."},
        {"time": "11:00", "title": "Khai Dinh Tomb", "desc": "Visit the spectacular, mosaic-filled mausoleum of Emperor Khai Dinh."},
        {"time": "12:30", "title": "Lunch", "desc": "Enjoy Hue specialty cuisine at a local restaurant."},
        {"time": "13:30", "title": "Imperial Citadel", "desc": "Explore the vast walled Hue Imperial City (Dai Noi)."},
        {"time": "15:00", "title": "Thien Mu Pagoda", "desc": "Visit the oldest and most iconic pagoda in Hue on the Perfume River."},
        {"time": "16:00", "title": "Return Journey", "desc": "Drive back to Da Nang (18:00) / Hoi An (19:00)."}
    ],
    "included": [{"ok": True, "text": "Transport"}, {"ok": True, "text": "All Entrance tickets (~$25 value)"}, {"ok": True, "text": "Hue Specialty Lunch"}, {"ok": True, "text": "Guide"}],
    "meta": [("⏱", "7:00–19:00"), ("📍", "Hue City"), ("👑", "Full Day")], "notes": ""
}

TOURS['t37'] = {
    "title": "The Ultimate Full Day: Danang + Hoi An + Forests", "badge": "💎 Mega", "region": "danang", "image": "hoian_signature.png",
    "desc_card": "Monkey Mtn, Marble Mountains, Hell Cave, Cam Thanh Coconut Forest, Hoi An Ancient Town walking, and Lantern Boat — literally everything in one day!",
    "highlights": ["⛰️ Marble Mountains", "🐵 Monkey Mountain", "🛶 Basket Boat Ride", "🏮 Hoi An Ancient Town", "🌸 Lantern Boat Ride", "🍽️ Local Meals"],
    "itinerary": [
        {"time": "08:00", "title": "Hotel Pickup", "desc": "Depart for Da Nang landmarks."},
        {"time": "09:00", "title": "Monkey Mountain", "desc": "Linh Ung Pagoda."},
        {"time": "10:00", "title": "Marble Mountains", "desc": "Caves and Hell Cave (Am Phu)."},
        {"time": "12:00", "title": "Lunch", "desc": "Enjoy lunch in Da Nang or Hoi An."},
        {"time": "14:00", "title": "Cam Thanh Village", "desc": "Basket boat ride in the water coconut forest."},
        {"time": "16:00", "title": "Hoi An Old Town", "desc": "Walking tour of ancient sites."},
        {"time": "18:00", "title": "Dinner & River", "desc": "Dinner followed by lantern boat ride on Hoai River."},
        {"time": "20:30", "title": "Hotel Drop-off", "desc": "Return to your hotel."}
    ],
    "included": [{"ok": True, "text": "Transport"}, {"ok": True, "text": "All Entrance tickets"}, {"ok": True, "text": "Basket boat & Lantern boat"}, {"ok": True, "text": "Guide & Meals"}],
    "meta": [("⏱", "8:00–20:30"), ("📍", "Multiple"), ("💥", "Action Packed")], "notes": ""
}

TOURS['t38'] = {
    "title": "Bay Mau Coconut Forest: Basic Tour", "badge": "🛶 Basic", "region": "hoian", "image": "hoian_signature.png",
    "desc_card": "A simple and budget-friendly basket boat ride through the Bay Mau coconut forest. Ride on the water and enjoy the greenery.",
    "highlights": ["🛶 Basket Boat", "🌿 Eco Forest", "💸 Budget Friendly", "📸 Photos"],
    "itinerary": [
        {"time": "Flexible", "title": "Arrival", "desc": "Check-in at the Bay Mau Coconut Forest dock."},
        {"time": "+15m", "title": "Basket Boat Ride", "desc": "Enjoy a peaceful ride under the canopy of water coconuts."},
        {"time": "+1h 15m", "title": "End of Ride", "desc": "Return to the pier."}
    ],
    "included": [{"ok": True, "text": "Basket boat ticket"}, {"ok": True, "text": "Local boatman"}],
    "meta": [("⏱", "1 hour"), ("📍", "Cam Thanh"), ("🛶", "Ride Only")], "notes": "Transport to the dock not included."
}

TOURS['t39'] = {
    "title": "Bay Mau Coconut Forest: Experience + Spinning", "badge": "🎡 Fun", "region": "hoian", "image": "hoian_signature.png",
    "desc_card": "The classic Bay Mau experience featuring the thrilling basket boat spinning dance, local crab catching, and fishing net demonstrations.",
    "highlights": ["🛶 Basket Boat", "🎡 Boat Spinning Show", "🦀 Crab Catching", "🎣 Net Casting", "🎶 Music"],
    "itinerary": [
        {"time": "Flexible", "title": "Arrival", "desc": "Welcome at Bay Mau Coconut Forest."},
        {"time": "+15m", "title": "Explore Forest", "desc": "Paddle deep into the water coconut channels."},
        {"time": "+45m", "title": "Spinning & Fishing", "desc": "Watch the famous boat spinning, participate in crab catching and net casting."},
        {"time": "+1h 30m", "title": "End", "desc": "Return to shore."}
    ],
    "included": [{"ok": True, "text": "Basket boat ticket"}, {"ok": True, "text": "Spinning experience"}, {"ok": True, "text": "Fishing tools"}],
    "meta": [("⏱", "1.5 hours"), ("📍", "Cam Thanh"), ("🎡", "Spinning")], "notes": "Transport to the dock not included."
}

TOURS['t40'] = {
    "title": "Bay Mau Coconut Forest: Full Package & Dining", "badge": "🍽️ Full", "region": "hoian", "image": "hoian_signature.png",
    "desc_card": "The premium Bay Mau package: hotel pickup, the full spinning basket boat and crab catching experience, followed by a delicious local meal at a riverside restaurant.",
    "highlights": ["🚐 Transport Included", "🛶 Basket Boat Ride", "🎡 Spinning Show", "🦀 Crab Catching", "🍽️ Riverside Meal", "📸 Photos"],
    "itinerary": [
        {"time": "09:00 / 14:00", "title": "Hotel Pickup", "desc": "Pick up by car from Hoi An hotel."},
        {"time": "09:30 / 14:30", "title": "Basket Boat Experience", "desc": "Spinning boats, fishing nets, and crab catching in the coconut forest."},
        {"time": "11:00 / 16:00", "title": "Riverside Lunch/Dinner", "desc": "Enjoy an authentic local meal by the river."},
        {"time": "12:30 / 17:30", "title": "Hotel Drop-off", "desc": "Return to your hotel."}
    ],
    "included": [{"ok": True, "text": "2-way Transport"}, {"ok": True, "text": "Basket boat & activities"}, {"ok": True, "text": "Full meal"}, {"ok": True, "text": "Water"}],
    "meta": [("⏱", "3.5 hours"), ("📍", "Cam Thanh"), ("🍽️", "Dining")], "notes": ""
}

with open(r'd:\project\booking\tours_part2.json', 'w', encoding='utf-8') as f:
    json.dump(TOURS, f, ensure_ascii=False, indent=2)

print("Saved tours_part2.json")
