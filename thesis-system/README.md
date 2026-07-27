# 🛡️ ForgeGuard — Mobile Wallet Receipt Forgery Detection System

[![Live Demo](https://img.shields.io/badge/Live_Demo-forgeguard.streamlit.app-8B5CF6?style=for-the-badge&logo=streamlit)](https://forgeguard.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13+-FF6F00?style=for-the-badge&logo=tensorflow)](https://tensorflow.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io)

### **BSCS Thesis:** *"Securing Mobile Transaction: A Comparative Evaluation of CNN Architectures in Detecting Digital Receipt Forgery"* (NDMC CITE, 2026)

---

## 🚀 System Architecture & Features

1. **Evidence Acquisition:** Single-image receipt screenshot upload (GCash/Maya) or live camera capture.
2. **Forensic Compute Engine:** Error Level Analysis (ELA) preprocessing to highlight re-compression and pixel alteration error maps.
3. **Multi-Model Evaluation Matrix:** Real-time comparative inference across three CNN architectures:
   - **Basic CNN (~2.1M params):** Baseline architecture
   - **ResNet50 (~23.5M params):** Deep residual feature extractor
   - **MobileNetV2 (~3.4M params):** Recommended lightweight mobile-optimized architecture
4. **Synthetic Evidence Generator:** Built-in GCash receipt generator producing authentic and 4 forgery artifact modes for ground-truth testing.

---

## 📊 Dataset Status (v2.0.0)

* **Authentic Receipts:** 104 samples
* **Forged Receipts:** 304 samples (104 Photoshop/Gallery digitally edited + 200 programmatically generated)
* **Total Labeled Data:** 408 images

---

## 📂 System Directory Layout

```
thesis-system/
├── dataset/             # 408 labeled authentic & forged receipt images
├── preprocessing/       # ELA image compute module (ela.py)
├── tools/               # GCash receipt generator & digital forgery script
├── webapp/              # Streamlit application UI (app.py)
└── models/              # Saved model weights (.keras / .h5)
```
