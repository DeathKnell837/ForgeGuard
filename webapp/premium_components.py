"""
ForgeGuard Premium UI Components — SaaS / Embien / Webstacks UI Architecture
===========================================================================
Pure CSS/SVG components inspired by SaaS Visual Hierarchy & Embien Design System.
Zero external library dependencies for bulletproof rendering on Streamlit Cloud.
"""

import textwrap


def svg_radial_dial(pct, color="#00F0FF", label="ACCURACY", size=130):
    """
    Renders an Embien/Webstacks-style SVG dual-ring radial dial with glow.
    """
    r = 48
    circumference = 2 * 3.14159265 * r # ~301.6
    filled = circumference * (min(100.0, max(0.0, pct)) / 100.0)
    gap = circumference - filled
    
    html = f"""<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin: 0.5rem 0;">
<svg width="{size}" height="{size}" viewBox="0 0 120 120">
  <defs>
    <filter id="dialGlow_{color.replace('#','')}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <!-- Background Track Ring -->
  <circle cx="60" cy="60" r="{r}" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="7" />
  <!-- Filled Glow Arc -->
  <circle cx="60" cy="60" r="{r}" fill="none" stroke="{color}" stroke-width="7"
          stroke-dasharray="{filled:.1f} {gap:.1f}"
          stroke-linecap="round"
          transform="rotate(-90 60 60)"
          filter="url(#dialGlow_{color.replace('#','')})" />
  <!-- Center Value -->
  <text x="60" y="58" text-anchor="middle" fill="#FFFFFF" font-family="'JetBrains Mono', monospace" font-size="19" font-weight="700">{pct:.1f}%</text>
  <text x="60" y="74" text-anchor="middle" fill="{color}" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="600" letter-spacing="1">{label}</text>
</svg>
</div>"""
    return textwrap.dedent(html).strip()


def svg_confidence_gauge(confidence_pct, verdict_color, verdict_label):
    """
    Renders the live scanner circular confidence gauge (speedometer style).
    """
    arc_length = 376.99
    filled = arc_length * (confidence_pct / 100.0)
    gap = arc_length - filled
    glow_opacity = min(0.6, confidence_pct / 150.0)
    
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
<text x="100" y="92" text-anchor="middle" fill="{verdict_color}" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="700">{confidence_pct:.1f}%</text>
<text x="100" y="115" text-anchor="middle" fill="{verdict_color}" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="600" letter-spacing="2" opacity="0.9">{simple_label}</text>
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


def render_saas_model_card(title, tag, acc, prec, rec, f1, speed, params, comp_acc, color="#00F0FF", is_recommended=False):
    """
    Renders a Webstacks / Dribbble SaaS Benchmark Card with SVG radial dial and mini bar meters.
    """
    rec_badge = f'<span style="background: rgba({int(color[1:3],16)},{int(color[3:5],16)},{int(color[5:7],16)},0.15); color: {color}; font-family: \'JetBrains Mono\', monospace; font-size: 0.68rem; font-weight: 700; padding: 2px 8px; border-radius: 6px; border: 1px solid rgba({int(color[1:3],16)},{int(color[3:5],16)},{int(color[5:7],16)},0.3);">{tag}</span>'
    card_border = f"border: 1.5px solid {color}; box-shadow: 0 8px 32px rgba({int(color[1:3],16)},{int(color[3:5],16)},{int(color[5:7],16)},0.15);" if is_recommended else "border: 1px solid rgba(255,255,255,0.08);"
    dial_html = svg_radial_dial(acc, color=color, label="ACCURACY", size=115)
    
    html = f"""<div style="background: #0B132B; border-radius: 16px; padding: 1.25rem; {card_border} display: flex; flex-direction: column; justify-content: space-between; height: 100%;">
  <!-- Card Header -->
  <div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
      <span style="font-family: 'Inter', sans-serif; font-weight: 700; font-size: 1.05rem; color: #F8FAFC;">{title}</span>
      {rec_badge}
    </div>
    
    <!-- Central Dial -->
    {dial_html}
    
    <!-- Mini Progress Bars (Precision, Recall, F1) -->
    <div style="margin: 0.8rem 0; display: flex; flex-direction: column; gap: 8px;">
      <!-- Precision -->
      <div>
        <div style="display: flex; justify-content: space-between; font-size: 0.72rem; color: #94A3B8; font-family: 'JetBrains Mono', monospace; margin-bottom: 2px;">
          <span>PRECISION</span>
          <strong style="color: #F8FAFC;">{prec:.1f}%</strong>
        </div>
        <div style="width: 100%; height: 5px; background: rgba(255,255,255,0.06); border-radius: 3px; overflow: hidden;">
          <div style="width: {prec}%; height: 100%; background: {color}; border-radius: 3px;"></div>
        </div>
      </div>
      
      <!-- Recall -->
      <div>
        <div style="display: flex; justify-content: space-between; font-size: 0.72rem; color: #94A3B8; font-family: 'JetBrains Mono', monospace; margin-bottom: 2px;">
          <span>RECALL</span>
          <strong style="color: #F8FAFC;">{rec:.1f}%</strong>
        </div>
        <div style="width: 100%; height: 5px; background: rgba(255,255,255,0.06); border-radius: 3px; overflow: hidden;">
          <div style="width: {rec}%; height: 100%; background: {color}; border-radius: 3px;"></div>
        </div>
      </div>

      <!-- F1-Score -->
      <div>
        <div style="display: flex; justify-content: space-between; font-size: 0.72rem; color: #94A3B8; font-family: 'JetBrains Mono', monospace; margin-bottom: 2px;">
          <span>F1-SCORE</span>
          <strong style="color: #F8FAFC;">{f1:.1f}%</strong>
        </div>
        <div style="width: 100%; height: 5px; background: rgba(255,255,255,0.06); border-radius: 3px; overflow: hidden;">
          <div style="width: {f1}%; height: 100%; background: {color}; border-radius: 3px;"></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Specs Footnote Row -->
  <div style="background: rgba(0,0,0,0.25); border: 1px solid rgba(255,255,255,0.04); border-radius: 10px; padding: 8px 10px; margin-top: 0.5rem; display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; text-align: center;">
    <div><span style="font-size: 0.62rem; color: #64748B;">SPEED</span><br><strong style="font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; color: #00F0FF;">{speed}</strong></div>
    <div><span style="font-size: 0.62rem; color: #64748B;">SIZE</span><br><strong style="font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; color: #F8FAFC;">{params}</strong></div>
    <div><span style="font-size: 0.62rem; color: #64748B;">90Q JPEG</span><br><strong style="font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; color: #10B981;">{comp_acc}</strong></div>
  </div>
</div>"""
    return textwrap.dedent(html).strip()


def render_comparative_breakdown_bars():
    """
    Renders Embien-style horizontal comparative bar gauges for Speed, Memory, and Compression.
    """
    html = """<div style="display: flex; flex-direction: column; gap: 1rem; margin: 1.5rem 0;">
  <!-- Metric 1: Inference Speed (Lower is Faster) -->
  <div style="background: #0B132B; border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 1.1rem 1.4rem;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
      <span style="font-family: 'Inter', sans-serif; font-size: 0.92rem; font-weight: 700; color: #F8FAFC;">INFERENCE LATENCY COMPARISON (MS)</span>
      <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: #00F0FF;">LOWER IS FASTER</span>
    </div>
    
    <div style="display: flex; flex-direction: column; gap: 8px;">
      <!-- MobileNetV2 -->
      <div style="display: flex; align-items: center; gap: 12px;">
        <span style="width: 110px; font-size: 0.78rem; color: #F8FAFC; font-weight: 600;">MobileNetV2</span>
        <div style="flex: 1; height: 10px; background: rgba(255,255,255,0.06); border-radius: 5px; overflow: hidden;">
          <div style="width: 27%; height: 100%; background: #00F0FF; border-radius: 5px; box-shadow: 0 0 10px rgba(0,240,255,0.5);"></div>
        </div>
        <span style="width: 65px; text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; font-weight: 700; color: #00F0FF;">12.4 ms</span>
      </div>

      <!-- ResNet50 -->
      <div style="display: flex; align-items: center; gap: 12px;">
        <span style="width: 110px; font-size: 0.78rem; color: #94A3B8;">ResNet50</span>
        <div style="flex: 1; height: 10px; background: rgba(255,255,255,0.06); border-radius: 5px; overflow: hidden;">
          <div style="width: 63%; height: 100%; background: #8B5CF6; border-radius: 5px;"></div>
        </div>
        <span style="width: 65px; text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; font-weight: 700; color: #8B5CF6;">28.6 ms</span>
      </div>

      <!-- Basic CNN -->
      <div style="display: flex; align-items: center; gap: 12px;">
        <span style="width: 110px; font-size: 0.78rem; color: #64748B;">Basic CNN</span>
        <div style="flex: 1; height: 10px; background: rgba(255,255,255,0.06); border-radius: 5px; overflow: hidden;">
          <div style="width: 100%; height: 100%; background: #F59E0B; border-radius: 5px;"></div>
        </div>
        <span style="width: 65px; text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; font-weight: 700; color: #F59E0B;">45.2 ms</span>
      </div>
    </div>
  </div>

  <!-- Metric 2: Parameter Size (Memory Footprint) -->
  <div style="background: #0B132B; border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 1.1rem 1.4rem;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
      <span style="font-family: 'Inter', sans-serif; font-size: 0.92rem; font-weight: 700; color: #F8FAFC;">MODEL RESOURCE FOOTPRINT (MILLIONS OF PARAMS)</span>
      <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: #10B981;">LIGHTER IS BETTER FOR MOBILE</span>
    </div>
    
    <div style="display: flex; flex-direction: column; gap: 8px;">
      <!-- MobileNetV2 -->
      <div style="display: flex; align-items: center; gap: 12px;">
        <span style="width: 110px; font-size: 0.78rem; color: #F8FAFC; font-weight: 600;">MobileNetV2</span>
        <div style="flex: 1; height: 10px; background: rgba(255,255,255,0.06); border-radius: 5px; overflow: hidden;">
          <div style="width: 14%; height: 100%; background: #10B981; border-radius: 5px; box-shadow: 0 0 10px rgba(16,185,129,0.5);"></div>
        </div>
        <span style="width: 65px; text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; font-weight: 700; color: #10B981;">3.4 M</span>
      </div>

      <!-- Basic CNN -->
      <div style="display: flex; align-items: center; gap: 12px;">
        <span style="width: 110px; font-size: 0.78rem; color: #64748B;">Basic CNN</span>
        <div style="flex: 1; height: 10px; background: rgba(255,255,255,0.06); border-radius: 5px; overflow: hidden;">
          <div style="width: 9%; height: 100%; background: #F59E0B; border-radius: 5px;"></div>
        </div>
        <span style="width: 65px; text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; font-weight: 700; color: #F59E0B;">2.1 M</span>
      </div>

      <!-- ResNet50 -->
      <div style="display: flex; align-items: center; gap: 12px;">
        <span style="width: 110px; font-size: 0.78rem; color: #94A3B8;">ResNet50</span>
        <div style="flex: 1; height: 10px; background: rgba(255,255,255,0.06); border-radius: 5px; overflow: hidden;">
          <div style="width: 100%; height: 100%; background: #8B5CF6; border-radius: 5px;"></div>
        </div>
        <span style="width: 65px; text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; font-weight: 700; color: #8B5CF6;">23.5 M</span>
      </div>
    </div>
  </div>
</div>"""
    return textwrap.dedent(html).strip()


def executive_sop5_recommendation_card():
    """
    Renders the formal thesis recommendation card answering SOP 5 for Midsayap local merchants.
    """
    html = """<div style="background: linear-gradient(135deg, rgba(0,240,255,0.08) 0%, rgba(139,92,246,0.08) 100%); border: 1.5px solid rgba(0,240,255,0.4); border-left: 5px solid #00F0FF; border-radius: 16px; padding: 1.25rem 1.5rem; margin-top: 1.5rem; box-shadow: 0 8px 32px rgba(0,240,255,0.1);">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
<div style="font-family: 'Rajdhani', sans-serif; font-size: 1.1rem; font-weight: 800; color: #00F0FF; letter-spacing: 0.8px;">THESIS SOP 5 — OPTIMAL ARCHITECTURE CONCLUSION</div>
<span style="background: rgba(0,240,255,0.15); color: #00F0FF; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; font-weight: 700; padding: 3px 10px; border-radius: 20px; border: 1px solid rgba(0,240,255,0.3);">MOBILENETV2 SELECTED</span>
</div>
<div style="color: #F8FAFC; font-size: 0.88rem; line-height: 1.6; margin-bottom: 0.6rem;">
<strong>Decision Rationale for Midsayap Online Sellers:</strong><br>
While <strong>ResNet50</strong> scores marginally higher raw accuracy (<strong>98.7%</strong> vs. <strong>98.4%</strong>, a difference of only <strong>0.3%</strong>), <strong>MobileNetV2</strong> executes in only <strong>12.4 ms</strong> (2.3x faster than ResNet50 at 28.6 ms) and consumes only <strong>3.4M parameters</strong> (85.5% lighter than ResNet50's 23.5M).
</div>
<div style="font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; color: #34D399; background: rgba(52,211,153,0.08); padding: 8px 12px; border-radius: 8px; border: 1px solid rgba(52,211,153,0.25);">
Pareto Verdict: <strong>MobileNetV2</strong> is the optimal real-time model for instant fraud detection on consumer smartphones.
</div>
</div>"""
    return textwrap.dedent(html).strip()



