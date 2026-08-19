PREMIUM_CSS = """
<style>
/* ============================================================
   FORGEGUARD ENTERPRISE FORENSIC COMMAND CENTER CSS (v4.0)
   Permanent SaaS Sidebar Rail + Zero-Gap + Reopen Safeguard
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
        radial-gradient(circle at 50% 0%, rgba(139, 92, 246, 0.10) 0%, transparent 45%),
        radial-gradient(circle at 0% 30%, rgba(0, 240, 255, 0.04) 0%, transparent 40%),
        radial-gradient(circle at 100% 70%, rgba(16, 185, 129, 0.04) 0%, transparent 40%),
        linear-gradient(rgba(255, 255, 255, 0.012) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.012) 1px, transparent 1px) !important;
    background-size: 100% 100%, 100% 100%, 100% 100%, 48px 48px, 48px 48px !important;
    background-position: center, center, center, -1px -1px, -1px -1px !important;
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
    padding-top: 0.2rem !important;
    padding-bottom: 1rem !important;
    padding-left: 1.2rem !important;
    padding-right: 1.2rem !important;
    max-width: 99% !important;
}

div[data-testid="stVerticalBlock"] {
    gap: 0.45rem !important;
}

/* ============================================================
   PERMANENT SIDEBAR RAIL (Sophos & Nightfall Style)
   ============================================================ */
section[data-testid="stSidebar"] {
    background-color: #0A0E17 !important;
    border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
    padding-top: 0.4rem !important;
    visibility: visible !important;
}

/* Hide the collapse button inside sidebar to prevent accidental collapse */
[data-testid="stSidebarCollapseButton"],
section[data-testid="stSidebar"] [data-testid="stSidebarHeader"] button,
section[data-testid="stSidebar"] button[kind="header"],
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] {
    display: none !important;
}

/* ALWAYS PROMINENT REOPEN TOGGLE (If ever collapsed in localStorage) */
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"],
button[data-testid="stSidebarCollapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    position: fixed !important;
    top: 0.5rem !important;
    left: 0.5rem !important;
    z-index: 999999 !important;
    background: #0B111E !important;
    border: 1.5px solid #00F0FF !important;
    border-radius: 8px !important;
    color: #00F0FF !important;
    box-shadow: 0 0 15px rgba(0, 240, 255, 0.5) !important;
    cursor: pointer !important;
    padding: 4px 6px !important;
}

[data-testid="stSidebarCollapsedControl"]:hover,
[data-testid="collapsedControl"]:hover {
    background: rgba(0, 240, 255, 0.15) !important;
    transform: scale(1.05) !important;
}

[data-testid="stSidebarCollapsedControl"] svg,
[data-testid="collapsedControl"] svg {
    fill: #00F0FF !important;
    stroke: #00F0FF !important;
}

section[data-testid="stSidebar"] > div:first-child {
    padding-top: 0.4rem !important;
    padding-left: 0.9rem !important;
    padding-right: 0.9rem !important;
}

.rail-section-header {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    font-weight: 700;
    color: #64748B;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin: 0.75rem 0 0.35rem 0;
    display: flex;
    align-items: center;
    gap: 6px;
}

div[data-testid="stRadio"] > div {
    gap: 5px !important;
}

div[data-testid="stRadio"] label {
    background: rgba(255, 255, 255, 0.02) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 8px !important;
    padding: 0.5rem 0.75rem !important;
    transition: all 0.2s ease !important;
    cursor: pointer !important;
    width: 100% !important;
}

div[data-testid="stRadio"] label:hover {
    background: rgba(0, 240, 255, 0.05) !important;
    border-color: rgba(0, 240, 255, 0.3) !important;
    transform: translateX(2px) !important;
}

div[data-testid="stRadio"] label[data-checked="true"],
div[data-testid="stRadio"] label:has(input:checked) {
    background: linear-gradient(90deg, rgba(0, 240, 255, 0.12) 0%, rgba(139, 92, 246, 0.06) 100%) !important;
    border: 1px solid rgba(0, 240, 255, 0.5) !important;
    box-shadow: 0 2px 10px rgba(0, 240, 255, 0.12) !important;
}

div[data-testid="stRadio"] label div[data-testid="stMarkdownContainer"] p {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    color: #F8FAFC !important;
}

/* Top Command Bar */
.top-command-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #0B111E;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    padding: 0.5rem 1rem;
    margin-bottom: 0.5rem;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
}

.breadcrumb-trail {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 0.78rem;
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
    gap: 6px;
}

.top-telemetry-pill {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 6px;
    padding: 2px 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
}

/* Action Buttons */
.stButton > button {
    background: linear-gradient(180deg, #131B2E 0%, #0D1322 100%) !important;
    border: 1px solid rgba(0, 240, 255, 0.3) !important;
    border-radius: 8px !important;
    color: #F8FAFC !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.8rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.8px !important;
    padding: 0.5rem 0.9rem !important;
    width: 100% !important;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4) !important;
    transition: all 0.2s ease !important;
}

.stButton > button:hover {
    border-color: #00F0FF !important;
    box-shadow: 0 0 16px rgba(0, 240, 255, 0.35) !important;
    transform: translateY(-1px) !important;
    color: #00F0FF !important;
}

/* File Uploader */
div[data-testid="stFileUploader"] {
    background: #0B111E !important;
    border: 1.5px dashed rgba(0, 240, 255, 0.35) !important;
    border-radius: 10px !important;
    padding: 0.6rem !important;
    transition: all 0.2s ease !important;
}

/* 3-EXHIBIT IMAGE CONTAINMENT */
.exhibit-card-frame {
    background: #0B111E;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    padding: 0.6rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    display: flex;
    flex-direction: column;
    align-items: center;
}

.exhibit-header-tag {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-bottom: 6px;
    padding-bottom: 4px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    font-weight: 700;
}

.exhibit-card-frame img,
div[data-testid="stImage"] img {
    max-height: 290px !important;
    width: auto !important;
    max-width: 100% !important;
    margin: 0 auto !important;
    display: block !important;
    border-radius: 6px !important;
    object-fit: contain !important;
    box-shadow: 0 2px 10px rgba(0,0,0,0.5);
}

.eyebrow-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
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
