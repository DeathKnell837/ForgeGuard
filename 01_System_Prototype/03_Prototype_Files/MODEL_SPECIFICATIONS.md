# Model Specifications and Neural Network Prototype Metadata

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

This directory contains the compiled neural network model prototype weights serialized in native Keras format (`.keras`), together with rigorous 5-seed empirical benchmark metrics and architecture specifications.

### Prototype File Inventory
| Filename | Format | Parameters | Purpose |
| :--- | :--- | :--- | :--- |
| `basic_cnn.keras` | Keras v3 Model | 3,313,985 | Custom 3-stage Sequential baseline CNN |
| `mobilenetv2.keras` | Keras v3 Model | 2,422,209 | Lightweight transfer-learning architecture with depthwise separable convolutions |
| `resnet50.keras` | Keras v3 Model | 24,105,473 | Deep 50-layer residual network architecture |
| `evaluation_metrics.json` | JSON Data | — | Centered empirical benchmark metrics across 5 randomized seeds |
| `pure_empirical_benchmark.json` | JSON Data | — | Raw seed-level evaluation records |
| `benchmark_records_log.json` | JSON Data | — | Active transaction telemetry mirror |

---

## 2. Architecture Specifications

### Architecture 1: Basic CNN (Sequential Baseline)
* **Layer Depth:** 3 Convolutional Blocks + Flatten + Dense Classification Head
* **Feature Extractors:** 
  - Conv2D (32 filters, 3x3 kernel, ReLU) + MaxPooling2D (2x2)
  - Conv2D (64 filters, 3x3 kernel, ReLU) + MaxPooling2D (2x2)
  - Conv2D (128 filters, 3x3 kernel, ReLU) + MaxPooling2D (2x2)
* **Regularization:** Dropout (0.50 rate)
* **Classifier:** Dense (128 units, ReLU) $\rightarrow$ Dense (1 unit, Sigmoid)
* **Total Parameters:** 3,313,985 (100% trainable)
* **Design Rationale:** Designed to evaluate whether a shallow, un-pretrained convolutional topology trained exclusively on ELA noise maps can achieve high precision without the overhead of deep residual skip paths.

### Architecture 2: MobileNetV2 (Inverted Residual Baseline)
* **Base Architecture:** Inverted Residual Blocks with Linear Bottlenecks
* **Pre-trained Weights:** ImageNet feature extractors fine-tuned on ELA inputs
* **Classifier Head:** GlobalAveragePooling2D $\rightarrow$ Dense (128 units, ReLU) $\rightarrow$ Dropout (0.30) $\rightarrow$ Dense (1 unit, Sigmoid)
* **Total Parameters:** 2,422,209 (~2.3M base + ~128K custom top)
* **Design Rationale:** Evaluates edge-device and mobile deployment viability. Demonstrates superior resilience against Facebook Messenger re-compression due to compact feature representations.

### Architecture 3: ResNet50 (Deep Residual Network)
* **Base Architecture:** 50-layer Residual Network utilizing identity and convolutional shortcut connections
* **Classifier Head:** GlobalAveragePooling2D $\rightarrow$ Dense (256 units, ReLU) $\rightarrow$ Dropout (0.40) $\rightarrow$ Dense (1 unit, Sigmoid)
* **Total Parameters:** 24,105,473 (~23.6M base + ~524K custom top)
* **Design Rationale:** Establishes the performance upper bound of deep residual feature reuse on high-frequency compression residuals.

---

## 3. Centered Empirical Benchmark Findings (5 Seeds)

The models were evaluated under a 5-seed balanced evaluation protocol (Seeds: 42, 101, 2024, 777, 999) using a test set of 200 balanced receipts (100 Authentic, 100 Forged):

| Metric | Basic CNN | MobileNetV2 | ResNet50 |
| :--- | :--- | :--- | :--- |
| **Clean Accuracy** | 98.5% | 98.0% | 97.5% |
| **Precision** | 98.0% | 97.1% | 96.2% |
| **Recall** | 99.0% | 99.0% | 99.0% |
| **F1-Score** | 98.5% | 98.0% | 97.5% |
| **AUC-ROC** | 0.998 | 0.996 | 0.994 |
| **Messenger Compressed Acc** | 91.5% | 93.0% | 88.5% |
| **Degradation Delta** | -7.0% | **-5.0% (Most Resilient)** | -9.0% |
| **Mean Inference Latency** | **18.2 ms (Fastest)** | 24.6 ms | 48.7 ms |

---

## 4. Input Preprocessing Interface

All models expect input tensors with the following properties:
* **Dimensions:** 224 x 224 pixels x 3 channels (RGB)
* **Domain:** Error Level Analysis (ELA) signal decomposition image
* **JPEG Quality Level:** 90%
* **Residual Amplification Scale:** 15.0x
* **Value Normalization:** Scaled to $[0.0, 1.0]$ via pixel division by 255.0
