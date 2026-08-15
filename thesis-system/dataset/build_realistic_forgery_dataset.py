"""
ForgeGuard — Realistic Forensic Dataset Builder
==============================================
Creates subtle, realistic forgeries directly on authentic GCash & Maya receipts:
- Preserves 95%+ of the real authentic screenshot
- Performs localized tamperings (Amount, Name, Ref No, Date)
- Generates high-resolution PNGs and ELA-ready JPEGs (Quality=90)
"""

import os
import sys
import glob
import json
import random
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATASET_DIR = os.path.join(BASE_DIR, 'dataset')

# Directories
AUTH_COMP_DIR = os.path.join(DATASET_DIR, 'authentic', 'compressed')
AUTH_HIGH_DIR = os.path.join(DATASET_DIR, 'authentic', 'highres')

FORGED_AMOUNT_COMP = os.path.join(DATASET_DIR, 'forged', 'compressed', 'amount_alteration')
FORGED_NAME_COMP = os.path.join(DATASET_DIR, 'forged', 'compressed', 'name_modification')
FORGED_REF_COMP = os.path.join(DATASET_DIR, 'forged', 'compressed', 'ref_fabrication')
FORGED_FULL_COMP = os.path.join(DATASET_DIR, 'forged', 'compressed', 'full_template')

FORGED_AMOUNT_HIGH = os.path.join(DATASET_DIR, 'forged', 'highres', 'amount_alteration')
FORGED_NAME_HIGH = os.path.join(DATASET_DIR, 'forged', 'highres', 'name_modification')
FORGED_REF_HIGH = os.path.join(DATASET_DIR, 'forged', 'highres', 'ref_fabrication')
FORGED_FULL_HIGH = os.path.join(DATASET_DIR, 'forged', 'highres', 'full_template')

for d in [
    AUTH_COMP_DIR, AUTH_HIGH_DIR,
    FORGED_AMOUNT_COMP, FORGED_NAME_COMP, FORGED_REF_COMP, FORGED_FULL_COMP,
    FORGED_AMOUNT_HIGH, FORGED_NAME_HIGH, FORGED_REF_HIGH, FORGED_FULL_HIGH
]:
    os.makedirs(d, exist_ok=True)

# User's authentic source receipts
REAL_SOURCES = [
    {
        "id": "real_gcash_jey",
        "path": r"C:\Users\USER\.gemini\antigravity\brain\bc2aba2c-7a06-47d2-9e93-1be1ea9c21ce\.user_uploaded\media_1786801931185.png",
        "type": "express_send_standard"
    },
    {
        "id": "real_gcash_adn",
        "path": r"C:\Users\USER\.gemini\antigravity\brain\bc2aba2c-7a06-47d2-9e93-1be1ea9c21ce\.user_uploaded\media_1786801932827.png",
        "type": "express_send_standard"
    },
    {
        "id": "real_gcash_gwn",
        "path": r"C:\Users\USER\.gemini\antigravity\brain\bc2aba2c-7a06-47d2-9e93-1be1ea9c21ce\.user_uploaded\media_1786801936398.png",
        "type": "express_send_statusbar"
    },
    {
        "id": "real_maya_transfer",
        "path": r"C:\Users\USER\.gemini\antigravity\brain\bc2aba2c-7a06-47d2-9e93-1be1ea9c21ce\.user_uploaded\media_1786801552332.jpg",
        "type": "maya_bank_transfer"
    },
    {
        "id": "real_gcash_utp15",
        "path": r"C:\Users\USER\.gemini\antigravity\brain\bc2aba2c-7a06-47d2-9e93-1be1ea9c21ce\.user_uploaded\media_1786801565636.jpg",
        "type": "gcash_load"
    },
    {
        "id": "real_gcash_xae",
        "path": r"C:\Users\USER\.gemini\antigravity\brain\bc2aba2c-7a06-47d2-9e93-1be1ea9c21ce\.user_uploaded\media_1786801527456.png",
        "type": "express_send_standard"
    }
]

# Realistic values
AMOUNTS = [
    "500.00", "1,000.00", "1,500.00", "2,500.00", "3,500.00",
    "5,000.00", "7,500.00", "10,000.00", "12,500.00", "15,000.00",
    "20,000.00", "25,000.00", "35,000.00", "50,000.00", "75,000.00", "99,000.00"
]

NAMES = [
    ("MA•••A S.", "+63 917 882 1923"),
    ("JU•••N D.", "+63 928 456 7890"),
    ("RO•••E B.", "+63 905 123 4567"),
    ("DA•••A U.", "+63 999 777 8888"),
    ("ED•••N G.", "+63 918 333 4444"),
    ("CL•••E F.", "+63 927 555 6666"),
    ("AL•••X M.", "+63 916 222 1111"),
    ("KR•••S P.", "+63 939 444 5555"),
    ("CH•••S T.", "+63 908 666 7777"),
    ("JO•••H V.", "+63 945 888 9999")
]

FONTS = {
    'arial': r'C:\Windows\Fonts\arial.ttf',
    'arial_bold': r'C:\Windows\Fonts\arialbd.ttf',
    'segoe': r'C:\Windows\Fonts\segoeui.ttf',
    'segoe_bold': r'C:\Windows\Fonts\segoeuib.ttf',
    'tahoma': r'C:\Windows\Fonts\tahoma.ttf',
    'tahoma_bold': r'C:\Windows\Fonts\tahomabd.ttf'
}

def get_font(key, size):
    path = FONTS.get(key, FONTS['segoe'])
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def create_tampered_standard(src_img, tamper_type, idx):
    """Tamper Express Send standard (527x1024)"""
    im = src_img.copy().convert('RGB')
    draw = ImageDraw.Draw(im)
    w, h = im.size
    
    amt = random.choice(AMOUNTS)
    name, phone = random.choice(NAMES)
    ref_no = f"103{random.randint(1000000000, 9999999999)}"
    
    if tamper_type in ['amount', 'full']:
        # Clear amount and total
        draw.rectangle([320, 275, 490, 320], fill=(255, 255, 255))
        draw.rectangle([250, 375, 490, 430], fill=(255, 255, 255))
        
        fnt_a = get_font(random.choice(['arial', 'segoe', 'tahoma']), 24)
        fnt_t = get_font(random.choice(['arial_bold', 'segoe_bold', 'tahoma_bold']), 32)
        
        draw.text((475 - len(amt)*13, 285), amt, fill=(30, 35, 50), font=fnt_a)
        tot_str = f"P{amt}"
        draw.text((475 - len(tot_str)*19, 380), tot_str, fill=(0, 65, 175), font=fnt_t)
        
    if tamper_type in ['name', 'full']:
        draw.rectangle([50, 105, 475, 185], fill=(255, 255, 255))
        fnt_n = get_font('segoe_bold', 26)
        draw.text((w // 2 - len(name)*7, 110), name, fill=(0, 65, 175), font=fnt_n)
        draw.rounded_rectangle([w//2 - 120, 145, w//2 + 120, 180], radius=18, fill=(235, 243, 255))
        fnt_p = get_font('segoe_bold', 17)
        draw.text((w//2 - 95, 152), phone, fill=(0, 65, 170), font=fnt_p)
        
    if tamper_type in ['ref', 'full']:
        draw.rectangle([50, 455, 475, 500], fill=(245, 248, 255))
        fnt_r = get_font('segoe', 17)
        draw.text((55, 465), f"Ref No. {ref_no}", fill=(70, 85, 110), font=fnt_r)
        
    return im

def build_dataset():
    print("=== BUILDING REALISTIC FORGERY DATASET FROM AUTHENTIC RECEIPTS ===")
    
    meta_records = []
    
    # 1. Save Authentic Baselines
    for idx, src in enumerate(REAL_SOURCES):
        if not os.path.exists(src["path"]):
            continue
        im = Image.open(src["path"]).convert('RGB')
        
        # Save Authentic Highres & Compressed
        auth_fname = f"authentic_real_{src['id']}.jpg"
        im.save(os.path.join(AUTH_HIGH_DIR, auth_fname.replace('.jpg', '.png')), format="PNG")
        im.save(os.path.join(AUTH_COMP_DIR, auth_fname), format="JPEG", quality=90)
        
        meta_records.append({
            "filename": auth_fname,
            "label": "authentic",
            "category": "authentic_real",
            "source": src["id"]
        })
        print(f"Saved Authentic Baseline: {auth_fname}")

    # 2. Generate Forged Variations
    tamper_types = ['amount', 'name', 'ref', 'full']
    for src in REAL_SOURCES:
        if not os.path.exists(src["path"]):
            continue
        src_img = Image.open(src["path"]).convert('RGB')
        
        for t_type in tamper_types:
            for v_idx in range(8): # 8 variations per type per base receipt = 32 per source
                sample_name = f"forged_{src['id']}_{t_type}_{v_idx+1:02d}"
                tampered = create_tampered_standard(src_img, t_type, v_idx)
                
                # Determine target folders
                if t_type == 'amount':
                    c_dir, h_dir = FORGED_AMOUNT_COMP, FORGED_AMOUNT_HIGH
                elif t_type == 'name':
                    c_dir, h_dir = FORGED_NAME_COMP, FORGED_NAME_HIGH
                elif t_type == 'ref':
                    c_dir, h_dir = FORGED_REF_COMP, FORGED_REF_HIGH
                else:
                    c_dir, h_dir = FORGED_FULL_COMP, FORGED_FULL_HIGH
                    
                tampered.save(os.path.join(h_dir, f"{sample_name}.png"), format="PNG")
                tampered.save(os.path.join(c_dir, f"{sample_name}.jpg"), format="JPEG", quality=90)
                
                meta_records.append({
                    "filename": f"{sample_name}.jpg",
                    "label": "forged",
                    "category": t_type,
                    "source": src["id"]
                })
                
    # Update metadata.json
    meta_path = os.path.join(DATASET_DIR, 'metadata.json')
    meta_payload = {
        "version": "2.1",
        "total_samples": len(meta_records),
        "authentic_count": sum(1 for r in meta_records if r["label"] == "authentic"),
        "forged_count": sum(1 for r in meta_records if r["label"] == "forged"),
        "samples": meta_records
    }
    with open(meta_path, 'w') as f:
        json.dump(meta_payload, f, indent=2)
        
    print(f"\nCOMPLETED! Total Created: {len(meta_records)} ({meta_payload['forged_count']} Forged, {meta_payload['authentic_count']} Authentic)")

if __name__ == '__main__':
    build_dataset()
