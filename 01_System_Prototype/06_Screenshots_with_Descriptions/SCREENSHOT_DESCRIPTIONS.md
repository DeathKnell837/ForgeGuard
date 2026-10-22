# ForgeGuard System Prototype - Visual Exhibit & Screenshot Guide

**Notre Dame of Midsayap College (NDMC)**  
**College of Information Technology and Engineering (CITE)**  
**Bachelor of Science in Computer Science (BSCS)**  
**Course:** CS Thesis Writing 1 (A.Y. 2026–2027)  
**Authors:** Daniela S. Ungab & Rogie P. Bacanto  
**Adviser:** Ms. Doris Ann Mariano  
**Approved Canonical Title:** *Receipt or Deceit: A Cross-Architecture Analysis of Convolutional Neural Network Models in Detecting Forged Digital Transaction Receipts*

---

## Screenshot Inventory & Descriptions

### Exhibit 01: System Landing Dashboard (`01_home_dashboard.png`)
* **Component:** User Interface & Upload Zone (Figure 4, Layer 1)
* **Description:** The primary entry point for ForgeGuard. Features a drag-and-drop receipt intake supporting JPEG, PNG, and WebP format transaction slips up to 200MB. Quick-evaluation benchmark buttons ("Authentic Receipt", "Edited Receipt", "Generated Receipt") allow immediate zero-upload forensic demonstration. The status badge confirms neural network graph compilation and target input dimensionality (224x224 ELA tensor). Adheres to NDMC zero-emoji cyber-forensics standards.

### Exhibit 02: Authentic Receipt Multi-CNN Verification (`02_authentic_receipt_analysis.png`)
* **Component:** Multi-Architecture Verification & Telemetry (Figure 4, Layers 2 & 3)
* **Description:** Diagnostic output evaluating a genuine downloadable GCash payment confirmation slip. Basic CNN confirms authenticity with 100.0% confidence (inference time: 53.8 ms; memory: 0.0 MB added). MobileNetV2 corroborates authenticity with 92.7% confidence (372.8 ms). ResNet50 demonstrates over-sensitivity to normal JPEG variance at 50.2% fraud verdict, documenting empirical baseline behavior reported in Chapter 2.

### Exhibit 03: Digitally Edited Receipt Forgery Detection (`03_forged_edited_receipt_analysis.png`)
* **Component:** Digital Forgery Modality Classification
* **Description:** Forensic evaluation of a tampered transaction slip where the amount was spliced from PHP 170.00 to PHP 50,000.00 using digital image editing software. Basic CNN successfully flags the forgery at 100.0% fraud confidence (processing latency: 126.5 ms). MobileNetV2 independently detects the forgery at 98.4% confidence (911.7 ms). High-contrast fraud badges highlight the security alert.

### Exhibit 04: Error Level Analysis Residual Matrix Exhibit (`04_ela_residual_matrix.png`)
* **Component:** Mathematical ELA Feature Transform (Section 1.3 / Section 3.2)
* **Description:** The raw Error Level Analysis (ELA) decomposition generated at calibrated quality Q=90 with 15.0x residual amplification. The exhibit clearly isolates the high-frequency compression error boundary surrounding the forged "PHP 50,000.00" characters, exposing inconsistent quantisation tables against the authentic background canvas.

### Exhibit 05: Dynamic Thermal Heatmap Localization (`05_tamper_heatmap_overlay.png`)
* **Component:** Visual Hotspot Heatmap Overlay (Figure 4, Layer 5)
* **Description:** Thermal colormap overlay synthesized from ELA spatial variance gradients. Quiet, unaltered receipt regions retain natural appearance without distracting tint, while mathematically anomalous compression boundaries surrounding the spliced text glow in vivid orange-red thermal contours, giving human auditors instantaneous visual explainability.

### Exhibit 06: Overall Architecture Benchmark Matrix (`06_overall_architecture_benchmark.png`)
* **Component:** Model Comparison & Empirical Evaluation (Chapter 2 & Table 2 Alignment)
* **Description:** Comprehensive cross-architecture benchmark matrix evaluating Basic CNN, MobileNetV2, and ResNet50 across both Standard and Compressed (Facebook Messenger) conditions. Centered desktop/laptop presentation detailing Accuracy, Compression Delta (Delta Acc), Precision, Recall, F1-Score, Execution Latency, Peak Working RAM, Parameter Count, and Section 2.10 Multi-Criteria Composite Scores (Basic CNN: 100.00%; MobileNetV2: 71.50% / 66.85%; ResNet50: 0.00%).

### Exhibit 07: Empirical Dataset Composition Matrix (`07_empirical_dataset_composition.png`)
* **Component:** Dataset Stratification & Partition Specification (Table 1 Alignment)
* **Description:** Fluid, centered layout of the 1,000-image base receipt corpus stratified into 900 experimental images (60% Training: 540 images; 15% Validation: 135 images; 25% Testing: 225 images) and 100 unseen-tool holdout validation images (50 Authentic + 50 Forged). Documents both Standard and Messenger-compressed evaluation conditions (2,000 evaluations total).

### Exhibit 08: Benchmark Records Telemetry & Audit Log (`08_benchmark_records_telemetry.png`)
* **Component:** Forensic Audit Trail & Database Layer (Figure 4, Layer 4)
* **Description:** Live transaction verification ledger persisting every analyzed receipt. Records Timestamp, Neural Architecture Evaluated, Prediction Verdict, Confidence Probability, Processing Time in milliseconds, and System Memory Load in Megabytes, fulfilling NDMC database logging criteria.
