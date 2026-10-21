# ForgeGuard: Cross-Architecture CNN Digital Receipt Forgery Detection System

<div align="center">

[![Live Application](https://img.shields.io/badge/Live_System-forgeguard.streamlit.app-8B5CF6?style=for-the-badge&logo=streamlit)](https://forgeguard.streamlit.app/)
[![Python Version](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![TensorFlow Engine](https://img.shields.io/badge/TensorFlow-2.13+-FF6F00?style=for-the-badge&logo=tensorflow)](https://tensorflow.org)
[![Peak Accuracy](https://img.shields.io/badge/Peak_Accuracy-91.82%25-10B981?style=for-the-badge)](https://forgeguard.streamlit.app/)
[![Fastest Latency](https://img.shields.io/badge/Fastest_Latency-74.25ms-06B6D4?style=for-the-badge)](https://forgeguard.streamlit.app/)
[![License](https://img.shields.io/badge/License-Academic_Research-64748B?style=for-the-badge)](LICENSE)

**Receipt or Deceit: A Cross-Architecture Analysis of Convolutional Neural Network Models in Detecting Forged Digital Transaction Receipts**

[Live Web Demo](https://forgeguard.streamlit.app/) &bull; [System Architecture](#system-architecture) &bull; [Empirical Benchmark](#empirical-benchmark-evaluation) &bull; [Dataset](#empirical-dataset-specifications) &bull; [Installation](#quickstart--local-deployment) &bull; [Academic Context](#academic-research-context)

</div>

---

## Overview

**ForgeGuard** is an AI-powered image forensics platform engineered to detect raster tampering, digital amount splicing, font manipulation, and synthetic generation in mobile wallet payment confirmation receipts, focusing specifically on the Philippine **GCash** transaction ecosystem.

Digital receipt fraud exploits the widespread reliance of peer-to-peer online merchants, micro-retailers, and transport operators on electronic payment confirmation slips. Fraudulent actors utilize graphic manipulation tools (such as Photoshop and Canva) or automated receipt generator applications to alter amounts, reference numbers, and recipient details without transferring funds.

ForgeGuard resolves this verification challenge by combining mathematical **Error Level Analysis (ELA)** signal decomposition with a rigorous comparative evaluation of **three distinct Convolutional Neural Network (CNN) architectures** (Basic CNN, MobileNetV2, and ResNet50), delivering millisecond-level verification, authentic inference latency benchmarking, and reproducible empirical evidence.

---

## Core Capabilities & Features

* **Error Level Analysis (ELA) Forensic Pipeline:**
  Re-compresses incoming receipt images at a calibrated JPEG quality factor ($Q = 90$) and amplifies pixel residual discrepancies by a $15.0\times$ difference multiplier, exposing altered or re-saved regions as localized compression variance spikes.
* **Cross-Architecture CNN Evaluation:**
  Evaluates three benchmarked deep learning models in parallel without synthetic score overrides or rule-based bypasses:
  * **Basic CNN (Baseline):** Custom 3-block convolutional network (~2.1M parameters) achieving **91.82%** standard accuracy (86.27 ms latency) and **91.73%** compressed accuracy (74.25 ms latency), achieving top Section 2.10 Composite Score (100.00%).
  * **MobileNetV2 (Efficient):** Inverted residual depthwise separable CNN (~3.4M parameters) achieving **82.22%** standard accuracy (91.43 ms latency) and **87.82%** compressed accuracy (84.63 ms latency), with strong compression resilience (+5.60% delta).
  * **ResNet50 (Deep Residual):** 50-layer deep network (~23.5M parameters) exhibiting 53.42% standard accuracy (128.08 ms latency) and 49.24% compressed accuracy (120.80 ms latency), demonstrating the empirical limits of deep feature extractors on compression residual artifacts.
* **Two-Screen Operational Workflow:**
  * **Classify a Receipt:** Real-time upload interface featuring tabbed forensic inspection (Original Exhibit, ELA Residual Matrix, and Tamper Heatmap Overlay), synchronized Tri-Spectral Forensic Evidence Decomposition gallery, parallel multi-model classification cards, raw confidence readouts, execution latencies, peak memory tracking, and persistent Benchmark Records (Logs and Records) table.
  * **Model Benchmark Suite:** Empirical performance table across both standard and compressed conditions, Section 2.10 Composite Scores, 3x2 ANOVA and Friedman statistical test analysis, Table 1 dataset composition overview, and comprehensive metric interpretation guide.
* **Zero-Emoji Enterprise Interface:**
  Adheres to strict institutional cybersecurity design standards with deep navy foundations (`#121620`), frosted glass panels (`#1C2333`), SVG line iconography, and typography powered by Inter and JetBrains Mono.

---

## System Architecture

The ForgeGuard system operates across a five-tier forensic pipeline:

```
[Uploaded GCash Receipt (JPG/PNG)]
         │
         ▼
[1. User Interface & Preprocessing Layer]
  • Mode Normalization (RGB)
  • JPEG Re-compression (Q = 90) & Pixel Residual Amplification (15.0x)
  • Preprocessing Resizing (224 x 224 x 3) & Normalization (/ 255.0)
  • Dynamic Input Tensor Adaptation
         │
         ▼
[2. Parallel CNN Inference Engine]
  ├── Basic CNN (~2.1M params, 86.27 ms standard, 74.25 ms compressed)
  ├── MobileNetV2 (~3.4M params, 91.43 ms standard, 84.63 ms compressed)
  └── ResNet50 (~23.5M params, 128.08 ms standard, 120.80 ms compressed)
         │
         ▼
[3. Result Processing & Telemetry Layer]
  • Independent Sigmoid Verdicts (Authentic < 0.50 <= Forged)
  • Probability Confidence Calculation
  • High-Resolution Execution Timer (perf_counter latency in ms)
  • Peak Working Set Memory Load (psutil RSS in MB)
         │
         ▼
[4. Database & Logging Layer]
  • Serialized Model Weights (HDF5 / Keras format)
  • Benchmark Records (Logs and Records): Prediction result, Confidence score,
    Processing time, Memory load, Date and time
         │
         ▼
[5. Presentation Layer (Streamlit)]
  • Synchronized Multi-Model Verdict Cards
  • ELA Exhibit Display & Tri-Spectral Heatmap
  • Full Empirical Benchmark Suite & Section 2.10 Composite Scores
```

---

## Empirical Benchmark Evaluation

All architectures were evaluated on the balanced 1:1 empirical test partition ($N = 225$ per seed: 112 Authentic, 56 Digitally Edited, 57 AI-Generated; 5 predetermined seeds: `[42, 101, 202, 303, 404]`) across both Standard and Compressed conditions:

### Standard Evaluation Condition (Uncompressed PNG)
*Partition Size: N = 225 per seed (112 Authentic, 56 Digitally Edited, 57 AI-Generated)*

| Architecture | Condition | Accuracy | Precision | Recall | F1-Score | End-to-End Latency | Peak Memory | Composite Score |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Basic CNN** | Standard | **91.82% &plusmn; 1.77%** | **98.16% &plusmn; 0.43%** | **85.31% &plusmn; 3.39%** | **91.25% &plusmn; 2.03%** | **86.27 &plusmn; 8.59 ms** | **659.8 MB** | **100.00%** |
| **MobileNetV2** | Standard | **82.22% &plusmn; 2.35%** | **78.57% &plusmn; 3.03%** | **89.56% &plusmn; 1.42%** | **83.64% &plusmn; 1.98%** | **91.43 &plusmn; 2.79 ms** | **665.5 MB** | **71.50%** |
| **ResNet50** | Standard | **53.42% &plusmn; 0.99%** | **51.88% &plusmn; 0.52%** | **100.00% &plusmn; 0.00%** | **68.32% &plusmn; 0.44%** | **128.08 &plusmn; 4.71 ms** | **670.9 MB** | **0.00%** |

### Compressed Evaluation Condition (Simulated Transmission Compression)
*Partition Size: N = 225 per seed (112 Authentic, 56 Digitally Edited, 57 AI-Generated)*

| Architecture | Condition | Accuracy | Delta | Precision | Recall | F1-Score | End-to-End Latency | Peak Memory | Composite Score |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Basic CNN** | Compressed | **91.73% &plusmn; 1.50%** | **-0.09%** | **98.57% &plusmn; 0.50%** | **84.78% &plusmn; 3.06%** | **91.12% &plusmn; 1.77%** | **74.25 &plusmn; 2.56 ms** | **671.7 MB** | **100.00%** |
| **MobileNetV2** | Compressed | **87.82% &plusmn; 2.04%** | **+5.60%** | **88.50% &plusmn; 2.27%** | **87.26% &plusmn; 1.83%** | **87.78% &plusmn; 1.99%** | **84.63 &plusmn; 5.90 ms** | **672.0 MB** | **66.85%** |
| **ResNet50** | Compressed | **49.24% &plusmn; 0.91%** | **-4.18%** | **49.71% &plusmn; 0.44%** | **93.98% &plusmn; 1.70%** | **64.99% &plusmn; 0.77%** | **120.80 &plusmn; 5.34 ms** | **672.1 MB** | **0.00%** |

> **Key Research Finding:** The compact custom Basic CNN demonstrated superior accuracy (91.82% standard, 91.73% compressed) and lowest end-to-end latency (74.25 ms compressed) compared to heavier transfer-learning architectures, with near-zero false alarms (mean FP = 1.8 of 112 authentic receipts). MobileNetV2 showed exceptional resilience under Messenger compression (+5.60% accuracy increase) with high recall on diffusion-generated fakes. ResNet50 over-fitted to background compression noise, generating high false positive rates (mean FP = 105 of 112 authentic), confirming that excessive network depth degrades ELA residual signal discrimination for digital transaction receipts.

---

## Empirical Dataset Specifications

The benchmark dataset consists of a 1:1 balanced distribution of 1,000 base downloadable GCash transaction receipts (and their paired 1,000 Messenger-compressed versions):

```
Empirical Evaluation Dataset (N = 1,000 Base Receipts)
├── Experimental Partition (N = 900 Images)
│   ├── Authentic Receipts (450 Images, 50.0%)
│   └── Forged Receipts (450 Images, 50.0%)
│       ├── Digitally Edited (Photoshop / Pixelmator): 225 Images (25.0%)
│       └── AI Diffusion Generated (Reference-Conditioned): 225 Images (25.0%)
│   ├── Training Split (60%): 540 Images (270 Auth, 135 Edited, 135 Gen)
│   ├── Validation Split (15%): 135 Images (67 Auth, 34 Edited, 34 Gen)
│   └── Testing Split (25%): 225 Images (112 Auth, 56 Edited, 57 Gen)
└── Holdout Evaluation Partition (N = 100 Images)
    ├── Unseen Authentic Receipts: 50 Images
    └── Unseen Third-Party Forgeries (Canva / Web Generators): 50 Images
```

*Scope Delimitation (Section 1.4):* The dataset strictly targets officially downloaded GCash transaction receipts. Screen captures containing operating system status bars, battery indicators, and mobile UI chrome are excluded to ensure controlled forensic evaluation.

---

## Quickstart & Local Deployment

### Prerequisites
* Python 3.10, 3.11, or 3.12
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

# Activate virtual environment
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Linux/macOS:
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt
```

### 3. Launch Local Forensic Webapp
```bash
streamlit run app.py
```
Open your browser and navigate to `http://localhost:8501`.

---

## Project Structure

```
ForgeGuard/
├── app.py                      # Root Streamlit deployment entrypoint
├── premium_css.py              # Dark forensic styling system & layout overrides
├── requirements.txt            # System Python dependencies
├── models/                     # Serialized neural network weights & evaluation telemetry
│   ├── basic_cnn.keras         # Serialized Basic CNN model weights
│   ├── mobilenetv2.keras       # Serialized MobileNetV2 model weights
│   ├── resnet50.keras          # Serialized ResNet50 model weights
│   └── evaluation_metrics.json # Empirical benchmark metrics
├── preprocessing/              # Forensic processing tools
│   └── ela.py                  # Error Level Analysis computation engine
├── generator/                  # GCash receipt template synthesis engine
└── dataset/                    # Labeled empirical receipt corpus
    ├── authentic/              # Authentic receipts (highres & compressed)
    └── forged/                 # Stratified forgery attack vectors
```

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
