PREMIUM_CSS = """
<style>
/* ============================================================
   FORGEGUARD SOPHOS ENTERPRISE FORENSIC SYSTEM CSS (v5.0)
   Sophos AI Smart Cybersecurity Visual Identity
   ============================================================ */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

/* Global Surface & Canvas */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    background-color: #0A0A0C !important;
    color: #E2E8F0 !important;
}

.stApp {
    background-color: #0A0A0C !important;
    background-image: radial-gradient(circle at 50% 0%, rgba(124, 111, 240, 0.05) 0%, transparent 50%) !important;
    background-attachment: fixed !important;
}

/* ZERO TOP WHITESPACE (Clean Header that preserves sidebar toggle) */
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
    padding-bottom: 1.5rem !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
    max-width: 98% !important;
}

div[data-testid="stVerticalBlock"] {
    gap: 0.6rem !important;
}

/* ============================================================
   SOPHOS FLAT SIDEBAR RAIL
   ============================================================ */
section[data-testid="stSidebar"] {
    background-color: #0A0A0C !important;
    border-right: 1px solid #232326 !important;
    padding-top: 0.2rem !important;
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
    background: #111114 !important;
    border: 1px solid #7C6FF0 !important;
    border-radius: 8px !important;
    color: #7C6FF0 !important;
    box-shadow: 0 4px 16px rgba(124, 111, 240, 0.25) !important;
    cursor: pointer !important;
    padding: 6px 8px !important;
    transition: all 0.2s ease !important;
}

[data-testid="stSidebarCollapsedControl"]:hover,
[data-testid="collapsedControl"]:hover {
    background: rgba(124, 111, 240, 0.15) !important;
    transform: scale(1.05) !important;
}

[data-testid="stSidebarCollapsedControl"] svg,
[data-testid="collapsedControl"] svg {
    fill: #7C6FF0 !important;
    stroke: #7C6FF0 !important;
}

section[data-testid="stSidebar"] > div:first-child {
    padding-top: 0.6rem !important;
    padding-left: 0.9rem !important;
    padding-right: 0.9rem !important;
}

/* Section Header Labels — Small, Muted Uppercase with Generous Whitespace */
.rail-section-header {
    font-family: 'Inter', -apple-system, sans-serif !important;
    font-size: 0.65rem !important;
    font-weight: 700 !important;
    color: #8A8A94 !important;
    letter-spacing: 1.2px !important;
    text-transform: uppercase !important;
    margin-top: 24px !important;
    margin-bottom: 8px !important;
    padding-left: 0.5rem !important;
    border: none !important;
    background: transparent !important;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* Flat Spacious Radio Buttons (Navigation & Model Selector) */
div[data-testid="stRadio"] > div {
    gap: 4px !important;
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}

div[data-testid="stRadio"] [data-baseweb="radio"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
}

div[data-testid="stRadio"] [data-baseweb="radio"] > div {
    background: transparent !important;
    border: none !important;
}

/* Remove all radio circles, dots, and native rings completely */
div[data-testid="stRadio"] label > div:first-of-type:not([data-testid="stMarkdownContainer"]),
div[data-testid="stRadio"] [data-baseweb="radio"] > div:first-of-type:not([data-testid="stMarkdownContainer"]),
div[data-testid="stRadio"] [data-baseweb="radio"] input + div,
div[data-testid="stRadio"] label input + div,
div[data-testid="stRadio"] [data-testid="stRadioDot"],
div[data-testid="stRadio"] input[type="radio"],
div[data-testid="stRadio"] [aria-hidden="true"],
div[data-testid="stRadio"] label > div:not([data-testid="stMarkdownContainer"]):not(:has([data-testid="stMarkdownContainer"])) {
    display: none !important;
    width: 0px !important;
    height: 0px !important;
    min-width: 0px !important;
    min-height: 0px !important;
    border: none !important;
    outline: none !important;
    background: transparent !important;
    box-shadow: none !important;
    opacity: 0 !important;
    visibility: hidden !important;
    margin: 0 !important;
    padding: 0 !important;
}

/* Inactive items: completely flat, generous padding (12-14px), muted text, no borders */
div[data-testid="stRadio"] label {
    background: transparent !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.7rem 0.9rem !important;
    margin: 0 !important;
    transition: all 0.15s ease !important;
    cursor: pointer !important;
    width: 100% !important;
    box-shadow: none !important;
    display: flex !important;
    align-items: center !important;
}

div[data-testid="stRadio"] label:hover {
    background: rgba(255, 255, 255, 0.04) !important;
    border: none !important;
    box-shadow: none !important;
    transform: none !important;
}

div[data-testid="stRadio"] label div[data-testid="stMarkdownContainer"] {
    width: 100% !important;
}

div[data-testid="stRadio"] label div[data-testid="stMarkdownContainer"] p {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.84rem !important;
    font-weight: 500 !important;
    color: #8A8A94 !important;
    letter-spacing: 0.1px !important;
    margin: 0 !important;
    transition: color 0.15s ease !important;
    line-height: 1.4 !important;
}

div[data-testid="stRadio"] label:hover div[data-testid="stMarkdownContainer"] p {
    color: #FFFFFF !important;
}

/* Active item: solid filled violet-tinted rounded rect background, crisp white text */
div[data-testid="stRadio"] label[data-checked="true"],
div[data-testid="stRadio"] label:has(input:checked) {
    background: rgba(124, 111, 240, 0.14) !important;
    border: none !important;
    border-radius: 8px !important;
    box-shadow: none !important;
}

div[data-testid="stRadio"] label[data-checked="true"] div[data-testid="stMarkdownContainer"] p,
div[data-testid="stRadio"] label:has(input:checked) div[data-testid="stMarkdownContainer"] p {
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
    color: #8A8A94 !important;
    margin-bottom: 3px !important;
}

div[data-testid="stSlider"] [data-baseweb="slider"] {
    margin-top: 4px !important;
}

div[data-testid="stSlider"] [data-baseweb="slider"] > div:first-child {
    background: #16161A !important;
}

div[data-testid="stSlider"] [role="slider"] {
    background: #7C6FF0 !important;
    border: 2px solid #FFFFFF !important;
    box-shadow: 0 0 10px rgba(124, 111, 240, 0.4) !important;
    width: 16px !important;
    height: 16px !important;
}

div[data-testid="stSlider"] [data-testid="stSliderThumbValue"],
div[data-testid="stSlider"] [data-testid="stSliderTickBar"] {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.7rem !important;
    color: #8A8A94 !important;
}

/* Alert & Notice Banners */
div[data-testid="stAlert"] {
    background: #111114 !important;
    border: 1px solid #232326 !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.8rem !important;
    color: #E2E8F0 !important;
}

/* Top Command / Breadcrumb Bar */
.top-command-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #111114;
    border: 1px solid #232326;
    border-radius: 10px;
    padding: 0.65rem 1.1rem;
    margin-bottom: 0.8rem;
}

.breadcrumb-trail {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.82rem;
    font-family: 'Inter', sans-serif;
    color: #8A8A94;
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
    background: #16161A;
    border: 1px solid #232326;
    border-radius: 6px;
    padding: 3px 10px;
    font-family: 'Inter', sans-serif;
    font-size: 0.72rem;
}

/* Action Buttons (Outline and Primary) */
.stButton > button {
    background: #111114 !important;
    border: 1px solid #232326 !important;
    border-radius: 8px !important;
    color: #E2E8F0 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    padding: 0.55rem 1rem !important;
    width: 100% !important;
    box-shadow: none !important;
    transition: all 0.2s ease !important;
}

.stButton > button:hover {
    border-color: #7C6FF0 !important;
    background: rgba(124, 111, 240, 0.08) !important;
    color: #FFFFFF !important;
    transform: translateY(-1px) !important;
}

/* File Uploader Container */
div[data-testid="stFileUploader"] {
    background: #111114 !important;
    border: 1px solid #232326 !important;
    border-radius: 12px !important;
    padding: 0.8rem !important;
    transition: all 0.2s ease !important;
}

div[data-testid="stFileUploader"]:hover {
    border-color: rgba(124, 111, 240, 0.4) !important;
}

div[data-testid="stFileUploader"] section {
    background: transparent !important;
    border: none !important;
}

/* Tabs Styling */
div[data-testid="stTabs"] [data-baseweb="tab-list"] {
    gap: 8px !important;
    background-color: transparent !important;
    border-bottom: 1px solid #232326 !important;
    padding-bottom: 4px !important;
}

div[data-testid="stTabs"] [data-baseweb="tab"] {
    background: transparent !important;
    border: none !important;
    border-radius: 6px !important;
    color: #8A8A94 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.84rem !important;
    font-weight: 500 !important;
    padding: 6px 14px !important;
}

div[data-testid="stTabs"] [aria-selected="true"] {
    background: rgba(124, 111, 240, 0.12) !important;
    color: #FFFFFF !important;
    font-weight: 600 !important;
}

/* 3-Exhibit Card Frames */
.exhibit-card-frame {
    background: #111114;
    border: 1px solid #232326;
    border-radius: 12px;
    padding: 0.75rem;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.exhibit-header-tag {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-bottom: 8px;
    padding-bottom: 6px;
    border-bottom: 1px solid #232326;
    font-family: 'Inter', sans-serif;
    font-size: 0.72rem;
    font-weight: 600;
}

.exhibit-card-frame img,
div[data-testid="stImage"] img {
    max-height: 290px !important;
    width: auto !important;
    max-width: 100% !important;
    margin: 0 auto !important;
    display: block !important;
    border-radius: 8px !important;
    object-fit: contain !important;
}

/* Section Title Micro-Labels */
.eyebrow-label {
    font-family: 'Inter', sans-serif;
    font-size: 0.68rem;
    font-weight: 700;
    color: #8A8A94;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* Incident Cockpit Card */
.incident-cockpit-card {
    background: #111114;
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
    margin-top: 0.8rem;
}

/* Benchmark KPI Tiles */
.bench-kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-bottom: 1rem;
}

.bench-kpi-card {
    background: #111114;
    border: 1px solid #232326;
    border-radius: 12px;
    padding: 14px 16px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.bench-kpi-icon-chip {
    width: 32px;
    height: 32px;
    border-radius: 8px;
    background: #16161A;
    border: 1px solid #232326;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 10px;
}

.bench-kpi-label {
    font-family: 'Inter', sans-serif;
    font-size: 0.65rem;
    font-weight: 700;
    color: #8A8A94;
    letter-spacing: 1.1px;
    text-transform: uppercase;
    margin-bottom: 4px;
}

.bench-kpi-value {
    font-family: 'Inter', sans-serif;
    font-size: 1.8rem;
    font-weight: 800;
    color: #FFFFFF;
    line-height: 1;
    margin-bottom: 6px;
}

.bench-kpi-sub {
    font-family: 'Inter', sans-serif;
    font-size: 0.72rem;
    font-weight: 500;
    color: #8A8A94;
}

/* Head to Head Model Cards */
.model-matrix-card {
    background: #111114;
    border: 1px solid #232326;
    border-radius: 12px;
    padding: 1.2rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 360px;
}

.model-matrix-card.recommended {
    border: 1.5px solid #7C6FF0;
    box-shadow: 0 4px 24px rgba(124, 111, 240, 0.15);
}

.progress-track-dark {
    width: 100%;
    height: 6px;
    background: #16161A;
    border-radius: 3px;
    overflow: hidden;
}

.progress-fill-rounded {
    height: 100%;
    border-radius: 3px;
}
</style>
"""
