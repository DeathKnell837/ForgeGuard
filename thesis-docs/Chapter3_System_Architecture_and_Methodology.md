# Chapter 3

## System Architecture and Research Methodology

### 3.1 Research Design

This study employed an empirical, comparative experimental research design to evaluate the diagnostic efficacy and computational efficiency of three Convolutional Neural Network (CNN) architectures in detecting digital receipt forgery. The experimental framework integrates digital image forensics, specifically Error Level Analysis (ELA), with deep learning classification. The system was realized through **ForgeGuard**, a deployed, full-stack forensic application providing real-time receipt triage, tamper localization, and architecture performance telemetry.

---

### 3.2 System Architecture

The ForgeGuard system is structured into five cohesive architectural layers that decouple user interaction, signal preprocessing, deep neural inference, data persistence, and forensic decision reporting. The architecture is formally illustrated in Figure 3.1 (`thesis-docs/forgeguard_system_architecture.svg`):

1. **Presentation Layer (Streamlit Web Interface):**
   * **Receipt Ingestion Module:** Accepts user uploads of digital transaction receipts in PNG, JPEG, and WEBP formats with structural verification.
   * **Tri-Spectral Comparison Gallery:** Synchronously presents the raw uploaded image, the computed ELA residual noise matrix, and the OpenCV tamper heatmap localization overlay.
   * **Model Benchmark Suite:** Renders interactive performance analytics, empirical confusion matrices, latency gauges, and parameter footprint comparisons across all evaluated models.

2. **Forensic Preprocessing Layer (Signal Processing Engine):**
   * **Dimension Normalization:** Verifies aspect ratios and standardizes input dimensions to ensure uniform tensor formatting.
   * **Error Level Analysis (ELA) Engine:** Implements lossy re-compression at quality factor Q = 90 and calculates the absolute difference matrix multiplied by a scale factor of 15.0x to isolate spliced pixels.
   * **Tensor Formatting:** Formats the ELA residual into a normalized 128 x 128 x 3 floating-point tensor ([0.0, 1.0]) for model ingestion.
   * **Tamper Heatmap Generator:** Employs OpenCV COLORMAP_JET and Gaussian spatial smoothing to localize the fraudulent Region of Interest (ROI), such as altered currency amounts or reference strings.

3. **Comparative Deep Learning Inference Layer (TensorFlow / Keras):**
   * **Basic CNN:** Custom 4-layer baseline model (~2.1M parameters) consisting of alternating Conv2D, MaxPooling2D, Dropout, and Dense classification layers.
   * **MobileNetV2:** Lightweight architecture (~3.4M parameters) utilizing inverted residual blocks and depthwise separable convolutions for low-latency mobile deployment.
   * **ResNet50:** Deep 50-layer residual network (~23.5M parameters) leveraging residual skip connections for deep feature representation.
   * **Consensus & Voting Engine:** Computes multi-model agreement (e.g., 3/3 unanimous consensus or 2/3 soft voting) and tracks latency metrics in milliseconds.

4. **Data and Model Repository Layer:**
   * **GCash Empirical Dataset (v2.2.0):** Houses 777 labeled receipt images partitioned into authentic samples and four distinct tampering attack vectors.
   * **Google Colab GPU Training Pipeline:** Reproducible training notebook (`ForgeGuard_Model_Training.ipynb`) accelerated by NVIDIA T4 GPUs.
   * **Serialized Weights:** Stores compiled Keras models (`basic_cnn.keras`, `mobilenetv2.keras`, `resnet50.keras`).
   * **Evaluation Telemetry:** Houses `evaluation_metrics.json` recording validation accuracy, precision, recall, F1-scores, and confusion matrices.

5. **Results and Forensic Decision Layer:**
   * **Authenticity Verdict:** Emits a high-contrast visual stamp: `AUTHENTIC VERIFIED` (Secure) or `FORGED / SPLICED DETECTED` (Fraud Alert).
   * **Architectural Readouts:** Displays individual model confidence percentages and millisecond execution latency.
   * **Spatial Localization Overlay:** Renders a 42% opacity heatmap bounding the altered text or figures.
   * **Explainable AI (XAI) Audit:** Employs Gemini 2.0 Flash to audit font baseline alignment, Karla/Poppins typography compliance, and 13-digit reference checksum syntax.

---

### 3.3 Data Flow Diagram (DFD Level 0 - Context Diagram)

The operational dataflow between external entities and the ForgeGuard system is formalized below:

* **External Entities:**
  * **User / Online Merchant:** Transmits `GCash Receipt Image Screenshot` into the system; receives `Authenticity Verdict & Threat Level`, `Multi-CNN Consensus Scores`, `ELA Forensic Heatmap & Noise Analysis`, and `Comparative Benchmark Metrics`.
  * **Researcher / Model Engineer:** Ingests `Trained CNN Model Weights (.keras)` and `Training Dataset Samples`; receives `Model Evaluation Metrics (Accuracy, Precision, Recall, F1, Latency)`.

---

### 3.4 Use Case Specifications

The system encapsulates the following core use cases:
* **UC-01: Upload GCash Digital Receipt:** The user submits a payment screenshot for verification.
* **UC-02: View Authenticity Verdict and Threat Level:** The user inspects the binary verdict and fraud likelihood.
* **UC-03: View Multi-CNN Consensus Scores:** The user inspects agreement across Basic CNN, MobileNetV2, and ResNet50.
* **UC-04: View ELA Forensic Heatmap & Noise Analysis:** The user localizes digital edits via the Tri-Spectral Gallery.
* **UC-05: View Benchmark Analytics:** Both User and Researcher inspect empirical test metrics and confusion matrices.
* **UC-06: Deploy & Update Trained CNN Models:** The Researcher manages and updates neural network weights.

---

### 3.5 Mathematical Formulation of Error Level Analysis (ELA)

Digital image manipulation typically alters the compression history of localized pixel clusters. In the ForgeGuard pipeline, an input receipt image I is re-saved under a deterministic JPEG quality factor Q = 90, yielding a re-compressed image I_resaved. The absolute pixel error residual E(x, y, c) for each spatial coordinate (x, y) across RGB color channels c in {R, G, B} is formulated as:

$$E(x, y, c) = |I(x, y, c) - I_{\text{resaved}}(x, y, c)|$$

To accentuate faint compression discrepancies and ensure clear feature extraction by convolutional kernels, the residual is scaled by an amplification constant alpha = 15.0:

$$E_{\text{scaled}}(x, y, c) = \min\left(255, \; 15.0 \cdot E(x, y, c)\right)$$

Regions possessing uniform compression noise remain dark, whereas digitally spliced elements (such as pasted digits or modified text lines) exhibit pronounced high-frequency luminance spikes, creating the diagnostic feature maps processed by the CNN models.

---

### 3.6 Empirical Dataset Specifications (Dataset v2.2.0)

The empirical dataset was rigorously curated to represent realistic payment scenarios encountered in Philippine mobile commerce:

| Class / Category | Count | Proportion | Forensic Description |
|:---|:---:|:---:|:---|
| **Authentic Receipts** | **153** | **19.7%** | Genuine GCash transaction confirmations verified against banking logs (51 original screenshots + 102 clean augmented). |
| **Amount Alteration** | **153** | **19.7%** | Precision text splices in payment figures rendered in Karla Bold (`#1972F9` GCash blue). |
| **Reference Fabrication** | **153** | **19.7%** | Manipulated 13-digit transaction reference numbers rendered in Karla Regular. |
| **Name Modification** | **153** | **19.7%** | Spliced recipient names rendered in Poppins SemiBold. |
| **AI Synthetic Template** | **153** | **19.7%** | Full synthetic receipts generated via diffusion models and template scripts. |
| **Legacy Template** | **12** | **1.5%** | Baseline synthetic receipt templates. |
| **Total Dataset** | **777** | **100.0%** | Comprehensive benchmark repository (`metadata.json`). |

---

### 3.7 Model Training and Evaluation Metrics

Models were trained using an 80% training (626 samples) and 20% validation split (151 samples) on an NVIDIA T4 GPU. Performance was evaluated using standard classification metrics:

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

$$\text{Precision} = \frac{TP}{TP + FP}$$

$$\text{Recall} = \frac{TP}{TP + FN}$$

$$F_1\text{-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

Inference latency was calculated as the mean elapsed time in milliseconds (t_ms) required to execute complete forward-pass inference over 100 consecutive trials per model on CPU and GPU hardware.
