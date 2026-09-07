PREMIUM_CSS = """
<style>
/* ForgeGuard visual system — forensic evidence workspace. Presentation only. */

:root {
    --fg-ink: #08111b;
    --fg-ink-2: #0b1723;
    --fg-panel: #101f2d;
    --fg-panel-raised: #142737;
    --fg-line: rgba(167, 196, 214, 0.16);
    --fg-line-strong: rgba(104, 223, 214, 0.34);
    --fg-paper: #edf6f7;
    --fg-muted: #9fb2bf;
    --fg-dim: #6f8797;
    --fg-cyan: #42d8cd;
    --fg-blue: #73a8ff;
    --fg-green: #54d29b;
    --fg-red: #ff6574;
    --fg-amber: #f5bd68;
    --fg-mono: "Cascadia Mono", Consolas, "Liberation Mono", monospace;
    --fg-sans: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
}

html, body, [class*="css"] {
    font-family: var(--fg-sans);
    color: var(--fg-paper);
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
}

html, body { background: var(--fg-ink); overflow-x: hidden; }

.stApp {
    background-color: var(--fg-ink);
    background-image:
        radial-gradient(circle at 71% -10%, rgba(54, 159, 186, .17), transparent 29rem),
        radial-gradient(circle at 0% 88%, rgba(51, 193, 167, .08), transparent 27rem),
        linear-gradient(rgba(127, 181, 198, .035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(127, 181, 198, .035) 1px, transparent 1px);
    background-size: auto, auto, 42px 42px, 42px 42px;
    background-attachment: fixed;
}

/* Streamlit chrome is intentionally kept out of the defense view. */
header[data-testid="stHeader"] {
    height: 0 !important; padding: 0 !important;
    background: transparent !important; pointer-events: none !important;
}
header[data-testid="stHeader"] > * { pointer-events: auto !important; }
.stAppDeployButton, div[data-testid="stAppDeployButton"], [data-testid="stToolbarActions"],
[data-testid="stMainMenu"], [data-testid="stDecoration"], [data-testid="stStatusWidget"],
#MainMenu, footer { display: none !important; visibility: hidden !important; }

.block-container {
    max-width: 1120px !important;
    padding: 5.8rem 2.75rem 5rem !important;
    margin: 0 auto !important;
}

/* Side rail */
@media (min-width: 769px) {
    section[data-testid="stSidebar"] {
        min-width: 288px !important;
        background: linear-gradient(180deg, #0c1825 0%, #09131e 100%) !important;
        border-right: 1px solid var(--fg-line) !important;
        box-shadow: 12px 0 36px rgba(0, 0, 0, .13) !important;
        transition: transform .28s ease, width .28s ease !important;
    }
    section[data-testid="stSidebar"][aria-expanded="false"] {
        width: 0 !important; min-width: 0 !important;
        transform: translateX(-110%) !important; overflow: hidden !important;
    }
}

@media (max-width: 768px) {
    .block-container { padding: 4.8rem 1.15rem 3rem !important; }
    section[data-testid="stSidebar"] {
        position: fixed !important; z-index: 999999 !important;
        width: 288px !important; max-width: 84% !important;
        background: #0b1723 !important; border-right: 1px solid var(--fg-line) !important;
        box-shadow: 12px 0 42px rgba(0,0,0,.45) !important;
    }
    section[data-testid="stSidebar"][aria-expanded="false"] { display: none !important; }
}

section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
    padding: 14px 18px 28px !important;
}
section[data-testid="stSidebar"] .stSidebarHeader,
section[data-testid="stSidebar"] [data-testid="stSidebarHeader"] {
    height: 62px !important; min-height: 62px !important;
    display: flex !important; justify-content: flex-end !important; align-items: center !important;
    padding: 0 6px !important; margin: 0 0 16px !important;
    border-bottom: 1px solid var(--fg-line) !important;
}

/* Shared, CSS-drawn menu control. */
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] button,
section[data-testid="stSidebar"] button[data-testid*="headerNoPadding"],
[data-testid="stSidebarCollapsedControl"], button[data-testid="stExpandSidebarButton"],
button[data-testid="stSidebarCollapsedControl"], div[data-testid="stSidebarCollapsedControl"] button {
    width: 40px !important; height: 40px !important; min-width: 40px !important; min-height: 40px !important;
    display: inline-flex !important; align-items: center !important; justify-content: center !important;
    padding: 0 !important; border: 1px solid rgba(154, 198, 218, .25) !important;
    border-radius: 8px !important; background: #132638 !important;
    box-shadow: inset 0 1px 0 rgba(255,255,255,.045), 0 5px 18px rgba(0,0,0,.22) !important;
    transition: background .18s ease, border-color .18s ease, transform .18s ease !important;
}
[data-testid="stSidebarCollapsedControl"], button[data-testid="stExpandSidebarButton"],
button[data-testid="stSidebarCollapsedControl"], div[data-testid="stSidebarCollapsedControl"] button {
    position: fixed !important; top: 20px !important; left: 20px !important; z-index: 999999 !important;
}
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] button:hover,
section[data-testid="stSidebar"] button[data-testid*="headerNoPadding"]:hover,
[data-testid="stSidebarCollapsedControl"]:hover, button[data-testid="stExpandSidebarButton"]:hover,
button[data-testid="stSidebarCollapsedControl"]:hover, div[data-testid="stSidebarCollapsedControl"] button:hover {
    background: #183246 !important; border-color: var(--fg-cyan) !important; transform: translateY(-1px) !important;
}
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] button *,
section[data-testid="stSidebar"] button[data-testid*="headerNoPadding"] *,
[data-testid="stSidebarCollapsedControl"] *, button[data-testid="stExpandSidebarButton"] *,
button[data-testid="stSidebarCollapsedControl"] *, div[data-testid="stSidebarCollapsedControl"] button * { display: none !important; }
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] button::after,
section[data-testid="stSidebar"] button[data-testid*="headerNoPadding"]::after,
[data-testid="stSidebarCollapsedControl"]::after, button[data-testid="stExpandSidebarButton"]::after,
button[data-testid="stSidebarCollapsedControl"]::after, div[data-testid="stSidebarCollapsedControl"] button::after {
    content: ""; width: 17px; height: 13px; display:block;
    background: linear-gradient(var(--fg-paper),var(--fg-paper)) top/100% 1px no-repeat,
                linear-gradient(var(--fg-paper),var(--fg-paper)) center/100% 1px no-repeat,
                linear-gradient(var(--fg-paper),var(--fg-paper)) bottom/100% 1px no-repeat;
}

/* Navigation */
div[data-testid="stSidebar"] [style*="System Navigation"] { padding-top: 14px !important; }
div[data-testid="stSidebar"] [style*="letter-spacing: 2px"] {
    color: var(--fg-cyan) !important; font-family: var(--fg-mono) !important;
    font-size: 10px !important; letter-spacing: 2.2px !important;
}
div[data-testid="stRadio"] > div[data-testid="stRadioGroup"] { display: flex !important; flex-direction: column !important; gap: 9px !important; }
div[data-testid="stRadio"] input[type="radio"],
div[data-testid="stRadio"] [data-testid="stRadioDot"],
div[data-testid="stRadio"] label div[class*="etak9234"],
div[data-testid="stRadio"] label div:has(> [data-testid="stMarkdownContainer"]) > div:first-child {
    display: none !important; width: 0 !important; height: 0 !important;
    min-width: 0 !important; margin: 0 !important; padding: 0 !important;
}
div[data-testid="stRadio"] label[data-testid="stRadioOption"] {
    min-height: 48px !important; box-sizing: border-box !important; margin: 0 !important; padding: 0 14px !important;
    display: flex !important; align-items: center !important; gap: 12px !important;
    border: 1px solid transparent !important; border-radius: 8px !important;
    background: transparent !important; position: relative !important; overflow: hidden !important;
    transition: background .18s ease, border-color .18s ease, transform .18s ease !important;
}
div[data-testid="stRadio"] label[data-testid="stRadioOption"]::after {
    content: ""; position: absolute; left: 0; top: 11px; bottom: 11px; width: 2px;
    background: transparent; transition: background .18s ease;
}
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:hover { background: rgba(97,167,197,.08) !important; border-color: rgba(125,199,218,.14) !important; }
div[data-testid="stRadio"] label[data-testid="stRadioOption"][aria-checked="true"],
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input:checked) {
    background: linear-gradient(90deg, rgba(51,202,193,.14), rgba(51,202,193,.025)) !important;
    border-color: rgba(66,216,205,.32) !important;
}
div[data-testid="stRadio"] label[data-testid="stRadioOption"][aria-checked="true"]::after,
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input:checked)::after { background: var(--fg-cyan) !important; }
div[data-testid="stRadio"] label[data-testid="stRadioOption"] p { color: #b7c8d1 !important; font-size: 13px !important; font-weight: 600 !important; }
div[data-testid="stRadio"] label[data-testid="stRadioOption"][aria-checked="true"] p,
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input:checked) p { color: var(--fg-paper) !important; }
div[data-testid="stRadio"] label[data-testid="stRadioOption"]::before {
    content: ""; width: 17px; height: 17px; flex: 0 0 17px; display: inline-block; background: #87a1b0;
}
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:nth-of-type(1)::before {
    clip-path: polygon(20% 5%,80% 5%,80% 95%,68% 86%,56% 95%,44% 86%,32% 95%,20% 86%);
    border: 1px solid #87a1b0;
}
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:nth-of-type(2)::before {
    clip-path: polygon(5% 95%,5% 62%,25% 62%,25% 95%,40% 95%,40% 29%,60% 29%,60% 95%,75% 95%,75% 5%,95% 5%,95% 95%);
}
div[data-testid="stRadio"] label[data-testid="stRadioOption"][aria-checked="true"]::before,
div[data-testid="stRadio"] label[data-testid="stRadioOption"]:has(input:checked)::before { background: var(--fg-cyan) !important; }
div[data-testid="stSidebar"] hr { border-color: var(--fg-line) !important; }
div[data-testid="stSidebar"] [style*="font-size: 11px; color: #64748B"] { color: var(--fg-dim) !important; }
div[data-testid="stSidebar"] [style*="color: #94A3B8"] { color: #bdd1db !important; }

/* Hero: a calm evidence dossier masthead. */
.block-container > div > div[data-testid="stMarkdownContainer"] > div[style*="margin-bottom: 28px"] {
    position: relative !important; padding: 0 0 27px !important; margin-bottom: 30px !important;
}
.block-container > div > div[data-testid="stMarkdownContainer"] > div[style*="margin-bottom: 28px"]::before {
    content: ""; width: 42px; height: 42px; display: block; float: right; margin: 5px 3px 0 20px;
    border: 1px solid rgba(66,216,205,.5); border-radius: 50%;
    background: radial-gradient(circle at center, var(--fg-cyan) 0 2px, transparent 3px),
                radial-gradient(circle at center, transparent 0 12px, rgba(66,216,205,.5) 13px 14px, transparent 15px),
                linear-gradient(90deg, transparent 48%, rgba(66,216,205,.5) 49% 51%, transparent 52%),
                linear-gradient(transparent 48%, rgba(66,216,205,.5) 49% 51%, transparent 52%);
    animation: fg-pulse 4s ease-in-out infinite;
}
@keyframes fg-pulse { 0%,100% { box-shadow: 0 0 0 rgba(66,216,205,0); } 50% { box-shadow: 0 0 20px rgba(66,216,205,.22); } }
.block-container div[style*="background: rgba(124, 111, 240, 0.1)"] {
    background: rgba(66,216,205,.08) !important; border-color: rgba(66,216,205,.28) !important;
    border-radius: 4px !important; padding: 5px 10px !important;
}
.block-container div[style*="background: rgba(124, 111, 240, 0.1)"] span { color: var(--fg-cyan) !important; font-family: var(--fg-mono) !important; }
.block-container div[style*="font-size: 36px"] { color: var(--fg-paper) !important; font-size: 39px !important; letter-spacing: -.9px !important; }
.block-container div[style*="font-size: 16px"] { color: #bdd2dc !important; }
.block-container div[style*="font-size: 13px; color: #64748B"] { color: var(--fg-dim) !important; }
.block-container div[style*="height: 1px; background: linear-gradient"] { background: linear-gradient(90deg, var(--fg-cyan), rgba(66,216,205,.2) 38%, transparent 72%) !important; }

/* Intake control */
div[data-testid="stFileUploader"] {
    padding: 20px !important; border: 1px solid var(--fg-line) !important; border-radius: 10px !important;
    background: linear-gradient(135deg, rgba(17,36,51,.97), rgba(12,25,37,.97)) !important;
    box-shadow: 0 16px 38px rgba(0,0,0,.22), inset 0 1px 0 rgba(255,255,255,.025) !important;
}
div[data-testid="stFileUploader"] label[data-testid="stWidgetLabel"] p { color: var(--fg-paper) !important; font-size: 14px !important; font-weight: 650 !important; }
div[data-testid="stFileUploader"] section[data-testid="stFileUploaderDropzone"] {
    min-height: 112px !important; border: 1px dashed rgba(91,191,207,.42) !important; border-radius: 7px !important;
    padding: 18px 20px !important; box-sizing: border-box !important;
    display: flex !important; flex-direction: column !important; align-items: center !important; justify-content: center !important;
    gap: 12px !important; text-align: center !important;
    background: rgba(4,14,23,.37) !important; transition: .2s ease !important;
}
div[data-testid="stFileUploader"] section[data-testid="stFileUploaderDropzone"]:hover {
    border-color: var(--fg-cyan) !important; background: rgba(35,171,165,.06) !important; box-shadow: inset 0 0 26px rgba(48,216,205,.06) !important;
}
div[data-testid="stFileUploader"] button[data-testid="stBaseButton-secondary"] {
    background: #18364a !important; color: var(--fg-paper) !important; border: 1px solid #3e7e92 !important;
    border-radius: 5px !important; box-shadow: none !important; font-weight: 650 !important;
}
div[data-testid="stFileUploader"] button[data-testid="stBaseButton-secondary"]:hover { background: #205169 !important; border-color: var(--fg-cyan) !important; }
div[data-testid="stFileUploader"] div[data-testid="stFileUploaderDropzoneInstructions"] span { color: #95b1be !important; font-family: var(--fg-mono) !important; }

/* Uploaded file exhibit chip / badge (no broken preview) */
div[data-testid="stFileChip"] {
    background: linear-gradient(135deg, rgba(16, 34, 50, 0.95), rgba(11, 23, 35, 0.95)) !important;
    border: 1px solid rgba(66, 216, 205, 0.3) !important;
    border-radius: 8px !important;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25) !important;
    padding: 6px 12px !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 10px !important;
}
div[data-testid="stFileChip"] > div:first-child {
    background: rgba(66, 216, 205, 0.12) !important;
    border: 1px solid rgba(66, 216, 205, 0.35) !important;
    border-radius: 6px !important;
    color: var(--fg-cyan) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 32px !important;
    height: 32px !important;
}
div[data-testid="stFileChip"] > div:first-child svg {
    fill: var(--fg-cyan) !important;
    color: var(--fg-cyan) !important;
    width: 18px !important;
    height: 18px !important;
}
div[data-testid="stFileChipName"] {
    color: var(--fg-paper) !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    letter-spacing: -0.2px !important;
}
div[data-testid="stFileChip"] .stFileChipName + div,
div[data-testid="stFileChip"] > div:nth-child(2) > div:last-child {
    color: var(--fg-dim) !important;
    font-family: var(--fg-mono) !important;
    font-size: 11px !important;
    font-weight: 500 !important;
}
div[data-testid="stFileChip"] small button,
div[data-testid="stFileChipDeleteBtn"] button {
    background: transparent !important;
    border: none !important;
    color: #8fa5b5 !important;
    transition: color 0.15s ease, transform 0.15s ease !important;
}
div[data-testid="stFileChip"] small button svg,
div[data-testid="stFileChipDeleteBtn"] button svg {
    fill: #8fa5b5 !important;
}
div[data-testid="stFileChip"] small button:hover svg,
div[data-testid="stFileChipDeleteBtn"] button:hover svg {
    fill: var(--fg-red) !important;
    transform: scale(1.1) !important;
}
button[data-testid="stBaseButton-borderlessIcon"] {
    background: rgba(16, 34, 50, 0.7) !important;
    border: 1px solid rgba(66, 216, 205, 0.25) !important;
    border-radius: 6px !important;
    color: var(--fg-cyan) !important;
    transition: background 0.15s ease !important;
}
button[data-testid="stBaseButton-borderlessIcon"]:hover {
    background: rgba(66, 216, 205, 0.15) !important;
    border-color: var(--fg-cyan) !important;
}
button[data-testid="stBaseButton-borderlessIcon"] span[data-testid="stIconMaterial"] {
    color: var(--fg-cyan) !important;
}

/* Real-time forensic neural inference loading indicator */
div[data-testid="stSpinner"] {
    background: linear-gradient(135deg, rgba(16, 34, 50, 0.96), rgba(11, 23, 35, 0.96)) !important;
    border: 1px solid rgba(66, 216, 205, 0.35) !important;
    border-left: 4px solid var(--fg-cyan) !important;
    border-radius: 9px !important;
    padding: 16px 20px !important;
    margin: 10px 0 18px 0 !important;
    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.3), 0 0 16px rgba(66, 216, 205, 0.08) !important;
}
div[data-testid="stSpinner"] > div {
    display: flex !important;
    align-items: center !important;
    gap: 14px !important;
}
div[data-testid="stSpinner"] > div > i {
    border-color: rgba(66, 216, 205, 0.2) !important;
    border-top-color: var(--fg-cyan) !important;
    width: 22px !important;
    height: 22px !important;
    min-width: 22px !important;
}
div[data-testid="stSpinner"] > div > span {
    color: var(--fg-paper) !important;
    font-family: var(--fg-sans) !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    letter-spacing: 0.3px !important;
    white-space: normal !important;
    word-break: break-word !important;
}
div[data-testid="stSpinner"] {
    position: relative !important;
    overflow: hidden !important;
}
div[data-testid="stSpinner"]::after {
    content: "";
    display: block;
    height: 3px;
    margin: 13px 0 0;
    border-radius: 999px;
    background: rgba(66,216,205,.12);
    box-shadow: inset 0 0 0 1px rgba(66,216,205,.1);
}
div[data-testid="stSpinner"]::before {
    content: "";
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    height: 3px;
    border-radius: 999px;
    background: linear-gradient(90deg, transparent, var(--fg-cyan), transparent);
    background-size: 42% 100%;
    background-repeat: no-repeat;
    animation: fg-loading-sweep 1.2s ease-in-out infinite;
}

/* Receipt exhibit and acquisition metadata */
div[data-testid="stImage"] {
    padding: 10px !important; margin-bottom: 15px !important; border: 1px solid var(--fg-line) !important;
    border-radius: 9px !important; background: #0f202e !important;
    box-shadow: 0 14px 32px rgba(0,0,0,.23) !important;
}
div[data-testid="stImage"] img { border-radius: 5px !important; width: 100% !important; }
div[data-testid="stImage"] button, div[data-testid="stImageToolbar"] { display: none !important; }
.fg-tech-specs {
    background: linear-gradient(135deg, rgba(16, 31, 45, 0.95), rgba(11, 23, 35, 0.95)) !important;
    border: 1px solid var(--fg-line) !important;
    border-radius: 9px !important;
    padding: 16px 20px !important;
    margin-top: 10px !important;
    box-shadow: 0 10px 26px rgba(0,0,0,.19), inset 0 1px 0 rgba(255,255,255,.025) !important;
}
.fg-spec-header {
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    margin-bottom: 10px !important;
    padding-bottom: 8px !important;
    border-bottom: 1px solid rgba(167,196,214,.11) !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    color: var(--fg-cyan) !important;
}
.fg-spec-dot {
    display: inline-block !important;
    width: 6px !important;
    height: 6px !important;
    border-radius: 50% !important;
    background: var(--fg-cyan) !important;
    box-shadow: 0 0 8px rgba(66,216,205,.6) !important;
}
.fg-spec-row {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    padding: 9px 0 !important;
    border-bottom: 1px solid rgba(167,196,214,.11) !important;
}
.fg-spec-row:last-child {
    border-bottom: none !important;
    padding-bottom: 0 !important;
}
.fg-spec-label {
    color: var(--fg-muted) !important;
    font-size: 11px !important;
    font-weight: 500 !important;
    letter-spacing: 0.5px !important;
    text-transform: uppercase !important;
}
.fg-spec-value {
    color: #d9e9ed !important;
    font-family: var(--fg-mono) !important;
    font-size: 11px !important;
    font-weight: 600 !important;
}

/* Model findings: intentionally strong only when a decision is present. */
.fg-result-card {
    background: linear-gradient(135deg, rgba(19,39,55,.98), rgba(12,26,38,.98)) !important;
    border: 1px solid var(--fg-line) !important; border-left-width: 3px !important; border-radius: 9px !important;
    padding: 21px 22px !important; margin-bottom: 14px !important; position: relative; overflow: hidden;
    box-shadow: 0 10px 26px rgba(0,0,0,.19), inset 0 1px 0 rgba(255,255,255,.025) !important;
    transition: transform .18s ease, border-color .18s ease, box-shadow .18s ease !important;
}
.fg-result-card::after { display: none; }
.fg-result-card:hover { transform: translateY(-2px); border-color: rgba(143,208,218,.35) !important; box-shadow: 0 15px 32px rgba(0,0,0,.27) !important; }
.fg-verdict-authentic { border-left-color: var(--fg-green) !important; }
.fg-verdict-forged { border-left-color: var(--fg-red) !important; }
.fg-model-name { color: var(--fg-paper); font-size: 17px; letter-spacing: -.2px; }
.fg-model-badge { color: #a9c0ca; background: rgba(137,187,200,.08); border-color: rgba(137,187,200,.16); border-radius: 4px; }
.fg-verdict-pill { border-radius: 4px; font-family: var(--fg-mono); font-size: 11px; letter-spacing: .65px; }
.fg-verdict-pill-authentic { color: var(--fg-green); background: rgba(84,210,155,.09); border-color: rgba(84,210,155,.3); }
.fg-verdict-pill-forged { color: var(--fg-red); background: rgba(255,101,116,.09); border-color: rgba(255,101,116,.3); }
.fg-confidence { font-family: var(--fg-mono); font-size: 27px; }
.fg-conf-authentic { color: var(--fg-green); }.fg-conf-forged { color: var(--fg-red); }
.fg-latency { color: #99b7c3; font-family: var(--fg-mono); }

/* Analytics */
.fg-chart-card {
    background: linear-gradient(135deg, #102233, #0e1d2b) !important; border: 1px solid var(--fg-line) !important;
    border-radius: 10px !important; padding: 24px !important; box-shadow: 0 16px 38px rgba(0,0,0,.2) !important;
    animation: fg-enter .5s cubic-bezier(.2,.8,.2,1) both;
}
.fg-chart-legend { align-items: center; flex-wrap: wrap; }
.fg-signal-key { display: inline-flex; align-items: center; gap: 6px; color: var(--fg-muted); white-space: nowrap; }
.fg-signal-key > span { width: 8px; height: 8px; border-radius: 2px; display: inline-block; }
.fg-signal-key-fast > span { background: var(--fg-green); box-shadow: 0 0 8px rgba(84,210,155,.42); }
.fg-signal-key-slow > span { background: var(--fg-amber); box-shadow: 0 0 8px rgba(245,189,104,.42); }
.fg-chart-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px; align-items: stretch; }
.fg-chart-subpanel { background: rgba(5,16,25,.43); border: 1px solid rgba(164,208,221,.1); border-radius: 7px; padding: 17px; animation: fg-enter .55s cubic-bezier(.2,.8,.2,1) both; }
.fg-chart-subpanel:nth-child(2) { animation-delay: .08s; }
.fg-chart-title { color: #dcebee; font-size: 13px; display: flex; justify-content: space-between; align-items: center; gap: 12px; }
.fg-bar-row { margin-bottom: 13px; }
.fg-bar-header { display: flex; justify-content: space-between; align-items: center; gap: 12px; margin-bottom: 6px; font-size: 12px; }
.fg-bar-label { color: #c6d8de; }.fg-bar-val { font-family: var(--fg-mono); font-weight: 700; white-space: nowrap; }.fg-bar-track { height: 6px; background: rgba(159,198,208,.12); border-radius: 99px; }
.fg-bar-fill { display: block; height: 100%; border-radius: 99px; box-shadow: 0 0 12px rgba(66,216,205,.18); transform-origin: left; animation: fg-bar-grow .9s cubic-bezier(.2,.8,.2,1) both; }
.fg-bar-row:nth-child(3) .fg-bar-fill { animation-delay: .08s; }.fg-bar-row:nth-child(4) .fg-bar-fill { animation-delay: .16s; }.fg-bar-row:nth-child(5) .fg-bar-fill { animation-delay: .24s; }
.fg-chart-subpanel:first-child .fg-bar-row:nth-of-type(2) .fg-bar-fill { background: linear-gradient(90deg, #159c96, #42d8cd) !important; }
.fg-chart-subpanel:first-child .fg-bar-row:nth-of-type(3) .fg-bar-fill { background: linear-gradient(90deg, #5b73d8, #8aa2ff) !important; }
.fg-chart-subpanel:first-child .fg-bar-row:nth-of-type(4) .fg-bar-fill { background: linear-gradient(90deg, #4b6174, #7892a8) !important; }
.fg-chart-subpanel:nth-child(2) .fg-bar-row:nth-of-type(2) .fg-bar-fill { background: linear-gradient(90deg, #159c96, #42d8cd) !important; }
.fg-chart-subpanel:nth-child(2) .fg-bar-row:nth-of-type(3) .fg-bar-fill { background: linear-gradient(90deg, #268f9a, #49c7d1) !important; }
.fg-chart-subpanel:nth-child(2) .fg-bar-row:nth-of-type(4) .fg-bar-fill { background: linear-gradient(90deg, #bd7d2d, #f5b94f) !important; }
.fg-chart-insight { color: var(--fg-dim); border-color: rgba(164,208,221,.1); }
.fg-metric-top { color: var(--fg-cyan) !important; background: rgba(66,216,205,.09) !important; border-color: rgba(66,216,205,.28) !important; border-radius: 4px !important; }
.fg-metric-fast { color: var(--fg-green) !important; background: rgba(84,210,155,.09) !important; border-color: rgba(84,210,155,.27) !important; border-radius: 4px !important; }
.fg-metric-slow { color: var(--fg-amber) !important; background: rgba(245,189,104,.09) !important; border: 1px solid rgba(245,189,104,.27) !important; border-radius: 4px !important; padding: 3px 6px !important; }

.fg-section-gap { margin-top: 38px; margin-bottom: 15px; }
.fg-section-title { color: #e3f0f2; font-size: 15px; font-weight: 650; letter-spacing: -.1px; }
.fg-section-title::before { content:""; display:inline-block; width: 5px; height: 5px; margin: 0 9px 2px 0; border-radius:50%; background: var(--fg-cyan); box-shadow: 0 0 10px rgba(66,216,205,.6); }
.fg-metrics-table { width: 100%; border-collapse: separate; border-spacing: 0; overflow: hidden; background: #0f202f; border: 1px solid var(--fg-line); border-radius: 8px; box-shadow: 0 10px 24px rgba(0,0,0,.14); animation: fg-enter .5s cubic-bezier(.2,.8,.2,1) .06s both; }
.fg-metrics-table thead tr { background: linear-gradient(90deg, #183449, #142b3e); }
.fg-metrics-table th { padding: 13px 14px; color: #b8d7df; font-size: 11px; letter-spacing: .75px; border-bottom: 1px solid var(--fg-line); white-space: nowrap; }
.fg-metrics-table th:not(:last-child), .fg-metrics-table td:not(:last-child) { border-right: 1px solid rgba(164,208,221,.075); }
.fg-metrics-table td { padding: 13px 14px; color: #dcebed; border-bottom: 1px solid rgba(164,208,221,.09); font-family: var(--fg-mono); font-size: 12px; white-space: nowrap; transition: background-color .18s ease, color .18s ease; }
.fg-metrics-table td.arch-cell { color: var(--fg-paper); font-family: var(--fg-sans); font-weight: 650; }
.fg-metrics-table tbody tr.fg-standard-row { background: rgba(66,216,205,.03); }
.fg-metrics-table tbody tr.fg-compressed-row { background: rgba(115,168,255,.022); }
.fg-metrics-table tbody tr.fg-model-start td { border-top: 1px solid rgba(66,216,205,.19); }
.fg-metrics-table tbody tr.fg-model-start:first-child td { border-top: 0; }
.fg-metrics-table tbody tr.fg-standard-row td:first-child { box-shadow: inset 3px 0 0 rgba(66,216,205,.62); }
.fg-metrics-table tbody tr.fg-compressed-row td:first-child { box-shadow: inset 3px 0 0 rgba(115,168,255,.42); }
.fg-metrics-table tbody tr { transition: background .18s ease, transform .18s ease, box-shadow .18s ease; }
.fg-metrics-table tbody tr:hover { background: rgba(66,216,205,.075) !important; transform: translateY(-1px); box-shadow: 0 7px 18px rgba(0,0,0,.13); }
.fg-metrics-table tbody tr:hover td { color: #f2fbfc; }
.fg-metrics-table tbody tr:nth-child(1) td { background-image: linear-gradient(90deg, rgba(66,216,205,.055), transparent 44%); }
.fg-metrics-table tbody td:nth-child(3), .fg-metrics-table tbody td:nth-child(6) { color: #b8f5ef; }
.fg-metrics-table tbody td:nth-child(7) { color: #b8d7df; }
.fg-pending { color: var(--fg-dim); }.fg-metrics-table tbody tr:has(td.fg-pending) { background: rgba(144,163,174,.035) !important; }

/* Matrix, dataset summary, and numeric treatment. Inline markup remains unchanged; these rules only restyle it. */
div[style*="background-color: #1C2333"] { background-color: #102131 !important; border-color: var(--fg-line) !important; border-radius: 9px !important; }
div[style*="font-size: 15px; font-weight: 700; color: #FFFFFF"] { color: var(--fg-paper) !important; }
div[style*="font-family: 'JetBrains Mono'"] { font-family: var(--fg-mono) !important; }
div[style*="color: #2DD4BF"] { color: var(--fg-cyan) !important; }
td[style*="rgba(16, 185, 129"] { background: rgba(84,210,155,.09) !important; border-color: rgba(84,210,155,.27) !important; }
td[style*="rgba(239, 68, 68"] { background: rgba(255,101,116,.08) !important; border-color: rgba(255,101,116,.26) !important; }
td div[style*="color: #10B981"] { color: var(--fg-green) !important; }
td div[style*="color: #EF4444"] { color: var(--fg-red) !important; }

.fg-advisory {
    background: rgba(245, 189, 104, 0.08) !important;
    border: 1px solid rgba(245, 189, 104, 0.28) !important;
    border-left: 4px solid var(--fg-amber) !important;
    border-radius: 8px !important;
    padding: 12px 18px !important;
    margin: 18px 0 22px 0 !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2) !important;
    box-sizing: border-box !important;
    width: 100% !important;
}
.fg-advisory-inner {
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
}
.fg-advisory-tag {
    display: inline-block !important;
    padding: 3px 8px !important;
    background: rgba(245, 189, 104, 0.16) !important;
    border: 1px solid rgba(245, 189, 104, 0.38) !important;
    border-radius: 4px !important;
    font-family: var(--fg-mono) !important;
    font-size: 10px !important;
    font-weight: 700 !important;
    letter-spacing: 0.8px !important;
    color: var(--fg-amber) !important;
    text-transform: uppercase !important;
    white-space: nowrap !important;
}
.fg-advisory-text {
    color: #e6eff0 !important;
    font-size: 12px !important;
    line-height: 1.5 !important;
    font-weight: 450 !important;
}

/* Select and popover controls */
div[data-testid="stSelectbox"] { max-width: 340px !important; }
div[data-testid="stSelectbox"] > div > div {
    background: #102332 !important; border-color: rgba(152,208,218,.25) !important; border-radius: 6px !important;
    color: var(--fg-paper) !important; font-family: var(--fg-sans) !important; box-shadow: none !important;
}
div[data-testid="stSelectbox"] > div > div:hover, div[data-testid="stSelectbox"] > div > div:focus-within { border-color: var(--fg-cyan) !important; box-shadow: 0 0 0 3px rgba(66,216,205,.1) !important; }
div[data-testid="stSelectbox"] svg { fill: var(--fg-cyan) !important; }
ul[data-testid="stSelectboxOptionsList"], div[data-baseweb="popover"] > div, div[data-baseweb="menu"] { background: #102332 !important; border-color: rgba(152,208,218,.25) !important; }
li[role="option"] { color: var(--fg-paper) !important; font-family: var(--fg-sans) !important; }
li[role="option"]:hover, li[role="option"][aria-selected="true"] { background: rgba(66,216,205,.11) !important; }

@keyframes fg-enter { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
@keyframes fg-bar-grow { from { transform: scaleX(0); } to { transform: scaleX(1); } }
@keyframes fg-loading-sweep { 0% { background-position: -42% 0; } 100% { background-position: 142% 0; } }

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { animation-duration: .01ms !important; animation-iteration-count: 1 !important; transition-duration: .01ms !important; }
}

::-webkit-scrollbar { width: 7px; height: 7px; }
::-webkit-scrollbar-track { background: #08111b; }
::-webkit-scrollbar-thumb { background: #29475a; border: 2px solid #08111b; border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: #46748a; }

@media (max-width: 768px) {
    .fg-chart-grid { grid-template-columns: 1fr; gap: 14px; }
    .fg-metrics-table { display: block; overflow-x: auto; white-space: nowrap; }
    .fg-result-card { padding: 18px !important; }
}
</style>
"""
