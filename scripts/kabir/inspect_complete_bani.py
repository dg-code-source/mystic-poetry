import urllib.request
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://hindi-kavita.com/HindiCompleteBaniBhagatKabirJi.php"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    soup = BeautifulSoup(html, 'html.parser')
    print("Title:", soup.title.string.strip() if soup.title else "")
    for a in soup.find_all('a', href=True):
        if '.php' in a['href']:
            print("  Link:", a['href'], "->", a.get_text(strip=True))
    for p in soup.find_all('p'):
        text = p.get_text(strip=True)
        if len(text) > 10:
            print("  P text:", text[:150])
except Exception as e:
    print("Error:", e)
