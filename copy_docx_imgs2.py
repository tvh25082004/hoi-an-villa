import sys, os, shutil
from PIL import Image
sys.stdout.reconfigure(encoding='utf-8')

# Based on docx_structure.txt analysis:
# 1. Nui Than Tai Hot Springs (Da Nang) - IMAGE #1, #2, #3 (image1, image2, image3)
# 2. VinWonders Nam Hoi An (Hoi An) - IMAGE #4, #5, #6 (image4, image5, image6)
# 3. Da Nang Dolphin Show (Da Nang) - IMAGE #7, #8, #9 (image7, image8, image9)
# 4. Hoi An Memories Show (Hoi An) - IMAGE #10, #11, #12 (image10, image11, image12)
# 5. Han River Night Cruise (Da Nang) - IMAGE #13, #14 (image13, image14)

src_dir = r'c:\Users\TranHuy_WIN\Desktop\booking-vietnam\docx_extracted'
dst_dir = r'c:\Users\TranHuy_WIN\Desktop\booking-vietnam\sontra-villa\picture'

# CORRECT mapping based on actual DOCX structure
image_map = {
    # Nui Than Tai (Da Nang) - images 1-3 ONLY
    'image1': 'docx_ntt1.png',
    'image2': 'docx_ntt2.png',
    'image3': 'docx_ntt3.png',
    # VinWonders (Hoi An) - images 4-6 ONLY
    'image4': 'docx_vinwonders1.png',
    'image5': 'docx_vinwonders2.png',
    'image6': 'docx_vinwonders3.png',
    # Dolphin Show (Da Nang) - images 7-9 ONLY
    'image7': 'docx_dolphin1.png',
    'image8': 'docx_dolphin2.png',
    'image9': 'docx_dolphin3.png',
    # Hoi An Memories Show (Hoi An) - images 10-12 ONLY
    'image10': 'docx_memories1.png',
    'image11': 'docx_memories2.png',
    'image12': 'docx_memories3.png',
    # Han River Night Cruise (Da Nang) - images 13-14 ONLY
    'image13': 'docx_hanriver1.png',
    'image14': 'docx_hanriver2.png',
}

print("Copying images from DOCX with CORRECT mapping...")
for src_base, dst_name in image_map.items():
    # Try both .jpeg and .png extensions
    src_jpeg = os.path.join(src_dir, src_base + '.jpeg')
    src_png = os.path.join(src_dir, src_base + '.png')
    dst_path = os.path.join(dst_dir, dst_name)
    
    src_path = None
    if os.path.exists(src_jpeg):
        src_path = src_jpeg
    elif os.path.exists(src_png):
        src_path = src_png
    
    if src_path:
        # Convert to PNG if needed
        if src_path.endswith('.jpeg') or src_path.endswith('.jpg'):
            try:
                img = Image.open(src_path)
                img.save(dst_path, 'PNG')
                print(f'✓ Converted & copied {os.path.basename(src_path)} -> {dst_name}')
            except Exception as e:
                print(f'✗ Error converting {os.path.basename(src_path)}: {e}')
        else:
            shutil.copy2(src_path, dst_path)
            print(f'✓ Copied {os.path.basename(src_path)} -> {dst_name}')
    else:
        print(f'✗ NOT FOUND: {src_base}.jpeg or {src_base}.png')

print('\nDone! Images copied with correct mapping from DOCX.')
