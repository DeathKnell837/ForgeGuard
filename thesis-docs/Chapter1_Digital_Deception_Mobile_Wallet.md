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

The widespread adoption of mobile wallets and e-payment platforms has transformed how transactions are conducted, particularly among online sellers, small business owners, and student entrepreneurs who often rely on screenshots of payment confirmations as proof of a completed transaction [1]. This reliance on screenshot-based verification, however, has created a new avenue for fraud, in which buyers manipulate or fabricate transaction receipts to deceive sellers into releasing goods or services without an actual payment having been made [1].

To address this problem, recent systems have combined Optical Character Recognition (OCR) with convolutional neural networks (CNNs) to automatically flag visually tampered payment screenshots, with early implementations demonstrating that such detection can run effectively even on lightweight, GPU-free infrastructure suited to small merchants [2]. Complementary techniques, such as error level analysis integrated with CNNs, have likewise proven effective at revealing subtle pixel-level manipulations introduced during image editing [3]. However, the robustness of these techniques against the heavy compression that images typically undergo when transmitted through messaging platforms remains comparatively underexplored [3].

The choice of underlying CNN architecture also carries practical trade-offs. Deep architectures such as ResNet have demonstrated strong feature-extraction capability through residual learning, making them well suited to capturing subtle forgery artifacts [4], while lightweight architectures such as MobileNetV2 were purpose-built for efficient inference on resource-constrained devices, making them attractive for deployment where GPU access is limited [5]. This raises the question of which architectural approach, a basic baseline model, a deep residual network, or a lightweight mobile-optimized network, offers the most practical balance of accuracy and efficiency for this specific forgery-detection task.

Local online sellers and student entrepreneurs, including those operating within school communities such as Notre Dame of Midsayap College, are especially vulnerable to this form of fraud given their frequent reliance on mobile wallet transactions and limited access to dedicated fraud-detection tools. It is against this backdrop that the present study sought to comparatively evaluate a Basic CNN, ResNet50, and MobileNetV2 in detecting digital forgery and pixel-level tampering in mobile wallet transaction receipts, in terms of classification accuracy, processing efficiency, and practical deployability.

Statement of the Problem

Mobile wallet and e-payment platforms have become frequent targets of screenshot-based fraud, in which manipulated or fabricated transaction receipts are used to deceive sellers into releasing goods or services without an actual payment having been made [1]. Recent systems combining Optical Character Recognition (OCR) with convolutional neural networks have demonstrated that visually tampered payment screenshots can be flagged effectively and in real time, even on lightweight, GPU-free infrastructure suited for small merchants [2]. Techniques such as error level analysis integrated with CNNs have likewise proven effective in detecting subtle pixel-level manipulations in digital images, although their robustness against the heavy compression typical of images transmitted through messaging platforms remains underexplored [3]. Deeper architectures such as ResNet have shown strong feature-extraction capability through residual learning [4], while lightweight architectures such as MobileNetV2 have been purpose-built for efficient inference on resource-constrained devices [5], raising the question of which architectural approach is best suited for practical forgery detection in this domain. The study sought to comparatively evaluate the performance of a Basic CNN, ResNet50, and MobileNetV2 in detecting digital forgery and pixel-level tampering in mobile wallet transaction receipts, in terms of classification accuracy, processing efficiency, and practical deployability. Specifically, this study sought to answer the following questions:

1. What is the classification accuracy of the Basic CNN, ResNet50, and MobileNetV2 models in detecting:

1.1. Manually edited transaction receipts (e.g., modified text or amounts)

1.2. Programmatically generated fake transaction receipts

2. What is the performance of the three models in classifying an image as authentic or fabricated using standard machine learning metrics in terms of:

2.1. Precision

2.2. Recall

2.3. F1-score

3. What is the inference speed and computational resource requirement of each of the three models?

4. Is there a significant difference in classification accuracy among the three models when analyzing:

4.1. Original high-resolution screenshots

4.2. Heavily compressed images

5. Which of the three architectures offers the most practical balance of accuracy and efficiency for real-world transaction verification by local online sellers and student entrepreneurs at Notre Dame of Midsayap College?

Significance of the Study

While mobile wallets offer great convenience, they have also caused a rise in scams using fake payment screenshots. This research addresses this security gap by testing different computer models to find the fastest and most accurate way to detect forged receipts on everyday devices. By identifying the best tool for the job, this study provides practical solutions and valuable information to the following stakeholders:

Local Online Sellers. This study benefits online sellers by offering a practical, benchmarked tool to verify the authenticity of payment receipts before releasing goods or services, reducing their exposure to payment fraud.

Small Business Owners in Midsayap. This study also benefits small business owners in Midsayap who accept mobile wallet payments in person and not only through online selling, by giving them a fast, reliable way to verify incoming receipts on the spot and protect their businesses from screenshot-based payment fraud.

Student Entrepreneurs. This study benefits student entrepreneurs at Notre Dame of Midsayap College by identifying which CNN architecture offers the most practical accuracy-to-efficiency trade-off, giving them an accessible means of confirming mobile wallet transactions and protecting their small-scale businesses from forged proof-of-payment scams.

Mobile Wallet Providers. This study contributes comparative findings that mobile wallet platforms may consider when selecting or strengthening the underlying architecture of their own fraud detection and receipt verification features.

Cybersecurity Researchers. This study adds to the growing body of work on image forensics and forgery detection, offering a domain-specific comparative benchmark of CNN architectures that future researchers may build upon.

Feasibility

The proposed comparative evaluation is feasible within the scope of an undergraduate thesis, as it relies on a purpose-built dataset of simulated receipts, free cloud computing resources, and mobile-efficient, well-documented model architectures suited to lightweight, GPU-free deployment.

Data Source. The study will use a custom dataset of simulated GCash transaction receipts, built by generating authentic-looking receipt templates and then producing manually edited and programmatically generated fake counterparts. Building a custom dataset is necessary because no public repository of labeled mobile wallet receipts currently exists, and it allows the researcher to control the balance between authentic and fabricated samples, as well as the range of tampering techniques represented, ensuring the dataset directly matches the study's detection objectives.

Training Environment. All three CNN architectures will be trained and evaluated using cloud-based processing through Google Colab, which provides free or low-cost access to GPU acceleration. This removes the need for the researcher to purchase or maintain dedicated high-performance hardware, making it feasible to train a Basic CNN, ResNet50, and MobileNetV2 within the timeline and budget of an undergraduate thesis.

Core Models. The study will implement a Basic/Baseline CNN, ResNet50, a deep residual architecture proven for feature-extraction capability, and MobileNetV2, a mobile-efficient architecture purpose-built for resource-constrained devices. Comparing a baseline, a deep, and a lightweight architecture directly supports the study's goal of identifying a model suited to real-world deployment on the GPU-free devices typically used by local sellers and student entrepreneurs.

Backend Stack. The system will be developed in Python, using standard image-processing and deep-learning libraries to implement the detection logic. This backend choice provides extensive documentation and community support for building, training, and evaluating CNN-based image classifiers, and is consistent with the majority of the forgery-detection literature reviewed in this study.

Frontend UI. A web application built using Streamlit or Flask will allow a user to upload a transaction receipt screenshot and receive a real-time classification result indicating whether the receipt is authentic or fabricated. This interface makes the study's output directly usable by its intended stakeholders, local online sellers, small business owners, and student entrepreneurs, and demonstrates the practical, real-world deployment angle that motivates the research.

Competence and Interest 

This research is fundamentally aligned with core competencies in system design, database logic, and Python programming developed within the College of Information Technology and Engineering (CITE). Practical experience in developing digitized platforms, specifically the CampusCrave canteen management system, provides a highly reliable foundation for understanding transaction data flows and the necessity of verifying digital payments. The ability to design structured logical models and flowcharts directly supports the task of configuring Convolutional Neural Networks (CNNs) for resource-constrained environments. By combining this technical background with a demonstrated interest in providing localized data security solutions for student entrepreneurs, the researchers are fully equipped to identify the most practical forgery detection model for everyday business use.

References

[1] C. Artaud, A. Doucet, J.-M. Ogier, and V. Poulain d'Andecy, "Receipt dataset for fraud detection," in Proc. 1st Int. Workshop on Computational Document Forensics (IWCDF), 2017. Available: http://iwcdf2017.univ-lr.fr/wp-content/uploads/2017/11/IWCDF2017_Artaud_1.pdf

[2] K. S. Vaishnavi and K. P. Narayan, "FakePay: A real-time UPI fraud detection system using OCR, CNN, and ensemble machine learning," Technical Report, Mar. 2026. Available: https://www.researchgate.net/publication/401550530_FakePay_A_Real-Time_UPI_Fraud_Detection_System_Using_OCR_CNN_and_Ensemble_Machine_Learning

[3] A. M. Nagm, M. M. Moussa, R. Shoitan, A. Ali, M. Mashhour, A. S. Salama, and H. I. AbdulWakel, "Detecting image manipulation with ELA-CNN integration: A powerful framework for authenticity verification," PeerJ Computer Science, vol. 10, p. e2205, 2024. Available: https://doi.org/10.7717/peerj-cs.2205

[4] K. He, X. Zhang, S. Ren, and J. Sun, "Deep residual learning for image recognition," in Proc. IEEE Conf. Computer Vision and Pattern Recognition (CVPR), 2016, pp. 770-778. Available: https://arxiv.org/abs/1512.03385

[5] M. Sandler, A. Howard, M. Zhu, A. Zhmoginov, and L.-C. Chen, "MobileNetV2: Inverted residuals and linear bottlenecks," in Proc. IEEE Conf. Computer Vision and Pattern Recognition (CVPR), 2018, pp. 4510-4520. Available: https://arxiv.org/abs/1801.04381