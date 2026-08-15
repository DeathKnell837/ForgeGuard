PREMIUM_CSS = """
<style>
/* ============================================================
   FORGEGUARD ULTIMATE CYBER FORENSIC COMMAND CENTER CSS (v2.0)
   ============================================================ */

/* 1. Google Fonts: JetBrains Mono (Data/Tech), Orbitron / Rajdhani / Spectral (Headers), Inter (Body) */
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700;800&family=Rajdhani:wght@500;600;700;800&family=Spectral:ital,wght@0,500;0,600;0,700;0,800;1,600&family=Inter:wght@300;400;500;600;700;800&display=swap');

/* 2. Cyber Surface System & Global Theme */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    background-color: #04070D !important;
    color: #E2E8F0 !important;
}

.stApp {
    background-color: #04070D !important;
    background-image: 
        radial-gradient(circle at 50% 0%, rgba(139, 92, 246, 0.15) 0%, transparent 50%),
        radial-gradient(circle at 10% 30%, rgba(0, 240, 255, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 90% 70%, rgba(201, 161, 95, 0.08) 0%, transparent 40%),
        linear-gradient(rgba(0, 240, 255, 0.02) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 240, 255, 0.02) 1px, transparent 1px) !important;
    background-size: 100% 100%, 100% 100%, 100% 100%, 40px 40px, 40px 40px !important;
    background-position: center, center, center, -1px -1px, -1px -1px !important;
    background-attachment: fixed !important;
}

/* Cyber Noise Scanline Texture */
.stApp::after {
    content: "";
    position: fixed;
    top: 0; left: 0; width: 100vw; height: 100vh;
    pointer-events: none;
    z-index: 999999;
    opacity: 0.025;
    background: repeating-linear-gradient(
        0deg,
        rgba(0, 0, 0, 0.15),
        rgba(0, 0, 0, 0.15) 1px,
        transparent 1px,
        transparent 2px
    );
}

/* Custom Scrollbar */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
::-webkit-scrollbar-track {
    background: #04070D;
}
::-webkit-scrollbar-thumb {
    background: #1E293B;
    border-radius: 3px;
    border: 1px solid rgba(0, 240, 255, 0.2);
}
::-webkit-scrollbar-thumb:hover {
    background: #8B5CF6;
    box-shadow: 0 0 10px rgba(139, 92, 246, 0.8);
}

/* Typography Hierarchy */
.serif-header {
    font-family: 'Rajdhani', 'Spectral', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px !important;
    text-transform: uppercase;
}

.mono-readout {
    font-family: 'JetBrains Mono', monospace !important;
}

/* STREAMLIT HEADER OVERRIDES */
header[data-testid="stHeader"] {
    background: transparent !important;
    z-index: 99990 !important;
}

button[data-testid="stSidebarCollapsedControl"],
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"] {
    display: inline-flex !important;
    position: fixed !important;
    top: 0.65rem !important;
    left: 0.65rem !important;
    width: 2.25rem !important;
    height: 2.25rem !important;
    z-index: 1000000 !important;
}

[data-testid="stSidebarCollapseButton"],
section[data-testid="stSidebar"] [data-testid="stSidebarHeader"] button {
    display: none !important;
}

.forgeguard-sidebar-launcher {
    position: fixed !important;
    top: 0.7rem !important;
    left: 0.7rem !important;
    z-index: 1000001 !important;
    width: 2.35rem !important;
    height: 2.35rem !important;
    border: 1px solid #00F0FF !important;
    border-radius: 8px !important;
    background: #0A0F1D !important;
    color: #00F0FF !important;
    cursor: pointer !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    box-shadow: 0 0 15px rgba(0, 240, 255, 0.3) !important;
    transition: all 0.3s ease !important;
}
.forgeguard-sidebar-launcher:hover {
    background: #111B2E !important;
    border-color: #8B5CF6 !important;
    color: #FFFFFF !important;
    box-shadow: 0 0 20px rgba(139, 92, 246, 0.6) !important;
    transform: scale(1.05) !important;
}

/* SIDEBAR COMMAND PANEL */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #070B14 0%, #04070D 100%) !important;
    border-right: 1px solid rgba(0, 240, 255, 0.15) !important;
    box-shadow: 8px 0 35px rgba(0, 0, 0, 0.8) !important;
}

section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {
    padding-top: 1.5rem !important;
}

/* HIDE UNNECESSARY CHROME */
#MainMenu, footer, 
[data-testid="stToolbar"], 
div[data-testid="stToast"], 
div[class*="stToast"], 
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
.stDeployButton {
    display: none !important;
}

/* MAIN CONTAINER CONSTRAINT */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 3rem !important;
    max-width: 1440px !important;
}

/* VIOLET / CYAN NEON SLIDERS */
div[data-baseweb="slider"] [role="slider"] {
    background-color: #00F0FF !important;
    border-color: #00F0FF !important;
    box-shadow: 0 0 16px rgba(0, 240, 255, 0.8) !important;
}

div[data-baseweb="slider"] div[style*="background"] {
    background: linear-gradient(90deg, #8B5CF6, #00F0FF) !important;
}

div[data-baseweb="slider"] > div > div > div {
    background: linear-gradient(90deg, #8B5CF6, #00F0FF) !important;
}

div[data-testid="stSliderTickBarMin"], div[data-testid="stSliderTickBarMax"],
div[data-baseweb="slider"] + div {
    color: #00F0FF !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.82rem !important;
}

/* SIDEBAR RADIO SELECTION CARDS (STACKED HUD CARDS) */
div[data-testid="stRadio"] div[role="radiogroup"] label {
    background: #0A0F1D !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 12px !important;
    padding: 14px 16px !important;
    margin-bottom: 10px !important;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    cursor: pointer !important;
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
    position: relative !important;
    overflow: hidden !important;
}

div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
    border-color: rgba(0, 240, 255, 0.4) !important;
    background: #111A2E !important;
    box-shadow: 0 0 18px rgba(0, 240, 255, 0.15) !important;
    transform: translateX(4px) !important;
}

div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.2) 0%, rgba(0, 240, 255, 0.15) 100%) !important;
    border: 1.5px solid #00F0FF !important;
    box-shadow: 0 0 20px rgba(0, 240, 255, 0.3), inset 0 0 15px rgba(0, 240, 255, 0.1) !important;
}

div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] span {
    color: #00F0FF !important;
    font-weight: 700 !important;
    text-shadow: 0 0 10px rgba(0, 240, 255, 0.5) !important;
}

/* ============================================================
   CYBER FORENSIC HUD BRAND BAR & BANNER
   ============================================================ */
.navbar-brand {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: linear-gradient(135deg, #090E1A 0%, #0D1527 100%);
    border: 1px solid rgba(0, 240, 255, 0.25);
    border-radius: 16px;
    padding: 1rem 2rem;
    margin-bottom: 0.5rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6), inset 0 0 15px rgba(0, 240, 255, 0.05);
    position: relative;
    overflow: hidden;
}

.navbar-brand::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; height: 1px;
    background: linear-gradient(90deg, transparent, #00F0FF, #8B5CF6, transparent);
}

.brand-title {
    font-family: 'Rajdhani', 'Spectral', sans-serif;
    font-size: 1.85rem;
    font-weight: 800;
    letter-spacing: 1px;
    color: #F8FAFC;
    display: flex;
    align-items: center;
    gap: 14px;
    text-transform: uppercase;
}

.brand-shield {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    filter: drop-shadow(0 0 12px rgba(0, 240, 255, 0.8));
    animation: shield-glow 3s ease-in-out infinite alternate;
}

@keyframes shield-glow {
    0% { filter: drop-shadow(0 0 8px rgba(0, 240, 255, 0.5)); }
    100% { filter: drop-shadow(0 0 18px rgba(139, 92, 246, 0.9)); }
}

.version-pill {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    font-size: 0.72rem;
    color: #00F0FF;
    background: rgba(0, 240, 255, 0.12);
    border: 1px solid rgba(0, 240, 255, 0.4);
    padding: 3px 10px;
    border-radius: 20px;
    margin-left: 8px;
    letter-spacing: 0.8px;
    box-shadow: 0 0 10px rgba(0, 240, 255, 0.2);
}

.badge-gold {
    background: rgba(201, 161, 95, 0.12);
    color: #F59E0B;
    border: 1px solid rgba(245, 158, 11, 0.4);
    padding: 6px 16px;
    border-radius: 30px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.74rem;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    box-shadow: 0 0 15px rgba(245, 158, 11, 0.15);
}

/* 3. Surface Depth System - Panels */
.glass-panel {
    background: #0F1419;
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1.25rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(12px);
}
.glass-panel-inner {
    background: #161D27;
    border-radius: 12px;
    padding: 1rem;
    border: 1px solid rgba(255,255,255,0.03);
}

.eyebrow-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: #8B5CF6;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.eyebrow-gold {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: #C9A15F;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* 13. Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: #0F1419 !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 16px !important;
    padding: 8px !important;
    gap: 8px !important;
    backdrop-filter: blur(12px) !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    color: #94A3B8 !important;
    border-radius: 10px !important;
    padding: 10px 20px !important;
    transition: all 0.3s ease !important;
}
.stTabs [data-baseweb="tab"]:hover {
    background: rgba(139, 92, 246, 0.1) !important;
    color: #F8FAFC !important;
}
.stTabs [aria-selected="true"] {
    background: rgba(139, 92, 246, 0.15) !important;
    color: #FFFFFF !important;
    box-shadow: 0 4px 12px rgba(139, 92, 246, 0.2) !important;
    border: 1px solid rgba(139, 92, 246, 0.3) !important;
}
.stTabs [data-baseweb="tab-border"], .stTabs [data-baseweb="tab-highlight"] {
    display: none !important;
}

/* 11. Verdict Stamps */
@keyframes stamp-slam {
  0% { transform: rotate(var(--stamp-rotate, 2deg)) scale(2.5); opacity: 0; }
  60% { transform: rotate(var(--stamp-rotate, 2deg)) scale(0.9); opacity: 1; }
  80% { transform: rotate(var(--stamp-rotate, 2deg)) scale(1.05); }
  100% { transform: rotate(var(--stamp-rotate, 2deg)) scale(1); }
}

.stamp-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin: 2rem 0;
}
.stamp-box {
    display: inline-block;
    padding: 1.5rem 2.5rem;
    border-radius: 12px;
    text-align: center;
    animation: stamp-slam 0.5s cubic-bezier(0.25, 1, 0.5, 1) forwards;
}
.stamp-forged {
    --stamp-rotate: -3deg;
    border: 4px double #F87171;
    background: rgba(248, 113, 113, 0.05);
    color: #F87171;
    box-shadow: inset 0 0 20px rgba(248, 113, 113, 0.1), 0 0 30px rgba(248, 113, 113, 0.15);
}
.stamp-auth {
    --stamp-rotate: 2deg;
    border: 4px double #34D399;
    background: rgba(52, 211, 153, 0.05);
    color: #34D399;
    box-shadow: inset 0 0 20px rgba(52, 211, 153, 0.1), 0 0 30px rgba(52, 211, 153, 0.15);
}
.stamp-warning {
    --stamp-rotate: -1deg;
    border: 4px double #FBBF24;
    background: rgba(251, 191, 36, 0.05);
    color: #FBBF24;
    box-shadow: inset 0 0 20px rgba(251, 191, 36, 0.1), 0 0 30px rgba(251, 191, 36, 0.15);
}
.stamp-title {
    font-family: 'Spectral', serif;
    font-size: 2rem;
    font-weight: 800;
    letter-spacing: 3px;
    text-transform: uppercase;
}
.stamp-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    letter-spacing: 1.5px;
}
.stamp-meta-bar {
    background: #0F1419;
    border: 1px solid rgba(255, 255, 255, 0.06);
    padding: 8px 16px;
    border-radius: 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    color: #94A3B8;
    margin-top: 1rem;
}

/* 10. Architecture Matrix Cards */
.glass-panel-matrix {
    background: #0F1419;
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 16px;
    padding: 1.5rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.glass-panel-matrix:hover {
    border-color: rgba(139, 92, 246, 0.3);
    box-shadow: 0 12px 40px rgba(139, 92, 246, 0.15);
}
.glass-panel-matrix.active-model {
    border-left: 3px solid #2DD4BF;
}

/* 4. Gold Shimmer Line */
@keyframes gold-shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}
.shimmer-line {
  height: 1px;
  background: linear-gradient(90deg, transparent, #C9A15F, transparent);
  background-size: 200% 100%;
  animation: gold-shimmer 3s ease-in-out infinite;
  margin: 1rem 0;
}

/* 6. Confidence Gauge Styles */
.confidence-gauge-svg {
    filter: drop-shadow(0 0 8px rgba(45, 212, 191, 0.4));
}
.gauge-bg { stroke: #1E2733; }
.gauge-val { stroke: #2DD4BF; stroke-linecap: round; }

/* 9. Metric Cards */
.metric-card {
    background: #0F1419;
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-top: 2px solid #8B5CF6;
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(12px);
}
.metric-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6);
}
.metric-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.8rem;
    color: #F8FAFC;
    font-weight: 700;
}
.metric-text {
    font-family: 'Inter', sans-serif;
    font-size: 0.8rem;
    color: #94A3B8;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Exhibit Frame */
.exhibit-frame-wrapper {
    background: #0F1419;
    border: 1px solid rgba(139, 92, 246, 0.2);
    border-radius: 16px;
    padding: 1.5rem;
    box-shadow: inset 0 0 20px rgba(0,0,0,0.5), 0 8px 32px rgba(0,0,0,0.4);
}
.exhibit-tag-header {
    background: #161D27;
    border: 1px solid #C9A15F;
    color: #C9A15F;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    padding: 4px 12px;
    border-radius: 6px;
}
.exhibit-placeholder {
    background: #161D27;
    border: 1px dashed rgba(139, 92, 246, 0.3);
    padding: 3rem;
    text-align: center;
    border-radius: 12px;
}
.exhibit-title { font-family: 'JetBrains Mono', monospace; color: #E2E8F0; }
.exhibit-sub { color: #94A3B8; font-size: 0.85rem; }

/* Custom Info Banner */
.custom-info-banner {
    background: rgba(139, 92, 246, 0.1);
    border: 1px solid rgba(139, 92, 246, 0.2);
    border-radius: 12px;
    padding: 1rem;
    color: #E2E8F0;
    font-size: 0.9rem;
}

/* Images */
div[data-testid="stImage"] img {
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
}

/* Buttons */
.stButton>button, div[data-testid="stDownloadButton"] button {
    background: linear-gradient(135deg, #8B5CF6 0%, #6D28D9 100%) !important;
    color: #FFF !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.8rem 1.5rem !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 16px rgba(139, 92, 246, 0.3) !important;
}
.stButton>button:hover, div[data-testid="stDownloadButton"] button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 24px rgba(139, 92, 246, 0.5) !important;
}

/* 16. Mobile Breakpoints */
@media (max-width: 768px) {
    .navbar-brand {
        flex-direction: column;
        gap: 12px;
        text-align: center;
    }
    .metric-num { font-size: 1.5rem; }
    .stamp-title { font-size: 1.5rem; }
}

.icon-inline {
    display: inline-block;
    vertical-align: middle;
}

/* ============================================
   PREMIUM COMPONENTS — ADDITIONAL STYLES
   ============================================ */

/* SVG CONFIDENCE GAUGE */
.gauge-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 1.5rem auto;
    max-width: 220px;
}

.gauge-svg {
    width: 100%;
    height: auto;
    filter: drop-shadow(0 0 12px rgba(0,0,0,0.5));
}

.gauge-arc {
    transition: stroke-dasharray 1.2s cubic-bezier(0.4, 0, 0.2, 1);
}

/* HERO PANEL */
.hero-panel {
    position: relative;
    overflow: hidden;
}

.hero-panel::before {
    content: "";
    position: absolute;
    top: 0;
    right: 0;
    width: 200px;
    height: 200px;
    background: radial-gradient(circle, rgba(139,92,246,0.06) 0%, transparent 70%);
    pointer-events: none;
}

/* INFO CHIPS (in hero banner) */
.info-chip {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-family: 'JetBrains Mono', 'IBM Plex Mono', monospace;
    font-size: 0.75rem;
    color: #94A3B8;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 8px;
    padding: 6px 12px;
    transition: all 0.2s ease;
}

.info-chip:hover {
    background: rgba(255,255,255,0.06);
    border-color: rgba(255,255,255,0.1);
}

/* VERSION PILL */
.version-pill {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    font-size: 0.7rem;
    color: #8B5CF6;
    background: rgba(139,92,246,0.12);
    border: 1px solid rgba(139,92,246,0.3);
    padding: 3px 10px;
    border-radius: 20px;
    margin-left: 8px;
    letter-spacing: 0.5px;
}

/* BRAND SHIELD ICON WRAPPER */
.brand-shield {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    position: relative;
}

.brand-shield svg {
    filter: drop-shadow(0 0 6px rgba(139,92,246,0.4));
}

/* STAMP RING DECORATION */
.stamp-ring {
    position: absolute;
    top: -4px;
    left: -4px;
    right: -4px;
    bottom: -4px;
    border: 1px dashed currentColor;
    border-radius: 18px;
    opacity: 0.3;
    pointer-events: none;
}

/* PULSING STATUS DOT (sidebar) */
@keyframes pulse-dot {
    0%, 100% { opacity: 1; box-shadow: 0 0 8px rgba(52,211,153,0.5); }
    50% { opacity: 0.6; box-shadow: 0 0 4px rgba(52,211,153,0.2); }
}

/* RESPONSIVE ADDITIONS */
@media (max-width: 768px) {
    .gauge-container {
        max-width: 160px;
    }
}

/* PREMIUM CYBER SCANNER SPINNER & STATUS WIDGET */
[data-testid="stStatusWidget"], .stSpinner {
    background: rgba(15, 23, 42, 0.85) !important;
    border: 1.5px solid rgba(139, 92, 246, 0.5) !important;
    border-radius: 12px !important;
    box-shadow: 0 0 25px rgba(139, 92, 246, 0.35) !important;
    color: #38BDF8 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px !important;
    padding: 0.75rem 1.25rem !important;
    margin: 1rem 0 !important;
}
.stSpinner > div > div {
    border-top-color: #00F0FF !important;
    border-right-color: #8B5CF6 !important;
    border-bottom-color: #38BDF8 !important;
}

</style>
"""
