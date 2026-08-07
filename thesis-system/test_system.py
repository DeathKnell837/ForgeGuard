"""
ForgeGuard System Verification Script
Tests both authentic and forged receipt images through the full pipeline.
"""
import sys, os
sys.path.insert(0, r"c:\Users\USER\Desktop\THESIS\thesis-system")

import numpy as np
from PIL import Image
from preprocessing.ela import compute_ela, convert_ela_to_array

# Test paths
AUTHENTIC_DIR = r"c:\Users\USER\Desktop\THESIS\thesis-system\dataset\authentic\compressed"
FORGED_DIR = r"c:\Users\USER\Desktop\THESIS\thesis-system\dataset\forged\compressed\amount_alteration"

def test_fallback_heuristic(img_path, label):
    """Simulates the exact fallback heuristic from app.py"""
    pil_img = Image.open(img_path).convert("RGB")
    w, h = pil_img.size
    aspect_ratio = h / float(w)
    
    # Pre-validation checks
    arr = np.array(pil_img, dtype=np.float32)
    std_dev = float(np.std(arr))
    
    if w < 180 or h < 240:
        return f"  [{label}] {os.path.basename(img_path)} -> REJECTED: Low resolution ({w}x{h})"
    if std_dev < 6.0:
        return f"  [{label}] {os.path.basename(img_path)} -> REJECTED: Blank image"
    if aspect_ratio < 0.70 or aspect_ratio > 3.6:
        return f"  [{label}] {os.path.basename(img_path)} -> HALTED: Non-receipt (aspect={aspect_ratio:.2f})"
    
    # ELA computation
    ela_img = compute_ela(pil_img, quality=90, scale=15.0)
    ela_np = np.array(ela_img, dtype=np.float32)
    var_val = float(np.var(ela_np))
    mean_val = float(np.mean(ela_np))
    max_val = float(np.max(ela_np))
    
    # Fallback heuristic (same as app.py)
    is_forged = (var_val > 210.0 and max_val > 230.0) or mean_val > 15.0
    if is_forged:
        forgery_score = min(0.98, max(0.85, 0.70 + (var_val / 500.0) * 0.3))
    else:
        forgery_score = min(0.35, max(0.02, (var_val / 500.0) * 0.3))
    
    confidence = forgery_score if is_forged else (1.0 - forgery_score)
    verdict = "FORGED" if is_forged else "AUTHENTIC"
    
    correct = (label == "AUTHENTIC" and not is_forged) or (label == "FORGED" and is_forged)
    status = "[OK]" if correct else "[FAIL]"
    
    return f"  [{label}] {os.path.basename(img_path):35s} -> {verdict:10s} (conf={confidence*100:.1f}%, var={var_val:.1f}, mean={mean_val:.1f}, max={max_val:.0f}) {status}"

# Test authentic images (first 10)
print("=" * 110)
print("TEST 1: AUTHENTIC RECEIPT IMAGES (Expected: AUTHENTIC)")
print("=" * 110)
authentic_files = sorted([f for f in os.listdir(AUTHENTIC_DIR) if f.endswith('.jpg')])[:10]
auth_correct = 0
for f in authentic_files:
    result = test_fallback_heuristic(os.path.join(AUTHENTIC_DIR, f), "AUTHENTIC")
    print(result)
    if "[OK]" in result:
        auth_correct += 1

# Test forged images (first 10)
print()
print("=" * 110)
print("TEST 2: FORGED RECEIPT IMAGES (Expected: FORGED)")
print("=" * 110)
forged_files = sorted([f for f in os.listdir(FORGED_DIR) if f.endswith('.jpg')])[:10]
forge_correct = 0
for f in forged_files:
    result = test_fallback_heuristic(os.path.join(FORGED_DIR, f), "FORGED")
    print(result)
    if "[OK]" in result:
        forge_correct += 1

# Summary
print()
print("=" * 110)
print(f"SUMMARY: Authentic {auth_correct}/{len(authentic_files)} correct | Forged {forge_correct}/{len(forged_files)} correct")
print("=" * 110)
