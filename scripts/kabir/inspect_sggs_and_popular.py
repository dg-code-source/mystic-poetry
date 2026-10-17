import urllib.request
from bs4 import BeautifulSoup
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

pages = [
    "HindiShabadBhagatKabir.php",
    "HindiSalokBhagatKabir.php",
    "HindiDoheBhagatKabir.php",
    "HindiPadBhagatKabir.php"
]

base_url = "https://hindi-kavita.com/"

for page in pages:
    url = base_url + page
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
        with open(f"data/kabir/raw/html/{page}.html", "w", encoding="utf-8") as f:
            f.write(html)
            
        soup = BeautifulSoup(html, 'html.parser')
        print(f"\n=================== {page} ===================")
        print(f"Saved {page}.html ({len(html)} bytes)")
        
        # Look for headings and paragraphs
        h2s = soup.find_all(['h2', 'h3'])
        print(f"Headings count: {len(h2s)}")
        for h in h2s[:5]:
            print(f"  H: {h.get_text(strip=True)}")
            
        # Count numbers in text or verses
        # In Salok, check how many saloks: look for ॥१॥, ॥२॥, etc.
        salok_matches = re.findall(r'॥(\d+)॥', soup.get_text())
        if salok_matches:
            print(f"Salok number markers found: {len(salok_matches)}, max: {max(int(x) for x in salok_matches if x.isdigit())}")
            
    except Exception as e:
        print(f"Error {page}: {e}")
