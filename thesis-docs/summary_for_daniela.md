# Summary Sheet for Daniela — ForgeGuard BSCS Thesis

## 1. Thesis Quick Info
* **Approved Title:** *Securing Mobile Transaction: A Comparative Evaluation of CNN Architectures in Detecting Digital Receipt Forgery*
* **System Name:** ForgeGuard
* **Status:** **Title Defense PASSED!** Currently in **Week 5+ (Proposal Writing for Chapters 1 & 2)**.
* **Live System Demo:** [forgeguard.streamlit.app](https://forgeguard.streamlit.app/)

---

## 2. Core Research Objectives (5 Statement of the Problem Questions)
1. **SOP 1:** What is the classification accuracy of **Basic CNN**, **ResNet50**, and **MobileNetV2** in detecting (1.1) Manually edited transaction receipts vs (1.2) Programmatically generated fake receipts?
2. **SOP 2:** What is the performance in terms of **Precision, Recall, and F1-score**?
3. **SOP 3:** What is the **inference speed (latency in ms)** and computational resource requirement of each model?
4. **SOP 4:** Is there a significant difference in classification accuracy between (4.1) Original high-resolution screenshots vs (4.2) Heavily compressed images?
5. **SOP 5:** Which architecture offers the most practical balance of accuracy and efficiency for local online sellers and student entrepreneurs at NDMC?

---

## 3. Dataset Status
* **Authentic Receipts:** 104 samples (from extracted GCash/Maya screenshots + data augmentation)
* **Forged Receipts:** 304 samples (104 Photoshop/Gallery digitally edited + 200 programmatically generated)
* **Total:** 408 labeled receipt images

---

## 4. Suggested Chapter 2 (RRL) Flow
* Digital Payment Fraud $\rightarrow$ Digital Image Forgery $\rightarrow$ Image Forensics $\rightarrow$ Error Level Analysis (ELA) $\rightarrow$ Deep Learning for Image Forgery Detection $\rightarrow$ CNN Architectures (Basic CNN, ResNet50, MobileNetV2) $\rightarrow$ Image Compression Effects $\rightarrow$ Performance Evaluation Metrics $\rightarrow$ AI Deployment for Mobile Devices
* Cited IEEE Paper: *"Image Forgery Detection Based on ELA and Deep Learning"* (IEEE 9142188)
