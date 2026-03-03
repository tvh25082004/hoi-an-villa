"""
Download Đà Nẵng & Hội An images from Pinterest into sontra-villa/picture/
Ensures no duplicate images between the two sets.
"""
import requests
import json
import re
import os
import hashlib
import time
from urllib.parse import unquote

SAVE_DIR = r"D:\project\booking\sontra-villa\picture"
os.makedirs(SAVE_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.pinterest.com/',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
}

def extract_pinterest_images(url, max_images=25):
    """Extract image URLs from Pinterest search page"""
    session = requests.Session()
    
    # First visit pinterest.com to get cookies
    try:
        session.get('https://www.pinterest.com/', headers=HEADERS, timeout=15)
        time.sleep(1)
    except:
        pass
    
    try:
        resp = session.get(url, headers=HEADERS, timeout=20)
        print(f"  Pinterest response status: {resp.status_code}")
        print(f"  Response length: {len(resp.text)} chars")
    except Exception as e:
        print(f"  Error fetching Pinterest: {e}")
        return []
    
    img_urls = set()
    
    # Strategy 1: Find pinimg.com URLs with originals or high-res
    patterns = [
        r'https://i\.pinimg\.com/originals/[a-f0-9]{2}/[a-f0-9]{2}/[a-f0-9]{2}/[a-f0-9]+\.\w{3,4}',
        r'https://i\.pinimg\.com/736x/[a-f0-9]{2}/[a-f0-9]{2}/[a-f0-9]{2}/[a-f0-9]+\.\w{3,4}',
        r'https://i\.pinimg\.com/564x/[a-f0-9]{2}/[a-f0-9]{2}/[a-f0-9]{2}/[a-f0-9]+\.\w{3,4}',
        r'https://i\.pinimg\.com/474x/[a-f0-9]{2}/[a-f0-9]{2}/[a-f0-9]{2}/[a-f0-9]+\.\w{3,4}',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, resp.text)
        for m in matches:
            # Upgrade to 736x for good quality
            upgraded = re.sub(r'/(?:474x|564x|236x|170x)/', '/736x/', m)
            img_urls.add(upgraded)
    
    # Strategy 2: Parse __PWS_DATA__ JSON
    pws_match = re.search(r'<script[^>]*id="__PWS_DATA__"[^>]*>(.*?)</script>', resp.text, re.DOTALL)
    if pws_match:
        try:
            pws_data = json.loads(pws_match.group(1))
            # Recursively find image URLs in JSON
            def find_images(obj):
                if isinstance(obj, dict):
                    for k, v in obj.items():
                        if k in ('url', 'src') and isinstance(v, str) and 'pinimg.com' in v:
                            upgraded = re.sub(r'/(?:474x|564x|236x|170x)/', '/736x/', v)
                            img_urls.add(upgraded)
                        else:
                            find_images(v)
                elif isinstance(obj, list):
                    for item in obj:
                        find_images(item)
            find_images(pws_data)
        except json.JSONDecodeError:
            pass
    
    # Strategy 3: Try to find JSON data in other script tags
    script_tags = re.findall(r'<script[^>]*>(.*?)</script>', resp.text, re.DOTALL)
    for script in script_tags:
        if 'pinimg.com' in script:
            for pattern in patterns:
                matches = re.findall(pattern, script)
                for m in matches:
                    upgraded = re.sub(r'/(?:474x|564x|236x|170x)/', '/736x/', m)
                    img_urls.add(upgraded)
    
    # Filter out tiny icons, avatars, profile pics
    filtered = []
    for url in img_urls:
        # Skip if it looks like a profile pic or tiny image
        if '/75x75_' in url or '/30x30_' in url or '/140x140_' in url:
            continue
        filtered.append(url)
    
    print(f"  Found {len(filtered)} unique image URLs")
    return filtered[:max_images]


def download_image(url, save_path, min_size=10000):
    """Download image, return True if successful and larger than min_size"""
    try:
        resp = requests.get(url, headers={
            'User-Agent': HEADERS['User-Agent'],
            'Referer': 'https://www.pinterest.com/'
        }, timeout=15)
        if resp.status_code == 200 and len(resp.content) > min_size:
            with open(save_path, 'wb') as f:
                f.write(resp.content)
            return True
        else:
            print(f"    Skipped (status={resp.status_code}, size={len(resp.content)})")
    except Exception as e:
        print(f"    Error: {e}")
    return False


def get_file_hash(filepath):
    """Get MD5 hash of file for duplicate detection"""
    h = hashlib.md5()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def main():
    # Pinterest URLs
    danang_url = "https://www.pinterest.com/search/pins/?q=%C4%91%C3%A0%20n%E1%BA%B5ng%20city&rs=ac&len=7&source_id=ac_IeZnoC0X&eq=%C4%90%C3%A0%20n%E1%BA%B5ng&etslf=7599"
    hoian_url = "https://www.pinterest.com/search/pins/?q=hoi%20an%20ancient%20town&rs=ac&len=6&source_id=ac_Rzh9KiYL&eq=H%E1%BB%99i%20an&etslf=10416"
    
    print("=" * 60)
    print("📥 Downloading Đà Nẵng images from Pinterest...")
    print("=" * 60)
    danang_imgs = extract_pinterest_images(danang_url, 15)
    
    print()
    print("=" * 60)
    print("📥 Downloading Hội An images from Pinterest...")
    print("=" * 60)
    hoian_imgs = extract_pinterest_images(hoian_url, 30)
    
    # Remove any URLs that appear in both sets
    danang_set = set(danang_imgs)
    hoian_set = set(hoian_imgs)
    overlap = danang_set & hoian_set
    if overlap:
        print(f"\n⚠️ Found {len(overlap)} overlapping URLs, removing from Hội An set")
        hoian_imgs = [u for u in hoian_imgs if u not in danang_set]
    
    # Download Đà Nẵng
    print(f"\n{'='*60}")
    print(f"⬇️ Downloading {len(danang_imgs)} Đà Nẵng images...")
    print(f"{'='*60}")
    danang_hashes = set()
    danang_downloaded = []
    for i, url in enumerate(danang_imgs):
        ext = url.split('.')[-1].split('?')[0][:4]
        if ext not in ('jpg', 'jpeg', 'png', 'webp'):
            ext = 'jpg'
        fname = f"danang_{i+1:02d}.{ext}"
        fpath = os.path.join(SAVE_DIR, fname)
        print(f"  [{i+1}/{len(danang_imgs)}] {fname}...")
        if download_image(url, fpath):
            fhash = get_file_hash(fpath)
            if fhash in danang_hashes:
                print(f"    ❌ Duplicate hash, removing {fname}")
                os.remove(fpath)
            else:
                danang_hashes.add(fhash)
                danang_downloaded.append(fname)
                print(f"    ✅ OK ({os.path.getsize(fpath)//1024} KB)")
    
    # Download Hội An
    print(f"\n{'='*60}")
    print(f"⬇️ Downloading {len(hoian_imgs)} Hội An images...")
    print(f"{'='*60}")
    hoian_hashes = set()
    hoian_downloaded = []
    for i, url in enumerate(hoian_imgs):
        ext = url.split('.')[-1].split('?')[0][:4]
        if ext not in ('jpg', 'jpeg', 'png', 'webp'):
            ext = 'jpg'
        fname = f"hoian_{i+1:02d}.{ext}"
        fpath = os.path.join(SAVE_DIR, fname)
        print(f"  [{i+1}/{len(hoian_imgs)}] {fname}...")
        if download_image(url, fpath):
            fhash = get_file_hash(fpath)
            if fhash in danang_hashes or fhash in hoian_hashes:
                print(f"    ❌ Duplicate hash (cross-check), removing {fname}")
                os.remove(fpath)
            else:
                hoian_hashes.add(fhash)
                hoian_downloaded.append(fname)
                print(f"    ✅ OK ({os.path.getsize(fpath)//1024} KB)")
    
    print(f"\n{'='*60}")
    print(f"📊 SUMMARY")
    print(f"{'='*60}")
    print(f"  Đà Nẵng: {len(danang_downloaded)} images downloaded")
    print(f"  Hội An:  {len(hoian_downloaded)} images downloaded")
    print(f"  Save dir: {SAVE_DIR}")
    print(f"\n  Đà Nẵng files: {danang_downloaded}")
    print(f"  Hội An files:  {hoian_downloaded}")
    
    # Verify no hash collision between sets
    if danang_hashes & hoian_hashes:
        print("  ⚠️ WARNING: Hash collision detected!")
    else:
        print("  ✅ No duplicates between Đà Nẵng and Hội An sets")


if __name__ == '__main__':
    main()
