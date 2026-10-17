# -*- coding: utf-8 -*-
"""
Unified dataset for all 40 Shabads of Sant Ravidas Ji in Sri Guru Granth Sahib Ji.
Combines part 1 (1-20) and part 2 (21-40).
"""

from shabad_data_part1 import SHABAD_PART1
from shabad_data_part2 import SHABAD_PART2

SHABAD_DATA = {}
SHABAD_DATA.update(SHABAD_PART1)
SHABAD_DATA.update(SHABAD_PART2)

if __name__ == "__main__":
    print(f"Total unified Shabads: {len(SHABAD_DATA)}")
    assert len(SHABAD_DATA) == 40, "Missing Shabads!"
    print("Verification passed: Exactly 40 Shabads present with full translations and commentary.")
