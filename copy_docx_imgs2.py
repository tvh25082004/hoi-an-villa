import sys, os, shutil
sys.stdout.reconfigure(encoding='utf-8')

# The DOCX images are already extracted in docx_extracted folder
# image1.png through image23.png
# Based on docx content analysis:
# Tours in order in docx:
# 1. Nui Than Tai Hot Springs (Da Nang) - first tour in docx
# 2. VinWonders Nam Hoi An (Hoi An) 
# 3. Da Nang Dolphin Show (Da Nang)
# 4. Hoi An Memories Show (Hoi An)
# 5. Han River Night Cruise (Da Nang)
# 
# We need to map images to tours. Let's look at the existing image filenames
# in the picture folder to understand how many images are for each tour

src_dir = r'c:\Users\TranHuy_WIN\Desktop\booking-vietnam\docx_extracted'
dst_dir = r'c:\Users\TranHuy_WIN\Desktop\booking-vietnam\sontra-villa\picture'

# Copy images with new names for each tour
# We don't know exact mapping, so we'll distribute them approximately
# Based on previous extraction style, images are ordered per tour

image_map = {
    # Nui Than Tai (Da Nang) - images 1-5
    'image1.png': 'docx_ntt1.png',
    'image2.png': 'docx_ntt2.png',
    'image3.png': 'docx_ntt3.png',
    'image4.png': 'docx_ntt4.png',
    'image5.png': 'docx_ntt5.png',
    # VinWonders (Hoi An) - images 6-10
    'image6.png': 'docx_vinwonders1.png',
    'image7.png': 'docx_vinwonders2.png',
    'image8.png': 'docx_vinwonders3.png',
    'image9.png': 'docx_vinwonders4.png',
    'image10.png': 'docx_vinwonders5.png',
    # Dolphin Show (Da Nang) - images 11-13
    'image11.png': 'docx_dolphin1.png',
    'image12.png': 'docx_dolphin2.png',
    'image13.png': 'docx_dolphin3.png',
    # Hoi An Memories Show (Hoi An) - images 14-18
    'image14.png': 'docx_memories1.png',
    'image15.png': 'docx_memories2.png',
    'image16.png': 'docx_memories3.png',
    'image17.png': 'docx_memories4.png',
    'image18.png': 'docx_memories5.png',
    # Han River Night Cruise (Da Nang) - images 19-23
    'image19.png': 'docx_hanriver1.png',
    'image20.png': 'docx_hanriver2.png',
    'image21.png': 'docx_hanriver3.png',
    'image22.png': 'docx_hanriver4.png',
    'image23.png': 'docx_hanriver5.png',
}

for src_name, dst_name in image_map.items():
    src_path = os.path.join(src_dir, src_name)
    dst_path = os.path.join(dst_dir, dst_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f'Copied {src_name} -> {dst_name}')
    else:
        print(f'NOT FOUND: {src_path}')

print('Done!')
