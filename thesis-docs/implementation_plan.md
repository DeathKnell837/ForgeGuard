# 📋 ForgeGuard BSCS Thesis — Master Implementation & Research Plan

**Approved Title:** *Securing Mobile Transaction: A Comparative Evaluation of CNN Architectures in Detecting Digital Receipt Forgery*
**Students:** Daniela S. Ungab & Rogie P. Bacanto (BSCS-4) | **Adviser:** Ms. Doris Ann Mariano | **Institution:** NDMC CITE (Midsayap, Cotabato)

---

## 🎯 Current Milestone & Timeline Alignment

| Phase | Milestone | Status | Target Date |
|:---|:---|:---:|:---|
| **Phase 1** | **Title Defense** | ✅ **PASSED** | July 2026 |
| **Phase 2** | **Dataset Pipeline (v2.0.0)** | ✅ **COMPLETED** | July 2026 (408 images) |
| **Phase 3** | **Live Web Demo Deployment** | ✅ **COMPLETED** | July 2026 ([forgeguard.streamlit.app](https://forgeguard.streamlit.app/)) |
| **Phase 4** | **Chapter 1 Proposal Writing** | 🔄 **IN PROGRESS** | Current Stage |
| **Phase 5** | **Chapter 2 (RRL) Writing** | 🔄 **IN PROGRESS** | Current Stage |
| **Phase 6** | **CNN Model Training on Colab** | ⏳ **UPCOMING** | Next Stage |
| **Phase 7** | **Chapter 3 (Methodology) Blueprint** | ⏳ **UPCOMING** | Next Stage |
| **Phase 8** | **Chapter 4 Evaluation Data Collection** | ⏳ **UPCOMING** | Next Semester |

---

## 📊 Dataset Pipeline Architecture (v2.0.0)

Total Labeled Receipt Images: **408 Images**

```
thesis-system/dataset/
├── authentic/
│   ├── compressed/     (104 JPG images)
│   └── highres/        (104 PNG images)
├── forged/
│   ├── compressed/     (304 JPG images: digitally_edited, amount_alteration, ref_fabrication, name_modification, full_template)
│   └── highres/        (304 PNG images)
└── metadata.json       (408 total samples indexed)
```

1. **Authentic Class (104 samples):**
   - 52 real GCash/Maya transaction receipt screenshots.
   - 52 augmented authentic receipts (subtle brightness, contrast, and noise adjustments).
2. **Forged Class (304 samples):**
   - **104 Digitally Edited Forgeries:** Simulated Photoshop, Gallery markup, and text alteration.
   - **200 Programmatic Synthetic Forgeries:** Amount alteration, reference number fabrication, recipient name modification, and full template fabrication.

---

## 🛠️ System Implementation Modules

| Module | File Location | Status | Function |
|:---|:---|:---:|:---|
| **Streamlit Web UI** | `webapp/app.py` | ✅ Ready | Interactive multi-model comparison dashboard |
| **ELA Engine** | `preprocessing/ela.py` | ✅ Ready | Error Level Analysis compression error heatmap compute |
| **Digital Forger** | `tools/receipt_forger.py` | ✅ Ready | Photoshop/Gallery text edit simulation script |
| **Receipt Generator** | `tools/gcash_receipt_generator.py` | ✅ Ready | Programmatic GCash receipt generator |
| **Training Pipeline** | `training/train.py` | ⏳ Planned | Google Colab GPU training script for Basic CNN, ResNet50, MobileNetV2 |

---

## 📖 Chapter 1 & Chapter 2 Writing Plan

### Chapter 1 (Introduction & Statement of the Problem)
- [x] Background of the Study (Local online sellers, screenshot fraud, compression challenges)
- [x] Statement of the Problem (SOP Questions 1-5 covering accuracy by forgery type, metrics, latency, compression impact, and best model)
- [x] Significance of the Study (Sellers, small business owners in Midsayap, student entrepreneurs, wallet providers, researchers)
- [x] Scope & Limitations (GCash/Maya receipts, 3 CNN models, GPU-free web deployment)

### Chapter 2 (Review of Related Literature & Studies)
- [ ] **Structured RRL Flow:**
  1. Digital Payment Fraud in Southeast Asia / Philippines
  2. Image Forgery Techniques (Splicing, Copy-Move, Photoshop Text Alteration)
  3. Image Forensics & Error Level Analysis (ELA)
  4. Deep Learning in Image Authentication (IEEE 9142188 citation)
  5. Comparative Evaluation of CNN Architectures (Basic CNN vs ResNet50 vs MobileNetV2)
  6. Image Compression & Resampling Artifacts
  7. Mobile-Efficient AI Deployment
