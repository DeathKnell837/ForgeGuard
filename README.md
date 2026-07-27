# 🎓 NDMC BSCS Thesis Workspace — Academic Research & Preparation

### **"Securing Mobile Transaction: A Comparative Evaluation of CNN Architectures in Detecting Digital Receipt Forgery"**

[![Live System Demo](https://img.shields.io/badge/Live_System-forgeguard.streamlit.app-8B5CF6?style=for-the-badge&logo=streamlit)](https://forgeguard.streamlit.app/)
[![Title Defense](https://img.shields.io/badge/Title_Defense-PASSED-34D399?style=for-the-badge)](https://forgeguard.streamlit.app/)
[![Chapters 1 & 2](https://img.shields.io/badge/Proposal-Chapters_1_%26_2_Completed-007ACC?style=for-the-badge)](https://forgeguard.streamlit.app/)

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

## 📊 Empirical Model Training Results (Google Colab GPU)

| CNN Architecture | Parameters | Accuracy | Precision | Recall | F1-Score | Latency (ms) | Training Time |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 🥇 **Basic CNN** | **~2.1M** | **100.00%** | **100.00%** | **100.00%** | **1.0000** | **8.61 ms** | 198.50 s |
| 🥈 **MobileNetV2** | **~3.4M** | **95.74%** | **94.67%** | **100.00%** | **0.9726** | **28.04 ms** | **76.59 s** |
| 🥉 **ResNet50** | **~23.5M** | **75.53%** | **75.53%** | **100.00%** | **0.8606** | **109.34 ms** | 413.11 s |

---

## 🖼️ Dataset v2.2.0 Summary (777 Labeled Images)

* **Authentic Receipts:** **153 Images** (51 real original GCash/Maya screenshots + 102 clean augmented)
* **Forged Receipts:** **624 Images**
  * **`amount_alteration`:** 153 images (Flawless Karla-Bold digital edits in GCash `#1972F9` blue)
  * **`ref_fabrication`:** 153 images (Flawless Karla-Regular 13-digit ref edits)
  * **`name_modification`:** 153 images (Flawless Poppins-SemiBold name edits)
  * **`ai_generated_template`:** 153 images (Full AI synthetic templates)
  * **`full_template`:** 12 images (Legacy templates)

---

## 📅 Timeline & Status

| Milestone | Status | Details |
|:---|:---:|:---|
| **Title Defense** | ✅ **PASSED** | Passed in July 2026 with approved title |
| **Dataset Preparation** | ✅ **v2.2.0 Ready** | 777 labeled images (153 Authentic + 624 Forged) |
| **Model GPU Training** | ✅ **Completed** | Models trained on Colab GPU (`.keras` weights saved) |
| **Chapter 1 Writing** | ✅ **Completed** | Available at [`thesis-docs/Chapter1_Digital_Deception_Mobile_Wallet.md`](thesis-docs/Chapter1_Digital_Deception_Mobile_Wallet.md) |
| **Chapter 2 Writing** | ✅ **Completed** | Available at [`thesis-docs/Chapter2_Review_of_Related_Literature.md`](thesis-docs/Chapter2_Review_of_Related_Literature.md) |
| **Forensic Guide** | ✅ **Completed** | Available at [`thesis-docs/gcash_receipt_forensics_guide.md`](thesis-docs/gcash_receipt_forensics_guide.md) |
| **Live System Demo** | ✅ **Deployed** | Live Streamlit Cloud app at [forgeguard.streamlit.app](https://forgeguard.streamlit.app/) |

---

## 📁 Workspace Structure

```
THESIS/
├── thesis-docs/                # Academic Proposal & Guidelines
│   ├── Chapter1_Digital_Deception_Mobile_Wallet.md
│   ├── Chapter2_Review_of_Related_Literature.md
│   ├── gcash_receipt_forensics_guide.md
│   └── summary_for_daniela.md
└── thesis-system/              # System Implementation & Models
    ├── assets/fonts/           # Official Karla & Poppins font assets
    ├── dataset/                # Dataset v2.2.0 (777 images + metadata.json)
    ├── models/                 # Trained .keras weights & evaluation_metrics.json
    ├── preprocessing/          # Error Level Analysis (ELA) engine
    ├── tools/                  # Forgery generator & synthetic receipt tools
    └── training/               # Python train.py & Colab notebook (.ipynb)
```
