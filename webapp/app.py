import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))
CANONICAL_DIR = os.path.join(ROOT_DIR, 'thesis-system', 'webapp')

for p in [CANONICAL_DIR, ROOT_DIR, BASE_DIR]:
    if p not in sys.path:
        sys.path.insert(0, p)

canonical_app = os.path.join(CANONICAL_DIR, 'app.py')
with open(canonical_app, 'r', encoding='utf-8') as f:
    code = f.read()

exec(compile(code, canonical_app, 'exec'))
