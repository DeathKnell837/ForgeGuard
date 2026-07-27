# 🛡️ ForgeGuard — Real-Time Digital Receipt Forgery Detection Web Application

[![Live App](https://img.shields.io/badge/Live_App-forgeguard.streamlit.app-8B5CF6?style=for-the-badge&logo=streamlit)](https://forgeguard.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13+-FF6F00?style=for-the-badge&logo=tensorflow)](https://tensorflow.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io)

**ForgeGuard** is an AI-powered image forensic web application built to detect digital tampering and forgery in mobile wallet receipt screenshots (GCash and Maya). It combines **Error Level Analysis (ELA)** image preprocessing with a real-time comparative matrix of **three Convolutional Neural Network (CNN) architectures** (MobileNetV2, ResNet50, and Basic CNN).

---

## 💻 Quick Start & Local Setup

### 1. Prerequisites
- Python 3.10 or higher
- Git

### 2. Installation
```bash
# Clone repository
git clone https://github.com/DeathKnell837/ForgeGuard.git
cd ForgeGuard

# Install dependencies
pip install -r requirements.txt
```

### 3. Run Web Application
```bash
streamlit run webapp/app.py
```
Open your browser at `http://localhost:8501`.

---

## ⚡ Core Software Modules

| Module Path | Description |
|:---|:---|
| **`webapp/app.py`** | Main Streamlit user interface with live ELA preview, model selector, and controls |
| **`preprocessing/ela.py`** | Error Level Analysis engine for computing pixel compression error heatmaps |
| **`tools/receipt_forger.py`** | Digital editing simulation script (Photoshop / Gallery alteration mode) |
| **`tools/gcash_receipt_generator.py`** | Synthetic GCash receipt generator for ground-truth testing |
| **`dataset/`** | 408 labeled receipt screenshots (104 Authentic + 304 Forged) |
| **`models/`** | Saved CNN model weights (`.keras` / `.h5` format) |

---

## 🧠 Neural Network Model Specifications

1. **MobileNetV2 (★ Recommended):**
   - ~3.4 Million Parameters
   - Inverted Residual Bottlenecks optimized for lightweight GPU-free inference.
2. **ResNet50:**
   - ~23.5 Million Parameters
   - Deep residual network benchmark for high-capacity feature extraction.
3. **Basic CNN:**
   - ~2.1 Million Parameters
   - 3-layer convolutional baseline model for comparative benchmarking.

---

## 🌐 Live Streamlit Cloud Deployment
This repository is configured for automatic deployment on **Streamlit Cloud**:
- Entrypoint file: `webapp/app.py`
- Live URL: [forgeguard.streamlit.app](https://forgeguard.streamlit.app/)
