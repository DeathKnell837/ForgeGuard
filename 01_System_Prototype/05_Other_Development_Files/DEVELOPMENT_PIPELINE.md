# Development Pipeline and Evaluation Harness Documentation

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

This directory contains experimental development scripts, training pipelines, benchmark evaluation harnesses, interactive Jupyter/Colab notebooks, and pre-loaded receipt exhibits used throughout the empirical research lifecycle.

### Development File Inventory
| Filename | Type | Purpose |
| :--- | :--- | :--- |
| `train.py` | Python Script | Complete training script for Basic CNN, MobileNetV2, and ResNet50 on ELA-transformed inputs |
| `ForgeGuard_Model_Training.ipynb` | Jupyter Notebook | Interactive Colab notebook containing training visualizer, confusion matrices, and loss curves |
| `evaluate_balanced_5seeds.py` | Python Script | Rigorous 5-seed randomized evaluation harness measuring Clean and Compressed metrics |
| `evaluate_compressed.py` | Python Script | Specialized Facebook Messenger compression degradation assessment script |
| `authentic.jpg` | Image Exhibit | Downloadable authentic GCash confirmation slip preset exhibit |
| `edited.jpg` | Image Exhibit | Tampered GCash receipt exhibit with spliced amounts and transaction reference numbers |
| `generated.jpg` | Image Exhibit | Fully synthetic AI/Canva generated fraudulent transaction receipt exhibit |
| `samples/` | Directory | Preset exhibit image directory mirrored for backward-compatible relative path resolution |

---

## 2. Model Training Pipeline (`train.py`)

The training script implements:
1. **Dynamic ELA Preprocessing:** Applies in-memory 90Q re-compression and 15x scale amplification on training receipts.
2. **Data Augmentation:** Bounded affine shifts, horizontal flips, and slight contrast jittering to preserve compression artifact integrity.
3. **Loss Function & Optimization:** Binary Cross-Entropy with Adam optimizer ($\text{lr} = 10^{-4}$ for transfer learning backbones, $\text{lr} = 10^{-3}$ for Basic CNN).
4. **Early Stopping & Checkpointing:** Monitors validation loss with a patience of 7 epochs to prevent over-fitting.

---

## 3. 5-Seed Evaluation Harness (`evaluate_balanced_5seeds.py`)

To eliminate sampling bias and conform to formal Computer Science empirical standards, all architectures were evaluated across 5 random seeds (42, 101, 2024, 777, 999):
* **Dataset Split:** 200 balanced test samples (100 Authentic, 100 Forged across editing categories).
* **Metrics Computed:** Accuracy, Precision, Recall, Specificity, F1-Score, AUC-ROC, Inference Latency, and Memory Footprint.
* **Aggregated Output:** Saved to `evaluation_metrics.json` and mirrored in `03_Prototype_Files/`.

---

## 4. Pre-Loaded Receipt Exhibits

Three benchmark exhibits ship directly with the prototype to facilitate instant verification testing without requiring manual file uploads during panel demonstrations:
1. **Authentic (`authentic.jpg`):** Valid, downloadable GCash transaction receipt with uniform error residuals across typography and background.
2. **Edited Spliced (`edited.jpg`):** Manipulated receipt showing localized high-energy ELA residual clusters around the spliced amount numbers.
3. **AI Generated (`generated.jpg`):** Synthetic receipt exhibiting global frequency anomalies and structural font inconsistencies.
