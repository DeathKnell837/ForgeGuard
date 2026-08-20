PREMIUM_CSS = """
<style>
/* ============================================================
   FORGEGUARD SOPHOS AI CYBERSECURITY DESIGN SYSTEM (v6.0)
   Exact Behance Reference Implementation
   ============================================================ */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

/* Global Surface & Canvas */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    background-color: #101216 !important;
    color: #E2E8F0 !important;
}

.stApp {
    background-color: #101216 !important;
    background-image: 
        radial-gradient(circle at 50% 0%, rgba(124, 111, 240, 0.06) 0%, transparent 60%),
        radial-gradient(circle at 100% 100%, rgba(45, 212, 191, 0.03) 0%, transparent 50%) !important;
    background-attachment: fixed !important;
}

/* ZERO TOP WHITESPACE (Clean Header) */
header[data-testid="stHeader"] {
    background: transparent !important;
    height: 0px !important;
    min-height: 0px !important;
    padding: 0px !important;
    margin: 0px !important;
    z-index: 99990 !important;
}

div[data-testid="stAppViewContainer"] > section.main {
    padding-top: 0.2rem !important;
}

.main .block-container,
div[data-testid="stAppViewBlockContainer"] {
    padding-top: 0.3rem !important;
    padding-bottom: 1.8rem !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
    max-width: 98% !important;
}

div[data-testid="stVerticalBlock"] {
    gap: 0.75rem !important;
}

/* ============================================================
   SOPHOS SIDEBAR RAIL
   ============================================================ */
section[data-testid="stSidebar"] {
    background-color: #101216 !important;
    border-right: 1px solid rgba(255, 255, 255, 0.06) !important;
    padding-top: 0.2rem !important;
    min-width: 300px !important;
    width: 300px !important;
    visibility: visible !important;
}

/* Hide collapse button inside sidebar */
[data-testid="stSidebarCollapseButton"],
section[data-testid="stSidebar"] [data-testid="stSidebarHeader"] button,
section[data-testid="stSidebar"] button[kind="header"],
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] {
    display: none !important;
}

/* Floating Reopen Toggle Button */
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"],
button[data-testid="stSidebarCollapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    position: fixed !important;
    top: 0.6rem !important;
    left: 0.6rem !important;
    z-index: 999999 !important;
    background: #1A1D26 !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 8px !important;
    color: #FFFFFF !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4) !important;
    cursor: pointer !important;
    padding: 6px 8px !important;
    transition: all 0.2s ease !important;
}

[data-testid="stSidebarCollapsedControl"]:hover,
[data-testid="collapsedControl"]:hover {
    background: rgba(124, 111, 240, 0.2) !important;
    border-color: #7C6FF0 !important;
    transform: scale(1.05) !important;
}

div[data-testid="stSidebarContent"] {
    padding: 0.8rem 1rem 1rem 1rem !important;
}

div[data-testid="stSidebarUserContent"] {
    padding: 0 0 3rem 0 !important;
}

/* Section Header Labels — Exact Sophos MENU style */
.rail-section-header {
    font-family: 'Inter', -apple-system, sans-serif !important;
    font-size: 0.64rem !important;
    font-weight: 700 !important;
    color: #6B7280 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    margin-top: 22px !important;
    margin-bottom: 10px !important;
    padding-left: 0.6rem !important;
    border: none !important;
    background: transparent !important;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* Sophos Radio Navigation Items */
div[data-testid="stElementContainer"]:has(div[data-testid="stRadio"]) {
    width: 100% !important;
}

div[data-testid="stRadio"] {
    width: 100% !important;
}

div[data-testid="stRadio"] > div[data-testid="stRadioGroup"] {
    display: flex !important;
    flex-direction: column !important;
    gap: 5px !important;
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    width: 100% !important;
}

/* Hide native input and radio dots */
div[data-testid="stRadio"] input[type="radio"],
div[data-testid="stRadio"] [data-testid="stRadioDot"] {
    display: none !important;
    opacity: 0 !important;
    width: 0px !important;
    height: 0px !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"] div:has(> div:empty):not(:has(p)),
div[data-testid="stRadio"] label[data-testid="stRadioOption"] > div > div > div:first-child:not(:has(p)):not([data-testid="stMarkdownContainer"]),
div[data-testid="stRadio"] label[data-testid="stRadioOption"] [data-baseweb="radio"] > div:first-child {
    display: none !important;
    width: 0px !important;
    height: 0px !important;
}

/* Sophos Nav Item Capsule */
div[data-testid="stRadio"] label[data-testid="stRadioOption"] {
    background: transparent !important;
    border: 1px solid transparent !important;
    border-radius: 8px !important;
    padding: 10px 14px !important;
    margin: 0 !important;
    transition: all 0.15s ease !important;
    cursor: pointer !important;
    width: 100% !important;
    box-sizing: border-box !important;
    display: flex !important;
    align-items: center !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"] > div,
div[data-testid="stRadio"] label[data-testid="stRadioOption"] > div > div {
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"] div[data-testid="stMarkdownContainer"] {
    width: 100% !important;
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
}

/* Inactive Nav text */
div[data-testid="stRadio"] label[data-testid="stRadioOption"] div[data-testid="stMarkdownContainer"] {
    display: flex !important;
    align-items: center !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"] div[data-testid="stMarkdownContainer"] p {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.86rem !important;
    font-weight: 500 !important;
    color: #9CA3AF !important;
    margin: 0 !important;
    line-height: 1.4 !important;
    display: flex !important;
    align-items: center !important;
    transition: color 0.15s ease !important;
}

/* Nav Item 1 Icon: Shield / Radar */
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:nth-child(1) div[data-testid="stMarkdownContainer"] p::before {
    content: "";
    display: inline-block;
    width: 17px;
    height: 17px;
    margin-right: 11px;
    background-color: currentColor;
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z'/%3E%3C/svg%3E") no-repeat center / contain;
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z'/%3E%3C/svg%3E") no-repeat center / contain;
    flex-shrink: 0;
}

/* Nav Item 2 Icon: Analytics / Bar Chart */
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:nth-child(2) div[data-testid="stMarkdownContainer"] p::before {
    content: "";
    display: inline-block;
    width: 17px;
    height: 17px;
    margin-right: 11px;
    background-color: currentColor;
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='20' x2='18' y2='10'%3E%3C/line%3E%3Cline x1='12' y1='20' x2='12' y2='4'%3E%3C/line%3E%3Cline x1='6' y1='20' x2='6' y2='14'%3E%3C/line%3E%3C/svg%3E") no-repeat center / contain;
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='20' x2='18' y2='10'%3E%3C/line%3E%3Cline x1='12' y1='20' x2='12' y2='4'%3E%3C/line%3E%3Cline x1='6' y1='20' x2='6' y2='14'%3E%3C/line%3E%3C/svg%3E") no-repeat center / contain;
    flex-shrink: 0;
}

/* Inactive Hover */
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:hover {
    background: rgba(255, 255, 255, 0.04) !important;
    border-color: rgba(255, 255, 255, 0.06) !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"]:hover div[data-testid="stMarkdownContainer"] p {
    color: #FFFFFF !important;
}

/* Active Highlight Capsule — Sophos Frosted Gradient */
div[data-testid="stRadio"] label[data-testid="stRadioOption"][data-selected="true"],
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input:checked) {
    background: linear-gradient(90deg, rgba(255, 255, 255, 0.12) 0%, rgba(255, 255, 255, 0.05) 100%) !important;
    border: 1px solid rgba(255, 255, 255, 0.14) !important;
    box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.12), 0 2px 8px rgba(0, 0, 0, 0.25) !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"][data-selected="true"] div[data-testid="stMarkdownContainer"] p,
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input:checked) div[data-testid="stMarkdownContainer"] p {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.84rem !important;
    font-weight: 600 !important;
    color: #FFFFFF !important;
}

/* Calibration Sliders — Sophos Dark Styling */
div[data-testid="stSlider"] {
    background: transparent !important;
    border: none !important;
    padding: 0 0.4rem 0.4rem 0.4rem !important;
    box-shadow: none !important;
}

div[data-testid="stSlider"] label {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.76rem !important;
    font-weight: 500 !important;
    color: #9CA3AF !important;
    margin-bottom: 3px !important;
}

div[data-testid="stSlider"] [data-baseweb="slider"] {
    margin-top: 4px !important;
}

div[data-testid="stSlider"] [data-baseweb="slider"] > div:first-child {
    background: #1A1D26 !important;
}

div[data-testid="stSlider"] [role="slider"] {
    background: #7C6FF0 !important;
    border: 2px solid #FFFFFF !important;
    box-shadow: 0 0 12px rgba(124, 111, 240, 0.5) !important;
    width: 16px !important;
    height: 16px !important;
}

div[data-testid="stSlider"] [data-testid="stSliderThumbValue"],
div[data-testid="stSlider"] [data-testid="stSliderTickBar"] {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.7rem !important;
    color: #6B7280 !important;
}

/* Top Command / Breadcrumb Bar */
.top-command-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #161922;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 0.7rem 1.2rem;
    margin-bottom: 0.9rem;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.2);
}

.breadcrumb-trail {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.82rem;
    font-family: 'Inter', sans-serif;
    color: #9CA3AF;
    font-weight: 500;
}

.breadcrumb-active {
    color: #FFFFFF;
    font-weight: 600;
}

.telemetry-pill-group {
    display: flex;
    align-items: center;
    gap: 8px;
}

.top-telemetry-pill {
    background: #1A1D26;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    padding: 4px 11px;
    font-family: 'Inter', sans-serif;
    font-size: 0.72rem;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* Action Buttons (Outline and Primary) */
.stButton > button {
    background: #161922 !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 10px !important;
    color: #E2E8F0 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    padding: 0.6rem 1.1rem !important;
    width: 100% !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15) !important;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.stButton > button:hover {
    border-color: rgba(124, 111, 240, 0.5) !important;
    background: rgba(124, 111, 240, 0.1) !important;
    color: #FFFFFF !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 16px rgba(124, 111, 240, 0.2) !important;
}

/* File Uploader Container */
div[data-testid="stFileUploader"] {
    background: #161922 !important;
    border: 1px dashed rgba(255, 255, 255, 0.15) !important;
    border-radius: 14px !important;
    padding: 1rem !important;
    transition: all 0.2s ease !important;
}

div[data-testid="stFileUploader"]:hover {
    border-color: rgba(124, 111, 240, 0.5) !important;
    background: #181C26 !important;
}

div[data-testid="stFileUploader"] section {
    background: transparent !important;
    border: none !important;
}

div[data-testid="stFileUploader"] button {
    background: #7C6FF0 !important;
    border: none !important;
    border-radius: 8px !important;
    color: #FFFFFF !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.78rem !important;
}

/* Tabs Styling */
div[data-testid="stTabs"] [data-baseweb="tab-list"] {
    gap: 8px !important;
    background-color: transparent !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
    padding-bottom: 6px !important;
}

div[data-testid="stTabs"] [data-baseweb="tab"] {
    background: transparent !important;
    border: none !important;
    border-radius: 8px !important;
    color: #9CA3AF !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.84rem !important;
    font-weight: 500 !important;
    padding: 7px 16px !important;
}

div[data-testid="stTabs"] [aria-selected="true"] {
    background: rgba(124, 111, 240, 0.15) !important;
    border: 1px solid rgba(124, 111, 240, 0.3) !important;
    color: #FFFFFF !important;
    font-weight: 600 !important;
}

/* 3-Exhibit Card Frames */
.exhibit-card-frame {
    background: #161922;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 0.9rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}

.exhibit-header-tag {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-bottom: 10px;
    padding-bottom: 8px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    font-family: 'Inter', sans-serif;
    font-size: 0.74rem;
    font-weight: 600;
}

.exhibit-card-frame img,
div[data-testid="stImage"] img {
    max-height: 290px !important;
    width: auto !important;
    max-width: 100% !important;
    margin: 0 auto !important;
    display: block !important;
    border-radius: 10px !important;
    object-fit: contain !important;
}

/* Section Title Micro-Labels */
.eyebrow-label {
    font-family: 'Inter', sans-serif;
    font-size: 0.66rem;
    font-weight: 700;
    color: #9CA3AF;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* Incident Cockpit Card */
.incident-cockpit-card {
    background: #161922;
    border-radius: 14px;
    padding: 1.3rem 1.5rem;
    margin-top: 0.9rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

/* Benchmark KPI Tiles (Exact Sophos Top 4 Cards) */
.bench-kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin-bottom: 1.1rem;
}

.bench-kpi-card {
    background: #161922;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 16px 18px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    transition: all 0.2s ease;
}

.bench-kpi-card:hover {
    border-color: rgba(255, 255, 255, 0.16);
    transform: translateY(-2px);
}

.bench-kpi-icon-chip {
    width: 36px;
    height: 36px;
    border-radius: 10px;
    background: #1A1D26;
    border: 1px solid rgba(255, 255, 255, 0.08);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 12px;
}

.bench-kpi-label {
    font-family: 'Inter', sans-serif;
    font-size: 0.68rem;
    font-weight: 600;
    color: #9CA3AF;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
}

.bench-kpi-value {
    font-family: 'Inter', sans-serif;
    font-size: 1.85rem;
    font-weight: 800;
    color: #FFFFFF;
    line-height: 1.1;
    margin-bottom: 6px;
}

.bench-kpi-sub {
    font-family: 'Inter', sans-serif;
    font-size: 0.74rem;
    font-weight: 500;
    color: #9CA3AF;
}

/* Head to Head Model Cards */
.model-matrix-card {
    background: #161922;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 1.3rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 370px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}

.model-matrix-card.recommended {
    border: 1.5px solid rgba(124, 111, 240, 0.6);
    box-shadow: 0 4px 24px rgba(124, 111, 240, 0.18);
}

.progress-track-dark {
    width: 100%;
    height: 7px;
    background: #1A1D26;
    border-radius: 4px;
    overflow: hidden;
}

.progress-fill-rounded {
    height: 100%;
    border-radius: 4px;
}

/* Alert & Notice Banners */
div[data-testid="stAlert"] {
    background: #161922 !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.8rem !important;
    color: #E2E8F0 !important;
}
</style>
"""
