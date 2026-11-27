# NDMC BSCS Thesis Research Workspace

<div align="center">

### **Notre Dame of Midsayap College**
**College of Information Technology and Engineering (CITE)**  
*Bachelor of Science in Computer Science (BSCS)*

---

## **Receipt or Deceit: A Cross-Architecture Analysis of Convolutional Neural Network Models in Detecting Forged Digital Transaction Receipts**

**System Name:** ForgeGuard  
**Academic Subject:** CS Thesis Writing 1 (A.Y. 2026–2027)

---

[![Thesis Status](https://img.shields.io/badge/Proposal-Chapters_1_%26_2_Completed-007ACC?style=for-the-badge)](thesis-docs/THESIS1UNGAB_BACANTO.md)
[![Title Defense](https://img.shields.io/badge/Title_Defense-PASSED-10B981?style=for-the-badge)](thesis-docs/)
[![Live System Demo](https://img.shields.io/badge/Live_System-forgeguard.streamlit.app-8B5CF6?style=for-the-badge&logo=streamlit)](https://forgeguard.streamlit.app/)
[![System Repo](https://img.shields.io/badge/System_Repo-DeathKnell837%2FForgeGuard-1E293B?style=for-the-badge&logo=github)](https://github.com/DeathKnell837/ForgeGuard)
[![Google Drive](https://img.shields.io/badge/Google_Drive-Thesis_Archive-F59E0B?style=for-the-badge&logo=googledrive)](https://drive.google.com/drive/folders/1bzRsI6Ywo2yRni5Ij7InCLh0CL0OO90_?usp=drive_link)

[Latest Manuscript (Word)](thesis-docs/THESIS1UNGAB_BACANTO.docx) &bull; [Latest Manuscript (Markdown)](thesis-docs/THESIS1UNGAB_BACANTO.md) &bull; [System Architecture](thesis-docs/forgeguard_system_architecture.svg) &bull; [Live Demo](https://forgeguard.streamlit.app/)

</div>

---

## Research Group & Faculty Profile

| Role | Name | Designation / Affiliation |
|:---|:---|:---|
| **Lead Researcher** | **Daniela S. Ungab** | BSCS-4 Student Candidate, NDMC CITE |
| **Co-Researcher** | **Rogie P. Bacanto** | BSCS-4 Student Candidate, NDMC CITE |
| **Thesis Adviser** | **Ms. Doris Ann Mariano** | Faculty Adviser, NDMC CITE |
| **Research Teacher** | **Mr. Nero L. Hontiveros** | CS Thesis Writing 1 Instructor |
| **Dean of CITE** | **Engr. Mark Bryan C. Tenebroso, PCPE, ME-CPE** | Dean, College of Information Technology & Engineering |
| **Academic Term** | **Academic Year 2026–2027** | CS Thesis Writing 1 (Enrolled, June 2026) |

---

### Research Overview & Abstract

Digital payment channels account for over **57.4% of monthly retail transactions** in the Philippines (Bangko Sentral ng Pilipinas 2024 Report). However, peer-to-peer mobile wallet confirmation receipts (specifically within the **GCash** ecosystem) have become a primary attack surface for receipt-based fraud. Scammers utilize image editing tools and programmatic template generators to modify transaction amounts, reference numbers, and recipient names without transferring actual funds.

Because proof-of-payment receipts shared over messaging platforms (Facebook Messenger) undergo lossy re-compression, conventional visual inspection and raw Error Level Analysis (ELA) frequently fail to expose subtle tampering. 

This study addresses this challenge through a **cross-architecture comparative evaluation of three Convolutional Neural Network (CNN) architectures**:
1. **Basic CNN (Custom sequential baseline, ~11.2M parameters at 224&times;224 input)**
2. **MobileNetV2 (Inverted residual mobile architecture, ~2.4M parameters)**
3. **ResNet50 (Deep 50-layer residual network, ~24.1M parameters)**

Each architecture is evaluated across both **Standard (high-resolution downloadable)** and **Compressed (Facebook Messenger re-compressed)** conditions across accuracy, precision, recall, F1-score, steady-state latency, and peak memory footprint.

---

## Statement of the Problem (SOP)

This research investigates the following specific research questions:

1. **Classification Performance:**
   * What is the diagnostic performance of Basic CNN, ResNet50, and MobileNetV2 in terms of **Accuracy**, **Precision**, **Recall**, and **F1-score**?
2. **Detection by Forgery Modality:**
   * What is the accuracy of each architecture across digitally edited receipts (amount, recipient name, reference number, font tampering) versus programmatically generated fake receipts?
3. **Computational Efficiency & Resource Footprint:**
   * What is the difference in **inference speed (ms)**, **peak memory (MB)**, and model footprint among the three architectures?
4. **Resilience to Messaging Platform Compression:**
   * Does social media compression (Facebook Messenger transmission) degrade or alter the detection efficacy of the CNN models?
5. **Practical Edge Deployability:**
   * Which CNN architecture provides the optimal balance of classification accuracy and execution latency for real-time mobile payment verification?

---

## Empirical Model Benchmark Results

All architectures were benchmarked under identical hardware conditions on the balanced 1:1 empirical test partition ($N = 225$ per seed: 112 Authentic, 56 Digitally Edited, 57 AI-Generated; 5 predetermined seeds; 224&times;224 ELA input per [docs/CHANGELOG_224.md](docs/CHANGELOG_224.md)) across both Standard and Compressed conditions:

| Architecture | Condition | Accuracy (%) | Compression Delta (&Delta;Acc) | Precision (%) | Recall (%) | F1-Score (%) | Latency (ms) | Peak Memory (MB) | Params | Composite Score | Architectural Finding |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **Basic CNN** | Standard | **94.58% &plusmn; 0.99%** | Baseline | **100.00% &plusmn; 0.00%** | **89.20% &plusmn; 1.97%** | **94.28% &plusmn; 1.09%** | **52.28 &plusmn; 0.90 ms** | **1004.9 MB** | **~11.2M** | **100.00%** | Most balanced, dependable model for uncompressed receipts; zero false alarms (mean FP=0 of 112 authentic). |
| **Basic CNN** | Compressed | **96.36% &plusmn; 1.03%** | **+1.78%** | **100.00% &plusmn; 0.00%** | **92.74% &plusmn; 2.05%** | **96.22% &plusmn; 1.10%** | **34.25 &plusmn; 2.38 ms** | **1019.1 MB** | **~11.2M** | **100.00%** | Top-performing architecture under Messenger compression; zero false alarms with 92.74% fraud detection rate. |
| **MobileNetV2** | Standard | **82.93% &plusmn; 1.53%** | Baseline | **94.53% &plusmn; 1.73%** | **70.09% &plusmn; 2.53%** | **80.47% &plusmn; 1.93%** | **56.21 &plusmn; 0.89 ms** | **1010.0 MB** | **~2.4M** | **73.11%** | Inverted residual mobile architecture; lightweight ~2.4M parameter footprint catching AI-generated fakes reliably. |
| **MobileNetV2** | Compressed | **89.87% &plusmn; 1.33%** | **+6.94%** | **100.00% &plusmn; 0.00%** | **79.82% &plusmn; 2.65%** | **88.76% &plusmn; 1.64%** | **38.48 &plusmn; 1.05 ms** | **1021.0 MB** | **~2.4M** | **72.85%** | Strong resilience under compression with +6.94% accuracy gain and zero false alarms. |
| **ResNet50** | Standard | **49.78% &plusmn; 0.00%** | Baseline | **0.00% &plusmn; 0.00%** | **0.00% &plusmn; 0.00%** | **0.00% &plusmn; 0.00%** | **79.11 &plusmn; 2.91 ms** | **1017.4 MB** | **~24.1M** | **0.00%** | Frozen ImageNet base failed to learn ELA residual signal, classifying every receipt as Authentic. |
| **ResNet50** | Compressed | **49.78% &plusmn; 0.00%** | **+0.00%** | **0.00% &plusmn; 0.00%** | **0.00% &plusmn; 0.00%** | **0.00% &plusmn; 0.00%** | **61.34 &plusmn; 1.47 ms** | **1022.1 MB** | **~24.1M** | **0.00%** | Heavy 24.1M footprint; highest end-to-end latency with zero forgery discrimination under frozen backbone. |

> **Key Takeaway:** Simpler, compact convolutional architectures (Basic CNN and MobileNetV2) decisively outperform heavy 50-layer deep networks for 224&times;224 ELA digital receipt verification. Section 2.10 Composite Scoring ranks Basic CNN as the optimal architecture for local merchant deployment.

---

## Dual Repository Architecture & Boundary Rules

To ensure clean separation between academic thesis documentation and live software engineering deployment, this research maintains two synchronized Git remotes:

| Remote | Target Repository | Scope & Purpose |
|:---|:---|:---|
| **`origin`** | [`DeathKnell837/NDMC-BSCS-THESIS-PREP`](https://github.com/DeathKnell837/NDMC-BSCS-THESIS-PREP) | **Academic Thesis Preparation Repository.** Contains all proposal documents (`thesis-docs/`), thesis manuscripts (`.docx` & `.md`), IEEE literature reviews, defense slides, guidelines, and research outlines. |
| **`forgeguard`** | [`DeathKnell837/ForgeGuard`](https://github.com/DeathKnell837/ForgeGuard) | **Software Engineering & Deployment Repository.** Contains the production Streamlit web application (`app.py`), serialized `.keras` models, ELA preprocessing engine, dataset generator tools, and deployment configs for [forgeguard.streamlit.app](https://forgeguard.streamlit.app/). |

### Non-Interference Push Policy
1. **Thesis Documentation updates** (`thesis-docs/`, manuscripts, proposal writing) must always be committed and pushed to `origin`.
2. **System & Webapp updates** (`thesis-system/`, models, UI components) are synced to `origin` (for complete archival) and pushed to `forgeguard` (for live Streamlit Cloud rebuilds).
3. The root `README.md` in `origin` represents the **Academic Thesis Workspace Hub**, while the root `README.md` in `forgeguard` represents the **ForgeGuard Software System Guide**.

---

## Workspace Directory Structure

```
THESIS/
├── README.md                           # Master Academic Workspace Hub (this file)
├── app.py                              # Streamlit Cloud deployment entrypoint
├── requirements.txt                    # System Python runtime dependencies
├── deploy-forgeguard.ps1               # Automated dual-remote deployment script
├── .agents/                            # Antigravity assistant customization rules
│   └── AGENTS.md                       # Canonical rules, boundary policies & thesis context
├── thesis-docs/                        # ACADEMIC THESIS DOCUMENTATION (Manuscripts & Guidelines)
│   ├── THESIS1UNGAB_BACANTO.docx       # Official compiled Chapters 1 & 2 Word Document
│   ├── THESIS1UNGAB_BACANTO.md         # Full Markdown transcript of latest manuscript
│   ├── Chapter1_Digital_Deception_Mobile_Wallet.md
│   ├── Chapter2_Review_of_Related_Literature.md
│   ├── Chapter3_System_Architecture_and_Methodology.md
│   ├── SECURING MOBILE TRANSACTIONS (1).pptx # Defense presentation slides
│   ├── bscs_thesis_guidelines.md       # NDMC CITE BSCS Thesis formatting standards
│   ├── student_info.md                 # Student profiles & thesis timeline
│   └── forgeguard_system_architecture.svg
├── 01_System_Prototype/                # NDMC Section III.1 Submission Package (6 Ordered Subfolders)
│   ├── README.md                       # Syllabus mapping & execution guide
│   ├── run_system.bat                  # One-click Windows offline launcher
│   ├── 01_Source_Code/                 # 1. Clean application source code & web engine
│   ├── 02_Project_Files/               # 2. Project dependencies, runtime & config
│   ├── 03_Prototype_Files/             # 3. Serialized Keras models & 5-seed metrics
│   ├── 04_Database_Files/              # 4. JSON persistent verification audit ledger
│   ├── 05_Other_Development_Files/     # 5. Training scripts, 5-seed harnesses & samples
│   └── 06_Screenshots_with_Descriptions/ # 6. 8 exhibits, descriptions & Word docx
└── thesis-system/                      # SYSTEM IMPLEMENTATION & EXPERIMENTAL PIPELINE
    ├── README.md                       # ForgeGuard Software System Guide
    ├── dataset/                        # Empirical Dataset (1:1 balanced evaluation: 456 base receipts)
    │   ├── authentic/                  # 228 authentic receipts (highres & compressed)
    │   └── forged/                     # 849 forged receipts (stratified attack vectors)
    ├── models/                         # Serialized weights (.keras) & evaluation_metrics.json
    ├── preprocessing/                  # Error Level Analysis (ELA) signal pipeline
    ├── generator/                      # GCash template synthesis engine
    └── webapp/                         # Streamlit application source & premium CSS
```

---

## Key Academic Thesis Documents

* **[Master Defense Study & System Guide (PDF)](thesis-docs/FORGEGUARD_MASTER_DEFENSE_GUIDE.pdf)** — All-in-One comprehensive study guide, plain-English translator, proposal ground truth, system guide, and presentation script.
* **[Master Defense Study & System Guide (Markdown)](thesis-docs/FORGEGUARD_MASTER_DEFENSE_GUIDE.md)** — Readable Markdown edition of the all-in-one master defense guide for instant viewing in code editors.
* **[Official Thesis Manuscript (Word)](thesis-docs/THESIS1UNGAB_BACANTO.docx)** — Complete Chapters 1 and 2 manuscript submitted for review (September 2026).
* **[Official Thesis Manuscript (Markdown)](thesis-docs/THESIS1UNGAB_BACANTO.md)** — Accessible Markdown version of the compiled manuscript.
* **[Chapter 1: Background & Problem Statement](thesis-docs/Chapter1_Digital_Deception_Mobile_Wallet.md)** — Detailed introduction, research gap, SOP, and SDG alignment.
* **[Chapter 2: Review of Related Literature](thesis-docs/Chapter2_Review_of_Related_Literature.md)** — Comprehensive 7-stage thematic synthesis with IEEE citations.
* **[Chapter 3: System Architecture & Methodology](thesis-docs/Chapter3_System_Architecture_and_Methodology.md)** — Five-tier forensic pipeline and CNN evaluation framework.
* **[BSCS Thesis Guidelines](thesis-docs/bscs_thesis_guidelines.md)** — NDMC CITE formatting and defense specifications.
* **[Student Information & Schedule](thesis-docs/student_info.md)** — Team contact details and academic schedule.
* **[01_System_Prototype Submission Package](01_System_Prototype/README.md)** — Complete NDMC Section III.1 submission package structured into the 6 syllabus subfolders with one-click launcher.

---

## Live System & Public Resources

* **Live Forensic Web Application:** [https://forgeguard.streamlit.app/](https://forgeguard.streamlit.app/)
* **Software System Repository:** [https://github.com/DeathKnell837/ForgeGuard](https://github.com/DeathKnell837/ForgeGuard)
* **Master Thesis Workspace Repository:** [https://github.com/DeathKnell837/NDMC-BSCS-THESIS-PREP](https://github.com/DeathKnell837/NDMC-BSCS-THESIS-PREP)
* **Google Drive Document Archive:** [NDMC BSCS Thesis Drive Folder](https://drive.google.com/drive/folders/1bzRsI6Ywo2yRni5Ij7InCLh0CL0OO90_?usp=drive_link)

---

&copy; 2026 Daniela S. Ungab & Rogie P. Bacanto. Notre Dame of Midsayap College, CITE. All rights reserved.
