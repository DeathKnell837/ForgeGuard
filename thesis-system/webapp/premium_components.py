# -*- coding: utf-8 -*-
"""
ForgeGuard Enterprise Forensic Command Center Components
Designed with Sophos, Nexora, Nightfall & SOC Command Center UI architectures.
"""

import math

def render_sophos_brand_sidebar():
    """
Renders the Sophos/Nightfall-style Brand Header in the left navigation rail.
"""
    return """<div style="padding-bottom: 0.8rem; margin-bottom: 0.8rem; border-bottom: 1px solid rgba(255,255,255,0.08);">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 4px;">
<div style="width: 32px; height: 32px; border-radius: 8px; background: linear-gradient(135deg, #00F0FF 0%, #8B5CF6 100%); display: flex; align-items: center; justify-content: center; box-shadow: 0 0 15px rgba(0,240,255,0.4);">
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#070A11" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
</svg>
</div>
<div>
<div style="font-family: 'Rajdhani', sans-serif; font-size: 1.25rem; font-weight: 800; color: #F8FAFC; letter-spacing: 1px; line-height: 1;">FORGEGUARD</div>
<div style="font-family: 'JetBrains Mono', monospace; font-size: 0.65rem; color: #00F0FF; letter-spacing: 0.5px;">MOBILE FORENSICS v2.4</div>
</div>
</div>
</div>"""


def render_investigator_profile_card():
    """
Renders the Sophos-style Investigator Profile Card in the sidebar footer.
"""
    return """<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 12px; margin-top: 1.5rem;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
<div style="width: 30px; height: 30px; border-radius: 50%; background: #1E293B; border: 1px solid #00F0FF; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; color: #00F0FF; font-weight: 700;">
BS
</div>
<div>
<div style="font-size: 0.78rem; font-weight: 700; color: #F8FAFC;">Rogie B. & Daniela U.</div>
<div style="font-size: 0.65rem; color: #64748B; font-family: 'JetBrains Mono', monospace;">NDMC CITE • BSCS-4</div>
</div>
</div>
<div style="display: flex; align-items: center; justify-content: space-between; font-size: 0.68rem; font-family: 'JetBrains Mono', monospace; color: #10B981; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 6px;">
<span style="display: flex; align-items: center; gap: 4px;">
<span style="width: 6px; height: 6px; border-radius: 50%; background: #10B981; box-shadow: 0 0 6px #10B981;"></span>
SYSTEM READY
</span>
<span style="color: #94A3B8;">3 CNNs ACTIVE</span>
</div>
</div>"""


def render_top_command_bar(breadcrumb_text, latency_ms=12.4, accuracy_pct=98.4, model_name="MobileNetV2"):
    """
Renders the SOC Command Center Top Bar with breadcrumbs and telemetry pills.
"""
    return f"""<div class="top-command-bar">
<div class="breadcrumb-trail">
<span>FORGEGUARD</span>
<span>/</span>
<span>EVIDENCE TRIAGE</span>
<span>/</span>
<span class="breadcrumb-active">{breadcrumb_text}</span>
</div>
<div class="telemetry-pill-group">
<div class="top-telemetry-pill">
<span style="color: #64748B;">SPEED:</span> <strong style="color: #00F0FF;">{latency_ms:.1f}ms</strong>
</div>
<div class="top-telemetry-pill">
<span style="color: #64748B;">GLOBAL ACC:</span> <strong style="color: #10B981;">{accuracy_pct:.1f}%</strong>
</div>
<div class="top-telemetry-pill">
<span style="color: #64748B;">ENGINE:</span> <strong style="color: #8B5CF6;">{model_name}</strong>
</div>
</div>
</div>"""


def render_exhibit_metadata_bar(filename, resolution, sha256_hash):
    """
Renders forensic exhibit chain-of-custody metadata.
"""
    return f"""<div style="display: flex; justify-content: space-between; align-items: center; background: rgba(0,0,0,0.4); border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 6px 12px; margin-bottom: 8px; font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; color: #94A3B8;">
<div>EXHIBIT: <span style="color: #F8FAFC; font-weight: 600;">{filename}</span></div>
<div>RES: <span style="color: #00F0FF;">{resolution}</span></div>
<div>HASH: <span style="color: #A78BFA;">{sha256_hash}</span></div>
</div>"""


def render_soc_incident_panel(verdict_text, is_forged, confidence, model_name, latency_ms, ela_mean, ela_var, ela_max, gemini_analysis=None):
    """
Renders a unified SOC / Nexora / Sophos Threat Analysis & Forensic Incident Console.
"""
    status_color = "#F87171" if is_forged else "#34D399"
    status_glow = "rgba(248, 113, 113, 0.25)" if is_forged else "rgba(52, 211, 153, 0.25)"
    status_border = "rgba(248, 113, 113, 0.4)" if is_forged else "rgba(52, 211, 153, 0.4)"
    severity_tag = "CRITICAL: TAMPERED ARTIFACT" if is_forged else "SECURE: ZERO TAMPERING"
    verdict_title = "DIGITAL FORGERY DETECTED" if is_forged else "AUTHENTIC RECEIPT VERIFIED"
    sub_desc = "Compression rate disparity & synthetic splicing detected in transaction fields." if is_forged else "Pixel noise gradient is uniform across all metadata and amount regions."
    
    pct = confidence * 100.0
    r = 44
    circumference = 2 * 3.14159265 * r
    filled = circumference * (min(100.0, max(0.0, pct)) / 100.0)
    gap = circumference - filled
    
    splicing_pct = min(98, max(8, int((ela_var / 400.0) * 100))) if is_forged else 4
    compression_pct = min(95, max(12, int((ela_mean / 15.0) * 100))) if is_forged else 9
    
    analysis_block = ""
    if gemini_analysis:
        analysis_block = f"""
<div style="background: rgba(15,23,42,0.8); border: 1px solid rgba(139,92,246,0.3); border-radius: 10px; padding: 12px 14px; margin-top: 12px;">
<div style="display: flex; align-items: center; gap: 6px; margin-bottom: 4px;">
<span style="width: 6px; height: 6px; border-radius: 50%; background: #8B5CF6;"></span>
<span style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #A78BFA; font-weight: 700;">EXPLAINABLE AI DIAGNOSTICS</span>
</div>
<div style="font-size: 0.8rem; color: #E2E8F0; line-height: 1.5;">{gemini_analysis}</div>
</div>"""

    return f"""<div style="background: #0B111E; border: 1px solid {status_border}; border-radius: 14px; padding: 1.25rem; box-shadow: 0 10px 40px {status_glow};">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
<div style="display: flex; align-items: center; gap: 8px;">
<span style="width: 10px; height: 10px; border-radius: 50%; background: {status_color}; box-shadow: 0 0 10px {status_color}; display: inline-block;"></span>
<span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; font-weight: 700; color: {status_color}; letter-spacing: 1px;">{severity_tag}</span>
</div>
<span style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #94A3B8; background: rgba(255,255,255,0.05); padding: 3px 8px; border-radius: 6px;">{model_name} • {latency_ms:.1f}ms</span>
</div>

<div style="font-family: 'Inter', sans-serif; font-size: 1.35rem; font-weight: 800; color: #F8FAFC; letter-spacing: 0.5px; margin-bottom: 4px;">{verdict_title}</div>
<div style="font-size: 0.82rem; color: #94A3B8; line-height: 1.4; margin-bottom: 14px;">{sub_desc}</div>

<div style="display: grid; grid-template-columns: 110px 1fr; gap: 14px; align-items: center; background: rgba(6,9,16,0.6); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 12px; margin-bottom: 12px;">
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center;">
<svg width="95" height="95" viewBox="0 0 100 100">
<circle cx="50" cy="50" r="{r}" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="8"/>
<circle cx="50" cy="50" r="{r}" fill="none" stroke="{status_color}" stroke-width="8" stroke-dasharray="{filled:.1f} {gap:.1f}" stroke-linecap="round" transform="rotate(-90 50 50)"/>
<text x="50" y="48" text-anchor="middle" fill="#F8FAFC" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="800">{pct:.1f}%</text>
<text x="50" y="62" text-anchor="middle" fill="{status_color}" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="700" letter-spacing="1">CERTAINTY</text>
</svg>
</div>

<div style="display: flex; flex-direction: column; gap: 8px;">
<div>
<div style="display: flex; justify-content: space-between; font-size: 0.7rem; font-family: 'JetBrains Mono', monospace; color: #94A3B8; margin-bottom: 2px;">
<span>PIXEL NOISE VARIANCE</span>
<strong style="color: {status_color};">{ela_var:.1f}</strong>
</div>
<div style="width: 100%; height: 6px; background: rgba(255,255,255,0.06); border-radius: 3px; overflow: hidden;">
<div style="width: {splicing_pct}%; height: 100%; background: {status_color}; border-radius: 3px;"></div>
</div>
</div>

<div>
<div style="display: flex; justify-content: space-between; font-size: 0.7rem; font-family: 'JetBrains Mono', monospace; color: #94A3B8; margin-bottom: 2px;">
<span>COMPRESSION DISPARITY</span>
<strong style="color: #00F0FF;">{ela_mean:.1f}</strong>
</div>
<div style="width: 100%; height: 6px; background: rgba(255,255,255,0.06); border-radius: 3px; overflow: hidden;">
<div style="width: {compression_pct}%; height: 100%; background: #00F0FF; border-radius: 3px;"></div>
</div>
</div>
</div>
</div>

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; text-align: center;">
<div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 8px;">
<div style="font-size: 0.65rem; color: #64748B; font-family: 'Inter', sans-serif;">PEAK PIXEL</div>
<div style="font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; font-weight: 700; color: #A78BFA;">{ela_max:.0f}</div>
</div>
<div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 8px;">
<div style="font-size: 0.65rem; color: #64748B; font-family: 'Inter', sans-serif;">ENGINE SPEED</div>
<div style="font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; font-weight: 700; color: #34D399;">{latency_ms:.1f}ms</div>
</div>
<div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 8px;">
<div style="font-size: 0.65rem; color: #64748B; font-family: 'Inter', sans-serif;">PIPELINE</div>
<div style="font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; font-weight: 700; color: #00F0FF;">ELA+CNN</div>
</div>
</div>
{analysis_block}
</div>"""


def render_sophos_benchmark_summary_tiles():
    """
Renders the Sophos-style 4 top metric tiles on Page 2 (Model Comparison).
"""
    return """<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 1.25rem;">
<div style="background: #0B111E; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 14px;">
<div style="font-size: 0.72rem; color: #64748B; font-family: 'JetBrains Mono', monospace; margin-bottom: 4px;">TOP ACCURACY</div>
<div style="font-family: 'JetBrains Mono', monospace; font-size: 1.45rem; font-weight: 800; color: #F8FAFC;">98.7%</div>
<div style="font-size: 0.68rem; color: #8B5CF6; margin-top: 4px;">ResNet50 (Deep Benchmark)</div>
</div>
<div style="background: #0B111E; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 14px;">
<div style="font-size: 0.72rem; color: #64748B; font-family: 'JetBrains Mono', monospace; margin-bottom: 4px;">FASTEST INFERENCE</div>
<div style="font-family: 'JetBrains Mono', monospace; font-size: 1.45rem; font-weight: 800; color: #00F0FF;">12.4ms</div>
<div style="font-size: 0.68rem; color: #00F0FF; margin-top: 4px;">MobileNetV2 (2.3x Faster)</div>
</div>
<div style="background: #0B111E; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 14px;">
<div style="font-size: 0.72rem; color: #64748B; font-family: 'JetBrains Mono', monospace; margin-bottom: 4px;">LIGHTEST FOOTPRINT</div>
<div style="font-family: 'JetBrains Mono', monospace; font-size: 1.45rem; font-weight: 800; color: #10B981;">3.4M</div>
<div style="font-size: 0.68rem; color: #10B981; margin-top: 4px;">85.5% Lighter than ResNet</div>
</div>
<div style="background: #0B111E; border: 1px solid rgba(0,240,255,0.3); border-radius: 12px; padding: 14px; box-shadow: 0 0 20px rgba(0,240,255,0.1);">
<div style="font-size: 0.72rem; color: #00F0FF; font-family: 'JetBrains Mono', monospace; margin-bottom: 4px;">SOP 5 PARETO WINNER</div>
<div style="font-family: 'JetBrains Mono', monospace; font-size: 1.25rem; font-weight: 800; color: #00F0FF;">MobileNetV2</div>
<div style="font-size: 0.68rem; color: #F8FAFC; margin-top: 4px;">Optimal Smartphone Model</div>
</div>
</div>"""


def svg_radial_dial(percent, color="#00F0FF", label="ACCURACY", size=120):
    """
Renders an SVG radial progress dial for benchmark cards.
"""
    r = 44
    circumference = 2 * 3.14159265 * r
    filled = circumference * (min(100.0, max(0.0, percent)) / 100.0)
    gap = circumference - filled
    
    return f"""<div style="display: flex; justify-content: center; margin: 0.6rem 0;">
<svg width="{size}" height="{size}" viewBox="0 0 120 120">
<circle cx="60" cy="60" r="{r}" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="8"/>
<circle cx="60" cy="60" r="{r}" fill="none" stroke="{color}" stroke-width="8" stroke-dasharray="{filled:.1f} {gap:.1f}" stroke-linecap="round" transform="rotate(-90 60 60)"/>
<text x="60" y="58" text-anchor="middle" fill="#F8FAFC" font-family="'JetBrains Mono', monospace" font-size="18" font-weight="800">{percent:.1f}%</text>
<text x="60" y="74" text-anchor="middle" fill="{color}" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="600" letter-spacing="1">{label}</text>
</svg>
</div>"""


def render_saas_model_card(title, tag, acc, prec, rec, f1, speed, params, comp_acc, color="#00F0FF", is_recommended=False):
    """
    Renders a Webstacks / Dribbble SaaS Benchmark Card with SVG radial dial and mini bar meters.
    """
    r_val, g_val, b_val = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
    rec_badge = f"""<span style="background:rgba({r_val},{g_val},{b_val},0.15);color:{color};font-family:'JetBrains Mono',monospace;font-size:0.68rem;font-weight:700;padding:2px 8px;border-radius:6px;border:1px solid rgba({r_val},{g_val},{b_val},0.3);">{tag}</span>"""
    card_border = f"border: 1.5px solid {color}; box-shadow: 0 8px 32px rgba({r_val},{g_val},{b_val},0.15);" if is_recommended else "border: 1px solid rgba(255,255,255,0.08);"
    dial_html = svg_radial_dial(acc, color=color, label="ACCURACY", size=115)
    
    return f"""<div style="background:#0B111E;border-radius:14px;padding:1.25rem;{card_border}display:flex;flex-direction:column;justify-content:space-between;min-height:380px;">
<div>
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
<span style="font-family:'Inter',sans-serif;font-weight:700;font-size:1.05rem;color:#F8FAFC;">{title}</span>
{rec_badge}
</div>
{dial_html}
<div style="margin:0.8rem 0;display:flex;flex-direction:column;gap:8px;">
<div>
<div style="display:flex;justify-content:space-between;font-size:0.72rem;color:#94A3B8;font-family:'JetBrains Mono',monospace;margin-bottom:2px;">
<span>PRECISION</span>
<strong style="color:#F8FAFC;">{prec:.1f}%</strong>
</div>
<div style="width:100%;height:5px;background:rgba(255,255,255,0.06);border-radius:3px;overflow:hidden;">
<div style="width:{prec}%;height:100%;background:{color};border-radius:3px;"></div>
</div>
</div>
<div>
<div style="display:flex;justify-content:space-between;font-size:0.72rem;color:#94A3B8;font-family:'JetBrains Mono',monospace;margin-bottom:2px;">
<span>RECALL</span>
<strong style="color:#F8FAFC;">{rec:.1f}%</strong>
</div>
<div style="width:100%;height:5px;background:rgba(255,255,255,0.06);border-radius:3px;overflow:hidden;">
<div style="width:{rec}%;height:100%;background:{color};border-radius:3px;"></div>
</div>
</div>
<div>
<div style="display:flex;justify-content:space-between;font-size:0.72rem;color:#94A3B8;font-family:'JetBrains Mono',monospace;margin-bottom:2px;">
<span>F1-SCORE</span>
<strong style="color:#F8FAFC;">{f1:.1f}%</strong>
</div>
<div style="width:100%;height:5px;background:rgba(255,255,255,0.06);border-radius:3px;overflow:hidden;">
<div style="width:{f1}%;height:100%;background:{color};border-radius:3px;"></div>
</div>
</div>
</div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;background:rgba(0,0,0,0.3);border-radius:8px;padding:8px;text-align:center;">
<div>
<div style="font-size:0.65rem;color:#64748B;font-family:'JetBrains Mono',monospace;">LATENCY</div>
<div style="font-size:0.9rem;font-weight:700;color:#F8FAFC;font-family:'JetBrains Mono',monospace;">{speed}</div>
</div>
<div>
<div style="font-size:0.65rem;color:#64748B;font-family:'JetBrains Mono',monospace;">PARAMS</div>
<div style="font-size:0.9rem;font-weight:700;color:#F8FAFC;font-family:'JetBrains Mono',monospace;">{params}</div>
</div>
</div>
</div>"""


def render_comparative_breakdown_bars():
    """
Renders comparative latency and parameter footprint bars.
"""
    return """<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 1.25rem;">
<div style="background: #0B111E; border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 1.1rem 1.4rem;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
<span style="font-family: 'Inter', sans-serif; font-size: 0.92rem; font-weight: 700; color: #F8FAFC;">INFERENCE LATENCY ON MOBILE CPU (LOWER IS BETTER)</span>
<span style="font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: #00F0FF;">MILLISECONDS</span>
</div>
<div style="display: flex; flex-direction: column; gap: 8px;">
<div style="display: flex; align-items: center; gap: 12px;">
<span style="width: 110px; font-size: 0.78rem; color: #F8FAFC; font-weight: 600;">MobileNetV2</span>
<div style="flex: 1; height: 10px; background: rgba(255,255,255,0.06); border-radius: 5px; overflow: hidden;">
<div style="width: 27%; height: 100%; background: #00F0FF; border-radius: 5px; box-shadow: 0 0 10px rgba(0,240,255,0.5);"></div>
</div>
<span style="width: 65px; text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; font-weight: 700; color: #00F0FF;">12.4 ms</span>
</div>
<div style="display: flex; align-items: center; gap: 12px;">
<span style="width: 110px; font-size: 0.78rem; color: #94A3B8;">ResNet50</span>
<div style="flex: 1; height: 10px; background: rgba(255,255,255,0.06); border-radius: 5px; overflow: hidden;">
<div style="width: 63%; height: 100%; background: #8B5CF6; border-radius: 5px;"></div>
</div>
<span style="width: 65px; text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; font-weight: 700; color: #8B5CF6;">28.6 ms</span>
</div>
<div style="display: flex; align-items: center; gap: 12px;">
<span style="width: 110px; font-size: 0.78rem; color: #64748B;">Basic CNN</span>
<div style="flex: 1; height: 10px; background: rgba(255,255,255,0.06); border-radius: 5px; overflow: hidden;">
<div style="width: 100%; height: 100%; background: #F59E0B; border-radius: 5px;"></div>
</div>
<span style="width: 65px; text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; font-weight: 700; color: #F59E0B;">45.2 ms</span>
</div>
</div>
</div>
<div style="background: #0B111E; border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 1.1rem 1.4rem;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
<span style="font-family: 'Inter', sans-serif; font-size: 0.92rem; font-weight: 700; color: #F8FAFC;">MODEL RESOURCE FOOTPRINT (MILLIONS OF PARAMS)</span>
<span style="font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: #10B981;">LIGHTER IS BETTER FOR MOBILE</span>
</div>
<div style="display: flex; flex-direction: column; gap: 8px;">
<div style="display: flex; align-items: center; gap: 12px;">
<span style="width: 110px; font-size: 0.78rem; color: #F8FAFC; font-weight: 600;">MobileNetV2</span>
<div style="flex: 1; height: 10px; background: rgba(255,255,255,0.06); border-radius: 5px; overflow: hidden;">
<div style="width: 14%; height: 100%; background: #10B981; border-radius: 5px; box-shadow: 0 0 10px rgba(16,185,129,0.5);"></div>
</div>
<span style="width: 65px; text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; font-weight: 700; color: #10B981;">3.4 M</span>
</div>
<div style="display: flex; align-items: center; gap: 12px;">
<span style="width: 110px; font-size: 0.78rem; color: #64748B;">Basic CNN</span>
<div style="flex: 1; height: 10px; background: rgba(255,255,255,0.06); border-radius: 5px; overflow: hidden;">
<div style="width: 9%; height: 100%; background: #F59E0B; border-radius: 5px;"></div>
</div>
<span style="width: 65px; text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; font-weight: 700; color: #F59E0B;">2.1 M</span>
</div>
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


def executive_sop5_recommendation_card():
    """
Renders the formal thesis recommendation card answering SOP 5 for Midsayap local merchants.
"""
    return """<div style="background: linear-gradient(135deg, rgba(0,240,255,0.08) 0%, rgba(139,92,246,0.08) 100%); border: 1.5px solid rgba(0,240,255,0.4); border-left: 5px solid #00F0FF; border-radius: 14px; padding: 1.25rem 1.5rem; margin-top: 1.25rem; box-shadow: 0 8px 32px rgba(0,240,255,0.1);">
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
