import os
import re
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_MD = os.path.join(BASE_DIR, "Bulleh_Shah_Kafian.md")
DATA_DIR = os.path.join(BASE_DIR, "data")
KAFIAN_DIR = os.path.join(DATA_DIR, "kafian")
RAW_OUTPUT_JSON = os.path.join(DATA_DIR, "raw_kafian.json")
CHECKPOINT_JSON = os.path.join(DATA_DIR, "checkpoint.json")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(KAFIAN_DIR, exist_ok=True)

with open(SOURCE_MD, "r", encoding="utf-8") as f:
    text = f.read()

# Split into poems based on '## <number>. '
# Notice poems start after the TOC.
sections = re.split(r'\n# (भाग \d+ [^\n]+)\n', text)

raw_kafian = []

# sections[0] is header + TOC
for i in range(1, len(sections), 2):
    sec_name = sections[i].strip()
    sec_body = sections[i+1]
    
    # Split by ## <num>.
    poem_chunks = re.split(r'\n## (\d+)\.\s*([^\n]+)\n', sec_body)
    for j in range(1, len(poem_chunks), 3):
        k_id = int(poem_chunks[j])
        k_title_text = poem_chunks[j+1].strip()
        k_full_title = f"{k_id}. {k_title_text}"
        k_body = poem_chunks[j+2]
        
        # Remove trailing horizontal rule or extra blank lines
        k_body = re.sub(r'\n---\s*$', '', k_body.strip()).strip()
        
        # Split into stanzas (separated by double newlines)
        stanzas_raw = k_body.split('\n\n')
        stanzas = []
        for s in stanzas_raw:
            # Clean each line (strip trailing spaces/markdown line breaks)
            lines = [re.sub(r'\s{2,}$', '', line).strip() for line in s.split('\n') if line.strip()]
            if lines:
                stanzas.append(lines)
        
        raw_kafian.append({
            "id": k_id,
            "title": k_full_title,
            "section": sec_name,
            "stanzas": stanzas
        })

# Sort by id
raw_kafian.sort(key=lambda x: x["id"])

with open(RAW_OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(raw_kafian, f, ensure_ascii=False, indent=2)

# Initialize checkpoint if not present
if not os.path.exists(CHECKPOINT_JSON):
    checkpoint = {
        "total_kafian": len(raw_kafian),
        "completed_count": 0,
        "completed_ids": [],
        "last_updated": None,
        "status": "ready"
    }
    with open(CHECKPOINT_JSON, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)

print(f"Successfully extracted {len(raw_kafian)} Kafian into {RAW_OUTPUT_JSON}")
print(f"Initialized checkpoint at {CHECKPOINT_JSON}")
