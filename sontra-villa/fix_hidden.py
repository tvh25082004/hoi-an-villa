
import re

html_path = r"d:\project\booking\sontra-villa\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Count tour cards with and without hidden class
all_cards = re.findall(r'<div class="tour-card fade-in-up(?: hidden)?"', content)
hidden_cards = re.findall(r'<div class="tour-card fade-in-up hidden"', content)
visible_cards = re.findall(r'<div class="tour-card fade-in-up"', content)

print(f"Total tour cards: {len(all_cards)}")
print(f"Hidden cards: {len(hidden_cards)}")
print(f"Visible cards: {len(visible_cards)}")

# Remove hidden class from all tour cards
new_content = content.replace('class="tour-card fade-in-up hidden"', 'class="tour-card fade-in-up"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

# Verify
newly_hidden = re.findall(r'<div class="tour-card fade-in-up hidden"', new_content)
print(f"\nAfter fix - Hidden cards remaining: {len(newly_hidden)}")
print("Done!")
