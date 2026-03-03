import json
import re
import os

with open(r'd:\project\booking\tours_part1.json', 'r', encoding='utf-8') as f:
    tours1 = json.load(f)
with open(r'd:\project\booking\tours_part2.json', 'r', encoding='utf-8') as f:
    tours2 = json.load(f)

ALL_TOURS = {**tours1, **tours2}

cards_html = []

# Exact old 5 cards first
old_5 = """
        <!-- Tour 1: Cham Island Snorkeling -->
        <div class="tour-card fade-in-up" data-region="hoian" style="animation-delay: 0.1s;" onclick="openTourModal('t07')">
          <div class="tour-badge">🌟 Popular</div>
          <div class="tour-image-container">
            <img src="cham_island.png" alt="Cham Island Snorkeling Daily Tour">
          </div>
          <div class="tour-info">
            <h3>Cham Island Snorkeling Daily Tour</h3>
            <p>Explore the stunning biosphere reserve. Includes speedboat, snorkeling at Bai Xep (45 mins), and a fresh seafood BBQ lunch on the island.</p>
            <div class="tour-meta">
              <div class="tour-meta-item">⏱ Full Day</div>
              <div class="tour-meta-item">📍 Cham Island</div>
              <div class="tour-meta-item">🌊 Snorkeling</div>
            </div>
          </div>
          <div class="tour-card-click-hint">Tap for full details →</div>
        </div>

        <!-- Tour 2: Cam Thanh Basket Boat -->
        <div class="tour-card fade-in-up" data-region="hoian" style="animation-delay: 0.2s;" onclick="openTourModal('t14')">
          <div class="tour-badge">🎭 Culture</div>
          <div class="tour-image-container">
            <img src="basket_boat.png" alt="Cam Thanh Village & Basket Boat">
          </div>
          <div class="tour-info">
            <h3>Cam Thanh Village &amp; Basket Boat</h3>
            <p>Navigate the lush coconut waterways in a traditional bamboo basket boat. Experience crab catching and local fishing techniques.</p>
            <div class="tour-meta">
              <div class="tour-meta-item">⏱ Half Day</div>
              <div class="tour-meta-item">📍 Coconut Forest</div>
              <div class="tour-meta-item">🛶 Adventure</div>
            </div>
          </div>
          <div class="tour-card-click-hint">Tap for full details →</div>
        </div>

        <!-- Tour 3: Ba Na Hills -->
        <div class="tour-card fade-in-up" data-region="danang" style="animation-delay: 0.3s;" onclick="openTourModal('t27')">
          <div class="tour-badge">✨ Must See</div>
          <div class="tour-image-container">
            <img src="golden_bridge.png" alt="Ba Na Hills & Golden Bridge">
          </div>
          <div class="tour-info">
            <h3>Ba Na Hills &amp; Golden Bridge</h3>
            <p>Ride the world's longest cable car to the iconic 'Hands of God' bridge. Explore the French Village and enjoy panoramic mountain views.</p>
            <div class="tour-meta">
              <div class="tour-meta-item">⏱ Full Day</div>
              <div class="tour-meta-item">📍 Da Nang</div>
              <div class="tour-meta-item">🚠 Cable Car</div>
            </div>
          </div>
          <div class="tour-card-click-hint">Tap for full details →</div>
        </div>

        <!-- Tour 4: Hoi An City -->
        <div class="tour-card fade-in-up" data-region="hoian" style="animation-delay: 0.4s;" onclick="openTourModal('t16')">
          <div class="tour-badge">🏮 Authentic</div>
          <div class="tour-image-container">
            <img src="hoi_an_town.png" alt="Hoi An City, Boat & Street Food">
          </div>
          <div class="tour-info">
            <h3>Hoi An City, Boat &amp; Street Food</h3>
            <p>Discover the ancient town's secrets, enjoy a romantic flower lantern boat ride, and taste famous local specialties like Banh Mi &amp; Cao Lau.</p>
            <div class="tour-meta">
              <div class="tour-meta-item">⏱ Afternoon</div>
              <div class="tour-meta-item">📍 Old Town</div>
              <div class="tour-meta-item">🍜 Foodie</div>
            </div>
          </div>
          <div class="tour-card-click-hint">Tap for full details →</div>
        </div>

        <!-- Tour 5: My Son Sanctuary -->
        <div class="tour-card fade-in-up" data-region="hoian" style="animation-delay: 0.5s;" onclick="openTourModal('t25')">
          <div class="tour-badge">🏛️ History</div>
          <div class="tour-image-container">
            <img src="my_son.png" alt="My Son Sanctuary Discovery">
          </div>
          <div class="tour-info">
            <h3>My Son Sanctuary Discovery</h3>
            <p>Journey to the spiritual heart of the Champa Kingdom. Explore ancient Hindu temples nestled in a lush valley with an expert guide.</p>
            <div class="tour-meta">
              <div class="tour-meta-item">⏱ 5-6 hours</div>
              <div class="tour-meta-item">📍 Duy Xuyen</div>
              <div class="tour-meta-item">🏛️ UNESCO</div>
            </div>
          </div>
          <div class="tour-card-click-hint">Tap for full details →</div>
        </div>
"""
cards_html.append(old_5)

skip_keys = {'t07', 't14', 't27', 't16', 't25'}

delay = 0.6
for key, tour in ALL_TOURS.items():
    if key in skip_keys:
        continue
    
    meta_html = ""
    for icon, text in tour['meta']:
        meta_html += f'<div class="tour-meta-item">{icon} {text}</div>\n              '
    
    card = f"""
        <!-- {key} -->
        <div class="tour-card fade-in-up hidden" data-region="{tour['region']}" style="animation-delay: 0.0s;" onclick="openTourModal('{key}')">
          <div class="tour-badge">{tour['badge']}</div>
          <div class="tour-image-container">
            <img src="{tour.get('image', 'hoi_an_town.png')}" alt="{tour['title'].replace('"', '&quot;')}">
          </div>
          <div class="tour-info">
            <h3>{tour['title']}</h3>
            <p>{tour['desc_card']}</p>
            <div class="tour-meta">
              {meta_html.strip()}
            </div>
          </div>
          <div class="tour-card-click-hint">Tap for full details →</div>
        </div>
"""
    cards_html.append(card)

full_html_cards = "\n".join(cards_html)

# Generate JS Object
js_obj = "const TOUR_DATA = {\n"
for key, tour in ALL_TOURS.items():
    js_obj += f"    '{key}': {json.dumps(tour, ensure_ascii=False)},\n"
js_obj += "  };"

html_path = r'd:\project\booking\sontra-villa\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace cards 
# find <div class="tour-list" id="tour-card-container"> or similar. Wait, it's just <div class="tour-list">
# Let's replace everything between <div class="tour-list"> and exactly before </div>\n    </div>\n\n  </div>\n\n  <!-- ===== TOUR DETAIL MODALS ===== -->
list_pattern = re.compile(r'(<div class="tour-list"[^>]*>)(.*?)(</div>\s*</div>\s*</div>\s*<!-- ===== TOUR DETAIL MODALS ===== -->)', re.DOTALL)
if list_pattern.search(content):
    content = list_pattern.sub(r'\1\n' + full_html_cards + r'\n      \3', content)
else:
    print("Could not find <div class='tour-list'> block via first regex, trying alternative...")
    # simpler block: <div class="tour-list"> to the end of that div (which is followed by </div> </div> </div>)
    alt_pattern = re.compile(r'(<div class="tour-list">).*?(</div>\s*</div>\s*</div>\s*<!-- ===== TOUR DETAIL MODALS)', re.DOTALL)
    if alt_pattern.search(content):
        content = alt_pattern.sub(r'\1\n' + full_html_cards + r'\n      \2', content)
    else:
        print("Still could not find <div class='tour-list'> block.")

# Replace JS
# const TOUR_DATA = { ... };
js_pattern = re.compile(r'const TOUR_DATA = \{.*?\n  \};', re.DOTALL)
if js_pattern.search(content):
    content = js_pattern.sub(js_obj, content)
else:
    print("Could not find TOUR_DATA block.")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully generated 40 tours to {html_path}")
