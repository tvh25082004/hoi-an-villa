import shutil
import os
import glob

src_dir = r"C:\Users\TranHuy_WIN\.gemini\antigravity\brain\279a6c46-762f-41cd-851a-c8fa50ac6650"
dst_dir = r"d:\project\booking\sontra-villa"

# Copy the generated signatures
if os.path.exists(os.path.join(src_dir, "hoian_signature_1772543804961.png")):
    shutil.copy(os.path.join(src_dir, "hoian_signature_1772543804961.png"), os.path.join(dst_dir, "hoian_signature.png"))

if os.path.exists(os.path.join(src_dir, "hue_signature_1772543822350.png")):
    shutil.copy(os.path.join(src_dir, "hue_signature_1772543822350.png"), os.path.join(dst_dir, "hue_signature.png"))

if os.path.exists(os.path.join(src_dir, "danang_signature_1772543844660.png")):
    shutil.copy(os.path.join(src_dir, "danang_signature_1772543844660.png"), os.path.join(dst_dir, "danang_signature.png"))

# Copy the original 5 images into sontra-villa if they aren't there
for f in ["cham_island.png", "basket_boat.png", "golden_bridge.png", "hoi_an_town.png", "my_son.png", "avartar.jpg", "806356723.jpg", "827248813.jpg"]:
    if os.path.exists(os.path.join(r"d:\project\booking", f)):
        shutil.copy(os.path.join(r"d:\project\booking", f), os.path.join(dst_dir, f))

print("Copied images successfully.")
