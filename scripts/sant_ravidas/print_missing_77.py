# -*- coding: utf-8 -*-
import sys
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(BASE_DIR, "scripts", "sant_ravidas"))

from vocab_slice1 import VOCAB_SLICE1
from vocab_slice2 import VOCAB_SLICE2
from vocab_slice3 import VOCAB_SLICE3
from vocab_slice4 import VOCAB_SLICE4

# Load CORE_DICT
spec_path = os.path.join(BASE_DIR, "scripts", "sant_ravidas", "build_complete_ravidas_dictionary.py")
import importlib.util
spec = importlib.util.spec_from_file_location("build_dict", spec_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
core = mod.CORE_DICT

WORDS_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "words_shabad_dohe.json")
OLD_SD_PATH = os.path.join(BASE_DIR, "data", "sant_ravidas", "shabad_dohe_lexicon.json")

words = json.load(open(WORDS_PATH, encoding='utf-8'))
old_sd = json.load(open(OLD_SD_PATH, encoding='utf-8'))

valid_old = {k: v for k, v in old_sd.items() if "प्रभु-वचन" not in v.get("hi", "") and "holy word" not in v.get("en", "") and v.get("hi", "") != k}

known = set(valid_old.keys()) | set(core.keys()) | set(VOCAB_SLICE1.keys()) | set(VOCAB_SLICE2.keys()) | set(VOCAB_SLICE3.keys()) | set(VOCAB_SLICE4.keys())

missing = [w for w in words if w not in known]
print(f"Total missing: {len(missing)}")
for i, m in enumerate(missing):
    print(f'    "{m}": ("{mod.romanize(m)}", "", ""),')
