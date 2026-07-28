"""Test the improved regional ELA differential heuristic"""
import sys, os
sys.path.insert(0, r"c:\Users\USER\Desktop\THESIS\thesis-system")

import numpy as np
from PIL import Image
from preprocessing.ela import compute_ela

AUTHENTIC_DIR = r"c:\Users\USER\Desktop\THESIS\thesis-system\dataset\authentic\compressed"
FORGED_DIR = r"c:\Users\USER\Desktop\THESIS\thesis-system\dataset\forged\compressed\amount_alteration"

def test_regional_heuristic(img_path, label):
    pil_img = Image.open(img_path).convert("RGB")
    ela_img = compute_ela(pil_img, quality=90, scale=15.0)
    ela_np = np.array(ela_img, dtype=np.float32)
    h_ela, w_ela = ela_np.shape[:2]
    
    center_start = int(h_ela * 0.2)
    center_end = int(h_ela * 0.8)
    center_band = ela_np[center_start:center_end, :, :]
    top_band = ela_np[:center_start, :, :]
    bottom_band = ela_np[center_end:, :, :]
    
    center_mean = float(np.mean(center_band))
    edge_mean = float(np.mean(np.concatenate([top_band, bottom_band], axis=0)))
    regional_diff = abs(center_mean - edge_mean)
    overall_mean = float(np.mean(ela_np))
    overall_var = float(np.var(ela_np))
    
    is_forged = regional_diff > 3.0 or overall_mean > 18.0
    correct = (label == "AUTHENTIC" and not is_forged) or (label == "FORGED" and is_forged)
    verdict = "FORGED" if is_forged else "AUTHENTIC"
    status = "[OK]" if correct else "[FAIL]"
    
    return f"  [{label:9s}] {os.path.basename(img_path):35s} -> {verdict:10s} regDiff={regional_diff:.2f}, mean={overall_mean:.1f}, var={overall_var:.1f} {status}"

print("=" * 120)
print("TEST: REGIONAL ELA DIFFERENTIAL HEURISTIC")
print("=" * 120)

print("\n-- AUTHENTIC IMAGES --")
auth_files = sorted([f for f in os.listdir(AUTHENTIC_DIR) if f.endswith('.jpg')])[:15]
auth_ok = 0
for f in auth_files:
    r = test_regional_heuristic(os.path.join(AUTHENTIC_DIR, f), "AUTHENTIC")
    print(r)
    if "[OK]" in r: auth_ok += 1

print("\n-- FORGED IMAGES --")
forge_ok = 0
forged_files = sorted([f for f in os.listdir(FORGED_DIR) if f.endswith('.jpg')])[:15]
for f in forged_files:
    r = test_regional_heuristic(os.path.join(FORGED_DIR, f), "FORGED")
    print(r)
    if "[OK]" in r: forge_ok += 1

# Also try other forgery types if available
OTHER_FORGED = r"c:\Users\USER\Desktop\THESIS\thesis-system\dataset\forged\compressed"
other_dirs = [d for d in os.listdir(OTHER_FORGED) if os.path.isdir(os.path.join(OTHER_FORGED, d)) and d != "amount_alteration"]
for d in other_dirs[:2]:
    print(f"\n-- FORGED ({d.upper()}) --")
    fdir = os.path.join(OTHER_FORGED, d)
    ffiles = sorted([f for f in os.listdir(fdir) if f.endswith('.jpg')])[:5]
    for f in ffiles:
        r = test_regional_heuristic(os.path.join(fdir, f), "FORGED")
        print(r)
        if "[OK]" in r: forge_ok += 1

print(f"\nSUMMARY: Authentic {auth_ok}/{len(auth_files)} | Forged {forge_ok}")
