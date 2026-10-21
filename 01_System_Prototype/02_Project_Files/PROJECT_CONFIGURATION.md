# Project and Environment Configuration Guide

## Notre Dame of Midsayap College
**College of Information Technology and Engineering (CITE)**  
**Bachelor of Science in Computer Science (BSCS)**  
**Subject:** CS Thesis Writing 1 (A.Y. 2026–2027)

---

### System Identity & Research Profile
* **System Name:** ForgeGuard
* **Approved Canonical Title:** Receipt or Deceit: A Cross-Architecture Analysis of Convolutional Neural Network Models in Detecting Forged Digital Transaction Receipts
* **Authors:** Daniela S. Ungab & Rogie P. Bacanto (BSCS-4)
* **Adviser:** Ms. Doris Ann Mariano
* **Instructor:** Mr. Nero L. Hontiveros

---

## 1. Directory Purpose & Contents

This folder contains the core execution configuration and dependency requirements for running the **ForgeGuard** system prototype in both local offline and cloud production environments.

### Manifest of Configuration Files
| Filename | Description | Purpose |
| :--- | :--- | :--- |
| `requirements.txt` | Python Package Specifications | Specifies pinned dependencies for the neural network and web runtime |
| `runtime.txt` | Python Engine Specification | Pinpoints Python runtime version (`python-3.12.10`) for cloud deployment |
| `.streamlit/config.toml` | Streamlit Engine Configuration | Configures forensic dark cyber-theme, server ports, and headless execution flags |

---

## 2. Hardware and Software Environment

### Minimum Hardware Requirements
* **Processor (CPU):** Intel Core i3 / AMD Ryzen 3 (2.0 GHz dual-core or higher)
* **System Memory (RAM):** 4 GB RAM minimum (8 GB recommended for simultaneous 3-model inference)
* **Storage:** 500 MB free space (encompasses full serialized model weights)
* **Display:** 1280 x 720 minimum resolution (optimized for 1366x768 to 1920x1080)

### Software Prerequisites
* **Operating System:** Windows 10/11, Ubuntu 20.04+, or macOS 12+
* **Python Runtime:** Python 3.10 to Python 3.12 (Validated on Python 3.12.10)
* **Package Manager:** `pip` version 23.0 or higher

---

## 3. Dependency Manifest (`requirements.txt`)

```text
streamlit>=1.30.0
tensorflow-cpu==2.20.0
Pillow>=10.0.0
numpy>=1.24.0,<2.0.0
psutil>=5.9.0
h5py>=3.10.0
```

### Dependency Rationale
1. **`streamlit` (>=1.30.0):** Provides the enterprise web dashboard, telemetry caching, and interactive multi-tab layout without heavy frontend frameworks.
2. **`tensorflow-cpu` (==2.20.0):** Provides optimized CPU tensor graph execution for Basic CNN, MobileNetV2, and ResNet50 models without requiring dedicated Nvidia CUDA hardware.
3. **`Pillow` (>=10.0.0):** Drives the mathematical Error Level Analysis (ELA) signal decomposition pipeline via controlled in-memory JPEG re-compression.
4. **`numpy` (>=1.24.0, <2.0.0):** Executes vectorized pixel difference operations, standard deviation calculations, and array normalizations for tamper heatmaps.
5. **`psutil` (>=5.9.0):** Monitors real-time process memory load (MB) during inference for academic telemetry logging.
6. **`h5py` (>=3.10.0):** Supports HDF5 tensor serialization for Keras weight loading.

---

## 4. Execution Configuration (`.streamlit/config.toml`)

```toml
[server]
headless = true
enableCORS = false
enableXsrfProtection = false
maxUploadSize = 25

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#2563eb"
backgroundColor = "#020617"
secondaryBackgroundColor = "#0b1222"
textColor = "#e2e8f0"
font = "sans serif"
```

The configuration locks the user interface into ForgeGuard's high-contrast forensic dark palette (`#020617` background, `#0b1222` surface containers, `#2563eb` cyber accents) and sets a 25 MB file upload ceiling for receipt images.
