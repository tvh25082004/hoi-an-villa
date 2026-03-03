
import urllib.request
import os
import time

SAVE_DIR = r"d:\project\booking\sontra-villa\picture"

danang_urls = [
    "https://i.pinimg.com/736x/0c/4d/e3/0c4de3927a9ea37f04c2fbd5bc6eff1f.jpg",
    "https://i.pinimg.com/736x/07/08/06/0708066f9554f28851da80a4530cc01a.jpg",
    "https://i.pinimg.com/736x/3d/fd/e2/3dfde278d05bf8ff433c1725c2779f7d.jpg",
    "https://i.pinimg.com/736x/8b/d9/5d/8bd95d7745e31655ef08c783a89e9985.jpg",
    "https://i.pinimg.com/736x/85/60/2c/85602cb2fed1f78ca33ff498503f1a2d.jpg",
    "https://i.pinimg.com/736x/b6/60/56/b6605629d32513820be82c161736c381.jpg",
    "https://i.pinimg.com/736x/69/62/29/696229a2d930c02da36bafee5a69f4c1.jpg",
    "https://i.pinimg.com/736x/13/08/ab/1308ab0fdc9cc301dea444385324908b.jpg",
    "https://i.pinimg.com/736x/93/b8/25/93b825e845c6cb96f73dcff437d1f899.jpg",
    "https://i.pinimg.com/736x/56/43/28/5643288ca447f84aeae3cd352acc30d9.jpg"
]

hoian_urls = [
    "https://i.pinimg.com/736x/1c/34/2c/1c342c37646a702737776eeb4ccd627b.jpg",
    "https://i.pinimg.com/736x/59/77/94/597794c5218a63958050929b8f241dba.jpg",
    "https://i.pinimg.com/736x/aa/64/09/aa64098c1a13e819ae28febf305a8b18.jpg",
    "https://i.pinimg.com/736x/47/a2/6c/47a26c84d2e1fdfc5520706842bacbd1.jpg",
    "https://i.pinimg.com/736x/30/43/3a/30433acea2db7c9081168470d5026cc8.jpg",
    "https://i.pinimg.com/736x/c3/ca/3f/c3ca3fa1c958467ed5444498821302ad.jpg",
    "https://i.pinimg.com/736x/bd/b0/fe/bdb0fe72285f4ea5ab5ade7837496298.jpg",
    "https://i.pinimg.com/736x/06/b3/4c/06b34c6fcd0ae864a687728629257dbf.jpg",
    "https://i.pinimg.com/736x/ba/9c/c2/ba9cc20e7c972f72fcf128973e290995.jpg",
    "https://i.pinimg.com/736x/26/9f/9e/269f9e356a81ec96520fabebb0d9eeb3.jpg"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

def download(urls, prefix):
    for i, url in enumerate(urls):
        fname = f"{prefix}_{i+1}.jpg"
        fpath = os.path.join(SAVE_DIR, fname)
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
            with open(fpath, 'wb') as f:
                f.write(data)
            print(f"[OK] {fname}")
            time.sleep(0.5)
        except Exception as e:
            print(f"[FAIL] {fname}: {e}")

print("Downloading Da Nang images...")
download(danang_urls, "danang")
print("\nDownloading Hoi An images...")
download(hoian_urls, "hoian")
