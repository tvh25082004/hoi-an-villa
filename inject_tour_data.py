#!/usr/bin/env python3
"""Generate TOUR_DATA JS entries for all 26 new PDF tours and inject into index.html"""
import re

# All 26 new tours from PDF (tours 1-20 from PDF = Hoi An region, 21-29=Da Nang, 30=Hue, 31=Combined)
# The existing 5 (cham-snorkeling, basket-boat, bana-hills, hoian-city, my-son) stay as-is.
# We map each fake card ID to a real PDF tour.

TOUR_DATA_ENTRIES = """
    'marble-mountains': {
      title: 'Market Tour, Basket Boat & Cooking Class',
      badge: '🍳 Culinary',
      image: 'tour_cooking_class.jpg',
      description: 'Experience rural Hoi An life and Vietnamese cuisine. Visit the morning market, paddle a basket boat through the water coconut forest, and join a 1.5-hour cooking class with a local chef.',
      highlights: ['🛒 Market Tour', '🛶 Basket Boat Ride', '👨‍🍳 Cooking Class', '🌿 Cam Thanh Village', '🍜 Vietnamese Dishes', '📸 Photo Ops'],
      itinerary: [
        { time: '08:00', title: 'Hotel Pickup', desc: 'Pick up at your hotel in Hoi An.' },
        { time: '08:30', title: 'Hoi An Market Visit', desc: 'Explore the local market — learn about ingredients for Vietnamese cooking.' },
        { time: '09:30', title: 'Transfer to Cam Thanh', desc: 'Drive to Cam Thanh Water Coconut Village by van.' },
        { time: '10:00', title: 'Basket Boat Ride', desc: 'Paddle bamboo basket boats through the lush water coconut forest.' },
        { time: '11:00', title: 'Cooking Class (1.5 hrs)', desc: 'Cook Banh Xeo, Pho Bo, Fresh Spring Rolls, and Vietnamese Tea with a local chef.' },
        { time: '12:30', title: 'Enjoy Your Meal', desc: 'Taste the dishes you cooked in a beautiful garden setting.' },
        { time: '13:30', title: 'Hotel Drop-off', desc: 'Return to your hotel.' },
      ],
      included: [
        { ok: true, text: 'Hotel pickup & drop-off' },
        { ok: true, text: 'Basket boat ride' },
        { ok: true, text: 'Cooking class with chef' },
        { ok: true, text: 'All ingredients' },
        { ok: true, text: 'Bottled water' },
        { ok: false, text: 'Drinks & personal expenses' },
      ],
      notes: '🍳 Duration: 5 hours. Morning (8:00–13:30) or Afternoon (13:00–18:00). By Hoi An Cooking School.',
    },
    'hue-imperial': {
      title: 'Sidewalk Food Tour of Hoi An',
      badge: '🥘 Street Food',
      image: 'tour_street_food.jpg',
      description: 'Discover Hoi An street food with an English-speaking guide — taste 9 signature dishes at the most beloved local spots. Small group (max 6).',
      highlights: ['🍜 9 Local Dishes', '☕ Vietnamese Coffee', '🥖 Banh Mi', '🍲 Cao Lau', '🦆 Balut Egg', '🚶 Walking Tour'],
      itinerary: [
        { time: '07:00', title: 'Hotel Pickup', desc: 'Meet at your hotel or a designated point.' },
        { time: '07:15', title: 'Walking Through Old Town', desc: 'Stroll through the atmospheric streets of Hoi An.' },
        { time: '07:30', title: '9 Dishes Tasting', desc: 'Vietnamese Coffee, Banh Mi, Banh Uot, Mi Quang/Cao Lau, Banh Xeo, Grilled Meat, Chicken Rice, Sugarcane Juice, Balut Egg.' },
        { time: '09:30', title: 'History & Culture', desc: 'Learn about Hoi An history and food culture along the way.' },
        { time: '10:00', title: 'Hotel Drop-off', desc: 'Return to your hotel.' },
      ],
      included: [
        { ok: true, text: 'Transportation' },
        { ok: true, text: '9 dishes & drinks' },
        { ok: true, text: 'English-speaking guide' },
        { ok: true, text: 'Insurance' },
        { ok: true, text: 'Hotel pickup & drop-off' },
        { ok: false, text: 'Personal expenses' },
      ],
      notes: '🍜 3–4 hours. Morning (7:00–10:00) or Afternoon (15:30–18:30). Max 6 guests per group.',
    },
    'cooking-class': {
      title: 'Buffalo Riding, Basket Boat & Cycling',
      badge: '🐃 Eco',
      image: 'tour_buffalo_cycling.jpg',
      description: 'Explore rural Hoi An by bicycle — ride through rice paddies, ride a water buffalo, paddle basket boats, and enjoy a traditional local lunch.',
      highlights: ['🚲 Cycling', '🐃 Buffalo Riding', '🛶 Basket Boat', '🌾 Rice Paddies', '🍽️ Local Lunch', '📸 Countryside Views'],
      itinerary: [
        { time: '08:15', title: 'Hotel Pickup by Bicycle', desc: 'Cycle from your hotel through the countryside.' },
        { time: '09:00', title: 'Eco Village', desc: 'Visit the eco village — see rice fields, ride a water buffalo.' },
        { time: '10:00', title: 'Basket Boat in Coconut Forest', desc: 'Paddle basket boats through the water coconut canals.' },
        { time: '11:00', title: 'Traditional Lunch', desc: 'Deep Fried Spring Rolls, Steamed Red Snapper, Banana Salad, Stir Fried Morning Glory, Fruit Dessert.' },
        { time: '12:30', title: 'Hotel Drop-off', desc: 'Return to your hotel by bicycle.' },
      ],
      included: [
        { ok: true, text: 'Bicycle & helmet' },
        { ok: true, text: 'Buffalo riding' },
        { ok: true, text: 'Basket boat ride' },
        { ok: true, text: 'Traditional lunch (5 dishes)' },
        { ok: true, text: 'English-speaking guide' },
        { ok: false, text: 'Drinks & tips' },
      ],
      notes: '🐃 5 hours. Morning (8:15–12:30) or Afternoon (13:15–18:00). By Hoi An Cooking School.',
    },
    'hai-van-pass': {
      title: 'Basket Boat Ride & Coconut Tour',
      badge: '🛶 Fun',
      image: 'tour_basket_boat_coconut.jpg',
      description: 'Experience bamboo basket boats on the water coconut canals. Enjoy spinning boats, folk singing, fishing nets, and crab catching. Fun for all ages!',
      highlights: ['🛶 Basket Boat', '🎶 Folk Music', '🦀 Crab Catching', '🎡 Boat Spinning', '📸 Great Photos', '👨‍👩‍👧 Family Friendly'],
      itinerary: [
        { time: 'Flexible', title: 'Hotel Pickup', desc: 'Driver picks you up at your hotel (available 8:00–16:00 daily).' },
        { time: '+15min', title: 'Welcome at Dragon Restaurant', desc: 'Greeted with welcome drink at the coconut forest entrance.' },
        { time: '+30min', title: '1 Hour Basket Boat Ride', desc: 'Spinning basket boats, karaoke on water, fishing nets, crab catching, folk music performance.' },
        { time: '+90min', title: 'End of Tour', desc: 'Return to the dock and transfer back to hotel.' },
      ],
      included: [
        { ok: true, text: 'Hotel pickup & drop-off' },
        { ok: true, text: '1 hour basket boat ride' },
        { ok: true, text: 'Bottled water' },
        { ok: true, text: 'Folk music show' },
        { ok: false, text: 'Lunch (optional)' },
        { ok: false, text: 'Tips' },
      ],
      notes: '🛶 Duration: ~1 hour on water. Available daily 8:00–16:00. Great for families!',
    },
    'hue-dmz': {
      title: 'Basket Boat Ride & Vietnamese Food',
      badge: '🍲 Combo',
      image: 'tour_basket_boat_food.jpg',
      description: 'Combine a basket boat ride in the historic water coconut forest with a traditional Vietnamese meal at a local restaurant.',
      highlights: ['🛶 Basket Boat', '🍲 Vietnamese Lunch', '🦀 Crab Catching', '🎶 Karaoke', '🌿 Coconut Forest', '📸 Photos'],
      itinerary: [
        { time: '09:30', title: 'Hotel Pickup', desc: 'Pick up at your hotel.' },
        { time: '10:00', title: 'Historic Coconut Forest', desc: 'Transfer to the historic water coconut forest.' },
        { time: '10:15', title: '1 Hour Basket Boat', desc: 'Spinning boats, karaoke, fishing nets, crab catching.' },
        { time: '11:15', title: 'Vietnamese Lunch', desc: 'Steamed Red Snapper, Spring Rolls, Morning Glory, Banana Flower Salad at local restaurant.' },
        { time: '11:30', title: 'Hotel Drop-off', desc: 'Return to your hotel.' },
      ],
      included: [
        { ok: true, text: 'Hotel pickup & drop-off' },
        { ok: true, text: 'Basket boat ride' },
        { ok: true, text: 'Vietnamese lunch (4 dishes)' },
        { ok: true, text: 'Bottled water' },
        { ok: false, text: 'Extra drinks' },
      ],
      notes: '🍲 Morning: 9:30–11:30 or Afternoon: 15:00–17:00.',
    },
    'countryside-cycling': {
      title: 'Lantern Making, Market, Cooking & Basket Boat',
      badge: '🏮 Ultimate',
      image: 'tour_lantern_cooking.jpg',
      description: 'The most complete Hoi An experience: handmade lantern workshop, market visit, cooking class, and basket boat ride — all in one tour!',
      highlights: ['🏮 Lantern Making', '🛒 Market Tour', '👨‍🍳 Cooking Class', '🛶 Basket Boat', '🎨 Handcraft', '📸 Souvenirs'],
      itinerary: [
        { time: '08:30', title: 'Hotel Pickup', desc: 'Pick up at your hotel.' },
        { time: '09:00', title: 'Local Market Visit', desc: 'Explore the market and buy cooking ingredients.' },
        { time: '10:00', title: 'Basket Boat Ride', desc: 'Paddle through the water coconut forest.' },
        { time: '11:00', title: 'Cooking Class', desc: 'Cook Pho Bo, Banh Xeo, Spring Rolls, and Vietnamese Tea.' },
        { time: '11:45', title: 'Enjoy Your Meal', desc: 'Taste your handmade dishes.' },
        { time: '12:00', title: 'Lantern Making Workshop', desc: 'Create your own handmade Hoi An silk lantern to take home.' },
        { time: '12:30', title: 'Drop-off', desc: 'End at the lantern workshop in the Old Town.' },
      ],
      included: [
        { ok: true, text: 'Hotel pickup' },
        { ok: true, text: 'Basket boat & cooking class' },
        { ok: true, text: '1 handmade lantern' },
        { ok: true, text: 'All ingredients' },
        { ok: true, text: 'Bottled water' },
        { ok: false, text: 'Drinks & tips' },
      ],
      notes: '🏮 4 hours. Morning (8:30–12:30) or Afternoon (13:30–18:00).',
    },
    'son-tra-peninsula': {
      title: 'Cham Island Handicraft Tour',
      badge: '🧶 Heritage',
      image: 'tour_cham_handicraft.jpg',
      description: 'Experience UNESCO-recognized traditional crafts on Cham Island: hammock weaving, fishing net making, Banh It La Gai cake, and visit the Whale Temple.',
      highlights: ['🧶 Hammock Weaving', '🎣 Net Making', '🍡 Traditional Cake', '⛩️ Whale Temple', '🤿 Snorkeling', '🏝️ Island Life'],
      itinerary: [
        { time: '08:00', title: 'Hotel Pickup', desc: 'Pick up in Hoi An.' },
        { time: '08:45', title: 'Speedboat to Cham Island', desc: 'Depart from Cua Dai Port by speedboat.' },
        { time: '09:30', title: 'Traditional Crafts', desc: 'Weave hammocks with rattan, learn fishing net making.' },
        { time: '10:30', title: 'Banh It La Gai', desc: 'Make traditional sticky rice cakes with pandan leaves.' },
        { time: '11:00', title: 'Whale Temple', desc: 'Visit the sacred Whale Temple on the island.' },
        { time: '11:30', title: 'Snorkeling', desc: '45 min snorkeling at Bai Xep / Hon Dai coral reef.' },
        { time: '12:30', title: 'Seafood BBQ Lunch', desc: 'Fresh seafood BBQ on the island.' },
        { time: '13:30', title: 'Return to Hoi An', desc: 'Speedboat back to Cua Dai, transfer to hotel.' },
      ],
      included: [
        { ok: true, text: 'Round-trip speedboat & vehicle' },
        { ok: true, text: 'English-speaking guide' },
        { ok: true, text: 'Snorkeling equipment' },
        { ok: true, text: 'BBQ lunch' },
        { ok: true, text: 'Entrance fees' },
        { ok: true, text: 'Travel insurance' },
        { ok: false, text: 'Personal expenses' },
      ],
      notes: '🏝️ 8:00–14:00. Min 2, Max 15 guests. Cham Island is plastic-bag free.',
    },
    'perfume-river': {
      title: 'Cham Island 2 Days 1 Night (Homestay)',
      badge: '🏕️ Overnight',
      image: 'tour_cham_homestay.jpg',
      description: 'Stay overnight on Cham Island in a local homestay. Two snorkeling sessions, island exploration, and authentic island dining experience.',
      highlights: ['🏕️ Homestay', '🤿 2x Snorkeling', '🏝️ Island Life', '🌅 Sunrise/Sunset', '🍽️ Local Meals', '🌊 Beach Time'],
      itinerary: [
        { time: 'Day 1 AM', title: 'Transfer to Cham Island', desc: 'Hotel pickup, speedboat to island, visit Bai Lang village.' },
        { time: 'Day 1 PM', title: 'Snorkeling Session 1', desc: 'Guided snorkeling at the coral reef, lunch, check-in homestay.' },
        { time: 'Day 1 Eve', title: 'Free Exploration', desc: 'Explore the island freely, dinner at homestay.' },
        { time: 'Day 2 AM', title: 'Morning & Snorkeling 2', desc: 'Breakfast at homestay, second snorkeling session (10:00–10:30).' },
        { time: 'Day 2 PM', title: 'Return to Hoi An', desc: 'Lunch, beach time, speedboat back (14:00–14:30).' },
      ],
      included: [
        { ok: true, text: 'Hotel pickup & drop-off' },
        { ok: true, text: 'Round-trip speedboat' },
        { ok: true, text: 'Homestay accommodation' },
        { ok: true, text: 'All meals (lunch x2, dinner, breakfast)' },
        { ok: true, text: '2x snorkeling sessions' },
        { ok: true, text: 'Travel insurance' },
        { ok: false, text: 'Personal expenses' },
      ],
      notes: '🏕️ 2 days 1 night. Minimum 2 guests.',
    },
    'fishing-village': {
      title: 'Cham Island Snorkeling Tour (Advanced)',
      badge: '🤿 Deep Dive',
      image: 'tour_cham_snorkeling.jpg',
      description: 'Advanced snorkeling at 2 premium spots in Cham Island Marine Park. Includes Vietnamese lunch at Bai Ong and beach swimming.',
      highlights: ['🤿 2 Snorkeling Spots', '🐠 Rich Marine Life', '🍽️ Vietnamese Lunch', '🏖️ Beach Swimming', '☕ Tea & Coffee', '📸 Coral Reef'],
      itinerary: [
        { time: '07:30', title: 'Hotel Pickup', desc: 'Pick up in Hoi An.' },
        { time: '08:30', title: 'Depart Cua Dai Port', desc: 'Speedboat to Cham Island.' },
        { time: '09:30', title: 'Snorkeling Spot 1', desc: 'First snorkeling session at pristine coral reef.' },
        { time: '11:00', title: 'Snorkeling Spot 2', desc: 'Second snorkeling at a different reef area.' },
        { time: '12:30', title: 'Vietnamese Lunch', desc: 'Lunch at Bai Ong or Bai Lang, beach swimming & rest.' },
        { time: '14:30', title: 'Depart Island', desc: 'Leave Bai Lang.' },
        { time: '15:30', title: 'Hotel Drop-off', desc: 'Return to Hoi An hotel.' },
      ],
      included: [
        { ok: true, text: 'Round-trip transport & speedboat' },
        { ok: true, text: 'Snorkeling instructor & equipment' },
        { ok: true, text: 'Vietnamese lunch' },
        { ok: true, text: 'Insurance' },
        { ok: true, text: 'Tea & coffee on boat' },
        { ok: false, text: 'Personal expenses' },
      ],
      notes: '🤿 7:30–15:30. Two snorkeling spots for the best coral experience.',
    },
    'danang-city': {
      title: 'Cham Island Try Dive Tour (Beginners)',
      badge: '🌊 Try Dive',
      image: 'tour_cham_trydive.jpg',
      description: 'Scuba diving for absolute beginners — no certification needed. 1-on-1 instructor, max depth 6–12m. Explore vibrant coral gardens.',
      highlights: ['🤿 No License Needed', '👤 1-on-1 Instructor', '🐠 Coral Gardens', '🏖️ Beach Lunch', '📸 Underwater Photos', '🎓 1–2 Dives'],
      itinerary: [
        { time: '08:00', title: 'Hotel Pickup', desc: 'Pick up in Hoi An.' },
        { time: '08:45', title: 'Depart Cua Dai', desc: 'Speedboat to Cham Island.' },
        { time: '10:00', title: 'Dive Session 1', desc: 'Briefing + first dive (1 hour minimum) with 1-on-1 instructor. Depth: 6–12m.' },
        { time: '11:30', title: 'Dive Session 2', desc: 'Optional second dive at a different spot.' },
        { time: '12:30', title: 'Beach Lunch', desc: 'Lunch at Bai Chong, swimming and relaxation.' },
        { time: '15:00', title: 'Return', desc: 'Speedboat back to Cua Dai.' },
        { time: '16:00', title: 'Hotel Drop-off', desc: 'Return to Hoi An hotel.' },
      ],
      included: [
        { ok: true, text: 'Hotel pickup & drop-off' },
        { ok: true, text: 'Full diving equipment' },
        { ok: true, text: 'English-speaking dive instructor' },
        { ok: true, text: 'Beach lunch' },
        { ok: true, text: 'Water, coffee, tea, fruit on boat' },
        { ok: true, text: 'Marine park fee' },
        { ok: false, text: 'Tips & personal expenses' },
      ],
      notes: '🌊 8:00–16:00. 1 or 2 dives. No certification required!',
    },
    'bach-ma-park': {
      title: 'Cham Island Fun Dive (Certified Divers)',
      badge: '🎓 PADI',
      image: 'tour_cham_fundive.jpg',
      description: 'For certified PADI divers. Explore rich marine life: nudibranchs, seahorses, lionfish, and reef sharks. Depth 10–25m.',
      highlights: ['🎓 PADI Required', '🦈 Reef Sharks', '🐡 Seahorses', '🪸 Deep Coral', '📸 Marine Life', '🏖️ Beach Lunch'],
      itinerary: [
        { time: '08:00', title: 'Hotel Pickup', desc: 'Pick up in Hoi An.' },
        { time: '08:45', title: 'Depart Cua Dai', desc: 'Speedboat to Cham Island.' },
        { time: '10:00', title: 'Fun Dive 1', desc: 'First dive (1 hour min) — marine life at 10–25m depth.' },
        { time: '11:30', title: 'Fun Dive 2', desc: 'Second dive at different spot.' },
        { time: '12:30', title: 'Lunch at Bai Chong', desc: 'Lunch and beach relaxation.' },
        { time: '15:00', title: 'Return', desc: 'Speedboat back.' },
        { time: '16:00', title: 'Hotel Drop-off', desc: 'Return to Hoi An.' },
      ],
      included: [
        { ok: true, text: 'Hotel pickup & drop-off' },
        { ok: true, text: 'Full diving equipment' },
        { ok: true, text: 'English-speaking dive master' },
        { ok: true, text: 'Lunch' },
        { ok: true, text: 'Water, coffee, tea, fruit' },
        { ok: true, text: 'Marine park fee' },
        { ok: false, text: 'Tips' },
      ],
      notes: '🎓 8:00–16:00. PADI certification required. 1 or 2 dives.',
    },
    'tra-que-village': {
      title: 'Walking Underwater at Cham Island',
      badge: '🪖 Seawalker',
      image: 'tour_cham_walkingunder.jpg',
      description: 'Walk on the ocean floor — no swimming or diving skills needed. Wear an air-pumped helmet and stroll among colorful fish and coral.',
      highlights: ['🪖 Seawalker Helmet', '🐠 Walk Among Fish', '🪸 Coral Reef', '🤿 Snorkeling Included', '🍽️ Seafood Lunch', '📸 Underwater Photos'],
      itinerary: [
        { time: '07:30', title: 'Hotel Pickup', desc: 'Pick up in Hoi An, transfer to Cua Dai Port.' },
        { time: '09:00', title: 'Speedboat to Cham Island', desc: '20-minute ride to the island.' },
        { time: '10:00', title: 'Walking Underwater', desc: 'Walk on the seabed at Bai Nhon with air helmet — see fish and coral up close.' },
        { time: '10:30', title: 'Snorkeling', desc: 'Free snorkeling at the coral reef.' },
        { time: '11:00', title: 'Seafood Lunch', desc: 'Fresh seafood lunch at Bai Chong, beach swimming.' },
        { time: '13:00', title: 'Return', desc: 'Speedboat back to Cua Dai.' },
        { time: '14:00', title: 'Hotel Drop-off', desc: 'Return to Hoi An.' },
      ],
      included: [
        { ok: true, text: 'English-speaking guide' },
        { ok: true, text: 'Round-trip speedboat' },
        { ok: true, text: 'Seawalker & snorkeling equipment' },
        { ok: true, text: 'Seafood lunch' },
        { ok: true, text: 'Towel & entrance fees' },
        { ok: true, text: 'Travel insurance' },
        { ok: false, text: 'Personal expenses' },
      ],
      notes: '🪖 7:30–14:00. No swimming skills required!',
    },
    'lantern-making': {
      title: 'Cam Thanh Eco Water Coconut Village',
      badge: '🌿 Eco',
      image: 'tour_camthanh_eco.jpg',
      description: 'Experience the Cam Thanh Water Coconut Village ecosystem — basket boats, fishing, and peaceful canal exploration under coconut palms.',
      highlights: ['🛶 Basket Boat', '🎣 Fishing', '🌿 Coconut Forest', '🏡 Local Village', '🍽️ Local Lunch', '📸 Nature Photos'],
      itinerary: [
        { time: '09:00', title: 'Hotel Pickup', desc: 'Guide picks you up at your hotel.' },
        { time: '09:15', title: 'Transfer to Cam Thanh', desc: 'Travel to Cam Thanh Village by boat/car.' },
        { time: '10:00', title: 'Basket Boat Experience', desc: 'History lesson, fishing nets, boat racing, crab catching.' },
        { time: '10:45', title: 'Local Village Visit', desc: 'Visit a local home, enjoy welcome drinks.' },
        { time: '11:00', title: 'Local Lunch', desc: 'Traditional lunch at a local restaurant.' },
        { time: '11:30', title: 'Hotel Drop-off', desc: 'Return to your hotel.' },
      ],
      included: [
        { ok: true, text: 'Tour vehicle' },
        { ok: true, text: 'Bamboo basket boat' },
        { ok: true, text: 'English-speaking guide' },
        { ok: true, text: 'Entrance fees' },
        { ok: true, text: 'Lunch & water' },
        { ok: false, text: 'Tips' },
      ],
      notes: '🌿 2.5 hours. Morning (9:00–11:30) or Afternoon (15:00–17:30).',
    },
    'photo-tour': {
      title: 'Cam Thanh Cooking Tour',
      badge: '🍳 Cooking',
      image: 'tour_camthanh_cooking.jpg',
      description: 'Market visit, basket boat ride, and cook 5 traditional Hoi An dishes at Cam Thanh Village.',
      highlights: ['🛒 Market Tour', '🛶 Basket Boat', '👨‍🍳 5-Dish Cooking', '🌿 Cam Thanh', '🍽️ Lunch', '📸 Photo Ops'],
      itinerary: [
        { time: '08:15', title: 'Hotel Pickup', desc: 'Pick up at your hotel.' },
        { time: '08:45', title: 'Hoi An Market', desc: 'Visit local market to shop for ingredients.' },
        { time: '09:30', title: 'Cam Thanh Basket Boat', desc: 'Basket boat ride through the coconut forest.' },
        { time: '10:30', title: 'Cooking Class', desc: 'Cook 5 dishes: Banana Roll, Spring Rolls, Banh Xeo, Pho, Caramelized Fish.' },
        { time: '12:00', title: 'Enjoy Your Meal', desc: 'Taste your creations + Morning Glory, Rice, Dessert.' },
        { time: '12:40', title: 'Hotel Drop-off', desc: 'Return to hotel.' },
      ],
      included: [
        { ok: true, text: 'Tour vehicle & basket boat' },
        { ok: true, text: 'Cooking class & all ingredients' },
        { ok: true, text: 'English-speaking guide' },
        { ok: true, text: 'Entrance fees' },
        { ok: true, text: 'Lunch & water' },
        { ok: false, text: 'Tips' },
      ],
      notes: '🍳 Morning 8:15–12:40 or Afternoon 13:15–17:00.',
    },
    'spa-wellness': {
      title: 'Hoi An City Tour – Boat Ride & Flower Lantern',
      badge: '🏮 Evening',
      image: 'tour_hoian_city_boat.jpg',
      description: 'Explore Hoi An Ancient Town in the afternoon — visit the market, Fukian Assembly Hall, ancient houses, Japanese Bridge, then enjoy a romantic flower lantern boat ride on the Hoai River.',
      highlights: ['🏮 Flower Lantern Release', '⛩️ Assembly Halls', '🌉 Japanese Bridge', '🚣 River Boat Ride', '🍽️ Dinner', '🎭 Art Show'],
      itinerary: [
        { time: '14:30', title: 'Hotel Pickup', desc: 'Pick up at your hotel.' },
        { time: '15:00', title: 'Hoi An Market', desc: 'Visit the bustling local market.' },
        { time: '15:30', title: 'Fukian Assembly Hall', desc: 'Visit the ornate Phuc Kien Assembly Hall.' },
        { time: '16:00', title: 'Ancient Houses', desc: 'Explore Phung Hung / Tan Ky old merchant houses.' },
        { time: '16:30', title: 'Folk Museum & Art Show', desc: 'Visit the Folk Culture Museum and watch traditional art.' },
        { time: '17:00', title: 'Japanese Bridge', desc: 'Cross the iconic 400-year-old Covered Bridge.' },
        { time: '17:30', title: 'Dinner', desc: 'Enjoy Chicken Rice / Cao Lau / Mi Quang.' },
        { time: '18:00', title: 'Boat Ride & Flower Lantern', desc: 'Romantic boat ride on the Hoai River, release a flower lantern.' },
        { time: '18:30', title: 'Hotel Drop-off', desc: 'Return to hotel.' },
      ],
      included: [
        { ok: true, text: 'Hotel pickup & drop-off' },
        { ok: true, text: 'English-speaking guide' },
        { ok: true, text: 'All entrance tickets' },
        { ok: true, text: 'Dinner (1 dish)' },
        { ok: true, text: 'Boat ride & flower lantern' },
        { ok: true, text: 'Bottled water' },
        { ok: false, text: 'Extra food & tips' },
      ],
      notes: '🏮 14:30–18:30. Min 2, Max 15 guests. Hoi An Green Travel.',
    },
    'tailoring-experience': {
      title: 'Cam Thanh Coconut – Hoi An City – Flower Lantern',
      badge: '🌃 Combo',
      image: 'tour_hoian_lantern_night.jpg',
      description: 'The complete experience: water coconut forest in Cam Thanh, Hoi An Ancient Town walking tour, and evening flower lantern boat ride on the river.',
      highlights: ['🛶 Coconut Forest', '🏮 Ancient Town', '🌸 Flower Lantern', '🍽️ Local Dinner', '🌙 Night Walk', '📸 Best Photos'],
      itinerary: [
        { time: '12:00', title: 'Hotel Pickup', desc: 'Pick up at your hotel.' },
        { time: '12:30', title: 'Cam Thanh Coconut Forest', desc: 'Basket boat ride through the water coconut channels.' },
        { time: '14:30', title: 'Hoi An Ancient Town', desc: 'Fukian Hall, ancient houses, Japanese Bridge, museum.' },
        { time: '17:00', title: 'Dinner', desc: 'Enjoy Hoi An specialty set menu dinner.' },
        { time: '18:00', title: 'Boat Ride & Flower Lantern', desc: 'Romantic boat ride on Hoai River with flower lantern release.' },
        { time: '19:30', title: 'Hotel Drop-off', desc: 'Return to hotel.' },
      ],
      included: [
        { ok: true, text: 'Hotel pickup & drop-off' },
        { ok: true, text: 'English-speaking guide' },
        { ok: true, text: 'Basket boat & entrance tickets' },
        { ok: true, text: 'Dinner set menu' },
        { ok: true, text: 'Flower lantern & boat ride' },
        { ok: true, text: 'Bottled water' },
        { ok: false, text: 'Extra food & tips' },
      ],
      notes: '🌃 12:00–19:30. Full afternoon-to-evening experience!',
    },
    'street-food-night': {
      title: 'Bicycle Tour: Cam Thanh & Tra Que',
      badge: '🚲 Cycling',
      image: 'tour_bicycle_camthanh.jpg',
      description: 'Cycle through Hoi An countryside — visit Cam Thanh coconut forest and Tra Que organic vegetable village. Includes basket boat, farming, and cooking class.',
      highlights: ['🚲 Cycling', '🛶 Basket Boat', '🌱 Organic Farming', '👨‍🍳 4-Dish Cooking', '🌾 Rice Fields', '📸 Country Views'],
      itinerary: [
        { time: '08:00', title: 'Hotel Pickup by Bicycle', desc: 'Cycle to Cam Thanh Coconut Forest.' },
        { time: '09:00', title: 'Basket Boat & Fishing', desc: 'Basket boat ride, fishing, local culture experience.' },
        { time: '10:30', title: 'Cycle to Tra Que', desc: 'Continue cycling to Tra Que Vegetable Village.' },
        { time: '11:00', title: 'Farming Experience', desc: 'Work with local farmers in the organic garden.' },
        { time: '11:30', title: 'Cooking Class', desc: 'Cook 4 dishes: Papaya Salad, Banh Xeo, Spring Rolls, Caramelized Fish.' },
        { time: '12:30', title: 'Enjoy Your Meal', desc: 'Taste your creations.' },
        { time: '13:30', title: 'Hotel Drop-off', desc: 'Cycle back to hotel.' },
      ],
      included: [
        { ok: true, text: 'Bicycle & helmet' },
        { ok: true, text: 'Basket boat ride' },
        { ok: true, text: 'Farming experience' },
        { ok: true, text: 'Cooking class & lunch' },
        { ok: true, text: 'English-speaking guide' },
        { ok: true, text: 'Bottled water' },
        { ok: false, text: 'Tips' },
      ],
      notes: '🚲 5.5 hours. Morning (8:00–13:30) or Afternoon (13:00–18:30). Min 2 guests.',
    },
    'pottery-village': {
      title: 'Tra Que Cooking Class Tour',
      badge: '🌱 Farm-to-Table',
      image: 'tour_traque_cooking.jpg',
      description: 'Cooking class at Tra Que Organic Village — market visit, farming, foot massage, and cook 4 traditional dishes.',
      highlights: ['🌱 Organic Farm', '👨‍🍳 4-Dish Cooking', '💆 Foot Massage', '🛒 Market Tour', '🌿 Herb Garden', '🍽️ Farm Lunch'],
      itinerary: [
        { time: '08:30', title: 'Hotel Pickup', desc: 'Pick up and drive to Hoi An Market.' },
        { time: '09:00', title: 'Tra Que Village', desc: 'Cycle to Tra Que, explore the organic garden.' },
        { time: '09:30', title: 'Farming Experience', desc: 'Work with farmers — dig, sow, plant, and harvest.' },
        { time: '10:00', title: 'Foot Massage', desc: 'Traditional herbal foot massage.' },
        { time: '10:30', title: 'Cooking Class', desc: 'Cook: Papaya Salad, Banh Xeo, Spring Rolls, Caramelized Fish.' },
        { time: '12:00', title: 'Enjoy Meal', desc: 'Taste your farm-to-table creations.' },
        { time: '13:30', title: 'Hotel Drop-off', desc: 'Return to hotel.' },
      ],
      included: [
        { ok: true, text: 'Hotel pickup & drop-off' },
        { ok: true, text: 'Welcome drink' },
        { ok: true, text: 'Cooking class & chef' },
        { ok: true, text: 'Herbal foot massage' },
        { ok: true, text: 'Lunch & water' },
        { ok: false, text: 'Tips' },
      ],
      notes: '🌱 4.5 hours. Morning 8:30–13:30 or Afternoon 13:30–18:00. Min 2 guests.',
    },
    'river-cruise-sunset': {
      title: 'Lantern Making & Farming at Tra Que Village',
      badge: '🏮 Crafts',
      image: 'tour_lantern_farming.jpg',
      description: 'Cycle through rice paddies to Tra Que Village for farming, then learn traditional Hoi An lantern making and take home your handmade lantern.',
      highlights: ['🏮 Lantern Workshop', '🌱 Farming', '🚲 Cycling', '🌾 Rice Fields', '🎁 Take Home Lantern', '🍽️ Local Lunch'],
      itinerary: [
        { time: '08:00', title: 'Hotel Pickup', desc: 'Cycle through rice paddies and shrimp ponds.' },
        { time: '09:00', title: 'Tra Que Village', desc: 'Dig, sow, plant, and harvest vegetables with farmers.' },
        { time: '10:00', title: 'Tra Que Special Tea', desc: 'Enjoy the village signature herbal tea.' },
        { time: '10:30', title: 'Lantern Workshop', desc: 'Cycle to the lantern workshop, learn the craft from artisans.' },
        { time: '12:00', title: 'Make Your Lantern', desc: 'Create your own handmade silk lantern to take home.' },
        { time: '13:00', title: 'Local Lunch', desc: 'Traditional lunch included.' },
        { time: '13:30', title: 'Hotel Drop-off', desc: 'Return to hotel.' },
      ],
      included: [
        { ok: true, text: 'Bicycle & hotel pickup' },
        { ok: true, text: 'English-speaking guide' },
        { ok: true, text: '1 handmade lantern' },
        { ok: true, text: 'Farming experience' },
        { ok: true, text: 'Lunch & water' },
        { ok: true, text: 'Travel insurance' },
        { ok: false, text: 'Tips' },
      ],
      notes: '🏮 8:00–13:30. Min 2 guests. Includes lunch.',
    },
    'water-puppet-show': {
      title: 'Cycling, Buffalo Riding – Farming & Fishing',
      badge: '🐃 Adventure',
      image: 'tour_cycling_buffalo.jpg',
      description: 'Complete countryside cycling tour — buffalo riding, farming, basket boat crab catching, and learning about Vietnam war history.',
      highlights: ['🐃 Buffalo Riding', '🚲 Cycling', '🛶 Basket Boat', '🦀 Crab Catching', '🏡 Local Home Visit', '📖 War History'],
      itinerary: [
        { time: '08:30', title: 'Hotel Pickup', desc: 'Cycle to Cam Thanh Village.' },
        { time: '09:00', title: 'Buffalo Riding & Farming', desc: 'Meet farmers, plow fields, plant rice, ride and feed buffalo.' },
        { time: '10:00', title: 'Local Home Visit', desc: 'Enjoy coconut and tea at a local home.' },
        { time: '10:30', title: 'Basket Boat & Crab Catching', desc: 'Paddle through coconut forest, catch crabs.' },
        { time: '11:00', title: 'War History', desc: 'Learn about the American-Vietnam War history of the area.' },
        { time: '11:30', title: 'Traditional Lunch', desc: 'Lunch at local home, learn to make Gao and Banh Xeo.' },
        { time: '13:00', title: 'Hotel Drop-off', desc: 'Return to hotel.' },
      ],
      included: [
        { ok: true, text: 'Hotel pickup & drop-off' },
        { ok: true, text: 'Traditional lunch' },
        { ok: true, text: 'English-speaking guide' },
        { ok: true, text: 'Basket boat & bicycle' },
        { ok: true, text: 'Entrance fees & water' },
        { ok: false, text: 'Tips' },
      ],
      notes: '🐃 4.5 hours. Morning 8:30–13:00 or Afternoon 14:00–18:30. Min 2 guests.',
    },
    'hue-water-park': {
      title: 'Tra Nhieu Eco Tour – Kim Bong Rural Village',
      badge: '🎨 Heritage',
      image: 'tour_tranhieu_kimbong.jpg',
      description: 'Cycling tour exploring Kim Bong woodworking village — traditional boat building, colorful mat weaving, and basket boat ride at Tra Nhieu.',
      highlights: ['🪵 Woodworking Village', '🎨 Mat Weaving', '🛶 Basket Boat', '🚲 Cycling', '🌾 Rice Fields', '🍽️ Local Lunch'],
      itinerary: [
        { time: '08:30', title: 'Hotel Pickup & Cycling', desc: 'Cycle to Kim Bong Woodworking Village.' },
        { time: '09:00', title: 'Kim Bong Village', desc: 'Discover traditional boat building and carpentry secrets.' },
        { time: '10:00', title: 'Mat Weaving', desc: 'Learn to weave colorful traditional mats.' },
        { time: '10:30', title: 'Cycling Through Rice Fields', desc: 'Cycle through endless green rice paddies.' },
        { time: '11:00', title: 'Basket Boat at Tra Nhieu', desc: 'Paddle basket boats on coconut forest canals.' },
        { time: '12:00', title: 'Local Lunch', desc: 'Traditional lunch at a local restaurant.' },
        { time: '13:00', title: 'Hotel Drop-off', desc: 'Return to Hoi An.' },
      ],
      included: [
        { ok: true, text: 'Bicycle & hotel pickup' },
        { ok: true, text: 'Basket boat' },
        { ok: true, text: 'English-speaking guide' },
        { ok: true, text: 'Entrance fees' },
        { ok: true, text: 'Lunch & water' },
        { ok: false, text: 'Tips & personal expenses' },
      ],
      notes: '🎨 Morning 8:30–13:00 or Afternoon 13:30–18:00. Great photo opportunities!',
    },
    'hue-royal-dinner': {
      title: 'Rice Paper & Noodle Making + Cooking – Kim Bong',
      badge: '🥟 Cooking',
      image: 'tour_ricepaper_kimbong.jpg',
      description: 'Experience handmade rice paper making at Kim Bong Village and join a 2-hour cooking class to prepare 5 traditional Vietnamese dishes.',
      highlights: ['🥟 Rice Paper Making', '👨‍🍳 5-Dish Cooking', '🪵 Kim Bong Village', '🍜 Cao Lau Noodles', '🐟 Grilled Fish', '🍌 Banana Caramel'],
      itinerary: [
        { time: '08:15', title: 'Hotel Pickup', desc: 'Pick up at your hotel.' },
        { time: '09:00', title: 'Kim Bong Village', desc: 'Transfer to Kim Bong Woodworking Village.' },
        { time: '09:30', title: 'Rice Paper Making', desc: 'Make traditional rice paper by hand with local artisans.' },
        { time: '10:00', title: '2-Hour Cooking Class', desc: 'Vietnamese Spring Rolls, Chicken Cao Lau, Banh Xeo with Mushroom, Grilled Squid, Banana Caramel.' },
        { time: '12:00', title: 'Enjoy Your Meal', desc: 'Taste your handmade Vietnamese feast.' },
        { time: '13:00', title: 'Hotel Drop-off', desc: 'Return to hotel.' },
      ],
      included: [
        { ok: true, text: 'Hotel pickup & drop-off' },
        { ok: true, text: 'English-speaking guide' },
        { ok: true, text: 'Entrance fees' },
        { ok: true, text: 'All ingredients & lunch' },
        { ok: true, text: 'Bottled water' },
        { ok: false, text: 'Tips' },
      ],
      notes: '🥟 Morning 8:15–13:00 or Afternoon 13:30–18:00. Min 2 guests.',
    },
    'danang-nightlife': {
      title: 'My Son Sunrise Daily Tour',
      badge: '🌅 Sunrise',
      image: 'tour_myson_sunrise.jpg',
      description: 'Visit My Son Sanctuary at sunrise — explore Cham Pa temples built from the 7th–13th centuries. UNESCO World Heritage Site.',
      highlights: ['🏛️ UNESCO Heritage', '🌅 Sunrise Visit', '⛩️ Champa Temples', '🍜 My Quang Breakfast', '🚐 Electric Cart', '📸 Quiet & Beautiful'],
      itinerary: [
        { time: '05:00', title: 'Hotel Pickup', desc: 'Early pickup at your hotel in Hoi An.' },
        { time: '06:30', title: 'Arrive My Son', desc: 'Electric cart ride into the sanctuary.' },
        { time: '07:00', title: '2 Hours Exploring', desc: 'Guided tour of Champa temples and ruins with English guide.' },
        { time: '08:30', title: 'My Quang Breakfast', desc: 'Local specialty My Quang noodles at a nearby restaurant.' },
        { time: '09:30', title: 'Hotel Drop-off', desc: 'Return to Hoi An hotel by 10:00.' },
      ],
      included: [
        { ok: true, text: 'Hotel pickup & drop-off' },
        { ok: true, text: 'Electric cart ride' },
        { ok: true, text: 'English-speaking guide' },
        { ok: true, text: 'Entrance ticket' },
        { ok: true, text: 'Breakfast (My Quang)' },
        { ok: true, text: 'Bottled water' },
        { ok: false, text: 'Tips' },
      ],
      notes: '🌅 5:30–10:00. Min 2, Max 10 guests. Beat the crowds!',
    },
    'danang-surfing': {
      title: 'My Son Sanctuary Luxury Tour',
      badge: '✨ Luxury',
      image: 'tour_myson_luxury.jpg',
      description: 'Premium My Son tour — sanctuary visit, traditional Cham dance performance, rice paper making, and wooden boat cruise down Thu Bon River back to Hoi An.',
      highlights: ['🏛️ My Son Sanctuary', '💃 Cham Dance Show', '🥟 Rice Paper Making', '⛵ River Boat Cruise', '🍽️ Lunch Included', '📸 Premium Experience'],
      itinerary: [
        { time: '07:30', title: 'Hotel Pickup', desc: 'Pick up at your hotel.' },
        { time: '09:00', title: 'My Son Sanctuary', desc: 'Explore the temples, watch Cham traditional dance performance.' },
        { time: '11:15', title: 'Rice Paper Making', desc: 'Learn rice paper making at a local home.' },
        { time: '11:45', title: 'Lunch', desc: 'Lunch at a local restaurant.' },
        { time: '12:30', title: 'Wooden Boat Cruise', desc: 'Scenic cruise down Thu Bon River back to Hoi An.' },
        { time: '13:30', title: 'Hotel Drop-off', desc: 'Arrive at your hotel.' },
      ],
      included: [
        { ok: true, text: 'Hotel pickup & drop-off' },
        { ok: true, text: 'Electric cart & wooden boat' },
        { ok: true, text: 'English-speaking guide' },
        { ok: true, text: 'Entrance ticket' },
        { ok: true, text: 'Lunch & water' },
        { ok: false, text: 'Tips' },
      ],
      notes: '✨ 7:30–13:30. Min 1, Max 12 guests.',
    },
    'danang-helicopter': {
      title: 'My Son Sunset Tour',
      badge: '🌇 Sunset',
      image: 'tour_myson_sunset.jpg',
      description: 'Discover My Son Sanctuary in the afternoon — Cham traditional dance, then a scenic boat cruise down Thu Bon River during golden sunset.',
      highlights: ['🏛️ Afternoon Visit', '💃 Cham Dance', '⛵ Sunset River Cruise', '🌅 Golden Hour', '🥖 Banh Mi Snack', '📸 Sunset Photos'],
      itinerary: [
        { time: '13:00', title: 'Hotel Pickup', desc: 'Pick up at your hotel.' },
        { time: '15:00', title: 'My Son Sanctuary', desc: '2-hour guided tour of Champa temples, Cham dance show.' },
        { time: '17:00', title: 'Boat Cruise', desc: 'Scenic wooden boat cruise on Thu Bon River to Hoi An during sunset.' },
        { time: '18:00', title: 'Hotel Drop-off', desc: 'Arrive at your hotel.' },
      ],
      included: [
        { ok: true, text: 'Hotel pickup & drop-off' },
        { ok: true, text: 'Electric cart & wooden boat' },
        { ok: true, text: 'English-speaking guide' },
        { ok: true, text: 'Entrance ticket' },
        { ok: true, text: 'Banh Mi Vietnamese sandwich' },
        { ok: true, text: 'Bottled water' },
        { ok: false, text: 'Tips' },
      ],
      notes: '🌇 13:00–18:00. Min 1, Max 12 guests. Best sunset views!',
    },
    'danang-golf': {
      title: 'Hue Imperial City Full Day Tour',
      badge: '🏯 Imperial',
      image: 'tour_hue_citytour.jpg',
      description: 'Full-day trip to the ancient imperial capital of Hue. Cross the scenic Hai Van Pass, visit Khai Dinh Tomb, the Imperial Citadel, and Thien Mu Pagoda.',
      highlights: ['🏯 Imperial Citadel', '⛰️ Hai Van Pass', '🪦 Khai Dinh Tomb', '🛕 Thien Mu Pagoda', '🍽️ Hue Royal Cuisine', '📸 Lap An Lagoon'],
      itinerary: [
        { time: '07:00', title: 'Hotel Pickup', desc: 'Pick up in Hoi An (or 8:00 from Da Nang).' },
        { time: '08:30', title: 'Hai Van Pass', desc: 'Cross the legendary Hai Van Pass — stop for panoramic photos.' },
        { time: '09:30', title: 'Lap An Lagoon', desc: 'Photo stop at the beautiful Lap An Lagoon.' },
        { time: '11:00', title: 'Khai Dinh Tomb', desc: 'Visit the elaborate French-influenced tomb of Emperor Khai Dinh.' },
        { time: '12:30', title: 'Hue Specialty Lunch', desc: 'Traditional Hue royal cuisine lunch.' },
        { time: '13:30', title: 'Imperial Citadel', desc: 'Explore the Forbidden Purple City and Imperial Palace.' },
        { time: '15:00', title: 'Thien Mu Pagoda', desc: 'Visit the oldest pagoda in Hue, overlooking the Perfume River.' },
        { time: '16:00', title: 'Return Journey', desc: 'Drive back to Da Nang (18:00) or Hoi An (19:00).' },
      ],
      included: [
        { ok: true, text: 'Hotel pickup & drop-off' },
        { ok: true, text: 'English-speaking guide' },
        { ok: true, text: 'All entrance tickets' },
        { ok: true, text: 'Hue specialty lunch' },
        { ok: true, text: 'Bottled water' },
        { ok: false, text: 'Tips & personal expenses' },
      ],
      notes: '🏯 7:00–19:00. Full day trip (~12 hours). One of the best day trips from Hoi An!',
    },
"""

# Read HTML
with open(r'd:\project\booking\sontra-villa\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the end of existing TOUR_DATA entries (after 'my-son' entry closing brace)
# Insert new entries before the closing of TOUR_DATA object
marker = "'my-son': {"
idx = html.find(marker)
if idx < 0:
    print("ERROR: Could not find 'my-son' entry")
    exit(1)

# Find the end of my-son entry (look for the next tour key or end of TOUR_DATA)
# Find the closing of my-son: look for "},\n  };" pattern
myson_end = html.find("};", idx)
# Actually, find the pattern "  };" which closes TOUR_DATA
# The TOUR_DATA closing is "};" after the last entry

# Better: find "  };" or just "};" after all tour entries
# Let's find the script section and the TOUR_DATA closing
tour_data_start = html.find("TOUR_DATA = {")
if tour_data_start < 0:
    print("ERROR: TOUR_DATA not found")
    exit(1)

# Find the closing "};" of TOUR_DATA
# We need to find the matching closing brace
depth = 0
found_start = False
close_idx = -1
for i in range(tour_data_start, len(html)):
    if html[i] == '{':
        depth += 1
        found_start = True
    elif html[i] == '}':
        depth -= 1
        if found_start and depth == 0:
            close_idx = i
            break

if close_idx < 0:
    print("ERROR: Could not find TOUR_DATA closing brace")
    exit(1)

print(f"TOUR_DATA closes at index {close_idx}")
print(f"Before close: ...{repr(html[close_idx-20:close_idx+5])}")

# Insert new entries before the closing brace
new_html = html[:close_idx] + TOUR_DATA_ENTRIES + "  " + html[close_idx:]

with open(r'd:\project\booking\sontra-villa\index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("SUCCESS: Added TOUR_DATA entries for 26 new tours!")
print(f"New file size: {len(new_html)} chars")
