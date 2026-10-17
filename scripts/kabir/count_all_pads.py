import os
import glob
import re
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_dir = "data/kabir/raw/html"
pad_files = sorted(glob.glob(os.path.join(html_dir, "Pad-Raag-*.html")))

total_pads = 0
pad_stats = []

for pf in pad_files:
    fname = os.path.basename(pf)
    with open(pf, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    title = soup.title.string.strip() if soup.title else fname
    text = soup.get_text()
    # In pads, each pad usually has ॥टेक॥ or number markers
    # Let's count pads
    # Count occurrences of टेक or number markers
    markers = re.findall(r'॥\s*(\d+)\s*॥', text)
    count = len(markers)
    total_pads += count
    pad_stats.append((fname, title, count))

print(f"Total Pad Raags: {len(pad_files)}")
print(f"Total Pad markers across all Raags: {total_pads}")
for fn, t, c in pad_stats:
    print(f"  {fn} ({c} markers): {t}")
