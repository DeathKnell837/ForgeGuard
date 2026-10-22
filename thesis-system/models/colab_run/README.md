# Google Colab T4 Live Empirical Training Run

> **Superseded (Oct 22, 2026):** this run used 128 x 128 inputs. The deployed models in `thesis-system/models/` were retrained at 224 x 224 to match the approved manuscript. See `docs/CHANGELOG_224.md` at the repository root. This folder is kept only as a historical record of the 128 x 128 run.


This directory stores the serialized neural network models and empirical evaluation metrics trained during the live Google Colab run on **October 16, 2026** using an NVIDIA T4 GPU with High RAM.

---

## 1. Environment & Runtime Specifications

* **Platform:** Google Colab Pro
* **Hardware Accelerator:** NVIDIA T4 GPU (16 GB VRAM)
* **System RAM:** High-RAM Environment (51 GB Host RAM)
* **Runtime Duration:** 22 minutes 47 seconds
* **Input Resolution:** 128 x 128 x 3 (ELA 90Q / 15x amplified residual tensors)
* **Optimizer:** Adam (lr = 1e-4) with Binary Cross-Entropy loss

---

## 2. Empirical Benchmark Summary Table

| Architecture | Test Accuracy | Precision | Recall | F1-Score | Inference Latency | Unseen Stress Recall |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Basic CNN** | **98.55%** | **100.00%** | **97.14%** | **0.9855** | **22.71 ms** | **89.21%** |
| **MobileNetV2** | **92.75%** | **96.88%** | **88.57%** | **0.9254** | **110.52 ms** | **66.99%** |
| **ResNet50** | **52.17%** | **51.47%** | **100.00%** | **0.6796** | **129.65 ms** | **99.03%** |

---

## 3. Included Artifacts

* `basic_cnn.keras`: Serialized 3-layer custom CNN model weights (~2.1M params).
* `mobilenetv2.keras`: Serialized inverted residual depthwise separable CNN model weights (~3.4M params).
* `resnet50.keras`: Serialized 50-layer deep residual network model weights (~23.5M params).
* `evaluation_metrics.json`: Detailed empirical evaluation logs, confusion matrices, and latency telemetry.
* `pure_empirical_benchmark.json`: Percentile latency and raw classification outputs.
