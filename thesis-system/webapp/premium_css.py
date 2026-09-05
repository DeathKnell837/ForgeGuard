PREMIUM_CSS = """
<style>
/* 
====================================================================
  FORGEGUARD - ENTERPRISE FORENSIC DESIGN SYSTEM
  Dark Cybersecurity Aesthetic | Zero Emoji | Pixel Precision
====================================================================
*/

/* --- 1. Global Typography and Canvas --- */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    color: #E2E8F0;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

html, body {
    background-color: #121620;
    overflow-x: hidden;
}

.stApp {
    background-color: #121620;
    background-image: 
        radial-gradient(circle at 50% 0%, rgba(124, 111, 240, 0.08) 0%, transparent 60%),
        radial-gradient(circle at 100% 100%, rgba(45, 212, 191, 0.05) 0%, transparent 50%);
    background-attachment: fixed;
    background-size: cover;
}

/* --- 2. Streamlit Chrome Suppression and Header Clearance --- */
header[data-testid="stHeader"] {
    height: 0 !important;
    padding: 0 !important;
    background: transparent !important;
    pointer-events: none !important;
}

header[data-testid="stHeader"] > * {
    pointer-events: auto !important;
}

/* Eliminate Deploy button, Main Menu, Decoration bar, and Status widgets */
.stAppDeployButton,
div[data-testid="stAppDeployButton"],
[data-testid="stToolbarActions"],
[data-testid="stMainMenu"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
#MainMenu,
footer {
    display: none !important;
    visibility: hidden !important;
    height: 0px !important;
    width: 0px !important;
    opacity: 0 !important;
    pointer-events: none !important;
}

/* --- 3. Perfectly Centered Content Container --- */
.block-container {
    max-width: 1040px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    padding-top: 5.2rem !important;
    padding-bottom: 4rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}

@media (max-width: 768px) {
    .block-container {
        padding-top: 4.8rem !important;
        padding-bottom: 2.5rem !important;
        padding-left: 1.2rem !important;
        padding-right: 1.2rem !important;
        max-width: 100% !important;
    }
}

/* --- 4. Sidebar Rail and Collapse Button --- */
@media (min-width: 769px) {
    section[data-testid="stSidebar"] {
        background-color: #181D2A !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
        min-width: 280px !important;
        transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    section[data-testid="stSidebar"][aria-expanded="false"] {
        width: 0 !important;
        min-width: 0 !important;
        transform: translateX(-110%) !important;
        overflow: hidden !important;
    }
}

@media (max-width: 768px) {
    section[data-testid="stSidebar"] {
        position: fixed !important;
        z-index: 999999 !important;
        background-color: #181D2A !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
        max-width: 82% !important;
        width: 280px !important;
        box-shadow: 4px 0 24px rgba(0, 0, 0, 0.5) !important;
        transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    section[data-testid="stSidebar"][aria-expanded="false"] {
        display: none !important;
        left: -9999px !important;
        transform: translateX(-100%) !important;
    }
}

/* Sidebar Header and Collapse Button inside open sidebar */
section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
    padding-top: 10px !important;
    padding-left: 18px !important;
    padding-right: 18px !important;
}

section[data-testid="stSidebar"] .stSidebarHeader,
section[data-testid="stSidebar"] [data-testid="stSidebarHeader"] {
    height: 60px !important;
    min-height: 60px !important;
    background: transparent !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: flex-end !important;
    padding: 0 4px !important;
    margin: 0 0 12px 0 !important;
    box-sizing: border-box !important;
}

section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 40px !important;
    height: 40px !important;
    margin: 0 !important;
    padding: 0 !important;
}

/* Make the collapse button 100% visible, perfectly sized, and interactive */
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] button,
section[data-testid="stSidebar"] button[data-testid="stBaseButton-headerNoPadding"],
section[data-testid="stSidebar"] button[data-testid="baseButton-headerNoPadding"] {
    display: inline-flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    pointer-events: auto !important;
    width: 40px !important;
    height: 40px !important;
    min-width: 40px !important;
    min-height: 40px !important;
    background-color: #1C2333 !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 8px !important;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.4) !important;
    cursor: pointer !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 0 !important;
    margin: 0 !important;
    box-sizing: border-box !important;
    position: relative !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] button:hover,
section[data-testid="stSidebar"] button[data-testid="stBaseButton-headerNoPadding"]:hover,
section[data-testid="stSidebar"] button[data-testid="baseButton-headerNoPadding"]:hover {
    background-color: #252D40 !important;
    border-color: rgba(124, 111, 240, 0.6) !important;
    box-shadow: 0 0 12px rgba(124, 111, 240, 0.3) !important;
}

/* Hide ALL child nodes inside the button (spans, text, SVGs, Material Icons) */
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] button *,
section[data-testid="stSidebar"] button[data-testid="stBaseButton-headerNoPadding"] *,
section[data-testid="stSidebar"] button[data-testid="baseButton-headerNoPadding"] * {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    width: 0 !important;
    height: 0 !important;
    pointer-events: none !important;
}

/* Clean 3-line hamburger icon on the button itself */
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] button::after,
section[data-testid="stSidebar"] button[data-testid="stBaseButton-headerNoPadding"]::after,
section[data-testid="stSidebar"] button[data-testid="baseButton-headerNoPadding"]::after {
    content: '' !important;
    display: block !important;
    width: 20px !important;
    height: 20px !important;
    background-color: #CBD5E1 !important;
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='3' y1='6' x2='21' y2='6'%3E%3C/line%3E%3Cline x1='3' y1='12' x2='21' y2='12'%3E%3C/line%3E%3Cline x1='3' y1='18' x2='21' y2='18'%3E%3C/line%3E%3C/svg%3E") no-repeat center / contain !important;
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='3' y1='6' x2='21' y2='6'%3E%3C/line%3E%3Cline x1='3' y1='12' x2='21' y2='12'%3E%3C/line%3E%3Cline x1='3' y1='18' x2='21' y2='18'%3E%3C/line%3E%3C/svg%3E") no-repeat center / contain !important;
    transition: background-color 0.2s ease !important;
}

section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] button:hover::after,
section[data-testid="stSidebar"] button[data-testid="stBaseButton-headerNoPadding"]:hover::after,
section[data-testid="stSidebar"] button[data-testid="baseButton-headerNoPadding"]:hover::after {
    background-color: #FFFFFF !important;
}

/* --- 5. Floating Sidebar Expand Button (3 Lines Hamburger Icon) --- */
/* Comfortably positioned with breathing room at top: 22px, left: 24px */
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"],
button[data-testid="stExpandSidebarButton"],
button[data-testid="stSidebarCollapsedControl"],
div[data-testid="stSidebarCollapsedControl"] button,
header[data-testid="stHeader"] [data-testid="stSidebarCollapsedControl"],
header[data-testid="stHeader"] [data-testid="stExpandSidebarButton"] {
    display: inline-flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    pointer-events: auto !important;
    position: fixed !important;
    top: 20px !important;
    left: 20px !important;
    z-index: 999999 !important;
    background-color: #1C2333 !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 8px !important;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.4) !important;
    width: 40px !important;
    height: 40px !important;
    min-width: 40px !important;
    min-height: 40px !important;
    padding: 0px !important;
    margin: 0px !important;
    align-items: center !important;
    justify-content: center !important;
    box-sizing: border-box !important;
    cursor: pointer !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

[data-testid="stSidebarCollapsedControl"]:hover,
button[data-testid="stExpandSidebarButton"]:hover,
button[data-testid="stSidebarCollapsedControl"]:hover,
div[data-testid="stSidebarCollapsedControl"] button:hover {
    background-color: #252D40 !important;
    border-color: rgba(124, 111, 240, 0.6) !important;
    box-shadow: 0 0 12px rgba(124, 111, 240, 0.3) !important;
}

/* Hide native child icons inside hamburger button */
[data-testid="stSidebarCollapsedControl"] *,
button[data-testid="stExpandSidebarButton"] *,
button[data-testid="stSidebarCollapsedControl"] *,
div[data-testid="stSidebarCollapsedControl"] button * {
    display: none !important;
    visibility: hidden !important;
}

/* The 3 Lines SVG Vector via CSS Mask -- Perfectly Centered with 6px spacing */
[data-testid="stSidebarCollapsedControl"]::after,
button[data-testid="stExpandSidebarButton"]::after,
button[data-testid="stSidebarCollapsedControl"]::after,
div[data-testid="stSidebarCollapsedControl"] button::after {
    content: '' !important;
    display: block !important;
    width: 20px !important;
    height: 20px !important;
    background-color: #CBD5E1 !important;
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='3' y1='6' x2='21' y2='6'%3E%3C/line%3E%3Cline x1='3' y1='12' x2='21' y2='12'%3E%3C/line%3E%3Cline x1='3' y1='18' x2='21' y2='18'%3E%3C/line%3E%3C/svg%3E") no-repeat center / contain !important;
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='3' y1='6' x2='21' y2='6'%3E%3C/line%3E%3Cline x1='3' y1='12' x2='21' y2='12'%3E%3C/line%3E%3Cline x1='3' y1='18' x2='21' y2='18'%3E%3C/line%3E%3C/svg%3E") no-repeat center / contain !important;
    transition: background-color 0.2s ease !important;
}

[data-testid="stSidebarCollapsedControl"]:hover::after,
button[data-testid="stExpandSidebarButton"]:hover::after,
button[data-testid="stSidebarCollapsedControl"]:hover::after,
div[data-testid="stSidebarCollapsedControl"] button:hover::after {
    background-color: #FFFFFF !important;
}

/* --- 6. Sidebar Navigation Items with Clean SVG Vector Icons --- */
div[data-testid="stSidebarContent"] {
    padding: 1.2rem 1.2rem 1.5rem 1.2rem !important;
}

div[data-testid="stRadio"] > div[data-testid="stRadioGroup"] {
    display: flex !important;
    flex-direction: column !important;
    gap: 8px !important;
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    width: 100% !important;
}

div[data-testid="stRadio"] input[type="radio"],
div[data-testid="stRadio"] label div[class*="etak9234"],
div[data-testid="stRadio"] label div:has(> [data-testid="stMarkdownContainer"]) > div:first-child,
div[data-testid="stRadio"] [data-testid="stRadioDot"] {
    display: none !important;
    opacity: 0 !important;
    width: 0px !important;
    height: 0px !important;
    visibility: hidden !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"] {
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
    background: #1C2333 !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 8px !important;
    padding: 12px 14px !important;
    margin: 0 !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    cursor: pointer !important;
    width: 100% !important;
    box-sizing: border-box !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"]:hover {
    background: #252D40 !important;
    border-color: rgba(124, 111, 240, 0.4) !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"][aria-checked="true"],
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input:checked) {
    background: #222B3D !important;
    border-color: #7C6FF0 !important;
    box-shadow: 0 0 12px rgba(124, 111, 240, 0.25) !important;
}

/* Icon 1: Classify a Receipt (Receipt Document Scan Vector Icon) */
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:nth-of-type(1)::before {
    content: '' !important;
    display: inline-block !important;
    width: 18px !important;
    height: 18px !important;
    min-width: 18px !important;
    background-color: #94A3B8 !important;
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M4 2v20l2-1 2 1 2-1 2 1 2-1 2 1 2-1 2 1V2l-2 1-2-1-2 1-2-1-2 1-2-1-2 1Z'/%3E%3Cpath d='M16 8h-8'/%3E%3Cpath d='M16 12h-8'/%3E%3Cpath d='M12 16h-4'/%3E%3C/svg%3E") no-repeat center / contain !important;
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M4 2v20l2-1 2 1 2-1 2 1 2-1 2 1 2-1 2 1V2l-2 1-2-1-2 1-2-1-2 1-2-1-2 1Z'/%3E%3Cpath d='M16 8h-8'/%3E%3Cpath d='M16 12h-8'/%3E%3Cpath d='M12 16h-4'/%3E%3C/svg%3E") no-repeat center / contain !important;
    transition: background-color 0.2s ease !important;
}

/* Icon 2: Model Comparison (Analytics Bar Chart Vector Icon) */
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:nth-of-type(2)::before {
    content: '' !important;
    display: inline-block !important;
    width: 18px !important;
    height: 18px !important;
    min-width: 18px !important;
    background-color: #94A3B8 !important;
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='20' x2='18' y2='10'/%3E%3Cline x1='12' y1='20' x2='12' y2='4'/%3E%3Cline x1='6' y1='20' x2='6' y2='14'/%3E%3C/svg%3E") no-repeat center / contain !important;
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='20' x2='18' y2='10'/%3E%3Cline x1='12' y1='20' x2='12' y2='4'/%3E%3Cline x1='6' y1='20' x2='6' y2='14'/%3E%3C/svg%3E") no-repeat center / contain !important;
    transition: background-color 0.2s ease !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"]:hover::before {
    background-color: #FFFFFF !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"][aria-checked="true"]::before,
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input:checked)::before {
    background-color: #2DD4BF !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"] p {
    font-size: 13px !important;
    font-weight: 500 !important;
    color: #CBD5E1 !important;
    margin: 0 !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"][aria-checked="true"] p,
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input:checked) p {
    color: #FFFFFF !important;
    font-weight: 600 !important;
}

/* --- 7. File Uploader Styling --- */
div[data-testid="stFileUploader"] {
    background: #1C2333 !important;
    border: 1px dashed rgba(255, 255, 255, 0.15) !important;
    border-radius: 12px !important;
    padding: 1.5rem !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}

div[data-testid="stFileUploader"]:hover {
    border-color: rgba(124, 111, 240, 0.5) !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3) !important;
}

div[data-testid="stFileUploader"] section {
    background: transparent !important;
    padding: 0 !important;
}

div[data-testid="stFileUploader"] button {
    background-color: #252D40 !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    color: #E2E8F0 !important;
    border-radius: 6px !important;
    font-weight: 500 !important;
    font-size: 13px !important;
    transition: all 0.2s ease !important;
}

div[data-testid="stFileUploader"] button:hover {
    background-color: #7C6FF0 !important;
    border-color: #7C6FF0 !important;
    color: #FFFFFF !important;
}

/* --- 8. Model Result Cards (Elevated Interactive Widgets) --- */
.fg-result-card {
    background: linear-gradient(180deg, #20293D 0%, #182030 100%);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 12px;
    padding: 18px 22px;
    margin-bottom: 16px;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.06);
    transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.2s ease, border-color 0.2s ease;
    position: relative;
    overflow: hidden;
}

.fg-result-card:hover {
    transform: translateY(-3px);
    border-color: rgba(255, 255, 255, 0.2);
}

.fg-verdict-authentic {
    border-left: 4px solid #10B981 !important;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.35), 0 0 16px rgba(16, 185, 129, 0.08), inset 0 1px 0 rgba(255, 255, 255, 0.06);
}

.fg-verdict-authentic:hover {
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45), 0 0 22px rgba(16, 185, 129, 0.18), inset 0 1px 0 rgba(255, 255, 255, 0.08);
}

.fg-verdict-forged {
    border-left: 4px solid #EF4444 !important;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.35), 0 0 16px rgba(239, 68, 68, 0.08), inset 0 1px 0 rgba(255, 255, 255, 0.06);
}

.fg-verdict-forged:hover {
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45), 0 0 22px rgba(239, 68, 68, 0.18), inset 0 1px 0 rgba(255, 255, 255, 0.08);
}

.fg-model-name {
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    font-size: 16px;
    color: #FFFFFF;
    margin-bottom: 2px;
}

.fg-model-badge {
    display: inline-block;
    font-size: 11px;
    font-family: 'Inter', sans-serif;
    color: #94A3B8;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 4px;
    padding: 2px 8px;
    margin-top: 4px;
}

.fg-confidence {
    font-family: 'JetBrains Mono', monospace;
    font-size: 28px;
    font-weight: 700;
    line-height: 1.1;
}

.fg-latency {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #94A3B8;
    margin-top: 4px;
}

/* --- 9. Metrics Table & Graphical Performance Visualizer --- */
/* Graphical Visualizer Card */
.fg-chart-card {
    background: #1C2333;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 22px 24px;
    margin-bottom: 24px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
}

.fg-chart-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
}

@media (max-width: 768px) {
    .fg-chart-grid {
        grid-template-columns: 1fr;
        gap: 20px;
    }
}

.fg-chart-subpanel {
    background: rgba(18, 22, 32, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 10px;
    padding: 16px 18px;
}

.fg-chart-title {
    font-size: 13px;
    font-weight: 600;
    color: #E2E8F0;
    margin-bottom: 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.fg-bar-row {
    margin-bottom: 12px;
}

.fg-bar-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 5px;
    font-size: 12px;
}

.fg-bar-label {
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    color: #CBD5E1;
}

.fg-bar-val {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
}

.fg-bar-track {
    width: 100%;
    height: 7px;
    background: rgba(255, 255, 255, 0.06);
    border-radius: 4px;
    overflow: hidden;
}

.fg-bar-fill {
    height: 100%;
    border-radius: 4px;
}

.fg-chart-insight {
    font-size: 11px;
    color: #64748B;
    line-height: 1.5;
    margin-top: 14px;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
    padding-top: 10px;
}

/* Strategic Top-Metric Accents */
.fg-metric-top {
    display: inline-block;
    color: #2DD4BF !important;
    font-weight: 700 !important;
    background: rgba(45, 212, 191, 0.12) !important;
    border: 1px solid rgba(45, 212, 191, 0.28) !important;
    border-radius: 5px !important;
    padding: 2px 8px !important;
}

.fg-metric-fast {
    display: inline-block;
    color: #10B981 !important;
    font-weight: 700 !important;
    background: rgba(16, 185, 129, 0.12) !important;
    border: 1px solid rgba(16, 185, 129, 0.28) !important;
    border-radius: 5px !important;
    padding: 2px 8px !important;
}

/* Metrics Table */
.fg-metrics-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    border-radius: 10px;
    overflow: hidden;
    background-color: #1C2333;
    border: 1px solid rgba(255, 255, 255, 0.08);
    margin-bottom: 28px;
}

.fg-metrics-table thead tr {
    background-color: #22293A;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.fg-metrics-table th {
    padding: 12px 16px;
    font-family: 'Inter', sans-serif;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #94A3B8;
    text-align: left;
}

.fg-metrics-table tbody tr {
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    transition: background-color 0.15s ease;
}

.fg-metrics-table tbody tr:hover {
    background-color: rgba(124, 111, 240, 0.06);
}

.fg-metrics-table td {
    padding: 14px 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: #E2E8F0;
}

.fg-metrics-table td.arch-cell {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    color: #FFFFFF;
}

.fg-pending {
    font-style: italic;
    color: #64748B;
    font-size: 12px;
}

/* --- 10. Advisory Box --- */
.fg-advisory {
    margin-top: 20px;
    padding: 14px 18px;
    background-color: rgba(245, 158, 11, 0.08);
    border-left: 4px solid #F59E0B;
    border-radius: 0 8px 8px 0;
    color: #F8FAFC;
    font-size: 13px;
    line-height: 1.6;
}

/* --- 11. Scrollbar --- */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
::-webkit-scrollbar-track {
    background: #121620;
}
::-webkit-scrollbar-thumb {
    background: #252D40;
    border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover {
    background: #3B4763;
}
</style>
"""
