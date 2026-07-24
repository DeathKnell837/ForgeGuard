import os, base64

with open(r"c:\Users\USER\Desktop\THESIS\thesis-system\webapp\cyber_background.jpg", "rb") as f:
    b64_content = base64.b64encode(f.read()).decode()

print("Background Base64 ready, length:", len(b64_content))
