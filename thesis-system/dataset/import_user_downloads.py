"""
ForgeGuard — Clean Dataset Organizer & Importer
==============================================
Imports user's AI-generated downloads into dedicated AI-diffusion folder
and keeps authentic receipts in a strictly separated folder.
"""

import os
import sys
import glob
import json
import shutil
from PIL import Image

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATASET_DIR = os.path.join(BASE_DIR, 'dataset')
DOWNLOADS_DIR = r"C:\Users\USER\Downloads"

# Dedicated separated folders
AI_DIFFUSION_DIR = os.path.join(DATASET_DIR, 'forged', 'compressed', 'ai_diffusion_generated')
AUTHENTIC_DIR = os.path.join(DATASET_DIR, 'authentic', 'compressed')

os.makedirs(AI_DIFFUSION_DIR, exist_ok=True)
os.makedirs(AUTHENTIC_DIR, exist_ok=True)

def import_downloads():
    print("=== IMPORTING AI GENERATED IMAGES FROM DOWNLOADS ===")
    
    # Match all downloaded receipt variations from Bing/DALL-E
    patterns = [
        os.path.join(DOWNLOADS_DIR, "Keep_this_exact_receipt_layout*.jpg"),
        os.path.join(DOWNLOADS_DIR, "A_clear_vertical_mobile_phone*.jpg"),
        os.path.join(DOWNLOADS_DIR, "A_photorealistic_vertical_mobile_phone*.jpg"),
        os.path.join(DOWNLOADS_DIR, "A_photorealistic_mobile_phone_screenshot*.jpg")
    ]
    
    downloaded_files = []
    for pat in patterns:
        downloaded_files.extend(glob.glob(pat))
        
    print(f"Found {len(downloaded_files)} newly downloaded AI images in Downloads folder.")
    
    imported_count = 0
    for idx, fpath in enumerate(sorted(downloaded_files)):
        try:
            target_name = f"ai_diffusion_bing_{idx+1:03d}.jpg"
            dest_path = os.path.join(AI_DIFFUSION_DIR, target_name)
            
            # Open with PIL, verify, save as clean compressed JPEG (quality=90)
            with Image.open(fpath) as img:
                img_rgb = img.convert('RGB')
                img_rgb.save(dest_path, format="JPEG", quality=90)
                
            imported_count += 1
            print(f"  [+] Imported -> {target_name} ({img_rgb.size[0]}x{img_rgb.size[1]})")
        except Exception as e:
            print(f"  [-] Error importing {fpath}: {e}")
            
    print(f"\nSuccessfully imported {imported_count} AI Diffusion receipts into: {AI_DIFFUSION_DIR}")

if __name__ == '__main__':
    import_downloads()
