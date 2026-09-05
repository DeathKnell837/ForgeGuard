"""
ForgeGuard — Streamlit Cloud Entrypoint
========================================
Redirects execution to canonical application in thesis-system/webapp/app.py
BSCS Thesis: "Securing Mobile Transaction: A Comparative Evaluation of
CNN Architectures in Detecting Digital Receipt Forgery"
Notre Dame of Midsayap College (NDMC) | CITE
Authors: Ungab and Bacanto | Adviser: Ms. Doris Ann Mariano
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WEBAPP_DIR = os.path.join(BASE_DIR, "thesis-system", "webapp")

for p in [WEBAPP_DIR, BASE_DIR]:
    if p not in sys.path:
        sys.path.insert(0, p)

# Execute canonical app
canonical_app = os.path.join(WEBAPP_DIR, "app.py")
with open(canonical_app, "r", encoding="utf-8") as f:
    code = f.read()

exec(compile(code, canonical_app, "exec"))

