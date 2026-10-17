import os
import glob
import re
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_dir = "data/kabir/raw/html"
sakhi_files = sorted(glob.glob(os.path.join(html_dir, "Sakhi-*-Ang-*.html")))

total_sakhis = 0
ang_stats = []

for sf in sakhi_files:
    fname = os.path.basename(sf)
    with open(sf, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    title = soup.title.string.strip() if soup.title else fname
    text = soup.get_text()
    markers = re.findall(r'॥\s*(\d+)\s*॥', text)
    count = len(markers)
    total_sakhis += count
    ang_stats.append((fname, title, count))

print(f"Total Angs: {len(sakhi_files)}")
print(f"Total individual Sakhis across all Angs: {total_sakhis}")
print("\nTop 10 Angs by Sakhi count:")
for fn, t, c in sorted(ang_stats, key=lambda x: x[2], reverse=True)[:10]:
    print(f"  {fn} ({c} Sakhis): {t}")
