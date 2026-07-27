import os
import glob
import random
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

def generate_forgeries():
    base_dir = r"c:\Users\USER\Desktop\THESIS\thesis-system\dataset"
    auth_dir = os.path.join(base_dir, "authentic", "highres")
    forged_dir = os.path.join(base_dir, "forged")

    categories = ["amount_alteration", "ref_fabrication", "name_modification"]
    for cat in categories:
        os.makedirs(os.path.join(forged_dir, "highres", cat), exist_ok=True)
        os.makedirs(os.path.join(forged_dir, "compressed", cat), exist_ok=True)

    auth_files = sorted(glob.glob(os.path.join(auth_dir, "*.png")))
    print(f"Processing {len(auth_files)} real authentic receipts into realistic digital forgeries...")

    counts = {cat: 0 for cat in categories}

    for idx, fpath in enumerate(auth_files, 1):
        with Image.open(fpath) as img:
            w, h = img.size
            
            # 1. AMOUNT ALTERATION FORGERY
            edited_amt = img.copy().convert("RGB")
            draw_amt = ImageDraw.Draw(edited_amt)
            ax, ay, aw, ah = int(w * 0.20), int(h * 0.42), int(w * 0.60), int(h * 0.08)
            bg_amt = edited_amt.getpixel((max(0, ax - 5), ay + 5))
            draw_amt.rectangle([ax, ay, ax + aw, ay + ah], fill=bg_amt)
            
            fake_amt = f"PHP {random.choice([5000, 10000, 15000, 25000, 50000]):,.2f}"
            draw_amt.text((ax + 20, ay + 10), fake_amt, fill=(0, 92, 230))
            
            # Patch and subtle compression blur for ELA artifact detection
            patch_box = (max(0, ax - 5), max(0, ay - 5), min(w, ax + aw + 5), min(h, ay + ah + 5))
            patch = edited_amt.crop(patch_box).filter(ImageFilter.GaussianBlur(radius=0.5))
            edited_amt.paste(patch, patch_box)
            
            counts["amount_alteration"] += 1
            name_a = f"forged_amount_{counts['amount_alteration']:04d}"
            edited_amt.save(os.path.join(forged_dir, "highres", "amount_alteration", f"{name_a}.png"), "PNG")
            edited_amt.save(os.path.join(forged_dir, "compressed", "amount_alteration", f"{name_a}.jpg"), "JPEG", quality=75)

            # 2. REF FABRICATION FORGERY
            edited_ref = img.copy().convert("RGB")
            draw_ref = ImageDraw.Draw(edited_ref)
            rx, ry, rw, rh = int(w * 0.15), int(h * 0.62), int(w * 0.70), int(h * 0.06)
            bg_ref = edited_ref.getpixel((max(0, rx - 5), ry + 5))
            draw_ref.rectangle([rx, ry, rx + rw, ry + rh], fill=bg_ref)
            
            fake_ref = f"Ref No. {random.randint(1000,9999)} {random.randint(100,999)} {random.randint(100,999)}"
            draw_ref.text((rx + 15, ry + 8), fake_ref, fill=(100, 116, 139))
            
            counts["ref_fabrication"] += 1
            name_r = f"forged_ref_{counts['ref_fabrication']:04d}"
            edited_ref.save(os.path.join(forged_dir, "highres", "ref_fabrication", f"{name_r}.png"), "PNG")
            edited_ref.save(os.path.join(forged_dir, "compressed", "ref_fabrication", f"{name_r}.jpg"), "JPEG", quality=75)

            # 3. NAME MODIFICATION FORGERY
            edited_name = img.copy().convert("RGB")
            draw_name = ImageDraw.Draw(edited_name)
            nx, ny, nw, nh = int(w * 0.20), int(h * 0.28), int(w * 0.60), int(h * 0.06)
            bg_name = edited_name.getpixel((max(0, nx - 5), ny + 5))
            draw_name.rectangle([nx, ny, nx + nw, ny + nh], fill=bg_name)
            
            fake_name = random.choice(["JUAN DELA CRUZ", "MARIA CLARA S.", "RODRIGO R. DUTARTE", "FERDINAND M. MARCOS"])
            draw_name.text((nx + 10, ny + 6), fake_name, fill=(15, 23, 42))
            
            counts["name_modification"] += 1
            name_n = f"forged_name_{counts['name_modification']:04d}"
            edited_name.save(os.path.join(forged_dir, "highres", "name_modification", f"{name_n}.png"), "PNG")
            edited_name.save(os.path.join(forged_dir, "compressed", "name_modification", f"{name_n}.jpg"), "JPEG", quality=75)

    print("\nSUCCESSFULLY GENERATED PROPER DIGITAL FORGERIES:")
    for cat, count in counts.items():
        print(f"  - {cat}: {count} images")

if __name__ == "__main__":
    generate_forgeries()
