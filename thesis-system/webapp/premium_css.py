PREMIUM_CSS = """
<style>
/* 
====================================================================
  FORGEGUARD - PREMIUM DESIGN SYSTEM
  Dark Enterprise Cybersecurity Aesthetic
====================================================================
*/

/* 
====================================================================
  1. Global Canvas & Typography
====================================================================
*/
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
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

/* 
====================================================================
  2. Header — Zero Top Whitespace
====================================================================
*/
header[data-testid='stHeader'] {
    height: 0 !important;
    padding: 0 !important;
    background: transparent !important;
    pointer-events: none !important;
}

header[data-testid='stHeader'] > * {
    pointer-events: auto !important;
}

/* 
====================================================================
  3. Block Container Padding
====================================================================
*/
.block-container {
    padding-top: 0.8rem !important;
    padding-bottom: 3.5rem !important;
    padding-left: 1.8rem !important;
    padding-right: 1.8rem !important;
    max-width: 98% !important;
}

@media (max-width: 768px) {
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
}

/* 
====================================================================
  4. Sidebar Rail
====================================================================
*/
/* Desktop Sidebar */
@media (min-width: 769px) {
    section[data-testid='stSidebar'] {
        background-color: #181D2A !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
        min-width: 280px !important;
        transition: transform 0.3s ease-in-out, width 0.3s ease-in-out;
    }
    
    section[data-testid='stSidebar'][aria-expanded='false'] {
        width: 0 !important;
        min-width: 0 !important;
        transform: translateX(-110%) !important;
        overflow: hidden !important;
    }
    
    section[data-testid='stSidebar'] .stSidebarHeader {
        height: 48px !important;
        background: transparent !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
        display: flex;
        align-items: center;
        padding: 0 1rem;
    }

    button[data-testid='baseButton-headerNoPadding'] {
        background-color: #252D40 !important;
        width: 32px !important;
        height: 32px !important;
        border-radius: 50% !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: background-color 0.2s;
    }

    button[data-testid='baseButton-headerNoPadding']:hover {
        background-color: #2E384D !important;
    }
}

/* Mobile Sidebar */
@media (max-width: 768px) {
    section[data-testid='stSidebar'] {
        position: fixed !important;
        z-index: 999999 !important;
        background-color: #181D2A !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
        max-width: 82% !important;
        width: 280px !important;
        box-shadow: 4px 0 24px rgba(0, 0, 0, 0.5) !important;
        transition: transform 0.3s ease-in-out;
    }
    
    section[data-testid='stSidebar'][aria-expanded='false'] {
        display: none !important;
        left: -9999px !important;
        transform: translateX(-100%) !important;
    }
}

/* 
====================================================================
  5. Sidebar Expand Button
====================================================================
*/
[data-testid='stSidebarCollapsedControl'],
[data-testid='stSidebarCollapsedControl'] * {
    transition: all 0.2s ease;
}

[data-testid='stSidebarCollapsedControl'] {
    position: fixed !important;
    top: 14px !important;
    left: 14px !important;
    z-index: 999999 !important;
    background-color: #1C2333 !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 8px !important;
    width: 36px !important;
    height: 36px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.35) !important;
    cursor: pointer !important;
}

[data-testid='stSidebarCollapsedControl']:hover {
    background-color: #252D40 !important;
}

[data-testid='stSidebarCollapsedControl'] > * {
    display: none !important;
    visibility: hidden !important;
}

[data-testid='stSidebarCollapsedControl']::after {
    content: '';
    display: block;
    width: 20px;
    height: 20px;
    background-color: #94A3B8;
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M3 6h18M3 12h18M3 18h18' stroke='currentColor' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") no-repeat center / contain;
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M3 6h18M3 12h18M3 18h18' stroke='currentColor' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") no-repeat center / contain;
}

[data-testid='stSidebarCollapsedControl']:hover::after {
    background-color: #FFFFFF;
}

/* 
====================================================================
  6. Hide Streamlit Chrome
====================================================================
*/
[data-testid='stToolbarActions'],
[data-testid='stMainMenu'],
[data-testid='stDecoration'],
[data-testid='stStatusWidget'] {
    display: none !important;
}

/* 
====================================================================
  7. Sidebar Content Styling
====================================================================
*/
/* Sidebar Radio Navigation */
section[data-testid='stSidebar'] .stRadio > div {
    gap: 0.5rem;
}

section[data-testid='stSidebar'] .stRadio label {
    background: transparent;
    padding: 10px 14px;
    border-radius: 6px;
    width: 100%;
    display: flex;
    align-items: center;
    border-left: 3px solid transparent;
    transition: all 0.2s ease;
    cursor: pointer;
    font-weight: 500;
}

section[data-testid='stSidebar'] .stRadio label:hover {
    background: rgba(255, 255, 255, 0.04);
}

section[data-testid='stSidebar'] .stRadio label[data-checked='true'] {
    background: rgba(45, 212, 191, 0.1);
    border-left: 3px solid #2DD4BF;
    color: #E2E8F0;
}

/* Hide the actual radio circle */
section[data-testid='stSidebar'] .stRadio label > div:first-child {
    display: none !important;
}

section[data-testid='stSidebar'] h1, 
section[data-testid='stSidebar'] h2, 
section[data-testid='stSidebar'] h3 {
    font-size: 0.75rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
    color: #94A3B8 !important;
    font-weight: 600 !important;
    margin-top: 1.5rem !important;
    margin-bottom: 0.5rem !important;
}

section[data-testid='stSidebar'] hr {
    border-color: rgba(255, 255, 255, 0.08) !important;
    margin: 1rem 0 !important;
}

/* 
====================================================================
  8. File Uploader Styling
====================================================================
*/
.stFileUploader > div {
    background-color: #1C2333 !important;
    border: 1px dashed rgba(255, 255, 255, 0.12) !important;
    border-radius: 12px !important;
    padding: 2rem !important;
    transition: all 0.3s ease;
}

.stFileUploader > div:hover {
    border-color: #2DD4BF !important;
    box-shadow: 0 0 15px rgba(45, 212, 191, 0.1) !important;
}

.stFileUploader section > button {
    background: linear-gradient(135deg, #2DD4BF 0%, #7C6FF0 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    font-weight: 600 !important;
    border-radius: 6px !important;
    padding: 0.5rem 1.5rem !important;
}

/* 
====================================================================
  9. Result Cards
====================================================================
*/
.fg-result-card {
    background-color: #1C2333;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 20px;
    margin-bottom: 16px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}

.fg-verdict-authentic {
    border-left: 3px solid #10B981;
}

.fg-verdict-forged {
    border-left: 3px solid #EF4444;
}

.fg-model-name {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 1.1rem;
    color: #E2E8F0;
    margin-bottom: 8px;
}

.fg-confidence {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.5rem;
    font-weight: 700;
    color: #E2E8F0;
}

.fg-latency {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    color: #94A3B8;
    margin-top: 4px;
}

/* 
====================================================================
  10. Metrics Table
====================================================================
*/
.fg-metrics-table-wrapper {
    overflow-x: auto;
    width: 100%;
}

.fg-metrics-table {
    width: 100%;
    border-collapse: collapse;
    background-color: #1C2333;
    border-radius: 8px;
    overflow: hidden;
    font-size: 0.9rem;
}

.fg-metrics-table th {
    background-color: #252D40;
    color: #CBD5E1;
    text-transform: uppercase;
    font-size: 0.75rem;
    letter-spacing: 0.05em;
    padding: 12px 16px;
    text-align: left;
    font-weight: 600;
}

.fg-metrics-table td {
    padding: 12px 16px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    font-family: 'JetBrains Mono', monospace;
    color: #E2E8F0;
}

.fg-metrics-table tr:hover td {
    background-color: rgba(255, 255, 255, 0.02);
}

.fg-metrics-table tr:last-child td {
    border-bottom: none;
}

.fg-pending {
    font-family: 'Inter', sans-serif !important;
    font-style: italic;
    color: #94A3B8 !important;
}

/* 
====================================================================
  11. Confusion Matrix
====================================================================
*/
.fg-cm-container {
    background-color: #1C2333;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 20px;
    display: inline-block;
}

.fg-cm-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
}

.fg-cm-cell {
    padding: 16px;
    border-radius: 8px;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

.fg-cm-tn, .fg-cm-tp {
    background-color: rgba(16, 185, 129, 0.12);
}

.fg-cm-fp, .fg-cm-fn {
    background-color: rgba(239, 68, 68, 0.12);
}

.fg-cm-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.75rem;
    font-weight: 700;
    color: #E2E8F0;
    line-height: 1.2;
}

.fg-cm-label {
    font-family: 'Inter', sans-serif;
    font-size: 0.75rem;
    color: #CBD5E1;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: 4px;
}

/* 
====================================================================
  12. Advisory Note
====================================================================
*/
.fg-advisory {
    background-color: rgba(245, 158, 11, 0.08);
    border-left: 3px solid #F59E0B;
    padding: 12px 16px;
    border-radius: 0 6px 6px 0;
    color: #CBD5E1;
    font-style: italic;
    font-size: 0.9rem;
    margin: 16px 0;
}

/* 
====================================================================
  13. Streamlit Widget Overrides & Global Scrollbar
====================================================================
*/
/* Scrollbar styling */
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
    background: #334155;
}

/* Inputs and Selects */
.stSelectbox > div > div {
    background-color: #1C2333 !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    color: #E2E8F0 !important;
}

.stTextInput > div > div > input {
    background-color: #1C2333 !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    color: #E2E8F0 !important;
}

/* Metric Cards */
[data-testid='stMetric'] {
    background-color: #1C2333;
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid rgba(255, 255, 255, 0.08);
}

[data-testid='stMetricValue'] {
    font-family: 'JetBrains Mono', monospace !important;
}

/* 
====================================================================
  14. Footer Area
====================================================================
*/
.fg-footer {
    text-align: center;
    color: #94A3B8;
    font-size: 0.8rem;
    margin-top: 4rem;
    padding-top: 2rem;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    padding-bottom: 2rem;
}

/*
====================================================================
  15. Streamlit Chrome Hiding
====================================================================
*/
[data-testid="stToolbar"],
header[data-testid="stHeader"] [data-testid="stToolbar"] {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    height: 0px !important;
    width: 100% !important;
    pointer-events: none !important;
    background: transparent !important;
}

[data-testid="stToolbar"] * {
    visibility: visible !important;
}

[data-testid="stToolbarActions"],
[data-testid="stMainMenu"],
[data-testid="stMainMenu"] *,
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    height: 0px !important;
    width: 0px !important;
    pointer-events: none !important;
}

/*
====================================================================
  16. Sidebar Rail (Desktop & Mobile)
====================================================================
*/
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

    section[data-testid="stSidebar"][aria-expanded="false"],
    section[data-testid="stSidebar"]:not([aria-expanded="true"]) {
        min-width: 0px !important;
        width: 0px !important;
        max-width: 0px !important;
        height: 0px !important;
        transform: translateX(-110%) !important;
        visibility: hidden !important;
        display: none !important;
        pointer-events: none !important;
    }

    section[data-testid="stSidebar"][aria-expanded="true"] [data-testid="stSidebarHeader"],
    section[data-testid="stSidebar"][aria-expanded="true"] [data-testid="stSidebarCollapseButton"],
    section[data-testid="stSidebar"][aria-expanded="true"] [data-testid="stSidebarHeader"] button,
    section[data-testid="stSidebar"][aria-expanded="true"] button[kind="header"],
    section[data-testid="stSidebar"][aria-expanded="true"] [data-testid="stBaseButton-headerNoPadding"] {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        pointer-events: auto !important;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarHeader"] {
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
    section[data-testid="stSidebar"] [data-testid="stBaseButton-headerNoPadding"] {
        background: #252D40 !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 8px !important;
        color: #CBD5E1 !important;
        width: 32px !important;
        height: 32px !important;
        min-width: 32px !important;
        min-height: 32px !important;
        padding: 0px !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.25) !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"]:hover,
    section[data-testid="stSidebar"] [data-testid="stSidebarHeader"] button:hover {
        background: #2E384D !important;
        color: #FFFFFF !important;
        border-color: rgba(129, 140, 248, 0.5) !important;
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
    section[data-testid="stSidebar"] button[kind="header"],
    section[data-testid="stSidebar"] [data-testid="stBaseButton-headerNoPadding"] {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        pointer-events: auto !important;
        color: #FFFFFF !important;
        background: #252D40 !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 8px !important;
        margin: 8px !important;
        width: 32px !important;
        height: 32px !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* Responsive column stacking */
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

/*
====================================================================
  17. Hamburger Menu Button (CRITICAL — Fixed Position)
====================================================================
*/
/* Hide ALL children inside sidebar controls */
[data-testid="stSidebarCollapsedControl"] *,
button[data-testid="stExpandSidebarButton"] *,
button[data-testid="stSidebarCollapsedControl"] *,
div[data-testid="stSidebarCollapsedControl"] button *,
header[data-testid="stHeader"] [data-testid="stSidebarCollapsedControl"] *,
header[data-testid="stHeader"] [data-testid="stExpandSidebarButton"] *,
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] *,
section[data-testid="stSidebar"] [data-testid="stSidebarHeader"] button *,
section[data-testid="stSidebar"] button[kind="header"] *,
section[data-testid="stSidebar"] [data-testid="stBaseButton-headerNoPadding"] * {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    font-size: 0px !important;
    width: 0px !important;
    height: 0px !important;
    line-height: 0 !important;
    pointer-events: none !important;
}

/* Floating expand sidebar button (when sidebar is collapsed) */
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
    top: 14px !important;
    left: 14px !important;
    z-index: 999999 !important;
    background: #1C2333 !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 8px !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.35) !important;
    width: 36px !important;
    height: 36px !important;
    min-width: 36px !important;
    min-height: 36px !important;
    padding: 0px !important;
    margin: 0px !important;
    align-items: center !important;
    justify-content: center !important;
    box-sizing: border-box !important;
    cursor: pointer !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

/* 3-Line hamburger SVG icon via CSS mask */
[data-testid="stSidebarCollapsedControl"]::after,
button[data-testid="stExpandSidebarButton"]::after,
button[data-testid="stSidebarCollapsedControl"]::after,
div[data-testid="stSidebarCollapsedControl"] button::after,
header[data-testid="stHeader"] [data-testid="stSidebarCollapsedControl"]::after,
header[data-testid="stHeader"] [data-testid="stExpandSidebarButton"]::after,
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"]::after,
section[data-testid="stSidebar"] [data-testid="stSidebarHeader"] button::after,
section[data-testid="stSidebar"] button[kind="header"]::after,
section[data-testid="stSidebar"] [data-testid="stBaseButton-headerNoPadding"]::after {
    content: "" !important;
    display: block !important;
    width: 18px !important;
    height: 18px !important;
    background-color: #CBD5E1 !important;
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='3' y1='12' x2='21' y2='12'%3E%3C/line%3E%3Cline x1='3' y1='6' x2='21' y2='6'%3E%3C/line%3E%3Cline x1='3' y1='18' x2='21' y2='18'%3E%3C/line%3E%3C/svg%3E") no-repeat center / contain !important;
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='3' y1='12' x2='21' y2='12'%3E%3C/line%3E%3Cline x1='3' y1='6' x2='21' y2='6'%3E%3C/line%3E%3Cline x1='3' y1='18' x2='21' y2='18'%3E%3C/line%3E%3C/svg%3E") no-repeat center / contain !important;
    transition: background-color 0.2s ease !important;
}

[data-testid="stSidebarCollapsedControl"]:hover,
button[data-testid="stExpandSidebarButton"]:hover,
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"]:hover,
section[data-testid="stSidebar"] [data-testid="stSidebarHeader"] button:hover {
    background: #252D40 !important;
    border-color: rgba(129, 140, 248, 0.6) !important;
    box-shadow: 0 0 12px rgba(129, 140, 248, 0.3) !important;
}

[data-testid="stSidebarCollapsedControl"]:hover::after,
button[data-testid="stExpandSidebarButton"]:hover::after,
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"]:hover::after,
section[data-testid="stSidebar"] [data-testid="stSidebarHeader"] button:hover::after {
    background-color: #FFFFFF !important;
}

/*
====================================================================
  18. Sidebar Radio Nav Items
====================================================================
*/
div[data-testid="stSidebarContent"] {
    padding: 0.8rem 1.1rem 1.2rem 1.1rem !important;
    padding-top: 0.8rem !important;
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

/* Hide native radio dots */
div[data-testid="stRadio"] input[type="radio"],
div[data-testid="stRadio"] [data-testid="stRadioDot"] {
    display: none !important;
    opacity: 0 !important;
    width: 0px !important;
    height: 0px !important;
}

/* Nav item capsule */
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

div[data-testid="stRadio"] label[data-testid="stRadioOption"] div[data-testid="stMarkdownContainer"] p {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.86rem !important;
    font-weight: 500 !important;
    color: #CBD5E1 !important;
    margin: 0 !important;
    line-height: 1.4 !important;
    transition: color 0.15s ease !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"]:hover {
    background: rgba(255, 255, 255, 0.05) !important;
    border-color: rgba(255, 255, 255, 0.08) !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"]:hover div[data-testid="stMarkdownContainer"] p {
    color: #FFFFFF !important;
}

/* Active nav highlight */
div[data-testid="stRadio"] label[data-testid="stRadioOption"][data-selected="true"],
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input:checked) {
    background: rgba(99, 102, 241, 0.16) !important;
    border: 1px solid rgba(99, 102, 241, 0.35) !important;
}

div[data-testid="stRadio"] label[data-testid="stRadioOption"][data-selected="true"] div[data-testid="stMarkdownContainer"] p,
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input:checked) div[data-testid="stMarkdownContainer"] p {
    font-weight: 600 !important;
    color: #FFFFFF !important;
}

/* Nav item 1 icon: Shield */
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

/* Nav item 2 icon: Bar Chart */
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

/* Hide radio dot wrapper divs */
div[data-testid="stRadio"] label[data-testid="stRadioOption"] div:has(> div:empty):not(:has(p)),
div[data-testid="stRadio"] label[data-testid="stRadioOption"] > div > div > div:first-child:not(:has(p)):not([data-testid="stMarkdownContainer"]),
div[data-testid="stRadio"] label[data-testid="stRadioOption"] [data-baseweb="radio"] > div:first-child {
    display: none !important;
    width: 0px !important;
    height: 0px !important;
}

</style>
"""
