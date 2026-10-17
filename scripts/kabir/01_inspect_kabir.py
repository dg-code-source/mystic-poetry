import urllib.request
import re
import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://hindi-kavita.com/BhaktKabir.php'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

print(f"Fetching {url}...")
try:
    with urllib.request.urlopen(req, timeout=20) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Save the landing page HTML
    with open('data/kabir/raw/html/BhaktKabir.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Saved BhaktKabir.html ({len(html)} bytes)")
    
    # Extract all links
    links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        text = a.get_text(strip=True)
        if '.php' in href:
            links.append((href, text))
            
    print(f"\nFound {len(links)} links:")
    for href, text in links:
        print(f"  {href} -> {text}")
        
except Exception as e:
    print(f"Error: {e}")
