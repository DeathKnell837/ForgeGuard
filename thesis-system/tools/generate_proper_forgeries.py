import os
import sys
import glob
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

# Include tools directory
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from gcash_receipt_generator import generate_receipt_data, draw_express_send_receipt

def get_gcash_font(style="bold", size=24):
    fonts_dir = r"c:\Users\USER\Desktop\THESIS\thesis-system\assets\fonts"
    font_files = {
        "karla_bold": "Karla-Bold.ttf",
        "karla_regular": "Karla-Regular.ttf",
        "poppins_bold": "Poppins-Bold.ttf",
        "poppins_semibold": "Poppins-SemiBold.ttf",
        "poppins_regular": "Poppins-Regular.ttf"
    }
    fname = font_files.get(style, "Karla-Bold.ttf")
    fpath = os.path.join(fonts_dir, fname)
    if os.path.exists(fpath):
        try:
            return ImageFont.truetype(fpath, size)
        except Exception:
            pass
    return ImageFont.load_default()

def generate_forgeries():
    base_dir = r"c:\Users\USER\Desktop\THESIS\thesis-system\dataset"
    auth_dir = os.path.join(base_dir, "authentic", "highres")
    forged_dir = os.path.join(base_dir, "forged")

    categories = ["amount_alteration", "ref_fabrication", "name_modification", "ai_generated_template"]
    for cat in categories:
        os.makedirs(os.path.join(forged_dir, "highres", cat), exist_ok=True)
        os.makedirs(os.path.join(forged_dir, "compressed", cat), exist_ok=True)

    auth_files = sorted(glob.glob(os.path.join(auth_dir, "*.png")))
    print(f"Processing {len(auth_files)} authentic receipts for high-precision digital edits...")

    counts = {cat: 0 for cat in categories}

    for idx, fpath in enumerate(auth_files, 1):
        with Image.open(fpath) as img:
            w, h = img.size
            
            # 1. FLAWLESS AMOUNT ALTERATION FORGERY
            edited_amt = img.copy().convert("RGB")
            draw_amt = ImageDraw.Draw(edited_amt)
            # Find white card region (usually middle vertical 35% to 50%)
            ax, ay, aw, ah = int(w * 0.25), int(h * 0.40), int(w * 0.50), int(h * 0.05)
            bg_amt = (255, 255, 255)  # GCash receipt inner card background is white (#FFFFFF)
            draw_amt.rectangle([ax, ay, ax + aw, ay + ah], fill=bg_amt)
            
            fake_amt = f"PHP {random.choice([2500, 5000, 10000, 15000, 25000, 50000]):,.2f}"
            font_amt = get_gcash_font("karla_bold", size=int(h * 0.034))
            draw_amt.text((ax + 10, ay + 5), fake_amt, fill=(25, 114, 249), font=font_amt)
            
            # Subtle compression artifacting over edited text bounding box
            patch_box = (max(0, ax - 2), max(0, ay - 2), min(w, ax + aw + 2), min(h, ay + ah + 2))
            patch = edited_amt.crop(patch_box).filter(ImageFilter.GaussianBlur(radius=0.4))
            edited_amt.paste(patch, patch_box)
            
            counts["amount_alteration"] += 1
            name_a = f"forged_amount_{counts['amount_alteration']:04d}"
            edited_amt.save(os.path.join(forged_dir, "highres", "amount_alteration", f"{name_a}.png"), "PNG")
            edited_amt.save(os.path.join(forged_dir, "compressed", "amount_alteration", f"{name_a}.jpg"), "JPEG", quality=75)

            # 2. FLAWLESS REF FABRICATION FORGERY
            edited_ref = img.copy().convert("RGB")
            draw_ref = ImageDraw.Draw(edited_ref)
            rx, ry, rw, rh = int(w * 0.15), int(h * 0.65), int(w * 0.70), int(h * 0.04)
            bg_ref = (255, 255, 255)
            draw_ref.rectangle([rx, ry, rx + rw, ry + rh], fill=bg_ref)
            
            fake_ref = f"Ref No. {random.randint(1000,9999)} {random.randint(100,999)} {random.randint(100,999)}"
            font_ref = get_gcash_font("karla_regular", size=int(h * 0.020))
            draw_ref.text((rx + 10, ry + 4), fake_ref, fill=(100, 116, 139), font=font_ref)
            
            counts["ref_fabrication"] += 1
            name_r = f"forged_ref_{counts['ref_fabrication']:04d}"
            edited_ref.save(os.path.join(forged_dir, "highres", "ref_fabrication", f"{name_r}.png"), "PNG")
            edited_ref.save(os.path.join(forged_dir, "compressed", "ref_fabrication", f"{name_r}.jpg"), "JPEG", quality=75)

            # 3. FLAWLESS NAME MODIFICATION FORGERY
            edited_name = img.copy().convert("RGB")
            draw_name = ImageDraw.Draw(edited_name)
            nx, ny, nw, nh = int(w * 0.20), int(h * 0.32), int(w * 0.60), int(h * 0.04)
            bg_name = (255, 255, 255)
            draw_name.rectangle([nx, ny, nx + nw, ny + nh], fill=bg_name)
            
            fake_name = random.choice(["JUAN DELA CRUZ", "MARIA CLARA S.", "RODRIGO R. DUTARTE", "FERDINAND M. MARCOS"])
            font_name = get_gcash_font("poppins_semibold", size=int(h * 0.022))
            draw_name.text((nx + 10, ny + 4), fake_name, fill=(15, 23, 42), font=font_name)
            
            counts["name_modification"] += 1
            name_n = f"forged_name_{counts['name_modification']:04d}"
            edited_name.save(os.path.join(forged_dir, "highres", "name_modification", f"{name_n}.png"), "PNG")
            edited_name.save(os.path.join(forged_dir, "compressed", "name_modification", f"{name_n}.jpg"), "JPEG", quality=75)

    # 4. AI-GENERATED / FULL SYNTHETIC RECEIPTS (153 Images)
    print(f"\nGenerating 153 AI-Generated Full Synthetic GCash Receipts...")
    for i in range(1, len(auth_files) + 1):
        data = generate_receipt_data()
        syn_img = draw_express_send_receipt(data, add_artifacts=False)
        counts["ai_generated_template"] += 1
        name_s = f"forged_ai_gen_{counts['ai_generated_template']:04d}"
        syn_img.save(os.path.join(forged_dir, "highres", "ai_generated_template", f"{name_s}.png"), "PNG")
        syn_img.convert("RGB").save(os.path.join(forged_dir, "compressed", "ai_generated_template", f"{name_s}.jpg"), "JPEG", quality=85)

    print("\nSUCCESSFULLY GENERATED ALL FORGERY CATEGORIES:")
    for cat, count in counts.items():
        print(f"  - {cat}: {count} images")

if __name__ == "__main__":
    generate_forgeries()
