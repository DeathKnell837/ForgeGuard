PREMIUM_CSS = """
<style>
/* ============================================================
   FORGEGUARD SOPHOS AI CYBERSECURITY DESIGN SYSTEM (v9.0-SLATE-GRAY)
   Polished Enterprise Slate Gray, Responsive Glassmorphism & Zero-Emoji Purity
   ============================================================ */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

/* Global Surface & Canvas — Polished Slate Gray Tone */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    background-color: #121620 !important;
    color: #E2E8F0 !important;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    overflow-x: hidden !important;
    width: 100% !important;
    max-width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
}

.stApp {
    background-color: #121620 !important;
    background-image: 
        radial-gradient(circle at 50% 0%, rgba(124, 111, 240, 0.08) 0%, transparent 60%),
        radial-gradient(circle at 100% 100%, rgba(45, 212, 191, 0.05) 0%, transparent 50%),
        radial-gradient(circle at 0% 50%, rgba(99, 102, 241, 0.04) 0%, transparent 40%) !important;
    background-attachment: fixed !important;
    overflow-x: hidden !important;
    width: 100% !important;
    max-width: 100% !important;
}

/* ZERO TOP WHITESPACE (Transparent Header Preserving Sidebar Controls) */
header[data-testid="stHeader"] {
    background: transparent !important;
    height: 0px !important;
    min-height: 0px !important;
    padding: 0px !important;
    margin: 0px !important;
    border: none !important;
    pointer-events: none !important;
    z-index: 99999 !important;
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
}

header[data-testid="stHeader"] > * {
    pointer-events: auto !important;
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
    padding-bottom: 3.5rem !important;
    padding-left: 1.8rem !important;
    padding-right: 1.8rem !important;
    max-width: 98% !important;
}

/* Responsive Block Container for Mobile/Tablet */
@media (max-width: 768px) {
    div[data-testid="stMainBlockContainer"],
    .stMainBlockContainer,
    .block-container,
    div[data-testid="stAppViewBlockContainer"] {
        padding-top: 0.5rem !important;
        padding-bottom: 4rem !important;
        padding-left: 0.75rem !important;
        padding-right: 0.75rem !important;
        max-width: 100% !important;
    }
}

/* Generous Breathing Room Between Vertical Blocks */
div[data-testid="stVerticalBlock"] {
    gap: 1.2rem !important;
}

@media (max-width: 768px) {
    div[data-testid="stVerticalBlock"] {
        gap: 0.9rem !important;
    }
}

/* ============================================================
   CYBER FORENSIC SCANNER (EVALUATION HUD & CENTERED DISPLAY)
   ============================================================ */
.cyber-scanner-frame {
    position: relative;
    background: #1C2333;
    border: 1px solid rgba(255, 255, 255, 0.09);
    border-radius: 14px;
    padding: 16px;
    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.28);
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    width: 100%;
}

.cyber-scanner-hud {
    position: relative;
    border-radius: 10px;
    overflow: hidden;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    background: #141926;
    border: 1px solid rgba(255, 255, 255, 0.08);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
    margin: 0 auto;
    text-align: center;
    max-width: 100%;
}

.cyber-evidence-img {
    display: block;
    margin: 0 auto;
    width: auto;
    max-width: 100%;
    height: auto;
    max-height: 520px;
    object-fit: contain;
    border-radius: 6px;
}

@media (max-width: 768px) {
    .cyber-evidence-img {
        max-height: 380px;
    }
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
    animation: cyber-laser-sweep 2.2s ease-in-out infinite alternate;
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
    animation: cyber-laser-sweep 2.2s ease-in-out infinite alternate;
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
    background: #1C2333;
    border: 1px solid rgba(124, 111, 240, 0.35);
    border-radius: 14px;
    padding: 22px 26px;
    margin: 1.2rem 0;
    box-shadow: 0 10px 36px rgba(0, 0, 0, 0.35), 0 0 24px rgba(124, 111, 240, 0.16);
    position: relative;
    overflow: hidden;
}

@media (max-width: 768px) {
    .cyber-loader-card {
        padding: 16px 16px;
        margin: 0.8rem 0;
    }
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
    background: #252D40;
    border-radius: 999px;
    overflow: hidden;
    position: relative;
    border: 1px solid rgba(255, 255, 255, 0.08);
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
   SOPHOS SIDEBAR RAIL (Desktop Docked vs Mobile Off-Canvas Drawer)
   ============================================================ */
@media (min-width: 769px) {
    section[data-testid="stSidebar"] {
        background-color: #181D2A !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
        position: relative !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    section[data-testid="stSidebar"][aria-expanded="true"] {
        min-width: 280px !important;
        width: 280px !important;
        visibility: visible !important;
        transform: translateX(0%) !important;
    }

    section[data-testid="stSidebar"][aria-expanded="false"] {
        min-width: 0px !important;
        width: 0px !important;
        transform: translateX(-100%) !important;
        visibility: hidden !important;
    }

    /* Desktop Sidebar Header & Built-in Collapse Button */
    section[data-testid="stSidebar"] [data-testid="stSidebarHeader"],
    [data-testid="stSidebarHeader"] {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        height: 48px !important;
        min-height: 48px !important;
        padding: 8px 14px !important;
        margin: 0px !important;
        justify-content: flex-end !important;
        align-items: center !important;
        background: transparent !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"],
    section[data-testid="stSidebar"] [data-testid="stSidebarHeader"] button,
    section[data-testid="stSidebar"] button[kind="header"],
    section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] button {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        pointer-events: auto !important;
        background: #252D40 !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 8px !important;
        color: #E2E8F0 !important;
        width: 34px !important;
        height: 34px !important;
        min-width: 34px !important;
        min-height: 34px !important;
        padding: 0px !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3) !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"]:hover,
    section[data-testid="stSidebar"] [data-testid="stSidebarHeader"] button:hover {
        background: #2D374D !important;
        color: #FFFFFF !important;
        border-color: rgba(129, 140, 248, 0.6) !important;
        box-shadow: 0 0 12px rgba(129, 140, 248, 0.35) !important;
        transform: scale(1.05) !important;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] svg,
    section[data-testid="stSidebar"] [data-testid="stSidebarHeader"] button svg,
    section[data-testid="stSidebar"] button[kind="header"] svg {
        stroke: #CBD5E1 !important;
        fill: #CBD5E1 !important;
        width: 18px !important;
        height: 18px !important;
    }
}

@media (max-width: 768px) {
    div[data-testid="stAppViewContainer"],
    .stAppViewContainer,
    div[data-testid="stAppViewContainer"] > section.main,
    section[data-testid="stMain"],
    .stMain {
        display: block !important;
        width: 100% !important;
        max-width: 100% !important;
        min-width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow-x: hidden !important;
        left: 0 !important;
        position: relative !important;
    }

    div[data-testid="stMainBlockContainer"],
    .stMainBlockContainer,
    .block-container,
    div[data-testid="stAppViewBlockContainer"] {
        padding-top: 0.4rem !important;
        padding-bottom: 5rem !important;
        padding-left: 0.65rem !important;
        padding-right: 0.65rem !important;
        width: 100% !important;
        max-width: 100% !important;
        min-width: 100% !important;
        box-sizing: border-box !important;
    }

    section[data-testid="stSidebar"] {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        bottom: 0 !important;
        height: 100vh !important;
        z-index: 999999 !important;
        transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    section[data-testid="stSidebar"]:not([aria-expanded="true"]),
    section[data-testid="stSidebar"][aria-expanded="false"] {
        display: none !important;
        width: 0px !important;
        min-width: 0px !important;
        max-width: 0px !important;
        height: 0px !important;
        left: -9999px !important;
        visibility: hidden !important;
        pointer-events: none !important;
        transform: translateX(-110%) !important;
    }

    section[data-testid="stSidebar"][aria-expanded="true"] {
        display: block !important;
        visibility: visible !important;
        width: 280px !important;
        max-width: 82% !important;
        transform: translateX(0%) !important;
        box-shadow: 14px 0 44px rgba(0, 0, 0, 0.7) !important;
        background: #181D2A !important;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"],
    section[data-testid="stSidebar"] [data-testid="stSidebarHeader"] button,
    section[data-testid="stSidebar"] button[kind="header"] {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        pointer-events: auto !important;
        color: #FFFFFF !important;
        background: #252D40 !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 8px !important;
        margin: 8px !important;
        width: 34px !important;
        height: 34px !important;
        align-items: center !important;
        justify-content: center !important;
    }
}

/* Floating Reopen / Expand Sidebar Toggle Button (Always Visible & Clickable When Sidebar is Collapsed) */
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"],
button[data-testid="stSidebarCollapsedControl"],
div[data-testid="stSidebarCollapsedControl"] button,
header[data-testid="stHeader"] [data-testid="stSidebarCollapsedControl"],
header[data-testid="stHeader"] button {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    pointer-events: auto !important;
    position: fixed !important;
    top: 14px !important;
    left: 14px !important;
    z-index: 999999 !important;
    background: #1C2333 !important;
    border: 1px solid rgba(129, 140, 248, 0.5) !important;
    border-radius: 9px !important;
    color: #FFFFFF !important;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.45), 0 0 12px rgba(129, 140, 248, 0.3) !important;
    cursor: pointer !important;
    padding: 7px 10px !important;
    min-width: 38px !important;
    min-height: 38px !important;
    align-items: center !important;
    justify-content: center !important;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

[data-testid="stSidebarCollapsedControl"] svg,
button[data-testid="stSidebarCollapsedControl"] svg,
div[data-testid="stSidebarCollapsedControl"] button svg,
header[data-testid="stHeader"] [data-testid="stSidebarCollapsedControl"] svg,
header[data-testid="stHeader"] button svg {
    stroke: #FFFFFF !important;
    fill: #FFFFFF !important;
    width: 20px !important;
    height: 20px !important;
}

[data-testid="stSidebarCollapsedControl"]:hover,
[data-testid="collapsedControl"]:hover,
button[data-testid="stSidebarCollapsedControl"]:hover,
div[data-testid="stSidebarCollapsedControl"] button:hover,
header[data-testid="stHeader"] [data-testid="stSidebarCollapsedControl"]:hover,
header[data-testid="stHeader"] button:hover {
    background: #252D40 !important;
    border-color: #818CF8 !important;
    box-shadow: 0 4px 20px rgba(129, 140, 248, 0.5) !important;
    transform: scale(1.06) !important;
}

/* Responsive Column Stacking for Mobile Layouts */
@media (max-width: 768px) {
    div[data-testid="stHorizontalBlock"] {
        flex-direction: column !important;
        gap: 12px !important;
    }
    div[data-testid="column"],
    div[data-testid="stColumn"] {
        min-width: 100% !important;
        width: 100% !important;
        flex: 1 1 100% !important;
    }
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
    color: #94A3B8 !important;
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
    color: #CBD5E1 !important;
    margin: 0 !important;
    line-height: 1.4 !important;
    display: flex !important;
    align-items: center !important;
    transition: color 0.15s ease !important;
}

/* Sidebar Nav Item 1 Icon: Shield / Radar */
section[data-testid="stSidebar"] div[data-testid="stRadio"] label[data-testid="stRadioOption"]:nth-child(1) div[data-testid="stMarkdownContainer"] p::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 10px;
    background-color: currentColor;
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z'/%3E%3C/svg%3E") no-repeat center / contain;
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z'/%3E%3C/svg%3E") no-repeat center / contain;
    flex-shrink: 0;
}

/* Sidebar Nav Item 2 Icon: Analytics / Bar Chart */
section[data-testid="stSidebar"] div[data-testid="stRadio"] label[data-testid="stRadioOption"]:nth-child(2) div[data-testid="stMarkdownContainer"] p::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 10px;
    background-color: currentColor;
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='20' x2='18' y2='10'%3E%3C/line%3E%3Cline x1='12' y1='20' x2='12' y2='4'%3E%3C/line%3E%3Cline x1='6' y1='20' x2='6' y2='14'%3E%3C/line%3E%3C/svg%3E") no-repeat center / contain;
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='20' x2='18' y2='10'%3E%3C/line%3E%3Cline x1='12' y1='20' x2='12' y2='4'%3E%3C/line%3E%3Cline x1='6' y1='20' x2='6' y2='14'%3E%3C/line%3E%3C/svg%3E") no-repeat center / contain;
    flex-shrink: 0;
}

/* Inactive Hover */
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:hover {
    background: rgba(255, 255, 255, 0.05) !important;
    border-color: rgba(255, 255, 255, 0.08) !important;
}

/* ============================================================
   FORENSIC LAYER SWITCHER ICONS (Original Receipt, ELA Noise Matrix, Splicing Heatmap)
   ============================================================ */
.st-key-layer_switcher_radio div[data-testid="stRadioGroup"] label:nth-child(1) div[data-testid="stMarkdownContainer"] p::before,
div.st-key-layer_switcher_radio label[data-testid="stRadioOption"]:nth-child(1) div[data-testid="stMarkdownContainer"] p::before,
div[data-testid="stMainBlockContainer"] div.st-key-layer_switcher_radio label:nth-child(1) div[data-testid="stMarkdownContainer"] p::before,
div[data-testid="stMainBlockContainer"] div[data-testid="stRadio"] label[data-testid="stRadioOption"]:nth-child(1) div[data-testid="stMarkdownContainer"] p::before {
    content: "" !important;
    display: inline-block !important;
    width: 15px !important;
    height: 15px !important;
    margin-right: 8px !important;
    background-color: currentColor !important;
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='3' width='18' height='18' rx='2' ry='2'/%3E%3Ccircle cx='8.5' cy='8.5' r='1.5'/%3E%3Cpolyline points='21 15 16 10 5 21'/%3E%3C/svg%3E") no-repeat center / contain !important;
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='3' width='18' height='18' rx='2' ry='2'/%3E%3Ccircle cx='8.5' cy='8.5' r='1.5'/%3E%3Cpolyline points='21 15 16 10 5 21'/%3E%3C/svg%3E") no-repeat center / contain !important;
    flex-shrink: 0 !important;
}

.st-key-layer_switcher_radio div[data-testid="stRadioGroup"] label:nth-child(2) div[data-testid="stMarkdownContainer"] p::before,
div.st-key-layer_switcher_radio label[data-testid="stRadioOption"]:nth-child(2) div[data-testid="stMarkdownContainer"] p::before,
div[data-testid="stMainBlockContainer"] div.st-key-layer_switcher_radio label:nth-child(2) div[data-testid="stMarkdownContainer"] p::before,
div[data-testid="stMainBlockContainer"] div[data-testid="stRadio"] label[data-testid="stRadioOption"]:nth-child(2) div[data-testid="stMarkdownContainer"] p::before {
    content: "" !important;
    display: inline-block !important;
    width: 15px !important;
    height: 15px !important;
    margin-right: 8px !important;
    background-color: currentColor !important;
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'/%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'/%3E%3C/svg%3E") no-repeat center / contain !important;
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'/%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'/%3E%3C/svg%3E") no-repeat center / contain !important;
    flex-shrink: 0 !important;
}

.st-key-layer_switcher_radio div[data-testid="stRadioGroup"] label:nth-child(3) div[data-testid="stMarkdownContainer"] p::before,
div.st-key-layer_switcher_radio label[data-testid="stRadioOption"]:nth-child(3) div[data-testid="stMarkdownContainer"] p::before,
div[data-testid="stMainBlockContainer"] div.st-key-layer_switcher_radio label:nth-child(3) div[data-testid="stMarkdownContainer"] p::before,
div[data-testid="stMainBlockContainer"] div[data-testid="stRadio"] label[data-testid="stRadioOption"]:nth-child(3) div[data-testid="stMarkdownContainer"] p::before {
    content: "" !important;
    display: inline-block !important;
    width: 15px !important;
    height: 15px !important;
    margin-right: 8px !important;
    background-color: currentColor !important;
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 3z'/%3E%3C/svg%3E") no-repeat center / contain !important;
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 3z'/%3E%3C/svg%3E") no-repeat center / contain !important;
    flex-shrink: 0 !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"]:hover div[data-testid="stMarkdownContainer"] p {
    color: #FFFFFF !important;
}

/* Soft, Low-Opacity Active Nav Highlight */
div[data-testid="stRadio"] label[data-testid="stRadioOption"][data-selected="true"],
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input:checked) {
    background: rgba(99, 102, 241, 0.16) !important;
    border: 1px solid rgba(99, 102, 241, 0.35) !important;
    box-shadow: none !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"][data-selected="true"] div[data-testid="stMarkdownContainer"] p,
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input:checked) div[data-testid="stMarkdownContainer"] p {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.86rem !important;
    font-weight: 600 !important;
    color: #FFFFFF !important;
}

/* Sliders — Sophos Slate Styling */
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
    color: #94A3B8 !important;
    margin-bottom: 2px !important;
}

div[data-testid="stSlider"] [data-baseweb="slider"] {
    margin-top: 2px !important;
}

div[data-testid="stSlider"] [data-baseweb="slider"] > div:first-child {
    background: #252D40 !important;
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
    color: #94A3B8 !important;
}

/* ============================================================
   TOP COMMAND / BREADCRUMB BAR (Fluid Responsive Flexbox)
   ============================================================ */
.top-command-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #1C2333;
    border: 1px solid rgba(255, 255, 255, 0.09);
    border-radius: 12px;
    padding: 0.8rem 1.4rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.2);
    flex-wrap: wrap;
    gap: 10px;
}

@media (max-width: 768px) {
    .top-command-bar {
        padding: 0.7rem 0.9rem;
        margin-bottom: 0.8rem;
        flex-direction: column;
        align-items: flex-start;
        gap: 8px;
    }
}

.breadcrumb-trail {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.82rem;
    font-family: 'Inter', sans-serif;
    color: #94A3B8;
    font-weight: 500;
    flex-wrap: wrap;
}

.breadcrumb-active {
    color: #FFFFFF;
    font-weight: 600;
}

.telemetry-pill-group {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
}

.top-telemetry-pill {
    background: #252D40;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    padding: 5px 12px;
    font-family: 'Inter', sans-serif;
    font-size: 0.72rem;
    display: flex;
    align-items: center;
    gap: 6px;
    white-space: nowrap;
}

/* Exhibit Metadata Bar Responsive */
.exhibit-metadata-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #1C2333;
    border: 1px solid rgba(255, 255, 255, 0.09);
    border-radius: 10px;
    padding: 9px 18px;
    margin-bottom: 12px;
    font-family: 'Inter', sans-serif;
    font-size: 0.74rem;
    color: #94A3B8;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    flex-wrap: wrap;
    gap: 8px;
}

@media (max-width: 768px) {
    .exhibit-metadata-bar {
        padding: 8px 12px;
        flex-direction: column;
        align-items: flex-start;
        gap: 4px;
        font-size: 0.70rem;
    }
}

/* Action Buttons (Secondary) */
.stButton > button {
    background: #222B3D !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 10px !important;
    color: #F1F5F9 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.80rem !important;
    font-weight: 600 !important;
    padding: 0.6rem 0.8rem !important;
    width: 100% !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25) !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    text-align: center !important;
    white-space: normal !important;
    line-height: 1.3 !important;
}

.stButton > button:hover {
    border-color: rgba(124, 111, 240, 0.5) !important;
    background: #2B364C !important;
    color: #FFFFFF !important;
    box-shadow: 0 4px 14px rgba(124, 111, 240, 0.25) !important;
    transform: translateY(-1px) !important;
}

.stButton > button:active {
    transform: translateY(0px) !important;
    background: #181F2C !important;
}

/* Primary Active Navigation / Action Buttons */
.stButton > button[kind="primary"],
.stButton > button[data-testid="baseButton-primary"] {
    background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%) !important;
    border: 1px solid rgba(167, 139, 250, 0.4) !important;
    color: #FFFFFF !important;
    box-shadow: 0 4px 16px rgba(124, 58, 237, 0.35) !important;
    font-weight: 700 !important;
}

.stButton > button[kind="primary"]:hover,
.stButton > button[data-testid="baseButton-primary"]:hover {
    background: linear-gradient(135deg, #4338CA 0%, #6D28D9 100%) !important;
    border-color: rgba(167, 139, 250, 0.6) !important;
    box-shadow: 0 6px 20px rgba(124, 58, 237, 0.5) !important;
}

/* File Uploader Container */
div[data-testid="stFileUploader"] {
    background: #1C2333 !important;
    border: 1px dashed rgba(255, 255, 255, 0.16) !important;
    border-radius: 14px !important;
    padding: 1.2rem !important;
    margin-top: 0.4rem !important;
    transition: all 0.2s ease !important;
}

@media (max-width: 768px) {
    div[data-testid="stFileUploader"] {
        padding: 0.8rem !important;
    }
}

div[data-testid="stFileUploader"]:hover {
    border-color: rgba(255, 255, 255, 0.28) !important;
    background: #232B3E !important;
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

/* Tabs Styling (Streamlit 1.37+ & Legacy BaseWeb) */
div[data-testid="stTabs"] div[role="tablist"],
div[data-testid="stTabs"] [data-baseweb="tab-list"],
div[data-testid="stTabs"] div[data-orientation="horizontal"] {
    gap: 8px !important;
    background-color: transparent !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
    padding-bottom: 6px !important;
    margin-top: 0.6rem !important;
    margin-left: 0px !important;
    padding-left: 0px !important;
    transform: none !important;
}

div[data-testid="stTabs"] div[data-testid="stTab"],
div[data-testid="stTabs"] [data-baseweb="tab"] {
    background: transparent !important;
    border: none !important;
    border-radius: 8px !important;
    color: #94A3B8 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.84rem !important;
    font-weight: 500 !important;
    padding: 8px 16px !important;
    margin-left: 0px !important;
    white-space: nowrap !important;
    cursor: pointer !important;
    transform: none !important;
}

div[data-testid="stTabs"] div[data-testid="stTab"][aria-selected="true"],
div[data-testid="stTabs"] [data-baseweb="tab"][aria-selected="true"],
div[data-testid="stTabs"] div[data-testid="stTab"][data-selected="true"] {
    background: rgba(255, 255, 255, 0.10) !important;
    border: 1px solid rgba(255, 255, 255, 0.18) !important;
    color: #FFFFFF !important;
    font-weight: 600 !important;
}

div[data-testid="stTabs"] div[data-testid="stTab"] p {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.82rem !important;
    margin: 0 !important;
    padding: 0 !important;
    white-space: nowrap !important;
    overflow: visible !important;
    line-height: 1.2 !important;
}

@media (max-width: 768px) {
    div[data-testid="stTabs"] div[role="tablist"],
    div[data-testid="stTabs"] [data-baseweb="tab-list"],
    div[data-testid="stTabs"] div[data-orientation="horizontal"] {
        display: flex !important;
        width: 100% !important;
        gap: 6px !important;
        margin-left: 0px !important;
        padding-left: 0px !important;
        padding-right: 0px !important;
    }
    div[data-testid="stTabs"] div[data-testid="stTab"],
    div[data-testid="stTabs"] [data-baseweb="tab"] {
        flex: 1 1 50% !important;
        text-align: center !important;
        justify-content: center !important;
        margin-left: 0px !important;
        padding: 8px 8px !important;
        font-size: 0.78rem !important;
    }
}

/* 3-Exhibit Card Frames */
.exhibit-card-frame {
    background: #1C2333;
    border: 1px solid rgba(255, 255, 255, 0.09);
    border-radius: 14px;
    padding: 1.2rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    width: 100%;
}

@media (max-width: 768px) {
    .exhibit-card-frame {
        padding: 0.8rem;
        margin-bottom: 0.6rem;
    }
}

.exhibit-header-tag {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-bottom: 12px;
    padding-bottom: 10px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
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
    color: #94A3B8;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* Incident Cockpit Card */
.incident-cockpit-card {
    background: #1C2333;
    border: 1px solid rgba(255, 255, 255, 0.09);
    border-radius: 14px;
    padding: 1.6rem 1.8rem;
    margin-top: 1.4rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.22);
}

@media (max-width: 768px) {
    .incident-cockpit-card {
        padding: 1.1rem 1.1rem;
        margin-top: 1rem;
    }
}

/* Incident Telemetry 4-Metric Grid */
.incident-metrics-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    text-align: center;
    margin-bottom: 16px;
}

@media (max-width: 640px) {
    .incident-metrics-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 8px;
    }
}

/* ============================================================
   BENCHMARK KPI TILES (Fluid 4-Col to 2x2 Grid)
   ============================================================ */
.bench-kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 1.5rem;
    width: 100%;
}

@media (max-width: 1024px) {
    .bench-kpi-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
    }
}

@media (max-width: 480px) {
    .bench-kpi-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 8px;
    }
}

.bench-kpi-card {
    background: #1C2333;
    border: 1px solid rgba(255, 255, 255, 0.09);
    border-radius: 14px;
    padding: 18px 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    transition: all 0.2s ease;
}

@media (max-width: 480px) {
    .bench-kpi-card {
        padding: 14px 14px;
    }
}

.bench-kpi-card:hover {
    border-color: rgba(255, 255, 255, 0.18);
    transform: translateY(-2px);
}

.bench-kpi-icon-chip {
    width: 36px;
    height: 36px;
    border-radius: 10px;
    background: #252D40;
    border: 1px solid rgba(255, 255, 255, 0.08);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 14px;
}

@media (max-width: 480px) {
    .bench-kpi-icon-chip {
        width: 30px;
        height: 30px;
        margin-bottom: 8px;
    }
}

.bench-kpi-label {
    font-family: 'Inter', sans-serif;
    font-size: 0.68rem;
    font-weight: 600;
    color: #94A3B8;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
}

.bench-kpi-value {
    font-family: 'Inter', sans-serif;
    font-size: clamp(1.4rem, 3.5vw, 1.85rem);
    font-weight: 800;
    color: #FFFFFF;
    line-height: 1.1;
    margin-bottom: 6px;
}

.bench-kpi-sub {
    font-family: 'Inter', sans-serif;
    font-size: 0.72rem;
    font-weight: 500;
    color: #94A3B8;
}

/* Head to Head Model Cards - All Flat Hairline Borders */
.model-matrix-card {
    background: #1C2333;
    border: 1px solid rgba(255, 255, 255, 0.09);
    border-radius: 14px;
    padding: 1.6rem 1.6rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 380px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    margin-bottom: 1rem;
}

@media (max-width: 768px) {
    .model-matrix-card {
        min-height: auto;
        padding: 1.2rem 1.2rem;
    }
}

.model-matrix-card.recommended {
    border: 1px solid rgba(99, 102, 241, 0.4);
    box-shadow: 0 4px 20px rgba(99, 102, 241, 0.15);
}

.progress-track-dark {
    width: 100%;
    height: 7px;
    background: #252D40;
    border-radius: 4px;
    overflow: hidden;
}

.progress-fill-rounded {
    height: 100%;
    border-radius: 4px;
}

/* Alert & Notice Banners */
div[data-testid="stAlert"] {
    background: #1C2333 !important;
    border: 1px solid rgba(255, 255, 255, 0.09) !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.8rem !important;
    color: #E2E8F0 !important;
}

/* Sophos Hatched Progress Track & Glowing Capsule Fill */
.sophos-hatched-track {
    width: 100%;
    height: 9px;
    background-color: #252D40;
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
    background: linear-gradient(90deg, #475569 0%, #64748B 100%);
}

.sophos-thumb {
    width: 13px;
    height: 13px;
    border-radius: 50%;
    background: #252D40;
    border: 2px solid #FFFFFF;
    box-shadow: 0 0 6px rgba(0, 0, 0, 0.4);
    position: absolute;
    right: -3px;
    top: -2px;
}

/* ============================================================
   FUTURISTIC STANDBY FORENSIC CONSOLE (Responsive & Uncompressed)
   ============================================================ */
@keyframes radar-sweep {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

@keyframes bus-pulse {
    0% { transform: translateX(-100%); opacity: 0; }
    50% { opacity: 1; }
    100% { transform: translateX(250%); opacity: 0; }
}

@keyframes beacon-ping {
    0% { transform: scale(0.95); opacity: 0.8; }
    50% { transform: scale(1.08); opacity: 1; }
    100% { transform: scale(0.95); opacity: 0.8; }
}

/* Standby Hub Flex/Grid Container (2-Column Desktop, Responsive Mobile) */
.standby-hub-container {
    background: #1C2333;
    border: 1px solid rgba(255, 255, 255, 0.09);
    border-radius: 16px;
    padding: 1.6rem 1.8rem;
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    display: grid;
    grid-template-columns: 1.15fr 1fr;
    align-items: center;
    gap: 2rem;
    width: 100%;
    box-sizing: border-box;
}

.standby-radar-left {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    width: 100%;
}

.standby-radar-info {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    text-align: left;
    width: 100%;
}

.standby-telemetry-right {
    display: flex;
    flex-direction: column;
    gap: 14px;
    width: 100%;
}

.telemetry-bar-unit {
    display: flex;
    flex-direction: column;
    gap: 5px;
    width: 100%;
}

.telemetry-bar-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: 'Inter', sans-serif;
    font-size: 0.78rem;
    width: 100%;
    gap: 8px;
}

.telemetry-bar-label {
    color: #FFFFFF;
    font-weight: 600;
    white-space: nowrap;
}

.telemetry-bar-val {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    font-size: 0.76rem;
    white-space: nowrap;
    text-align: right;
}

@media (max-width: 768px) {
    .standby-hub-container {
        grid-template-columns: 1fr;
        padding: 1.2rem 1rem;
        gap: 1.2rem;
    }
    .standby-radar-left {
        flex-direction: column;
        align-items: center;
        text-align: center;
        gap: 1rem;
    }
    .standby-radar-info {
        align-items: center;
        text-align: center;
    }
    .telemetry-bar-header {
        font-size: 0.73rem;
    }
    .telemetry-bar-val {
        font-size: 0.71rem;
    }
}

.radar-chassis {
    position: relative;
    width: 190px;
    height: 190px;
    border-radius: 50%;
    background: radial-gradient(circle, #182030 0%, #121824 100%);
    border: 1px solid rgba(45, 212, 191, 0.3);
    box-shadow: 0 0 30px rgba(45, 212, 191, 0.12), inset 0 0 20px rgba(0,0,0,0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    flex-shrink: 0;
}

@media (max-width: 480px) {
    .radar-chassis {
        width: 160px;
        height: 160px;
    }
}

.radar-sweep-blade {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: conic-gradient(from 0deg at 50% 50%, rgba(45, 212, 191, 0) 0deg, rgba(45, 212, 191, 0) 270deg, rgba(45, 212, 191, 0.35) 360deg);
    animation: radar-sweep 4s linear infinite;
    pointer-events: none;
}

.radar-ring {
    position: absolute;
    border-radius: 50%;
    border: 1px solid rgba(45, 212, 191, 0.18);
    pointer-events: none;
}

/* ============================================================
   PIPELINE BUS FLOW (Desktop Horizontal -> Mobile Vertical)
   ============================================================ */
.pipeline-bus-grid {
    display: grid;
    grid-template-columns: 1fr auto 1fr auto 1fr auto 1fr;
    align-items: center;
    gap: 8px;
    width: 100%;
}

@media (max-width: 860px) {
    .pipeline-bus-grid {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    
    .pipeline-connector-line {
        display: none !important;
    }
}

.pipeline-node {
    background: #252D40;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 14px 18px;
    position: relative;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    width: 100%;
    box-sizing: border-box;
}

.pipeline-node:hover {
    border-color: rgba(99, 102, 241, 0.5);
    background: #2D374D;
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.3), 0 0 16px rgba(99, 102, 241, 0.15);
}

.pipeline-connector-line {
    height: 2px;
    width: 28px;
    background: linear-gradient(90deg, #6366F1, #2DD4BF);
    position: relative;
    overflow: hidden;
    flex-shrink: 0;
}

.pipeline-connector-line::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 40px;
    height: 100%;
    background: #FFFFFF;
    box-shadow: 0 0 8px #FFFFFF, 0 0 16px #2DD4BF;
    animation: bus-pulse 2.5s infinite;
}

/* ============================================================
   THREAT SCOPE MATRIX GRID (Responsive 3-Col -> 2-Col -> 1-Col)
   ============================================================ */
.threat-scope-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    width: 100%;
}

@media (max-width: 900px) {
    .threat-scope-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
    }
}

@media (max-width: 580px) {
    .threat-scope-grid {
        grid-template-columns: 1fr;
        gap: 10px;
    }
}

/* ============================================================
   SOPHOS 3D PILLAR COLUMNS & BENCHMARK BAR STYLES
   ============================================================ */
.sophos-pillar-container {
    background: #1C2333;
    border: 1px solid rgba(255, 255, 255, 0.09);
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    margin-top: 1.4rem;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    width: 100%;
}

@media (max-width: 768px) {
    .sophos-pillar-container {
        padding: 1rem 0.8rem;
    }
}

.sophos-chart-scroll-wrapper {
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    padding-bottom: 6px;
}

.sophos-pillar-chart-row {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    min-width: 680px;
    gap: 18px;
    height: 180px;
    padding: 0 14px 10px 14px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.sophos-pillar {
    width: 14px;
    border-radius: 4px 4px 2px 2px;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    display: inline-block;
}

.sophos-pillar.purple {
    background: linear-gradient(180deg, #818CF8 0%, #4338CA 100%);
    box-shadow: 0 0 10px rgba(99, 102, 241, 0.45);
}

.sophos-pillar.emerald {
    background: linear-gradient(180deg, #34D399 0%, #059669 100%);
    box-shadow: 0 0 10px rgba(16, 185, 129, 0.45);
}

.sophos-pillar.slate {
    background: linear-gradient(180deg, #94A3B8 0%, #334155 100%);
    box-shadow: 0 0 8px rgba(148, 163, 184, 0.25);
}

.sophos-pillar:hover {
    filter: brightness(1.25);
    transform: scaleY(1.05);
}

/* ============================================================
   DONUT & EFFICIENCY ROW (Responsive 2-Col Split)
   ============================================================ */
.benchmark-split-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 1.4rem;
}

@media (max-width: 860px) {
    .benchmark-split-row {
        grid-template-columns: 1fr;
        gap: 14px;
    }
}

.donut-card-inner {
    display: flex;
    align-items: center;
    justify-content: space-around;
    gap: 20px;
    padding: 0.4rem 0;
    flex-wrap: wrap;
}

@media (max-width: 480px) {
    .donut-card-inner {
        flex-direction: column;
        gap: 14px;
    }
}

</style>
"""
