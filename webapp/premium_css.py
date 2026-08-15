PREMIUM_CSS = """
<style>
/* 1. Font Import */
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Spectral:ital,wght@0,500;0,600;0,700;0,800;1,600&family=Inter:wght@300;400;500;600;700&display=swap');

/* 2. Background and Noise */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    background-color: #060910 !important;
    color: #F1F5F9 !important;
}

.stApp {
    background: radial-gradient(circle at 50% 0%, rgba(20, 26, 36, 1) 0%, rgba(6, 9, 16, 1) 100%) !important;
    background-color: #060910 !important;
}

.stApp::after {
    content: "";
    position: fixed;
    top: 0; left: 0; width: 100vw; height: 100vh;
    pointer-events: none;
    z-index: 999999;
    opacity: 0.03;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
}

/* 15. Scrollbar */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
::-webkit-scrollbar-track {
    background: #060910;
}
::-webkit-scrollbar-thumb {
    background: #1E2733;
    border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover {
    background: #8B5CF6;
}

/* Typography Classes */
.serif-header {
    font-family: 'Spectral', Georgia, serif !important;
    font-weight: 700 !important;
    letter-spacing: -0.3px !important;
}

.mono-readout {
    font-family: 'JetBrains Mono', monospace !important;
}

/* STREAMLIT HEADER & CONTROLS */
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
    border: 1px solid #C9A15F !important;
    border-radius: 8px !important;
    background: #0F1419 !important;
    color: #C9A15F !important;
    cursor: pointer !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.5) !important;
    transition: all 0.3s ease !important;
}
.forgeguard-sidebar-launcher:hover {
    background: #161D27 !important;
    border-color: #F8FAFC !important;
    color: #FFFFFF !important;
}

/* 7. Premium Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0A0F15 !important;
    border-right: 1px solid rgba(139, 92, 246, 0.15) !important;
    box-shadow: 4px 0 30px rgba(139, 92, 246, 0.05) !important;
}

/* Pulsing Green Dot */
.status-dot {
    width: 8px; height: 8px;
    background-color: #34D399;
    border-radius: 50%;
    display: inline-block;
    box-shadow: 0 0 8px #34D399;
    animation: pulse-dot 2s infinite;
}
@keyframes pulse-dot {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.7); }
    70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(52, 211, 153, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(52, 211, 153, 0); }
}

/* Sidebar Dividers */
hr {
    border-color: rgba(201, 161, 95, 0.2) !important;
    margin: 1.5rem 0 !important;
}

/* 18. Hide Unnecessary Chrome */
#MainMenu, footer, 
[data-testid="stToolbar"], 
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] {
    display: none !important;
}

.block-container {
    padding-top: 1.25rem !important;
    padding-bottom: 2.5rem !important;
    max-width: 1400px !important;
}

/* Violet Accent Root */
:root {
    --primary-color: #8B5CF6 !important;
}

/* 7. Custom Slider Styling */
div[data-baseweb="slider"] [role="slider"] {
    background-color: #8B5CF6 !important;
    border-color: #8B5CF6 !important;
    box-shadow: 0 0 12px rgba(139, 92, 246, 0.6) !important;
}
div[data-baseweb="slider"] div[style*="background"] {
    background-color: #8B5CF6 !important;
}
div[data-testid="stSliderTickBarMin"], div[data-testid="stSliderTickBarMax"] {
    font-family: 'JetBrains Mono', monospace !important;
    color: #A78BFA !important;
}

/* 14. Radio Buttons - Stacked Cards */
div[data-testid="stRadio"] div[role="radiogroup"] label {
    background: #161D27 !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 12px !important;
    padding: 12px 16px !important;
    margin-bottom: 8px !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
}
div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
    background: #1E2733 !important;
    border-color: rgba(139, 92, 246, 0.4) !important;
}
div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
    background: rgba(139, 92, 246, 0.1) !important;
    border: 1px solid #8B5CF6 !important;
    box-shadow: 0 0 16px rgba(139, 92, 246, 0.2) !important;
}
div[data-baseweb="radio"] div[aria-checked="true"] {
    background-color: #8B5CF6 !important;
    border-color: #8B5CF6 !important;
}

/* 12. File Uploader */
div[data-testid="stFileUploader"] {
    background: #0F1419 !important;
    border: 2px dashed rgba(139, 92, 246, 0.3) !important;
    border-radius: 16px !important;
    padding: 2rem !important;
    transition: all 0.3s ease !important;
}
div[data-testid="stFileUploader"]:hover {
    border-color: #8B5CF6 !important;
    background: #161D27 !important;
    box-shadow: 0 0 20px rgba(139, 92, 246, 0.15) !important;
}

/* 8. Header Brand Bar */
.navbar-brand {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #0F1419;
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 16px;
    padding: 1rem 2rem;
    margin-bottom: 1.5rem;
    box-shadow: inset 0 0 20px rgba(139, 92, 246, 0.05), 0 8px 32px rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(12px);
}
.brand-title {
    font-family: 'Spectral', serif;
    font-size: 1.8rem;
    font-weight: 800;
    color: #F8FAFC;
}
.nav-toggle-btn {
    background: rgba(139, 92, 246, 0.1);
    border: 1px solid rgba(139, 92, 246, 0.3);
    color: #F8FAFC;
    padding: 6px 14px;
    border-radius: 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    cursor: pointer;
    transition: all 0.2s ease;
}
.nav-toggle-btn:hover {
    background: rgba(139, 92, 246, 0.2);
    box-shadow: 0 0 12px rgba(139, 92, 246, 0.4);
}
.badge-gold {
    background: rgba(201, 161, 95, 0.1);
    color: #C9A15F;
    border: 1px solid rgba(201, 161, 95, 0.4);
    padding: 4px 12px;
    border-radius: 20px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    box-shadow: inset 0 0 8px rgba(201, 161, 95, 0.1);
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
    .info-chip {
        font-size: 0.68rem;
        padding: 4px 8px;
    }
    .version-pill {
        font-size: 0.62rem;
        padding: 2px 8px;
    }
}

</style>
"""
