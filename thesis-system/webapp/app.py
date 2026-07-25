"""
ForgeGuard — Streamlit Web Application
======================================
BSCS Thesis System: "Securing Mobile Transaction: A Comparative Evaluation of 
CNN Architectures in Detecting Digital Receipt Forgery"

Notre Dame of Midsayap College (NDMC) | CITE
Authors: Rogie P. Bacanto & Daniela S. Ungab
Adviser: Ms. Doris Ann Mariano
"""

import os
import sys
import site
import time
import io
import datetime
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageChops, ImageFont, ImageDraw
import streamlit as st

# Ensure user site packages and project root directory are in sys.path
APP_DIR = os.path.dirname(os.path.abspath(__file__))
SYS_DIR = os.path.abspath(os.path.join(APP_DIR, ".."))

if SYS_DIR not in sys.path:
    sys.path.insert(0, SYS_DIR)
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)
if hasattr(site, 'USER_SITE') and site.USER_SITE not in sys.path:
    sys.path.append(site.USER_SITE)

def masked_phone(phone):
    """Mask middle digits of phone number e.g. 0976 *** 7835"""
    p = str(phone).strip()
    parts = p.split()
    if len(parts) == 3:
        return f"{parts[0]} *** {parts[2]}"
    if len(p) >= 11:
        return f"{p[:4]} *** {p[-4:]}"
    return p

try:
    from preprocessing.ela import generate_ela_image, evaluate_ela_forgery_risk
except Exception:
    def generate_ela_image(image: Image.Image, quality: int = 90, scale: float = 15.0) -> Image.Image:
        """Fallback ELA generator."""
        if image.mode != 'RGB':
            image = image.convert('RGB')
        buf = io.BytesIO()
        image.save(buf, format='JPEG', quality=quality)
        buf.seek(0)
        resaved = Image.open(buf).convert('RGB')
        ela_diff = ImageChops.difference(image, resaved)
        return ImageEnhance.Brightness(ela_diff).enhance(scale)

    def evaluate_ela_forgery_risk(ela_image: Image.Image) -> dict:
        """Fallback ELA risk evaluator."""
        arr = np.array(ela_image, dtype=np.float32)
        mean_val = float(np.mean(arr))
        var_val = float(np.var(arr))
        max_val = float(np.max(arr))
        return {
            'mean': mean_val,
            'variance': var_val,
            'max': max_val,
            'is_suspicious': var_val > 185.0 or max_val > 210.0
        }

# GCash brand colors & dimensions for receipt generator
GCASH_BLUE = (0, 100, 210)
GCASH_WHITE = (255, 255, 255)
RECEIPT_WIDTH = 1080
RECEIPT_HEIGHT = 1920
FONTS_DIR = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')

def get_font(name, size):
    """Load a font cross-platform (Windows/Linux), falling back to sized default."""
    font_map = {
        'bold': 'arialbd.ttf',
        'regular': 'arial.ttf',
        'italic': 'ariali.ttf',
        'light': 'segoeuil.ttf',
        'segoe': 'segoeui.ttf',
        'segoe_bold': 'segoeuib.ttf',
    }
    font_filename = font_map.get(name, 'arial.ttf')
    is_bold = 'bold' in name
    search_paths = [
        FONTS_DIR,
        '/usr/share/fonts/truetype/dejavu',
        '/usr/share/fonts/truetype/liberation',
        '/usr/share/fonts/truetype/freefont',
        '/usr/share/fonts/TTF',
        '/usr/share/fonts'
    ]
    for s_dir in search_paths:
        if not s_dir or not os.path.exists(s_dir):
            continue
        p = os.path.join(s_dir, font_filename)
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    fallback_fonts = ['DejaVuSans-Bold.ttf' if is_bold else 'DejaVuSans.ttf',
                      'LiberationSans-Bold.ttf' if is_bold else 'LiberationSans-Regular.ttf']
    for s_dir in search_paths:
        if not s_dir or not os.path.exists(s_dir):
            continue
        for ff in fallback_fonts:
            p = os.path.join(s_dir, ff)
            if os.path.exists(p):
                try:
                    return ImageFont.truetype(p, size)
                except Exception:
                    pass
    try:
        return ImageFont.load_default(size=size)
    except Exception:
        return ImageFont.load_default()
def mask_name_gcash(full_name):
    """Format name in GCash Express Send style: GW••••••N D."""
    parts = str(full_name).strip().split()
    if len(parts) >= 2:
        first = parts[0]
        last = parts[-1]
        if len(first) >= 2:
            masked_first = first[:2] + "\u2022\u2022\u2022\u2022\u2022\u2022" + first[-1]
        else:
            masked_first = first + "\u2022\u2022\u2022\u2022\u2022\u2022"
        return f"{masked_first.upper()} {last[0].upper()}."
    return f"{str(full_name)[:2].upper()}\u2022\u2022\u2022\u2022\u2022\u2022{str(full_name)[-1].upper()}"

def draw_express_send_receipt(receipt_data, add_artifacts=False, artifact_type=None):
    """
    Draw 1:1 pixel-perfect GCash 'Express Send' receipt image matching authentic screenshots (908x2048).
    Includes vector bullet dots, double-bar Peso symbol, and vector leaf icon for cross-platform Linux servers.
    """
    W, H = 908, 2048
    GCASH_BLUE = (0, 110, 235)
    GCASH_WHITE = (255, 255, 255)
    
    img = Image.new('RGB', (W, H), GCASH_BLUE)
    draw = ImageDraw.Draw(img)
    
    font_time = get_font('segoe_bold', 28)
    font_header_title = get_font('bold', 42)
    font_name_large = get_font('segoe_bold', 44)
    font_phone = get_font('segoe_bold', 34)
    font_sub = get_font('regular', 28)
    font_label = get_font('segoe_bold', 32)
    font_val = get_font('segoe_bold', 34)
    font_total_label = get_font('segoe_bold', 34)
    font_total_val = get_font('segoe_bold', 48)
    font_ref = get_font('segoe_bold', 30)
    font_date = get_font('regular', 26)
    font_eco_bold = get_font('segoe_bold', 30)
    font_eco_text = get_font('regular', 24)
    font_download = get_font('segoe_bold', 34)
    
    # 1. ANDROID STATUS BAR (TOP)
    draw.rectangle([0, 0, W, 70], fill=GCASH_BLUE)
    dt_val = receipt_data.get('datetime', datetime.datetime.now())
    time_str = dt_val.strftime("%I:%M").lstrip('0')
    draw.text((45, 18), time_str, fill=GCASH_WHITE, font=font_time)
    draw.text((W - 220, 18), "VoLTE 4G 66%", fill=GCASH_WHITE, font=get_font('regular', 24))
    
    # 2. HEADER BAR
    y = 70
    draw.text((50, y + 25), "X", fill=GCASH_WHITE, font=get_font('bold', 42))
    title = "Express Send"
    bbox = draw.textbbox((0, 0), title, font=font_header_title)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) // 2, y + 20), title, fill=GCASH_WHITE, font=font_header_title)
    
    card_x1 = 45
    card_x2 = W - 45
    card_top = 260
    
    # Measure vertical positions for tight bottom calculation
    y = card_top + 52 + 45
    name_y = y
    y += 75
    
    phone_raw = receipt_data.get('recipient_phone', '+63 975 343 9451')
    if not str(phone_raw).startswith('+63'):
        phone_clean = str(phone_raw).replace(' ', '')
        if phone_clean.startswith('0'):
            phone_raw = f"+63 {phone_clean[1:4]} {phone_clean[4:7]} {phone_clean[7:]}"
        else:
            phone_raw = f"+63 {phone_raw}"
            
    phone_str = str(phone_raw)
    pill_y = y
    y += 64 + 16
    
    sub_y = y
    y += 55 + 35
    
    amt_y = y
    amt_val = receipt_data.get('amount', 100.0)
    amt_str = f"{amt_val:,.2f}" if isinstance(amt_val, (int, float)) else str(amt_val)
    if add_artifacts and artifact_type == 'amount_alteration':
        amt_str = "5,000.00"
        
    y += 75 + 35
    
    total_y = y
    y += 110
    
    ref_y = y
    ref_num = receipt_data.get('ref_number', '2043 210 185624')
    if add_artifacts and artifact_type == 'ref_fabrication':
        ref_num = '3890 838 637940'
    elif len(str(ref_num).replace(' ', '')) == 13:
        clean_ref = str(ref_num).replace(' ', '')
        ref_num = f"{clean_ref[:4]} {clean_ref[4:7]} {clean_ref[7:]}"
        
    y += 45
    date_y = y
    y += 75
    
    eco_x1 = card_x1 + 40
    eco_x2 = card_x2 - 40
    eco_y1 = y
    eco_h = 195
    
    card_bottom = eco_y1 + eco_h + 15
    
    # 3. DRAW WHITE RECEIPT CARD TIGHTLY
    draw.rounded_rectangle([card_x1, card_top, card_x2, card_bottom], radius=36, fill=GCASH_WHITE)
    
    # 4. CHECKMARK CIRCLE
    cx = W // 2
    circle_cy = card_top
    circle_r = 52
    draw.ellipse([cx - circle_r, circle_cy - circle_r, cx + circle_r, circle_cy + circle_r], fill=(0, 105, 230))
    draw.line([cx - 20, circle_cy + 2, cx - 4, circle_cy + 18], fill=GCASH_WHITE, width=7)
    draw.line([cx - 4, circle_cy + 18, cx + 22, circle_cy - 16], fill=GCASH_WHITE, width=7)
    
    # 5. RECIPIENT MASKED NAME (WITH CLEAN VECTOR BULLET DOTS)
    raw_name = receipt_data.get('recipient_name', 'Angel N. Soriano')
    parts = str(raw_name).strip().split()
    if len(parts) >= 2:
        prefix = parts[0][:2].upper()
        suffix = f"{parts[0][-1].upper()} {parts[-1][0].upper()}."
    else:
        prefix = str(raw_name)[:2].upper()
        suffix = str(raw_name)[-1].upper()
        
    if add_artifacts and artifact_type == 'name_modification':
        prefix = 'JU'
        suffix = 'N R.'

    b_pre = draw.textbbox((0, 0), prefix, font=font_name_large)
    w_pre = b_pre[2] - b_pre[0]
    b_suf = draw.textbbox((0, 0), suffix, font=font_name_large)
    w_suf = b_suf[2] - b_suf[0]
    
    dots_w = 6 * 18
    total_name_w = w_pre + 10 + dots_w + 10 + w_suf
    start_x = (W - total_name_w) // 2
    
    draw.text((start_x, name_y), prefix, fill=(0, 65, 175), font=font_name_large)
    dot_cx = start_x + w_pre + 16
    for _ in range(6):
        draw.ellipse([dot_cx - 5, name_y + 24 - 5, dot_cx + 5, name_y + 24 + 5], fill=(0, 65, 175))
        dot_cx += 18
    draw.text((dot_cx + 8, name_y), suffix, fill=(0, 65, 175), font=font_name_large)
        
    # 6. PHONE NUMBER PILL
    bbox = draw.textbbox((0, 0), phone_str, font=font_phone)
    tw = bbox[2] - bbox[0]
    pill_w = tw + 70
    pill_x1 = (W - pill_w) // 2
    draw.rounded_rectangle([pill_x1, pill_y, pill_x1 + pill_w, pill_y + 64], radius=32, fill=(235, 243, 255))
    draw.text(((W - tw) // 2, pill_y + 12), phone_str, fill=(0, 65, 170), font=font_phone)
    
    # SUBTITLE
    sub_str = "Sent via GCash"
    bbox = draw.textbbox((0, 0), sub_str, font=font_sub)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) // 2, sub_y), sub_str, fill=(150, 155, 165), font=font_sub)
    
    # DIVIDERS
    left_m = card_x1 + 50
    right_m = card_x2 - 50
    draw.line([left_m, pill_y + 64 + 16 + 55, right_m, pill_y + 64 + 16 + 55], fill=(230, 235, 242), width=2)
    
    # 7. AMOUNT ROW
    draw.text((left_m, amt_y), "Amount", fill=(30, 35, 50), font=font_label)
    bbox = draw.textbbox((0, 0), amt_str, font=font_val)
    tw = bbox[2] - bbox[0]
    draw.text((right_m - tw, amt_y), amt_str, fill=(30, 35, 50), font=font_val)
    
    draw.line([left_m, amt_y + 75, right_m, amt_y + 75], fill=(230, 235, 242), width=2)
    
    # 8. TOTAL AMOUNT SENT ROW WITH VECTOR DOUBLE-BAR PESO SIGN
    draw.text((left_m, total_y + 6), "Total Amount Sent", fill=(20, 25, 40), font=font_total_label)
    
    amt_total_str = f"P{amt_str}"
    bbox = draw.textbbox((0, 0), amt_total_str, font=font_total_val)
    tw = bbox[2] - bbox[0]
    total_x = right_m - tw
    draw.text((total_x, total_y), amt_total_str, fill=(0, 65, 175), font=font_total_val)
    
    # Draw double horizontal bar over the letter P to guarantee Peso sign rendering
    draw.line([total_x + 3, total_y + 24, total_x + 32, total_y + 24], fill=(0, 65, 175), width=4)
    draw.line([total_x + 3, total_y + 32, total_x + 32, total_y + 32], fill=(0, 65, 175), width=4)
        
    # 9. REF NO & TIMESTAMP SECTION
    ref_str = f"Ref No. {ref_num}"
    bbox = draw.textbbox((0, 0), ref_str, font=font_ref)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) // 2, ref_y), ref_str, fill=(70, 85, 110), font=font_ref)
    
    date_str = dt_val.strftime("%b %d, %Y %I:%M %p").replace(" 0", " ")
    bbox = draw.textbbox((0, 0), date_str, font=font_date)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) // 2, date_y), date_str, fill=(120, 130, 150), font=font_date)
    
    # 10. GREEN CARBON FOOTPRINT CARD (gCO2e) WITH VECTOR LEAF ICON
    draw.rounded_rectangle([eco_x1, eco_y1, eco_x2, eco_y1 + eco_h], radius=20, fill=(166, 233, 206))
    draw.rounded_rectangle([eco_x1, eco_y1, eco_x1 + 16, eco_y1 + eco_h], radius=8, fill=(35, 160, 110))
    
    # Vector Leaf Icon
    lx, ly = eco_x1 + 55, eco_y1 + 45
    draw.arc([lx - 16, ly - 16, lx + 16, ly + 16], start=45, end=225, fill=(10, 110, 60), width=4)
    draw.arc([lx - 16, ly - 16, lx + 16, ly + 16], start=225, end=45, fill=(10, 110, 60), width=4)
    draw.line([lx - 10, ly + 12, lx + 12, ly - 10], fill=(10, 110, 60), width=3)
    
    draw.text((eco_x1 + 90, eco_y1 + 25), "279g (gCO2e)", fill=(10, 75, 45), font=font_eco_bold)
    draw.text((eco_x1 + 30, eco_y1 + 82), "By going digital, you reduce your carbon footprint", fill=(15, 85, 50), font=font_eco_text)
    draw.text((eco_x1 + 30, eco_y1 + 120), "from transportation, paper, and plastic.", fill=(15, 85, 50), font=font_eco_text)
    
    # 11. SAWTOOTH TEAR LINE DIRECTLY AT BOTTOM OF WHITE CARD
    tear_y = card_bottom
    saw_w, saw_h = 26, 20
    for x_pos in range(card_x1, card_x2, saw_w):
        poly = [
            (x_pos, tear_y),
            (x_pos + saw_w // 2, tear_y + saw_h),
            (x_pos + saw_w, tear_y)
        ]
        draw.polygon(poly, fill=GCASH_BLUE)
        
    # 12. DOWNLOAD PILL BUTTON TIGHTLY BELOW SAWTOOTH LINE
    btn_y = card_bottom + 85
    btn_w, btn_h = 360, 75
    btn_x1 = (W - btn_w) // 2
    btn_x2 = btn_x1 + btn_w
    draw.rounded_rectangle([btn_x1, btn_y, btn_x2, btn_y + btn_h], radius=38, outline=GCASH_WHITE, width=3)
    
    # Download tray icon
    tx = btn_x1 + 65
    ty = btn_y + 38
    draw.line([tx, ty - 15, tx, ty + 8], fill=GCASH_WHITE, width=4)
    draw.line([tx - 10, ty - 2, tx, ty + 8], fill=GCASH_WHITE, width=4)
    draw.line([tx + 10, ty - 2, tx, ty + 8], fill=GCASH_WHITE, width=4)
    draw.line([tx - 14, ty + 16, tx + 14, ty + 16], fill=GCASH_WHITE, width=4)
    
    draw.text((btn_x1 + 105, btn_y + 18), "Download", fill=GCASH_WHITE, font=font_download)
    
    # 13. ANDROID BOTTOM NAVIGATION BAR
    nav_y = H - 90
    draw.rectangle([0, nav_y, W, H], fill=(0, 0, 0))
    draw.line([W // 4 - 25, nav_y + 30, W // 4 - 25, nav_y + 60], fill=(180, 180, 180), width=4)
    draw.line([W // 4, nav_y + 30, W // 4, nav_y + 60], fill=(180, 180, 180), width=4)
    draw.line([W // 4 + 25, nav_y + 30, W // 4 + 25, nav_y + 60], fill=(180, 180, 180), width=4)
    draw.ellipse([W // 2 - 18, nav_y + 27, W // 2 + 18, nav_y + 63], outline=(180, 180, 180), width=4)
    draw.line([3 * W // 4 + 15, nav_y + 25, 3 * W // 4 - 15, nav_y + 45], fill=(180, 180, 180), width=4)
    draw.line([3 * W // 4 - 15, nav_y + 45, 3 * W // 4 + 15, nav_y + 65], fill=(180, 180, 180), width=4)
    
    return img

def draw_gcash_receipt(receipt_data, add_artifacts=False, artifact_type=None):
    """Self-contained Express Send receipt renderer."""
    return draw_express_send_receipt(receipt_data, add_artifacts=add_artifacts, artifact_type=artifact_type)

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="ForgeGuard — Digital Receipt Forensic Suite",
    layout="wide",
    initial_sidebar_state="expanded"
)
try:
    from bg_data import BG_BASE64
except Exception:
    BG_BASE64 = ""

if BG_BASE64:
    bg_style_rule = f""".stApp {{
        background: linear-gradient(135deg, rgba(11, 14, 20, 0.92) 0%, rgba(20, 26, 36, 0.95) 100%),
                    url("data:image/jpeg;base64,{BG_BASE64}") no-repeat center center fixed !important;
        background-size: cover !important;
    }}"""
else:
    bg_style_rule = """.stApp {
        background-color: #0B0E14 !important;
        background-image: 
            radial-gradient(circle at 50% 15%, rgba(139, 92, 246, 0.1) 0%, transparent 45%),
            radial-gradient(circle at 85% 85%, rgba(201, 161, 95, 0.06) 0%, transparent 40%),
            linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px) !important;
        background-size: 100% 100%, 100% 100%, 36px 36px, 36px 36px !important;
        background-position: center, center, -1px -1px, -1px -1px !important;
    }"""

# ============================================================
# DIGITAL FORENSIC CASE FILE CSS SYSTEM
# ============================================================
CUSTOM_CSS = "<style>\n" + bg_style_rule + """
/* Import Google Fonts: Spectral (Serif Display), Inter (Sans Body), IBM Plex Mono (Monospace Readouts) */
@import url('https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,500;0,600;0,700;0,800;1,600&family=Inter:wght@300;400;500;600;700&family=IBM+Plex+Mono:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap');

/* Global Reset & Surface Hierarchy */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    background-color: #0B0E14 !important;
    color: #F1F5F9 !important;
}

/* Typography Classes */
.serif-header {
    font-family: 'Spectral', Georgia, serif !important;
    font-weight: 700 !important;
    letter-spacing: -0.3px !important;
}

.mono-readout {
    font-family: 'IBM Plex Mono', monospace !important;
}

/* HIDE STREAMLIT CHROME ARTIFACTS */
#MainMenu, footer, header, 
[data-testid="stToolbar"], 
div[data-testid="stToast"], 
div[class*="stToast"], 
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
.stDeployButton {
    display: none !important;
    visibility: hidden !important;
}

/* Page Container Constraints */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 2.5rem !important;
    max-width: 1400px !important;
}

/* SIDEBAR STYLING (LAYER 1 SURFACE: #141A24) */
section[data-testid="stSidebar"] {
    background-color: #141A24 !important;
    border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 1.4rem !important;
}

/* STREAMLIT PRIMARY ACCENT OVERRIDE -> FORENSIC VIOLET (#8B5CF6) */
:root {
    --primary-color: #8B5CF6 !important;
}

/* Force Streamlit Red accents to Violet */
[style*="rgb(255, 75, 75)"], [style*="#ff4b4b"], [style*="RGB(255, 75, 75)"] {
    background-color: #8B5CF6 !important;
    color: #8B5CF6 !important;
    border-color: #8B5CF6 !important;
}

/* VIOLET SLIDERS */
div[data-baseweb="slider"] [role="slider"] {
    background-color: #8B5CF6 !important;
    border-color: #8B5CF6 !important;
    box-shadow: 0 0 12px rgba(139, 92, 246, 0.5) !important;
}

div[data-baseweb="slider"] div[style*="background"] {
    background-color: #8B5CF6 !important;
}

div[data-testid="stSliderTickBarMin"], div[data-testid="stSliderTickBarMax"],
div[data-baseweb="slider"] + div {
    color: #A78BFA !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.82rem !important;
}

/* SIDEBAR STACKED MODEL PICKER CARDS */
div[data-testid="stRadio"] label span {
    color: #E2E8F0 !important;
    font-size: 0.88rem !important;
    font-weight: 500 !important;
}

div[data-testid="stRadio"] div[role="radiogroup"] label {
    background: #1B222D !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 12px !important;
    padding: 12px 14px !important;
    margin-bottom: 8px !important;
    transition: all 0.25s ease !important;
    cursor: pointer !important;
    display: flex !important;
    align-items: center !important;
    width: 100% !important;
}

div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
    border-color: rgba(139, 92, 246, 0.4) !important;
    background: #222B38 !important;
}

div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
    background: rgba(139, 92, 246, 0.14) !important;
    border: 1.5px solid #8B5CF6 !important;
    box-shadow: 0 0 16px rgba(139, 92, 246, 0.25) !important;
}

div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] span {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

div[data-testid="stRadio"] div[role="radiogroup"] div[style*="background"] {
    background-color: #8B5CF6 !important;
}

/* HEADER BRAND BAR */
.navbar-brand {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #141A24;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 0.9rem 1.75rem;
    margin-bottom: 1.25rem;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.45);
}

.brand-title {
    font-family: 'Spectral', Georgia, serif;
    font-size: 1.7rem;
    font-weight: 800;
    letter-spacing: -0.3px;
    color: #F8FAFC;
    display: flex;
    align-items: center;
    gap: 12px;
}

.badge-gold {
    background: rgba(201, 161, 95, 0.12);
    color: #C9A15F;
    border: 1px solid rgba(201, 161, 95, 0.35);
    padding: 5px 14px;
    border-radius: 30px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    white-space: nowrap;
}

/* FORENSIC CASE FILE PANELS (LAYER 1 SURFACE: #141A24) */
.glass-panel {
    background: #141A24;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 1.4rem;
    margin-bottom: 1.25rem;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.35);
}

.eyebrow-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.76rem;
    font-weight: 700;
    color: #8B5CF6;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}

.eyebrow-gold {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.76rem;
    font-weight: 700;
    color: #C9A15F;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}

/* NUMBERED TABS (01 FORENSIC DETECTOR / 02 FORGERY GENERATOR) */
.stTabs [data-baseweb="tab-list"] {
    gap: 12px !important;
    background: #141A24 !important;
    padding: 8px !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3) !important;
}

.stTabs [data-baseweb="tab"] {
    height: 46px !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.86rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.8px !important;
    color: #94A3B8 !important;
    padding: 0 22px !important;
    background: transparent !important;
    border-radius: 10px !important;
    border: 1px solid transparent !important;
    transition: all 0.2s ease !important;
}

.stTabs [data-baseweb="tab"]:hover {
    color: #F1F5F9 !important;
    background: rgba(139, 92, 246, 0.08) !important;
    border-color: rgba(139, 92, 246, 0.2) !important;
}

.stTabs [aria-selected="true"] {
    background: rgba(139, 92, 246, 0.15) !important;
    color: #FFFFFF !important;
    border-bottom: 2.5px solid #8B5CF6 !important;
    border-top: 1px solid rgba(139, 92, 246, 0.3) !important;
    border-left: 1px solid rgba(139, 92, 246, 0.3) !important;
    border-right: 1px solid rgba(139, 92, 246, 0.3) !important;
    box-shadow: 0 4px 16px rgba(139, 92, 246, 0.2) !important;
}

.stTabs [data-baseweb="tab-border"] { display: none !important; }
.stTabs [data-baseweb="tab-highlight"] { display: none !important; }

/* INK STAMP CLASSIFICATION VERDICT (OFFICIAL EVIDENCE STAMP) */
.stamp-container {
    text-align: center;
    margin: 1.5rem 0 1rem 0;
}

.stamp-box {
    display: inline-block;
    padding: 1.2rem 2.4rem;
    border-radius: 14px;
    text-align: center;
    position: relative;
}

.stamp-forged {
    border: 3.5px double #F87171;
    background: rgba(248, 113, 113, 0.09);
    color: #F87171;
    transform: rotate(-2.5deg);
    box-shadow: 0 0 25px rgba(248, 113, 113, 0.15), inset 0 0 15px rgba(248, 113, 113, 0.08);
}

.stamp-auth {
    border: 3.5px double #34D399;
    background: rgba(52, 211, 153, 0.09);
    color: #34D399;
    transform: rotate(2deg);
    box-shadow: 0 0 25px rgba(52, 211, 153, 0.15), inset 0 0 15px rgba(52, 211, 153, 0.08);
}

.stamp-title {
    font-family: 'Spectral', Georgia, serif;
    font-size: 1.7rem;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.stamp-sub {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.76rem;
    letter-spacing: 1px;
    margin-top: 4px;
    opacity: 0.9;
}

.stamp-meta-bar {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.8rem;
    color: #94A3B8;
    background: #141A24;
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 8px 16px;
    border-radius: 8px;
    margin-top: 1rem;
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    justify-content: center;
}

/* EXHIBIT A EVIDENCE PREVIEW FRAME (RECEIPT GENERATOR) */
.exhibit-frame-wrapper {
    position: relative;
    width: 100%;
    max-width: 380px;
    margin: 0 auto;
    background: #141A24;
    border: 2px solid rgba(139, 92, 246, 0.25);
    border-radius: 20px;
    padding: 1.6rem 1rem 1rem 1rem;
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.5), inset 0 0 20px rgba(0, 0, 0, 0.4);
    min-height: 580px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.exhibit-tag {
    position: absolute;
    top: -13px;
    left: 20px;
    background: #141A24;
    border: 1px solid #C9A15F;
    color: #C9A15F;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    font-weight: 700;
    padding: 3px 12px;
    border-radius: 4px;
    letter-spacing: 1px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4);
}

.exhibit-placeholder {
    text-align: center;
    color: #64748B;
    padding: 2rem 1rem;
}

.exhibit-title {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.88rem;
    font-weight: 700;
    color: #94A3B8;
    letter-spacing: 1px;
    margin-top: 10px;
}

.exhibit-sub {
    font-size: 0.8rem;
    color: #64748B;
    margin-top: 6px;
    line-height: 1.45;
}

/* NESTED INPUT CONTROLS (LAYER 2 SURFACE: #1B222D) */
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    background-color: #1B222D !important;
    border: 1px solid rgba(139, 92, 246, 0.2) !important;
    border-radius: 10px !important;
    color: #F1F5F9 !important;
    transition: all 0.2s ease !important;
}

div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="select"] > div:focus-within {
    border-color: #8B5CF6 !important;
    box-shadow: 0 0 14px rgba(139, 92, 246, 0.35) !important;
}

div[data-baseweb="input"] input,
div[data-baseweb="select"] input {
    color: #F1F5F9 !important;
}

label[data-testid="stWidgetLabel"] p {
    color: #CBD5E1 !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
}

/* METRIC READOUT CARDS */
.metric-card {
    background: #141A24;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
}

.metric-num {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 1.45rem;
    font-weight: 700;
    color: #A78BFA;
}

.metric-text {
    font-size: 0.72rem;
    color: #94A3B8;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    margin-top: 3px;
}

/* CUSTOM INFO BANNER */
.custom-info-banner {
    background: rgba(139, 92, 246, 0.08);
    border: 1px solid rgba(139, 92, 246, 0.22);
    border-radius: 12px;
    padding: 0.9rem 1.2rem;
    display: flex;
    align-items: center;
    gap: 12px;
    color: #94A3B8;
    font-size: 0.86rem;
    margin-top: 1rem;
}

/* IMAGE FORENSICS CONTAINER PRESERVING ASPECT RATIO */
div[data-testid="stImage"] img {
    border-radius: 12px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    background-color: #000000 !important;
    max-height: 440px !important;
    object-fit: contain !important;
}

/* BUTTONS (VIOLET ACCENT) */
.stButton>button {
    background: linear-gradient(135deg, #7C3AED 0%, #6D28D9 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.7rem 1.5rem !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.92rem !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 18px rgba(124, 58, 237, 0.35) !important;
    width: 100% !important;
}

.stButton>button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 22px rgba(124, 58, 237, 0.5) !important;
}

.icon-inline {
    display: inline-block;
    vertical-align: middle;
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
