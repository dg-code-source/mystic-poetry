# -*- coding: utf-8 -*-
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for name in ['gandhan', 'dohre', 'siharfian']:
    path = f'data/raw_other_works/{name}.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    print(f'==============================')
    print(f'=== {name.upper()} ===')
    print(f'==============================')
    h2_idx = html.find('</h2>')
    snippet = html[h2_idx+5:h2_idx+2000] if h2_idx != -1 else html[:2000]
    # Remove script and style tags
    clean_snippet = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', snippet, flags=re.DOTALL)
    print(clean_snippet[:1500])
