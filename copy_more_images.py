import shutil
import os

src_dir = r"C:\Users\TranHuy_WIN\.gemini\antigravity\brain\279a6c46-762f-41cd-851a-c8fa50ac6650"
dst_dir = r"d:\project\booking\sontra-villa"

imgs = {
    "hoian_cooking_signature_1772544751646.png": "hoian_cooking_signature.png",
    "hoian_eco_signature_1772544767452.png": "hoian_eco_signature.png",
    "cham_island_signature_1772544786136.png": "cham_island_signature.png",
    "myson_signature_1772544812357.png": "myson_signature.png",
    "danang_marble_signature_1772544828819.png": "danang_marble_signature.png",
    "danang_dragon_signature_1772544848237.png": "danang_dragon_signature.png"
}

for src_name, dst_name in imgs.items():
    src_path = os.path.join(src_dir, src_name)
    dst_path = os.path.join(dst_dir, dst_name)
    if os.path.exists(src_path):
        shutil.copy(src_path, dst_path)
        print(f"Copied {dst_name}")
    else:
        print(f"Missing {src_path}")
