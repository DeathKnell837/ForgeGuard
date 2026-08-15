"""
ForgeGuard Premium UI Components — HTML/SVG Templates
=====================================================
Pure CSS/SVG components for the premium redesign.
Uses textwrap.dedent to ensure Streamlit's markdown parser never treats HTML/SVG as code blocks.
"""

import textwrap


def svg_confidence_gauge(confidence_pct, verdict_color, verdict_label):
    """
    Renders a clean SVG circular confidence gauge (speedometer style).
    """
    arc_length = 376.99
    filled = arc_length * (confidence_pct / 100.0)
    gap = arc_length - filled
    glow_opacity = min(0.6, confidence_pct / 150.0)
    
    # User-friendly simple label
    simple_label = "GENUINE" if "AUTH" in verdict_label.upper() else "EDITED / FAKE"
    
    html = f"""<div class="gauge-container">
<svg viewBox="0 0 200 200" class="gauge-svg">
<defs>
<filter id="gaugeGlow">
<feGaussianBlur stdDeviation="4" result="blur"/>
<feFlood flood-color="{verdict_color}" flood-opacity="{glow_opacity}"/>
<feComposite in2="blur" operator="in"/>
<feMerge>
<feMergeNode/>
<feMergeNode in="SourceGraphic"/>
</feMerge>
</filter>
<linearGradient id="gaugeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
<stop offset="0%" style="stop-color:{verdict_color};stop-opacity:0.4"/>
<stop offset="100%" style="stop-color:{verdict_color};stop-opacity:1"/>
</linearGradient>
</defs>
<circle cx="100" cy="100" r="80" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="8" stroke-dasharray="{arc_length} {502.65 - arc_length}" stroke-dashoffset="-{502.65 * 0.125}" stroke-linecap="round" transform="rotate(0 100 100)"/>
<circle cx="100" cy="100" r="80" fill="none" stroke="url(#gaugeGrad)" stroke-width="8" stroke-dasharray="{filled} {gap + (502.65 - arc_length)}" stroke-dashoffset="-{502.65 * 0.125}" stroke-linecap="round" filter="url(#gaugeGlow)" class="gauge-arc"/>
<g stroke="rgba(255,255,255,0.15)" stroke-width="1">
<line x1="100" y1="28" x2="100" y2="22" transform="rotate(-135 100 100)"/>
<line x1="100" y1="28" x2="100" y2="24" transform="rotate(-108 100 100)"/>
<line x1="100" y1="28" x2="100" y2="24" transform="rotate(-81 100 100)"/>
<line x1="100" y1="28" x2="100" y2="22" transform="rotate(-54 100 100)"/>
<line x1="100" y1="28" x2="100" y2="24" transform="rotate(-27 100 100)"/>
<line x1="100" y1="28" x2="100" y2="22" transform="rotate(0 100 100)"/>
<line x1="100" y1="28" x2="100" y2="24" transform="rotate(27 100 100)"/>
<line x1="100" y1="28" x2="100" y2="24" transform="rotate(54 100 100)"/>
<line x1="100" y1="28" x2="100" y2="22" transform="rotate(81 100 100)"/>
<line x1="100" y1="28" x2="100" y2="24" transform="rotate(108 100 100)"/>
<line x1="100" y1="28" x2="100" y2="22" transform="rotate(135 100 100)"/>
</g>
<text x="100" y="92" text-anchor="middle" fill="{verdict_color}" font-family="'JetBrains Mono', 'IBM Plex Mono', monospace" font-size="28" font-weight="700">{confidence_pct:.1f}%</text>
<text x="100" y="115" text-anchor="middle" fill="{verdict_color}" font-family="'JetBrains Mono', 'IBM Plex Mono', monospace" font-size="9" font-weight="600" letter-spacing="2" opacity="0.9">{simple_label}</text>
</svg>
</div>"""
    return textwrap.dedent(html).strip()


def premium_verdict_stamp(verdict_text, stamp_class, sub_reason, verdict_color, verdict_label, confidence, model_name, latency_ms):
    """
    Renders the stamp verdict with plain-English summary.
    """
    clean_verdict = "VERIFIED GENUINE" if "AUTH" in verdict_label.upper() else "EDITED / FAKE RECEIPT"
    
    html = f"""<div class="stamp-container">
<div class="stamp-box {stamp_class}">
<div class="stamp-ring"></div>
<div class="stamp-title">{verdict_text}</div>
<div class="stamp-sub">{sub_reason}</div>
</div>
<div class="stamp-meta-bar">
<span>Result: <strong style="color: {verdict_color};">{clean_verdict}</strong></span>
<span>Certainty: <strong style="color: {verdict_color};">{confidence * 100:.1f}%</strong></span>
<span>Model: <strong style="color: #F8FAFC;">{model_name}</strong></span>
<span>Speed: <strong style="color: #2DD4BF;">{latency_ms:.1f} ms</strong></span>
</div>
</div>"""
    return textwrap.dedent(html).strip()


def premium_metric_card(value, label, color="#2DD4BF", icon_type="bar"):
    """
    Renders a clean metric card with mini sparkline SVG.
    """
    if icon_type == "bar":
        sparkline = """<svg width="32" height="16" viewBox="0 0 32 16"><rect x="0" y="8" width="5" height="8" rx="1" fill="rgba(255,255,255,0.15)"/><rect x="7" y="4" width="5" height="12" rx="1" fill="rgba(255,255,255,0.2)"/><rect x="14" y="6" width="5" height="10" rx="1" fill="rgba(255,255,255,0.15)"/><rect x="21" y="2" width="5" height="14" rx="1" fill="rgba(255,255,255,0.25)"/><rect x="28" y="0" width="4" height="16" rx="1" fill="rgba(255,255,255,0.12)"/></svg>"""
    else:
        sparkline = """<svg width="32" height="16" viewBox="0 0 32 16"><polyline points="0,14 8,8 16,10 24,3 32,6" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/></svg>"""
    
    html = f"""<div class="metric-card" style="border-top: 2px solid {color};">
<div style="display: flex; justify-content: space-between; align-items: center; width: 100%; margin-bottom: 6px;">
<div class="metric-text">{label}</div>
{sparkline}
</div>
<div class="metric-num" style="color: {color};">{value}</div>
</div>"""
    return textwrap.dedent(html).strip()


def premium_arch_card(name, score, latency, params, is_active=False, is_forged=False):
    """
    Renders an architecture comparison card with simple plain-English terms.
    """
    score_pct = score * 100
    bar_color = "#F87171" if is_forged else "#34D399"
    active_border = "border-left: 3px solid #2DD4BF;" if is_active else ""
    active_badge = '<span style="background: rgba(45,212,191,0.15); color: #2DD4BF; font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; font-weight: 700;">CURRENT</span>' if is_active else ""
    verdict_badge = "FAKE" if is_forged else "REAL"
    badge_color = "#F87171" if is_forged else "#34D399"
    
    html = f"""<div class="glass-panel-matrix" style="{active_border}">
<div>
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
<div class="serif-header" style="font-size: 1.05rem; color: #F8FAFC;">{name}</div>
<span style="color: {badge_color}; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; font-weight: 700;">[{verdict_badge}]</span>
</div>
<div style="color: #64748B; font-size: 0.75rem; margin-bottom: 0.75rem;">{active_badge}</div>
<div style="font-family: 'JetBrains Mono', monospace; font-size: 1.6rem; font-weight: 700; color: {badge_color}; margin-bottom: 0.5rem;">{score_pct:.1f}%</div>
<div style="width: 100%; height: 4px; background: rgba(255,255,255,0.06); border-radius: 4px; overflow: hidden; margin-bottom: 0.75rem;">
<div style="width: {score_pct}%; height: 100%; background: linear-gradient(90deg, {bar_color}88, {bar_color}); border-radius: 4px; transition: width 1s ease;"></div>
</div>
</div>
<div style="display: flex; justify-content: space-between; align-items: center;">
<div style="font-family: 'JetBrains Mono', monospace; font-size: 0.74rem; color: #64748B;">
<span style="color: #94A3B8;">Speed:</span> <strong style="color: #2DD4BF;">{latency}ms</strong>
</div>
<div style="font-family: 'JetBrains Mono', monospace; font-size: 0.74rem; color: #64748B;">
<span style="color: #94A3B8;">Model Size:</span> <strong style="color: #F8FAFC;">{params}</strong>
</div>
</div>
</div>"""
    return textwrap.dedent(html).strip()


def premium_header_bar(svg_shield):
    """
    Renders the header brand bar.
    """
    html = f"""<div class="navbar-brand">
<div class="brand-title">
<div class="brand-shield">{svg_shield}</div>
<span>ForgeGuard</span>
<span class="version-pill">v2.0</span>
</div>
<div>
<span class="badge-gold">NDMC CITE BSCS THESIS</span>
</div>
</div>
<div class="shimmer-line"></div>"""
    return textwrap.dedent(html).strip()


def premium_hero_banner():
    """
    Renders the hero dashboard banner with simple, clear English.
    """
    html = """<div class="glass-panel hero-panel">
<div class="eyebrow-gold" style="display: flex; align-items: center; gap: 8px;">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#C9A15F" stroke-width="2.5" stroke-linecap="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
DIGITAL RECEIPT VERIFICATION SYSTEM
</div>
<div class="serif-header" style="font-size: 1.65rem; color: #F8FAFC; margin-bottom: 0.5rem; line-height: 1.2;">
Fake Receipt Scanner & Image Forensic Suite
</div>
<div style="color: #94A3B8; font-size: 0.88rem; line-height: 1.6; margin-bottom: 1rem; max-width: 820px;">
An AI-powered system that scans GCash and Maya receipt screenshots to catch fake or edited proof of payment. 
It uses <strong>Error Level Analysis (ELA)</strong> and Convolutional Neural Networks to find edited text, altered amounts, and tampered reference numbers.
</div>
<div style="display: flex; gap: 1.5rem; flex-wrap: wrap; align-items: center;">
<div class="info-chip">
<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#94A3B8" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
<span><strong style="color: #CBD5E1;">Authors:</strong> Rogie P. Bacanto & Daniela S. Ungab</span>
</div>
<div class="info-chip">
<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#94A3B8" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 1 4 3 6 3s6-2 6-3v-5"/></svg>
<span><strong style="color: #CBD5E1;">Adviser:</strong> Ms. Doris Ann Mariano</span>
</div>
<div class="info-chip">
<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#C9A15F" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
<span><strong style="color: #C9A15F;">School:</strong> Notre Dame of Midsayap College</span>
</div>
</div>
</div>"""
    return textwrap.dedent(html).strip()


def inference_mode_badge(inference_mode, mode_color):
    """
    Renders the inference engine mode badge.
    """
    mode_desc = "Trained neural network active" if inference_mode == "CNN" else "Error analysis scanner active"
    icon = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>' if inference_mode == "CNN" else '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>'
    
    html = f"""<div style="display: flex; align-items: center; justify-content: center; gap: 8px; padding: 6px 16px; background: rgba({int(mode_color[1:3],16)},{int(mode_color[3:5],16)},{int(mode_color[5:7],16)},0.08); border: 1px solid rgba({int(mode_color[1:3],16)},{int(mode_color[3:5],16)},{int(mode_color[5:7],16)},0.25); border-radius: 8px; margin: 0.5rem auto 1rem auto; width: fit-content;">
<span style="color: {mode_color};">{icon}</span>
<span style="font-family: 'JetBrains Mono', monospace; font-size: 0.74rem; color: {mode_color}; letter-spacing: 0.5px;">
AI SCANNER: <strong>{inference_mode}</strong> — {mode_desc}
</span>
</div>"""
    return textwrap.dedent(html).strip()


def telemetry_card_html(title, value, subtitle, color, svg_path):
    """
    Renders an individual telemetry card with clear, simple labels.
    """
    html = f"""<div style="background: linear-gradient(135deg, #090E1A 0%, #0D1627 100%); border: 1px solid rgba(255, 255, 255, 0.08); border-left: 3.5px solid {color}; border-radius: 14px; padding: 1.1rem 1.2rem; box-shadow: 0 6px 25px rgba(0, 0, 0, 0.5); min-height: 105px; display: flex; flex-direction: column; justify-content: space-between;">
<div style="display: flex; justify-content: space-between; align-items: center;">
<div style="font-family: 'Rajdhani', sans-serif; font-size: 0.82rem; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.8px;">{title}</div>
<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{svg_path}</svg>
</div>
<div style="font-family: 'JetBrains Mono', monospace; font-size: 1.7rem; font-weight: 800; color: {color}; letter-spacing: -0.5px; margin: 4px 0;">{value}</div>
<div style="font-size: 0.74rem; color: #64748B; font-family: 'JetBrains Mono', monospace;">{subtitle}</div>
</div>"""
    return textwrap.dedent(html).strip()



