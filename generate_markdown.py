import sys
import urllib.request
import re
import unicodedata

urls = [
    ('भाग 1 (काफ़ियां 1–50)', '', 1, 50),
    ('भाग 2 (काफ़ियां 51–100)', '', 51, 100),
    ('भाग 3 (काफ़ियां 101–160)', '', 101, 160)
]

def gfm_slug(text):
    text = text.strip().lower()
    clean = []
    for ch in text:
        cat = unicodedata.category(ch)
        if cat.startswith('L') or cat.startswith('M') or cat.startswith('N') or cat == 'Pd' or ch.isspace() or ch == '-':
            clean.append(ch)
    s = ''.join(clean)
    s = re.sub(r'[\s]+', '-', s)
    return s.strip('-')

def clean_poem(content_chunk):
    cutoff_match = re.search(r'<(div|footer|ul|form)', content_chunk, re.IGNORECASE)
    poem_html = content_chunk[:cutoff_match.start()] if cutoff_match else content_chunk
    
    poem_html = re.sub(r'(<br\s*/?>\s*){2,}', '\n\n', poem_html, flags=re.IGNORECASE)
    poem_html = re.sub(r'</p>\s*<p[^>]*>', '\n\n', poem_html, flags=re.IGNORECASE)
    poem_html = re.sub(r'<br\s*/?>', '\n', poem_html, flags=re.IGNORECASE)
    poem_text = re.sub(r'<[^>]+>', '', poem_html).strip()
    
    raw_stanzas = poem_text.split('\n\n')
    cleaned_stanzas = []
    for s in raw_stanzas:
        lines = [line.strip() for line in s.split('\n') if line.strip()]
        if lines:
            cleaned_stanzas.append('  \n'.join(lines))
    return '\n\n'.join(cleaned_stanzas)

sections = []

for section_name, url, start_num, end_num in urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='replace')
    parts = re.split(r'<h3[^>]*>', html, flags=re.IGNORECASE)
    
    kafian_list = []
    for p in parts[1:]:
        title_chunk, content_chunk = p.split('</h3>', 1)
        title = re.sub(r'<[^>]+>', '', title_chunk).strip()
        if '51-100' in title or '101-160' in title:
            continue
        cleaned = clean_poem(content_chunk)
        m = re.match(r'^(\d+)\.\s*(.*)', title)
        if m:
            num = int(m.group(1))
            t_text = m.group(2).strip()
        else:
            num = 0
            t_text = title
        kafian_list.append((num, title, t_text, cleaned))
    sections.append((section_name, url, kafian_list))

md = []
md.append('# बाबा बुल्ले शाह : सम्पूर्ण काफ़ियां (1–160)')
md.append('## Baba Bulleh Shah : Complete Kafian in Hindi\n')
md.append('> **प्रमाणिक संकलन:** बाबा बुल्ले शाह जी की 160 काफ़ियों का देवनागरी संकलन\n')
md.append('---\n')
md.append('## विषय-सूची (Table of Contents)\n')

for sec_name, sec_url, k_list in sections:
    md.append(f'### {sec_name}\n')
    for num, full_title, t_text, _ in k_list:
        slug = gfm_slug(full_title)
        md.append(f'- [{full_title}](#{slug})')
    md.append('')

md.append('---\n')

for sec_name, sec_url, k_list in sections:
    md.append(f'# {sec_name}\n')
    for num, full_title, t_text, poem in k_list:
        md.append(f'## {full_title}\n')
        md.append(poem)
        md.append('\n---\n')

content = '\n'.join(md)

with open(r'c:\my-code\Bulleh-Shah\Bulleh_Shah_Kafian.md', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'File successfully written to c:\\my-code\\Bulleh-Shah\\Bulleh_Shah_Kafian.md')
print(f'Total size: {len(content.encode("utf-8"))} bytes')
print(f'Total lines: {len(content.splitlines())}')
