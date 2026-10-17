# -*- coding: utf-8 -*-
import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://hindi-kavita.com/SantRavidas.php'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

# Collect all section headers and their links
sections = re.findall(r'<div class="content-section">(.*?)</div>\s*</div>', html, re.DOTALL)
if not sections:
    sections = re.findall(r'<div class="content-section">(.*?)</div>', html, re.DOTALL)

print(f"Total content sections found: {len(sections)}")

for i, sec in enumerate(sections):
    title_m = re.search(r'<h[23][^>]*>(.*?)</h[23]>', sec, re.DOTALL)
    title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else f"Section {i+1}"
    links = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', sec, re.DOTALL)
    print(f"\n--- {title} (Total links: {len(links)}) ---")
    for h, t in links[:15]:
        ct = re.sub(r'<[^>]+>', '', t).strip()
        print(f"  {h} -> {ct}")
    if len(links) > 15:
        print(f"  ... and {len(links) - 15} more")

# Check linked pages: Shabad, Pad, Dohe
targets = [
    ("Shabad (Guru Granth Sahib)", "https://hindi-kavita.com/HindiShabadBhagatRavidas.php"),
    ("Padaavali", "https://hindi-kavita.com/HindiPoetryBhagatRavidas.php"),
    ("Dohe", "https://hindi-kavita.com/HindiDoheBhagatRavidas.php"),
]

for label, turl in targets:
    try:
        treq = urllib.request.Request(turl, headers={'User-Agent': 'Mozilla/5.0'})
        thtml = urllib.request.urlopen(treq).read().decode('utf-8', errors='ignore')
        tlinks = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', thtml, re.DOTALL)
        # Count anchor targets or poem blocks
        anchors = re.findall(r'id=["\'](Ravidas\d+)["\']', thtml)
        if not anchors:
            anchors = re.findall(r'name=["\'](Ravidas\d+)["\']', thtml)
        print(f"\nTarget: {label} ({turl}) -> Bytes: {len(thtml)}, Poem anchors: {len(anchors)}")
    except Exception as e:
        print(f"Error checking {label}: {e}")
