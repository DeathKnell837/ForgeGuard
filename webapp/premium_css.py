PREMIUM_CSS = """
<style>
/* ============================================================
   FORGEGUARD SOPHOS AI CYBERSECURITY DESIGN SYSTEM (v6.2)
   Calibrated Saturation, Hairline Borders & Generous Spacing
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
        radial-gradient(circle at 50% 0%, rgba(124, 111, 240, 0.04) 0%, transparent 60%),
        radial-gradient(circle at 100% 100%, rgba(45, 212, 191, 0.02) 0%, transparent 50%) !important;
    background-attachment: fixed !important;
}

/* ZERO TOP WHITESPACE (Clean Header & No Wide Forehead) */
header[data-testid="stHeader"] {
    display: none !important;
    height: 0px !important;
    min-height: 0px !important;
    padding: 0px !important;
    margin: 0px !important;
    z-index: -1 !important;
}

div[data-testid="stAppViewContainer"] > section.main,
section[data-testid="stMain"] {
    padding-top: 0px !important;
}

div[data-testid="stMainBlockContainer"],
.stMainBlockContainer,
.block-container,
div[data-testid="stAppViewBlockContainer"] {
    padding-top: 0.8rem !important;
    padding-bottom: 2rem !important;
    padding-left: 1.8rem !important;
    padding-right: 1.8rem !important;
    max-width: 98% !important;
}

/* Generous Breathing Room Between Vertical Blocks */
div[data-testid="stVerticalBlock"] {
    gap: 1.2rem !important;
}

/* ============================================================
   CYBER FORENSIC SCANNER (ANIMATED LASER BEAM HUD)
   ============================================================ */
.cyber-scanner-frame {
    position: relative;
    background: #101216;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 14px;
    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.35);
}

.cyber-scanner-hud {
    position: relative;
    border-radius: 10px;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #060910;
    border: 1px solid rgba(255, 255, 255, 0.04);
}

.cyber-scanner-laser {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, transparent, #2DD4BF, #7C6FF0, #2DD4BF, transparent);
    box-shadow: 0 0 16px #2DD4BF, 0 0 28px rgba(124, 111, 240, 0.8);
    z-index: 10;
    animation: cyber-laser-sweep 2.8s ease-in-out infinite alternate;
    pointer-events: none;
}

.cyber-scanner-radar-glow {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 48px;
    background: linear-gradient(180deg, rgba(45, 212, 191, 0.16), transparent);
    z-index: 9;
    animation: cyber-laser-sweep 2.8s ease-in-out infinite alternate;
    pointer-events: none;
}

@keyframes cyber-laser-sweep {
    0% {
        top: 0%;
        opacity: 0.7;
    }
    50% {
        opacity: 1;
    }
    100% {
        top: calc(100% - 4px);
        opacity: 0.7;
    }
}

.cyber-corner-tl {
    position: absolute;
    top: 6px;
    left: 6px;
    width: 14px;
    height: 14px;
    border-top: 2px solid #2DD4BF;
    border-left: 2px solid #2DD4BF;
    z-index: 12;
    pointer-events: none;
}

.cyber-corner-tr {
    position: absolute;
    top: 6px;
    right: 6px;
    width: 14px;
    height: 14px;
    border-top: 2px solid #2DD4BF;
    border-right: 2px solid #2DD4BF;
    z-index: 12;
    pointer-events: none;
}

.cyber-corner-bl {
    position: absolute;
    bottom: 6px;
    left: 6px;
    width: 14px;
    height: 14px;
    border-bottom: 2px solid #2DD4BF;
    border-left: 2px solid #2DD4BF;
    z-index: 12;
    pointer-events: none;
}

.cyber-corner-br {
    position: absolute;
    bottom: 6px;
    right: 6px;
    width: 14px;
    height: 14px;
    border-bottom: 2px solid #2DD4BF;
    border-right: 2px solid #2DD4BF;
    z-index: 12;
    pointer-events: none;
}

/* ============================================================
   CYBER FORENSIC LOADING ANIMATION (Zero Emoji, Enterprise HUD)
   ============================================================ */
.cyber-loader-card {
    background: #101216;
    border: 1px solid rgba(124, 111, 240, 0.3);
    border-radius: 14px;
    padding: 22px 26px;
    margin: 1.2rem 0;
    box-shadow: 0 10px 36px rgba(0, 0, 0, 0.45), 0 0 24px rgba(124, 111, 240, 0.14);
    position: relative;
    overflow: hidden;
}

.cyber-loader-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: -100%;
    width: 200%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #2DD4BF, #7C6FF0, transparent);
    animation: cyber-top-shimmer 2.2s linear infinite;
}

@keyframes cyber-top-shimmer {
    0% { transform: translateX(0%); }
    100% { transform: translateX(100%); }
}

.cyber-loader-spinner {
    width: 24px;
    height: 24px;
    border: 2.5px solid rgba(45, 212, 191, 0.18);
    border-top: 2.5px solid #2DD4BF;
    border-right: 2.5px solid #7C6FF0;
    border-radius: 50%;
    animation: cyber-spin 0.8s linear infinite;
    flex-shrink: 0;
    box-shadow: 0 0 10px rgba(45, 212, 191, 0.3);
}

@keyframes cyber-spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.cyber-loader-progress-track {
    width: 100%;
    height: 6px;
    background: #1A1D26;
    border-radius: 999px;
    overflow: hidden;
    position: relative;
    border: 1px solid rgba(255, 255, 255, 0.06);
}

.cyber-loader-progress-bar {
    height: 100%;
    background: linear-gradient(90deg, #7C6FF0, #2DD4BF);
    border-radius: 999px;
    position: relative;
    transition: width 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 0 12px rgba(45, 212, 191, 0.6);
}

.cyber-loader-pulse-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #2DD4BF;
    box-shadow: 0 0 8px #2DD4BF;
    display: inline-block;
    animation: cyber-pulse 1.1s ease-in-out infinite alternate;
}

@keyframes cyber-pulse {
    0% { opacity: 0.35; transform: scale(0.85); }
    100% { opacity: 1; transform: scale(1.2); }
}

/* ============================================================
   SOPHOS SIDEBAR RAIL (Flush Top Header)
   ============================================================ */
section[data-testid="stSidebar"] {
    background-color: #101216 !important;
    border-right: 1px solid rgba(255, 255, 255, 0.06) !important;
    padding-top: 0px !important;
    min-width: 300px !important;
    width: 300px !important;
    visibility: visible !important;
}

/* Eliminate empty sidebar header (wide forehead) */
section[data-testid="stSidebar"] [data-testid="stSidebarHeader"],
[data-testid="stSidebarHeader"] {
    display: none !important;
    height: 0px !important;
    min-height: 0px !important;
    padding: 0px !important;
    margin: 0px !important;
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
    background: rgba(139, 92, 246, 0.15) !important;
    border-color: rgba(139, 92, 246, 0.3) !important;
}

div[data-testid="stSidebarContent"] {
    padding: 0.8rem 1.1rem 1.2rem 1.1rem !important;
    padding-top: 0.8rem !important;
}

div[data-testid="stSidebarUserContent"] {
    padding: 0 0 2rem 0 !important;
}

/* Section Header Labels — Exact Sophos MENU style */
.rail-section-header {
    font-family: 'Inter', -apple-system, sans-serif !important;
    font-size: 0.64rem !important;
    font-weight: 700 !important;
    color: #6B7280 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    margin-top: 24px !important;
    margin-bottom: 12px !important;
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
    gap: 6px !important;
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
    display: flex !important;
    align-items: center !important;
    visibility: visible !important;
    opacity: 1 !important;
}

/* Inactive Nav text */
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

/* ============================================================
   FORENSIC LAYER SWITCHER (PURE SVG MASKS, ZERO EMOJIS)
   ============================================================ */
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input[value="Original Receipt"]) div[data-testid="stMarkdownContainer"] p::before {
    content: "";
    display: inline-block;
    width: 14px;
    height: 14px;
    margin-right: 8px;
    background-color: currentColor;
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='3' width='18' height='18' rx='2' ry='2'/%3E%3Ccircle cx='8.5' cy='8.5' r='1.5'/%3E%3Cpolyline points='21 15 16 10 5 21'/%3E%3C/svg%3E") no-repeat center / contain;
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='3' width='18' height='18' rx='2' ry='2'/%3E%3Ccircle cx='8.5' cy='8.5' r='1.5'/%3E%3Cpolyline points='21 15 16 10 5 21'/%3E%3C/svg%3E") no-repeat center / contain;
    flex-shrink: 0;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input[value="ELA Noise Matrix"]) div[data-testid="stMarkdownContainer"] p::before {
    content: "";
    display: inline-block;
    width: 14px;
    height: 14px;
    margin-right: 8px;
    background-color: currentColor;
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'/%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'/%3E%3C/svg%3E") no-repeat center / contain;
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'/%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'/%3E%3C/svg%3E") no-repeat center / contain;
    flex-shrink: 0;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input[value="Splicing Heatmap"]) div[data-testid="stMarkdownContainer"] p::before {
    content: "";
    display: inline-block;
    width: 14px;
    height: 14px;
    margin-right: 8px;
    background-color: currentColor;
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M14 14.76V3.5a2.5 2.5 0 0 0-5 0v11.26a4.5 4.5 0 1 0 5 0z'/%3E%3C/svg%3E") no-repeat center / contain;
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M14 14.76V3.5a2.5 2.5 0 0 0-5 0v11.26a4.5 4.5 0 1 0 5 0z'/%3E%3C/svg%3E") no-repeat center / contain;
    flex-shrink: 0;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"]:hover div[data-testid="stMarkdownContainer"] p {
    color: #FFFFFF !important;
}

/* Soft, Low-Opacity Active Nav Highlight */
div[data-testid="stRadio"] label[data-testid="stRadioOption"][data-selected="true"],
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input:checked) {
    background: rgba(139, 92, 246, 0.10) !important;
    border: 1px solid rgba(139, 92, 246, 0.18) !important;
    box-shadow: none !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"][data-selected="true"] div[data-testid="stMarkdownContainer"] p,
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input:checked) div[data-testid="stMarkdownContainer"] p {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.86rem !important;
    font-weight: 600 !important;
    color: #FFFFFF !important;
}

/* Advanced Calibration Collapsible Expander in Sidebar */
section[data-testid="stSidebar"] div[data-testid="stExpander"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    margin-top: 18px !important;
    margin-bottom: 12px !important;
}

section[data-testid="stSidebar"] div[data-testid="stExpander"] details {
    background: transparent !important;
    border: none !important;
}

section[data-testid="stSidebar"] div[data-testid="stExpander"] summary {
    background: transparent !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 8px 10px !important;
    color: #9CA3AF !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.76rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.4px !important;
    transition: all 0.15s ease !important;
}

section[data-testid="stSidebar"] div[data-testid="stExpander"] summary:hover {
    background: rgba(255, 255, 255, 0.04) !important;
    color: #FFFFFF !important;
}

section[data-testid="stSidebar"] div[data-testid="stExpander"] summary svg {
    fill: #6B7280 !important;
    width: 14px !important;
    height: 14px !important;
}

section[data-testid="stSidebar"] div[data-testid="stExpander"] div[data-testid="stExpanderDetails"] {
    background: transparent !important;
    border: none !important;
    padding: 10px 4px 4px 4px !important;
}

/* Calibration Sliders — Sophos Dark Styling */
div[data-testid="stSlider"] {
    background: transparent !important;
    border: none !important;
    padding: 0 0.2rem 0.6rem 0.2rem !important;
    box-shadow: none !important;
}

div[data-testid="stSlider"] label {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.74rem !important;
    font-weight: 500 !important;
    color: #9CA3AF !important;
    margin-bottom: 2px !important;
}

div[data-testid="stSlider"] [data-baseweb="slider"] {
    margin-top: 2px !important;
}

div[data-testid="stSlider"] [data-baseweb="slider"] > div:first-child {
    background: #1A1D26 !important;
}

div[data-testid="stSlider"] [role="slider"] {
    background: #7C6FF0 !important;
    border: 2px solid #FFFFFF !important;
    box-shadow: 0 0 8px rgba(124, 111, 240, 0.4) !important;
    width: 14px !important;
    height: 14px !important;
}

div[data-testid="stSlider"] [data-testid="stSliderThumbValue"],
div[data-testid="stSlider"] [data-testid="stSliderTickBar"] {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.68rem !important;
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
    padding: 0.8rem 1.4rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
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
    padding: 5px 12px;
    font-family: 'Inter', sans-serif;
    font-size: 0.72rem;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* Neutral Outline Action Buttons (Secondary) */
.stButton > button {
    background: transparent !important;
    border: 1px solid rgba(255, 255, 255, 0.10) !important;
    border-radius: 10px !important;
    color: #9CA3AF !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    padding: 0.65rem 1.2rem !important;
    width: 100% !important;
    box-shadow: none !important;
    transition: all 0.15s ease !important;
}

.stButton > button:hover {
    border-color: rgba(255, 255, 255, 0.25) !important;
    background: rgba(255, 255, 255, 0.04) !important;
    color: #FFFFFF !important;
    transform: none !important;
    box-shadow: none !important;
}

/* File Uploader Container */
div[data-testid="stFileUploader"] {
    background: #161922 !important;
    border: 1px dashed rgba(255, 255, 255, 0.14) !important;
    border-radius: 14px !important;
    padding: 1.2rem !important;
    margin-top: 0.4rem !important;
    transition: all 0.2s ease !important;
}

div[data-testid="stFileUploader"]:hover {
    border-color: rgba(255, 255, 255, 0.25) !important;
    background: #181C26 !important;
}

div[data-testid="stFileUploader"] section {
    background: transparent !important;
    border: none !important;
}

/* Primary CTA Button (Upload) - Solid Controlled Violet */
div[data-testid="stFileUploader"] button {
    background: #7C6FF0 !important;
    border: none !important;
    border-radius: 8px !important;
    color: #FFFFFF !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.78rem !important;
    box-shadow: 0 2px 8px rgba(124, 111, 240, 0.3) !important;
}

div[data-testid="stFileUploader"] button:hover {
    background: #6D5DE7 !important;
}

/* Tabs Styling */
div[data-testid="stTabs"] [data-baseweb="tab-list"] {
    gap: 8px !important;
    background-color: transparent !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
    padding-bottom: 6px !important;
    margin-top: 0.6rem !important;
}

div[data-testid="stTabs"] [data-baseweb="tab"] {
    background: transparent !important;
    border: none !important;
    border-radius: 8px !important;
    color: #9CA3AF !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.84rem !important;
    font-weight: 500 !important;
    padding: 8px 18px !important;
}

div[data-testid="stTabs"] [aria-selected="true"] {
    background: rgba(255, 255, 255, 0.06) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    color: #FFFFFF !important;
    font-weight: 600 !important;
}

/* 3-Exhibit Card Frames */
.exhibit-card-frame {
    background: #161922;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 1.2rem;
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
    margin-bottom: 12px;
    padding-bottom: 10px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    font-family: 'Inter', sans-serif;
    font-size: 0.76rem;
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
    padding: 1.6rem 1.8rem;
    margin-top: 1.4rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
}

/* Benchmark KPI Tiles (Exact Sophos Top 4 Cards) */
.bench-kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 1.5rem;
}

.bench-kpi-card {
    background: #161922;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 20px 22px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    transition: all 0.2s ease;
}

.bench-kpi-card:hover {
    border-color: rgba(255, 255, 255, 0.14);
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
    margin-bottom: 14px;
}

.bench-kpi-label {
    font-family: 'Inter', sans-serif;
    font-size: 0.68rem;
    font-weight: 600;
    color: #9CA3AF;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
}

.bench-kpi-value {
    font-family: 'Inter', sans-serif;
    font-size: 1.85rem;
    font-weight: 800;
    color: #FFFFFF;
    line-height: 1.1;
    margin-bottom: 8px;
}

.bench-kpi-sub {
    font-family: 'Inter', sans-serif;
    font-size: 0.74rem;
    font-weight: 500;
    color: #9CA3AF;
}

/* Head to Head Model Cards - All Flat Hairline Borders */
.model-matrix-card {
    background: #161922;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 1.6rem 1.6rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 380px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}

.model-matrix-card.recommended {
    border: 1px solid rgba(255, 255, 255, 0.08);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
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

/* Sophos Hatched Progress Track & Glowing Capsule Fill */
.sophos-hatched-track {
    width: 100%;
    height: 9px;
    background-color: #1A1D26;
    background-image: repeating-linear-gradient(45deg, transparent, transparent 5px, rgba(255, 255, 255, 0.03) 5px, rgba(255, 255, 255, 0.03) 10px);
    border-radius: 6px;
    position: relative;
    overflow: visible;
}

.sophos-hatched-fill {
    height: 100%;
    border-radius: 6px;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: flex-end;
}

.sophos-hatched-fill.purple {
    background: linear-gradient(90deg, #4338CA 0%, #6366F1 100%);
    box-shadow: 0 0 10px rgba(99, 102, 241, 0.35);
}

.sophos-hatched-fill.emerald {
    background: linear-gradient(90deg, #047857 0%, #10B981 100%);
    box-shadow: 0 0 10px rgba(16, 185, 129, 0.35);
}

.sophos-hatched-fill.slate {
    background: linear-gradient(90deg, #334155 0%, #64748B 100%);
}

.sophos-thumb {
    width: 13px;
    height: 13px;
    border-radius: 50%;
    background: #1A1D26;
    border: 2px solid #FFFFFF;
    box-shadow: 0 0 6px rgba(0, 0, 0, 0.6);
    position: absolute;
    right: -3px;
    top: -2px;
}

/* Sophos 3D Pillar Columns */
.sophos-pillar {
    width: 12px;
    border-radius: 5px 5px 3px 3px;
    transition: all 0.2s ease;
}

.sophos-pillar.purple {
    background: linear-gradient(180deg, #818CF8 0%, #4338CA 100%);
    box-shadow: 0 0 8px rgba(99, 102, 241, 0.3);
}

.sophos-pillar.slate {
    background: linear-gradient(180deg, #64748B 0%, #1E293B 100%);
}

</style>
"""
