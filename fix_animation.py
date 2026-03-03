import re

with open(r'd:\project\booking\sontra-villa\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the filterTour function with a smoother animated version
old_fn = """  // ===== FILTER TOURS BY REGION =====
  function filterTour(region, btn) {
    document.querySelectorAll('#tour-view .rec-tab').forEach(t => t.classList.remove('active'));
    btn.classList.add('active');
    const cards = document.querySelectorAll('#tour-list-container .tour-card');
    let visibleIndex = 0;
    cards.forEach((card) => {
      const match = (region === 'all') || (card.dataset.region === region);
      if (match) {
        card.classList.remove('hidden');
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        const delay = visibleIndex * 50;
        setTimeout(() => {
          card.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
          card.style.opacity = '1';
          card.style.transform = 'translateY(0)';
        }, delay);
        visibleIndex++;
      } else {
        card.classList.add('hidden');
        card.style.opacity = '';
        card.style.transform = '';
      }
    });
  }"""

new_fn = """  // ===== FILTER TOURS BY REGION =====
  function filterTour(region, btn) {
    // Animate tab switch
    document.querySelectorAll('#tour-view .rec-tab').forEach(t => t.classList.remove('active'));
    btn.classList.add('active');
    
    const container = document.getElementById('tour-list-container');
    const cards = container.querySelectorAll('.tour-card');
    
    // Fade out container first
    container.style.transition = 'opacity 0.2s ease';
    container.style.opacity = '0';
    
    setTimeout(() => {
      let visibleIndex = 0;
      cards.forEach((card) => {
        const match = (region === 'all') || (card.dataset.region === region);
        if (match) {
          card.classList.remove('hidden');
          card.style.opacity = '0';
          card.style.transform = 'translateY(30px) scale(0.95)';
          visibleIndex++;
        } else {
          card.classList.add('hidden');
        }
      });
      
      // Fade in container
      container.style.opacity = '1';
      
      // Stagger animate each visible card
      let delay = 0;
      cards.forEach((card) => {
        if (!card.classList.contains('hidden')) {
          setTimeout(() => {
            card.style.transition = 'opacity 0.45s cubic-bezier(0.4,0,0.2,1), transform 0.45s cubic-bezier(0.4,0,0.2,1)';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0) scale(1)';
          }, delay);
          delay += 60;
        }
      });
      
      // Scroll to top of tour list
      container.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 200);
  }"""

if old_fn in html:
    html = html.replace(old_fn, new_fn)
    print("SUCCESS: filterTour function replaced with smooth animation version!")
else:
    print("WARNING: Could not find exact old filterTour. Trying partial match...")
    # Try finding by the function signature
    start = html.find('function filterTour(region, btn) {')
    if start >= 0:
        # Find the end of the function (next function or end of script)
        end = html.find('\n  }', start + 50)
        if end >= 0:
            end += 4  # include the closing brace and newline
            old_block = html[start:end]
            html = html[:start] + new_fn.split('function filterTour')[1] + html[end:]
            html = html[:start] + 'function filterTour' + html[start:]
            print(f"SUCCESS: Replaced filterTour at {start}-{end}")
        else:
            print("ERROR: Could not find end of old filterTour")
    else:
        print("ERROR: filterTour not found at all")

with open(r'd:\project\booking\sontra-villa\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
