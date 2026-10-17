import urllib.request
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

pages = [
    "Sakhi-Bhakt-Kabir-Ji.php",
    "Pad-Bhakt-Kabir-Ji.php",
    "Kabir-Granthavali-Shyam-Sundar-Das.php",
    "HindiSalokBhagatKabir.php",
    "HindiDoheBhagatKabir.php",
    "HindiPadBhagatKabir.php",
    "Ramaini-Bhakt-Kabir-Ji.php"
]

base_url = "https://hindi-kavita.com/"

for page in pages:
    url = base_url + page
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            print(f"================== {page} ==================")
            # Check links
            links = []
            for a in soup.find_all('a', href=True):
                h = a['href']
                t = a.get_text(strip=True)
                if '.php' in h and not any(x in h for x in ['HindiPoetry', 'HindiPunjabiKavita', 'hindikahani', 'hindikavitacontactus', 'index']):
                    links.append((h, t))
            print(f"Unique internal poem/section links ({len(links)}):")
            for h, t in links[:15]:
                print(f"   {h} -> {t}")
            if len(links) > 15:
                print(f"   ... and {len(links)-15} more")
                
            # Check text structure
            # Count paragraphs or verses
            ps = [p.get_text(strip=True) for p in soup.find_all('p') if len(p.get_text(strip=True)) > 20]
            print(f"Significant paragraphs: {len(ps)}")
            if ps:
                print(f"First p preview: {ps[0][:100]}...")
    except Exception as e:
        print(f"Error for {page}: {e}")
