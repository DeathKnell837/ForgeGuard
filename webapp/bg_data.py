"""
Base64 background data module
"""
import base64
import os

APP_DIR = os.path.dirname(os.path.abspath(__file__))
BG_FILE = os.path.join(APP_DIR, "cyber_background.jpg")

if os.path.exists(BG_FILE):
    with open(BG_FILE, "rb") as f:
        BG_BASE64 = base64.b64encode(f.read()).decode("utf-8")
else:
    BG_BASE64 = ""
