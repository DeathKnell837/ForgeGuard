PREMIUM_CSS = """
<style>
/* ============================================================
   FORGEGUARD ENTERPRISE FORENSIC COMMAND CENTER CSS (v3.0)
   Sophos, Nexora, Nightfall & SOC Command Center Architecture
   ============================================================ */

@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700;800&family=Rajdhani:wght@600;700;800&display=swap');

/* Global Surface & Canvas */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    background-color: #070A11 !important;
    color: #E2E8F0 !important;
}

.stApp {
    background-color: #070A11 !important;
    background-image: 
        radial-gradient(circle at 50% 0%, rgba(139, 92, 246, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 0% 30%, rgba(0, 240, 255, 0.05) 0%, transparent 40%),
        radial-gradient(circle at 100% 70%, rgba(16, 185, 129, 0.05) 0%, transparent 40%),
        linear-gradient(rgba(255, 255, 255, 0.015) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.015) 1px, transparent 1px) !important;
    background-size: 100% 100%, 100% 100%, 100% 100%, 48px 48px, 48px 48px !important;
    background-position: center, center, center, -1px -1px, -1px -1px !important;
    background-attachment: fixed !important;
}

/* Custom Sleek Scrollbar */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
::-webkit-scrollbar-track {
    background: #070A11;
}
::-webkit-scrollbar-thumb {
    background: #1E293B;
    border-radius: 3px;
    border: 1px solid rgba(255, 255, 255, 0.06);
}
::-webkit-scrollbar-thumb:hover {
    background: #00F0FF;
}

/* Streamlit Header Override */
header[data-testid="stHeader"] {
    background: transparent !important;
    z-index: 99990 !important;
}

/* Sidebar: Sophos & Nightfall Navigation Rail */
section[data-testid="stSidebar"] {
    background-color: #0A0E17 !important;
    border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
    padding-top: 1rem !important;
}

section[data-testid="stSidebar"] > div:first-child {
    padding-top: 0.5rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
}

/* Sidebar Section Headers */
.rail-section-header {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    font-weight: 700;
    color: #64748B;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin: 1.25rem 0 0.5rem 0;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* Custom Radio Navigation Pills */
div[data-testid="stRadio"] > div {
    gap: 6px !important;
}

div[data-testid="stRadio"] label {
    background: rgba(255, 255, 255, 0.02) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 10px !important;
    padding: 0.65rem 0.9rem !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    cursor: pointer !important;
    width: 100% !important;
}

div[data-testid="stRadio"] label:hover {
    background: rgba(0, 240, 255, 0.05) !important;
    border-color: rgba(0, 240, 255, 0.3) !important;
    transform: translateX(3px) !important;
}

div[data-testid="stRadio"] label[data-checked="true"],
div[data-testid="stRadio"] label:has(input:checked) {
    background: linear-gradient(90deg, rgba(0, 240, 255, 0.12) 0%, rgba(139, 92, 246, 0.06) 100%) !important;
    border: 1px solid rgba(0, 240, 255, 0.5) !important;
    box-shadow: 0 4px 16px rgba(0, 240, 255, 0.12) !important;
}

div[data-testid="stRadio"] label div[data-testid="stMarkdownContainer"] p {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    color: #F8FAFC !important;
}

/* Sidebar Sliders */
div[data-testid="stSlider"] label {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.72rem !important;
    font-weight: 600 !important;
    color: #94A3B8 !important;
    letter-spacing: 0.5px !important;
}

/* Top Command Bar & Breadcrumbs */
.top-command-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #0B111E;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 0.8rem 1.25rem;
    margin-bottom: 1.25rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.breadcrumb-trail {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.82rem;
    font-family: 'Inter', sans-serif;
    color: #64748B;
}

.breadcrumb-active {
    color: #F8FAFC;
    font-weight: 700;
    letter-spacing: 0.3px;
}

.telemetry-pill-group {
    display: flex;
    align-items: center;
    gap: 8px;
}

.top-telemetry-pill {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 8px;
    padding: 4px 10px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
}

/* Quick Action Test Buttons */
.stButton > button {
    background: linear-gradient(180deg, #131B2E 0%, #0D1322 100%) !important;
    border: 1px solid rgba(0, 240, 255, 0.3) !important;
    border-radius: 12px !important;
    color: #F8FAFC !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.85rem !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    padding: 0.75rem 1.25rem !important;
    width: 100% !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4) !important;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

.stButton > button:hover {
    border-color: #00F0FF !important;
    box-shadow: 0 0 20px rgba(0, 240, 255, 0.35) !important;
    transform: translateY(-2px) !important;
    color: #00F0FF !important;
}

/* Cyber Upload Dropzone */
div[data-testid="stFileUploader"] {
    background: #0B111E !important;
    border: 1.5px dashed rgba(0, 240, 255, 0.35) !important;
    border-radius: 14px !important;
    padding: 1.25rem !important;
    transition: all 0.3s ease !important;
}

div[data-testid="stFileUploader"]:hover {
    border-color: #00F0FF !important;
    box-shadow: inset 0 0 24px rgba(0, 240, 255, 0.08), 0 0 16px rgba(0, 240, 255, 0.15) !important;
}

/* Streamlit Tabs Override (Sophos & Nexora Style) */
div[data-baseweb="tab-list"] {
    background: #0A0E17 !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 10px !important;
    padding: 4px !important;
    gap: 4px !important;
    margin-bottom: 0.8rem !important;
}

div[data-baseweb="tab"] {
    background: transparent !important;
    border: none !important;
    border-radius: 8px !important;
    color: #94A3B8 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.76rem !important;
    font-weight: 700 !important;
    padding: 6px 14px !important;
    transition: all 0.2s ease !important;
}

div[data-baseweb="tab"][aria-selected="true"] {
    background: #1E293B !important;
    color: #00F0FF !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3) !important;
}

/* Exhibit Visual Card Wrapper */
.visual-card-wrapper {
    background: #0B111E;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 0.9rem;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
}

.visual-card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
    padding-bottom: 6px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

/* Section Eyebrow Labels */
.eyebrow-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 700;
    color: #00F0FF;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 6px;
}
</style>
"""
