#!/usr/bin/env python3
"""
Fix Google Maps links in Local Recommendations section of index.html.
VERSION 2: Uses EXACT Google Maps Search API format for ALL venues
(`https://www.google.com/maps/search/?api=1&query={Exact_Name}+Hoi+An+Vietnam`)
Also features the Top 10 Bars from TripAdvisor.
"""

import re
import urllib.parse

# Format: (icon, name, stars, rating, comment)

BARS = [
    # --- Top 10 TripAdvisor Bars ---
    ("🎸", "Guitar Hawaii Hoi An Live Music Bar", "★★★★★", "5.0", "&quot;Top-rated live music venue with amazing local talent.&quot;"),
    ("🍸", "Hair Of The Dog Bar Hoi An", "★★★★☆", "4.5", "&quot;Vibrant night market bar, great crowd, perfect to party.&quot;"),
    ("🌇", "The Deck Rooftop Bar Hoi An", "★★★★★", "5.0", "&quot;Stunning panoramic views of Hoi An, incredible cocktails.&quot;"),
    ("🍹", "Mezcal Cocteleria", "★★★★★", "5.0", "&quot;Authentic Mexican mezcal bar with phenomenal mixology.&quot;"),
    ("🪩", "New 92 Club", "★★★★☆", "4.5", "&quot;Energetic club atmosphere for dancing the night away.&quot;"),
    ("🍻", "Woop Woop Bar", "★★★★★", "5.0", "&quot;Friendly Australian-style bar with cold beers and great vibes.&quot;"),
    ("🎉", "Why Not Club Bar Hoi An", "★★★★☆", "4.3", "&quot;Legendary party spot on the main strip. Open late, cheap drinks.&quot;"),
    ("🌴", "Serendipity Hoi An", "★★★★★", "5.0", "&quot;Hidden gem with a relaxed atmosphere and excellent service.&quot;"),
    ("🤪", "Mr Tom Crazy Bar", "★★★★☆", "4.5", "&quot;Fun, eccentric bar with quirky drinks and a very lively crowd.&quot;"),
    ("🍷", "MAJI KA", "★★★★☆", "4.5", "&quot;Cozy spot for late night drinks in the heart of the ancient town.&quot;"),

    # --- Other Great Bars ---
    ("🍺", "Market Bar", "★★★★★", "4.8", "&quot;Amazing rooftop vibe overlooking the Central Market.&quot;"),
    ("🌊", "Shore Club An Bang", "★★★★★", "4.9", "&quot;Best beach club in the area. Pool, cocktails, watch the sea.&quot;"),
    ("🎸", "Q Bar Hoi An", "★★★★☆", "4.6", "&quot;Laid-back atmosphere, signature cocktails in a gorgeous lounge.&quot;"),
    ("🏮", "White Marble Wine Bar", "★★★★★", "4.7", "&quot;Sophisticated wine selection, intimate setting.&quot;"),
    ("🌙", "Dive Bar Hoi An", "★★★★☆", "4.5", "&quot;Funky dive bar, cheap buckets, pool table, very social crowd.&quot;"),
    ("🎶", "Tiger Tiger Bar", "★★★★☆", "4.5", "&quot;Great live music venue with affordable drinks. Lively atmosphere.&quot;"),
    ("🥃", "Mia Coffee", "★★★★★", "4.6", "&quot;Hidden gem near the river. Amazing sunset cocktails and chill music.&quot;"),
    ("🎤", "Tam Tam Cafe Lounge", "★★★★☆", "4.4", "&quot;Two-story colonial bar with live jazz and classic cocktails.&quot;"),
]

COCKTAILS = [
    ("🍸", "Mango Mango", "★★★★★", "4.8", "&quot;Riverside setting, creative tropical cocktails, lantern reflections.&quot;"),
    ("🥂", "Before and Now Bar", "★★★★★", "4.9", "&quot;The best cocktails in Hoi An. Creative drinks, stunning presentation.&quot;"),
    ("🌴", "Soluna D'Annam", "★★★★☆", "4.6", "&quot;Chill lounge vibes, Vietnamese-inspired cocktails, try the lychee mojito!&quot;"),
    ("🍋", "Bitter Sweet Cocktail Bar", "★★★★★", "4.7", "&quot;Small intimate craft cocktail bar. Every drink is a work of art.&quot;"),
    ("🫧", "The Field Bar", "★★★★☆", "4.5", "&quot;Open-air bar in a rice paddy setting. Signature gin cocktails.&quot;"),
    ("🌺", "The Little Menu", "★★★★★", "4.7", "&quot;Tiny hidden speakeasy with incredible molecular cocktails.&quot;"),
    ("🍊", "Son Cocktail Bar", "★★★★☆", "4.5", "&quot;Rooftop views with Vietnamese-twist cocktails. Try lemongrass gimlet.&quot;"),
    ("🧊", "Sakura Bar Hoi An", "★★★★☆", "4.4", "&quot;Japanese-inspired cocktail lounge. Excellent sake-based cocktails.&quot;"),
]

HOTFOOD = [
    ("🥖", "Banh Mi Phuong", "★★★★★", "4.9", "&quot;Anthony Bourdain called it the best sandwich ever. Essential Hoi An.&quot;"),
    ("🍲", "Morning Glory Original", "★★★★★", "4.8", "&quot;Cao Lau and White Rose are life-changing here. Heritage setting.&quot;"),
    ("🍜", "Pho Xua", "★★★★★", "4.7", "&quot;Traditional pho in old Hoi An style. Secret family recipe.&quot;"),
    ("🥢", "Nu Eatery", "★★★★★", "4.8", "&quot;Modern Vietnamese tapas. Every small plate is a flavor explosion.&quot;"),
    ("🥬", "Quan Com Chay An Nhien", "★★★★☆", "4.5", "&quot;Best vegetarian restaurant in town. Healthy and affordable.&quot;"),
    ("🥖", "Madam Khanh - The Banh Mi Queen", "★★★★★", "4.8", "&quot;Queue up — it's always worth it for this crispy banh mi.&quot;"),
    ("🍲", "Cao Lau Thanh", "★★★★★", "4.7", "&quot;One of the best Cao Lau in Hoi An. Smoky noodles, crispy croutons.&quot;"),
    ("🍗", "Ba Buoi Chicken Rice", "★★★★★", "4.8", "&quot;Hoi An's iconic com ga. Turmeric rice, shredded chicken, perfection.&quot;"),
    ("🫔", "Bale Well", "★★★★★", "4.7", "&quot;DIY spring rolls with grilled pork. Local hidden gem, no menu.&quot;"),
    ("🍜", "Com Ga Ba Nga", "★★★★☆", "4.6", "&quot;Another great chicken rice spot. Tender chicken, yellow rice.&quot;"),
    ("🍝", "Mi Quang Ong Hai", "★★★★★", "4.7", "&quot;Legendary Mi Quang — turmeric noodles, shrimp, pork, peanuts.&quot;"),
    ("🍽️", "Vy's Market Restaurant", "★★★★☆", "4.5", "&quot;Cooking class + restaurant. Try every Hoi An specialty.&quot;"),
    ("🍛", "Streets Restaurant", "★★★★★", "4.7", "&quot;Social enterprise restaurant training street kids. Incredible food.&quot;"),
    ("🥟", "White Rose Restaurant", "★★★★☆", "4.6", "&quot;Home of the famous White Rose dumplings. Must-try Hoi An dish.&quot;"),
    ("🍜", "Mot Hoi An", "★★★★★", "4.7", "&quot;Modern Vietnamese fine dining. Beautiful presentation, local flavors.&quot;"),
    ("🥬", "Minh Hien Vegetarian", "★★★★☆", "4.5", "&quot;Delicious Buddhist vegetarian food. Generous portions, low prices.&quot;"),
    ("🌿", "Secret Garden Restaurant", "★★★★☆", "4.6", "&quot;Hidden garden dining with traditional Vietnamese home cooking.&quot;"),
    ("🥗", "Baby Mustard Restaurant", "★★★★☆", "4.5", "&quot;Local favorites — try the baby mustard greens and com ga.&quot;"),
    ("🍵", "Tam Tam Cafe Restaurant", "★★★★☆", "4.4", "&quot;French-Vietnamese heritage restaurant. Great for lunch on balcony.&quot;"),
    ("🍖", "Dac San Tran Restaurant", "★★★★☆", "4.5", "&quot;Traditional Hoi An dishes — com ga, cao lau served family style.&quot;"),
    ("🍲", "Pho Hung Hoi An", "★★★★☆", "4.4", "&quot;Simple, perfect pho. Beef or chicken. Early morning breakfast spot.&quot;"),
    ("🥞", "Banh Xeo Ba Le", "★★★★★", "4.6", "&quot;Crispy Vietnamese crepes. Huge portions, dip in fish sauce.&quot;"),
    ("🥬", "Lien Hoa Restaurant", "★★★★☆", "4.3", "&quot;Vegetarian buffet-style. Great variety, very affordable prices.&quot;"),
    ("🥟", "Banh Cuon Hoi An", "★★★★☆", "4.5", "&quot;Steamed rice rolls with minced pork. Light and delicious.&quot;"),
]

SNACKS = [
    ("☕", "Hoi An Roastery", "★★★★★", "4.7", "&quot;Local specialty coffee roasters. Try egg coffee or coconut coffee.&quot;"),
    ("🥟", "Banh Bao Banh Vac White Rose", "★★★★★", "4.8", "&quot;Original White Rose dumpling workshop. Buy fresh, see them made.&quot;"),
    ("🥜", "Phuoc Thanh Nuts", "★★★★☆", "4.5", "&quot;Roasted peanuts, cashews, dried fruits. Great for gifts.&quot;"),
    ("🍰", "Cargo Club Patisserie", "★★★★★", "4.6", "&quot;French pastries, cakes and brunch. Riverside balcony seating.&quot;"),
    ("🍨", "Coco Box Ice Cream", "★★★★☆", "4.5", "&quot;Homemade Vietnamese-inspired ice cream. Coconut flavor is the best.&quot;"),
    ("🧆", "Hoi An Central Market Food Stalls", "★★★★★", "4.7", "&quot;Street food paradise. Fresh spring rolls, banh mi, che desserts.&quot;"),
    ("🍧", "Che Hoi An Dessert Soup", "★★★★☆", "4.4", "&quot;Traditional Vietnamese dessert soup. Colorful, sweet, refreshing.&quot;"),
    ("🥤", "Sinh To Stand An Bang", "★★★★☆", "4.6", "&quot;Fresh tropical smoothies on the beach. Mango, passion fruit.&quot;"),
    ("🍮", "Banh Flan Hoi An", "★★★★☆", "4.4", "&quot;Vietnamese caramel custard with strong coffee. Afternoon treat.&quot;"),
    ("🧇", "Banh Trang Nuong", "★★★★☆", "4.5", "&quot;Vietnamese pizza! Grilled rice paper with egg and chili sauce.&quot;"),
    ("🥭", "Mango Rooms", "★★★★★", "4.7", "&quot;Creative mango desserts riverside. Mango sticky rice is divine.&quot;"),
    ("🍪", "Reaching Out Tea House", "★★★★★", "4.8", "&quot;Silent tea house run by deaf artisans. Beautiful teas and cookies.&quot;"),
]

CAFES = [
    ("☕", "Rosie Cafe", "★★★★★", "4.8", "&quot;Instagram-worthy coffeeshop with amazing breakfast and gorgeous decor.&quot;"),
    ("🍵", "The Espresso Station", "★★★★★", "4.7", "&quot;Best specialty coffee in Hoi An. Single origin beans, expert baristas.&quot;"),
    ("🫖", "Faifo Coffee", "★★★★☆", "4.6", "&quot;Rooftop cafe with panoramic old town views. Great sunset coffee.&quot;"),
    ("🧋", "Co Muoi Cafe", "★★★★☆", "4.5", "&quot;Hidden garden cafe in ancient town. Peaceful oasis, coconut coffee.&quot;"),
    ("☕", "Mot Coffee", "★★★★★", "4.7", "&quot;Trendy modern cafe with excellent cold brew and healthy bowls.&quot;"),
    ("🍵", "U Cafe Hoi An", "★★★★☆", "4.6", "&quot;Riverside cafe with hammocks and lantern views. Super chill vibes.&quot;"),
    ("🫖", "An Bang Hideaway Cafe", "★★★★☆", "4.5", "&quot;Beach cafe with fresh juices and smoothie bowls. After a swim.&quot;"),
    ("☕", "Sound of Silence Coffee", "★★★★★", "4.8", "&quot;Run by deaf baristas. Order via menu cards. Meaningful experience.&quot;"),
    ("🧋", "The Deck House An Bang", "★★★★☆", "4.6", "&quot;Beachside cafe with great coffee and cocktails. Lovely sunset.&quot;"),
    ("☕", "Cocobox", "★★★★★", "4.7", "&quot;Organic coffee and smoothie bowls. Beautiful coconut theme decor.&quot;"),
]

SHOPS = [
    ("🏮", "Reaching Out Arts & Crafts", "★★★★★", "4.9", "&quot;Magical shop staffed by deaf artisans. Handmade silk lanterns.&quot;"),
    ("🛒", "Hoi An Central Market", "★★★★☆", "4.5", "&quot;Heart of Hoi An. Fresh produce, handicrafts, spices, street food.&quot;"),
    ("🌸", "Tra Que Herb Village", "★★★★★", "4.7", "&quot;Fresh herbs, organic teas and natural skincare from the village.&quot;"),
    ("📿", "Hoi An Handmade Souvenirs", "★★★★☆", "4.3", "&quot;Handwoven baskets, lacquerware, ceramic bowls, embroidered pouches.&quot;"),
    ("🪭", "Metiseko Boutique", "★★★★☆", "4.6", "&quot;Eco-friendly fashion with Vietnamese prints. Beautiful silk scarves.&quot;"),
    ("🎭", "Hoi An Lantern Company", "★★★★☆", "4.5", "&quot;Handmade silk lanterns in every color and shape. Ships worldwide.&quot;"),
    ("🖼️", "Rehahn Art Gallery", "★★★★★", "4.9", "&quot;Stunning fine-art photography of Vietnam's 54 ethnic groups.&quot;"),
    ("👞", "Friendly Shoe Leather Shop", "★★★★★", "4.8", "&quot;Custom-made leather shoes, bags & jackets. High quality craftsmanship.&quot;"),
    ("👜", "Blue Lotus Leather", "★★★★☆", "4.6", "&quot;Wide range of leather products — shoes, bags, wallets, jackets.&quot;"),
    ("🎒", "Da Bao Real Leather", "★★★★★", "4.7", "&quot;One of the oldest leather boutiques. 100% real buffalo leather goods.&quot;"),
    ("🎁", "Cocobox Shop", "★★★★☆", "4.5", "&quot;Beautifully packaged made-in-Vietnam goodies, coffee & coconut products.&quot;"),
    ("💎", "Cotic", "★★★★★", "4.7", "&quot;Art installations, essential oils, silver jewelry in a stunning old building.&quot;"),
    ("🧶", "Mekong Quilts", "★★★★★", "4.8", "&quot;Beautiful bedding handmade by disadvantaged women. Social enterprise.&quot;"),
    ("🧸", "Lifestart Foundation Shop", "★★★★☆", "4.6", "&quot;Handmade toys & body lotions. Supports local scholarships.&quot;"),
    ("🌙", "Hoi An Night Market Nguyen Hoang Street", "★★★★☆", "4.4", "&quot;Bustling night market along the river. Apparel, accessories & snacks.&quot;"),
    ("🎨", "Cui Lu Art Space", "★★★★★", "4.8", "&quot;Curated art space with silver jewelry, textiles, ceramics & fine art.&quot;"),
    ("🎪", "March Gallery", "★★★★☆", "4.6", "&quot;Contemporary Vietnamese art. Vibrant watercolors of landscapes.&quot;"),
    ("🪵", "Au Lac Wood Art", "★★★★☆", "4.5", "&quot;Intricately carved wooden statues, souvenirs & traditional art pieces.&quot;"),
    ("🏺", "Thanh Ha Pottery Village", "★★★★★", "4.7", "&quot;Traditional pottery village. Buy handcrafted vases, figurines & teapots.&quot;"),
    ("🍵", "Cocobana Tearoom", "★★★★☆", "4.5", "&quot;Beautifully displayed & packaged teas. Perfect gift from Hoi An.&quot;"),
    ("✂️", "Hoi An Handicraft Workshop", "★★★★☆", "4.4", "&quot;Try embroidery, mask painting & lantern-making. Buy handmade crafts.&quot;"),
    ("🖌️", "Ngan Xua Gallery", "★★★★☆", "4.5", "&quot;Authentic Vietnamese lacquer artworks on wood using traditional techniques.&quot;"),
    ("🧳", "Hoi An Soul Leather Shop", "★★★★★", "4.7", "&quot;Full-grain leather goods — bags, belts, wallets. Handmade quality.&quot;"),
    ("📸", "Precious Heritage Museum", "★★★★★", "4.9", "&quot;Free museum by Réhahn — portraits, costumes of Vietnam's ethnic groups.&quot;"),
    ("🎋", "Taboo Bamboo Workshop", "★★★★☆", "4.4", "&quot;Sustainable bamboo products — lamps, baskets & kitchenware.&quot;"),
]


def gen_card(cat, icon, name, stars, rating, comment, badge_key, delay):
    """Generate a single rec-card HTML block using proper Search URL formatting."""
    # Build exact Google Maps Search API query string 
    # e.g., "Guitar Hawaii Hoi An Live Music Bar Hoi An Vietnam"
    search_query = f"{name} Hoi An Vietnam"
    safe_query = urllib.parse.quote_plus(search_query)
    final_url = f"https://www.google.com/maps/search/?api=1&query={safe_query}"
    
    return f"""        <div class="rec-card fade-in-up" data-cat="{cat}" style="animation-delay:{delay:.2f}s" onclick="window.open('{final_url}','_blank')">
          <div class="rec-icon">{icon}</div>
          <div class="rec-content">
            <div class="rec-badge {cat}-badge" data-i18n="{badge_key}">{badge_key.replace('rec_badge_', '').title()}</div>
            <h4>{name}</h4>
            <div class="rec-stars">{stars} <span>{rating}</span></div>
            <p class="rec-comment">{comment}</p>
            <a class="rec-map-btn" href="{final_url}" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation()">📍 Get Directions</a>
          </div>
        </div>"""


def gen_section(items, cat_name, badge_key):
    """Generate all cards for a category."""
    cards = []
    for i, item in enumerate(items):
        icon, name, stars, rating, comment = item
        delay = 0.05 * (i + 1)
        cards.append(gen_card(cat_name, icon, name, stars, rating, comment, badge_key, delay))
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
    pattern = re.compile(
        r'(<div class="recommendation-list" id="rec-list">)\s*.*?\s*(</div>\s*</div>\s*<!-- TOUR VIEW -->)',
        re.DOTALL
    )

    match = pattern.search(content)
    if not match:
        pattern2 = re.compile(
            r'(<div class="recommendation-list" id="rec-list">)\s*.*?\s*(</div>\s*\n\s*</div>\s*\n+\s*\n+\s*<!\-\- TOUR VIEW)',
            re.DOTALL
        )
        match = pattern2.search(content)

    if match:
        new_rec_block = f'{match.group(1)}\n\n{all_cards}\n\n      </div>\n\n    </div>\n\n\n    <!-- TOUR VIEW -->'
        new_content = content[:match.start()] + new_rec_block + content[match.end():]
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(new_content)
        
        total = len(BARS) + len(COCKTAILS) + len(HOTFOOD) + len(SNACKS) + len(CAFES) + len(SHOPS)
        print(f"✅ Updated {total} recommendation cards with exact Google Maps URLs")
        print("  - Search Format: https://www.google.com/maps/search/?api=1&query={Name}+Hoi+An+Vietnam")
    else:
        print("ERROR: Could not locate recommendation list section inside index.html")

if __name__ == "__main__":
    main()
