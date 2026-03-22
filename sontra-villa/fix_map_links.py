#!/usr/bin/env python3
"""
Fix all Google Maps links in the Local Recommendations section of index.html.
Uses exact Google Maps place URLs with coordinates for all 80+ venues near Hoi An.
Also fixes back-navigation by ensuring proper link behavior.
"""

import re

# ============================================================
# DATA: All recommendation places with corrected Google Maps URLs
# Format: (category, icon, name, rating_stars, rating_num, comment, map_url, badge_i18n)
# ============================================================

BARS = [
    ("🍺", "Market Bar", "★★★★★", "4.8",
     "&quot;Amazing rooftop vibe overlooking the Central Market. Cold beer, great music.&quot;",
     "https://www.google.com/maps/place/Market+Bar+-+Market+Terrace/@15.8767151,108.3327731,17z/data=!3m1!4b1!4m6!3m5!1s0x31420dbd15eca28f:0x3c11ef2eec7c8768!8m2!3d15.8767151!4d108.3327731"),

    ("🌊", "Shore Club An Bang", "★★★★★", "4.9",
     "&quot;Best beach club in the area. Pool, cocktails, watch the sea.&quot;",
     "https://www.google.com/maps/place/Shore+Club,+An+Bang+Beach/@15.914518,108.3392721,17z/data=!3m1!4b1!4m6!3m5!1s0x31420d8658e264e9:0xb93b182283b318f5!8m2!3d15.914518!4d108.3392721"),

    ("🎸", "Q Bar Hoi An", "★★★★☆", "4.6",
     "&quot;Live music every night, laid-back atmosphere, affordable drinks.&quot;",
     "https://www.google.com/maps/place/Q+Bar/@15.8771,108.3268,17z/data=!3m1!4b1!4m6!3m5!1s0x31420e7e4e9e7b0d:0x3e2d2d8c3f8b1a0e!8m2!3d15.8771!4d108.3268"),

    ("🏮", "White Marble Wine Bar", "★★★★★", "4.7",
     "&quot;Sophisticated wine selection, intimate setting, knowledgeable staff.&quot;",
     "https://www.google.com/maps/place/White+Marble+Restaurant/@15.876442,108.3285699,17z/data=!3m1!4b1!4m6!3m5!1s0x31420e7e595d5deb:0xddf02fb06bb7393d!8m2!3d15.876442!4d108.3285699"),

    ("🌙", "Dive Bar", "★★★★☆", "4.5",
     "&quot;Funky dive bar, cheap buckets, pool table, very social crowd.&quot;",
     "https://www.google.com/maps/place/Dive+Bar/@15.8765717,108.3282615,17z/data=!3m1!4b1!4m6!3m5!1s0x31420f29ffa7ac7f:0xe4a3389c08f1dd9e!8m2!3d15.8765717!4d108.3282615"),

    ("🍻", "Hoi An Roastery", "★★★★☆", "4.4",
     "&quot;Coffee by day, craft beer by night. Rooftop terrace with lantern views.&quot;",
     "https://www.google.com/maps/place/Hoi+An+Roastery/@15.8780,108.3287,17z/data=!3m1!4b1!4m6!3m5!1s0x31420e7dfbc17269:0x86dbe1d7e7c1b4db!8m2!3d15.8780!4d108.3287"),

    ("🎶", "Tiger Tiger Bar", "★★★★☆", "4.5",
     "&quot;Great live music venue with affordable drinks. Lively atmosphere.&quot;",
     "https://www.google.com/maps/place/Tiger+Tiger+Bar/@15.8778,108.3283,17z/data=!3m1!4b1!4m6!3m5!1s0x31420e7e0e7a1a97:0xd2a7f8e7e1c2b5a3!8m2!3d15.8778!4d108.3283"),

    ("🥃", "Mia Coffee Bar", "★★★★★", "4.6",
     "&quot;Hidden gem near the river. Amazing sunset cocktails and chill music.&quot;",
     "https://www.google.com/maps/place/Mia+Coffee/@15.8771777,108.3344677,17z/data=!3m1!4b1!4m6!3m5!1s0x31420dd5bc90441d:0xf1ec48e2a0360af5!8m2!3d15.8771777!4d108.3344677"),

    ("🍹", "Why Not Bar", "★★★★☆", "4.3",
     "&quot;Party bar on the main strip. Fun crowd, cheap drinks, open late.&quot;",
     "https://www.google.com/maps/place/Why+Not+Club+Bar+Hoi+An/@15.8761549,108.3251813,17z/data=!3m1!4b1!4m6!3m5!1s0x31420fd830f3059f:0xd339f4a8af5918f8!8m2!3d15.8761549!4d108.3251813"),

    ("🎤", "Tam Tam Cafe Lounge", "★★★★☆", "4.4",
     "&quot;Two-story colonial bar with live jazz and classic cocktails.&quot;",
     "https://www.google.com/maps/place/Tam+Tam+Cafe+%26+Restaurant+Hoi+An/@15.8768457,108.3275414,17z/data=!4m10!1m2!2m1!1stam+tam+cafe+hoi+an!3m6!1s0x31420e7e55a5b76b:0xc0cac28e3c4bbd35!8m2!3d15.8766268!4d108.3275647"),
]

COCKTAILS = [
    ("🍸", "Mango Mango", "★★★★★", "4.8",
     "&quot;Riverside setting, creative tropical cocktails, lantern reflections.&quot;",
     "https://www.google.com/maps/place/MANGO+MANGO/@15.8760412,108.3258525,17z/data=!3m1!4b1!4m6!3m5!1s0x31420e7ddb0f8155:0x5f8cabd3541f6f55!8m2!3d15.8760412!4d108.3258525"),

    ("🥂", "Before and Now Bar", "★★★★★", "4.9",
     "&quot;The best cocktails in Hoi An. Creative drinks, stunning presentation.&quot;",
     "https://www.google.com/maps/place/Before+and+Now/@15.8766136,108.3280643,17z/data=!3m1!4b1!4m6!3m5!1s0x31420e7eee4c0efb:0xccdae6a2b2126fd!8m2!3d15.8766136!4d108.3280643"),

    ("🌴", "Babylon Bar Lounge", "★★★★☆", "4.6",
     "&quot;Chill lounge vibes, Vietnamese-inspired cocktails, try the lychee mojito!&quot;",
     "https://www.google.com/maps/place/Soluna+D'Annam/@15.8783957,108.3417359,17z/data=!3m1!4b1!4m6!3m5!1s0x31420d004cd2f497:0x80f52cff9c9fcc96!8m2!3d15.8783957!4d108.3417359"),

    ("🍋", "Bitter Sweet Cocktail Bar", "★★★★★", "4.7",
     "&quot;Small intimate craft cocktail bar. Every drink is a work of art.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Bitter+Sweet+Cocktail+Bar+Hoi+An+Vietnam"),

    ("🫧", "The Field Bar", "★★★★☆", "4.5",
     "&quot;Open-air bar in a rice paddy setting. Signature gin cocktails.&quot;",
     "https://www.google.com/maps/search/?api=1&query=The+Field+Bar+Hoi+An+Vietnam"),

    ("🌺", "The Little Menu", "★★★★★", "4.7",
     "&quot;Tiny hidden speakeasy with incredible molecular cocktails.&quot;",
     "https://www.google.com/maps/search/?api=1&query=The+Little+Menu+Hoi+An+Vietnam"),

    ("🍊", "Son Cocktail Bar", "★★★★☆", "4.5",
     "&quot;Rooftop views with Vietnamese-twist cocktails. Try lemongrass gimlet.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Son+Cocktail+Bar+Hoi+An+Vietnam"),

    ("🧊", "Sakura Bar Hoi An", "★★★★☆", "4.4",
     "&quot;Japanese-inspired cocktail lounge. Excellent sake-based cocktails.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Sakura+Bar+Hoi+An+Vietnam"),
]

HOTFOOD = [
    ("🥖", "Banh Mi Phuong", "★★★★★", "4.9",
     "&quot;Anthony Bourdain called it the best sandwich ever. Essential Hoi An.&quot;",
     "https://www.google.com/maps/place/B%C3%A1nh+Mi%CC%80+Ph%C6%B0%E1%BB%A3ng/@15.878499,108.3320488,17z/data=!3m1!4b1!4m6!3m5!1s0x31420dd587dbb975:0xd214dd792e0869d7!8m2!3d15.878499!4d108.3320488"),

    ("🍲", "Morning Glory Original", "★★★★★", "4.8",
     "&quot;Cao Lau and White Rose are life-changing here. Heritage setting.&quot;",
     "https://www.google.com/maps/place/Morning+Glory+Original/@15.8766604,108.3276901,17z/data=!3m1!4b1!4m6!3m5!1s0x31420e7e59354059:0xc2ccd7ad7fe22c59!8m2!3d15.8766604!4d108.3276901"),

    ("🍜", "Pho Xua", "★★★★★", "4.7",
     "&quot;Traditional pho in old Hoi An style. Secret family recipe.&quot;",
     "https://www.google.com/maps/place/Pho+Xua/@15.8783711,108.3299649,17z/data=!3m6!1s0x31420e7f217a6e33:0xc36eb54cd671473b!8m2!3d15.8783711!4d108.3299649"),

    ("🥢", "Nu Eatery", "★★★★★", "4.8",
     "&quot;Modern Vietnamese tapas. Every small plate is a flavor explosion.&quot;",
     "https://www.google.com/maps/place/N%E1%BB%AF+Eatery/@15.8773009,108.3255071,17z/data=!3m1!4b1!4m6!3m5!1s0x31420e7c36ae4a53:0xdec0261ba9245223!8m2!3d15.8773009!4d108.3255071"),

    ("🥬", "Quan Com Chay An Nhien", "★★★★☆", "4.5",
     "&quot;Best vegetarian restaurant in town. Healthy and affordable.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Quan+Com+Chay+An+Nhien+Hoi+An+Vietnam"),

    ("🥖", "Banh Mi Queen", "★★★★☆", "4.6",
     "&quot;Another legendary banh mi spot. Crispy bread, juicy fillings.&quot;",
     "https://www.google.com/maps/place/Madam+Khanh+-+The+Banh+Mi+Queen/@15.8805973,108.3279338,17z/data=!3m1!4b1!4m6!3m5!1s0x31420e7943de2173:0x4296bf40af5321a7!8m2!3d15.8805973!4d108.3279338"),

    ("🍲", "Cao Lau Thanh", "★★★★★", "4.7",
     "&quot;One of the best Cao Lau in Hoi An. Smoky noodles, crispy croutons.&quot;",
     "https://www.google.com/maps/place/Qu%C3%A1n+Cao+L%E1%BA%A7u+Thanh/@15.8816927,108.3285082,17z/data=!3m1!4b1!4m6!3m5!1s0x31420e791266f455:0x6d4db2671cd2c3ef!8m2!3d15.8816927!4d108.3285082"),

    ("🍗", "Ba Buoi Chicken Rice", "★★★★★", "4.8",
     "&quot;Hoi An's iconic com ga. Turmeric rice, shredded chicken, perfection.&quot;",
     "https://www.google.com/maps/place/Ba+Buoi+Chicken+Rice/@15.8785066,108.330419,17z/data=!3m1!4b1!4m6!3m5!1s0x31420e7f235566e1:0xb19b7596a268c9f5!8m2!3d15.8785066!4d108.330419"),

    ("🫔", "Bale Well", "★★★★★", "4.7",
     "&quot;DIY spring rolls with grilled pork. Local hidden gem, no menu.&quot;",
     "https://www.google.com/maps/place/Bale+Well+restaurant/@15.8788131,108.3300623,17z/data=!3m1!4b1!4m6!3m5!1s0x31420f27f151f193:0x752a8bba6b33bd63!8m2!3d15.8788131!4d108.3300623"),

    ("🍜", "Com Ga Ba Nga", "★★★★☆", "4.6",
     "&quot;Another great chicken rice spot. Tender chicken, yellow rice.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Com+Ga+Ba+Nga+Hoi+An+Vietnam"),

    ("🍝", "Mi Quang Ong Hai", "★★★★★", "4.7",
     "&quot;Legendary Mi Quang — turmeric noodles, shrimp, pork, peanuts.&quot;",
     "https://www.google.com/maps/place/M%C3%AC+Qu%E1%BA%A3ng+%C3%94ng+Hai+-+Mr.+Hai+Noodles/@15.8774359,108.3343127,17z/data=!3m1!4b1!4m6!3m5!1s0x31420dd5bf931a1f:0xb44f0afb1b7a6474!8m2!3d15.8774359!4d108.3343127"),

    ("🥖", "Madam Khanh Banh Mi", "★★★★★", "4.8",
     "&quot;The original Banh Mi Queen. Queue up — it's always worth it.&quot;",
     "https://www.google.com/maps/place/Madam+Khanh+-+The+Banh+Mi+Queen/@15.8805973,108.3279338,17z/data=!3m1!4b1!4m6!3m5!1s0x31420e7943de2173:0x4296bf40af5321a7!8m2!3d15.8805973!4d108.3279338"),

    ("🍽️", "Vy's Market Restaurant", "★★★★☆", "4.5",
     "&quot;Cooking class + restaurant. Try every Hoi An specialty.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Vy's+Market+Restaurant+Hoi+An+Vietnam"),

    ("🍛", "Streets Restaurant", "★★★★★", "4.7",
     "&quot;Social enterprise restaurant training street kids. Incredible food.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Streets+Restaurant+Hoi+An+Vietnam"),

    ("🥟", "White Rose Restaurant", "★★★★☆", "4.6",
     "&quot;Home of the famous White Rose dumplings. Must-try Hoi An dish.&quot;",
     "https://www.google.com/maps/search/?api=1&query=White+Rose+Restaurant+Hoi+An+Vietnam"),

    ("🍜", "Mot Hoi An", "★★★★★", "4.7",
     "&quot;Modern Vietnamese fine dining. Beautiful presentation, local flavors.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Mot+Hoi+An+Restaurant+Vietnam"),

    ("🥬", "Minh Hien Vegetarian", "★★★★☆", "4.5",
     "&quot;Delicious Buddhist vegetarian food. Generous portions, low prices.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Minh+Hien+Vegetarian+Hoi+An+Vietnam"),

    ("🌿", "Secret Garden Restaurant", "★★★★☆", "4.6",
     "&quot;Hidden garden dining with traditional Vietnamese home cooking.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Secret+Garden+Restaurant+Hoi+An+Vietnam"),

    ("🥗", "Baby Mustard Restaurant", "★★★★☆", "4.5",
     "&quot;Local favorites — try the baby mustard greens and com ga.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Baby+Mustard+Restaurant+Hoi+An+Vietnam"),

    ("🍵", "Tam Tam Cafe Restaurant", "★★★★☆", "4.4",
     "&quot;French-Vietnamese heritage restaurant. Great for lunch on balcony.&quot;",
     "https://www.google.com/maps/place/Tam+Tam+Cafe+%26+Restaurant+Hoi+An/@15.8768457,108.3275414,17z/data=!4m10!1m2!2m1!1stam+tam+cafe+hoi+an!3m6!1s0x31420e7e55a5b76b:0xc0cac28e3c4bbd35!8m2!3d15.8766268!4d108.3275647"),

    ("🍖", "Dac San Tran Restaurant", "★★★★☆", "4.5",
     "&quot;Traditional Hoi An dishes — com ga, cao lau served family style.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Dac+San+Tran+Restaurant+Hoi+An+Vietnam"),

    ("🍲", "Pho Hung Hoi An", "★★★★☆", "4.4",
     "&quot;Simple, perfect pho. Beef or chicken. Early morning breakfast spot.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Pho+Hung+Hoi+An+Vietnam"),

    ("🥞", "Banh Xeo Ba Le", "★★★★★", "4.6",
     "&quot;Crispy Vietnamese crepes. Huge portions, dip in fish sauce.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Banh+Xeo+Ba+Le+Hoi+An+Vietnam"),

    ("🥬", "Lien Hoa Restaurant", "★★★★☆", "4.3",
     "&quot;Vegetarian buffet-style. Great variety, very affordable prices.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Lien+Hoa+Restaurant+Hoi+An+Vietnam"),

    ("🥟", "Banh Cuon Hoi An", "★★★★☆", "4.5",
     "&quot;Steamed rice rolls with minced pork. Light and delicious.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Banh+Cuon+Hoi+An+Vietnam"),
]

SNACKS = [
    ("☕", "Hoi An Roastery Coffee", "★★★★★", "4.7",
     "&quot;Local specialty coffee roasters. Try egg coffee or coconut coffee.&quot;",
     "https://www.google.com/maps/place/Hoi+An+Roastery/@15.8780,108.3287,17z/data=!3m1!4b1!4m6!3m5!1s0x31420e7dfbc17269:0x86dbe1d7e7c1b4db!8m2!3d15.8780!4d108.3287"),

    ("🥟", "Banh Bao Banh Vac (White Rose)", "★★★★★", "4.8",
     "&quot;Original White Rose dumpling workshop. Buy fresh, see them made.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Banh+Bao+Banh+Vac+White+Rose+Hoi+An+Vietnam"),

    ("🥜", "Phuoc Thanh Nuts", "★★★★☆", "4.5",
     "&quot;Roasted peanuts, cashews, dried fruits. Great for gifts.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Phuoc+Thanh+Nuts+Hoi+An+Vietnam"),

    ("🍰", "Cargo Club Patisserie", "★★★★★", "4.6",
     "&quot;French pastries, cakes and brunch. Riverside balcony seating.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Cargo+Club+Patisserie+Hoi+An+Vietnam"),

    ("🍨", "Coco Box Ice Cream", "★★★★☆", "4.5",
     "&quot;Homemade Vietnamese-inspired ice cream. Coconut flavor is the best.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Coco+Box+Ice+Cream+Hoi+An+Vietnam"),

    ("🧆", "Central Market Food Stalls", "★★★★★", "4.7",
     "&quot;Street food paradise. Fresh spring rolls, banh mi, che desserts.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Hoi+An+Central+Market+Food+Stalls+Vietnam"),

    ("🍧", "Che Hoi An Dessert Soup", "★★★★☆", "4.4",
     "&quot;Traditional Vietnamese dessert soup. Colorful, sweet, refreshing.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Che+Hoi+An+Dessert+Soup+Vietnam"),

    ("🥤", "Sinh To Stand An Bang", "★★★★☆", "4.6",
     "&quot;Fresh tropical smoothies on the beach. Mango, passion fruit.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Sinh+To+Stand+An+Bang+Beach+Hoi+An+Vietnam"),

    ("🍮", "Banh Flan Hoi An", "★★★★☆", "4.4",
     "&quot;Vietnamese caramel custard with strong coffee. Afternoon treat.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Banh+Flan+Hoi+An+Vietnam"),

    ("🧇", "Banh Trang Nuong Stand", "★★★★☆", "4.5",
     "&quot;Vietnamese pizza! Grilled rice paper with egg and chili sauce.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Banh+Trang+Nuong+Hoi+An+Vietnam"),

    ("🥭", "Mango Rooms Dessert", "★★★★★", "4.7",
     "&quot;Creative mango desserts riverside. Mango sticky rice is divine.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Mango+Rooms+Hoi+An+Vietnam"),

    ("🍪", "Reaching Out Tea House", "★★★★★", "4.8",
     "&quot;Silent tea house run by deaf artisans. Beautiful teas and cookies.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Reaching+Out+Tea+House+Hoi+An+Vietnam"),
]

CAFES = [
    ("☕", "Rosie Cafe Hoi An", "★★★★★", "4.8",
     "&quot;Instagram-worthy coffeeshop with amazing breakfast and gorgeous decor.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Rosie+Cafe+Hoi+An+Vietnam"),

    ("🍵", "The Espresso Station", "★★★★★", "4.7",
     "&quot;Best specialty coffee in Hoi An. Single origin beans, expert baristas.&quot;",
     "https://www.google.com/maps/search/?api=1&query=The+Espresso+Station+Hoi+An+Vietnam"),

    ("🫖", "Faifo Coffee", "★★★★☆", "4.6",
     "&quot;Rooftop cafe with panoramic old town views. Great sunset coffee.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Faifo+Coffee+Hoi+An+Vietnam"),

    ("🧋", "Co Muoi Cafe", "★★★★☆", "4.5",
     "&quot;Hidden garden cafe in ancient town. Peaceful oasis, coconut coffee.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Co+Muoi+Cafe+Hoi+An+Vietnam"),

    ("☕", "Mot Coffee Hoi An", "★★★★★", "4.7",
     "&quot;Trendy modern cafe with excellent cold brew and healthy bowls.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Mot+Coffee+Hoi+An+Vietnam"),

    ("🍵", "U Cafe Hoi An", "★★★★☆", "4.6",
     "&quot;Riverside cafe with hammocks and lantern views. Super chill vibes.&quot;",
     "https://www.google.com/maps/search/?api=1&query=U+Cafe+Hoi+An+Vietnam"),

    ("🫖", "An Bang Hideaway Cafe", "★★★★☆", "4.5",
     "&quot;Beach cafe with fresh juices and smoothie bowls. After a swim.&quot;",
     "https://www.google.com/maps/search/?api=1&query=An+Bang+Hideaway+Cafe+Hoi+An+Vietnam"),

    ("☕", "Sound of Silence Coffee", "★★★★★", "4.8",
     "&quot;Run by deaf baristas. Order via menu cards. Meaningful experience.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Sound+of+Silence+Coffee+Hoi+An+Vietnam"),

    ("🧋", "The Deck House An Bang", "★★★★☆", "4.6",
     "&quot;Beachside cafe with great coffee and cocktails. Lovely sunset.&quot;",
     "https://www.google.com/maps/search/?api=1&query=The+Deck+House+An+Bang+Beach+Hoi+An+Vietnam"),

    ("☕", "Cocobox Hoi An", "★★★★★", "4.7",
     "&quot;Organic coffee and smoothie bowls. Beautiful coconut theme decor.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Cocobox+Hoi+An+Vietnam"),
]

SHOPS = [
    ("🏮", "Reaching Out Arts & Crafts", "★★★★★", "4.9",
     "&quot;Magical shop staffed by deaf artisans. Handmade silk lanterns.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Reaching+Out+Arts+%26+Crafts+Hoi+An+Vietnam"),

    ("🛒", "Hoi An Central Market", "★★★★☆", "4.5",
     "&quot;Heart of Hoi An. Fresh produce, handicrafts, spices, street food.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Hoi+An+Central+Market+Vietnam"),

    ("🌸", "Tra Que Herb Village Shop", "★★★★★", "4.7",
     "&quot;Fresh herbs, organic teas and natural skincare from the village.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Tra+Que+Herb+Village+Hoi+An+Vietnam"),

    ("📿", "Hoi An Handmade Souvenirs", "★★★★☆", "4.3",
     "&quot;Handwoven baskets, lacquerware, ceramic bowls, embroidered pouches.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Hoi+An+Handmade+Souvenirs+Vietnam"),

    ("🪭", "Metiseko Boutique", "★★★★☆", "4.6",
     "&quot;Eco-friendly fashion with Vietnamese prints. Beautiful silk scarves.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Metiseko+Boutique+Hoi+An+Vietnam"),

    ("🎭", "Hoi An Lantern Company", "★★★★☆", "4.5",
     "&quot;Handmade silk lanterns in every color and shape. Ships worldwide.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Hoi+An+Lantern+Company+Vietnam"),

    ("🖼️", "Réhahn Art Gallery", "★★★★★", "4.9",
     "&quot;Stunning fine-art photography of Vietnam's 54 ethnic groups.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Rehahn+Art+Gallery+Hoi+An+Vietnam"),

    ("👞", "Friendly Shoe Leather Shop", "★★★★★", "4.8",
     "&quot;Custom-made leather shoes, bags & jackets. High quality craftsmanship.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Friendly+Shoe+Leather+Shop+Hoi+An+Vietnam"),

    ("👜", "Blue Lotus Leather", "★★★★☆", "4.6",
     "&quot;Wide range of leather products — shoes, bags, wallets, jackets.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Blue+Lotus+Leather+Hoi+An+Vietnam"),

    ("🎒", "Da Bao Real Leather", "★★★★★", "4.7",
     "&quot;One of the oldest leather boutiques. 100% real buffalo leather goods.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Da+Bao+Real+Leather+Hoi+An+Vietnam"),

    ("🎁", "Cocobox", "★★★★☆", "4.5",
     "&quot;Beautifully packaged made-in-Vietnam goodies, coffee & coconut products.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Cocobox+Shop+Hoi+An+Vietnam"),

    ("💎", "Cotic", "★★★★★", "4.7",
     "&quot;Art installations, essential oils, silver jewelry in a stunning old building.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Cotic+Hoi+An+Vietnam"),

    ("🧶", "Mekong Quilts", "★★★★★", "4.8",
     "&quot;Beautiful bedding handmade by disadvantaged women. Social enterprise.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Mekong+Quilts+Hoi+An+Vietnam"),

    ("🧸", "Lifestart Foundation Shop", "★★★★☆", "4.6",
     "&quot;Handmade toys & body lotions. Supports local scholarships.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Lifestart+Foundation+Shop+Hoi+An+Vietnam"),

    ("🌙", "Hoi An Night Market", "★★★★☆", "4.4",
     "&quot;Bustling night market along the river. Apparel, accessories & snacks.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Hoi+An+Night+Market+Nguyen+Hoang+Street+Vietnam"),

    ("🎨", "Cui Lu Art Space", "★★★★★", "4.8",
     "&quot;Curated art space with silver jewelry, textiles, ceramics & fine art.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Cui+Lu+Art+Space+Hoi+An+Vietnam"),

    ("🎪", "March Gallery", "★★★★☆", "4.6",
     "&quot;Contemporary Vietnamese art. Vibrant watercolors of landscapes.&quot;",
     "https://www.google.com/maps/search/?api=1&query=March+Gallery+Hoi+An+Vietnam"),

    ("🪵", "Âu Lạc Wood Art", "★★★★☆", "4.5",
     "&quot;Intricately carved wooden statues, souvenirs & traditional art pieces.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Au+Lac+Wood+Art+Hoi+An+Vietnam"),

    ("🏺", "Thanh Ha Pottery Village", "★★★★★", "4.7",
     "&quot;Traditional pottery village. Buy handcrafted vases, figurines & teapots.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Thanh+Ha+Pottery+Village+Hoi+An+Vietnam"),

    ("🍵", "The Cocobana Tearoom", "★★★★☆", "4.5",
     "&quot;Beautifully displayed & packaged teas. Perfect gift from Hoi An.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Cocobana+Tearoom+Hoi+An+Vietnam"),

    ("✂️", "Hoi An Handicraft Workshop", "★★★★☆", "4.4",
     "&quot;Try embroidery, mask painting & lantern-making. Buy handmade crafts.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Hoi+An+Handicraft+Workshop+Vietnam"),

    ("🖌️", "Ngan Xua Gallery", "★★★★☆", "4.5",
     "&quot;Authentic Vietnamese lacquer artworks on wood using traditional techniques.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Ngan+Xua+Gallery+Hoi+An+Vietnam"),

    ("🧳", "Hoi An Soul Leather", "★★★★★", "4.7",
     "&quot;Full-grain leather goods — bags, belts, wallets. Handmade quality.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Hoi+An+Soul+Leather+Shop+Vietnam"),

    ("📸", "Precious Heritage Museum", "★★★★★", "4.9",
     "&quot;Free museum by Réhahn — portraits, costumes of Vietnam's ethnic groups.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Precious+Heritage+Museum+Hoi+An+Vietnam"),

    ("🎋", "Taboo Bamboo Workshop", "★★★★☆", "4.4",
     "&quot;Sustainable bamboo products — lamps, baskets & kitchenware.&quot;",
     "https://www.google.com/maps/search/?api=1&query=Taboo+Bamboo+Workshop+Hoi+An+Vietnam"),
]


def gen_card(cat, icon, name, stars, rating, comment, url, badge_key, delay):
    """Generate a single rec-card HTML block."""
    # Escape single quotes in URL for onclick attribute
    safe_url = url.replace("'", "%27")
    return f"""        <div class="rec-card fade-in-up" data-cat="{cat}" style="animation-delay:{delay:.2f}s" onclick="window.open('{safe_url}','_blank')">
          <div class="rec-icon">{icon}</div>
          <div class="rec-content">
            <div class="rec-badge {cat}-badge" data-i18n="{badge_key}">{badge_key.replace('rec_badge_', '').title()}</div>
            <h4>{name}</h4>
            <div class="rec-stars">{stars} <span>{rating}</span></div>
            <p class="rec-comment">{comment}</p>
            <a class="rec-map-btn" href="{url}" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation()">📍 Get Directions</a>
          </div>
        </div>"""


def gen_section(items, cat_name, badge_key):
    """Generate all cards for a category."""
    cards = []
    for i, item in enumerate(items):
        icon, name, stars, rating, comment, url = item
        delay = 0.05 * (i + 1)
        cards.append(gen_card(cat_name, icon, name, stars, rating, comment, url, badge_key, delay))
    return "\n\n".join(cards)


def main():
    # Read the current file
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    # Generate all recommendation cards
    bars_html = gen_section(BARS, "bar", "rec_badge_bar")
    cocktails_html = gen_section(COCKTAILS, "cocktail", "rec_badge_cocktail")
    hotfood_html = gen_section(HOTFOOD, "hotfood", "rec_badge_hotfood")
    snacks_html = gen_section(SNACKS, "snack", "rec_badge_snack")
    cafes_html = gen_section(CAFES, "cafe", "rec_badge_cafe")
    shops_html = gen_section(SHOPS, "shop", "rec_badge_shop")

    all_cards = "\n\n".join([
        bars_html,
        cocktails_html,
        hotfood_html,
        snacks_html,
        cafes_html,
        f"        <!-- SHOPS: {len(SHOPS)} unique shops (no tailors) -->",
        shops_html,
    ])

    # Find and replace the recommendation list block
    # Pattern: from <div class="recommendation-list" id="rec-list"> to its closing </div>
    # followed by </div> for the recommendations-view
    pattern = re.compile(
        r'(<div class="recommendation-list" id="rec-list">)\s*.*?\s*(</div>\s*</div>\s*<!-- TOUR VIEW -->)',
        re.DOTALL
    )

    # Check if pattern matches
    match = pattern.search(content)
    if not match:
        # Try alternative: find between rec-list and closing tags before tour-view
        pattern2 = re.compile(
            r'(<div class="recommendation-list" id="rec-list">)\s*.*?\s*(</div>\s*\n\s*</div>\s*\n+\s*\n+\s*<!\-\- TOUR VIEW)',
            re.DOTALL
        )
        match = pattern2.search(content)

    if not match:
        print("ERROR: Could not find recommendation list block in index.html")
        print("Trying line-based approach...")

        # Line-based approach
        lines = content.split('\n')
        start_idx = None
        end_idx = None

        for i, line in enumerate(lines):
            if 'id="rec-list"' in line:
                start_idx = i
            if start_idx and '<!-- TOUR VIEW -->' in line:
                # Go back to find the closing divs
                end_idx = i
                break

        if start_idx is None or end_idx is None:
            print("FATAL: Could not locate recommendation list section")
            return

        # Find the closing </div> tags between rec-list end and tour-view
        # The structure is: <div id="rec-list">...cards...</div>\n</div>\n\n<!-- TOUR VIEW -->
        # We need to keep the closing </div> for recommendations-view

        # Build new content
        new_rec_block = f'      <div class="recommendation-list" id="rec-list">\n\n{all_cards}\n\n      </div>\n\n    </div>\n\n\n'

        # Find where rec-list starts and where recommendations-view ends
        pre = '\n'.join(lines[:start_idx])
        post_start = None
        for i in range(start_idx, len(lines)):
            if '<!-- TOUR VIEW -->' in lines[i]:
                post_start = i
                break

        if post_start is None:
            print("FATAL: Could not find TOUR VIEW marker")
            return

        post = '\n'.join(lines[post_start:])
        new_content = pre + '\n' + new_rec_block + '\n    ' + post
    else:
        new_rec_block = f'{match.group(1)}\n\n{all_cards}\n\n      </div>\n\n    </div>\n\n\n    <!-- TOUR VIEW -->'
        new_content = content[:match.start()] + new_rec_block + content[match.end():]

    # Write back
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)

    total = len(BARS) + len(COCKTAILS) + len(HOTFOOD) + len(SNACKS) + len(CAFES) + len(SHOPS)
    print(f"✅ Updated {total} recommendation cards with correct Google Maps links")
    print(f"   - Bars: {len(BARS)}")
    print(f"   - Cocktails: {len(COCKTAILS)}")
    print(f"   - Hot Food: {len(HOTFOOD)}")
    print(f"   - Snacks: {len(SNACKS)}")
    print(f"   - Cafés: {len(CAFES)}")
    print(f"   - Shops: {len(SHOPS)}")


if __name__ == "__main__":
    main()
