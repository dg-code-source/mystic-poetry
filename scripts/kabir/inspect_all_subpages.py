import urllib.request
from bs4 import BeautifulSoup
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

pages = [
    "ShabadBhaktKabirJi.php",
    "HindiSalokBhagatKabir.php",
    "HindiDoheBhagatKabir.php",
    "HindiPadBhagatKabir.php",
    "Sakhi-Bhakt-Kabir-Ji.php",
    "Pad-Bhakt-Kabir-Ji.php",
    "Ramaini-Bhakt-Kabir-Ji.php",
    "Prastavna-Kabir-Granthavali-Shyam-Sundar-Das.php",
    "Kabir-Granthavali-Shyam-Sundar-Das.php",
    "HindiCompleteBaniBhagatKabirJi.php",
    "HindiShabadBhagatKabir.php"
]

base_url = "https://hindi-kavita.com/"

for page in pages:
    url = base_url + page
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string.strip() if soup.title else ""
            anchors = [a['id'] for a in soup.find_all(['a', 'div', 'p', 'span'], id=True) if a.get('id')]
            links_in_page = [a['href'] for a in soup.find_all('a', href=True) if '.php' in a['href']]
            # Check for poem containers or titles
            h2s = [h.get_text(strip=True) for h in soup.find_all(['h2', 'h3'])]
            print(f"=== {page} ===")
            print(f"  Title: {title}")
            print(f"  HTML size: {len(html)} bytes")
            print(f"  IDs found: {len(anchors)}")
            print(f"  H2/H3 count: {len(h2s)} (e.g. {h2s[:3]})")
            print(f"  Links to .php: {len(links_in_page)}")
            # Sample first anchor
            if anchors:
                print(f"  Sample IDs: {anchors[:5]}")
    except Exception as e:
        print(f"=== {page} === Error: {e}")
