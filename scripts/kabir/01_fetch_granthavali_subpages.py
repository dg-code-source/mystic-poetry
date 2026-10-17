import urllib.request
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.stdout.reconfigure(encoding='utf-8')

# Read subpage links from Sakhi and Pad
from bs4 import BeautifulSoup

def get_links():
    urls = []
    # Sakhi
    if os.path.exists('data/kabir/raw/html/Sakhi-Bhakt-Kabir-Ji.html'):
        with open('data/kabir/raw/html/Sakhi-Bhakt-Kabir-Ji.html', 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        for a in soup.find_all('a', href=True):
            h = a['href']
            if 'Sakhi-' in h and h != 'Sakhi-Bhakt-Kabir-Ji.php':
                urls.append(h)
                
    # Pad
    if os.path.exists('data/kabir/raw/html/Pad-Bhakt-Kabir-Ji.html'):
        with open('data/kabir/raw/html/Pad-Bhakt-Kabir-Ji.html', 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        for a in soup.find_all('a', href=True):
            h = a['href']
            if 'Pad-' in h and h != 'Pad-Bhakt-Kabir-Ji.php':
                urls.append(h)
                
    return sorted(list(set(urls)))

subpages = get_links()
print(f"Total Granthavali subpages to fetch: {len(subpages)}")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
base_url = "https://hindi-kavita.com/"

def download_one(filename):
    outpath = os.path.join("data/kabir/raw/html", filename.replace('.php', '.html'))
    if os.path.exists(outpath) and os.path.getsize(outpath) > 1000:
        return filename, True, "Already cached"
    
    url = base_url + filename
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = resp.read()
            with open(outpath, 'wb') as f:
                f.write(data)
            return filename, True, f"Downloaded {len(data)} bytes"
        except Exception as e:
            time.sleep(1)
            err = str(e)
    return filename, False, err

# Download using ThreadPoolExecutor
success_count = 0
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(download_one, sp): sp for sp in subpages}
    for f in as_completed(futures):
        fn, ok, msg = f.result()
        if ok:
            success_count += 1
            if "Downloaded" in msg:
                print(f"[{success_count}/{len(subpages)}] {fn}: {msg}")
        else:
            print(f"[FAIL] {fn}: {msg}")

print(f"\nFinished: {success_count}/{len(subpages)} pages cached.")
