import urllib.request
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Get Sakhi-Bhakt-Kabir-Ji.php
url = "https://hindi-kavita.com/Sakhi-Bhakt-Kabir-Ji.php"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    soup = BeautifulSoup(html, 'html.parser')
    sakhi_links = []
    for a in soup.find_all('a', href=True):
        if 'Sakhi-' in a['href'] and a['href'] != 'Sakhi-Bhakt-Kabir-Ji.php':
            sakhi_links.append((a['href'], a.get_text(strip=True)))
    print(f"Sakhi Angs count: {len(sakhi_links)}")
    for h, t in sakhi_links[:10]:
        print(f"  {h} -> {t}")
except Exception as e:
    print(f"Error: {e}")

# Get Pad-Bhakt-Kabir-Ji.php
url2 = "https://hindi-kavita.com/Pad-Bhakt-Kabir-Ji.php"
req2 = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req2, timeout=15) as resp:
        html2 = resp.read().decode('utf-8', errors='ignore')
    soup2 = BeautifulSoup(html2, 'html.parser')
    pad_links = []
    for a in soup2.find_all('a', href=True):
        if 'Pad-Raag-' in a['href']:
            pad_links.append((a['href'], a.get_text(strip=True)))
    print(f"\nPad Raags count: {len(pad_links)}")
    for h, t in pad_links:
        print(f"  {h} -> {t}")
except Exception as e:
    print(f"Error: {e}")
