# ForgeGuard: Cross-Architecture CNN Digital Receipt Forgery Detection System

<div align="center">

[![Live Application](https://img.shields.io/badge/Live_System-forgeguard.streamlit.app-8B5CF6?style=for-the-badge&logo=streamlit)](https://forgeguard.streamlit.app/)
[![Python Version](https://img.shields.io/badge/Python-3.10_to_3.12-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![TensorFlow Engine](https://img.shields.io/badge/TensorFlow-2.16+_(Keras_3)-FF6F00?style=for-the-badge&logo=tensorflow)](https://tensorflow.org)
[![Peak Accuracy](https://img.shields.io/badge/Reported_Peak_Accuracy-99.56%25-10B981?style=for-the-badge)](#empirical-benchmark-evaluation)
[![Reported Latency](https://img.shields.io/badge/Reported_Latency-22.51ms-06B6D4?style=for-the-badge)](#empirical-benchmark-evaluation)
[![License](https://img.shields.io/badge/License-Academic_Research-64748B?style=for-the-badge)](#license)

**Receipt or Deceit: A Cross-Architecture Analysis of Convolutional Neural Network Models in Detecting Forged Digital Transaction Receipts**

[Live Web Demo](https://forgeguard.streamlit.app/) &bull; [System Architecture](#system-architecture) &bull; [Empirical Benchmark](#empirical-benchmark-evaluation) &bull; [Dataset](#empirical-dataset-specifications) &bull; [Installation](#quickstart--local-deployment) &bull; [Deployment](#deployment) &bull; [Academic Context](#academic-research-context)

</div>

> If the live app shows "This app has gone to sleep due to inactivity", click the wake-up button and wait about a minute while it restarts.

---

## Overview

**ForgeGuard** is an AI-powered image forensics platform engineered to detect raster tampering, digital amount splicing, font manipulation, and synthetic generation in mobile wallet payment confirmation receipts, focusing specifically on the Philippine **GCash** transaction ecosystem.

Digital receipt fraud exploits the widespread reliance of peer-to-peer online merchants, micro-retailers, and transport operators on electronic payment confirmation slips. Fraudulent actors utilize graphic manipulation tools (such as Photoshop and Canva) or automated receipt generator applications to alter amounts, reference numbers, and recipient details without transferring funds.

ForgeGuard addresses this verification challenge by combining **Error Level Analysis (ELA)** signal decomposition with a comparative evaluation of **three Convolutional Neural Network (CNN) architectures** (Basic CNN, MobileNetV2, and ResNet50), together with an offline benchmark of accuracy, latency, and memory for each model.

---

## Core Capabilities & Features

* **Error Level Analysis (ELA) Forensic Pipeline:**
  Re-compresses incoming receipt images at a JPEG quality factor of $Q = 90$ and amplifies pixel residual differences by a $15.0\times$ multiplier, exposing altered or re-saved regions as localized compression variance spikes.
* **Cross-Architecture CNN Evaluation:**
  Runs all three trained models, one after another, on the same ELA input:
  * **Basic CNN (Baseline):** Custom 3-block convolutional network (Conv 32/64/128, Dense 128; about 3.3M parameters). Reported **92.92%** standard accuracy (22.51 ms benchmark latency) and **99.56%** compressed accuracy (24.12 ms).
  * **MobileNetV2 (Efficient):** Inverted residual, depthwise separable CNN with a custom classification head (about 2.4M parameters). Reported **86.06%** standard accuracy (215.75 ms) and **93.42%** compressed accuracy (221.40 ms).
  * **ResNet50 (Deep Residual):** 50-layer residual network with a Dense 256 head (about 24.1M parameters). Reported 53.54% standard accuracy (395.03 ms), illustrating the limits of deep feature extractors on compression residual artifacts.
  * When TensorFlow loads, every score comes from the trained `.keras` models. **If TensorFlow is unavailable**, the app falls back to a NumPy forward pass of Basic CNN (or, failing that, a simple ELA-brightness rule), and the MobileNetV2 and ResNet50 scores are derived from the Basic CNN score with a small offset rather than from their own models.
* **Two-Screen Operational Workflow:**
  * **Classify a Receipt:** Upload a receipt (PNG, JPG, JPEG, or WEBP) or load one of three benchmark samples ("Authentic Receipt", "Edited Tampering", "Generated Template"). Includes tabbed forensic inspection (Original Exhibit, ELA Residual Matrix, Tamper Heatmap), the Tri-Spectral Forensic Evidence Decomposition gallery, per-model classification cards with confidence readouts and a latency figure, a "How the AI Analyzes This Receipt" explanation panel, and an advisory notice when an image does not look like a standard GCash receipt by size or aspect ratio (the advisory does not block or change the verdict).
  * **Model Comparison (Model Benchmark Suite):** Benchmark table across the standard and compressed conditions, an "Accuracy vs. Speed Comparison" chart, a confusion matrix that can be switched by model and condition, a one-line dataset partition note, and a metric interpretation guide.
* **Zero-Emoji Enterprise Interface:**
  Dark navy theme (`#121620` background, set in `.streamlit/config.toml`), translucent panels, SVG line iconography, and system UI fonts (Segoe UI, Helvetica Neue, Arial) with Cascadia Mono or Consolas for numeric readouts. No web fonts are loaded.

### About the latency shown in the live demo

The latency displayed on the result cards is **calibrated to the offline benchmark values; it is not the time measured on the server**. The app measures each inference with `time.perf_counter()`, but then displays a fixed base plus a small remainder of the measured time (`thesis-system/webapp/app.py`): `22.8 + (measured % 1.5)` ms for Basic CNN, `216.5 + (measured % 4.8)` ms for MobileNetV2, and `397.2 + (measured % 7.5)` ms for ResNet50. In a local test on CPU, measured median times of about 3.4 ms, 8.1 ms, and 17.7 ms were displayed as about 23.2 ms, 219.8 ms, and 399.9 ms.

---

## System Architecture

The ForgeGuard system operates as a four-stage forensic pipeline:

```
[Uploaded GCash Receipt]
         │
         ▼
[1. Preprocessing Layer]
  • Mode Normalization (RGB)
  • JPEG Resaving (Q = 90)
  • Pixel Difference Amplification (15.0x)
  • Tensor Resizing (128 x 128 x 3) & Normalization (/ 255.0)
         │
         ▼
[2. Model Inference Layer (models run one after another on the same input)]
  ├── Basic CNN   (~3.3M params, 22.51 ms benchmark)
  ├── MobileNetV2 (~2.4M params, 215.75 ms benchmark)
  └── ResNet50    (~24.1M params, 395.03 ms benchmark)
         │
         ▼
[3. Decision & Telemetry Layer]
  • Independent Sigmoid Verdicts (Authentic < 0.50 <= Forged)
  • Confidence Percentage Calculation
  • perf_counter timing, displayed as calibrated benchmark latency
         │
         ▼
[4. Presentation Layer (Streamlit)]
  • Per-Model Verdict Cards
  • ELA Exhibit Display
  • Model Comparison Page & Interpretation Guide
```

Parameter counts are taken from the saved model files (frozen weights included). Note that the app's own UI text still shows older estimates (~2.1M, ~3.4M, ~23.5M) that are hard-coded in `app.py`.

---

## Empirical Benchmark Evaluation

The figures below are the headline values stored in `thesis-system/models/evaluation_metrics.json`, which is the file the live app reads and displays. Peak memory values are the ones recorded in that file.

### Standard Evaluation Condition (Uncompressed PNG)
*Reported sample count: 452 (226 Authentic, 226 Forged)*

| Architecture | Condition | Accuracy | Precision | Recall | F1-Score | Inference Latency | Peak Memory | Parameters |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Basic CNN** | Standard | **92.92%** | **98.99%** | **86.73%** | **92.45%** | **22.51 ms** | **626.5 MB** | **~3.3M** |
| **MobileNetV2** | Standard | **86.06%** | **89.76%** | **81.42%** | **85.38%** | **215.75 ms** | **632.2 MB** | **~2.4M** |
| **ResNet50** | Standard | **53.54%** | **51.83%** | **100.00%** | **68.28%** | **395.03 ms** | **638.0 MB** | **~24.1M** |

### Compressed Evaluation Condition (Simulated Transmission Compression)
*Reported sample count: 456 (228 Authentic, 228 Forged)*

| Architecture | Condition | Accuracy | Delta | Precision | Recall | F1-Score | Inference Latency | Peak Memory | Parameters |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Basic CNN** | Compressed | **99.56%** | **+6.64%** | **99.56%** | **99.56%** | **99.56%** | **24.12 ms** | **638.26 MB** | **~3.3M** |
| **MobileNetV2** | Compressed | **93.42%** | **+7.36%** | **92.67%** | **94.30%** | **93.48%** | **221.40 ms** | **638.3 MB** | **~2.4M** |
| **ResNet50** | Compressed | **53.95%** | **+0.41%** | **52.05%** | **100.00%** | **68.47%** | **405.18 ms** | **638.8 MB** | **~24.1M** |

> **Key Research Finding:** The compact custom Basic CNN showed the highest reported accuracy (92.92% standard, 99.56% compressed) and the lowest reported latency (22.51 ms) of the three architectures. ResNet50 flagged 210 of 226 authentic receipts as forged in the standard condition (100% recall, 51.83% precision), suggesting that excessive network depth degrades ELA residual signal discrimination.

### Reproducibility Notes

* **No script in this repository produces a 452-image or 456-image test.** `thesis-system/training/train.py` splits the balanced corpus 70/15/15 (a test split of about 69 images); `thesis-system/evaluate_balanced_5seeds.py` samples 150 images (75 authentic, 75 forged) per seed across 5 seeds; `thesis-system/evaluate_compressed.py` loads every compressed image. 456 is the size of the full balanced corpus that `train.py` trains on, so if the 452/456 figures were computed on the full set, they include training images.
* **The per-seed runs stored in the same JSON do not match the compressed headline values.** The five compressed `seed_runs` (150 images each) average 98.27% / 91.20% / 51.20% accuracy and 4.04 / 9.39 / 26.42 ms latency for Basic CNN / MobileNetV2 / ResNet50.
* The standard-condition latencies (22.51, 215.75, 395.03 ms) are the same values as in `thesis-system/models/pure_empirical_benchmark.json`.

---

## Empirical Dataset Specifications

The corpus lives in `thesis-system/dataset/` and targets officially downloaded GCash transaction receipts.

```
Balanced Training Corpus (compressed condition, sampled by training/train.py)
├── Authentic Receipts: 227 (authentic/compressed, including 102 augmented copies)
└── Forged Receipts: 228
    ├── Edited (114)
    │   ├── Amount Alteration: 29
    │   ├── Reference Number Fabrication: 29
    │   ├── Recipient Name Modification: 29
    │   └── Font Tampering: 27
    └── Generated (114)
        ├── AI-Generated Template: 81
        ├── AI Diffusion Generation: 25
        └── Full Template Synthesis: 8

Remaining 622 compressed forged images: unseen holdout (stress test)
```

Full folder contents:

* **Authentic:** `authentic/highres` 226, `authentic/compressed` 227 (102 of these are `_aug1` / `_aug2` augmented copies, not separate receipts).
* **Forged, compressed (850):** amount alteration 203, name modification 203, reference fabrication 203, font tampering 50, AI-generated template 153, AI diffusion 26, full template 12.
* **Forged, high-res (624):** amount alteration 153, name modification 153, reference fabrication 153, AI-generated template 153, full template 12 (no font tampering or diffusion folders).

*Scope Delimitation (Section 1.4):* The dataset strictly targets officially downloaded GCash transaction receipts. Screen captures containing operating system status bars, battery indicators, and mobile UI chrome are excluded to ensure controlled forensic evaluation.

---

## Quickstart & Local Deployment

### Prerequisites
* Python 3.10, 3.11, or 3.12 (Python 3.13 and newer will fail to install, because `requirements.txt` pins `numpy<2.0.0`)
* Git

### 1. Clone Repository
```bash
git clone https://github.com/DeathKnell837/ForgeGuard.git
cd ForgeGuard
```

### 2. Set Up Virtual Environment & Dependencies
```bash
# Create virtual environment
python -m venv venv
# On Windows, to pick Python 3.12 explicitly:
# py -3.12 -m venv venv

# Activate virtual environment
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Linux/macOS:
source venv/bin/activate

# Install required dependencies (the first install downloads TensorFlow, which is large)
pip install -r requirements.txt
```

### 3. Launch Local Forensic Webapp
```bash
streamlit run app.py
```
Open your browser and navigate to `http://localhost:8501`.

The root `app.py` (and the identical `streamlit_app.py`, and `webapp/app.py`) are small wrappers that run the real application, `thesis-system/webapp/app.py`.

A ready GitHub Codespaces dev container is also included (`.devcontainer/devcontainer.json`, Python 3.11); it runs `streamlit run webapp/app.py` on port 8501.

---

## Deployment

* **Host:** Streamlit Community Cloud, app `forgeguard`, deployed from the `main` branch of this repository at [forgeguard.streamlit.app](https://forgeguard.streamlit.app/).
* **Entry file:** `webapp/app.py`, a wrapper that executes `thesis-system/webapp/app.py`.
* **Runtime:** Python 3.12 via `runtime.txt`; theme in `.streamlit/config.toml`; dependencies from the root `requirements.txt`.
* **Publishing:** pushes come from the thesis workspace through `deploy-forgeguard.ps1`, which copies `thesis-system/README.md` over the root `README.md` before pushing. Edit `thesis-system/README.md`, not the root copy.

---

## Project Structure

```
ForgeGuard/
├── app.py                      # Local entry wrapper (runs thesis-system/webapp/app.py)
├── streamlit_app.py            # Identical entry wrapper
├── webapp/
│   └── app.py                  # Streamlit Cloud entry wrapper (runs thesis-system/webapp/app.py)
├── premium_css.py              # Dark forensic styling system & layout overrides
├── requirements.txt            # Python dependencies used for deployment
├── runtime.txt                 # Python 3.12 for Streamlit Cloud
├── .streamlit/config.toml      # Theme configuration
├── .devcontainer/              # GitHub Codespaces dev container
├── assets/                     # Static assets
├── models/                     # Older copy of weights & metrics (not used when thesis-system/models/ exists)
├── preprocessing/              # Standalone ELA and forensic helper scripts (not imported by the app)
├── deploy-forgeguard.ps1       # Publishing script (see Deployment)
├── thesis-docs/                # Manuscripts and defense material
└── thesis-system/
    ├── README.md               # Source of this README
    ├── webapp/app.py           # The actual Streamlit application (ELA is built in)
    ├── models/                 # Weights loaded by the app & evaluation_metrics.json
    │   ├── basic_cnn.keras
    │   ├── mobilenetv2.keras
    │   ├── resnet50.keras
    │   └── evaluation_metrics.json
    ├── dataset/                # Receipt corpus and build scripts
    │   ├── authentic/{highres,compressed}
    │   ├── forged/{highres,compressed}/<category>
    │   ├── build_realistic_forgery_dataset.py
    │   ├── ingest_authentic_receipts.py
    │   └── import_user_downloads.py
    ├── training/               # train.py and Colab notebooks
    ├── evaluate_balanced_5seeds.py
    ├── evaluate_compressed.py
    ├── tests/
    ├── prototype_title2/       # Earlier phishing URL prototype
    └── webapp_backup_*/        # Older UI backups
```

The app loads models from `thesis-system/models/` first (`get_models_dir()` in `app.py`). The root `models/evaluation_metrics.json` holds older numbers.

---

## Academic Research Context

This software system represents the practical implementation and artifact for the undergraduate thesis:

* **Approved Canonical Title:** *Receipt or Deceit: A Cross-Architecture Analysis of Convolutional Neural Network Models in Detecting Forged Digital Transaction Receipts* (ForgeGuard System)
* **Institution:** Notre Dame of Midsayap College (NDMC)
* **College:** College of Information Technology and Engineering (CITE)
* **Program:** Bachelor of Science in Computer Science (BSCS)
* **Researchers:**
  * **Rogie P. Bacanto** (BSCS-4)
  * **Daniela S. Ungab** (BSCS-4)
* **Adviser:** **Ms. Doris Ann Mariano**
* **Live Deployment:** [forgeguard.streamlit.app](https://forgeguard.streamlit.app/)

---

## License

This project is developed for academic research and educational evaluation under Notre Dame of Midsayap College. All rights reserved.
