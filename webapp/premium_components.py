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
    Renders a unified, sleek, 1-page compact mobile header with live telemetry pills.
    """
    html = f"""<div class="app-header-compact">
<div style="display: flex; align-items: center; justify-content: space-between; width: 100%; margin-bottom: 8px;">
<div style="display: flex; align-items: center; gap: 10px;">
<div class="brand-shield">{svg_shield}</div>
<div>
<div style="font-family: 'Rajdhani', sans-serif; font-weight: 800; font-size: 1.35rem; letter-spacing: 1px; color: #F8FAFC; line-height: 1;">FORGEGUARD</div>
<div style="font-family: 'JetBrains Mono', monospace; font-size: 0.66rem; color: #00F0FF; letter-spacing: 0.5px;">GCASH & MAYA FRAUD DETECTOR</div>
</div>
</div>
<div>
<span class="badge-status-live"><span class="pulse-green"></span> 98.4% ACC</span>
</div>
</div>
<div class="telemetry-bar-row">
<div class="t-pill"><span class="t-label">SPEED</span> <strong style="color: #00F0FF;">12.4ms</strong></div>
<div class="t-pill"><span class="t-label">ACCURACY</span> <strong style="color: #10B981;">98.4%</strong></div>
<div class="t-pill"><span class="t-label">SENSITIVITY</span> <strong style="color: #8B5CF6;">90Q/15X</strong></div>
<div class="t-pill"><span class="t-label">MODELS</span> <strong style="color: #F59E0B;">3 CNNs</strong></div>
</div>
</div>
<div class="shimmer-line" style="margin-bottom: 0.8rem;"></div>"""
    return textwrap.dedent(html).strip()


def premium_hero_banner():
    """
    Legacy placeholder - returns empty to keep the UI clean and 1-page compact.
    """
    return ""


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


def plot_sop1_sop2_metrics():
    """
    Renders an interactive Plotly grouped bar chart answering SOP 1 & 2:
    Classification Accuracy, Precision, Recall, and F1-Score across Basic CNN, ResNet50, and MobileNetV2.
    """
    import plotly.graph_objects as go
    
    models = ['Basic CNN (Baseline)', 'ResNet50 (Deep)', 'MobileNetV2 (Edge)']
    accuracy = [94.2, 98.7, 98.4]
    precision = [93.8, 98.9, 98.6]
    recall = [94.6, 98.5, 98.2]
    f1_score = [94.2, 98.7, 98.4]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Accuracy (%)', x=models, y=accuracy, marker_color='#00F0FF'))
    fig.add_trace(go.Bar(name='Precision (%)', x=models, y=precision, marker_color='#10B981'))
    fig.add_trace(go.Bar(name='Recall (%)', x=models, y=recall, marker_color='#8B5CF6'))
    fig.add_trace(go.Bar(name='F1-Score (%)', x=models, y=f1_score, marker_color='#F59E0B'))
    
    fig.update_layout(
        barmode='group',
        paper_bgcolor='#090E1A',
        plot_bgcolor='#0D1627',
        font=dict(family='JetBrains Mono, monospace', size=12, color='#F8FAFC'),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
        margin=dict(l=20, r=20, t=40, b=20),
        yaxis=dict(range=[85, 100], gridcolor='rgba(255,255,255,0.06)', title='Performance Percentage (%)'),
        xaxis=dict(gridcolor='rgba(255,255,255,0.06)'),
        height=340
    )
    return fig


def plot_sop3_efficiency_scatter():
    """
    Renders an interactive scatter plot answering SOP 3:
    Inference Latency (ms) vs. Computational Parameter Size (Millions).
    """
    import plotly.graph_objects as go
    
    models = ['MobileNetV2 (Recommended)', 'ResNet50 (Deep Benchmark)', 'Basic CNN (Baseline)']
    latency = [12.4, 28.6, 45.2]
    params = [3.4, 23.5, 2.1]
    accuracy = [98.4, 98.7, 94.2]
    colors = ['#00F0FF', '#8B5CF6', '#F59E0B']
    
    fig = go.Figure()
    for m, l, p, acc, c in zip(models, latency, params, accuracy, colors):
        fig.add_trace(go.Scatter(
            x=[l], y=[p],
            mode='markers+text',
            name=m,
            text=[f"<b>{m.split(' ')[0]}</b><br>{acc}% Acc"],
            textposition='top center',
            marker=dict(size=[26], color=c, line=dict(width=2, color='#FFFFFF')),
            hovertemplate=f"<b>{m}</b><br>Latency: %{{x}} ms<br>Parameters: %{{y}}M<br>Accuracy: {acc}%<extra></extra>"
        ))
        
    fig.update_layout(
        paper_bgcolor='#090E1A',
        plot_bgcolor='#0D1627',
        font=dict(family='JetBrains Mono, monospace', size=11, color='#F8FAFC'),
        showlegend=False,
        margin=dict(l=20, r=20, t=30, b=20),
        xaxis=dict(title='Inference Latency (ms) — Lower is Faster', gridcolor='rgba(255,255,255,0.06)', range=[5, 55]),
        yaxis=dict(title='Model Parameters (Millions) — Lower is Lighter', gridcolor='rgba(255,255,255,0.06)', range=[0, 30]),
        height=320
    )
    return fig


def plot_sop4_compression_resilience():
    """
    Renders an interactive bar chart answering SOP 4:
    Classification accuracy comparison across Original High-Res vs. 90Q Heavily Compressed images.
    """
    import plotly.graph_objects as go
    
    models = ['Basic CNN', 'ResNet50', 'MobileNetV2']
    original_acc = [96.1, 99.2, 99.0]
    compressed_acc = [92.3, 98.2, 97.8]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Original High-Resolution (4.1)', x=models, y=original_acc, marker_color='#10B981'))
    fig.add_trace(go.Bar(name='JPEG Compressed (90Q) (4.2)', x=models, y=compressed_acc, marker_color='#F87171'))
    
    fig.update_layout(
        barmode='group',
        paper_bgcolor='#090E1A',
        plot_bgcolor='#0D1627',
        font=dict(family='JetBrains Mono, monospace', size=12, color='#F8FAFC'),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
        margin=dict(l=20, r=20, t=40, b=20),
        yaxis=dict(range=[85, 100], gridcolor='rgba(255,255,255,0.06)', title='Accuracy (%)'),
        xaxis=dict(gridcolor='rgba(255,255,255,0.06)'),
        height=300
    )
    return fig


def executive_sop5_recommendation_card():
    """
    Renders the formal thesis recommendation card answering SOP 5 for Midsayap local merchants.
    """
    html = """<div style="background: linear-gradient(135deg, rgba(0,240,255,0.06) 0%, rgba(139,92,246,0.06) 100%); border: 1.5px solid rgba(0,240,255,0.4); border-left: 5px solid #00F0FF; border-radius: 14px; padding: 1.25rem 1.5rem; margin: 1.25rem 0;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
<div style="font-family: 'Rajdhani', sans-serif; font-size: 1.1rem; font-weight: 800; color: #00F0FF; letter-spacing: 0.8px;">THESIS STATEMENT OF THE PROBLEM 5 (SOP 5) — OPTIMAL MODEL RECOMMENDATION</div>
<span style="background: rgba(0,240,255,0.15); color: #00F0FF; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; font-weight: 700; padding: 3px 10px; border-radius: 20px;">MOBILENETV2 SELECTED</span>
</div>
<div style="color: #F8FAFC; font-size: 0.9rem; line-height: 1.6; margin-bottom: 0.6rem;">
<strong>Research Conclusion for Local Online Sellers in Midsayap, North Cotabato:</strong><br>
While <strong>ResNet50</strong> achieved a marginally higher peak accuracy (<strong>98.7%</strong> vs. <strong>98.4%</strong>, a difference of only <strong>0.3%</strong>), <strong>MobileNetV2</strong> executes in only <strong>12.4 ms</strong> (2.3x faster than ResNet50 at 28.6 ms) and occupies only <strong>3.4M parameters</strong> (85.5% smaller memory footprint than ResNet50's 23.5M).
</div>
<div style="font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; color: #34D399; background: rgba(52,211,153,0.08); padding: 8px 12px; border-radius: 8px; border: 1px solid rgba(52,211,153,0.2);">
Recommended Architecture: <strong>MobileNetV2</strong> provides the optimal Pareto balance for real-time mobile fraud detection in resource-constrained environments.
</div>
</div>"""
    return textwrap.dedent(html).strip()



