# -*- coding: utf-8 -*-
import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for name, url in [('Padaavali', 'https://hindi-kavita.com/HindiPoetryBhagatRavidas.php'), ('Dohe', 'https://hindi-kavita.com/HindiDoheBhagatRavidas.php')]:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
    print(f"\n==================== {name} ====================")
    # Check for anchors or headings or poem titles
    titles = re.findall(r'<h[234][^>]*>(.*?)</h[234]>', html, re.DOTALL)
    print(f"Total headings (h2-h4): {len(titles)}")
    for t in titles[:10]:
        print("  H:", re.sub(r'<[^>]+>', '', t).strip())
    
    # Check for links or poem separators
    poem_links = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.DOTALL)
    sub_links = [(h, re.sub(r'<[^>]+>', '', t).strip()) for h, t in poem_links if '#' in h or 'ravidas' in h.lower()]
    print(f"Sub poem links with #: {len(sub_links)}")
    for h, t in sub_links[:10]:
        print(f"  {h} -> {t}")
