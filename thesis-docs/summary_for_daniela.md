# 📋 Summary Sheet for Daniela & Rogie — BSCS Thesis Writing 1 Progress

**Authors:** Daniela S. Ungab & Rogie P. Bacanto (BSCS-4)  
**School:** Notre Dame of Midsayap College (NDMC), College of Information Technology and Engineering (CITE)  
**Adviser:** Ms. Doris Ann Mariano  
**Research Teacher:** Mr. Nero L. Hontiveros  
**Status:** **TITLE DEFENSE PASSED** | **Chapters 1 & 2 Completed** | **Dataset v2.2.0 (777 images) Trained**  
**Approved Title:** *Securing Mobile Transaction: A Comparative Evaluation of CNN Architectures in Detecting Digital Receipt Forgery*  
**System Name:** ForgeGuard  
**Live App Link:** [forgeguard.streamlit.app](https://forgeguard.streamlit.app/)

---

## 🌟 Key Project Highlights

### 1. 📄 Official Document Files
- 📘 **Chapter 1 (Introduction & Proposal Outline):** [`thesis-docs/Chapter1_Digital_Deception_Mobile_Wallet.md`](file:///c:/Users/USER/Desktop/THESIS/thesis-docs/Chapter1_Digital_Deception_Mobile_Wallet.md)
- 📗 **Chapter 2 (Review of Related Literature & Studies - RRL):** [`thesis-docs/Chapter2_Review_of_Related_Literature.md`](file:///c:/Users/USER/Desktop/THESIS/thesis-docs/Chapter2_Review_of_Related_Literature.md)
- 🔍 **GCash Forensic & Design Guide:** [`thesis-docs/gcash_receipt_forensics_guide.md`](file:///c:/Users/USER/Desktop/THESIS/thesis-docs/gcash_receipt_forensics_guide.md)

---

### 2. 📊 Empirical Model Training Results (Google Colab GPU)

| Model Architecture | Parameters | Accuracy | Precision | Recall | F1-Score | Inference Latency | Training Time |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 🥇 **Basic CNN** | **~2.1M** | **100.00%** | **100.00%** | **100.00%** | **1.0000** | **8.61 ms** | 198.50 s |
| 🥈 **MobileNetV2** | **~3.4M** | **95.74%** | **94.67%** | **100.00%** | **0.9726** | **28.04 ms** | **76.59 s** |
| 🥉 **ResNet50** | **~23.5M** | **75.53%** | **75.53%** | **100.00%** | **0.8606** | **109.34 ms** | 413.11 s |

---

### 3. 🖼️ Dataset v2.2.0 Breakdown (777 Total Images)
- **153 Authentic Receipts:** 51 real original GCash/Maya screenshots + 102 augmented receipts.
- **624 Forged Receipts:**
  - `amount_alteration`: 153 images (Karla-Bold in GCash `#1972F9` blue)
  - `ref_fabrication`: 153 images (Karla-Regular for 13-digit reference numbers)
  - `name_modification`: 153 images (Poppins-SemiBold for recipient names)
  - `ai_generated_template`: 153 images (Full AI synthetic templates)
  - `full_template`: 12 images (Legacy templates)

---

## 🚀 Next Steps for Thesis Defense Prep:
1. **Adviser Review:** Present Chapters 1 & 2 draft documents to Ms. Doris Ann Mariano.
2. **Web App Deployment Sync:** Live app on Streamlit Cloud is updated with trained models and ELA preprocessor.
