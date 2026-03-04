import os
import json
import re

target_dir = "C:\\Users\\TranHuy_WIN\\Desktop\\booking-vietnam\\sontra-villa"
target_file = os.path.join(target_dir, "index.html")

with open(target_file, "r", encoding="utf-8") as f:
    text = f.read()

translations = {
    "Son Tra Villa Hoi An | Link in Bio": "Sơn Trà Villa Hội An | Liên kết trong Tụ",
    "Son Tra Villa Hoi An - Quiet Pool Villa Near Old Town": "Sơn Trà Villa Hội An - Biệt thự có hồ bơi tĩnh lặng ngay cạnh khu phố cổ",
    "Quiet Pool Villa Near Old Town": "Biệt thự hồ bơi nhỏ gọn yên tĩnh gần với Phố cổ",
    "Quick Support": "Hỗ trợ Nhanh",
    "Villa Gallery": "Khu trưng bày Biệt thự",
    "Relaxing Vibe": "Tận hưởng thư giãn",
    "Tropical Summer": "Mùa hè Nhiệt đới",
    "Villa WiFi": "Wifi Biệt Thự",
    "Network": "Mạng",
    "Password": "Mật khẩu",
    "Google Maps Location": "Vị trí trên bản đồ Google",
    "Hoi An Tour List": "Danh sách các Tour đi Hội An",
    "Local Recommendations": "Khuyến nghị các Địa Phương (Đến)",
    "Go Back": "Quay Trở về",
    "Select a contact method below for assistance": "Vui vòng chọn phương thức hỗ trợ bạn đi theo bên dưới này",
    "Direct Call": "Gặp mặt nói chuyện gọi hỏi thẳng",
    "WhatsApp Chat": "Nói chuyện bên Whatsapp",
    "Local Highlights": "Sức hấp dẫn ở Địa Phương",
    "hand-picked spots for food, drinks": "Các địa điểm ăn ngọt và uống do thủ chong (cầm tay)",
    "80+ hand-picked spots for food, drinks &amp; vibes in Hoi An": "Có hơn khoảng 80+ địa điểm của đồ ăn , Các điểm đến ngọt thanh thán trên cho mình một sự thoải mát ở TP. Hội An",
    "Bars": "Quầy Bar",
    "Cocktails": "Cocktail",
    "Hot Food": "Đồ Ăn Nóng",
    "Snacks": "Đồ Ăn Vặt",
    "Cafés": "Quán Cà Phê",
    "Shops": "Mua Sắm",
    "All": "Tất Cả",
    "Get Directions": "Nhận Đường dẫn chỉ đường"
}

# The cards could be using DeepTranslator
import sys
try:
    from bs4 import BeautifulSoup
    from deep_translator import GoogleTranslator
except ImportError as e:
    print("Dependencies not met:", e)
    sys.exit(1)

soup = BeautifulSoup(text, "html.parser")
translator = GoogleTranslator(source='en', target='vi')

# Translate regular strings
def t_text(t):
    if not t or not t.strip(): return t
    if t.strip() in translations:
        return t.replace(t.strip(), translations[t.strip()])
    # let's only translate strings with letters
    if re.search('[a-zA-Z]', t):
        try:
            return translator.translate(t.strip())
        except:
            return t
    return t

# Translate all textual elements that aren't scripts or styles
for element in soup.find_all(string=True):
    if element.parent.name not in ['style', 'script', 'head', 'title', 'meta']:
        orig = str(element)
        if orig.strip():
            translated = t_text(orig)
            if translated and translated != orig.strip():
                element.replace_with(orig.replace(orig.strip(), translated))

# Hardcode replace values on strings that were in meta and titles
for t in soup.find_all('title'):
    if t.string:
        t.string = "Sơn Trà Villa Hội An | Link in Bio"

meta_desc = soup.find('meta', {'name': 'description'})
if meta_desc and meta_desc.get('content'):
    meta_desc['content'] = "Sơn Trà Villa Hội An - Biệt thự hồ bơi nhỏ gọn yên tĩnh gần với Phố cổ"

# Additional attributes
for btn in soup.find_all(title=True):
    orig = btn['title']
    btn['title'] = t_text(orig)
    
with open(target_file, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Translation applied.")
