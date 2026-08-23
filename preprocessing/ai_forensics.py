"""
AI-Generated Image Forensics Module — ForgeGuard Thesis System
==============================================================
Detects AI-generated receipt images (Nano Banana, Gemini, DALL-E, Midjourney,
Flux, Stable Diffusion) using 4 mathematical forensic tests:

1. DCT Block Grid Absence — real screenshots have 8x8 JPEG block structure
2. Frequency Spectrum Power-Law Deviation — AI violates natural 1/f^β decay
3. Micro-Texture Smoothness (GLCM) — AI produces hyper-smooth textures
4. Typography Glyph Edge Variance — AI melts/warps text characters

Combined weighted score determines AI-generation probability.
"""

import io
import numpy as np
from PIL import Image, ImageFilter


def _compute_dct_grid_score(pil_img):
    """
    Test 1: DCT Block Grid Absence Check.
    Real JPEG screenshots have periodic 8x8 block boundaries from DCT compression.
    AI-generated images lack these boundaries because they're pixel-synthesized.
    
    Returns float 0.0 (no grid = likely AI) to 1.0 (strong grid = real).
    """
    try:
        gray = np.array(pil_img.convert("L"), dtype=np.float64)
        h, w = gray.shape
        if h < 64 or w < 64:
            return 0.5

        # Compute horizontal and vertical differences
        h_diff = np.abs(np.diff(gray, axis=1))
        v_diff = np.abs(np.diff(gray, axis=0))

        # Measure periodicity at 8-pixel intervals (JPEG block boundaries)
        h_boundary_strength = 0.0
        h_non_boundary_strength = 0.0
        for col in range(h_diff.shape[1]):
            if (col + 1) % 8 == 0:
                h_boundary_strength += np.mean(h_diff[:, col])
            else:
                h_non_boundary_strength += np.mean(h_diff[:, col])

        v_boundary_strength = 0.0
        v_non_boundary_strength = 0.0
        for row in range(v_diff.shape[0]):
            if (row + 1) % 8 == 0:
                v_boundary_strength += np.mean(v_diff[row, :])
            else:
                v_non_boundary_strength += np.mean(v_diff[row, :])

        num_h_boundaries = max(1, h_diff.shape[1] // 8)
        num_h_non = max(1, h_diff.shape[1] - num_h_boundaries)
        num_v_boundaries = max(1, v_diff.shape[0] // 8)
        num_v_non = max(1, v_diff.shape[0] - num_v_boundaries)

        h_ratio = (h_boundary_strength / num_h_boundaries) / max(0.001, h_non_boundary_strength / num_h_non)
        v_ratio = (v_boundary_strength / num_v_boundaries) / max(0.001, v_non_boundary_strength / num_v_non)

        avg_ratio = (h_ratio + v_ratio) / 2.0

        # Real JPEG images have ratio > 1.05 (boundaries are stronger)
        # AI-generated images have ratio ~ 1.0 (uniform, no grid)
        if avg_ratio >= 1.15:
            return 1.0
        elif avg_ratio >= 1.05:
            return 0.7
        elif avg_ratio >= 1.01:
            return 0.4
        else:
            return 0.1
    except Exception:
        return 0.5


def _compute_frequency_deviation_score(pil_img):
    """
    Test 2: Frequency Spectrum Power-Law Deviation.
    Natural photos follow 1/f^β power-law decay (β ≈ 1.5-2.5).
    AI-generated images violate this — over-smoothed or periodic artifacts.
    
    Returns float 0.0 (natural spectrum = real) to 1.0 (anomalous = AI).
    """
    try:
        gray = np.array(pil_img.convert("L"), dtype=np.float64)
        h, w = gray.shape
        if h < 64 or w < 64:
            return 0.5

        # Center crop to square for clean FFT
        s = min(h, w, 512)
        cy, cx = h // 2, w // 2
        crop = gray[cy - s // 2:cy + s // 2, cx - s // 2:cx + s // 2]

        # 2D FFT
        f_transform = np.fft.fft2(crop)
        f_shift = np.fft.fftshift(f_transform)
        magnitude = np.abs(f_shift) + 1e-10
        log_mag = np.log10(magnitude)

        # Compute radial average power spectrum
        center_y, center_x = s // 2, s // 2
        y_coords, x_coords = np.mgrid[:s, :s]
        radii = np.sqrt((y_coords - center_y) ** 2 + (x_coords - center_x) ** 2).astype(int)
        max_radius = min(s // 2, 200)

        radial_profile = np.zeros(max_radius)
        for r in range(1, max_radius):
            mask = radii == r
            if np.any(mask):
                radial_profile[r] = np.mean(log_mag[mask])

        # Fit log-log linear regression (power law: log(P) = -β * log(f) + c)
        valid_start = 5
        valid_end = max_radius - 1
        freqs = np.arange(valid_start, valid_end)
        powers = radial_profile[valid_start:valid_end]
        log_freqs = np.log10(freqs + 1e-10)

        if len(log_freqs) < 10:
            return 0.5

        # Linear regression
        A = np.vstack([log_freqs, np.ones(len(log_freqs))]).T
        try:
            result = np.linalg.lstsq(A, powers, rcond=None)
            slope = result[0][0]
            residuals = powers - (slope * log_freqs + result[0][1])
            rmse = np.sqrt(np.mean(residuals ** 2))
        except Exception:
            return 0.5

        # Natural images: slope between -2.5 and -1.0, low RMSE
        # AI images: slope outside range or high RMSE (poor fit)
        beta = -slope

        deviation_score = 0.0

        # Check beta range
        if beta < 0.8 or beta > 3.0:
            deviation_score += 0.4
        elif beta < 1.2 or beta > 2.8:
            deviation_score += 0.2

        # Check fit quality (RMSE)
        if rmse > 0.8:
            deviation_score += 0.4
        elif rmse > 0.5:
            deviation_score += 0.2

        # Check high-frequency energy (AI often has unusual HF patterns)
        hf_energy = np.mean(radial_profile[max_radius * 3 // 4:])
        lf_energy = np.mean(radial_profile[valid_start:max_radius // 4])
        hf_ratio = hf_energy / max(0.001, lf_energy)
        if hf_ratio > 0.6:
            deviation_score += 0.2
        elif hf_ratio < 0.15:
            deviation_score += 0.2

        return min(1.0, deviation_score)
    except Exception:
        return 0.5


def _compute_texture_smoothness_score(pil_img):
    """
    Test 3: Micro-Texture Smoothness Analysis (simplified GLCM).
    AI models produce hyper-smooth textures lacking natural noise/grain.
    
    Returns float 0.0 (natural texture = real) to 1.0 (unnaturally smooth = AI).
    """
    try:
        gray = np.array(pil_img.convert("L"), dtype=np.float64)
        h, w = gray.shape
        if h < 64 or w < 64:
            return 0.5

        # Sample multiple 64x64 patches from the image
        patch_size = 64
        num_patches = min(12, (h // patch_size) * (w // patch_size))
        if num_patches < 1:
            num_patches = 1

        contrast_values = []
        homogeneity_values = []

        step_y = max(1, (h - patch_size) // max(1, int(np.sqrt(num_patches))))
        step_x = max(1, (w - patch_size) // max(1, int(np.sqrt(num_patches))))

        for py in range(0, h - patch_size, step_y):
            for px in range(0, w - patch_size, step_x):
                patch = gray[py:py + patch_size, px:px + patch_size]

                # Local contrast: standard deviation of pixel differences
                local_diff_h = np.abs(np.diff(patch, axis=1))
                local_diff_v = np.abs(np.diff(patch, axis=0))
                local_contrast = (np.std(local_diff_h) + np.std(local_diff_v)) / 2.0
                contrast_values.append(local_contrast)

                # Local homogeneity: inverse of variance in local neighborhood
                local_var = np.var(patch)
                homogeneity = 1.0 / (1.0 + local_var / 100.0)
                homogeneity_values.append(homogeneity)

                if len(contrast_values) >= num_patches:
                    break
            if len(contrast_values) >= num_patches:
                break

        if not contrast_values:
            return 0.5

        avg_contrast = np.mean(contrast_values)
        avg_homogeneity = np.mean(homogeneity_values)

        # Real images: higher contrast (10-40), lower homogeneity (0.3-0.7)
        # AI images: lower contrast (3-12), higher homogeneity (0.6-0.95)
        smoothness_score = 0.0

        if avg_contrast < 6.0:
            smoothness_score += 0.5
        elif avg_contrast < 12.0:
            smoothness_score += 0.3
        elif avg_contrast < 18.0:
            smoothness_score += 0.1

        if avg_homogeneity > 0.85:
            smoothness_score += 0.5
        elif avg_homogeneity > 0.7:
            smoothness_score += 0.3
        elif avg_homogeneity > 0.55:
            smoothness_score += 0.1

        return min(1.0, smoothness_score)
    except Exception:
        return 0.5


def _compute_glyph_integrity_score(pil_img):
    """
    Test 4: Typography Glyph Edge Integrity Check.
    AI-generated text has melted/warped characters with inconsistent edges.
    Real screenshots have sharp, consistent character boundaries.
    
    Returns float 0.0 (sharp text = real) to 1.0 (warped/melted text = AI).
    """
    try:
        gray = np.array(pil_img.convert("L"), dtype=np.float64)
        h, w = gray.shape
        if h < 64 or w < 64:
            return 0.5

        # Focus on the center portion where text usually appears on receipts
        cy = h // 2
        text_region = gray[max(0, cy - h // 4):min(h, cy + h // 4), :]

        # Edge detection using Sobel-like gradient
        edges_h = np.abs(np.diff(text_region, axis=1))
        edges_v = np.abs(np.diff(text_region, axis=0))

        # Strong edges (potential text boundaries)
        edge_threshold = 30.0
        strong_h = edges_h > edge_threshold
        strong_v = edges_v > edge_threshold

        if np.sum(strong_h) < 10 or np.sum(strong_v) < 10:
            return 0.5

        # Measure consistency of edge strengths
        strong_h_values = edges_h[strong_h]
        strong_v_values = edges_v[strong_v]

        # Coefficient of variation (CV) of edge strengths
        cv_h = np.std(strong_h_values) / max(0.001, np.mean(strong_h_values))
        cv_v = np.std(strong_v_values) / max(0.001, np.mean(strong_v_values))
        avg_cv = (cv_h + cv_v) / 2.0

        # Real text: consistent edge strengths, low CV (0.3-0.6)
        # AI text: variable edge strengths, high CV (0.7-1.5+)
        if avg_cv > 1.0:
            return 0.8
        elif avg_cv > 0.8:
            return 0.6
        elif avg_cv > 0.65:
            return 0.3
        else:
            return 0.1
    except Exception:
        return 0.5


def detect_ai_generation(pil_img):
    """
    Master function: runs all 4 forensic tests and returns combined verdict.
    
    Args:
        pil_img: PIL Image object (RGB mode).
        
    Returns:
        dict with keys:
            is_ai_generated (bool): True if image is likely AI-generated
            ai_confidence (float): 0.0-1.0 overall confidence
            dct_grid_score (float): 0.0 (no grid/AI) to 1.0 (strong grid/real)
            freq_deviation_score (float): 0.0 (natural/real) to 1.0 (anomalous/AI)
            texture_smoothness_score (float): 0.0 (natural/real) to 1.0 (smooth/AI)
            glyph_integrity_score (float): 0.0 (sharp/real) to 1.0 (warped/AI)
            ai_generation_type (str): "DIFFUSION" | "GAN" | "TEMPLATE" | "NONE"
            explanation (str): Human-readable forensic reasoning
    """
    if pil_img.mode != "RGB":
        pil_img = pil_img.convert("RGB")

    # Run all 4 tests
    dct_score = _compute_dct_grid_score(pil_img)
    freq_score = _compute_frequency_deviation_score(pil_img)
    texture_score = _compute_texture_smoothness_score(pil_img)
    glyph_score = _compute_glyph_integrity_score(pil_img)

    # Invert DCT score (0=AI becomes 1 for AI likelihood)
    dct_ai_likelihood = 1.0 - dct_score

    # Weighted ensemble: S_AI = 0.30*DCT + 0.25*freq + 0.25*texture + 0.20*glyph
    ai_score = (
        0.30 * dct_ai_likelihood +
        0.25 * freq_score +
        0.25 * texture_score +
        0.20 * glyph_score
    )

    is_ai = ai_score >= 0.55

    # Determine generation type
    if is_ai:
        if texture_score > 0.6 and freq_score > 0.4:
            ai_type = "DIFFUSION"
        elif glyph_score > 0.6:
            ai_type = "GAN"
        else:
            ai_type = "TEMPLATE"
    else:
        ai_type = "NONE"

    # Build explanation
    reasons = []
    if dct_ai_likelihood > 0.5:
        reasons.append(f"Missing JPEG 8x8 DCT block grid structure (grid score: {dct_score:.2f})")
    if freq_score > 0.4:
        reasons.append(f"Anomalous frequency spectrum violating natural 1/f power-law (deviation: {freq_score:.2f})")
    if texture_score > 0.4:
        reasons.append(f"Hyper-smooth micro-texture lacking authentic pixel noise (smoothness: {texture_score:.2f})")
    if glyph_score > 0.4:
        reasons.append(f"Inconsistent typography edge boundaries suggesting warped/melted glyphs (integrity: {glyph_score:.2f})")

    if is_ai:
        explanation = f"AI-generation probability {ai_score*100:.1f}%. Forensic indicators: {'; '.join(reasons) if reasons else 'Multiple subtle anomalies detected'}."
    else:
        explanation = f"AI-generation probability {ai_score*100:.1f}%. Image exhibits natural photographic characteristics consistent with genuine device screenshots."

    return {
        "is_ai_generated": is_ai,
        "ai_confidence": round(ai_score, 4),
        "dct_grid_score": round(dct_score, 4),
        "freq_deviation_score": round(freq_score, 4),
        "texture_smoothness_score": round(texture_score, 4),
        "glyph_integrity_score": round(glyph_score, 4),
        "ai_generation_type": ai_type,
        "explanation": explanation
    }
