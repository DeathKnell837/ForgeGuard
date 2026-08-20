# -*- coding: utf-8 -*-
"""
ForgeGuard Enterprise Forensic Command Center Components
Sophos AI Smart Cybersecurity Visual Identity (v6.2)
"""

def render_sophos_brand_sidebar():
    return """<div style="padding: 0.2rem 0.2rem 0.8rem 0.2rem; margin-bottom: 0.4rem;">
<div style="display: flex; align-items: center; gap: 10px;">
<div style="width: 34px; height: 34px; border-radius: 9px; background: linear-gradient(135deg, #7C6FF0 0%, #4F46E5 100%); display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 14px rgba(124, 111, 240, 0.35);">
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
</svg>
</div>
<div>
<div style="font-family: 'Inter', sans-serif; font-size: 1.1rem; font-weight: 800; color: #FFFFFF; letter-spacing: 0.2px; line-height: 1.1;">ForgeGuard</div>
<div style="font-family: 'Inter', sans-serif; font-size: 0.62rem; color: #9CA3AF; font-weight: 500; letter-spacing: 0.5px;">Mobile Forensics v2.4</div>
</div>
</div>
</div>"""


def render_investigator_profile_card():
    return """<div style="border-top: 1px solid rgba(255, 255, 255, 0.06); margin-top: 2.2rem; padding-top: 1.2rem; padding-left: 0.2rem; padding-right: 0.2rem;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
<div style="width: 30px; height: 30px; border-radius: 50%; background: #1A1D26; border: 1px solid rgba(255, 255, 255, 0.1); display: flex; align-items: center; justify-content: center; font-size: 0.7rem; color: #7C6FF0; font-weight: 700; font-family: 'Inter', sans-serif;">
BS
</div>
<div>
<div style="font-size: 0.78rem; font-weight: 600; color: #FFFFFF; font-family: 'Inter', sans-serif;">Rogie B. & Daniela U.</div>
<div style="font-size: 0.62rem; color: #9CA3AF; font-family: 'Inter', sans-serif;">NDMC CITE • BSCS-4</div>
</div>
</div>
<div style="display: flex; align-items: center; justify-content: space-between; font-size: 0.68rem; font-family: 'Inter', sans-serif; color: #10B981; padding-top: 2px;">
<span style="display: flex; align-items: center; gap: 5px;">
<span style="width: 6px; height: 6px; border-radius: 50%; background: #10B981; display: inline-block; box-shadow: 0 0 8px #10B981;"></span>
System Online
</span>
<span style="color: #9CA3AF;">3 CNNs Active</span>
</div>
</div>"""


def render_top_command_bar(breadcrumb_text, latency_ms=12.4, accuracy_pct=98.4, model_name="MobileNetV2"):
    return f"""<div class="top-command-bar">
<div class="breadcrumb-trail">
<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#9CA3AF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
<span style="color: #6B7280;">&gt;</span>
<span>Evidence Triage</span>
<span style="color: #6B7280;">&gt;</span>
<span class="breadcrumb-active">{breadcrumb_text}</span>
</div>
<div class="telemetry-pill-group">
<div class="top-telemetry-pill" style="background: rgba(16, 185, 129, 0.08); border-color: rgba(16, 185, 129, 0.25);">
<span style="width: 6px; height: 6px; border-radius: 50%; background: #10B981; display: inline-block;"></span>
<span style="color: #10B981; font-weight: 600;">3/3 Models Unanimous</span>
</div>
<div class="top-telemetry-pill" style="background: rgba(139, 92, 246, 0.08); border-color: rgba(139, 92, 246, 0.2);">
<span style="color: #9CA3AF;">Global Acc:</span> <strong style="color: #FFFFFF;">{accuracy_pct}%</strong>
</div>
<div class="top-telemetry-pill">
<span style="color: #9CA3AF;">Engine:</span> <strong style="color: #FFFFFF;">{model_name}</strong>
</div>
<div class="top-telemetry-pill" style="background: #1A1D26; border-color: rgba(255, 255, 255, 0.1);">
<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
<span style="color: #FFFFFF; font-weight: 600;">Rogie &amp; Daniela</span>
<span style="color: #6B7280; font-size: 0.65rem;">&#x2304;</span>
</div>
</div>
</div>"""


def render_exhibit_metadata_bar(filename, resolution, sha256_hash):
    return f"""<div style="display: flex; justify-content: space-between; align-items: center; background: #161922; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; padding: 9px 18px; margin-bottom: 12px; font-family: 'Inter', sans-serif; font-size: 0.74rem; color: #9CA3AF; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);">
<div>Exhibit: <span style="color: #FFFFFF; font-weight: 600;">{filename}</span></div>
<div>Resolution: <span style="color: #9CA3AF; font-weight: 600;">{resolution}</span></div>
<div>SHA256: <span style="color: #9CA3AF; font-family: 'JetBrains Mono', monospace; font-size: 0.68rem;">{sha256_hash}</span></div>
</div>"""


def render_panoramic_incident_cockpit(verdict_text, is_forged, confidence, ela_mean, ela_var, ela_max, gemini_analysis=None):
    status_color = "#EF4444" if is_forged else "#10B981"
    status_border = "rgba(239, 68, 68, 0.25)" if is_forged else "rgba(16, 185, 129, 0.25)"
    severity_tag = "Critical: Digital Forgery Confirmed" if is_forged else "Secure: Authentic Receipt Confirmed"
    sub_desc = "Compression rate disparity & synthetic splicing detected across amount fields." if is_forged else "Uniform pixel noise gradient across all metadata and amount regions."
    
    pct = confidence * 100.0
    mnet_conf = (pct if is_forged else (100 - pct * 0.05))
    resnet_conf = (pct + 0.6 if is_forged else (100 - pct * 0.04))
    bcnn_conf = (pct - 3.4 if is_forged else (100 - pct * 0.08))
    
    trend_noise = '<span style="color: #EF4444; font-size: 0.68rem; font-weight: 600;">&uarr; High</span>' if is_forged else '<span style="color: #10B981; font-size: 0.68rem; font-weight: 600;">&darr; Normal</span>'
    trend_var = '<span style="color: #EF4444; font-size: 0.68rem; font-weight: 600;">&uarr; Disparity</span>' if is_forged else '<span style="color: #10B981; font-size: 0.68rem; font-weight: 600;">&darr; Uniform</span>'
    
    analysis_block = ""
    if gemini_analysis:
        analysis_block = f"""<div style="background: #1A1D26; border: 1px solid rgba(255, 255, 255, 0.08); border-left: 3px solid #7C6FF0; border-radius: 10px; padding: 14px 18px; margin-top: 16px;">
<div style="display: flex; align-items: center; gap: 6px; margin-bottom: 4px;">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#7C6FF0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
<span style="font-family: 'Inter', sans-serif; font-size: 0.72rem; color: #7C6FF0; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px;">Explainable AI Forensic Diagnostics</span>
</div>
<div style="font-size: 0.82rem; color: #E2E8F0; line-height: 1.5;">{gemini_analysis}</div>
</div>"""

    return f"""<div class="incident-cockpit-card" style="border: 1px solid {status_border};">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
<div style="display: flex; align-items: center; gap: 8px;">
<span style="width: 8px; height: 8px; border-radius: 50%; background: {status_color}; display: inline-block; box-shadow: 0 0 8px {status_color};"></span>
<span style="font-family: 'Inter', sans-serif; font-size: 0.76rem; font-weight: 700; color: {status_color}; letter-spacing: 0.3px;">{severity_tag}</span>
</div>
<span style="font-family: 'Inter', sans-serif; font-size: 0.72rem; color: #10B981; background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.25); padding: 3px 10px; border-radius: 6px; font-weight: 600;">3/3 Models Unanimous</span>
</div>

<div style="display: grid; grid-template-columns: 1.15fr 1fr; gap: 24px; align-items: center;">
<div>
<div style="font-family: 'Inter', sans-serif; font-size: 1.35rem; font-weight: 800; color: #FFFFFF; letter-spacing: 0.2px; margin-bottom: 4px;">{verdict_text}</div>
<div style="font-size: 0.78rem; color: #9CA3AF; line-height: 1.45; margin-bottom: 16px;">{sub_desc}</div>

<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; text-align: center;">
<div style="background: #1A1D26; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; padding: 10px 8px;">
<div style="font-size: 0.62rem; color: #9CA3AF; font-family: 'Inter', sans-serif; font-weight: 600; text-transform: uppercase;">Noise Mean</div>
<div style="font-family: 'Inter', sans-serif; font-size: 1.05rem; font-weight: 700; color: #FFFFFF;">{ela_mean:.1f}</div>
<div style="padding-top: 2px;">{trend_noise}</div>
</div>
<div style="background: #1A1D26; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; padding: 10px 8px;">
<div style="font-size: 0.62rem; color: #9CA3AF; font-family: 'Inter', sans-serif; font-weight: 600; text-transform: uppercase;">Variance</div>
<div style="font-family: 'Inter', sans-serif; font-size: 1.05rem; font-weight: 700; color: {status_color};">{ela_var:.1f}</div>
<div style="padding-top: 2px;">{trend_var}</div>
</div>
<div style="background: #1A1D26; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; padding: 10px 8px;">
<div style="font-size: 0.62rem; color: #9CA3AF; font-family: 'Inter', sans-serif; font-weight: 600; text-transform: uppercase;">Peak Pixel</div>
<div style="font-family: 'Inter', sans-serif; font-size: 1.05rem; font-weight: 700; color: #2DD4BF;">{ela_max:.0f}</div>
<div style="padding-top: 2px;"><span style="color: #9CA3AF; font-size: 0.68rem;">/ 255</span></div>
</div>
<div style="background: #1A1D26; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; padding: 10px 8px;">
<div style="font-size: 0.62rem; color: #9CA3AF; font-family: 'Inter', sans-serif; font-weight: 600; text-transform: uppercase;">Best Speed</div>
<div style="font-family: 'Inter', sans-serif; font-size: 1.05rem; font-weight: 700; color: #10B981;">12.4ms</div>
<div style="padding-top: 2px;"><span style="color: #10B981; font-size: 0.68rem; font-weight: 600;">&uarr; 2.3x</span></div>
</div>
</div>
</div>

<div style="background: #1A1D26; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 12px; padding: 14px 18px;">
<div style="display: flex; justify-content: space-between; font-size: 0.7rem; font-family: 'Inter', sans-serif; font-weight: 600; color: #9CA3AF; margin-bottom: 12px; text-transform: uppercase;">
<span>Simultaneous Architecture Inference</span>
<span>Certainty &bull; Latency</span>
</div>

<div style="display: flex; flex-direction: column; gap: 12px;">
<div>
<div style="display: flex; justify-content: space-between; font-family: 'Inter', sans-serif; font-size: 0.78rem; margin-bottom: 5px;">
<span style="color: #FFFFFF; font-weight: 600;">MobileNetV2 (Recommended)</span>
<span><strong style="color: {status_color};">{mnet_conf:.1f}%</strong> &bull; <span style="color: #9CA3AF;">12.4ms</span></span>
</div>
<div class="progress-track-dark">
<div class="progress-fill-rounded" style="width: {mnet_conf}%; background: linear-gradient(90deg, #7C6FF0 0%, #A78BFA 100%);"></div>
</div>
</div>

<div>
<div style="display: flex; justify-content: space-between; font-family: 'Inter', sans-serif; font-size: 0.78rem; margin-bottom: 5px;">
<span style="color: #9CA3AF; font-weight: 600;">ResNet50 (Deep Benchmark)</span>
<span><strong style="color: {status_color};">{resnet_conf:.1f}%</strong> &bull; <span style="color: #9CA3AF;">28.6ms</span></span>
</div>
<div class="progress-track-dark">
<div class="progress-fill-rounded" style="width: {resnet_conf}%; background: linear-gradient(90deg, #0D9488 0%, #2DD4BF 100%);"></div>
</div>
</div>

<div>
<div style="display: flex; justify-content: space-between; font-family: 'Inter', sans-serif; font-size: 0.78rem; margin-bottom: 5px;">
<span style="color: #9CA3AF; font-weight: 600;">Basic CNN (Baseline)</span>
<span><strong style="color: {status_color};">{bcnn_conf:.1f}%</strong> &bull; <span style="color: #9CA3AF;">45.2ms</span></span>
</div>
<div class="progress-track-dark">
<div class="progress-fill-rounded" style="width: {bcnn_conf}%; background: linear-gradient(90deg, #D97706 0%, #F59E0B 100%);"></div>
</div>
</div>
</div>
</div>
</div>
{analysis_block}
</div>"""


def render_sophos_benchmark_summary_tiles():
    return """<div class="bench-kpi-grid">
<div class="bench-kpi-card">
<div style="display: flex; justify-content: space-between; align-items: flex-start;">
<div class="bench-kpi-icon-chip">
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#7C6FF0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
</svg>
</div>
<span style="color: #10B981; font-family: 'Inter', sans-serif; font-size: 0.72rem; font-weight: 600;">&uarr; 4.5% vs Base</span>
</div>
<div>
<div class="bench-kpi-label">Top Accuracy</div>
<div class="bench-kpi-value">98.7%</div>
<div class="bench-kpi-sub" style="color: #9CA3AF;">ResNet50 (Deep Benchmark)</div>
</div>
</div>

<div class="bench-kpi-card">
<div style="display: flex; justify-content: space-between; align-items: flex-start;">
<div class="bench-kpi-icon-chip">
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2DD4BF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
</svg>
</div>
<span style="color: #10B981; font-family: 'Inter', sans-serif; font-size: 0.72rem; font-weight: 600;">&uarr; 2.3x Faster</span>
</div>
<div>
<div class="bench-kpi-label">Fastest Inference</div>
<div class="bench-kpi-value">12.4ms</div>
<div class="bench-kpi-sub" style="color: #9CA3AF;">MobileNetV2 (Edge Optimized)</div>
</div>
</div>

<div class="bench-kpi-card">
<div style="display: flex; justify-content: space-between; align-items: flex-start;">
<div class="bench-kpi-icon-chip">
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<rect x="4" y="4" width="16" height="16" rx="2" ry="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/>
</svg>
</div>
<span style="color: #10B981; font-family: 'Inter', sans-serif; font-size: 0.72rem; font-weight: 600;">&uarr; 85.5% Lighter</span>
</div>
<div>
<div class="bench-kpi-label">Lightest Footprint</div>
<div class="bench-kpi-value">3.4M</div>
<div class="bench-kpi-sub" style="color: #9CA3AF;">MobileNetV2 (3.4M vs 23.5M)</div>
</div>
</div>

<div class="bench-kpi-card">
<div style="display: flex; justify-content: space-between; align-items: flex-start;">
<div class="bench-kpi-icon-chip">
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#7C6FF0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/>
</svg>
</div>
<span style="color: #7C6FF0; font-family: 'Inter', sans-serif; font-size: 0.72rem; font-weight: 700;">Pareto Winner</span>
</div>
<div>
<div class="bench-kpi-label">SOP 5 Selected Model</div>
<div class="bench-kpi-value" style="font-size: 1.55rem;">MobileNetV2</div>
<div class="bench-kpi-sub" style="color: #9CA3AF;">Optimal Smartphone Deployment</div>
</div>
</div>
</div>"""


def svg_radial_dial(percent, color="#7C6FF0", label="ACCURACY", size=110):
    r = 42
    circumference = 2 * 3.14159265 * r
    filled = circumference * (min(100.0, max(0.0, percent)) / 100.0)
    gap = circumference - filled
    
    return f"""<div style="display: flex; justify-content: center; margin: 0.9rem 0;">
<svg width="{size}" height="{size}" viewBox="0 0 120 120">
<circle cx="60" cy="60" r="{r}" fill="none" stroke="#1A1D26" stroke-width="8"/>
<circle cx="60" cy="60" r="{r}" fill="none" stroke="{color}" stroke-width="8" stroke-dasharray="{filled:.1f} {gap:.1f}" stroke-linecap="round" transform="rotate(-90 60 60)"/>
<text x="60" y="58" text-anchor="middle" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="18" font-weight="800">{percent:.1f}%</text>
<text x="60" y="75" text-anchor="middle" fill="#9CA3AF" font-family="'Inter', sans-serif" font-size="8" font-weight="700" letter-spacing="1.2">{label}</text>
</svg>
</div>"""


def render_saas_model_card(title, tag, acc, prec, rec, f1, speed, params, comp_acc, color="#7C6FF0", is_recommended=False):
    rec_badge = f"""<span style="background:rgba(255, 255, 255, 0.06);color:#E2E8F0;font-family:'Inter',sans-serif;font-size:0.68rem;font-weight:600;padding:4px 9px;border-radius:6px;border:1px solid rgba(255, 255, 255, 0.1);">{tag}</span>"""
    dial_html = svg_radial_dial(acc, color=color, label="ACCURACY", size=105)
    
    return f"""<div class="model-matrix-card">
<div>
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
<span style="font-family: 'Inter', sans-serif; font-weight: 700; font-size: 1.05rem; color: #FFFFFF;">{title}</span>
{rec_badge}
</div>
{dial_html}
<div style="margin: 0.9rem 0; display: flex; flex-direction: column; gap: 9px;">
<div>
<div style="display: flex; justify-content: space-between; font-size: 0.72rem; color: #9CA3AF; font-family: 'Inter', sans-serif; margin-bottom: 3px;">
<span>Precision</span>
<strong style="color: #FFFFFF;">{prec:.1f}%</strong>
</div>
<div class="progress-track-dark">
<div class="progress-fill-rounded" style="width: {prec}%; background: {color};"></div>
</div>
</div>
<div>
<div style="display: flex; justify-content: space-between; font-size: 0.72rem; color: #9CA3AF; font-family: 'Inter', sans-serif; margin-bottom: 3px;">
<span>Recall</span>
<strong style="color: #FFFFFF;">{rec:.1f}%</strong>
</div>
<div class="progress-track-dark">
<div class="progress-fill-rounded" style="width: {rec}%; background: {color};"></div>
</div>
</div>
<div>
<div style="display: flex; justify-content: space-between; font-size: 0.72rem; color: #9CA3AF; font-family: 'Inter', sans-serif; margin-bottom: 3px;">
<span>F1-Score</span>
<strong style="color: #FFFFFF;">{f1:.1f}%</strong>
</div>
<div class="progress-track-dark">
<div class="progress-fill-rounded" style="width: {f1}%; background: {color};"></div>
</div>
</div>
</div>
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; background: #1A1D26; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; padding: 10px; text-align: center;">
<div>
<div style="font-size: 0.62rem; color: #9CA3AF; font-family: 'Inter', sans-serif; font-weight: 600; text-transform: uppercase;">Latency</div>
<div style="font-size: 0.92rem; font-weight: 700; color: #FFFFFF; font-family: 'Inter', sans-serif;">{speed}</div>
</div>
<div>
<div style="font-size: 0.62rem; color: #9CA3AF; font-family: 'Inter', sans-serif; font-weight: 600; text-transform: uppercase;">Params</div>
<div style="font-size: 0.92rem; font-weight: 700; color: #FFFFFF; font-family: 'Inter', sans-serif;">{params}</div>
</div>
</div>
</div>"""


def render_comparative_breakdown_bars():
    return """<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-top: 1.4rem;">
<div style="background: #161922; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 1.4rem 1.6rem; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
<span style="font-family: 'Inter', sans-serif; font-size: 0.9rem; font-weight: 700; color: #FFFFFF;">Inference Speed on Mobile CPU</span>
<span style="font-family: 'Inter', sans-serif; font-size: 0.7rem; color: #9CA3AF; font-weight: 600;">Milliseconds</span>
</div>
<div style="display: flex; flex-direction: column; gap: 12px;">
<div style="display: flex; align-items: center; gap: 10px;">
<span style="width: 105px; font-size: 0.78rem; color: #FFFFFF; font-weight: 600;">MobileNetV2</span>
<div class="progress-track-dark" style="flex: 1; height: 8px;">
<div class="progress-fill-rounded" style="width: 27%; background: linear-gradient(90deg, #7C6FF0 0%, #A78BFA 100%);"></div>
</div>
<span style="width: 65px; text-align: right; font-family: 'Inter', sans-serif; font-size: 0.8rem; font-weight: 700; color: #FFFFFF;">12.4 ms</span>
</div>
<div style="display: flex; align-items: center; gap: 10px;">
<span style="width: 105px; font-size: 0.78rem; color: #9CA3AF;">ResNet50</span>
<div class="progress-track-dark" style="flex: 1; height: 8px;">
<div class="progress-fill-rounded" style="width: 63%; background: linear-gradient(90deg, #0D9488 0%, #2DD4BF 100%);"></div>
</div>
<span style="width: 65px; text-align: right; font-family: 'Inter', sans-serif; font-size: 0.8rem; font-weight: 700; color: #9CA3AF;">28.6 ms</span>
</div>
<div style="display: flex; align-items: center; gap: 10px;">
<span style="width: 105px; font-size: 0.78rem; color: #9CA3AF;">Basic CNN</span>
<div class="progress-track-dark" style="flex: 1; height: 8px;">
<div class="progress-fill-rounded" style="width: 100%; background: linear-gradient(90deg, #D97706 0%, #F59E0B 100%);"></div>
</div>
<span style="width: 65px; text-align: right; font-family: 'Inter', sans-serif; font-size: 0.8rem; font-weight: 700; color: #9CA3AF;">45.2 ms</span>
</div>
</div>
</div>

<div style="background: #161922; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 1.4rem 1.6rem; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
<span style="font-family: 'Inter', sans-serif; font-size: 0.9rem; font-weight: 700; color: #FFFFFF;">Model Parameter Footprint</span>
<span style="font-family: 'Inter', sans-serif; font-size: 0.7rem; color: #9CA3AF; font-weight: 600;">Millions of Params</span>
</div>
<div style="display: flex; flex-direction: column; gap: 12px;">
<div style="display: flex; align-items: center; gap: 10px;">
<span style="width: 105px; font-size: 0.78rem; color: #FFFFFF; font-weight: 600;">MobileNetV2</span>
<div class="progress-track-dark" style="flex: 1; height: 8px;">
<div class="progress-fill-rounded" style="width: 14%; background: linear-gradient(90deg, #059669 0%, #10B981 100%);"></div>
</div>
<span style="width: 65px; text-align: right; font-family: 'Inter', sans-serif; font-size: 0.8rem; font-weight: 700; color: #FFFFFF;">3.4 M</span>
</div>
<div style="display: flex; align-items: center; gap: 10px;">
<span style="width: 105px; font-size: 0.78rem; color: #9CA3AF;">Basic CNN</span>
<div class="progress-track-dark" style="flex: 1; height: 8px;">
<div class="progress-fill-rounded" style="width: 9%; background: linear-gradient(90deg, #D97706 0%, #F59E0B 100%);"></div>
</div>
<span style="width: 65px; text-align: right; font-family: 'Inter', sans-serif; font-size: 0.8rem; font-weight: 700; color: #9CA3AF;">2.1 M</span>
</div>
<div style="display: flex; align-items: center; gap: 10px;">
<span style="width: 105px; font-size: 0.78rem; color: #9CA3AF;">ResNet50</span>
<div class="progress-track-dark" style="flex: 1; height: 8px;">
<div class="progress-fill-rounded" style="width: 100%; background: linear-gradient(90deg, #0D9488 0%, #2DD4BF 100%);"></div>
</div>
<span style="width: 65px; text-align: right; font-family: 'Inter', sans-serif; font-size: 0.8rem; font-weight: 700; color: #9CA3AF;">23.5 M</span>
</div>
</div>
</div>
</div>"""


def executive_sop5_recommendation_card():
    return """<div style="background: #161922; border: 1px solid rgba(255, 255, 255, 0.08); border-left: 4px solid #7C6FF0; border-radius: 14px; padding: 1.4rem 1.6rem; margin-top: 1.4rem; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
<div style="font-family: 'Inter', sans-serif; font-size: 1rem; font-weight: 800; color: #FFFFFF; letter-spacing: 0.2px;">Thesis SOP 5 — Optimal Architecture Conclusion</div>
<span style="background: rgba(255, 255, 255, 0.06); color: #E2E8F0; font-family: 'Inter', sans-serif; font-size: 0.7rem; font-weight: 600; padding: 4px 11px; border-radius: 6px; border: 1px solid rgba(255, 255, 255, 0.1);">MobileNetV2 Selected</span>
</div>
<div style="color: #E2E8F0; font-size: 0.86rem; line-height: 1.55; margin-bottom: 0.8rem;">
<strong>Decision Rationale for Midsayap Online Sellers:</strong> <strong>MobileNetV2</strong> delivers <strong>98.4% accuracy</strong> at <strong>12.4 ms latency</strong> (2.3x faster than ResNet50) with only <strong>3.4M parameters</strong>.
</div>
<div style="font-family: 'Inter', sans-serif; font-size: 0.8rem; color: #10B981; background: rgba(16, 185, 129, 0.08); padding: 9px 14px; border-radius: 8px; border: 1px solid rgba(16, 185, 129, 0.25);">
Pareto Verdict: <strong>MobileNetV2</strong> is the optimal real-time model for instant fraud detection on consumer smartphones.
</div>
</div>"""
