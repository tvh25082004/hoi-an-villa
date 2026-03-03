import requests
import json
import re

session = requests.Session()
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*, q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.pinterest.com/',
    'X-Requested-With': 'XMLHttpRequest',
}

# First get cookies
resp0 = session.get('https://www.pinterest.com/', headers={
    'User-Agent': HEADERS['User-Agent']
}, timeout=15)
print(f"Homepage cookies: {list(session.cookies.keys())}")

# Extract CSRF token
csrftoken = session.cookies.get('csrftoken', '')
print(f"CSRF token: {csrftoken[:20]}...")

# Try Pinterest search resource API
HEADERS['X-CSRFToken'] = csrftoken

# Method 1: Resource API
search_data = {
    "options": {
        "query": "da nang city vietnam",
        "scope": "pins",
        "no_fetch_context_on_resource": False
    },
    "context": {}
}

api_url = 'https://www.pinterest.com/resource/BaseSearchResource/get/'
params = {
    'source_url': '/search/pins/?q=da+nang+city+vietnam',
    'data': json.dumps(search_data),
}

resp = session.get(api_url, headers=HEADERS, params=params, timeout=15)
print(f"\nAPI Status: {resp.status_code}")
print(f"Response length: {len(resp.text)}")
print(f"Content type: {resp.headers.get('content-type', 'unknown')}")

try:
    data = resp.json()
    # Find image URLs
    def find_images(obj, found=None):
        if found is None:
            found = set()
        if isinstance(obj, str):
            if 'pinimg.com' in obj and ('originals' in obj or '736x' in obj or '564x' in obj or '474x' in obj):
                found.add(obj)
        elif isinstance(obj, dict):
            for v in obj.values():
                find_images(v, found)
        elif isinstance(obj, list):
            for item in obj:
                find_images(item, found)
        return found
    
    imgs = find_images(data)
    print(f"\nFound {len(imgs)} image URLs!")
    for i, img in enumerate(sorted(imgs)[:15]):
        print(f"  {i+1}. {img}")
    
    # Save full response
    with open('pinterest_api_resp.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("\nSaved pinterest_api_resp.json")
except Exception as e:
    print(f"Error parsing JSON: {e}")
    print(f"First 500 chars: {resp.text[:500]}")
