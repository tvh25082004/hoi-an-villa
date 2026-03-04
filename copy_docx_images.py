"""
This script:
1. Copies extracted docx images to picture/ folder with semantic names
2. Updates index.html tour cards to use swipeable gallery with correct images

IMAGE MAPPING from docx analysis:
- Cham Island (3 tours: t07, t11, t10): image8.png, image19.png, image5.png
- Cam Thanh / Bay Mau (4 tours: t14, t38, t39, t40): image6.png, image1.png, image15.png
- My Son (2 tours: t25, t26): image9.png, image17.png, image12.png
- Buffalo/Cycling (2 tours: t03, t21): image4.png, image18.png, image20.png
- Basket Boat / Lantern (3 tours: t04, t05, t06): image16.png, image23.png
- Lantern Tra Que (2 tours: t20, t19): image21.png, image10.png
- Monkey Mountain / Marble group 1 (t30, t33): image2.png, image7.png  
- Monkey Mountain / Marble / Hell Cave 3 tours (t32, t34, t35): image13.png, image11.png, image22.png, image3.png, image14.png
"""
import shutil
import os
import re

src_dir = r"c:\Users\TranHuy_WIN\Desktop\booking-vietnam\docx_extracted"
pic_dir = r"c:\Users\TranHuy_WIN\Desktop\booking-vietnam\sontra-villa\picture"

# Copy images with semantic names
copies = {
    # Cham Island images
    "image8.png":  "docx_cham1.png",
    "image19.png": "docx_cham2.png",
    "image5.png":  "docx_cham3.png",
    # Cam Thanh / Bay Mau images
    "image6.png":  "docx_camthanh1.png",
    "image1.png":  "docx_camthanh2.png",
    "image15.png": "docx_camthanh3.png",
    # My Son images
    "image9.png":  "docx_myson1.png",
    "image17.png": "docx_myson2.png",
    "image12.png": "docx_myson3.png",
    # Buffalo/Cycling
    "image4.png":  "docx_buffalo1.png",
    "image18.png": "docx_buffalo2.png",
    "image20.png": "docx_buffalo3.png",
    # Basket Boat / Lantern (t04, t05, t06)
    "image16.png": "docx_basket1.png",
    "image23.png": "docx_basket2.png",
    # Lantern Tra Que
    "image21.png": "docx_lantern1.png",
    "image10.png": "docx_lantern2.png",
    # Monkey Mountain group 1 (t30 Monkey Mt+Marble+Hoi An Night, t33 Monkey+Marble+MySon)
    "image2.png":  "docx_monkey1.png",
    "image7.png":  "docx_monkey2.png",
    # Hell Cave group 3 tours (t32, t34, t35)
    "image13.png": "docx_hell1.png",
    "image11.png": "docx_hell2.png",
    "image22.png": "docx_hell3.png",
    "image3.png":  "docx_hell4.png",
    "image14.png": "docx_hell5.png",
}

for src_name, dst_name in copies.items():
    src = os.path.join(src_dir, src_name)
    dst = os.path.join(pic_dir, dst_name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied {src_name} -> {dst_name}")
    else:
        print(f"NOT FOUND: {src_name}")

print("\nDone copying images!")
print(f"\nImages in picture dir: {[f for f in os.listdir(pic_dir) if f.startswith('docx_')]}")
