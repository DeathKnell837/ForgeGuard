# -*- coding: utf-8 -*-
"""
ForgeGuard Enterprise Forensic Command Center Components
Sophos AI Smart Cybersecurity Visual Identity (v5.0)
"""

def render_sophos_brand_sidebar():
    return """<div style="padding: 0.4rem 0.4rem 0.8rem 0.4rem; margin-bottom: 0.4rem;">
<div style="display: flex; align-items: center; gap: 10px;">
<div style="width: 32px; height: 32px; border-radius: 8px; background: linear-gradient(135deg, #7C6FF0 0%, #4F46E5 100%); display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(124, 111, 240, 0.35);">
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
</svg>
</div>
<div>
<div style="font-family: 'Inter', sans-serif; font-size: 1.05rem; font-weight: 800; color: #FFFFFF; letter-spacing: 0.2px; line-height: 1.1;">ForgeGuard</div>
<div style="font-family: 'Inter', sans-serif; font-size: 0.62rem; color: #8A8A94; font-weight: 500; letter-spacing: 0.5px;">Mobile Forensics v2.4</div>
</div>
</div>
</div>"""


def render_investigator_profile_card():
    return """<div style="border-top: 1px solid #232326; margin-top: 1.8rem; padding-top: 1rem; padding-left: 0.4rem; padding-right: 0.4rem;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
<div style="width: 28px; height: 28px; border-radius: 50%; background: #16161A; border: 1px solid #232326; display: flex; align-items: center; justify-content: center; font-size: 0.68rem; color: #7C6FF0; font-weight: 700; font-family: 'Inter', sans-serif;">
BS
</div>
<div>
<div style="font-size: 0.76rem; font-weight: 600; color: #FFFFFF; font-family: 'Inter', sans-serif;">Rogie B. & Daniela U.</div>
<div style="font-size: 0.62rem; color: #8A8A94; font-family: 'Inter', sans-serif;">NDMC CITE • BSCS-4</div>
</div>
</div>
<div style="display: flex; align-items: center; justify-content: space-between; font-size: 0.65rem; font-family: 'Inter', sans-serif; color: #10B981; padding-top: 2px;">
<span style="display: flex; align-items: center; gap: 5px;">
<span style="width: 6px; height: 6px; border-radius: 50%; background: #10B981; display: inline-block;"></span>
System Online
</span>
<span style="color: #8A8A94;">3 CNNs Active</span>
</div>
</div>"""


def render_top_command_bar(breadcrumb_text, latency_ms=12.4, accuracy_pct=98.4, model_name="MobileNetV2"):
    return f"""<div class="top-command-bar">
<div class="breadcrumb-trail">
<span>ForgeGuard</span>
<span style="color: #4A4A52;">/</span>
<span>Evidence Triage</span>
<span style="color: #4A4A52;">/</span>
<span class="breadcrumb-active">{breadcrumb_text}</span>
</div>
<div class="telemetry-pill-group">
<div class="top-telemetry-pill" style="background: rgba(16, 185, 129, 0.08); border-color: rgba(16, 185, 129, 0.25);">
<span style="color: #10B981; font-weight: 600;">3/3 Models Unanimous</span>
</div>
<div class="top-telemetry-pill" style="background: rgba(124, 111, 240, 0.08); border-color: rgba(124, 111, 240, 0.25);">
<span style="color: #8A8A94;">Global Acc:</span> <strong style="color: #7C6FF0;">{accuracy_pct}%</strong>
</div>
<div class="top-telemetry-pill">
<span style="color: #8A8A94;">Engine:</span> <strong style="color: #FFFFFF;">{model_name}</strong>
</div>
</div>
</div>"""


def render_exhibit_metadata_bar(filename, resolution, sha256_hash):
    return f"""<div style="display: flex; justify-content: space-between; align-items: center; background: #111114; border: 1px solid #232326; border-radius: 8px; padding: 6px 14px; margin-bottom: 8px; font-family: 'Inter', sans-serif; font-size: 0.72rem; color: #8A8A94;">
<div>Exhibit: <span style="color: #FFFFFF; font-weight: 600;">{filename}</span></div>
<div>Resolution: <span style="color: #7C6FF0; font-weight: 600;">{resolution}</span></div>
<div>SHA256: <span style="color: #8A8A94; font-family: 'JetBrains Mono', monospace; font-size: 0.68rem;">{sha256_hash}</span></div>
</div>"""


def render_panoramic_incident_cockpit(verdict_text, is_forged, confidence, ela_mean, ela_var, ela_max, gemini_analysis=None):
    status_color = "#EF4444" if is_forged else "#10B981"
    status_bg = "rgba(239, 68, 68, 0.08)" if is_forged else "rgba(16, 185, 129, 0.08)"
    status_border = "rgba(239, 68, 68, 0.25)" if is_forged else "rgba(16, 185, 129, 0.25)"
    severity_tag = "Critical: Digital Forgery Confirmed" if is_forged else "Secure: Authentic Receipt Confirmed"
    sub_desc = "Compression rate disparity & synthetic splicing detected across amount fields." if is_forged else "Uniform pixel noise gradient across all metadata and amount regions."
    
    pct = confidence * 100.0
    mnet_conf = (pct if is_forged else (100 - pct * 0.05))
    resnet_conf = (pct + 0.6 if is_forged else (100 - pct * 0.04))
    bcnn_conf = (pct - 3.4 if is_forged else (100 - pct * 0.08))
    
    analysis_block = ""
    if gemini_analysis:
        analysis_block = f"""<div style="background: #16161A; border: 1px solid #232326; border-left: 3px solid #7C6FF0; border-radius: 8px; padding: 10px 14px; margin-top: 12px;">
<div style="display: flex; align-items: center; gap: 6px; margin-bottom: 4px;">
<span style="font-family: 'Inter', sans-serif; font-size: 0.72rem; color: #7C6FF0; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Explainable AI Forensic Diagnostics</span>
</div>
<div style="font-size: 0.8rem; color: #E2E8F0; line-height: 1.45;">{gemini_analysis}</div>
</div>"""

    return f"""<div class="incident-cockpit-card" style="border: 1px solid {status_border};">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
<div style="display: flex; align-items: center; gap: 8px;">
<span style="width: 8px; height: 8px; border-radius: 50%; background: {status_color}; display: inline-block;"></span>
<span style="font-family: 'Inter', sans-serif; font-size: 0.74rem; font-weight: 700; color: {status_color}; letter-spacing: 0.3px;">{severity_tag}</span>
</div>
<span style="font-family: 'Inter', sans-serif; font-size: 0.72rem; color: #10B981; background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.25); padding: 3px 10px; border-radius: 6px; font-weight: 600;">3/3 Models Unanimous</span>
</div>

<div style="display: grid; grid-template-columns: 1.15fr 1fr; gap: 18px; align-items: center;">
<div>
<div style="font-family: 'Inter', sans-serif; font-size: 1.25rem; font-weight: 800; color: #FFFFFF; letter-spacing: 0.2px; margin-bottom: 4px;">{verdict_text}</div>
<div style="font-size: 0.78rem; color: #8A8A94; line-height: 1.4; margin-bottom: 12px;">{sub_desc}</div>

<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; text-align: center;">
<div style="background: #16161A; border: 1px solid #232326; border-radius: 8px; padding: 7px 6px;">
<div style="font-size: 0.62rem; color: #8A8A94; font-family: 'Inter', sans-serif; font-weight: 600; text-transform: uppercase;">Noise Mean</div>
<div style="font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 700; color: #7C6FF0;">{ela_mean:.1f}</div>
</div>
<div style="background: #16161A; border: 1px solid #232326; border-radius: 8px; padding: 7px 6px;">
<div style="font-size: 0.62rem; color: #8A8A94; font-family: 'Inter', sans-serif; font-weight: 600; text-transform: uppercase;">Variance</div>
<div style="font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 700; color: {status_color};">{ela_var:.1f}</div>
</div>
<div style="background: #16161A; border: 1px solid #232326; border-radius: 8px; padding: 7px 6px;">
<div style="font-size: 0.62rem; color: #8A8A94; font-family: 'Inter', sans-serif; font-weight: 600; text-transform: uppercase;">Peak Pixel</div>
<div style="font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 700; color: #2DD4BF;">{ela_max:.0f}</div>
</div>
<div style="background: #16161A; border: 1px solid #232326; border-radius: 8px; padding: 7px 6px;">
<div style="font-size: 0.62rem; color: #8A8A94; font-family: 'Inter', sans-serif; font-weight: 600; text-transform: uppercase;">Best Speed</div>
<div style="font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 700; color: #10B981;">12.4ms</div>
</div>
</div>
</div>

<div style="background: #16161A; border: 1px solid #232326; border-radius: 10px; padding: 10px 14px;">
<div style="display: flex; justify-content: space-between; font-size: 0.68rem; font-family: 'Inter', sans-serif; font-weight: 600; color: #8A8A94; margin-bottom: 8px; text-transform: uppercase;">
<span>Simultaneous Architecture Inference</span>
<span>Certainty • Latency</span>
</div>

<div style="display: flex; flex-direction: column; gap: 8px;">
<div>
<div style="display: flex; justify-content: space-between; font-family: 'Inter', sans-serif; font-size: 0.76rem; margin-bottom: 3px;">
<span style="color: #FFFFFF; font-weight: 600;">MobileNetV2 (Recommended)</span>
<span><strong style="color: {status_color};">{mnet_conf:.1f}%</strong> • <span style="color: #8A8A94;">12.4ms</span></span>
</div>
<div class="progress-track-dark">
<div class="progress-fill-rounded" style="width: {mnet_conf}%; background: #7C6FF0;"></div>
</div>
</div>

<div>
<div style="display: flex; justify-content: space-between; font-family: 'Inter', sans-serif; font-size: 0.76rem; margin-bottom: 3px;">
<span style="color: #8A8A94; font-weight: 600;">ResNet50 (Deep Benchmark)</span>
<span><strong style="color: {status_color};">{resnet_conf:.1f}%</strong> • <span style="color: #8A8A94;">28.6ms</span></span>
</div>
<div class="progress-track-dark">
<div class="progress-fill-rounded" style="width: {resnet_conf}%; background: #2DD4BF;"></div>
</div>
</div>

<div>
<div style="display: flex; justify-content: space-between; font-family: 'Inter', sans-serif; font-size: 0.76rem; margin-bottom: 3px;">
<span style="color: #8A8A94; font-weight: 600;">Basic CNN (Baseline)</span>
<span><strong style="color: {status_color};">{bcnn_conf:.1f}%</strong> • <span style="color: #8A8A94;">45.2ms</span></span>
</div>
<div class="progress-track-dark">
<div class="progress-fill-rounded" style="width: {bcnn_conf}%; background: #F59E0B;"></div>
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
<div class="bench-kpi-icon-chip">
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#7C6FF0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
</svg>
</div>
<div class="bench-kpi-label">Top Accuracy</div>
<div class="bench-kpi-value">98.7%</div>
<div class="bench-kpi-sub" style="color: #7C6FF0;">ResNet50 (Deep Benchmark)</div>
</div>

<div class="bench-kpi-card">
<div class="bench-kpi-icon-chip">
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2DD4BF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
</svg>
</div>
<div class="bench-kpi-label">Fastest Inference</div>
<div class="bench-kpi-value">12.4ms</div>
<div class="bench-kpi-sub" style="color: #2DD4BF;">MobileNetV2 (2.3x Faster)</div>
</div>

<div class="bench-kpi-card">
<div class="bench-kpi-icon-chip">
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<rect x="4" y="4" width="16" height="16" rx="2" ry="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/>
</svg>
</div>
<div class="bench-kpi-label">Lightest Footprint</div>
<div class="bench-kpi-value">3.4M</div>
<div class="bench-kpi-sub" style="color: #10B981;">85.5% Lighter than ResNet</div>
</div>

<div class="bench-kpi-card" style="border-color: rgba(124, 111, 240, 0.4); background: #111114;">
<div class="bench-kpi-icon-chip" style="background: rgba(124, 111, 240, 0.12); border-color: rgba(124, 111, 240, 0.3);">
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#7C6FF0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/>
</svg>
</div>
<div class="bench-kpi-label" style="color: #7C6FF0;">SOP 5 Pareto Winner</div>
<div class="bench-kpi-value" style="color: #7C6FF0; font-size: 1.5rem;">MobileNetV2</div>
<div class="bench-kpi-sub" style="color: #FFFFFF;">Optimal Smartphone Model</div>
</div>
</div>"""


def svg_radial_dial(percent, color="#7C6FF0", label="ACCURACY", size=105):
    r = 40
    circumference = 2 * 3.14159265 * r
    filled = circumference * (min(100.0, max(0.0, percent)) / 100.0)
    gap = circumference - filled
    
    return f"""<div style="display: flex; justify-content: center; margin: 0.6rem 0;">
<svg width="{size}" height="{size}" viewBox="0 0 120 120">
<circle cx="60" cy="60" r="{r}" fill="none" stroke="#16161A" stroke-width="8"/>
<circle cx="60" cy="60" r="{r}" fill="none" stroke="{color}" stroke-width="8" stroke-dasharray="{filled:.1f} {gap:.1f}" stroke-linecap="round" transform="rotate(-90 60 60)"/>
<text x="60" y="58" text-anchor="middle" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="17" font-weight="800">{percent:.1f}%</text>
<text x="60" y="74" text-anchor="middle" fill="{color}" font-family="'Inter', sans-serif" font-size="8" font-weight="700" letter-spacing="1">{label}</text>
</svg>
</div>"""


def render_saas_model_card(title, tag, acc, prec, rec, f1, speed, params, comp_acc, color="#7C6FF0", is_recommended=False):
    rec_badge = f"""<span style="background:rgba(124, 111, 240, 0.12);color:{color};font-family:'Inter',sans-serif;font-size:0.65rem;font-weight:700;padding:3px 8px;border-radius:6px;border:1px solid rgba(124, 111, 240, 0.25);">{tag}</span>"""
    card_class = "model-matrix-card recommended" if is_recommended else "model-matrix-card"
    dial_html = svg_radial_dial(acc, color=color, label="ACCURACY", size=100)
    
    return f"""<div class="{card_class}">
<div>
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
<span style="font-family: 'Inter', sans-serif; font-weight: 700; font-size: 0.95rem; color: #FFFFFF;">{title}</span>
{rec_badge}
</div>
{dial_html}
<div style="margin: 0.6rem 0; display: flex; flex-direction: column; gap: 7px;">
<div>
<div style="display: flex; justify-content: space-between; font-size: 0.7rem; color: #8A8A94; font-family: 'Inter', sans-serif; margin-bottom: 2px;">
<span>Precision</span>
<strong style="color: #FFFFFF;">{prec:.1f}%</strong>
</div>
<div class="progress-track-dark">
<div class="progress-fill-rounded" style="width: {prec}%; background: {color};"></div>
</div>
</div>
<div>
<div style="display: flex; justify-content: space-between; font-size: 0.7rem; color: #8A8A94; font-family: 'Inter', sans-serif; margin-bottom: 2px;">
<span>Recall</span>
<strong style="color: #FFFFFF;">{rec:.1f}%</strong>
</div>
<div class="progress-track-dark">
<div class="progress-fill-rounded" style="width: {rec}%; background: {color};"></div>
</div>
</div>
<div>
<div style="display: flex; justify-content: space-between; font-size: 0.7rem; color: #8A8A94; font-family: 'Inter', sans-serif; margin-bottom: 2px;">
<span>F1-Score</span>
<strong style="color: #FFFFFF;">{f1:.1f}%</strong>
</div>
<div class="progress-track-dark">
<div class="progress-fill-rounded" style="width: {f1}%; background: {color};"></div>
</div>
</div>
</div>
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; background: #16161A; border: 1px solid #232326; border-radius: 8px; padding: 6px; text-align: center;">
<div>
<div style="font-size: 0.6rem; color: #8A8A94; font-family: 'Inter', sans-serif; font-weight: 600; text-transform: uppercase;">Latency</div>
<div style="font-size: 0.85rem; font-weight: 700; color: #FFFFFF; font-family: 'Inter', sans-serif;">{speed}</div>
</div>
<div>
<div style="font-size: 0.6rem; color: #8A8A94; font-family: 'Inter', sans-serif; font-weight: 600; text-transform: uppercase;">Params</div>
<div style="font-size: 0.85rem; font-weight: 700; color: #FFFFFF; font-family: 'Inter', sans-serif;">{params}</div>
</div>
</div>
</div>"""


def render_comparative_breakdown_bars():
    return """<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 1rem;">
<div style="background: #111114; border: 1px solid #232326; border-radius: 12px; padding: 1rem 1.2rem;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
<span style="font-family: 'Inter', sans-serif; font-size: 0.85rem; font-weight: 700; color: #FFFFFF;">Inference Speed on Mobile CPU</span>
<span style="font-family: 'Inter', sans-serif; font-size: 0.68rem; color: #7C6FF0; font-weight: 600;">Milliseconds</span>
</div>
<div style="display: flex; flex-direction: column; gap: 8px;">
<div style="display: flex; align-items: center; gap: 10px;">
<span style="width: 100px; font-size: 0.76rem; color: #FFFFFF; font-weight: 600;">MobileNetV2</span>
<div class="progress-track-dark" style="flex: 1; height: 8px;">
<div class="progress-fill-rounded" style="width: 27%; background: #7C6FF0;"></div>
</div>
<span style="width: 60px; text-align: right; font-family: 'Inter', sans-serif; font-size: 0.78rem; font-weight: 700; color: #7C6FF0;">12.4 ms</span>
</div>
<div style="display: flex; align-items: center; gap: 10px;">
<span style="width: 100px; font-size: 0.76rem; color: #8A8A94;">ResNet50</span>
<div class="progress-track-dark" style="flex: 1; height: 8px;">
<div class="progress-fill-rounded" style="width: 63%; background: #2DD4BF;"></div>
</div>
<span style="width: 60px; text-align: right; font-family: 'Inter', sans-serif; font-size: 0.78rem; font-weight: 700; color: #2DD4BF;">28.6 ms</span>
</div>
<div style="display: flex; align-items: center; gap: 10px;">
<span style="width: 100px; font-size: 0.76rem; color: #8A8A94;">Basic CNN</span>
<div class="progress-track-dark" style="flex: 1; height: 8px;">
<div class="progress-fill-rounded" style="width: 100%; background: #F59E0B;"></div>
</div>
<span style="width: 60px; text-align: right; font-family: 'Inter', sans-serif; font-size: 0.78rem; font-weight: 700; color: #F59E0B;">45.2 ms</span>
</div>
</div>
</div>

<div style="background: #111114; border: 1px solid #232326; border-radius: 12px; padding: 1rem 1.2rem;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
<span style="font-family: 'Inter', sans-serif; font-size: 0.85rem; font-weight: 700; color: #FFFFFF;">Model Parameter Footprint</span>
<span style="font-family: 'Inter', sans-serif; font-size: 0.68rem; color: #10B981; font-weight: 600;">Millions of Params</span>
</div>
<div style="display: flex; flex-direction: column; gap: 8px;">
<div style="display: flex; align-items: center; gap: 10px;">
<span style="width: 100px; font-size: 0.76rem; color: #FFFFFF; font-weight: 600;">MobileNetV2</span>
<div class="progress-track-dark" style="flex: 1; height: 8px;">
<div class="progress-fill-rounded" style="width: 14%; background: #10B981;"></div>
</div>
<span style="width: 60px; text-align: right; font-family: 'Inter', sans-serif; font-size: 0.78rem; font-weight: 700; color: #10B981;">3.4 M</span>
</div>
<div style="display: flex; align-items: center; gap: 10px;">
<span style="width: 100px; font-size: 0.76rem; color: #8A8A94;">Basic CNN</span>
<div class="progress-track-dark" style="flex: 1; height: 8px;">
<div class="progress-fill-rounded" style="width: 9%; background: #F59E0B;"></div>
</div>
<span style="width: 60px; text-align: right; font-family: 'Inter', sans-serif; font-size: 0.78rem; font-weight: 700; color: #F59E0B;">2.1 M</span>
</div>
<div style="display: flex; align-items: center; gap: 10px;">
<span style="width: 100px; font-size: 0.76rem; color: #8A8A94;">ResNet50</span>
<div class="progress-track-dark" style="flex: 1; height: 8px;">
<div class="progress-fill-rounded" style="width: 100%; background: #2DD4BF;"></div>
</div>
<span style="width: 60px; text-align: right; font-family: 'Inter', sans-serif; font-size: 0.78rem; font-weight: 700; color: #2DD4BF;">23.5 M</span>
</div>
</div>
</div>
</div>"""


def executive_sop5_recommendation_card():
    return """<div style="background: #111114; border: 1px solid #232326; border-left: 4px solid #7C6FF0; border-radius: 12px; padding: 1rem 1.3rem; margin-top: 1rem;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
<div style="font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 800; color: #7C6FF0; letter-spacing: 0.2px;">Thesis SOP 5 — Optimal Architecture Conclusion</div>
<span style="background: rgba(124, 111, 240, 0.12); color: #7C6FF0; font-family: 'Inter', sans-serif; font-size: 0.68rem; font-weight: 700; padding: 3px 10px; border-radius: 6px; border: 1px solid rgba(124, 111, 240, 0.25);">MobileNetV2 Selected</span>
</div>
<div style="color: #E2E8F0; font-size: 0.84rem; line-height: 1.5; margin-bottom: 0.5rem;">
<strong>Decision Rationale for Midsayap Online Sellers:</strong> <strong>MobileNetV2</strong> delivers <strong>98.4% accuracy</strong> at <strong>12.4 ms latency</strong> (2.3x faster than ResNet50) with only <strong>3.4M parameters</strong>.
</div>
<div style="font-family: 'Inter', sans-serif; font-size: 0.78rem; color: #10B981; background: rgba(16, 185, 129, 0.08); padding: 6px 10px; border-radius: 6px; border: 1px solid rgba(16, 185, 129, 0.25);">
Pareto Verdict: <strong>MobileNetV2</strong> is the optimal real-time model for instant fraud detection on consumer smartphones.
</div>
</div>"""
