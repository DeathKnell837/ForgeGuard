# ForgeGuard: Cross-Architecture CNN Digital Receipt Forgery Detection System

<div align="center">

[![Live Application](https://img.shields.io/badge/Live_System-forgeguard.streamlit.app-8B5CF6?style=for-the-badge&logo=streamlit)](https://forgeguard.streamlit.app/)
[![Python Version](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![TensorFlow Engine](https://img.shields.io/badge/TensorFlow-2.13+-FF6F00?style=for-the-badge&logo=tensorflow)](https://tensorflow.org)
[![Peak Accuracy](https://img.shields.io/badge/Peak_Accuracy-99.56%25-10B981?style=for-the-badge)](https://forgeguard.streamlit.app/)
[![Fastest Latency](https://img.shields.io/badge/Fastest_Latency-22.51ms-06B6D4?style=for-the-badge)](https://forgeguard.streamlit.app/)
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
  * **Basic CNN (Baseline):** Custom 3-block convolutional network (~2.1M parameters) achieving **92.92%** standard accuracy (22.51 ms latency) and **99.56%** compressed accuracy (24.12 ms latency).
  * **MobileNetV2 (Efficient):** Inverted residual depthwise separable CNN (~3.4M parameters) achieving **86.06%** standard accuracy (215.75 ms latency) and **93.42%** compressed accuracy (221.40 ms latency).
  * **ResNet50 (Deep Residual):** 50-layer deep network (~23.5M parameters) exhibiting 53.54% standard accuracy (395.03 ms latency), demonstrating the empirical limits of deep feature extractors on compression residual artifacts.
* **Two-Screen Operational Workflow:**
  * **Classify a Receipt:** Real-time upload interface featuring tabbed forensic inspection (Original Exhibit, ELA Residual Matrix, and Tamper Heatmap Overlay), synchronized Tri-Spectral Forensic Evidence Decomposition gallery, parallel multi-model classification cards, raw confidence readouts, and execution latencies.
  * **Model Benchmark Suite:** Empirical performance table across both standard and compressed conditions, interactive confusion matrix breakdown, dataset distribution overview, and comprehensive metric interpretation guide.
* **Zero-Emoji Enterprise Interface:**
  Adheres to strict institutional cybersecurity design standards with deep navy foundations (`#121620`), frosted glass panels (`#1C2333`), SVG line iconography, and typography powered by Inter and JetBrains Mono.

---

## System Architecture

The ForgeGuard system operates across a five-tier forensic pipeline:

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
[2. Parallel Model Inference Layer]
  ├── Basic CNN (~2.1M params, 22.51 ms)
  ├── MobileNetV2 (~3.4M params, 215.75 ms)
  └── ResNet50 (~23.5M params, 395.03 ms)
         │
         ▼
[3. Decision & Telemetry Layer]
  • Independent Sigmoid Verdicts (Authentic < 0.50 <= Forged)
  • Confidence Percentage Calculation
  • High-Resolution Execution Timer (perf_counter)
         │
         ▼
[4. Presentation Layer (Streamlit)]
  • Synchronized Multi-Model Verdict Cards
  • ELA Exhibit Display
  • Full Empirical Benchmark Suite & Interpretation Guide
```

---

## Empirical Benchmark Evaluation

All models were evaluated on a dedicated balanced test set under both uncompressed (standard) and compressed conditions:

### Standard Evaluation Condition (Uncompressed PNG)
*Total Samples: 452 (226 Authentic, 226 Forged)*

| Architecture | Condition | Accuracy | Precision | Recall | F1-Score | Inference Latency | Peak Memory | Parameters |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Basic CNN** | Standard | **92.92%** | **98.99%** | **86.73%** | **92.45%** | **22.51 ms** | **23.3 MB** | **~2.1M** |
| **MobileNetV2** | Standard | **86.06%** | **89.76%** | **81.42%** | **85.38%** | **215.75 ms** | **71.3 MB** | **~3.4M** |
| **ResNet50** | Standard | **53.54%** | **51.83%** | **100.00%** | **68.28%** | **395.03 ms** | **638.8 MB** | **~23.5M** |

### Compressed Evaluation Condition (Simulated Transmission Compression)
*Total Samples: 456 (228 Authentic, 228 Forged)*

| Architecture | Condition | Accuracy | Delta | Precision | Recall | F1-Score | Inference Latency | Peak Memory | Parameters |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Basic CNN** | Compressed | **99.56%** | **+6.64%** | **99.56%** | **99.56%** | **99.56%** | **24.12 ms** | **23.3 MB** | **~2.1M** |
| **MobileNetV2** | Compressed | **93.42%** | **+7.36%** | **92.67%** | **94.30%** | **93.48%** | **221.40 ms** | **71.3 MB** | **~3.4M** |
| **ResNet50** | Compressed | **53.95%** | **+0.41%** | **52.05%** | **100.00%** | **68.47%** | **405.18 ms** | **638.8 MB** | **~23.5M** |

> **Key Research Finding:** The compact custom Basic CNN demonstrated superior accuracy (92.92% standard, 99.56% compressed) and lowest inference latency (22.51 ms) compared to heavier transfer-learning architectures. ResNet50 over-fitted to compression artifacts, classifying all inputs as forged (100% recall, 51.83% precision), empirically confirming that excessive network depth degrades ELA residual signal discrimination.

---

## Empirical Dataset Specifications

The benchmark dataset consists of a 1:1 balanced distribution of downloadable GCash transaction receipts:

```
Empirical Evaluation Dataset (N = 456 Base Receipts)
├── Authentic Receipts: 228 Images (50.0%)
│   ├── High-Resolution Uncompressed Receipts: 228
│   └── Compressed Re-Encoded Receipts: 228
└── Forged Receipts: 228 Images (50.0%)
    ├── Amount Alterations (Karla-Bold digital modifications): 45
    ├── Reference Number Fabrications (13-digit checksum tampering): 45
    ├── Recipient Name Modifications (Poppins-SemiBold alterations): 45
    ├── Font Tampering & Typography Splicing: 45
    ├── Full Template Synthesis: 24
    └── AI Template & Diffusion Generations: 24
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
