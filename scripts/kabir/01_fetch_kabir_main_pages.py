import urllib.request
import time
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

urls = [
    ("BhaktKabir.html", "https://hindi-kavita.com/BhaktKabir.php"),
    ("ShabadBhaktKabirJi.html", "https://hindi-kavita.com/ShabadBhaktKabirJi.php"),
    ("HindiShabadBhagatKabir.html", "https://hindi-kavita.com/HindiShabadBhagatKabir.php"),
    ("HindiSalokBhagatKabir.html", "https://hindi-kavita.com/HindiSalokBhagatKabir.php"),
    ("HindiDoheBhagatKabir.html", "https://hindi-kavita.com/HindiDoheBhagatKabir.php"),
    ("HindiPadBhagatKabir.html", "https://hindi-kavita.com/HindiPadBhagatKabir.php"),
    ("Sakhi-Bhakt-Kabir-Ji.html", "https://hindi-kavita.com/Sakhi-Bhakt-Kabir-Ji.php"),
    ("Pad-Bhakt-Kabir-Ji.html", "https://hindi-kavita.com/Pad-Bhakt-Kabir-Ji.php"),
    ("Ramaini-Bhakt-Kabir-Ji.html", "https://hindi-kavita.com/Ramaini-Bhakt-Kabir-Ji.php"),
    ("Kabir-Granthavali-Shyam-Sundar-Das.html", "https://hindi-kavita.com/Kabir-Granthavali-Shyam-Sundar-Das.php"),
]

os.makedirs("data/kabir/raw/html", exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for fname, url in urls:
    filepath = os.path.join("data/kabir/raw/html", fname)
    if os.path.exists(filepath) and os.path.getsize(filepath) > 1000:
        print(f"Already cached: {fname} ({os.path.getsize(filepath)} bytes)")
        continue
    print(f"Fetching {url} -> {fname}...")
    success = False
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                content = resp.read()
                with open(filepath, 'wb') as f:
                    f.write(content)
                print(f"Saved {fname} ({len(content)} bytes)")
                success = True
                break
        except Exception as e:
            print(f"Attempt {attempt+1} failed for {url}: {e}")
            time.sleep(2)
    if not success:
        print(f"FAILED to download {url}")
