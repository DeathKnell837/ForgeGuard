PREMIUM_CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
/* ForgeGuard visual system — Crisp Fintech Light Workspace. Presentation only. */

:root {
    --fg-bg: #F5F7FB;
    --fg-surface: #FFFFFF;
    --fg-surface-muted: #F8FAFC;
    --fg-surface-subtle: #EEF2F6;
    --fg-border: #E2E8F0;
    --fg-border-strong: #CBD5E1;

    --fg-ink: #0F172A;
    --fg-ink-2: #334155;
    --fg-muted: #475569;
    --fg-subtle: #64748B;

    --fg-accent: #1D4ED8;
    --fg-accent-hover: #1E40AF;
    --fg-accent-soft: #EFF6FF;
    --fg-accent-border: #BFDBFE;

    --fg-authentic: #047857;
    --fg-authentic-bg: #ECFDF5;
    --fg-authentic-border: #A7F3D0;

    --fg-forged: #BE123C;
    --fg-forged-bg: #FFF1F2;
    --fg-forged-border: #FECDD3;

    --fg-warning: #B45309;
    --fg-warning-bg: #FFFBEB;
    --fg-warning-border: #FDE68A;

    --fg-info: #0E7490;
    --fg-info-bg: #ECFEFF;
    --fg-info-border: #A5F3FC;

    --fg-sans: "Plus Jakarta Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    --fg-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;

    --fg-shadow-xs: 0 1px 2px rgba(15, 23, 42, 0.04);
    --fg-shadow-sm: 0 2px 8px rgba(15, 23, 42, 0.05), 0 1px 2px rgba(15, 23, 42, 0.03);
    --fg-shadow-md: 0 8px 24px rgba(15, 23, 42, 0.07), 0 2px 6px rgba(15, 23, 42, 0.03);

    --fg-r-sm: 8px;
    --fg-r-md: 12px;
    --fg-r-lg: 16px;
    --fg-r-pill: 999px;
}

html, body, [class*="css"] {
    font-family: var(--fg-sans);
    color: var(--fg-ink);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-rendering: optimizeLegibility;
}

html, body, .stApp, [data-testid="stAppViewContainer"] {
    background-color: var(--fg-bg) !important;
    color: var(--fg-ink) !important;
    overflow-x: clip !important;
    max-width: 100vw !important;
}
[data-testid="stMain"] {
    background-color: var(--fg-bg) !important;
    color: var(--fg-ink) !important;
    width: 100% !important;
    max-width: 100vw !important;
    overflow-x: clip !important;
    overflow-y: auto !important;
}

.stApp {
    background-color: var(--fg-bg) !important;
    background-image: radial-gradient(ellipse 80% 40% at 50% -10%, rgba(29, 78, 216, 0.055), transparent) !important;
}

/* Hide Streamlit top chrome & unused sidebar */
header[data-testid="stHeader"] {
    height: 0 !important;
    min-height: 0 !important;
    padding: 0 !important;
    background: transparent !important;
    pointer-events: none !important;
}
header[data-testid="stHeader"] > * { pointer-events: auto !important; }

.stAppDeployButton,
div[data-testid="stAppDeployButton"],
[data-testid="stToolbarActions"],
[data-testid="stMainMenu"],
[data-testid="stDecoration"],
#MainMenu,
footer,
section[data-testid="stSidebar"],
[data-testid="stSidebarCollapsedControl"],
button[data-testid="stExpandSidebarButton"],
button[data-testid="stSidebarCollapsedControl"],
div[data-testid="stSidebarCollapsedControl"] button,
[data-testid="collapsedControl"] {
    display: none !important;
    visibility: hidden !important;
}

/* Execution status indicator */
div[data-testid="stStatusWidget"] {
    display: inline-flex !important;
    visibility: visible !important;
    position: fixed !important;
    top: 14px !important;
    right: 18px !important;
    z-index: 999999 !important;
    background: rgba(255, 255, 255, 0.96) !important;
    border: 1px solid var(--fg-border) !important;
    border-radius: var(--fg-r-pill) !important;
    padding: 5px 14px !important;
    box-shadow: var(--fg-shadow-sm) !important;
    backdrop-filter: blur(8px) !important;
}
div[data-testid="stStatusWidget"] svg {
    fill: var(--fg-accent) !important;
    color: var(--fg-accent) !important;
}
div[data-testid="stStatusWidget"] * {
    color: var(--fg-ink-2) !important;
    font-family: var(--fg-mono) !important;
    font-size: 11px !important;
}

/* Main Layout Container */
.block-container {
    max-width: 1160px !important;
    padding: 1.05rem 2rem 1.5rem !important;
    margin: 0 auto !important;
    overflow: visible !important;
    overflow-x: visible !important;
    overflow-y: visible !important;
}
.block-container img,
.block-container canvas,
.block-container svg {
    max-width: 100%;
}
div[data-testid="stElementContainer"],
div[data-testid="stMarkdownContainer"] {
    max-width: 100% !important;
}

/* Top Brand Header */
.fg-topbar {
    padding: 2px 0 12px 0;
    margin-bottom: 10px;
    border-bottom: 1px solid var(--fg-border);
}
.fg-topbar-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    flex-wrap: wrap;
}
.fg-brand-wrap {
    display: inline-flex;
    align-items: center;
    gap: 11px;
}
.fg-brand-mark {
    width: 34px;
    height: 34px;
    border-radius: 9px;
    background: var(--fg-accent-soft);
    border: 1px solid var(--fg-accent-border);
    color: var(--fg-accent);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex: 0 0 34px;
    box-shadow: var(--fg-shadow-xs);
}
.fg-brand-mark svg {
    width: 18px;
    height: 18px;
}
.fg-brand-title {
    font-family: var(--fg-sans);
    font-size: 24px;
    font-weight: 800;
    color: var(--fg-ink);
    letter-spacing: -0.03em;
    line-height: 1.1;
}
.fg-topbar-badge {
    font-family: var(--fg-mono);
    font-size: 11px;
    font-weight: 600;
    color: var(--fg-accent);
    background: var(--fg-accent-soft);
    border: 1px solid var(--fg-accent-border);
    border-radius: var(--fg-r-pill);
    padding: 4px 12px;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    white-space: nowrap;
}
.fg-topbar-subtitle {
    margin-top: 8px;
    font-size: 13.5px;
    font-weight: 500;
    color: var(--fg-muted);
    line-height: 1.5;
    max-width: 78ch;
}

/* Segmented Top Navigation Switcher (st.radio horizontal) */
div[data-testid="stRadio"] {
    margin: 0 0 14px 0 !important;
}
div[data-testid="stRadio"] > div[data-testid="stRadioGroup"],
div[data-testid="stRadio"] div[role="radiogroup"] {
    display: inline-flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    align-items: center !important;
    gap: 4px !important;
    padding: 4px !important;
    background: var(--fg-surface-subtle) !important;
    border: 1px solid var(--fg-border) !important;
    border-radius: 11px !important;
    box-shadow: inset 0 1px 2px rgba(15, 23, 42, 0.03) !important;
}
div[data-testid="stRadio"] input[type="radio"] {
    position: absolute !important;
    opacity: 0 !important;
    width: 1px !important;
    height: 1px !important;
    pointer-events: none !important;
}
div[data-testid="stRadio"] [data-testid="stRadioDot"],
div[data-testid="stRadio"] label > div:first-child:not([data-testid="stMarkdownContainer"]),
div[data-testid="stRadio"] label div:has(> [data-testid="stMarkdownContainer"]) > div:first-child {
    display: none !important;
    width: 0 !important;
    height: 0 !important;
    min-width: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
}
div[data-testid="stRadio"] label[data-testid="stRadioOption"],
div[data-testid="stRadio"] label[data-baseweb="radio"] {
    min-height: 40px !important;
    box-sizing: border-box !important;
    margin: 0 !important;
    padding: 8px 18px !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
    border: 1px solid transparent !important;
    border-radius: 8px !important;
    background: transparent !important;
    color: var(--fg-muted) !important;
    cursor: pointer !important;
    transition: background 180ms ease, color 180ms ease, border-color 180ms ease, box-shadow 180ms ease !important;
}
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:hover,
div[data-testid="stRadio"] label[data-baseweb="radio"]:hover {
    background: rgba(255, 255, 255, 0.65) !important;
    color: var(--fg-ink) !important;
}
div[data-testid="stRadio"] label[data-testid="stRadioOption"][aria-checked="true"],
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input:checked),
div[data-testid="stRadio"] label[data-baseweb="radio"][aria-checked="true"],
div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) {
    background: var(--fg-surface) !important;
    border-color: var(--fg-border) !important;
    color: var(--fg-accent) !important;
    box-shadow: var(--fg-shadow-xs) !important;
}
div[data-testid="stRadio"] label[data-testid="stRadioOption"] [data-testid="stMarkdownContainer"] p,
div[data-testid="stRadio"] label[data-baseweb="radio"] p {
    margin: 0 !important;
    font-family: var(--fg-sans) !important;
    font-size: 13.5px !important;
    font-weight: 600 !important;
    color: var(--fg-muted) !important;
    white-space: nowrap !important;
    line-height: 1.25 !important;
}
div[data-testid="stRadio"] label[data-testid="stRadioOption"][aria-checked="true"] p,
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input:checked) p,
div[data-testid="stRadio"] label[data-baseweb="radio"][aria-checked="true"] p,
div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) p {
    color: var(--fg-accent) !important;
    font-weight: 700 !important;
}
div[data-testid="stRadio"] label[data-testid="stRadioOption"]::before,
div[data-testid="stRadio"] label[data-baseweb="radio"]::before {
    content: "";
    width: 15px;
    height: 15px;
    flex: 0 0 15px;
    display: inline-block;
    background-color: var(--fg-subtle);
    -webkit-mask-repeat: no-repeat;
    -webkit-mask-position: center;
    -webkit-mask-size: contain;
    mask-repeat: no-repeat;
    mask-position: center;
    mask-size: contain;
    transition: background-color 180ms ease;
}
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:nth-of-type(1)::before,
div[data-testid="stRadio"] label[data-baseweb="radio"]:nth-of-type(1)::before,
div[data-testid="stRadio"] [data-testid="stRadioGroup"] > :nth-child(1) label::before,
div[data-testid="stRadio"] div[role="radiogroup"] > :nth-child(1) label::before {
    -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M4 3h16v18l-3-2-2.5 2L12 19l-2.5 2L7 19l-3 2V3z'/%3E%3Cpath d='M8 8h8'/%3E%3Cpath d='M8 12h8'/%3E%3Cpath d='M8 16h5'/%3E%3C/svg%3E");
    mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M4 3h16v18l-3-2-2.5 2L12 19l-2.5 2L7 19l-3 2V3z'/%3E%3Cpath d='M8 8h8'/%3E%3Cpath d='M8 12h8'/%3E%3Cpath d='M8 16h5'/%3E%3C/svg%3E");
}
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:nth-of-type(2)::before,
div[data-testid="stRadio"] label[data-baseweb="radio"]:nth-of-type(2)::before,
div[data-testid="stRadio"] [data-testid="stRadioGroup"] > :nth-child(2) label::before,
div[data-testid="stRadio"] div[role="radiogroup"] > :nth-child(2) label::before {
    -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M3 3v18h18'/%3E%3Crect x='7' y='10' width='3' height='7' rx='1'/%3E%3Crect x='12' y='6' width='3' height='11' rx='1'/%3E%3Crect x='17' y='13' width='3' height='4' rx='1'/%3E%3C/svg%3E");
    mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M3 3v18h18'/%3E%3Crect x='7' y='10' width='3' height='7' rx='1'/%3E%3Crect x='12' y='6' width='3' height='11' rx='1'/%3E%3Crect x='17' y='13' width='3' height='4' rx='1'/%3E%3C/svg%3E");
}
div[data-testid="stRadio"] label[data-testid="stRadioOption"][aria-checked="true"]::before,
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input:checked)::before,
div[data-testid="stRadio"] label[data-baseweb="radio"][aria-checked="true"]::before,
div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked)::before {
    background-color: var(--fg-accent) !important;
}

/* File Uploader Card (Sightengine-inspired clean dropzone) */
div[data-testid="stFileUploader"] {
    background: var(--fg-surface) !important;
    border: 1px solid var(--fg-border) !important;
    border-radius: var(--fg-r-lg) !important;
    padding: 16px 20px !important;
    box-shadow: var(--fg-shadow-sm) !important;
}
div[data-testid="stFileUploader"] label[data-testid="stWidgetLabel"] p {
    color: var(--fg-ink) !important;
    font-family: var(--fg-sans) !important;
    font-size: 14.5px !important;
    font-weight: 700 !important;
    letter-spacing: -0.01em !important;
}
div[data-testid="stFileUploader"] section[data-testid="stFileUploaderDropzone"] {
    min-height: 94px !important;
    background: var(--fg-surface-muted) !important;
    border: 1.5px dashed var(--fg-border-strong) !important;
    border-radius: var(--fg-r-md) !important;
    padding: 14px 18px !important;
    box-sizing: border-box !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
    text-align: center !important;
    transition: border-color 180ms ease, background 180ms ease, box-shadow 180ms ease !important;
}
div[data-testid="stFileUploader"] section[data-testid="stFileUploaderDropzone"]:hover {
    border-color: var(--fg-accent) !important;
    background: var(--fg-accent-soft) !important;
    box-shadow: 0 0 0 3px rgba(29, 78, 216, 0.08) !important;
}
div[data-testid="stFileUploader"] div[data-testid="stFileUploaderDropzoneInstructions"] span,
div[data-testid="stFileUploader"] div[data-testid="stFileUploaderDropzoneInstructions"] small {
    color: var(--fg-muted) !important;
    font-family: var(--fg-sans) !important;
}
div[data-testid="stFileUploader"] button[data-testid="stBaseButton-secondary"] {
    background: var(--fg-accent) !important;
    color: #FFFFFF !important;
    border: 1px solid var(--fg-accent) !important;
    border-radius: var(--fg-r-sm) !important;
    min-height: 40px !important;
    padding: 0 18px !important;
    font-family: var(--fg-sans) !important;
    font-size: 13.5px !important;
    font-weight: 600 !important;
    box-shadow: var(--fg-shadow-xs) !important;
    transition: background 180ms ease, transform 180ms ease, box-shadow 180ms ease !important;
}
div[data-testid="stFileUploader"] button[data-testid="stBaseButton-secondary"]:hover {
    background: var(--fg-accent-hover) !important;
    border-color: var(--fg-accent-hover) !important;
    transform: translateY(-1px) !important;
}

/* Uploaded File Chip */
div[data-testid="stFileChip"] {
    background: var(--fg-surface) !important;
    border: 1px solid var(--fg-border) !important;
    border-radius: var(--fg-r-sm) !important;
    box-shadow: var(--fg-shadow-xs) !important;
    padding: 6px 12px !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 10px !important;
}
div[data-testid="stFileChip"] > div:first-child {
    background: var(--fg-accent-soft) !important;
    border: 1px solid var(--fg-accent-border) !important;
    border-radius: 6px !important;
    color: var(--fg-accent) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 32px !important;
    height: 32px !important;
}
div[data-testid="stFileChip"] > div:first-child svg {
    fill: var(--fg-accent) !important;
    color: var(--fg-accent) !important;
    width: 18px !important;
    height: 18px !important;
}
div[data-testid="stFileChipName"] {
    color: var(--fg-ink) !important;
    font-size: 13px !important;
    font-weight: 600 !important;
}
div[data-testid="stFileChip"] .stFileChipName + div,
div[data-testid="stFileChip"] > div:nth-child(2) > div:last-child {
    color: var(--fg-subtle) !important;
    font-family: var(--fg-mono) !important;
    font-size: 11px !important;
}
div[data-testid="stFileChip"] small button,
div[data-testid="stFileChipDeleteBtn"] button {
    background: transparent !important;
    border: none !important;
    color: var(--fg-subtle) !important;
}
div[data-testid="stFileChip"] small button svg,
div[data-testid="stFileChipDeleteBtn"] button svg {
    fill: var(--fg-subtle) !important;
}
div[data-testid="stFileChip"] small button:hover svg,
div[data-testid="stFileChipDeleteBtn"] button:hover svg {
    fill: var(--fg-forged) !important;
}

/* Scope Caption & Section Divider */
.fg-scope-note {
    text-align: center;
    font-size: 12px;
    color: var(--fg-subtle);
    margin: 6px 0 12px 0;
    line-height: 1.5;
}
.fg-divider-label {
    display: flex;
    align-items: center;
    gap: 14px;
    margin: 2px 0 10px 0;
}
.fg-divider-line {
    height: 1px;
    flex: 1;
    background: var(--fg-border);
}
.fg-divider-text {
    font-family: var(--fg-mono);
    font-size: 10.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--fg-subtle);
    white-space: nowrap;
}

/* Unified Action & Sample Buttons */
div[data-testid="stButton"] button,
div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"] {
    width: 100% !important;
    min-height: 44px !important;
    height: auto !important;
    background: var(--fg-surface) !important;
    border: 1px solid var(--fg-border-strong) !important;
    border-radius: 10px !important;
    color: var(--fg-ink) !important;
    font-family: var(--fg-sans) !important;
    font-size: 13.5px !important;
    font-weight: 600 !important;
    letter-spacing: -0.01em !important;
    padding: 10px 14px !important;
    box-shadow: var(--fg-shadow-xs) !important;
    transition: background 180ms ease, border-color 180ms ease, color 180ms ease, transform 180ms ease, box-shadow 180ms ease !important;
}
div[data-testid="stButton"] button:hover,
div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"]:hover {
    background: var(--fg-accent-soft) !important;
    border-color: var(--fg-accent) !important;
    color: var(--fg-accent) !important;
    transform: translateY(-1px) !important;
    box-shadow: var(--fg-shadow-sm) !important;
}
div[data-testid="stButton"] button:focus-visible,
div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"]:focus-visible {
    outline: none !important;
    border-color: var(--fg-accent) !important;
    box-shadow: 0 0 0 3px rgba(29, 78, 216, 0.16) !important;
}
div[data-testid="stButton"] button:active,
div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"]:active {
    transform: translateY(0) !important;
}

/* Active Sample / Upload Banner */
.fg-sample-banner {
    display: flex;
    align-items: center;
    min-height: 44px;
    box-sizing: border-box;
    padding: 10px 16px;
    background: var(--fg-accent-soft);
    border: 1px solid var(--fg-accent-border);
    border-left: 4px solid var(--fg-accent);
    border-radius: var(--fg-r-sm);
    margin: 0 0 12px 0;
    font-size: 13px;
    color: var(--fg-ink);
    box-shadow: var(--fg-shadow-xs);
    word-break: break-word;
}
.fg-sample-banner-upload {
    border-left-color: var(--fg-info);
    background: var(--fg-info-bg);
    border-color: var(--fg-info-border);
}

/* Advisory Notice */
.fg-advisory {
    background: var(--fg-warning-bg);
    border: 1px solid var(--fg-warning-border);
    border-left: 4px solid var(--fg-warning);
    border-radius: var(--fg-r-sm);
    padding: 12px 16px;
    margin: 12px 0 18px 0;
    box-shadow: var(--fg-shadow-xs);
}
.fg-advisory-inner {
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
}
.fg-advisory-tag {
    display: inline-block;
    padding: 3px 8px;
    background: #FEF3C7;
    border: 1px solid #FCD34D;
    border-radius: 5px;
    font-family: var(--fg-mono);
    font-size: 10.5px;
    font-weight: 700;
    letter-spacing: 0.06em;
    color: var(--fg-warning);
    text-transform: uppercase;
    white-space: nowrap;
}
.fg-advisory-text {
    color: #78350F;
    font-size: 12.5px;
    line-height: 1.5;
    font-weight: 500;
}

/* Splash Loader (Light Fintech) */
.fg-splash-overlay {
    position: fixed;
    inset: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(245, 247, 251, 0.96);
    backdrop-filter: blur(8px);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9999999;
}
.fg-splash-card {
    background: var(--fg-surface);
    border: 1px solid var(--fg-border);
    border-radius: var(--fg-r-lg);
    padding: 36px 40px;
    width: min(460px, 90vw);
    text-align: center;
    box-shadow: var(--fg-shadow-md);
}
.fg-splash-icon-wrapper {
    position: relative;
    width: 52px;
    height: 52px;
    margin: 0 auto 18px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.fg-splash-spinner {
    position: absolute;
    inset: 0;
    border-radius: 50%;
    border: 3px solid var(--fg-accent-soft);
    border-top-color: var(--fg-accent);
    border-right-color: var(--fg-accent);
    animation: fg-splash-spin 0.9s linear infinite;
}
.fg-splash-core-dot {
    width: 10px;
    height: 10px;
    background: var(--fg-accent);
    border-radius: 50%;
}
@keyframes fg-splash-spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}
.fg-splash-brand {
    font-family: var(--fg-mono);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.16em;
    color: var(--fg-accent);
    text-transform: uppercase;
    margin-bottom: 6px;
}
.fg-splash-title {
    font-family: var(--fg-sans);
    font-size: 19px;
    font-weight: 700;
    color: var(--fg-ink);
    margin-bottom: 20px;
    letter-spacing: -0.02em;
}
.fg-splash-track {
    width: 100%;
    height: 4px;
    background: var(--fg-surface-subtle);
    border-radius: var(--fg-r-pill);
    overflow: hidden;
    position: relative;
    margin-bottom: 16px;
}
.fg-splash-bar {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 45%;
    background: linear-gradient(90deg, var(--fg-accent), #3B82F6);
    border-radius: var(--fg-r-pill);
    animation: fg-splash-sweep 1.2s ease-in-out infinite;
}
@keyframes fg-splash-sweep {
    0% { left: -45%; }
    50% { left: 45%; }
    100% { left: 100%; }
}
.fg-splash-status {
    font-family: var(--fg-mono);
    font-size: 12px;
    font-weight: 600;
    color: var(--fg-ink-2);
    margin-bottom: 6px;
}
.fg-splash-status span { color: var(--fg-accent); }
.fg-splash-sub {
    font-family: var(--fg-sans);
    font-size: 12.5px;
    color: var(--fg-subtle);
    line-height: 1.5;
}

/* Inline Analysis Spinner */
div[data-testid="stSpinner"] {
    background: var(--fg-surface) !important;
    border: 1px solid var(--fg-border) !important;
    border-left: 4px solid var(--fg-accent) !important;
    border-radius: var(--fg-r-md) !important;
    padding: 14px 18px !important;
    margin: 12px 0 18px 0 !important;
    box-shadow: var(--fg-shadow-sm) !important;
    position: relative !important;
    overflow: hidden !important;
}
div[data-testid="stSpinner"] > div {
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
}
div[data-testid="stSpinner"] > div > i {
    border-color: var(--fg-accent-soft) !important;
    border-top-color: var(--fg-accent) !important;
    width: 20px !important;
    height: 20px !important;
    min-width: 20px !important;
}
div[data-testid="stSpinner"] > div > span {
    color: var(--fg-ink) !important;
    font-family: var(--fg-sans) !important;
    font-size: 13.5px !important;
    font-weight: 600 !important;
}

/* Receipt Inspector Tabs (VirusTotal / Sightengine crisp underline tabs) */
div[data-testid="stTabs"] button[data-baseweb="tab"] {
    background: transparent !important;
    color: var(--fg-muted) !important;
    font-family: var(--fg-sans) !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    min-height: 42px !important;
    padding: 8px 12px !important;
    border-radius: 6px 6px 0 0 !important;
    transition: color 180ms ease, background 180ms ease !important;
}
div[data-testid="stTabs"] button[data-baseweb="tab"]:hover {
    color: var(--fg-ink) !important;
    background: rgba(29, 78, 216, 0.04) !important;
}
div[data-testid="stTabs"] button[data-baseweb="tab"][aria-selected="true"] {
    color: var(--fg-accent) !important;
    font-weight: 700 !important;
}
div[data-testid="stTabs"] div[data-baseweb="tab-border"] {
    background-color: var(--fg-border) !important;
}
div[data-testid="stTabs"] div[data-baseweb="tab-highlight"] {
    background-color: var(--fg-accent) !important;
    height: 2px !important;
}

/* Receipt Exhibit Image Mat */
div[data-testid="stImage"] {
    padding: 12px !important;
    margin-bottom: 10px !important;
    border: 1px solid var(--fg-border) !important;
    border-radius: var(--fg-r-md) !important;
    background: var(--fg-surface) !important;
    box-shadow: var(--fg-shadow-sm) !important;
}
div[data-testid="stImage"] img {
    border-radius: 7px !important;
    width: 100% !important;
}
div[data-testid="stImage"] button,
div[data-testid="stImageToolbar"],
div[data-testid="stElementToolbar"] {
    display: none !important;
}

.fg-img-caption {
    font-size: 12px;
    color: var(--fg-subtle);
    margin-top: 2px;
    margin-bottom: 8px;
    text-align: center;
}
.fg-exhibit-meta {
    font-family: var(--fg-mono);
    font-size: 11px;
    color: var(--fg-muted);
    margin-top: 10px;
    line-height: 1.6;
    background: var(--fg-surface);
    padding: 10px 14px;
    border-radius: var(--fg-r-sm);
    border: 1px solid var(--fg-border);
    box-shadow: var(--fg-shadow-xs);
}

/* CNN Result Verdict Cards (Sightengine-inspired clean white + confidence bar) */
.fg-result-card {
    background: var(--fg-surface);
    border: 1px solid var(--fg-border);
    border-left-width: 4px;
    border-radius: var(--fg-r-md);
    padding: 18px 20px;
    margin-bottom: 14px;
    box-shadow: var(--fg-shadow-sm);
    transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
    animation: fg-enter 320ms cubic-bezier(0.2, 0.8, 0.2, 1) both;
}
.fg-result-card:hover {
    transform: translateY(-1px);
    box-shadow: var(--fg-shadow-md);
}
.fg-verdict-authentic {
    border-left-color: var(--fg-authentic);
}
.fg-verdict-forged {
    border-left-color: var(--fg-forged);
}
.fg-result-head {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 14px;
}
.fg-model-name {
    color: var(--fg-ink);
    font-size: 17px;
    font-weight: 700;
    letter-spacing: -0.02em;
    line-height: 1.25;
}
.fg-model-badge {
    display: inline-block;
    margin-top: 5px;
    padding: 3px 8px;
    font-size: 11.5px;
    font-weight: 500;
    color: var(--fg-muted);
    background: var(--fg-surface-muted);
    border: 1px solid var(--fg-border);
    border-radius: 6px;
}
.fg-result-score-col {
    text-align: right;
    flex-shrink: 0;
}
.fg-verdict-pill {
    display: inline-block;
    padding: 4px 10px;
    border: 1px solid;
    border-radius: var(--fg-r-pill);
    font-family: var(--fg-mono);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}
.fg-verdict-pill-authentic {
    color: var(--fg-authentic);
    background: var(--fg-authentic-bg);
    border-color: var(--fg-authentic-border);
}
.fg-verdict-pill-forged {
    color: var(--fg-forged);
    background: var(--fg-forged-bg);
    border-color: var(--fg-forged-border);
}
.fg-confidence {
    font-family: var(--fg-mono);
    font-size: 26px;
    font-weight: 700;
    letter-spacing: -0.03em;
    line-height: 1.15;
    margin-top: 6px;
    font-variant-numeric: tabular-nums;
}
.fg-conf-authentic { color: var(--fg-authentic); }
.fg-conf-forged { color: var(--fg-forged); }

.fg-conf-track {
    width: 100%;
    height: 6px;
    background: var(--fg-surface-subtle);
    border-radius: var(--fg-r-pill);
    overflow: hidden;
    margin: 12px 0 11px 0;
}
.fg-conf-fill {
    height: 100%;
    border-radius: var(--fg-r-pill);
    transform-origin: left;
    animation: fg-bar-grow 500ms cubic-bezier(0.2, 0.8, 0.2, 1) both;
}
.fg-conf-fill-authentic { background: var(--fg-authentic); }
.fg-conf-fill-forged { background: var(--fg-forged); }

.fg-result-meta-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 8px;
    padding-top: 9px;
    border-top: 1px solid var(--fg-border);
    font-family: var(--fg-mono);
    font-size: 11px;
    color: var(--fg-subtle);
}
.fg-meta-accent-lat { color: var(--fg-info); font-weight: 600; }
.fg-meta-accent-mem { color: var(--fg-accent); font-weight: 600; }

/* Section Headers & Panels */
.fg-section-gap {
    margin-top: 32px;
    margin-bottom: 14px;
}
.fg-section-title {
    color: var(--fg-ink);
    font-size: 15px;
    font-weight: 700;
    letter-spacing: -0.015em;
    display: flex;
    align-items: center;
    gap: 8px;
}
.fg-section-title::before {
    content: "";
    display: inline-block;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--fg-accent);
    flex-shrink: 0;
}
.fg-subhead-kicker {
    margin-top: 28px;
    margin-bottom: 12px;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--fg-muted);
}

/* Tri-Spectral Gallery Headers */
.fg-tri-header {
    background: var(--fg-surface);
    border: 1px solid var(--fg-border);
    border-top-width: 3px;
    border-radius: var(--fg-r-sm);
    padding: 10px 14px;
    margin-bottom: 8px;
    min-height: 54px;
    box-shadow: var(--fg-shadow-xs);
}
.fg-tri-orig { border-top-color: var(--fg-subtle); }
.fg-tri-ela { border-top-color: var(--fg-accent); }
.fg-tri-heat { border-top-color: var(--fg-info); }
.fg-tri-title {
    font-size: 13px;
    font-weight: 700;
    color: var(--fg-ink);
}
.fg-tri-sub {
    font-size: 11px;
    color: var(--fg-subtle);
    margin-top: 2px;
}

/* Generic Elevated Card Panels */
.fg-panel {
    margin-top: 24px;
    background: var(--fg-surface);
    border: 1px solid var(--fg-border);
    border-radius: var(--fg-r-md);
    padding: 20px 22px;
    box-shadow: var(--fg-shadow-sm);
}
.fg-panel-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 16px;
}
.fg-panel-title {
    font-size: 15px;
    font-weight: 700;
    color: var(--fg-ink);
    letter-spacing: -0.015em;
}
.fg-panel-subtitle {
    font-size: 12.5px;
    color: var(--fg-muted);
    margin-top: 2px;
    line-height: 1.45;
}

/* How the AI Analyzes Grid */
.fg-how-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 14px;
    font-size: 12.5px;
    line-height: 1.6;
    color: var(--fg-ink-2);
}
.fg-how-step {
    background: var(--fg-surface-muted);
    border: 1px solid var(--fg-border);
    border-radius: var(--fg-r-sm);
    padding: 14px 16px;
}
.fg-how-step-title {
    font-weight: 700;
    font-size: 13px;
    margin-bottom: 6px;
}
.fg-how-ela { color: var(--fg-accent); }
.fg-how-heat { color: var(--fg-info); }
.fg-how-cnn { color: var(--fg-warning); }

/* Empty State Readiness Card (Solid border — avoids double-dashed clutter) */
.fg-ready-card {
    margin-top: 14px;
    padding: 20px 22px;
    background: var(--fg-surface);
    border: 1px solid var(--fg-border);
    border-radius: var(--fg-r-md);
    text-align: center;
    box-shadow: var(--fg-shadow-sm);
}
.fg-ready-title {
    font-size: 15px;
    font-weight: 700;
    color: var(--fg-ink);
    letter-spacing: -0.015em;
    margin-bottom: 6px;
}
.fg-ready-desc {
    font-size: 13px;
    color: var(--fg-muted);
    max-width: 520px;
    margin: 0 auto 16px auto;
    line-height: 1.55;
}
.fg-spec-row {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    flex-wrap: wrap;
}
.fg-spec-chip {
    padding: 5px 11px;
    background: var(--fg-surface-muted);
    border: 1px solid var(--fg-border);
    border-radius: 6px;
    font-family: var(--fg-mono);
    font-size: 11px;
    font-weight: 600;
    color: var(--fg-ink-2);
}

/* Charts & Analytics (Model Comparison) */
.fg-chart-card {
    background: var(--fg-surface);
    border: 1px solid var(--fg-border);
    border-radius: var(--fg-r-md);
    padding: 22px 24px;
    box-shadow: var(--fg-shadow-sm);
    animation: fg-enter 350ms cubic-bezier(0.2, 0.8, 0.2, 1) both;
}
.fg-chart-legend {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 14px;
    font-family: var(--fg-mono);
    font-size: 11px;
    color: var(--fg-muted);
}
.fg-signal-key {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: var(--fg-muted);
    white-space: nowrap;
}
.fg-signal-key > span {
    width: 9px;
    height: 9px;
    border-radius: 2px;
    display: inline-block;
}
.fg-signal-key-accuracy > span { background: var(--fg-accent); }
.fg-signal-key-fast > span { background: var(--fg-authentic); }
.fg-signal-key-mid > span { background: var(--fg-info); }
.fg-signal-key-slow > span { background: #D97706; }

.fg-chart-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 18px;
    align-items: stretch;
}
.fg-chart-subpanel {
    background: var(--fg-surface-muted);
    border: 1px solid var(--fg-border);
    border-radius: var(--fg-r-sm);
    padding: 18px;
    display: flex;
    flex-direction: column;
}
.fg-chart-title {
    color: var(--fg-ink);
    font-size: 13.5px;
    font-weight: 700;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    margin-bottom: 14px;
}
.fg-chart-hint-acc {
    font-family: var(--fg-mono);
    font-size: 11px;
    font-weight: 600;
    color: var(--fg-accent);
}
.fg-chart-hint-lat {
    font-family: var(--fg-mono);
    font-size: 11px;
    font-weight: 600;
    color: var(--fg-authentic);
}
.fg-bar-row { margin-bottom: 13px; }
.fg-bar-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    margin-bottom: 6px;
    font-size: 12.5px;
}
.fg-bar-label {
    color: var(--fg-ink);
    font-weight: 600;
}
.fg-bar-val {
    font-family: var(--fg-mono);
    font-weight: 700;
    white-space: nowrap;
    font-variant-numeric: tabular-nums;
}
.fg-bar-sd {
    font-size: 10.5px;
    font-weight: 500;
    color: var(--fg-subtle);
}
.fg-bar-track {
    height: 8px;
    background: var(--fg-border);
    border-radius: var(--fg-r-pill);
    overflow: hidden;
}
.fg-bar-fill {
    display: block;
    height: 100%;
    border-radius: var(--fg-r-pill);
    transform-origin: left;
    animation: fg-bar-grow 600ms cubic-bezier(0.2, 0.8, 0.2, 1) both;
}
.fg-fill-acc { background: linear-gradient(90deg, #1D4ED8, #3B82F6); }
.fg-fill-acc-mid { background: linear-gradient(90deg, #2563EB, #60A5FA); }
.fg-fill-acc-low { background: #94A3B8; }
.fg-fill-fast { background: linear-gradient(90deg, #059669, #10B981); }
.fg-fill-mid { background: linear-gradient(90deg, #0E7490, #06B6D4); }
.fg-fill-slow { background: linear-gradient(90deg, #D97706, #F59E0B); }

.fg-val-acc { color: var(--fg-accent); }
.fg-val-fast { color: var(--fg-authentic); }
.fg-val-mid { color: var(--fg-info); }
.fg-val-slow { color: var(--fg-warning); }

.fg-chart-insight {
    margin-top: auto;
    padding-top: 12px;
    border-top: 1px solid var(--fg-border);
    font-size: 12px;
    line-height: 1.5;
    color: var(--fg-muted);
}

/* Publication-Grade Horizontal-Rule Tables */
.fg-table-card {
    width: 100%;
    max-width: 100%;
    border-radius: var(--fg-r-md);
    border: 1px solid var(--fg-border);
    background: var(--fg-surface);
    box-shadow: var(--fg-shadow-sm);
    margin-bottom: 22px;
    overflow: hidden;
}
.fg-table-card-head {
    padding: 16px 20px 14px 20px;
    border-bottom: 1px solid var(--fg-border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 10px;
}
.fg-records-count {
    font-family: var(--fg-mono);
    font-size: 11px;
    font-weight: 600;
    color: var(--fg-muted);
    background: var(--fg-surface-muted);
    padding: 4px 10px;
    border-radius: var(--fg-r-pill);
    border: 1px solid var(--fg-border);
}
.fg-table-scroll {
    width: 100%;
    max-width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
}
.fg-metrics-table {
    width: 100%;
    border-collapse: collapse;
    border-spacing: 0;
    background: transparent;
    margin: 0;
}
.fg-metrics-table thead tr {
    background: var(--fg-surface-muted);
}
.fg-metrics-table th {
    padding: 11px 10px;
    color: var(--fg-muted);
    font-family: var(--fg-sans);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.02em;
    border-top: none !important;
    border-left: none !important;
    border-right: none !important;
    border-bottom: 1px solid var(--fg-border) !important;
    white-space: normal;
    line-height: 1.25;
    vertical-align: middle;
    text-align: center;
}
.fg-metrics-table td {
    padding: 11px 10px;
    color: var(--fg-ink-2);
    border-top: none !important;
    border-left: none !important;
    border-right: none !important;
    border-bottom: 1px solid var(--fg-border) !important;
    font-family: var(--fg-mono);
    font-size: 12px;
    white-space: nowrap;
    vertical-align: middle;
    text-align: center;
    font-variant-numeric: tabular-nums;
    transition: background-color 140ms ease;
}
.fg-metrics-table td.arch-cell {
    color: var(--fg-ink);
    font-family: var(--fg-sans);
    font-weight: 700;
    font-size: 13px;
    white-space: normal;
}
.fg-metrics-table td.fg-cond-cell {
    font-family: var(--fg-sans);
    font-size: 12px;
    font-weight: 600;
    color: var(--fg-muted);
}
.fg-metrics-table tbody tr.fg-model-start td {
    border-top: 2px solid var(--fg-border-strong);
}
.fg-metrics-table tbody tr.fg-model-start:first-child td {
    border-top: 0;
}
.fg-metrics-table tbody tr:hover td {
    background: var(--fg-surface-muted);
}
.fg-metrics-table tbody tr:last-child td {
    border-bottom: none;
}
.fg-std {
    display: block;
    font-size: 10px;
    color: var(--fg-subtle);
    font-weight: 500;
    margin-top: 2px;
    line-height: 1.1;
}
.fg-metric-top {
    color: var(--fg-accent);
    background: var(--fg-accent-soft);
    border: 1px solid var(--fg-accent-border);
    border-radius: 5px;
    padding: 2px 7px;
    font-weight: 700;
    display: inline-block;
}
.fg-metric-fast {
    color: var(--fg-authentic);
    background: var(--fg-authentic-bg);
    border: 1px solid var(--fg-authentic-border);
    border-radius: 5px;
    padding: 2px 7px;
    font-weight: 700;
    display: inline-block;
}
.fg-metric-slow {
    color: var(--fg-warning);
    background: var(--fg-warning-bg);
    border: 1px solid var(--fg-warning-border);
    border-radius: 5px;
    padding: 2px 7px;
    font-weight: 700;
    display: inline-block;
}
.fg-delta-pos {
    color: var(--fg-authentic);
    font-weight: 700;
}
.fg-delta-zero {
    color: var(--fg-subtle);
}
.fg-comp-score {
    font-weight: 700;
    color: var(--fg-accent);
}

/* Logs & Records Table */
.fg-log-table {
    width: 100%;
    border-collapse: collapse;
    text-align: left;
}
.fg-log-table thead tr {
    background: var(--fg-surface-muted);
    border-bottom: 1px solid var(--fg-border);
}
.fg-log-table th {
    padding: 10px 14px;
    font-family: var(--fg-mono);
    font-size: 10.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--fg-muted);
    white-space: nowrap;
    border-top: none !important;
    border-left: none !important;
    border-right: none !important;
    border-bottom: 1px solid var(--fg-border) !important;
}
.fg-log-table td {
    padding: 10px 14px;
    border-top: none !important;
    border-left: none !important;
    border-right: none !important;
    border-bottom: 1px solid var(--fg-border) !important;
    font-family: var(--fg-mono);
    font-size: 12px;
    color: var(--fg-ink-2);
    white-space: nowrap;
}
.fg-log-table tbody tr:hover td {
    background: var(--fg-surface-muted);
}
.fg-log-table tbody tr:last-child td {
    border-bottom: none;
}
.fg-log-arch { font-family: var(--fg-sans) !important; font-weight: 700; color: var(--fg-ink) !important; }
.fg-verdict-text-authentic { color: var(--fg-authentic) !important; font-weight: 700; }
.fg-verdict-text-forged { color: var(--fg-forged) !important; font-weight: 700; }
.fg-log-lat { color: var(--fg-info) !important; font-weight: 600; }
.fg-log-mem { color: var(--fg-accent) !important; font-weight: 600; }

/* Dataset Composition Summary Rows */
.fg-sub-note {
    display: block;
    font-family: var(--fg-sans);
    font-size: 10.5px;
    font-weight: 500;
    color: var(--fg-subtle);
    margin-top: 2px;
}
.fg-subtotal-row td {
    background: var(--fg-surface-muted);
    border-top: 1px solid var(--fg-border-strong);
    font-weight: 700;
    color: var(--fg-ink);
}
.fg-holdout-row td {
    background: var(--fg-surface);
    color: var(--fg-muted);
}
.fg-total-row td {
    background: var(--fg-accent-soft);
    border-top: 2px solid var(--fg-accent-border);
    font-weight: 700;
    color: var(--fg-accent);
}

/* Metric Interpretation Guide Expander */
div[data-testid="stExpander"] {
    background-color: var(--fg-surface) !important;
    border: 1px solid var(--fg-border) !important;
    border-radius: var(--fg-r-md) !important;
    box-shadow: var(--fg-shadow-xs) !important;
    margin: 8px 0 24px 0 !important;
    overflow: hidden !important;
}
div[data-testid="stExpander"] details {
    border: none !important;
    background: transparent !important;
}
div[data-testid="stExpander"] summary {
    background: var(--fg-surface-muted) !important;
    padding: 12px 16px !important;
    color: var(--fg-ink) !important;
    font-family: var(--fg-sans) !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    border-bottom: 1px solid var(--fg-border) !important;
    transition: background 180ms ease, color 180ms ease !important;
}
div[data-testid="stExpander"] details:not([open]) summary {
    border-bottom: none !important;
}
div[data-testid="stExpander"] summary p {
    font-size: 13px !important;
    font-weight: 700 !important;
    color: var(--fg-ink) !important;
    margin: 0 !important;
}
div[data-testid="stExpander"] summary:hover,
div[data-testid="stExpander"] summary:hover p {
    color: var(--fg-accent) !important;
    background: var(--fg-accent-soft) !important;
}
div[data-testid="stExpander"] summary svg {
    color: var(--fg-accent) !important;
    fill: var(--fg-accent) !important;
}
div[data-testid="stExpander"] [data-testid="stExpanderDetails"] {
    padding: 16px 18px !important;
    background-color: var(--fg-surface) !important;
}

.fg-guide-metrics-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    font-size: 12.5px;
    line-height: 1.55;
    color: var(--fg-ink-2);
}
.fg-guide-item {
    background: var(--fg-surface-muted);
    border: 1px solid var(--fg-border);
    border-radius: var(--fg-r-sm);
    padding: 12px 14px;
    box-sizing: border-box;
}
.fg-guide-foot {
    margin-top: 12px;
    font-size: 12px;
    color: var(--fg-muted);
    border-top: 1px solid var(--fg-border);
    padding-top: 10px;
}

/* Selectbox Controls */
div[data-testid="stSelectbox"] {
    max-width: 100% !important;
}
div[data-testid="stSelectbox"] label p {
    color: var(--fg-ink) !important;
    font-family: var(--fg-sans) !important;
    font-size: 13px !important;
    font-weight: 600 !important;
}
div[data-testid="stSelectbox"] > div > div {
    min-height: 44px !important;
    background: var(--fg-surface) !important;
    border-color: var(--fg-border-strong) !important;
    border-radius: var(--fg-r-sm) !important;
    color: var(--fg-ink) !important;
    font-family: var(--fg-sans) !important;
    box-shadow: var(--fg-shadow-xs) !important;
}
div[data-testid="stSelectbox"] > div > div:hover,
div[data-testid="stSelectbox"] > div > div:focus-within {
    border-color: var(--fg-accent) !important;
    box-shadow: 0 0 0 3px rgba(29, 78, 216, 0.12) !important;
}
div[data-testid="stSelectbox"] svg {
    fill: var(--fg-accent) !important;
}
ul[data-testid="stSelectboxOptionsList"],
div[data-baseweb="popover"] > div,
div[data-baseweb="menu"] {
    background: var(--fg-surface) !important;
    border: 1px solid var(--fg-border) !important;
    box-shadow: var(--fg-shadow-md) !important;
}
li[role="option"] {
    color: var(--fg-ink) !important;
    font-family: var(--fg-sans) !important;
}
li[role="option"]:hover,
li[role="option"][aria-selected="true"] {
    background: var(--fg-accent-soft) !important;
    color: var(--fg-accent) !important;
}

/* Confusion Matrix */
.fg-threshold-pill {
    font-family: var(--fg-mono);
    font-size: 11.5px;
    font-weight: 600;
    color: var(--fg-accent);
    background: var(--fg-accent-soft);
    border: 1px solid var(--fg-accent-border);
    border-radius: var(--fg-r-pill);
    padding: 5px 12px;
    white-space: nowrap;
}
.fg-cm-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 8px;
    text-align: center;
    table-layout: fixed;
}
.fg-cm-th {
    padding: 8px 6px;
    font-size: 11px;
    font-weight: 700;
    color: var(--fg-muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
.fg-cm-row-label {
    padding: 10px 10px;
    font-size: 11.5px;
    font-weight: 700;
    color: var(--fg-muted);
    text-align: right;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    width: 24%;
}
.fg-cm-table th,
.fg-cm-table td {
    border-top: none !important;
    border-left: none !important;
    border-right: none !important;
    border-bottom: none !important;
}
.fg-cm-cell-good {
    background: var(--fg-authentic-bg);
    border: 1px solid var(--fg-authentic-border) !important;
    border-radius: 10px;
    padding: 16px 10px;
}
.fg-cm-cell-bad {
    background: var(--fg-forged-bg);
    border: 1px solid var(--fg-forged-border) !important;
    border-radius: 10px;
    padding: 16px 10px;
}
.fg-cm-num-good {
    font-family: var(--fg-mono);
    font-size: 26px;
    font-weight: 700;
    color: var(--fg-authentic);
    line-height: 1.1;
}
.fg-cm-num-bad {
    font-family: var(--fg-mono);
    font-size: 26px;
    font-weight: 700;
    color: var(--fg-forged);
    line-height: 1.1;
}
.fg-cm-tag-good {
    font-size: 11.5px;
    font-weight: 700;
    color: var(--fg-authentic);
    margin-top: 4px;
}
.fg-cm-tag-bad {
    font-size: 11.5px;
    font-weight: 700;
    color: var(--fg-forged);
    margin-top: 4px;
}
.fg-cm-desc {
    font-size: 11px;
    color: var(--fg-muted);
    margin-top: 2px;
}
.fg-cm-note {
    margin-top: 14px;
    padding: 12px 14px;
    background: var(--fg-surface-muted);
    border: 1px solid var(--fg-border);
    border-radius: var(--fg-r-sm);
    font-size: 12.5px;
    color: var(--fg-ink-2);
    line-height: 1.55;
}

/* Footer & Forensic Delimitation */
.fg-footer {
    margin-top: 16px;
    padding-top: 12px;
    border-top: 1px solid var(--fg-border);
    text-align: center;
}
.fg-scope-disclaimer {
    padding: 11px 16px;
    background: var(--fg-surface);
    border: 1px solid var(--fg-border);
    border-radius: var(--fg-r-sm);
    font-size: 12px;
    color: var(--fg-muted);
    line-height: 1.5;
    text-align: center;
}
.fg-credit-line {
    margin-top: 10px;
    font-family: var(--fg-mono);
    font-size: 11px;
    color: var(--fg-subtle);
}

/* Animations */
@keyframes fg-enter {
    from { opacity: 0; transform: translateY(6px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes fg-bar-grow {
    from { transform: scaleX(0); }
    to { transform: scaleX(1); }
}
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}

/* Scrollbar */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--fg-border-strong); border-radius: 999px; border: 2px solid transparent; background-clip: content-box; }
::-webkit-scrollbar-thumb:hover { background: var(--fg-subtle); border: 2px solid transparent; background-clip: content-box; }

/* Laptop Breakpoint (<= 1366px) */
@media (max-width: 1366px) {
    .block-container {
        padding: 0.9rem 1.5rem 1.25rem !important;
    }
}

/* Tablet Breakpoint (<= 900px) */
@media (max-width: 900px) {
    .fg-how-grid { grid-template-columns: 1fr; }
    .fg-chart-grid { grid-template-columns: 1fr; }
    .fg-guide-metrics-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}

/* Mobile Breakpoint (<= 640px) */
@media (max-width: 640px) {
    .block-container {
        padding: 1rem 0.95rem 2.5rem !important;
    }
    .fg-brand-title { font-size: 21px; }
    .fg-topbar-subtitle { font-size: 12.5px; }

    /* Full-width 2-column top navigation on mobile */
    div[data-testid="stRadio"] > div[data-testid="stRadioGroup"],
    div[data-testid="stRadio"] div[role="radiogroup"] {
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
        width: 100% !important;
    }
    div[data-testid="stRadio"] label[data-testid="stRadioOption"],
    div[data-testid="stRadio"] label[data-baseweb="radio"] {
        min-height: 44px !important;
        padding: 8px 10px !important;
        width: 100% !important;
    }
    div[data-testid="stRadio"] label[data-testid="stRadioOption"] p,
    div[data-testid="stRadio"] label[data-baseweb="radio"] p {
        font-size: 12.5px !important;
    }

    .fg-guide-metrics-grid { grid-template-columns: 1fr; }
    .fg-result-card { padding: 15px 16px; }
    .fg-confidence { font-size: 22px; }
    .fg-panel { padding: 16px 14px; }
    .fg-chart-card { padding: 16px 14px; }

    /* Mobile-safe Confusion Matrix */
    .fg-cm-table { border-spacing: 5px; }
    .fg-cm-th { font-size: 9.5px; padding: 6px 3px; }
    .fg-cm-row-label {
        font-size: 9.5px;
        padding: 6px 4px;
        text-align: center;
        width: 22%;
    }
    .fg-cm-cell-good, .fg-cm-cell-bad { padding: 11px 6px; }
    .fg-cm-num-good, .fg-cm-num-bad { font-size: 20px; }
    .fg-cm-tag-good, .fg-cm-tag-bad { font-size: 10px; }
    .fg-cm-desc { font-size: 9.5px; }
}
</style>
"""
