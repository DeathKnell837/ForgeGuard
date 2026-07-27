# 🎓 NDMC BSCS Thesis Workspace — Academic Research & Preparation

### **"Securing Mobile Transaction: A Comparative Evaluation of CNN Architectures in Detecting Digital Receipt Forgery"**

[![Live System Demo](https://img.shields.io/badge/Live_System-forgeguard.streamlit.app-8B5CF6?style=for-the-badge&logo=streamlit)](https://forgeguard.streamlit.app/)
[![Title Defense](https://img.shields.io/badge/Title_Defense-PASSED-34D399?style=for-the-badge)](https://forgeguard.streamlit.app/)

📁 **Google Drive Folder:** [All Thesis Documents & Resources](https://drive.google.com/drive/folders/1bzRsI6Ywo2yRni5Ij7InCLh0CL0OO90_?usp=drive_link)

---

## 👥 Student & Adviser Profiles
* **Group Members:**
  * **Daniela S. Ungab** (BSCS-4)
  * **Rogie P. Bacanto** (BSCS-4)
* **Adviser:** **Ms. Doris Ann Mariano**
* **Research Teacher:** **Mr. Nero L. Hontiveros**
* **Dean:** **Engr. Mark Bryan C. Tenebroso, PCPE, ME-CPE**
* **School:** Notre Dame of Midsayap College (NDMC), College of Information Technology and Engineering (CITE)
* **Program:** Bachelor of Science in Computer Science
* **Subject:** CS Thesis Writing 1 (Enrolled, June 2026)

---

## 📅 Timeline & Status

| Milestone | Status | Details |
|:---|:---:|:---|
| **Title Defense** | ✅ **PASSED** | Passed in July 2026 with approved title |
| **Dataset Preparation** | ✅ **v2.0.0 Ready** | 408 labeled images (104 Authentic + 304 Forged) |
| **System Demo** | ✅ **Deployed** | Live at [forgeguard.streamlit.app](https://forgeguard.streamlit.app/) |
| **Proposal Writing** | 🔄 **In Progress** | Chapters 1 & 2 (Introduction & Literature Review) |

---

## 📖 Study Overview & Research Questions

### Problem Statement
The rapid adoption of mobile wallets (GCash, Maya) has led to a rise in screenshot-based payment fraud. Buyers manipulate transaction details in photo editors, gallery markup, or synthetic receipt generators to deceive small business owners and student entrepreneurs into releasing goods without payment.

### Core Objective
To comparatively evaluate three Convolutional Neural Network (CNN) architectures — **Basic CNN (~2.1M params)**, **ResNet50 (~23.5M params)**, and **MobileNetV2 (~3.4M params)** — using **Error Level Analysis (ELA)** to detect pixel-level digital forgery in mobile wallet receipt screenshots across varying JPEG compression levels.

### 5 Statement of the Problem (SOP) Questions
1. **Accuracy by Forgery Type:** Classification accuracy on (1.1) Manually edited receipts vs (1.2) Programmatically generated fake receipts.
2. **Standard Evaluation Metrics:** Precision, Recall, and F1-score across architectures.
3. **Computational Efficiency:** Real-time inference speed (latency in ms) and resource requirements.
4. **Compression Robustness:** Classification performance on (4.1) Original high-resolution vs (4.2) Heavily compressed images.
5. **Practical Deployment:** Best architecture recommendation for GPU-free devices used by NDMC student entrepreneurs.

---

## 📁 Workspace Layout

| Directory | Purpose |
|:---|:---|
| **`thesis-docs/`** | Official thesis proposals, guidelines, PDFs, student info, Chapter 1 & 2 drafts |
| **`thesis-system/`** | Python system code, ELA preprocessors, dataset generator, models, training scripts |

---

## 📚 Primary Academic References
* [1] C. Artaud et al., *"Receipt dataset for fraud detection,"* IWCDF, 2017.
* [2] K. S. Vaishnavi & K. P. Narayan, *"FakePay: Real-time UPI fraud detection using OCR & CNN,"* Technical Report, 2026.
* [3] A. M. Nagm et al., *"Detecting image manipulation with ELA-CNN integration,"* *PeerJ Computer Science*, vol. 10, p. e2205, 2024.
* [4] K. He et al., *"Deep residual learning for image recognition,"* IEEE CVPR, 2016.
* [5] M. Sandler et al., *"MobileNetV2: Inverted residuals and linear bottlenecks,"* IEEE CVPR, 2018.
* [6] IEEE 9142188: *"Image Forgery Detection Based on ELA and Deep Learning"*.
