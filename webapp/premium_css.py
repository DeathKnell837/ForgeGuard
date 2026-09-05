import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))
CANONICAL_DIR = os.path.join(ROOT_DIR, 'thesis-system', 'webapp')

if CANONICAL_DIR not in sys.path:
    sys.path.insert(0, CANONICAL_DIR)

from premium_css import PREMIUM_CSS
