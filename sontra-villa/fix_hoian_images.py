
import urllib.request
import os
import time
import re

SAVE_DIR = r"d:\project\booking\sontra-villa\picture"

# 40 new Hoi An images from Pinterest
new_hoian_urls = [
    "https://i.pinimg.com/736x/53/9f/69/539f6917d62331a36a657ea83ed026a6.jpg",
    "https://i.pinimg.com/736x/85/7a/60/857a60c599e7a6a0d820ce64c6fc376c.jpg",
    "https://i.pinimg.com/736x/fa/a5/57/faa55738114c19eebacb115a70228577.jpg",
    "https://i.pinimg.com/736x/2e/6e/a2/2e6ea29564f338e01e6c9b67d6c6b0fc.jpg",
    "https://i.pinimg.com/736x/e6/95/9d/e6959ded746f78aa2630059bfd51bd7f.jpg",
    "https://i.pinimg.com/736x/16/29/31/162931caf376a109f11310b962b5b1a4.jpg",
    "https://i.pinimg.com/736x/e6/b0/5b/e6b05b37a0b33b484e6fb10749fe3626.jpg",
    "https://i.pinimg.com/736x/10/9a/22/109a22c0931eda2a1499ae450b562f58.jpg",
    "https://i.pinimg.com/736x/df/34/1a/df341a00a7d6a5ff2c2bd8527038d784.jpg",
    "https://i.pinimg.com/736x/30/ac/07/30ac072553a76ca733226220a98152b9.jpg",
    "https://i.pinimg.com/736x/bc/29/d5/bc29d52f4fb0a979ad6327eb5edab4c7.jpg",
    "https://i.pinimg.com/736x/48/f6/3b/48f63b78d110b7d1439d46767820441f.jpg",
    "https://i.pinimg.com/736x/11/c6/15/11c6153a25c076d781d1d9ae2b5449fd.jpg",
    "https://i.pinimg.com/736x/32/32/74/323274293c3c05ec31d6583abb448814.jpg",
    "https://i.pinimg.com/736x/a6/31/43/a6314343a23540f78fd0270bf01555ac.jpg",
    "https://i.pinimg.com/736x/20/20/24/202024632abb3dd4215b58fcfe13a0de.jpg",
    "https://i.pinimg.com/736x/6a/41/08/6a410820f658c3e79b4c0361e5fad620.jpg",
    "https://i.pinimg.com/736x/c9/73/be/c973be9eec558c46cd21c5dc821f07c7.jpg",
    "https://i.pinimg.com/736x/90/f3/8f/90f38f105cce10d4c746966ddfec2a34.jpg",
    "https://i.pinimg.com/736x/38/2e/21/382e2147964ff425c470bef029023017.jpg",
    "https://i.pinimg.com/736x/e5/33/17/e5331742ed3867fb69ebcb6628159599.jpg",
    "https://i.pinimg.com/736x/83/82/dd/8382dd25dc597aaf73d951cd12f700f2.jpg",
    "https://i.pinimg.com/736x/77/7e/2d/777e2d31145d9f8d6083ac6070def597.jpg",
    "https://i.pinimg.com/736x/3c/79/c1/3c79c135029d28d8a945e914c020be05.jpg",
    "https://i.pinimg.com/736x/60/f6/28/60f628cdd92c1f0ab01c1306c3813135.jpg",
    "https://i.pinimg.com/736x/45/87/4c/45874c9e5ca58650c2bd4ef5baef92e2.jpg",
    "https://i.pinimg.com/736x/7f/65/dd/7f65dd66c74529b1da5d6af1fa4a68f4.jpg",
    "https://i.pinimg.com/736x/c5/a8/95/c5a895d7f7d585a88d8c90e9397f96ff.jpg",
    "https://i.pinimg.com/736x/30/91/61/3091619b6d6af94eb4aff65ede93772e.jpg",
    "https://i.pinimg.com/736x/60/f5/43/60f543f4c5aa18659fc14e3cbef6d9be.jpg",
    "https://i.pinimg.com/736x/96/22/54/9622544f23f992b58fa0afa2b3883f4b.jpg",
    "https://i.pinimg.com/736x/50/75/3b/50753be1e616da7eb05fd8342f212084.jpg",
    "https://i.pinimg.com/736x/31/cd/94/31cd9409126c5cdb053344617df2fd32.jpg",
    "https://i.pinimg.com/736x/93/79/18/937918cdb2a565c87e9674a2aad4abed.jpg",
    "https://i.pinimg.com/736x/0a/3a/c9/0a3ac95f577ae98c2d4f9a0cdeaa839a.jpg",
    "https://i.pinimg.com/736x/6b/11/6c/6b116c0adad43b7d897f0d535204149a.jpg",
    "https://i.pinimg.com/736x/ed/6c/5f/ed6c5f95dc3967e545ee84e7a9015099.jpg",
    "https://i.pinimg.com/736x/60/51/51/6051514999d95b814806b5d052177657.jpg",
    "https://i.pinimg.com/736x/2c/8f/2e/2c8f2e4b75551a4e63fd807d335e04b8.jpg",
    "https://i.pinimg.com/736x/c1/63/99/c1639923ceab741fe4f5bc9f14d04853.jpg",
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

# Download new images as hoian_11.jpg to hoian_50.jpg
print("Downloading new Hoi An images...")
failed = []
for i, url in enumerate(new_hoian_urls):
    fname = f"hoian_{i+11}.jpg"
    fpath = os.path.join(SAVE_DIR, fname)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        with open(fpath, 'wb') as f:
            f.write(data)
        print(f"[OK] {fname}")
        time.sleep(0.3)
    except Exception as e:
        print(f"[FAIL] {fname}: {e}")
        failed.append(i+11)

print(f"\nDownload complete! Failed: {failed}")

# Now rebuild image assignments for HTML - use all 50 hoian images and cycle through
html_path = r"d:\project\booking\sontra-villa\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# All available hoian images (skip failed ones)
available = [i for i in range(1, 51) if i not in failed]
print(f"\nAvailable Hoi An images: {len(available)}")

# Reassign images to hoian tour cards in order
hoian_idx = 0

def reassign_hoian(match):
    global hoian_idx
    card_html = match.group(0)
    region_match = re.search(r'data-region="([^"]+)"', card_html)
    if region_match and region_match.group(1) == 'hoian':
        img_num = available[hoian_idx % len(available)]
        hoian_idx += 1
        # Replace img src
        card_html = re.sub(r'src="picture/hoian_\d+\.jpg"', f'src="picture/hoian_{img_num}.jpg"', card_html)
    return card_html

pattern = r'(<div class="tour-card[^>]*>.*?<div class="tour-card-click-hint">.*?</div>\s*</div>)'
new_content = re.sub(pattern, reassign_hoian, content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Updated {hoian_idx} Hoi An tour cards with unique images.")

# Also update TOUR_DATA
with open(html_path, 'r', encoding='utf-8') as f:
    content_after = f.read()

hoian_tour_idx = 0
def reassign_tourdata_hoian(match):
    global hoian_tour_idx
    data_str = match.group(0)
    if '"region": "hoian"' in data_str:
        img_num = available[hoian_tour_idx % len(available)]
        hoian_tour_idx += 1
        data_str = re.sub(r'"image": "picture/hoian_\d+\.jpg"', f'"image": "picture/hoian_{img_num}.jpg"', data_str)
    return data_str

# Match each tour entry: 't01': { ... },
tour_entry_pattern = r"'t\d+': \{.*?\},"
new_content2 = re.sub(tour_entry_pattern, reassign_tourdata_hoian, content_after, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content2)

print(f"Updated {hoian_tour_idx} Hoi An TOUR_DATA entries with unique images.")
