# -*- coding: utf-8 -*-
"""
Unified Sant Ravidas Padaavali Poetic Translations and Commentary Data
Merges all 4 batches (Padas 1 to 117).
"""

try:
    from padaavali_data_batch1 import PADAAVALI_BATCH1
    from padaavali_data_batch2 import PADAAVALI_BATCH2
    from padaavali_data_batch3 import PADAAVALI_BATCH3
    from padaavali_data_batch4 import PADAAVALI_BATCH4
except ImportError:
    from scripts.sant_ravidas.padaavali_data_batch1 import PADAAVALI_BATCH1
    from scripts.sant_ravidas.padaavali_data_batch2 import PADAAVALI_BATCH2
    from scripts.sant_ravidas.padaavali_data_batch3 import PADAAVALI_BATCH3
    from scripts.sant_ravidas.padaavali_data_batch4 import PADAAVALI_BATCH4

PADAAVALI_DATA = {}
PADAAVALI_DATA.update(PADAAVALI_BATCH1)
PADAAVALI_DATA.update(PADAAVALI_BATCH2)
PADAAVALI_DATA.update(PADAAVALI_BATCH3)
PADAAVALI_DATA.update(PADAAVALI_BATCH4)

assert len(PADAAVALI_DATA) == 117, f"Expected 117 Padas, found {len(PADAAVALI_DATA)}"

if __name__ == "__main__":
    print(f"Successfully loaded and unified all {len(PADAAVALI_DATA)} Padaavali entries!")
    print(f"Padas range: {min(PADAAVALI_DATA.keys())} to {max(PADAAVALI_DATA.keys())}")
