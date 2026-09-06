# 🎓 NDMC BSCS Thesis Research Workspace

<div align="center">

### **Notre Dame of Midsayap College**
**College of Information Technology and Engineering (CITE)**  
*Bachelor of Science in Computer Science (BSCS)*

---

## **Securing Mobile Transaction: A Comparative Evaluation of CNN Architectures in Detecting Digital Receipt Forgery**

**Working / Paper Title:**  
*‘Receipt or Deceit?’: A Cross-Architecture Analysis of Convolutional Neural Network Models in Detecting Forged Digital Transaction Receipts*

---

[![Thesis Status](https://img.shields.io/badge/Proposal-Chapters_1_%26_2_Completed-007ACC?style=for-the-badge)](thesis-docs/THESIS1UNGAB_BACANTO.md)
[![Title Defense](https://img.shields.io/badge/Title_Defense-PASSED-10B981?style=for-the-badge)](thesis-docs/)
[![Live System Demo](https://img.shields.io/badge/Live_System-forgeguard.streamlit.app-8B5CF6?style=for-the-badge&logo=streamlit)](https://forgeguard.streamlit.app/)
[![System Repo](https://img.shields.io/badge/System_Repo-DeathKnell837%2FForgeGuard-1E293B?style=for-the-badge&logo=github)](https://github.com/DeathKnell837/ForgeGuard)
[![Google Drive](https://img.shields.io/badge/Google_Drive-Thesis_Archive-F59E0B?style=for-the-badge&logo=googledrive)](https://drive.google.com/drive/folders/1bzRsI6Ywo2yRni5Ij7InCLh0CL0OO90_?usp=drive_link)

[Latest Manuscript (Word)](thesis-docs/THESIS1UNGAB_BACANTO.docx) &bull; [Latest Manuscript (Markdown)](thesis-docs/THESIS1UNGAB_BACANTO.md) &bull; [Chapter 1](thesis-docs/Chapter1_Digital_Deception_Mobile_Wallet.md) &bull; [Chapter 2](thesis-docs/Chapter2_Review_of_Related_Literature.md) &bull; [System Architecture](thesis-docs/forgeguard_system_architecture.svg) &bull; [Live Demo](https://forgeguard.streamlit.app/)

</div>

---

## 👥 Research Group & Faculty Profile

| Role | Name | Designation / Affiliation |
|:---|:---|:---|
| **Lead Researcher** | **Daniela S. Ungab** | BSCS-4 Student Candidate, NDMC CITE |
| **Co-Researcher** | **Rogie P. Bacanto** | BSCS-4 Student Candidate, NDMC CITE |
| **Thesis Adviser** | **Ms. Doris Ann Mariano** | Faculty Adviser, NDMC CITE |
| **Research Teacher** | **Mr. Nero L. Hontiveros** | CS Thesis Writing 1 Instructor |
| **Dean of CITE** | **Engr. Mark Bryan C. Tenebroso, PCPE, ME-CPE** | Dean, College of Information Technology & Engineering |
| **Academic Term** | **Academic Year 2026–2027** | CS Thesis Writing 1 (Enrolled, June 2026) |

---

## 📌 Research Overview & Abstract

Digital payment channels now account for over **57.4% of monthly retail transactions** in the Philippines (Bangko Sentral ng Pilipinas 2024 Report). However, peer-to-peer mobile wallet confirmation receipts (specifically within the **GCash** and **Maya** ecosystems) have become a primary attack surface for receipt-based fraud. Scammers utilize image editing tools (Photoshop, Canva) and programmatic generators to modify transaction amounts, reference numbers, and recipient names without transferring actual funds.

Because screenshots shared over messaging platforms (Messenger, Viber, WhatsApp) undergo lossy compression, conventional visual inspection and raw Error Level Analysis (ELA) frequently fail to expose subtle tampering. 

This study addresses this gap by conducting a rigorous **comparative evaluation of three distinct Convolutional Neural Network (CNN) architectures**:
1. **Basic CNN (Custom 4-block baseline, ~2.1M parameters)**
2. **ResNet50 (Deep residual benchmark, ~23.5M parameters)**
3. **MobileNetV2 (Inverted residual mobile architecture, ~3.4M parameters — SOP-5 Recommended)**

Each model is evaluated on its ability to classify original high-resolution and heavily compressed receipts as authentic or forged across precision, recall, F1-score, inference latency, and memory footprint.

---

## 🎯 Statement of the Problem (SOP)

This research investigates the following specific research questions:

1. **Classification Performance (Standard ML Metrics):**
   * What is the performance of Basic CNN, ResNet50, and MobileNetV2 in terms of **Precision**, **Recall**, and **F1-score**?
2. **Detection by Forgery Modality:**
   * What is the accuracy of each architecture in detecting:
     * *SOP 2.1:* **Digitally edited transaction receipts** (raster splicing, font replacement in amount/name/ref).
     * *SOP 2.2:* **Programmatically generated fake transaction receipts** (full template and diffusion-generated fakes).
3. **Computational Efficiency & Resource Footprint:**
   * Is there a statistically significant difference in **inference speed (ms)** and **memory load** among the three models?
4. **Resilience to Messaging Platform Compression:**
   * Is there a significant difference in accuracy when evaluating **original high-resolution receipts** versus **heavily compressed images** ($Q=25\text{--}45$)?
5. **Practical Edge Deployability:**
   * Which CNN architecture delivers the optimal trade-off between classification accuracy and processing latency on resource-constrained devices without dedicated GPUs?

---

## 📊 Empirical Model Benchmark Results (Google Colab T4 GPU)

| CNN Architecture | Parameters | Accuracy | Precision | Recall | F1-Score | Latency (ms) | Training Time | Assessment |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 🥇 **Basic CNN** | **~2.1M** | **100.00%** | **100.00%** | **100.00%** | **1.0000** | **8.61 ms** | 198.50 s | Ultra-fast baseline model |
| 🥈 **MobileNetV2** | **~3.4M** | **95.74%** | **94.67%** | **100.00%** | **0.9726** | **28.04 ms** | **76.59 s** | **SOP-5 Optimal: Best mobile Pareto trade-off** |
| 🥉 **ResNet50** | **~23.5M** | **75.53%** | **75.53%** | **100.00%** | **0.8606** | **109.34 ms** | 413.11 s | High computational overhead |

---

## 🗂️ Dual Repository Architecture & Boundary Rules

To ensure clean separation between **academic thesis documentation** and **live software engineering deployment**, this research maintains two synchronized Git remotes:

| Remote | Target Repository | Scope & Purpose |
|:---|:---|:---|
| **`origin`** | [`DeathKnell837/NDMC-BSCS-THESIS-PREP`](https://github.com/DeathKnell837/NDMC-BSCS-THESIS-PREP) | **Academic Thesis Preparation Repository.** Contains all proposal documents (`thesis-docs/`), thesis manuscripts (`.docx` & `.md`), IEEE literature reviews, defense slides, guidelines, and research outlines. |
| **`forgeguard`** | [`DeathKnell837/ForgeGuard`](https://github.com/DeathKnell837/ForgeGuard) | **Software Engineering & Deployment Repository.** Contains the production Streamlit web application (`app.py`), serialized `.keras` models, ELA preprocessing engine, dataset generator tools, and deployment configs for [forgeguard.streamlit.app](https://forgeguard.streamlit.app/). |

### 🛡️ Non-Interference Push Policy
1. **Thesis Documentation updates** (`thesis-docs/`, manuscripts, proposal writing) must always be committed and pushed to `origin`.
2. **System & Webapp updates** (`thesis-system/`, models, UI components) are synced to `origin` (for complete archival) and pushed to `forgeguard` (for live Streamlit Cloud rebuilds).
3. The root `README.md` in `origin` represents the **Academic Thesis Workspace Hub**, while the root `README.md` in `forgeguard` represents the **ForgeGuard Software System Guide**.

---

## 📁 Workspace Directory Structure

```
THESIS/
├── README.md                           # Master Academic Workspace Hub (this file)
├── app.py                              # Streamlit Cloud deployment entrypoint
├── requirements.txt                    # System Python runtime dependencies
├── thesis-docs/                        # ACADEMIC THESIS DOCUMENTATION (Manuscripts & Guidelines)
│   ├── THESIS1UNGAB_BACANTO.docx       # Official compiled Chapters 1 & 2 Word Document
│   ├── THESIS1UNGAB_BACANTO.md         # Full Markdown transcript of latest manuscript
│   ├── Chapter1_Digital_Deception_Mobile_Wallet.md
│   ├── Chapter2_Review_of_Related_Literature.md
│   ├── Chapter3_System_Architecture_and_Methodology.md
│   ├── SECURING MOBILE TRANSACTIONS (1).pptx # Defense presentation slides
│   ├── bscs_thesis_guidelines.md       # NDMC CITE BSCS Thesis formatting standards
│   ├── NDMC Thesis Guidelines v5 - 2025.pdf
│   ├── Research Outline for CITE 2024.pdf
│   ├── CITE Research Agenda for 2024-2030.pdf
│   ├── student_info.md                 # Student profiles & thesis timeline
│   └── forgeguard_system_architecture.svg
└── thesis-system/                      # SYSTEM IMPLEMENTATION & EXPERIMENTAL PIPELINE
    ├── README.md                       # ForgeGuard Software System Guide
    ├── dataset/                        # Dataset v2.2.0 (777 labeled samples + metadata.json)
    │   ├── authentic/                  # 153 authentic receipts (highres & compressed)
    │   └── forged/                     # 624 forged receipts (4 forgery categories)
    ├── models/                         # Serialized weights (.keras) & evaluation_metrics.json
    ├── preprocessing/                  # Error Level Analysis (ELA) & heatmap generation
    ├── tools/                          # Synthetic evidence & receipt generator tools
    ├── training/                       # Colab GPU training scripts & Jupyter notebook
    └── webapp/                         # Streamlit application source & custom CSS
```

---

## 📑 Key Academic Thesis Documents

* 📄 **[Official Thesis Manuscript (Word)](thesis-docs/THESIS1UNGAB_BACANTO.docx)** — Complete Chapters 1 and 2 manuscript submitted for review (September 2026).
* 📄 **[Official Thesis Manuscript (Markdown)](thesis-docs/THESIS1UNGAB_BACANTO.md)** — Accessible Markdown version of the compiled manuscript.
* 📄 **[Chapter 1: Background & Problem Statement](thesis-docs/Chapter1_Digital_Deception_Mobile_Wallet.md)** — Detailed introduction, research gap, SOP, and SDG alignment.
* 📄 **[Chapter 2: Review of Related Literature](thesis-docs/Chapter2_Review_of_Related_Literature.md)** — Comprehensive 7-stage thematic synthesis with IEEE citations.
* 📄 **[Chapter 3: System Architecture & Methodology](thesis-docs/Chapter3_System_Architecture_and_Methodology.md)** — Five-tier forensic pipeline and CNN evaluation framework.
* 📄 **[BSCS Thesis Guidelines](thesis-docs/bscs_thesis_guidelines.md)** — NDMC CITE formatting and defense specifications.
* 📄 **[Student Information & Schedule](thesis-docs/student_info.md)** — Team contact details and academic schedule.

---

## 🌐 Live System & Public Resources

* **Live Forensic Web Application:** [https://forgeguard.streamlit.app/](https://forgeguard.streamlit.app/)
* **Software System Repository:** [https://github.com/DeathKnell837/ForgeGuard](https://github.com/DeathKnell837/ForgeGuard)
* **Master Thesis Workspace Repository:** [https://github.com/DeathKnell837/NDMC-BSCS-THESIS-PREP](https://github.com/DeathKnell837/NDMC-BSCS-THESIS-PREP)
* **Google Drive Document Archive:** [NDMC BSCS Thesis Drive Folder](https://drive.google.com/drive/folders/1bzRsI6Ywo2yRni5Ij7InCLh0CL0OO90_?usp=drive_link)

---

&copy; 2026 Daniela S. Ungab & Rogie P. Bacanto. Notre Dame of Midsayap College, CITE. All rights reserved.
