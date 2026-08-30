# 🛡️ ForgeGuard — Real-Time Digital Receipt Forgery Detection System

[![Live App](https://img.shields.io/badge/Live_App-forgeguard.streamlit.app-8B5CF6?style=for-the-badge&logo=streamlit)](https://forgeguard.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13+-FF6F00?style=for-the-badge&logo=tensorflow)](https://tensorflow.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io)

**ForgeGuard** is an AI-powered image forensic application that detects digital tampering and forgery in GCash mobile wallet receipt screenshots. It combines **Error Level Analysis (ELA)** image preprocessing with a real-time comparative evaluation of **three Convolutional Neural Network (CNN) architectures** (Basic CNN, MobileNetV2, ResNet50).

---

## 📊 Empirical Model Performance Results (Google Colab GPU)

| CNN Architecture | Parameters | Accuracy | Precision | Recall | F1-Score | Latency (ms) | Colab Train Time |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 🥇 **Basic CNN** | **~2.1M** | **100.00%** | **100.00%** | **100.00%** | **1.0000** | **8.61 ms** | 198.50 s |
| 🥈 **MobileNetV2** | **~3.4M** | **95.74%** | **94.67%** | **100.00%** | **0.9726** | **28.04 ms** | **76.59 s** |
| 🥉 **ResNet50** | **~23.5M** | **75.53%** | **75.53%** | **100.00%** | **0.8606** | **109.34 ms** | 413.11 s |

---

## 🖼️ Dataset v2.2.0 Summary (777 Labeled Images)

- **Authentic Receipts (153 Images):** 51 real original GCash screenshots + 102 clean augmented receipts.
- **Forged Receipts (624 Images):**
  - `amount_alteration`: 153 images (Flawless Karla-Bold digital edits in GCash `#1972F9` blue)
  - `ref_fabrication`: 153 images (Flawless Karla-Regular 13-digit ref edits)
  - `name_modification`: 153 images (Flawless Poppins-SemiBold name edits)
  - `ai_generated_template`: 153 images (Full AI synthetic templates)
  - `full_template`: 12 images (Legacy templates)

---

## 💻 Quick Start & Local Setup

### 1. Installation & Dependencies
```bash
# Clone repository
git clone https://github.com/DeathKnell837/ForgeGuard.git
cd ForgeGuard/thesis-system

# Install dependencies
pip install -r ../requirements.txt
```

### 2. Run Live Web Application
```bash
streamlit run webapp/app.py
```
Open browser at `http://localhost:8501`.

### 3. Model Training Pipeline
To train or re-evaluate the models on Google Colab GPU:
Open 👉 **[`training/ForgeGuard_Model_Training.ipynb`](training/ForgeGuard_Model_Training.ipynb)** on Google Colab and click **Runtime $\rightarrow$ Run all**.

---

## ⚡ Core System Directory

| Directory / File | Description |
|:---|:---|
| **`assets/fonts/`** | Official Karla (`Karla-Regular.ttf`, `Karla-Bold.ttf`) and Poppins (`Poppins-Bold.ttf`, `Poppins-SemiBold.ttf`) fonts |
| **`dataset/`** | Dataset v2.2.0 containing 777 labeled samples & `metadata.json` |
| **`models/`** | Trained `.keras` weights (`basic_cnn.keras`, `mobilenetv2.keras`, `resnet50.keras`) and `evaluation_metrics.json` |
| **`preprocessing/ela.py`** | Error Level Analysis (ELA) engine ($Q=90$, scale factor=15.0) |
| **`tools/generate_proper_forgeries.py`** | High-precision digital forgery generator |
| **`tools/gcash_receipt_generator.py`** | Synthetic GCash receipt generator |
| **`training/train.py`** | TensorFlow/Keras multi-architecture model training script |
| **`webapp/app.py`** | Streamlit interactive web interface with live ELA heatmaps & comparative metrics |
