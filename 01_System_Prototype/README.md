# ForgeGuard System Prototype

## Notre Dame of Midsayap College
**College of Information Technology and Engineering (CITE)**  
**Bachelor of Science in Computer Science (BSCS)**  
**Subject:** CS Thesis Writing 1 (A.Y. 2026–2027)

---

### **Receipt or Deceit: A Cross-Architecture Analysis of Convolutional Neural Network Models in Detecting Forged Digital Transaction Receipts**

* **System Name:** ForgeGuard
* **Authors:** Daniela S. Ungab & Rogie P. Bacanto (BSCS-4)
* **Thesis Adviser:** Ms. Doris Ann Mariano
* **Instructor:** Mr. Nero L. Hontiveros
* **Live Deployment:** [forgeguard.streamlit.app](https://forgeguard.streamlit.app/)

---

## 1. System Overview

**ForgeGuard** is an AI-driven image forensics system designed to detect raster tampering, digital amount splicing, font forgery, and synthetic generation in digital proof-of-payment confirmation slips, specifically within the Philippine **GCash** mobile transaction ecosystem.

The system integrates mathematical **Error Level Analysis (ELA)** signal decomposition with a comparative evaluation of three benchmarked Convolutional Neural Network (CNN) architectures:
1. **Basic CNN (Custom Sequential Baseline, ~3.3M parameters):** Optimized for low latency and high precision on compression residuals.
2. **MobileNetV2 (Inverted Residual Architecture, ~2.4M parameters):** Lightweight mobile architecture demonstrating strong resilience under Facebook Messenger re-compression.
3. **ResNet50 (Deep 50-Layer Residual Network, ~24.1M parameters):** Benchmark deep residual network illustrating the performance boundaries of deep representations on fine compression noise.

---

## 2. Directory Structure

```
01_System_Prototype/
├── README.md                      # Complete system documentation & execution guide
├── requirements.txt               # Python package dependencies
├── runtime.txt                    # Target Python runtime specification (python-3.12.10)
├── run_system.bat                 # One-click Windows launch script
├── src/                           # Clean system source code
│   ├── app.py                     # Primary Streamlit web application
│   ├── premium_css.py             # Cyber-forensics CSS design system
│   ├── assets/                    # System branding, icons, vector graphics
│   ├── samples/                   # Pre-loaded benchmark sample receipts
│   ├── preprocessing/             # ELA extraction & forensic visualizer
│   │   ├── __init__.py
│   │   ├── ela.py                 # Mathematical Error Level Analysis engine (Q=90, 15.0x)
│   │   └── ai_forensics.py        # Heatmap overlay generator & anomaly statistics
│   ├── evaluation/                # Empirical evaluation & 5-seed benchmark scripts
│   │   ├── evaluate_compressed.py
│   │   └── evaluate_balanced_5seeds.py
│   └── training/                  # Model training pipeline
│       └── train.py
├── models/                        # Serialized Keras neural network models
│   ├── basic_cnn.keras            # Trained Basic CNN model weights
│   ├── mobilenetv2.keras          # Trained MobileNetV2 model weights
│   ├── resnet50.keras             # Trained ResNet50 model weights
│   ├── evaluation_metrics.json    # Full empirical benchmark metrics (5 seeds)
│   └── pure_empirical_benchmark.json
├── database/                      # Persistent records & audit logs
│   └── benchmark_records_log.json # JSON transaction verification log
└── screenshots/                   # Prototype visual documentation
    ├── 01_home_dashboard.png
    ├── 02_authentic_receipt_analysis.png
    ├── 03_forged_edited_receipt_analysis.png
    ├── 04_ela_residual_matrix.png
    ├── 05_tamper_heatmap_overlay.png
    ├── 06_overall_architecture_benchmark.png
    ├── 07_empirical_dataset_composition.png
    ├── 08_benchmark_records_telemetry.png
    └── SCREENSHOT_DESCRIPTIONS.md  # Detailed annotations for each exhibit
```

---

## 3. Hardware & Software Specifications

### Minimum Hardware Specifications
* **Processor (CPU):** Intel Core i3 / AMD Ryzen 3 or equivalent dual-core processor (2.0 GHz+)
* **System Memory (RAM):** 4 GB RAM minimum (8 GB recommended for parallel model loading)
* **Storage:** 500 MB free hard drive space (includes trained `.keras` model weights)
* **Display Resolution:** 1280 x 720 minimum (optimized for 1366x768 laptop up to 1920x1080 desktop displays)

### Software & Environment Specifications
* **Operating System:** Windows 10/11, macOS, or Linux (Ubuntu 20.04+)
* **Python Runtime:** Python 3.10 to Python 3.12 (Tested on Python 3.12.10)
* **Core Libraries:**
  * `streamlit` >= 1.30.0 (Interactive dashboard presentation)
  * `tensorflow-cpu` == 2.20.0 (Neural network graph execution)
  * `Pillow` >= 10.0.0 (Image processing & ELA re-compression)
  * `numpy` >= 1.24.0, < 2.0.0 (Tensor mathematics)
  * `psutil` >= 5.9.0 (Real-time memory telemetry)
  * `h5py` >= 3.10.0 (Serialized weight loading)

---

## 4. Installation & Execution Guide

### Method A: Quick Launch via Batch Script (Windows)
1. Double-click `run_system.bat`.
2. The script will automatically verify the Python environment, check dependencies, and launch the web interface in your default browser.

### Method B: Manual Command-Line Execution
1. Open a terminal or PowerShell prompt in this folder (`01_System_Prototype`).
2. (Optional) Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit application:
   ```bash
   streamlit run src/app.py
   ```
5. Open your web browser and navigate to `http://localhost:8501`.

---

## 5. System Features & Operations

1. **Receipt Verification:** Upload any downloadable GCash transaction receipt (or click one of the pre-loaded sample buttons) to trigger instant parallel classification across Basic CNN, MobileNetV2, and ResNet50.
2. **Forensic Evidence Inspection:** Switch between the **Original Exhibit**, the **ELA Residual Matrix** (Q=90 JPEG error amplification), and the **Tamper Heatmap** overlay to localize manipulated regions.
3. **Model Benchmark Suite:** Open the sidebar navigation and select **Model Comparison** to inspect the centered empirical performance matrix, compression degradation deltas, confusion matrix distributions, and Table 1 dataset composition.
4. **Audit Logging:** All analyzed receipts automatically append an entry to the persistent Benchmark Records log (`database/benchmark_records_log.json`).
