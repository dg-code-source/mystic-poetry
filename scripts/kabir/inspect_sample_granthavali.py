import urllib.request
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

sample_urls = [
    "Sakhi-Gurudev-Ko-Ang-Bhakt-Kabir-Ji.php",
    "Sakhi-Sumiran-Ko-Ang-Bhakt-Kabir-Ji.php",
    "Pad-Raag-Gaudi-Bhakt-Kabir-Ji.php"
]

base_url = "https://hindi-kavita.com/"

for page in sample_urls:
    url = base_url + page
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            print(f"=== {page} ===")
            print(f"Title: {soup.title.string.strip() if soup.title else ''}")
            print(f"HTML size: {len(html)} bytes")
            # Look for poem text
            p_text = [p.get_text(separator='\n', strip=True) for p in soup.find_all('p') if len(p.get_text(strip=True)) > 30]
            print(f"Paragraphs count: {len(p_text)}")
            if p_text:
                print(f"First 200 chars:\n{p_text[0][:200]}...\n")
    except Exception as e:
        print(f"Error {page}: {e}")
