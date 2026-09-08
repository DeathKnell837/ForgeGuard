"""
ForgeGuard — Authentic Receipt Ingestion & Messenger-Compression Pipeline
========================================================================
Implements Section 2.4 (Phases 2, 4, and 5) of the Thesis Methodology:
1. Ingests collected authentic GCash receipts from Google Forms.
2. Screens for duplicates via MD5 hash against existing dataset.
3. Saves original base images into `dataset/authentic/highres/` (.png).
4. Generates exact Facebook Messenger compressed counterparts into `dataset/authentic/compressed/` (.jpg)
   matching Messenger's verified parameters:
   - Max dimension <= 2048px (Lanczos downsampling)
   - Chroma Subsampling: 4:2:0 (YUV420)
   - JPEG Quality: Q=75 (IJG standard)
   - Baseline encoding (non-progressive)
   - EXIF stripped for contributor privacy (Section 2.11)
5. Emits a provenance manifest JSON for full auditability.
"""

import os
import sys
import glob
import json
import hashlib
from datetime import datetime
from PIL import Image, JpegImagePlugin

def get_image_hash(img):
    return hashlib.md5(img.tobytes()).hexdigest()

def messenger_compress_and_save(img, out_path, quality=75):
    """
    Applies Facebook Messenger's exact compression pipeline:
    1. Longest edge capped at 2048 px (Lanczos resampling).
    2. RGB conversion (strips alpha if present).
    3. Baseline JPEG at Quality 75 with 4:2:0 chroma subsampling.
    4. Strips personal EXIF tags for privacy.
    """
    w, h = img.size
    if max(w, h) > 2048:
        scale = 2048.0 / max(w, h)
        new_w = int(round(w * scale))
        new_h = int(round(h * scale))
        processed = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    else:
        processed = img.copy()

    if processed.mode != 'RGB':
        processed = processed.convert('RGB')

    # Save to out_path with exact Messenger parameters
    processed.save(
        out_path,
        format='JPEG',
        quality=quality,
        subsampling='4:2:0',
        progressive=False,
        optimize=True
    )
    return processed.size

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    source_dir = r"C:\Users\USER\Downloads\authentic_receipts_extracted"
    highres_dir = os.path.join(repo_root, "thesis-system", "dataset", "authentic", "highres")
    compressed_dir = os.path.join(repo_root, "thesis-system", "dataset", "authentic", "compressed")
    manifest_path = os.path.join(repo_root, "thesis-system", "dataset", "authentic_ingestion_manifest.json")

    os.makedirs(highres_dir, exist_ok=True)
    os.makedirs(compressed_dir, exist_ok=True)

    print("=== 1. Scanning Existing Dataset Hashes ===")
    existing_hashes = set()
    for root, _, files in os.walk(os.path.join(repo_root, "thesis-system", "dataset", "authentic")):
        for f in files:
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                p = os.path.join(root, f)
                try:
                    with Image.open(p) as img:
                        existing_hashes.add(get_image_hash(img))
                except:
                    pass
    print(f"Existing authentic image hashes indexed: {len(existing_hashes)}")

    # Determine starting index
    existing_nums = []
    for f in os.listdir(highres_dir):
        if f.startswith('authentic_') and f.lower().endswith('.png'):
            parts = f.split('_')
            if len(parts) >= 2 and parts[1][:4].isdigit():
                existing_nums.append(int(parts[1][:4]))
    next_idx = max(existing_nums) + 1 if existing_nums else 1
    print(f"Next available authentic index: authentic_{next_idx:04d}")

    print(f"\n=== 2. Ingesting & Deduplicating from: {source_dir} ===")
    source_files = sorted(os.listdir(source_dir))
    seen_in_batch = set()
    manifest_records = []
    ingested_count = 0
    duplicate_count = 0

    for fname in source_files:
        fpath = os.path.join(source_dir, fname)
        if not os.path.isfile(fpath) or not fname.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            continue

        try:
            with Image.open(fpath) as img:
                img_rgb = img.convert('RGB')
                h = get_image_hash(img_rgb)

                if h in existing_hashes:
                    print(f"  [DUP-EXISTING] Skipping '{fname}' (already in dataset)")
                    duplicate_count += 1
                    continue
                if h in seen_in_batch:
                    print(f"  [DUP-BATCH] Skipping '{fname}' (duplicate within download batch)")
                    duplicate_count += 1
                    continue

                seen_in_batch.add(h)
                existing_hashes.add(h)

                receipt_id = f"authentic_{next_idx:04d}"
                hr_filename = f"{receipt_id}.png"
                cp_filename = f"{receipt_id}.jpg"

                hr_path = os.path.join(highres_dir, hr_filename)
                cp_path = os.path.join(compressed_dir, cp_filename)

                # 1. Save High-Res Original (Lossless PNG)
                img_rgb.save(hr_path, format='PNG', optimize=True)

                # 2. Save Messenger-Compressed Counterpart
                cp_dims = messenger_compress_and_save(img_rgb, cp_path, quality=75)

                manifest_records.append({
                    "id": receipt_id,
                    "original_source_file": fname,
                    "highres_file": hr_filename,
                    "highres_dimensions": list(img_rgb.size),
                    "compressed_file": cp_filename,
                    "compressed_dimensions": list(cp_dims),
                    "compression_quality": 75,
                    "chroma_subsampling": "4:2:0",
                    "md5": h,
                    "timestamp": datetime.now().isoformat()
                })

                print(f"  [INGESTED] {receipt_id} <- '{fname}' (Orig: {img_rgb.size} -> Comp: {cp_dims})")
                next_idx += 1
                ingested_count += 1

        except Exception as e:
            print(f"  [ERROR] Failed to process '{fname}': {e}")

    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest_records, f, indent=2)

    print(f"\n=== Ingestion Complete! ===")
    print(f"Successfully ingested & compressed: {ingested_count} unique authentic receipts.")
    print(f"Duplicates screened out: {duplicate_count}")
    print(f"Provenance manifest saved to: {manifest_path}")

if __name__ == '__main__':
    main()
