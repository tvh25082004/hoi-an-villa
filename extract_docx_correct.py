import zipfile
import os
import shutil

# Extract from the CORRECT DOCX file
docx_path = r"c:\Users\TranHuy_WIN\Desktop\booking-vietnam\DaNang_HoiAn_Experience_Guide.docx"
output_dir = r"c:\Users\TranHuy_WIN\Desktop\booking-vietnam\docx_extracted"

# Clean and create output dir
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

# Extract images from docx (which is a zip)
print("Extracting images from DaNang_HoiAn_Experience_Guide.docx...")
with zipfile.ZipFile(docx_path, 'r') as z:
    for name in z.namelist():
        if name.startswith('word/media/'):
            filename = os.path.basename(name)
            if filename:
                out_path = os.path.join(output_dir, filename)
                with z.open(name) as src, open(out_path, 'wb') as dst:
                    shutil.copyfileobj(src, dst)
                print(f"Extracted: {filename} ({os.path.getsize(out_path)} bytes)")

print(f"\nTotal images extracted: {len(os.listdir(output_dir))}")
print(f"Images: {sorted(os.listdir(output_dir))}")
