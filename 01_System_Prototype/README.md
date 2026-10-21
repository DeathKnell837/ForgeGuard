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

## 1. Submission Structure (NDMC Thesis Writing 1 Syllabus Alignment)

In strict accordance with the NDMC BSCS Thesis Writing 1 Submission Guidelines (**Section III. Required Subfolders: 1. System or Prototype - `01_System_Prototype`**), this folder and its corresponding archive (`01_System_Prototype.zip`) are structured into the six numbered subfolders matching the rubric bullet points:

```
01_System_Prototype/
├── README.md                              # Master prototype documentation and folder index
├── run_system.bat                         # One-click Windows offline launcher
│
├── 01_Source_Code/                        # Content Item 1: Source code
│   ├── app.py                             # Canonical Streamlit application
│   ├── premium_css.py                     # High-contrast cyber-forensics design system
│   ├── assets/                            # Brand logos, SVG icons, and telemetry graphics
│   ├── preprocessing/                     # ELA mathematical engine and forensic heatmaps
│   │   ├── __init__.py
│   │   ├── ela.py                         # Error Level Analysis (Q=90, 15.0x scale)
│   │   └── ai_forensics.py                # Anomaly statistics and thermal colormaps
│   ├── samples/                           # Bundled verification receipts for offline demos
│   └── .streamlit/
│       └── config.toml                    # Local application UI and dark theme configuration
│
├── 02_Project_Files/                      # Content Item 2: Project files
│   ├── requirements.txt                   # Complete pinned pip dependency manifest
│   ├── runtime.txt                        # Python 3.12 runtime specification
│   ├── PROJECT_CONFIGURATION.md           # Hardware & software environment guidelines
│   └── .streamlit/
│       └── config.toml                    # Server and dark forensic theme parameters
│
├── 03_Prototype_Files/                    # Content Item 3: Prototype files
│   ├── basic_cnn.keras                    # Compiled Basic CNN model weights (~3.3M params)
│   ├── mobilenetv2.keras                  # Compiled MobileNetV2 model weights (~2.4M params)
│   ├── resnet50.keras                     # Compiled ResNet50 model weights (~24.1M params)
│   ├── evaluation_metrics.json            # 5-seed centered empirical benchmark metrics
│   ├── pure_empirical_benchmark.json      # Raw per-seed evaluation records
│   ├── benchmark_records_log.json         # Prototype model audit trail mirror
│   └── MODEL_SPECIFICATIONS.md            # Architecture specs, layer depths, and parameters
│
├── 04_Database_Files/                     # Content Item 4: Database files
│   ├── benchmark_records_log.json         # Active JSON transaction audit ledger
│   └── DATABASE_SPECIFICATIONS.md         # Schema documentation and telemetry logging rules
│
├── 05_Other_Development_Files/            # Content Item 5: Other related development files
│   ├── train.py                           # Multi-architecture training pipeline
│   ├── ForgeGuard_Model_Training.ipynb    # Interactive Google Colab / Jupyter notebook
│   ├── evaluate_balanced_5seeds.py        # 5-seed randomized empirical benchmark harness
│   ├── evaluate_compressed.py             # Messenger re-compression robustness harness
│   ├── DEVELOPMENT_PIPELINE.md            # Experimental workflow and training guidelines
│   ├── authentic.jpg                      # Downloadable authentic GCash confirmation slip
│   ├── edited.jpg                         # Tampered GCash receipt (spliced PHP 50,000.00)
│   ├── generated.jpg                      # Synthetic AI/Canva fraudulent confirmation slip
│   └── samples/                           # Preset exhibit directory for path compatibility
│
└── 06_Screenshots_with_Descriptions/      # Content Item 6: Screenshots with descriptions (required)
    ├── 01_home_dashboard.png              # Exhibit 1: System landing and intake interface
    ├── 02_authentic_receipt_analysis.png  # Exhibit 2: Genuine receipt multi-CNN classification
    ├── 03_forged_edited_receipt_analysis.png # Exhibit 3: Spliced amount forgery detection
    ├── 04_ela_residual_matrix.png         # Exhibit 4: ELA Q=90 residual error amplification
    ├── 05_tamper_heatmap_overlay.png      # Exhibit 5: Thermal anomaly localization heatmap
    ├── 06_overall_architecture_benchmark.png # Exhibit 6: Cross-architecture performance matrix
    ├── 07_empirical_dataset_composition.png # Exhibit 7: Table 1 dataset partition breakdown
    ├── 08_benchmark_records_telemetry.png # Exhibit 8: Real-time audit ledger telemetry
    ├── SCREENSHOT_DESCRIPTIONS.md          # Comprehensive academic annotations for each exhibit
    └── System_Prototype_Screenshots.docx  # Formal Word exhibit document with captions
    │   └── System_Prototype_Screenshots.pdf   # Formal print-ready PDF exhibit with embedded screenshots
```

---

## 2. Quick Execution Guide

### Method A: One-Click Offline Launcher (Windows)
1. Double-click `run_system.bat` located at the root of `01_System_Prototype/`.
2. The launcher will automatically detect Python (`python` or `py`), verify dependencies, and launch the ForgeGuard web application in your default browser at `http://localhost:8501`.

### Method B: Manual Terminal Execution
1. Open a terminal or PowerShell prompt in `01_System_Prototype/`.
2. (Optional) Activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```powershell
   pip install -r 02_Project_Files/requirements.txt
   ```
4. Run the Streamlit application:
   ```powershell
   streamlit run 01_Source_Code/app.py
   ```
5. Navigate to `http://localhost:8501` in any modern web browser.

---

## 3. System Highlights & Benchmark Summary

* **Task Domain:** Binary classification of downloadable GCash mobile transaction receipts into **Authentic** or **Forged** classes.
* **Forensic Feature Transform:** Dual-stage Error Level Analysis (JPEG Q=90, 15.0x scale amplification) and spatial thermal gradient overlays.
* **Architectures Evaluated:**
  * **Basic CNN:** Custom 3-stage sequential baseline (~3.3M parameters). Lowest inference latency (18.2 ms) and highest clean accuracy (98.5%).
  * **MobileNetV2:** Inverted residual architecture (~2.4M parameters). Highest resilience under Facebook Messenger re-compression (-5.0% delta).
  * **ResNet50:** Benchmark 50-layer deep residual network (~24.1M parameters).
* **Audit Trail:** Persistent local ledger (`04_Database_Files/benchmark_records_log.json`) recording timestamp, evaluated model, classification verdict, confidence percentage, processing latency, and memory load for every processed receipt.
