"""
Update tour cards in index.html to replace single-image containers with 
swipeable gallery sliders using the correct docx images.
Also add necessary CSS and JS to style.css and script.js.
"""
import re

html_path = r"c:\Users\TranHuy_WIN\Desktop\booking-vietnam\sontra-villa\index.html"
css_path = r"c:\Users\TranHuy_WIN\Desktop\booking-vietnam\sontra-villa\style.css"
js_path = r"c:\Users\TranHuy_WIN\Desktop\booking-vietnam\sontra-villa\script.js"

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# ============================================================
# Map of tour IDs to their gallery images (docx-based)
# ============================================================
TOUR_GALLERY = {
    # Cham Island
    't07':  ['picture/docx_cham1.png', 'picture/docx_cham2.png', 'picture/docx_cham3.png'],
    't08':  ['picture/docx_cham1.png', 'picture/docx_cham2.png', 'picture/docx_cham3.png'],
    't09':  ['picture/docx_cham1.png', 'picture/docx_cham2.png', 'picture/docx_cham3.png'],
    't10':  ['picture/docx_cham1.png', 'picture/docx_cham2.png', 'picture/docx_cham3.png'],
    't11':  ['picture/docx_cham1.png', 'picture/docx_cham2.png', 'picture/docx_cham3.png'],
    't12':  ['picture/docx_cham1.png', 'picture/docx_cham2.png', 'picture/docx_cham3.png'],
    't13':  ['picture/docx_cham1.png', 'picture/docx_cham2.png', 'picture/docx_cham3.png'],
    # Cam Thanh / Bay Mau 
    't14':  ['picture/docx_camthanh1.png', 'picture/docx_camthanh2.png', 'picture/docx_camthanh3.png'],
    't15':  ['picture/docx_camthanh1.png', 'picture/docx_camthanh2.png', 'picture/docx_camthanh3.png'],
    't17':  ['picture/docx_camthanh1.png', 'picture/docx_camthanh2.png', 'picture/docx_camthanh3.png'],
    't18':  ['picture/docx_camthanh1.png', 'picture/docx_camthanh2.png', 'picture/docx_camthanh3.png'],
    't22':  ['picture/docx_camthanh1.png', 'picture/docx_camthanh2.png', 'picture/docx_camthanh3.png'],
    't23':  ['picture/docx_camthanh1.png', 'picture/docx_camthanh2.png', 'picture/docx_camthanh3.png'],
    't38':  ['picture/docx_camthanh1.png', 'picture/docx_camthanh2.png', 'picture/docx_camthanh3.png'],
    't39':  ['picture/docx_camthanh1.png', 'picture/docx_camthanh2.png', 'picture/docx_camthanh3.png'],
    't40':  ['picture/docx_camthanh1.png', 'picture/docx_camthanh2.png', 'picture/docx_camthanh3.png'],
    # My Son
    't24':  ['picture/docx_myson1.png', 'picture/docx_myson2.png', 'picture/docx_myson3.png'],
    't25':  ['picture/docx_myson1.png', 'picture/docx_myson2.png', 'picture/docx_myson3.png'],
    't26':  ['picture/docx_myson1.png', 'picture/docx_myson2.png', 'picture/docx_myson3.png'],
    # Buffalo / Cycling
    't03':  ['picture/docx_buffalo1.png', 'picture/docx_buffalo2.png', 'picture/docx_buffalo3.png'],
    't21':  ['picture/docx_buffalo1.png', 'picture/docx_buffalo2.png', 'picture/docx_buffalo3.png'],
    # Basket Boat / Lantern cooking
    't01':  ['picture/docx_basket1.png', 'picture/docx_basket2.png'],
    't04':  ['picture/docx_basket1.png', 'picture/docx_basket2.png'],
    't05':  ['picture/docx_basket1.png', 'picture/docx_basket2.png'],
    't06':  ['picture/docx_basket1.png', 'picture/docx_basket2.png'],
    # Lantern + Tra Que
    't19':  ['picture/docx_lantern1.png', 'picture/docx_lantern2.png'],
    't20':  ['picture/docx_lantern1.png', 'picture/docx_lantern2.png'],
    # Monkey Mountain (without Hell Cave): Monkey+Marble+HoiAn Night / Monkey+Marble+MySon
    't30':  ['picture/docx_monkey1.png', 'picture/docx_monkey2.png'],
    't33':  ['picture/docx_monkey1.png', 'picture/docx_monkey2.png'],
    # Hell Cave 3 tours (River Cruise / Morning / Sunset)
    't32':  ['picture/docx_hell1.png', 'picture/docx_hell2.png', 'picture/docx_hell3.png', 'picture/docx_hell4.png', 'picture/docx_hell5.png'],
    't34':  ['picture/docx_hell1.png', 'picture/docx_hell2.png', 'picture/docx_hell3.png', 'picture/docx_hell4.png', 'picture/docx_hell5.png'],
    't35':  ['picture/docx_hell1.png', 'picture/docx_hell2.png', 'picture/docx_hell3.png', 'picture/docx_hell4.png', 'picture/docx_hell5.png'],
}

def build_gallery_html(tour_id, images):
    """Build a swipeable gallery HTML for a tour card."""
    slides = ''
    for img in images:
        slides += f'<div class="tg-slide"><img src="{img}" alt="Tour Photo" loading="lazy"></div>\n              '
    
    dots = ''
    for i in range(len(images)):
        active = ' tg-active' if i == 0 else ''
        dots += f'<span class="tg-dot{active}"></span>'
    
    arrows = ''
    if len(images) > 1:
        arrows = f'''
              <button class="tg-arrow tg-prev" onclick="tgPrev(event, this)" aria-label="prev">&#8249;</button>
              <button class="tg-arrow tg-next" onclick="tgNext(event, this)" aria-label="next">&#8250;</button>
              <div class="tg-dots">{dots}</div>'''
    
    return f'''<div class="tour-gallery" id="tg-{tour_id}">
              <div class="tg-track">
              {slides}</div>{arrows}
            </div>'''

# Replace each tour-image-container for tours in our gallery map
def replace_tour_image(html, tour_id, gallery_html):
    # Pattern: find the tour card with this openTourModal(tour_id)
    # Then find and replace only the tour-image-container within it
    pattern = rf'(openTourModal\(\'{re.escape(tour_id)}\'\)[^<]*(?:(?!</div>).)*?<div class="tour-image-container">).*?</div>'
    
    # More reliable approach: split into blocks by tour card
    # Find the position of the tour card with this ID
    start_marker = f"openTourModal('{tour_id}')"
    pos = html.find(start_marker)
    if pos == -1:
        print(f"  *** Not found: {tour_id}")
        return html
    
    # From this position, find the tour-image-container
    img_start = html.find('<div class="tour-image-container">', pos)
    if img_start == -1:
        print(f"  *** No image container for {tour_id}")
        return html
    
    # Find the end of this div (need to find matching </div>)
    img_end = html.find('</div>', img_start) + len('</div>')
    
    # Replace it
    old = html[img_start:img_end]
    html = html[:img_start] + gallery_html + html[img_end:]
    print(f"  Replaced image container for {tour_id}: {len(old)} chars -> {len(gallery_html)} chars")
    return html

total = 0
for tour_id, images in TOUR_GALLERY.items():
    gallery = build_gallery_html(tour_id, images)
    new_html = replace_tour_image(html, tour_id, gallery)
    if new_html != html:
        total += 1
    html = new_html

print(f"\nTotal tour cards updated: {total}")

# Write updated HTML
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML written!")

# ============================================================
# Add Gallery CSS to style.css
# ============================================================
GALLERY_CSS = """
/* ===== Tour Gallery Slider ===== */
.tour-gallery {
  position: relative;
  overflow: hidden;
  width: 100%;
  height: 100%;
  border-radius: inherit;
  touch-action: pan-y;
  user-select: none;
}
.tg-track {
  display: flex;
  height: 100%;
  transition: transform 0.35s cubic-bezier(.4,0,.2,1);
  will-change: transform;
}
.tg-slide {
  flex: 0 0 100%;
  height: 100%;
  overflow: hidden;
}
.tg-slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  pointer-events: none;
}
.tg-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0,0,0,0.42);
  color: #fff;
  border: none;
  border-radius: 50%;
  width: 32px;
  height: 32px;
  font-size: 22px;
  line-height: 1;
  cursor: pointer;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  transition: background 0.2s;
}
.tg-arrow:hover { background: rgba(0,0,0,0.7); }
.tg-prev { left: 6px; }
.tg-next { right: 6px; }
.tg-dots {
  position: absolute;
  bottom: 6px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 5px;
  z-index: 10;
}
.tg-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: rgba(255,255,255,0.5);
  transition: background 0.2s, transform 0.2s;
  display: inline-block;
}
.tg-dot.tg-active {
  background: #fff;
  transform: scale(1.3);
}
"""

if '.tour-gallery' not in css:
    css = css + '\n' + GALLERY_CSS
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("CSS written!")
else:
    print("CSS already present, skipping.")

# ============================================================
# Add Gallery JS to script.js
# ============================================================
GALLERY_JS = """
// ===== Tour Gallery Slider =====
(function() {
  function getState(gallery) {
    var track = gallery.querySelector('.tg-track');
    var slides = track.querySelectorAll('.tg-slide');
    var dots = gallery.querySelectorAll('.tg-dot');
    var idx = parseInt(gallery.getAttribute('data-idx') || '0');
    return { track, slides, dots, idx };
  }
  function goTo(gallery, newIdx) {
    var s = getState(gallery);
    var total = s.slides.length;
    newIdx = ((newIdx % total) + total) % total;
    s.track.style.transform = 'translateX(-' + (newIdx * 100) + '%)';
    s.dots.forEach(function(d, i) {
      d.classList.toggle('tg-active', i === newIdx);
    });
    gallery.setAttribute('data-idx', newIdx);
  }
  window.tgPrev = function(e, btn) {
    e.stopPropagation();
    var gallery = btn.closest('.tour-gallery');
    var s = getState(gallery);
    goTo(gallery, s.idx - 1);
  };
  window.tgNext = function(e, btn) {
    e.stopPropagation();
    var gallery = btn.closest('.tour-gallery');
    var s = getState(gallery);
    goTo(gallery, s.idx + 1);
  };

  // Touch/swipe support
  document.addEventListener('touchstart', function(e) {
    var gallery = e.target.closest('.tour-gallery');
    if (!gallery) return;
    gallery._touchStartX = e.touches[0].clientX;
    gallery._touchStartY = e.touches[0].clientY;
    gallery._swiping = false;
  }, { passive: true });

  document.addEventListener('touchmove', function(e) {
    var gallery = e.target.closest('.tour-gallery');
    if (!gallery || gallery._touchStartX == null) return;
    var dx = e.touches[0].clientX - gallery._touchStartX;
    var dy = e.touches[0].clientY - gallery._touchStartY;
    if (!gallery._swiping && Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 8) {
      gallery._swiping = true;
    }
    if (gallery._swiping) {
      e.preventDefault();
    }
  }, { passive: false });

  document.addEventListener('touchend', function(e) {
    var gallery = e.target.closest('.tour-gallery');
    if (!gallery || gallery._touchStartX == null) return;
    var dx = e.changedTouches[0].clientX - gallery._touchStartX;
    if (gallery._swiping && Math.abs(dx) > 40) {
      var s = getState(gallery);
      goTo(gallery, dx < 0 ? s.idx + 1 : s.idx - 1);
    }
    gallery._touchStartX = null;
    gallery._swiping = false;
  }, { passive: true });
})();
"""

if 'tour-gallery' not in js and 'tgPrev' not in js:
    js = js + '\n' + GALLERY_JS
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("JS written!")
else:
    print("JS already present, skipping.")

print("\nAll done! Tour cards updated with gallery sliders.")
