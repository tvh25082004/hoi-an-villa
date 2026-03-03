
import pdfplumber
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with pdfplumber.open('tong_hop_tour_hoi_an_2026.pdf') as pdf:
    print(f'Total pages: {len(pdf.pages)}')
    for i, page in enumerate(pdf.pages):
        print(f'--- PAGE {i+1} ---')
        text = page.extract_text()
        if text:
            print(text)
        print()
