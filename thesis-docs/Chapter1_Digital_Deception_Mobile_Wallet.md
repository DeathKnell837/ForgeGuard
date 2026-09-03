Securing Mobile Transaction: A Comparative Evaluation of CNN Architectures in Detecting Digital Receipt Forgery

Daniela S. Ungab

Rogie P. Bacanto

Bachelor of Science in Computer Science

Notre Dame of Midsayap College

Midsayap, Cotabato

July 2026

Chapter 1

Introduction

Background of the Study

The widespread adoption of mobile wallets and e-payment platforms has transformed how transactions are conducted, particularly among online sellers, small business owners, and student entrepreneurs who routinely rely on screenshots of payment confirmations as proof of a completed transaction [1]. Within the Philippine digital financial ecosystem, GCash has become the dominant platform for peer-to-peer commerce and over-the-counter mobile payments. However, this heavy reliance on visual, screenshot-based verification has created a critical security vulnerability: unscrupulous buyers frequently manipulate or fabricate digital payment receipts to deceive merchants into releasing goods or services without actual monetary transfer taking place [1].

To counter this form of financial deception, modern forensic approaches have integrated computer vision techniques with deep learning architectures. Digital image forensics demonstrates that manipulating raster graphics introduces imperceptible disruptions in the underlying pixel statistics. Specifically, Error Level Analysis (ELA) exploits the lossy compression characteristics of the JPEG standard: when an image is modified and re-saved, spliced or edited regions display markedly distinct compression error rates compared to untouched background pixels [3]. By extracting these compression residuals and feeding them into Convolutional Neural Networks (CNNs), automated systems can learn spatial and spectral artifacts that distinguish genuine receipts from fraudulent alterations [2], [3].

However, the practical viability of automated receipt forensics depends heavily on the choice of underlying neural architecture. Deep convolutional networks, such as ResNet50, employ residual skip connections to facilitate deep feature extraction, making them adept at capturing complex hierarchical textures [4]. Conversely, lightweight architectures such as MobileNetV2 utilize depthwise separable convolutions and inverted residual bottlenecks to drastically reduce parameter footprint and computational complexity, enabling real-time inference on consumer devices without dedicated hardware accelerators [5]. Custom baseline networks (Basic CNNs) provide an empirical control point to assess whether deep representations provide tangible diagnostic advantages over shallower feature extractors for standardized document templates.

Local online merchants, micro-retailers, and student entrepreneurs at Notre Dame of Midsayap College and within the municipality of Midsayap are acutely susceptible to receipt forgery due to rapid transaction turnaround times and lack of enterprise fraud verification infrastructure. In response to this challenge, the present study developed and comparatively evaluated ForgeGuard, an automated forensic system benchmarking Basic CNN, MobileNetV2, and ResNet50 in classifying digital GCash receipt authenticity, localizing pixel-level tampering, and assessing operational deployability in resource-constrained environments.

Statement of the Problem

Mobile wallet platforms have become pervasive targets of screenshot-based payment fraud, where digitally altered or synthetically generated receipts are leveraged to defraud merchants [1]. While computer vision and machine learning frameworks have demonstrated capability in identifying image tampering [2], [3], empirical research remains scarce regarding the comparative efficiency and diagnostic performance of diverse CNN architectures when applied to domain-specific mobile receipt forensics under varied compression states. Densely parameterized architectures such as ResNet50 require substantial compute resources [4], whereas mobile-optimized architectures like MobileNetV2 prioritize latency and parameter efficiency [5].

This study comparatively evaluated the empirical performance of a Basic CNN, MobileNetV2, and ResNet50 in detecting digital forgery and pixel-level tampering in GCash mobile wallet receipts, in terms of classification accuracy, precision, recall, F1-score, and inference latency. Specifically, this study addressed the following research questions:

1. What is the classification performance of the Basic CNN, MobileNetV2, and ResNet50 models in detecting:
   1.1. Digitally altered transaction receipts (e.g., amount splicing, reference number fabrication, and recipient name modification)?
   1.2. Programmatically generated synthetic transaction receipts?

2. How do the three benchmarked architectures compare in classifying receipt authenticity using standard machine learning metrics in terms of:
   2.1. Classification Accuracy
   2.2. Precision
   2.3. Recall
   2.4. F1-Score

3. What are the inference latency (milliseconds per transaction) and computational parameter footprints of each of the three models during real-time verification?

4. Is there a statistically significant difference in diagnostic performance across the three architectures when evaluating Error Level Analysis (ELA) compression residual matrices?

5. Which of the three evaluated CNN architectures achieves the optimal Pareto trade-off between classification accuracy and computational efficiency for real-world deployment by local online sellers and student entrepreneurs at Notre Dame of Midsayap College?

Significance of the Study

This research addresses a prevalent cybersecurity and financial vulnerability in local electronic commerce. By establishing an empirical benchmark of CNN architectures paired with Error Level Analysis, the study provides practical utility and academic contributions to the following stakeholders:

Local Online Sellers. Provides an objective, accessible verification framework to validate proof-of-payment screenshots prior to dispatching goods, mitigating direct financial losses from fraudulent payment claims.

Small Business Owners and Micro-Retailers in Midsayap. Delivers a fast, lightweight diagnostic tool enabling over-the-counter verification of mobile payments on everyday computing hardware, shielding local establishments from digital payment deception.

Student Entrepreneurs. Protects campus-based micro-enterprises at Notre Dame of Midsayap College by identifying an efficient, resource-friendly model that can run reliably on standard laptops or smartphones without paid server infrastructure.

Financial Technology and Mobile Wallet Service Providers. Contributes empirical benchmarks regarding the behavior of lightweight and deep neural networks on payment receipt forgery, offering architecture recommendations for client-side fraud screening modules.

Cybersecurity and Computer Science Researchers. Expands the academic literature on computational document forensics and transfer learning by providing an empirical dataset of 777 labeled GCash receipts and a validated ELA-CNN pipeline for mobile payment forensics.

Feasibility and Technical Specifications

The system implementation and empirical comparative evaluation have been verified as fully feasible and operational within the scope of undergraduate Computer Science thesis research:

Data Source and Dataset Specifications. The study established Dataset v2.2.0, comprising 777 labeled high-resolution mobile receipt images. This includes 153 authentic receipts (genuine GCash transaction confirmations verified through banking records) and 624 tampered receipts covering four critical attack vectors: digital amount splicing, reference number fabrication, recipient name substitution, and synthetic diffusion templates.

Training Environment. Model training and empirical evaluation were conducted on an NVIDIA T4 Tensor Core GPU using Google Colab. The pipeline utilized an 80/20 stratified train-test split with Adam optimization and binary cross-entropy loss, ensuring rigorous and reproducible experimental results without high hardware costs.

Core Neural Architectures. The comparative study implemented and benchmarked three distinct CNN paradigms:
1. Basic CNN: Custom 4-layer baseline model (~2.1M parameters).
2. MobileNetV2: Inverted residual depthwise separable architecture (~3.4M parameters).
3. ResNet50: Deep residual network featuring 50 convolutional layers with residual skip connections (~23.5M parameters).

Backend Processing and Forensic Stack. Developed in Python 3.10+ using TensorFlow/Keras for deep learning inference, Pillow and NumPy for Error Level Analysis (JPEG Q=90, scale multiplier 15.0x), and OpenCV for JET-colormap tamper heatmap localization.

Frontend User Interface and Deployment. Implemented as an interactive web platform using Streamlit and deployed live to production at forgeguard.streamlit.app. The interface features a Tri-Spectral Comparison Gallery (Original Image, ELA Noise Matrix, and Tamper Heatmap Overlay) and an interactive Model Benchmark Suite displaying empirical confusion matrices and latency gauges.

Conceptual and Architectural Framework

The system follows a 5-tier modular pipeline comprising:
1. Presentation Layer (Streamlit Web UI)
2. Forensic Preprocessing Layer (ELA 90Q Engine & OpenCV Heatmap)
3. Comparative CNN Inference Layer (TensorFlow / Keras Benchmark)
4. Data & Model Repository Layer (777-Sample Dataset & Serialized Weights)
5. Results & Forensic Decision Layer (Authenticity Verdict & Spatial Localization)

The complete architectural diagram and dataflow specification are illustrated in thesis-docs/forgeguard_system_architecture.svg.

Competence and Interest

This research builds directly upon core competencies in computer vision, deep learning, software engineering, and database logic developed within the College of Information Technology and Engineering (CITE) at Notre Dame of Midsayap College. The researchers' technical experience in developing full-stack database-driven platforms (such as the CampusCrave canteen management system) provided practical domain insight into transaction processing vulnerabilities. Combining rigorous software engineering practices with specialized machine learning workflows equipped the researchers to implement, train, and deploy an end-to-end image forensics system tailored to local community needs.

References

[1] C. Artaud, A. Doucet, J.-M. Ogier, and V. Poulain d'Andecy, "Receipt dataset for fraud detection," in Proc. 1st Int. Workshop on Computational Document Forensics (IWCDF), 2017. Available: http://iwcdf2017.univ-lr.fr/wp-content/uploads/2017/11/IWCDF2017_Artaud_1.pdf

[2] K. S. Vaishnavi and K. P. Narayan, "FakePay: A real-time UPI fraud detection system using OCR, CNN, and ensemble machine learning," Technical Report, Mar. 2026. Available: https://www.researchgate.net/publication/401550530_FakePay_A_Real-Time_UPI_Fraud_Detection_System_Using_OCR_CNN_and_Ensemble_Machine_Learning

[3] A. M. Nagm, M. M. Moussa, R. Shoitan, A. Ali, M. Mashhour, A. S. Salama, and H. I. AbdulWakel, "Detecting image manipulation with ELA-CNN integration: A powerful framework for authenticity verification," PeerJ Computer Science, vol. 10, p. e2205, 2024. Available: https://doi.org/10.7717/peerj-cs.2205

[4] K. He, X. Zhang, S. Ren, and J. Sun, "Deep residual learning for image recognition," in Proc. IEEE Conf. Computer Vision and Pattern Recognition (CVPR), 2016, pp. 770-778. Available: https://arxiv.org/abs/1512.03385

[5] M. Sandler, A. Howard, M. Zhu, A. Zhmoginov, and L.-C. Chen, "MobileNetV2: Inverted residuals and linear bottlenecks," in Proc. IEEE Conf. Computer Vision and Pattern Recognition (CVPR), 2018, pp. 4510-4520. Available: https://arxiv.org/abs/1801.04381
