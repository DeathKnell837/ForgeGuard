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
| `basic_cnn.keras` | Keras v3 Model | 11,169,089 | Custom 3-stage Sequential baseline CNN |
| `mobilenetv2.keras` | Keras v3 Model | 2,422,081 | Lightweight transfer-learning architecture with depthwise separable convolutions |
| `resnet50.keras` | Keras v3 Model | 24,112,513 | Deep 50-layer residual network architecture |
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
* **Total Parameters:** 11,169,089 (100% trainable; at 224 x 224 input the flattened 26 x 26 x 128 feature map feeds the 128-unit dense layer)
* **Design Rationale:** Designed to evaluate whether a shallow, un-pretrained convolutional topology trained exclusively on ELA noise maps can achieve high precision without the overhead of deep residual skip paths.

### Architecture 2: MobileNetV2 (Inverted Residual Baseline)
* **Base Architecture:** Inverted Residual Blocks with Linear Bottlenecks
* **Pre-trained Weights:** ImageNet feature extractors fine-tuned on ELA inputs
* **Classifier Head:** GlobalAveragePooling2D $\rightarrow$ Dense (128 units, ReLU) $\rightarrow$ Dropout (0.30) $\rightarrow$ Dense (1 unit, Sigmoid)
* **Total Parameters:** 2,422,081 (~2.26M frozen base + ~164K custom top)
* **Design Rationale:** Evaluates edge-device and mobile deployment viability. Demonstrates superior resilience against Facebook Messenger re-compression due to compact feature representations.

### Architecture 3: ResNet50 (Deep Residual Network)
* **Base Architecture:** 50-layer Residual Network utilizing identity and convolutional shortcut connections
* **Classifier Head:** GlobalAveragePooling2D $\rightarrow$ Dense (256 units, ReLU) $\rightarrow$ Dropout (0.40) $\rightarrow$ Dense (1 unit, Sigmoid)
* **Total Parameters:** 24,112,513 (~23.6M frozen base + ~525K custom top)
* **Design Rationale:** Establishes the performance upper bound of deep residual feature reuse on high-frequency compression residuals.

---

## 3. Benchmark Findings at 224 x 224 (retrained Oct 22, 2026)

All three models were retrained at **224 x 224 x 3** (see `docs/CHANGELOG_224.md` at the repository root). The earlier figures in this section did not come from the deployed models and were removed.

### 3.1 5-seed balanced evaluation (`thesis-system/evaluate_balanced_5seeds.py`; seeds 42, 101, 202, 303, 404; N = 225 per seed: 112 authentic, 113 forged)

| Metric | Basic CNN | MobileNetV2 | ResNet50 |
| :--- | :--- | :--- | :--- |
| **Accuracy (Standard)** | 94.58% | 82.93% | 49.78% |
| **Precision (Standard)** | 100.00% | 94.53% | 0.00% |
| **Recall (Standard)** | 89.20% | 70.09% | 0.00% |
| **F1-Score (Standard)** | 94.28% | 80.47% | 0.00% |
| **Accuracy (Compressed)** | 96.36% | 89.87% | 49.78% |
| **Mean Latency (Standard, CPU)** | 52.28 ms | 56.21 ms | 79.11 ms |

### 3.2 Held-out test split from training (`thesis-system/training/train.py`; 70/15/15 split, seed 42; N = 69: 34 authentic, 35 forged)

| Metric | Basic CNN | MobileNetV2 | ResNet50 |
| :--- | :--- | :--- | :--- |
| **Accuracy** | 97.10% | 95.65% | 49.28% |
| **Precision** | 100.00% | 97.06% | 0.00% |
| **Recall** | 94.29% | 94.29% | 0.00% |
| **F1-Score** | 97.06% | 95.65% | 0.00% |
| **Inference Latency (CPU)** | 9.10 ms | 35.17 ms | 63.74 ms |
| **Unseen Holdout Recall (621 forgeries)** | 84.70% | 72.30% | 0.00% |

---

## 4. Input Preprocessing Interface

All models expect input tensors with the following properties:
* **Dimensions:** 224 x 224 pixels x 3 channels (RGB)
* **Domain:** Error Level Analysis (ELA) signal decomposition image
* **JPEG Quality Level:** 90%
* **Residual Amplification Scale:** 15.0x
* **Value Normalization:** Scaled to $[0.0, 1.0]$ via pixel division by 255.0
