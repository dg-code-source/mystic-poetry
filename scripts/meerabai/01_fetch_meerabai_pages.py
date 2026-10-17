# -*- coding: utf-8 -*-
"""
01_fetch_meerabai_pages.py
Download and locally cache all 9 parts of Mirabai's Padavali from hindi-kavita.com.
Saves to data/meerabai/raw/html/part_1.html ... part_9.html.
"""

import os
import sys
import time
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HTML_DIR = os.path.join(BASE_DIR, "data", "meerabai", "raw", "html")
os.makedirs(HTML_DIR, exist_ok=True)

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def fetch_with_retry(url, retries=3, delay=3, timeout=30):
    for attempt in range(1, retries + 1):
        try:
            print(f"  Attempt {attempt} fetching {url}...")
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = resp.read().decode('utf-8', errors='ignore')
                print(f"  Successfully fetched ({len(data):,} bytes)")
                return data
        except Exception as e:
            print(f"  Attempt {attempt} failed: {e}")
            if attempt < retries:
                time.sleep(delay)
            else:
                raise

def main():
    print("=" * 60)
    print("CRAWLING ALL 9 PARTS OF SANT MIRABAI PADAVALI")
    print("=" * 60)

    for i in range(1, 10):
        suffix = str(i) if i > 1 else ""
        url = f"https://hindi-kavita.com/HindiPoetrySantMeeraBai{suffix}.php"
        out_path = os.path.join(HTML_DIR, f"part_{i}.html")

        if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
            print(f"Part {i}: Already cached at {out_path} ({os.path.getsize(out_path):,} bytes). Skipping.")
            continue

        print(f"\nPart {i}: Fetching from {url}...")
        try:
            html = fetch_with_retry(url)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Part {i}: Saved to {out_path}")
            time.sleep(1) # courteous delay
        except Exception as e:
            print(f"Part {i}: Failed completely: {e}")

    print("\nFetch complete. All available parts cached in data/meerabai/raw/html/")

if __name__ == "__main__":
    main()
