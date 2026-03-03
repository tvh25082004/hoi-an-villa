
import re

with open(r'd:\project\booking\sontra-villa\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the tour-list-container div
idx = html.find('id="tour-list-container"')
if idx < 0:
    idx = html.find('tour-list-container')
print(f"Container at: {idx}")

# Check section after container
section = html[idx:idx+5000]

# Find all onclick attrs in this section
onclicks = re.findall(r"onclick=['\"]([^'\"]+)", section)
print("First 20 onclicks:", onclicks[:20])

# Look for imgs in new tour cards
imgs = re.findall(r'<img\s+src="([^"]+)"', section[:3000])
print("First 10 imgs:", imgs[:10])
