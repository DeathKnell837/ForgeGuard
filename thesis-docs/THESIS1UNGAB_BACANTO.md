‘Receipt or Deceit?’: A Cross-Architecture Analysis of Convolutional Neural Network Models in Detecting Forged Digital Transaction Receipts














Daniela S. Ungab

Rogie P. Bacanto



Bachelor of Science in Computer Science


Notre Dame of Midsayap College

Midsayap, Cotabato




September 2026



# Chapter 1


# Introduction


## 1.1 Background of the Study

A payment receipt can be downloaded, opened in a photo editor, and altered to show a different amount, reference number, or recipient. Digital payment channels now account for a substantial share of everyday retail transactions in the Philippines [1], and the downloadable receipt they issue has become the document merchants rely on to confirm that money has been sent. Fraudsters exploit this reliance by editing those details on a genuine receipt file and presenting it as convincing proof of a payment that was never made, walking away with goods no one paid for [2]. The use of downloadable receipts as proof of payment therefore presents a security weakness that automated image-forensic screening could address.

Globally, digital forgery has driven advances in image-forensic architectures based on deep learning and Convolutional Neural Networks (CNNs). Benchmarks show that CNNs can learn to extract latent manipulation artifacts such as compression inconsistencies, noise variations, and edge aberrations [3]. The deep residual network ResNet50 achieves high performance on splice forgeries and pixel-level manipulations by using residual learning to enable deep feature extraction [4]. MobileNetV2, in contrast, offers efficient feature extraction at far lower computational cost, allowing deployment on mobile or edge devices without dedicated GPUs [5].

In the Philippines, the widespread use of mobile wallets such as GCash and Maya has democratized financial services but also increased opportunities for cyber fraud. As reported by the Bangko Sentral ng Pilipinas in its 2025 measurement report covering the 2024 calendar year, digital channels accounted for 57.4 percent of monthly retail payment transactions in 2024, up from 42.1 percent in 2022 [1], yet the adoption of robust real-time verification practices among MSMEs remains limited. Receipt fraud has consequently become a national concern. GCash has publicly warned that fabricated and artificially generated receipts are being circulated to claim payments that were never made, and has advised sellers not to release goods on the strength of a receipt image alone [2]. Because messaging apps heavily compress these images, visual inspection and the unaided interpretation of Error Level Analysis (ELA) maps often fail to reveal subtle modifications, requiring models trained explicitly on heavily compressed data [6]. ELA is therefore treated in this study not as a detector in its own right but as a residual-enhancement step whose output the models learn to classify.

This vulnerability is of direct concern to small business owners, local online sellers, and student entrepreneurs in Midsayap, Cotabato. Merchants here accept mobile wallet payments but typically lack the technical infrastructure to cross-check transactions with banking servers during fast-paced exchanges. No formal incidence data on forged proof-of-payment scams in the municipality has been documented. Informal accounts gathered by the researchers from student entrepreneurs, whose micro-businesses rely on peer-to-peer e-wallet transfers, point to it as an observed local concern; these accounts motivate the study but are not offered as a measure of how frequently such scams occur. Manipulated documents are increasingly difficult to detect by visual means, prompting the construction of dedicated receipt forgery datasets for training automated detectors [7]. Yet within the literature reviewed for this study, no work has comparatively evaluated Basic CNN, ResNet50, and MobileNetV2 for classifying forged downloadable GCash transaction receipts, covering both digitally edited and programmatically generated forgeries under original and messaging-platform-compressed image conditions. Without that evidence, merchants have no lightweight basis for screening the receipts they are shown.

To address this gap, this study comparatively evaluates Basic CNN, ResNet50, and MobileNetV2 in classifying GCash transaction receipt images as authentic or forged. Each model is assessed on classification accuracy, precision, recall, and F1-score under both original and heavily compressed conditions, together with end-to-end processing time and memory load. The primary goal is to determine which architecture offers the most practical balance of accuracy and processing efficiency on the limited hardware available to local merchants.

The research is well aligned with the CITE Research Agenda 2024-2030 under the Computer Science program focus areas “Emerging Technologies in Computer Science” and “Cybersecurity Threat Detection and Prevention”. It evaluates machine learning capabilities for real-time threat analysis and digital fraud prevention. The study contributes to SDG 9: Industry, Innovation and Infrastructure, and to SDG 8: Decent Work and Economic Growth, and to SDG 16: Peace, Justice and Strong Institutions through the safe and ethical use of artificial intelligence to protect digital systems.


## 1.2 Statement of the Problem

The spread of mobile wallets among local merchants has opened a security vulnerability: receipt-based payment fraud, in which manipulated transaction receipt images deceive sellers into releasing goods without an actual fund transfer [2]. Convolutional Neural Networks (CNNs) detect pixel-level tampering and compression anomalies effectively [8], but architectures such as ResNet50 and MobileNetV2 differ sharply in accuracy and computational cost [4], [5]. Which approach best holds its accuracy on heavily compressed forgeries while running on resource-constrained hardware remains unestablished.

This study therefore comparatively evaluates a Basic CNN, ResNet50, and MobileNetV2 in classifying GCash transaction receipt images as authentic or forged, assessing classification accuracy, processing efficiency, and deployability to identify the architecture best suited to receipt authenticity screening by local online sellers.

Specifically, this study seeks to answer the following questions:

What is the performance of the three models in classifying an image as authentic or forged using metrics in terms of:

1.1 Precision

1.2 Recall

1.3 F1-score

What is the classification accuracy of the Basic CNN, ResNet50, and MobileNetV2 models in detecting:

2.1 Digitally edited transaction receipts

2.2 Programmatically generated fake transaction receipts

Is there a significant difference among the Basic CNN, ResNet50, and MobileNetV2 in terms of:

3.1 End-to-end processing time

3.2 Memory load

Is there a significant difference in classification accuracy among the Basic CNN, MobileNetV2, and ResNet50 when analyzing:

4.1 Original high-resolution downloadable receipts

4.2 Compressed receipt images

Which of the Basic CNN, MobileNetV2, and ResNet50 offers the most practical balance of classification accuracy and processing efficiency on merchant-grade hardware?

## 1.3 Significance of the Study


Mobile wallets are convenient, but their adoption has been accompanied by a rise in fraud committed through fabricated payment receipts. This research addresses that security gap by comparatively evaluating three convolutional neural network architectures to determine which detects forged digital transaction receipts most accurately and most efficiently on ordinary hardware. Its findings provide the following stakeholders with practical, evidence-based guidance:

Local Online Sellers. This study provides online sellers with comparative evidence of which CNN architecture is best suited to a future receipt-verification application that could be used before goods or services are released, informing the design of tools that would reduce their exposure to payment fraud.

Small Business Owners. This study also serves small business owners in Midsayap who accept mobile wallet payments in person rather than online. It identifies which architecture can deliver a verification decision quickly enough on modest hardware to be practical at the point of sale, thereby establishing the technical basis on which such a tool could be built.

Student Entrepreneurs. This study identifies for student entrepreneurs the CNN architecture with the most feasible accuracy-efficiency trade-off, providing the evidence base for an accessible verification tool that could help secure their small-scale businesses against forged proof-of-payment scams.

Mobile Wallet Providers. The study contributes comparative findings that mobile wallet platforms may consider in selecting or reinforcing the underlying architecture of their own fraud detection and receipt verification features.

Software and Application Developers. This study helps developers build highly accurate, efficient fraud-detection tools for resource-constrained hardware. The comparative results may serve as a reference for designing lightweight verification applications suited to the constrained hardware of local merchants.

Local Government Units (LGUs) and Policymakers. This study equips Midsayap’s local government with insights to combat receipt-based fraud, protecting the economic stability of local businesses and driving sustainable economic growth.

Law Enforcement and Cybercrime Investigators. This research supports authorities working on image-based financial fraud by documenting how well convolutional neural networks of differing depth recover the latent manipulation artifacts left in forged receipts, and at what computational cost, which may inform the selection of tools used in examining pixel-level tampering and fabricated receipts.

Cybersecurity Researchers. This study adds to the growing body of work on image forensics and forgery detection, offering a domain-specific comparative benchmark of CNN architectures that future researchers may build upon.

## 1.4 Scope and Delimitations of the Study


This study is limited to the comparative evaluation of three Convolutional Neural Network (CNN) architectures, a Basic CNN, ResNet50 and MobileNetV2, in the detection of forged digital transaction receipts. The study focuses exclusively on the transaction receipts of the GCash mobile wallet because GCash is one of the most common e-wallet platforms used by local online sellers, small business owners, and student entrepreneurs in Midsayap, Cotabato. The experimental dataset is a curated sample of nine hundred experimental base images, half of them legitimate GCash downloadable transaction receipts collected from consenting local users and half of them forged versions constructed by the researchers. A further one hundred base images, fifty authentic and fifty forged using a second toolchain, are reserved as an unseen-tool holdout set, giving one thousand base images in all (500 authentic and 500 forged). Only receipts obtained through the application’s download function are included; screenshots are excluded, as they are produced by the device rather than issued by the platform and therefore carry a different artifact signature. Types of forged images include digitally edited receipts, where the text, amounts, or transaction details are altered with photo or graphic editing applications, and programmatically generated receipts, where script or template-based fabrication is used. The study also examines two image conditions: the original downloadable receipt as issued by the application, and a heavily compressed version produced by transmitting the image through Facebook Messenger at standard send quality and retaining the received file. This condition therefore carries the recompression that messaging platforms actually apply when receipts are forwarded rather than an approximation of it.

The comparative evaluation of the three architectures is confined to the following performance measures: classification accuracy, precision, recall, and F1-score in distinguishing authentic from forged receipts, as well as end-to-end processing time and memory load in assessing practical deployability on limited hardware. All efficiency measurements are taken on a single fixed benchmarking machine of ordinary specification and without a dedicated graphics processing unit, representative of the hardware available to local merchants. This study is limited to the training, testing, and benchmarking of the three models using the curated dataset, together with the Forged GCash Receipt Detection System, a lightweight web interface built solely to demonstrate and test the trained models; the development of a production verification system for merchant use is not undertaken. The study is further delimited to image-level authenticity detection: the models classify a receipt image as authentic or forged based on its visual and structural characteristics, and do not query GCash servers or any transaction database. Determining whether a payment was in fact credited to the recipient's account lies outside the scope of this study.

This study is subject to the following delimitations. It does not cover other mobile wallet platforms such as Maya or bank-issued e-wallets, focusing solely on GCash receipts. This exclusion is deliberate: the widespread use of GCash among local merchants and student micro-businesses in Midsayap made it the only platform for which a sufficient volume of authentic receipts could feasibly be collected, and confining the dataset to a single receipt layout keeps the comparative evaluation free of confounding variation in template design. It does not address other forms of digital payment fraud, such as phishing, account takeover, or SIM-swapping, as these fall outside the scope of image-based forgery detection. The forged half of the dataset is produced by the researchers with a fixed toolchain, one image editor and one template renderer, so the study reports performance on a small unseen-tool holdout set as a check on toolchain dependence rather than claiming generalization to forgeries produced by arbitrary tools. The study is also delimited to the three selected architectures and does not include a comparative evaluation of other emerging models, such as Vision Transformers or generative adversarial network (GAN)-based detectors. It is likewise delimited to whole-image classification at a common input resolution of 224 × 224 pixels, which is what the ImageNet-pretrained weights of ResNet50 and MobileNetV2 require. Patch-based classification at native resolution would retain the fine block-level compression evidence that downscaling discards. It is not undertaken here and is identified as the principal recommended extension of this work. Finally, the findings of this study are contextually anchored to the local setting of Midsayap, Cotabato, and are intended primarily to benefit local online sellers, small business owners, and student entrepreneurs; broader generalization to other regions or larger-scale commercial contexts is beyond the scope of this research.

## 1.5 Definition of Terms


The following terms are operationally defined as used in this study; the formulas by which the performance measures are computed are presented in the methodology:

Basic CNN. This refers to the baseline model built with standard convolutional, pooling and fully connected layers, trained and evaluated on the same dataset and measures as ResNet50 and MobileNetV2 for direct comparison.

Classification Accuracy. Refers to the overall correctness of a model on the test set, that is, the extent to which it assigns the authentic or forged label correctly across the images tested.

Convolutional Neural Network (CNN). Refers to the deep learning framework used to build, train, and test the Basic CNN, ResNet50, and MobileNetV2 models that classify receipt images as authentic or forged.

Dataset. Refers to the collection of GCash downloadable transaction receipt images compiled for this study, consisting of authentic and forged receipts, and partitioned into training, validation, and test sets.

Deep Learning. Refers to the branch of machine learning that uses multi-layered neural networks to learn features directly from image data, and is the approach applied to classify the receipt images as authentic or forged.

Deployability. Refers to the practicality of running a trained model on merchant-grade hardware, assessed jointly through its end-to-end processing time and memory load rather than through classification accuracy alone.

Digitally Edited Transaction Receipt. Refers to authentic GCash receipts whose text, amount, or other details were manually altered using photo or graphic-editing software, one of the two categories of forged images in the dataset.

End-to-end Processing Time. The mean elapsed time required for a trained model to process a single receipt image, timed from the reading of the stored file through decoding, preprocessing, and inference to the returned classification, one of the two components of processing efficiency.

Error Level Analysis (ELA). Refers to the technique that re-compresses an image at a fixed JPEG quality and renders the resulting compression-error differences as a visual map, applied in this study as a preprocessing transform that supplies the representation on which the models are trained, and not as a stand-alone detector.

F1-score. Refers to the single measure that balances a model's precision against its recall, used to summarize its overall classification performance on the test set.

Forgery Detection. Refers to the process of determining whether a GCash transaction receipt image has been altered or fabricated, performed by the three trained models.

GCash. Refers to the Philippine mobile e-wallet application whose downloadable transaction receipts form the dataset images, both authentic and forged.

Machine Learning. Refers to the process by which the three models are fitted to the labeled receipt images in the training set so that they can assign labels to unseen receipt images in the test set.

Memory Load. The highest resident set size reached by the detection process while it handles a single receipt image, measured in megabytes and inclusive of the loaded model, the second component of processing efficiency.

Merchant-grade Hardware. Refers to the modest, resource-constrained computing hardware typical of local online sellers, against which the practical deployability of each architecture is evaluated.

MobileNetV2. Refers to the lightweight architecture implemented and trained on the dataset and compared against the Basic CNN and ResNet50 on the same performance and resource measures.

Mobile Wallet. Refers to the smartphone application, such as GCash, through which a user stores funds and completes transactions, and which issues the downloadable transaction receipt that serves as proof of payment in this study.

Precision. Refers to the reliability of a model's forged verdicts, that is, the degree to which the receipt images it flags as forged are in fact forged.

Processing Efficiency. Refers to the computational cost of processing one receipt image end to end, from the reading and decoding of the stored file through preprocessing to inference, comprising end-to-end processing time and memory load.

Programmatically Generated Fake Receipt. Refers to receipts in the dataset fabricated through scripts or receipt-generating templates rather than manual editing, one of the two categories of forged images.

Recall. Refers to the completeness of a model's detection, that is, the degree to which it succeeds in identifying the forged receipt images present in the test set.

Receipt-based Payment Fraud. Refers to the fraud scenario represented by the forged receipts in the dataset, wherein a fabricated or altered downloadable receipt is used to simulate proof of payment that was never actually made.

ResNet50. Refers to the 50-layer residual network implemented and trained on the dataset and compared against the Basic CNN and MobileNetV2 on the same performance and resource measures.

## 1.6 Review of Related Literature and Systems


This section reviews the literature and systems most relevant to the study: digital payment fraud, digital image forgery, the effect of lossy compression on the forensic traces that detection depends on, convolutional neural networks and the characteristics of Basic CNN, ResNet50, and MobileNetV2, the metrics used to evaluate model performance, and existing receipt verification and fraud detection systems. Together, these related literature and systems establish the foundation for a comparative evaluation of CNN architectures in detecting forged GCash transaction receipts.

### 1.6.1 Related Literature



Digital Payment Fraud

The rapid growth of digital payment systems has transformed financial transactions by providing increased convenience, accessibility, and efficiency for consumers and businesses in general. However, this growth has also increased the risk of fraudulent activities and the digital payment fraud has become a growing concern across the globe. Recent studies have revealed that fraud techniques continue to evolve and exploit weaknesses in digital payment platforms, highlighting the need for advanced technologies such as artificial intelligence, machine learning, blockchain and electronic signatures to improve fraud detection and prevention. The study finds that promising research areas like digital forensics, neural networks, and image-based fraud detection are emerging to address the shortcomings of conventional fraud detection techniques, stressing the need for more intelligent and flexible security solutions in digital payment systems [9].

Two broad approaches dominate the literature that follows. Supervised classification learns fraud signatures from labeled historical transactions: one study integrated dynamic group selection and double error measurement into a machine learning classifier and demonstrated experimentally that such a model could identify fraudulent transactions reliably enough to improve customer protection and reduce financial loss [10]. Another study applied deep learning to credit card and banking data and reported improved detection accuracy over conventional machine learning baselines while maintaining latency suitable for time-sensitive banking applications [11]. Working from a different premise, a study of online payment fraud compared rule-based, statistical, and machine learning techniques and argued that no single detection model suffices on its own. It recommends instead a layered risk management system in which unsupervised anomaly detection is combined with supervised classification so that previously unseen fraud patterns can be caught without inflating the false alarm rate [12].

Cutting across both approaches is the question of timing. A real-time fraud detection framework built on machine learning classifiers processed streaming transaction data as it arrived rather than in batches after the fact, and demonstrated that doing so substantially narrows the window between a fraudulent transaction and its identification [13]. The same concern for responsiveness appears in the deep learning detector discussed above, which was reported to meet the latency demands of point-of-sale and mobile payment verification without introducing unacceptable delay [11]. Taken together, these works treat detection speed as a requirement of standing equal to detection accuracy, a dual concern the present study similarly incorporates into its own evaluation.

Taken together, these studies establish that digital payment fraud is a recognized global problem and that machine learning has become the dominant countermeasure against it. However, all of the reviewed works detect fraud from transactional and behavioral signals such as transaction amounts, timing, and account histories [9]–[13], which presupposes access to the payment platform’s internal records. None of them examines the visual authenticity of the proof-of-payment image itself. This leaves unaddressed the situation faced by local online sellers and student entrepreneurs in Midsayap, who are shown only a receipt image and have no access to GCash transaction logs. The present study addresses this gap by shifting the unit of analysis from the transaction record to the receipt image.


Image Forgery Detection

One study proposed a deep learning-based method using a pretrained AlexNet architecture to detect and localize both copy-move and spliced forgeries within a single image. The researchers generated binary masks using Sobel operators to pinpoint forged regions and extracted patch-wise feature vectors for classification. Their approach demonstrated that transfer learning from large pretrained networks could be adapted effectively to the comparatively narrow and specialized task of forgery localization, even with limited domain-specific training data [14].

A comprehensive survey examined deep learning-based approaches to image forgery detection published in recent years, organizing them into a taxonomy spanning convolutional, generative, and transformer-based detectors. The survey identified compression robustness as a persistent open challenge, noting that most existing detectors experience substantial accuracy degradation when evaluated on images that have undergone the heavy lossy compression typical of messaging and social media platforms. This finding directly parallels the compression conditions relevant to GCash receipts forwarded through chat applications [15].

Another study proposed transforming traditional handcrafted local descriptors into deep-derived features, combining the interpretability of classical image forensics techniques with the representational power of deep neural networks. The hybrid approach improved detection accuracy over purely handcrafted or purely deep baselines on standard forgery benchmarks. The authors argued that fusing classical and deep-learning features offers a practical middle ground for forgery detectors that must remain both accurate and computationally efficient [16].

A separate survey specifically reviewed recent deep-learning techniques for image forgery detection, comparing convolutional architectures, autoencoders, and hybrid detectors across splicing, copy-move, and inpainting forgery types. The survey concluded that architecture choice interacts strongly with the type of forgery being detected, meaning no single architecture consistently demonstrates superior performance across all forgery categories, which underscores the value of comparative, multi-architecture evaluations such as the one undertaken in this study [17].

To support the training of forgery detectors, one study introduced the Multiple Image Splicing Dataset (MISD), a curated benchmark specifically designed for evaluating detectors on images containing more than one spliced region. The dataset addressed a gap in earlier benchmarks, which typically contained only single-splice forgeries, and thereby provided a more realistic testbed for detectors intended for real-world deployment where multiple manipulations may coexist within a single altered document or image [18].

Collectively, this body of work confirms that manipulation leaves recoverable statistical traces and that deep learning can be trained to detect them, while also establishing that no single architecture dominates across all forgery types [17]. Two limitations are particularly relevant to the present study. First, the datasets and benchmarks used are composed of natural photographic scenes [18] rather than software-generated digital documents such as mobile wallet receipts, whose uniform templates and synthetic text present a different artifact profile. Second, programmatically generated fabrications, as opposed to edited authentic images, are rarely treated as a separate detection class. This study addresses both by constructing a receipt-specific dataset and by treating digitally edited and programmatically generated GCash receipts as distinct categories of forgery.


Compression and Forensic Detection

Three related studies establish that JPEG recompression itself leaves a learnable signature. Convolutional detectors trained to identify aligned and non-aligned double JPEG compression achieved strong performance even on small image patches and outperformed earlier state-of-the-art solutions, including in the case widely regarded as most difficult, where the first compression quality factor is higher than the second [19]. A closely comparable result was obtained by classifying histograms of discrete cosine transform coefficients with a convolutional network, which separated single-compressed from double-compressed regions and used the classification to localize tampering, again performing best when the first quality factor exceeded the second [20]. The three works agree on the finding but differ in how the compressed data is presented to the network, and a comparison of pixel-domain against frequency-domain inputs showed that this choice materially affects detection performance, making input representation a design decision with measurable forensic consequences rather than an implementation detail [21].

Addressing the practical case most similar to this study, one work examined image forgery detection specifically for images transmitted over online social networks, noting that the lossy compression and resizing operations these platforms apply pose substantial obstacles to reliable detection. The authors modeled the noise introduced by such platforms and incorporated it into a robust training scheme, reporting marked improvements over competing detectors on forgeries that had actually been uploaded to and downloaded from four widely used platforms. This confirms both that platform recompression degrades detection performance and that training on compressed data can partially recover it [6].

A broader survey of media forensics on social media platforms reviewed source identification, integrity verification, and platform provenance analysis for content shared online, describing how the community has attempted to scale forensic analysis to real-world web-based systems. The survey documented the open challenges that remain when forensic traces must survive platform processing, reinforcing that compression robustness is an unresolved problem rather than a solved one [22].

This literature confirms the premise underlying the second image condition in this study: recompression both creates its own detectable artifacts and erodes the artifacts left by earlier manipulation, so detection accuracy cannot be assumed to transfer from original to compressed images. The gap, however, is one of domain and scale. These works address natural photographs circulated on social networks and pursue pixel-level localization using specialized or computationally heavy detectors [6], whereas the present study concerns template-based mobile wallet receipts forwarded through messaging applications and requires a binary authentic-or-forged decision that runs on ordinary merchant hardware. Among the works reviewed, none measures how much accuracy standard, deployable CNN architectures lose when receipt images are heavily compressed, which is precisely what the comparison of image conditions in this study was designed to quantify.


Convolutional Neural Networks

One study directly compared convolutional neural networks against recurrent neural networks for image classification tasks, evaluating both architectures, as well as a hybrid CNN-RNN model, on the ILSVRC dataset. The results confirmed that CNNs consistently outperformed RNNs on standard image classification benchmarks, reinforcing the architectural choice of convolution-based models, rather than sequence-based models, for image forensic tasks such as receipt forgery detection [23].

Another study implemented and reviewed convolutional neural networks for general-purpose image classification, examining how convolutional and pooling layers interact to extract hierarchical visual features. The study confirmed that properly tuned CNNs achieved strong classification accuracy even on relatively small and specialized image datasets, supporting the feasibility of training the Basic CNN architecture used in this study on a curated GCash receipt dataset of limited size [24].

A separate study proposed augmenting standard CNN inputs with wavelet-domain representations, arguing that combining spatial and frequency-domain information improves a network’s sensitivity to fine-grained image artifacts. The wavelet-augmented CNN outperformed a purely spatial-domain baseline on standard classification tasks, suggesting that frequency-domain cues, such as those introduced by JPEG compression, can meaningfully improve a CNN’s ability to detect subtle image manipulations [25].

A widely cited comprehensive review traced the development of deep convolutional neural networks for image classification from their early conceptual origins through the deep learning renaissance that began in the early 2010s. The review synthesized the architectural innovations, such as convolutional weight sharing and pooling-based downsampling, that allow CNNs to generalize well across diverse visual classification tasks, providing the theoretical grounding for the Basic CNN, ResNet50, and MobileNetV2 architectures compared in this study [26].

More recently, a review specifically examined the continued role of convolutional neural networks in computer vision amid the rise of transformer-based alternatives. The review concluded that CNNs remain the more computationally efficient choice for many practical deployment scenarios, particularly on resource-constrained hardware, reaffirming the relevance of CNN-based architectures for the local, hardware-limited deployment context this study targets [27].

These foundational works support the selection of convolutional architectures over competing model families and confirm that CNNs remain the efficient choice for constrained hardware [27]. They also establish that CNNs can perform well on small, specialized datasets [24], which supports the feasibility of the modest, curated dataset used here. What they do not provide is guidance on which specific convolutional architecture should be preferred when accuracy and computational cost must be weighed against each other for a particular deployment. This general literature treats efficiency as a broad architectural property rather than as a measured quantity for a given task, and the present study responds by measuring it directly for three named architectures on a single receipt dataset.


Comparison of CNN Architectures

One study compared MobileNetV2, ResNet50, and VGG-16 for a binary image classification task involving the detection of helmet use in surveillance footage. ResNet50 achieved the highest classification accuracy at 97.81 percent, while MobileNetV2 achieved a slightly lower but still strong accuracy of 96.36 percent with a considerably smaller computational footprint. This finding is directly analogous to the accuracy-versus-efficiency trade-off this study investigates between ResNet50 and MobileNetV2 for GCash receipt classification [28].

Another study proposed lightweight edge-enhancement layers designed to improve the sensitivity of CNN-based detectors to the boundary-level artifacts common in document forgery. The proposed layers were tested across a Basic CNN, DenseNet121, ResNet50, and a Vision Transformer, evaluated specifically on a receipt forgery dataset alongside document and identity-card datasets. The study found consistent accuracy and F1-score improvements across all tested architectures, though at the cost of increased inference latency, illustrating the same accuracy-efficiency trade-off central to the comparative evaluation undertaken in this study [29].

A separate study benchmarked several lightweight convolutional neural network architectures for an image distortion classification task, systematically comparing their classification performance under differing algorithmic configurations. The study found that lightweight architectures could approach the accuracy of larger networks while requiring substantially fewer computational resources, supporting the inclusion of MobileNetV2 as a practical, resource-efficient alternative to deeper architectures such as ResNet50 in this study [30].

To address the scarcity of realistic receipt forgery data, one study introduced a dedicated receipt forgery detection dataset built from the Scanned Receipts OCR and Information Extraction (SROIE) dataset, comprising nearly one thousand scanned receipt images with a subset subjected to realistic fraudulent modifications. The study provided baseline detection results using both image- and text-based methods, offering a methodological precedent for constructing and annotating a curated, receipt-specific forgery dataset such as the GCash dataset compiled for this study [7].

A further comparative study evaluated a custom, resource-efficient CNN architecture against pretrained ResNet18 and VGG16 models for a medical image classification task. The custom CNN, despite its lower architectural complexity, achieved competitive accuracy relative to the larger pretrained models while requiring markedly fewer computational resources. This result parallels the expectation in the present study that a Basic CNN, though architecturally simpler than ResNet50 or MobileNetV2, may still achieve competitive classification performance on GCash receipt images [31].

These comparative studies supply the methodological template for the present research and consistently indicate that deeper architectures may improve representational capacity but generally involve greater computational cost [28], [31]. A remaining gap concerns the application domain. The three-way comparison has been carried out on helmet detection, brain tumor imaging, image distortion, and general document forgery, but none of the works reviewed applies it to GCash downloadable transaction receipts, and the one receipt-specific dataset located is built from scanned paper receipts [7] rather than the software-generated digital receipts issued by mobile wallets. Furthermore, none of these comparisons evaluates the same architectures across differing image quality conditions, nor across both digitally edited and programmatically generated forgeries within a single receipt domain. This study addresses these gaps by comparatively evaluating Basic CNN, ResNet50, and MobileNetV2 on downloadable GCash receipts spanning digitally edited and programmatically generated forgeries, under original and heavily compressed conditions alike.


Metrics and Model Efficiency

One study conducted a rigorous statistical evaluation of accuracy, precision, recall, F1-score, and the Matthews Correlation Coefficient across several classifiers applied to imbalanced business datasets. Using repeated-measures ANOVA and bootstrap confidence intervals, the study found that the F1-score consistently provided the most stable and balanced evaluation across varying conditions, while plain accuracy proved unreliable under class imbalance. This finding supports the decision in this study to rely primarily on precision, recall, and F1-score, rather than accuracy alone, when comparing the three CNN architectures [32].

Another study evaluated fourteen different classifiers for a binary classification task using precision, recall, F1-score, and accuracy, further examining the performance of soft-voting and hard-voting ensemble combinations. The study demonstrated that no single metric alone told the full story of classifier performance, and that F1-score in particular was necessary to reveal trade-offs between precision and recall that accuracy alone obscured, reinforcing the multi-metric evaluation strategy adopted in this study [33].

The lightweight CNN benchmarking study discussed earlier also incorporated accuracy alongside considerations of model complexity and computational demand when comparing architectures, reflecting the same dual concern for classification performance and deployability that motivates this study’s evaluation of end-to-end processing time and memory load alongside classification accuracy [30].

A separate study compared micro, macro, and weighted F1-score variants for multilabel classification under class imbalance, finding that each variant told a meaningfully different story about model performance depending on how heavily majority and minority classes were weighted. The study recommended reporting multiple F1-score variants rather than a single aggregate figure. Although the present task is binary rather than multilabel, the same underlying caution carries over: because F1-score is sensitive to how it is weighted across classes, this study reports precision, recall, and F1-score explicitly for the forged class rather than a single unqualified figure, so that performance on the class merchants most need flagged is not masked by strong performance on the other [34].

The edge-focused document forgery detection study discussed earlier also measured single-image inference latency directly, in milliseconds, when comparing baseline and enhanced CNN architectures, reporting that added architectural complexity increased latency even as it improved accuracy and F1-score. This direct measurement of the accuracy-versus-latency trade-off closely mirrors the end-to-end processing time and memory load measures this study applies when comparing the Basic CNN, ResNet50, and MobileNetV2 architectures [29].

This literature establishes best practice for reporting classification performance under class imbalance and confirms that accuracy alone is an insufficient measure [32]–[34]. The gap is that classification metrics and efficiency metrics are largely treated in separate literatures: studies that rigorously analyze precision, recall, and F1-score seldom report end-to-end processing time or resource consumption, while those that measure latency do so as a secondary observation rather than as a criterion for selection [29]. Within the studies reviewed, none jointly evaluates both families of measures for receipt forgery detection in a manner tailored to the limited hardware available to local online sellers, small business owners, and student entrepreneurs in Midsayap, Cotabato. The present study treats accuracy and efficiency as equally weighted criteria and reports them together, so that the architecture recommended is the one offering the most practical balance under realistic local conditions.



### 1.6.2 Related Systems




Fraud Detection Systems

The most directly comparable existing systems are the fraud-detection mechanisms already deployed within mobile wallet platforms themselves. One such system implemented and benchmarked four machine learning models, namely Random Forest, Logistic Regression, Support Vector Machine, and an Artificial Neural Network, to detect fraudulent activity across four prominent mobile wallet platforms, evaluating each model using accuracy, precision, and recall [35]. While this system operates in the same mobile wallet domain as the present study and adopts a comparable multi-model benchmarking methodology, it detects fraud from structured transaction records and behavioral attributes rather than from the visual content of the proof-of-payment image. Consequently, such a system cannot assist a seller who has been shown only a receipt image and has no access to the platform’s internal transaction logs, which is precisely the situation faced by local online sellers and student entrepreneurs in Midsayap.

A closely related existing system is TrustBill AI, an invoice verification and fraud-detection platform that integrates dual-engine optical character recognition, an IsolationForest anomaly-detection model, perceptual-hash-based duplicate detection, and a lightweight CNN module to flag fraudulent Goods and Services Tax (GST) invoices in a corporate procurement setting. The system achieved a fraud-detection F1-score of 0.892 by combining OCR-extracted textual fields with vendor behavioral profiling and image-based template-similarity checks [36]. While TrustBill AI demonstrates that CNN-assisted visual analysis can be combined with OCR for financial document fraud detection, it targets structured, text-heavy corporate GST invoices rather than the simpler, template-based downloadable receipts issued by consumer mobile wallets. It also depends on a full multi-role backend with GST-registry API access that is not available or appropriate for individual local online sellers and student entrepreneurs in Midsayap.

Another existing system automates the extraction of key fields, such as item descriptions, totals, and dates, from invoice images using deep learning-based object detection and text recognition, enabling end-to-end digitization of paper and scanned invoices for business information systems [37]. This system, like several others reviewed in this section, is designed for information extraction and workflow automation rather than authenticity verification; it assumes that the invoice presented is genuine and focuses on correctly reading its contents, leaving the separate problem of detecting whether the document itself has been digitally altered unaddressed.

A further system applied document layout analysis and object detection models to automatically validate machine-written invoices against multiple criteria, including the presence of required signatures and stamps, using a manually annotated dataset of real-world invoices [38]. Although this validation pipeline improves the efficiency of confirming that an invoice is structurally complete, it checks for the presence of expected layout elements rather than for pixel-level manipulation artifacts, and therefore would not be able to identify a downloadable receipt whose amount or reference number had been digitally edited or programmatically fabricated.

An earlier industrial system used a double-check processing chain that combined deep convolutional neural networks with classical image and text processing to automatically extract the store brand, purchased products, and prices from sale receipts photographed with a smartphone [39]. This system illustrates that CNN-based processing of photographed receipt images is technically feasible even under uncontrolled scanning conditions, reinforcing the choice of CNN architectures in the present study. Its objective, however, was consumption-statistics extraction rather than forgery detection. The system was also developed for physical paper till receipts rather than the software-generated, downloadable digital receipts issued by mobile wallets such as GCash.

Outside the receipt and invoice domain, a different class of system addresses image authenticity through cryptography rather than through learned visual features. PhotoProof is an image authentication system that attaches a succinct cryptographic proof of computational integrity to a signed source image, allowing any verifier to confirm that the image presented was derived from the original through an approved set of transformations such as cropping or compression [40]. Systems of this kind offer strong, mathematically grounded authenticity guarantees, but they require that the image be cryptographically signed at the point of origin. GCash downloadable receipts carry no such signature, so no trusted original exists against which a presented receipt can be verified. Establishing the authenticity of these images after the fact therefore requires a post-hoc, content-based forensic approach, such as the comparative CNN classification investigated in this study, rather than a provenance-signing system applied at the moment of creation.

Taken together, the systems reviewed above show that automated fraud-detection and document-validation platforms already exist for corporate invoices, that transaction-level machine learning systems already operate inside mobile wallet platforms, and that cryptographic provenance systems already exist for signed source images. However, none of the systems reviewed performs post-hoc, CNN-based image-forensic classification of downloadable mobile-wallet transaction receipts of the kind issued by GCash, particularly under the heavily compressed conditions typical of messaging-app transmission, and none is deployable by an individual seller who possesses only the receipt image itself. This system-level gap, alongside the literature-level gap identified in the preceding section, is what the comparative evaluation of Basic CNN, ResNet50, and MobileNetV2 undertaken in this study is intended to address.

## 1.7 Theoretical Framework


This study is anchored in two established theories. Locard’s Exchange Principle explains why a forged receipt can be detected from the image alone, while the hierarchy model of visual processing proposed by Hubel and Wiesel explains why convolutional neural networks can recover that evidence and why architectural depth trades accuracy against efficiency.

Locard’s Exchange Principle, formulated by Edmond Locard, holds that every contact leaves a trace, and it is accepted as the foundational concept of digital forensics, where every interaction with a digital artifact leaves a recoverable trace [41]. Manipulating a receipt is such a contact. An image carries statistical regularities introduced by the process that produced it, and editing disturbs them measurably [42]. Because GCash receipts carry no watermark or signature, only the passive branch applies: edited regions recompress differently from their surroundings, and generated fakes fail to reproduce the artifact signature of a genuine receipt [3], [8]. Traces also degrade under later handling, so accuracy is expected to fall under the compressed condition [15]. Resizing to a common input resolution of 224 × 224 pixels leaves the models the coarser expressions of these traces, which is a constraint of the pipeline rather than of the principle.

The hierarchy model, proposed by Hubel and Wiesel from recordings of the cat visual cortex, holds that simple cells responsive to oriented edges feed complex cells with larger receptive fields, so that abstract representations are built from local ones [43]. Fukushima realized this computationally in the Neocognitron [44], and LeCun and colleagues developed it into the trainable convolutional network [45]. A convolutional network is therefore expected to combine edge discontinuities and tonal irregularities in its early layers into representations that separate authentic from forged receipts in its deeper layers. Depth carries a cost: ResNet50 builds richer hierarchies through residual learning [4] while MobileNetV2 trades depth for efficiency [5], which is what makes the comparative evaluation undertaken in this study necessary [26], [30].

Together, the two accounts are complementary. Locard’s Exchange Principle establishes that evidence of forgery persists within the receipt image, while the hierarchy model explains how a convolutional architecture recovers that evidence and why architectures of differing depth do so with differing accuracy and cost. Their combination justifies the comparative evaluation of a Basic CNN, ResNet50, and MobileNetV2 on both original and compressed GCash transaction receipts.



## 1.8 Conceptual Framework


Figure 1 presents the Input–Process–Output (IPO) conceptual framework for the comparative evaluation of Basic CNN, ResNet50, and MobileNetV2 in detecting forged GCash receipts. As shown, the inputs are authentic and forged receipt images, the three CNN architectures, and image preprocessing parameters. The process includes image preprocessing (resizing and normalization), model training, validation and testing, model inference and classification, and performance evaluation using accuracy, precision, recall, and F1-score. The outputs are an authentic-or-forged classification, classification metrics, processing time, memory load, and a comparative model ranking. The figure summarizes the research workflow rather than listing every collection and evaluation procedure. As detailed in Sections 1.4 and 2.3, the study uses 1,000 base images (900 experimental and 100 unseen-tool holdout images); each base image also has an original and a Messenger-compressed condition. The two conditions and holdout procedures are described in the methodology but are not individually drawn in this simplified IPO figure.


Figure 1. Conceptual Framework of the Study



## 1.9 Hypotheses


Hypothesis (H₀1): There is no significant difference in the classification performance of the Basic CNN, ResNet50, and MobileNetV2 models in detecting forged GCash transaction receipts, measured by accuracy, precision, recall, and F1-score.

Hypothesis (H₀2): There is no significant difference in the classification performance of the three models between original high-resolution downloadable receipts and heavily compressed receipt images, measured by accuracy, precision, recall, and F1-score.

Hypothesis (H₀3): There is no significant difference in the processing efficiency of the Basic CNN, ResNet50, and MobileNetV2 models, measured by end-to-end processing time and memory load.

Hypothesis (H₀4): There is no significant difference in how the classification accuracy of Basic CNN, ResNet50, and MobileNetV2 changes when analyzing original and compressed GCash receipt images.



# Chapter 2


# Methodology


This chapter presents the methodology of the study. It describes the research design, the locale and the units of analysis, the sampling technique, the construction of the receipt dataset, the evaluation pipeline and the tools used to implement it, the instruments and measurements that will be applied to the three architectures, and the statistical and ethical procedures that will be observed.


## 2.1 Research Design


This study will employ a quantitative, comparative-experimental research design. Because the objective is to determine which of three existing convolutional neural network architectures, the Basic CNN, ResNet50, and MobileNetV2, offers the most practical balance of accuracy and efficiency in detecting forged GCash transaction receipts rather than to build an original system, the design will center on comparing these architectures under identical conditions. Holding the dataset, preprocessing procedure, and training configuration constant will isolate architecture as the variable of interest, so that any observed difference in performance can be attributed to the architecture itself.

The study will use a 3 × 2 factorial design: CNN architecture (Basic CNN, ResNet50, MobileNetV2) crossed with image condition (original downloadable and Messenger-compressed receipts). As specified in Section 2.7, each architecture will be trained separately for each condition using five prespecified matched random seeds, producing 30 training runs in total. The corresponding held-out receipt groups will be evaluated consistently, and their linked original and compressed images will remain within the same data partition to prevent leakage. Accuracy, precision, recall, F1-score, end-to-end processing time, and memory load will be summarized descriptively. The architecture effect (H₀1), image-condition effect (H₀2), and architecture-by-condition interaction for accuracy (H₀4) will be examined through the matched factorial analysis in Section 2.10; processing-efficiency differences (H₀3) will be assessed separately. Research Questions 1 and 2 will be answered descriptively, Research Questions 3 and 4 will also use the specified inferential comparisons, and Research Question 5 will use the predefined accuracy–efficiency decision rule. Because each image condition has a separately trained model, condition-related results will describe performance under condition-specific training rather than the robustness of one unchanged model to compression.

## 2.2 Locale and Respondents of the Study


The study will be conducted at Notre Dame of Midsayap College, situated on Quezon Avenue, Poblacion 5, Midsayap, Cotabato Province, during the first semester of the 2026–2027 academic year. Authentic GCash downloadable transaction receipts contributed by local online sellers, small business owners, and student entrepreneurs who transact within the municipality will serve as the primary data source, and together with the forged samples generated from them they will form the dataset on which the Basic CNN, ResNet50, and MobileNetV2 will be comparatively evaluated. Dataset construction will be carried out in the computer laboratory of the College of Information Technology and Engineering (CITE) and on the researchers’ personal computers, and model training in Google Colab; because processing efficiency is one of the dependent variables, however, every processing-time and memory-load measurement will be taken on a single fixed machine of ordinary specification without a dedicated graphics card, representative of the equipment available to local merchants, whose specifications will be recorded and reported alongside the results.

Because the units of analysis in this study are receipt images and the models trained on them rather than persons, no participant will be surveyed for personal opinions or behavioral data. Persons will nonetheless take part in two supporting capacities, which are distinguished here so that the two roles are not conflated.

The first group are the receipt contributors. Approximately thirty to fifty local online sellers, small business owners, and student entrepreneurs who actively transact through GCash within Midsayap will each contribute approximately ten to twenty downloadable receipts from their own completed transactions, until the five hundred authentic base images, including fifty reserved for the holdout set required by the study have been assembled. Their participation consists of submitting receipt images together with their electronic consent through the procedure set out in Section 2.4; they will not be asked to answer any questionnaire. The second group are the expert validators. Three faculty members of Notre Dame of Midsayap College specifically from College of Criminal Justice Education with teaching or professional experience in cybersecurity, or a related field will assess the realism of the forged receipt samples and the appropriateness of the evaluation instruments, using the Forgery Realism Validation Rubric described in Section 2.8. The validators will be drawn from faculty who are not members of the researchers' thesis panel, so that the content validation of the forged samples remains independent of the evaluation of the study itself. Apart from these ratings, they will supply no data of their own. Excluded from the study will be transaction receipts issued by other digital wallet or banking platforms, photographed, scanned, printed, or handwritten receipts, and individuals who do not transact through GCash within Midsayap.


## 2.3 Sampling Technique


This study will use purposive sampling to recruit approximately thirty to fifty local GCash-transacting receipt contributors and three independent expert validators. Quota sampling will set the dataset totals at 900 experimental base images (450 authentic and 450 forged, with 225 digitally edited and 225 programmatically generated) and 100 additional unseen-tool holdout base images (50 authentic and 50 forged). The experimental base images will be assigned to training (60%), validation (15%), and testing (25%) partitions through stratified group-based allocation, with the intended counts shown in Table 1. Group identifiers will connect each authentic source receipt, any forged versions derived from that receipt, any donor receipts used during editing, and all compressed counterparts. All linked images will remain in the same partition; donor-source links spanning multiple receipts will be grouped together before splitting. Where grouping prevents the exact category quotas in Table 1, the achieved counts and reason for deviation will be reported. Contributors whose receipts appear in the unseen-tool holdout will be excluded from the experimental splits wherever feasible, and any unavoidable overlap will be documented. The holdout set will remain separate from model fitting, validation, and hyperparameter selection.

Table 1. Composition and Partitioning of the Dataset

| Category | Subcategory | Base Images | Training (60%) | Validation (15%) | Testing (25%) |
| --- | --- | --- | --- | --- | --- |
| Authentic | Downloadable GCash receipts | 450 | 270 | 68 | 112 |
| Forged | Digitally edited receipts | 225 | 135 | 34 | 56 |
| Forged | Programmatically generated receipts | 225 | 135 | 33 | 57 |
| Total (Experimental Set) |  | 900 | 540 | 135 | 225 |
| Holdout | Authentic (withheld receipts) | 50 | — | — | — |
| Holdout | Forged (second toolchain) | 50 | — | — | — |
| Total (Holdout Set) |  | 100 | — | — | — |
| Grand Total |  | 1,000 | 540 | 135 | 225 |


## 2.4 Data Gathering Procedure


The image corpus will be assembled in six phases, separately from the performance data generated once the models are running.

Phase 1. Permission and Consent. The thesis adviser and the CITE department will approve the study before collection begins, and contributors will be informed of its purpose, the images requested, and their right to withdraw. Consent will be affirmed electronically on the submission form, so every submission will carry a timestamped record as the Data Privacy Act of 2012 [46] allows.

Phase 2. Collection of Authentic Receipts. Contributors will download receipts of their own completed transactions and submit them through a Google Form that preserves the original resolution and encoding. Screenshots will be excluded because they are produced by the device rather than issued by the platform and so carry a different artifact signature. Submissions will be logged and screened for duplicates.

Phase 3. Construction of the Forged Receipts. The researchers will work offline, using splicing and copy-move to alter the amount, reference number, recipient’s name, and timestamp of authentic receipts, recording each source and donor receipt so that provenance can be enforced at partitioning. Editing will be varied in care and save quality so that the models learn tampering in general rather than one editing signature. The remaining forgeries will be rendered from templates reproducing the GCash layout with randomized fields.

Phase 4. Generation of the Compressed Condition. Every base image will be transmitted through Facebook Messenger at standard send quality, the platform local buyers and sellers most commonly used to forward proof of payment, and the received file will be kept as its compressed counterpart. The same path, devices, and send setting will be used for both classes so that compression cannot itself become a class cue [6], [19]–[21].

Phase 5. Labeling, Organization, and Storage. Images will receive coded filenames in a structure organized by class, forgery subtype, and image condition, with a label file recording the ground-truth class and provenance group. Ground truth will be known by construction, labels will be cross-checked by both researchers, and the dataset will be stored encrypted.

Phase 6. Unseen-Tool Holdout Set. One hundred base images—fifty authentic receipts and fifty forged receipts produced using a second image editor and an independently written template implementation—will be reserved before model development for a final test of toolchain dependence. Every holdout receipt, its compressed counterpart, and any related source or donor image will be kept outside the experimental training, validation, and test partitions. No holdout image, label, or metric will be used to select models, tune thresholds, or adjust preprocessing. The holdout will be evaluated only after the models and evaluation procedure have been finalized, and its results will be reported separately from the experimental test-set results.

## 2.5 System Architecture


This section presents the lightweight Forged GCash Receipt Detection System used to demonstrate the trained models and the experimental evaluation pipeline used to measure them. Figure 2 shows the data exchanged with the User; Figure 3 shows the functions exposed to that User; and Figure 4 summarizes the interface, application processing and storage components. The system is a research demonstration, not a production payment-verification service. The experimental training, paired image-condition comparisons, validation and benchmarking procedures are described in Sections 2.3–2.10 and are more detailed than the simplified system diagrams. In particular, the demonstration classifies image appearance only and cannot confirm that a GCash payment actually reached an account.

### 2.5.1 Context Diagram


Figure 2 presents the context diagram of the Forged GCash Receipt Detection System, using a single system process and one external entity, the User. The User can submit a GCash receipt image, issue a classification request (Run Analysis), or select an available test sample. In response, the system provides an authentic-or-forged classification result, confidence scores for the Basic CNN, ResNet50, and MobileNetV2 models, benchmark metrics, and a processed receipt image represented as an Error Level Analysis (ELA) image. The context diagram shows information exchanged across the system boundary; it does not show the internal image processing, classification, or data-storage modules. Classification is based on image characteristics and does not verify an underlying financial transaction.


Figure 2. Context Diagram of the Forged GCash Receipt Detection System


### 2.5.2 Use Case Diagram


Figure 3 shows the use case diagram of the Forged GCash Receipt Detection System. The diagram identifies one external actor, the User, who can upload a GCash receipt or select an available test sample, run the classification analysis, view the authentic-or-forged classification result, inspect model confidence scores, and view benchmark metrics. The three trained CNN architectures operate within the system rather than as separate actors. Dataset collection, forging and labeling, model training, validation, and statistical testing are research activities described in the methodology and are not shown as User use cases. Functions such as managing models, generating threat levels, or displaying a multi-CNN consensus are not represented in this figure and are not claimed as separate use cases.


Figure 3. Use Case Diagram of the Forged GCash Receipt Detection System

### 2.5.3 Architecture Diagram


Figure 4 shows the system architecture in three layers: User Interface, Application Layer, and Database Layer. Through the User Interface, the User uploads a JPG or PNG receipt image. The Application Layer includes Image Preprocessing, CNN Inference, and Result Processing. As depicted, Image Preprocessing resizes the image to 224 × 224 pixels, normalizes it to values between 0 and 1, and prepares a three-channel tensor. CNN Inference applies the trained Basic CNN, ResNet50, and MobileNetV2 models; Result Processing produces an authentic-or-forged classification and confidence score and records processing time and memory load. The Database Layer retains trained model files and benchmark records, including prediction and measurement data. The figure is a high-level architecture: the Error Level Analysis (ELA) transformation prescribed in the experimental methodology is included within image preprocessing but is not separately labeled in this drawing. For reproducibility, Section 2.6 specifies its proposed 90% JPEG quality and fifteen-fold error amplification; its exact position relative to resizing and normalization will be fixed for all models before training and documented in the implementation. End-to-end efficiency measurements used for the thesis will be obtained through the separate fixed-hardware profiling procedure described in Sections 2.6 and 2.8, rather than relying on browser response time. The architecture diagram is not intended to represent model training, the full factorial experiment, or financial transaction verification.[47][48]


Figure 4. Architecture Diagram of the Evaluation Pipeline


## 2.6 Software and Tools


The study will be implemented entirely in software, and the tools described in this section are those that will be used to construct the dataset, build and train the models, take the performance measurements, and analyze the results. All versions will be fixed at the outset and recorded, since a change of library version during experimentation would compromise the comparability of measurements taken before and after it.

The backend of the pipeline will be implemented in Python, which will serve as the primary programming language for the image processing and detection logic, covering preprocessing, model training, evaluation, and measurement. The three architectures under comparison, namely the Basic CNN, ResNet50, and MobileNetV2, will be constructed and trained in TensorFlow using the Keras API, with model development and training carried out in Google Colab notebooks using its graphics-accelerated runtime. ResNet50 and MobileNetV2 utilize convolutional backbones initialized with pretrained weights from the ImageNet database [47], whereas the Basic CNN is initialized from scratch with random weight distributions. Model parameter updates during training are governed by the Adam optimizer [48] under a binary cross-entropy loss function.

Dataset construction will rely on Google Forms for the collection of authentic receipts from contributors, on OpenCV and Pillow for image reading, resizing, format handling, and the Error Level Analysis transform configured at 90 percent JPEG quality with fifteen-fold error amplification, on Facebook Messenger for the transmission that produces the compressed image condition, on consumer image editing applications such as Canva for the production of the digitally edited forged receipts, and on Python imaging and document rendering libraries for the production of the programmatically generated forged receipts. A second image editor, either GIMP or Photopea, and a second rendering implementation using a different imaging library and font stack will be reserved exclusively for the unseen-tool holdout set described in Phase 6, and will be used for no other part of the dataset. Stratified partitioning of the dataset into its training, validation, and test sets will be performed with scikit-learn.

Measurement and analysis will draw on the Python time module and psutil for end-to-end per-image latency and peak memory consumption, on NumPy and pandas for numerical computation and the tabulation of the recorded performance data, and on scikit-learn for the confusion matrices and the computation of precision, recall, and F1-score. The assumption tests, the analysis of variance, and the post hoc comparisons will be carried out in SciPy and SPSS, with SciPy used for the Shapiro-Wilk test of normality and for the Friedman and Wilcoxon signed-rank tests where the non-parametric fallback is applied, and SPSS for the repeated-measures analysis of variance, Mauchly's test of sphericity, the Greenhouse-Geisser correction, and the Bonferroni post hoc comparisons, while Matplotlib and seaborn will generate the training curves, confusion matrix plots, and comparative charts of the results.

The frontend will be a lightweight web application built with Streamlit, which will provide a simple interactive interface through which the trained models can be demonstrated and tested on individual receipt images. It will communicate with the Python backend that performs the classification, and will not be used to take any of the efficiency measurements reported in this study, which will be recorded directly by the profiling harness described later in this chapter.

The same software environment will be used for every training run and, more importantly, for every efficiency measurement, since inference latency and memory consumption are sensitive to the computational environment in which they are recorded.

## 2.7 Data Collection


After securing adviser and CITE department approval, contributors will submit their own GCash receipts with electronic consent, from which the forged and compressed counterparts will be constructed. Each of the three architectures will then be trained five times under each image condition using the same fixed seeds, with training carried out in Google Colab. Efficiency will be measured on a single fixed, ordinary-specification machine without a dedicated GPU, representative of merchant hardware, with background applications closed and power settings held constant. This design yields thirty runs in total, whose accuracy, precision, recall, F1-score, latency, and memory will be reported as means and standard deviations rather than single-run outcomes. The unseen-tool holdout set will be evaluated once per trained model and reported descriptively rather than entered into any hypothesis test. Each independent training run will use a proposed maximum of 50 epochs; the epoch-by-epoch training and validation results and the number of epochs actually completed will be logged. The five independent runs per architecture–image-condition combination are distinct from the number of epochs within each run.

Three validators will separately rate a random sample of the forged receipts on visual plausibility, layout fidelity, internal consistency of transaction details, and absence of conspicuous editing artifacts. Their ratings will be used to confirm that the forged samples represent a realistic fraud attempt rather than an implausibly crude one. All data obtained, including contributed receipts and validator responses, will be handled under the Data Privacy Act of 2012 (RA 10173) [46] , with confidentiality maintained throughout and access restricted to the researchers and the thesis adviser.

## 2.8 Instrumentation


The instruments of this study will be computational and documentary rather than survey-based, since the objects measured are models and images rather than persons. Four instruments will be used.

The Curated Dataset and Labeling Protocol. The dataset described earlier will function as the test instrument through which the three architectures will be examined. Its ground-truth labels will be known by construction, its class composition will be balanced by design, and its partitioning will be fixed in advance, which together will allow every model to be examined under identical conditions.

The Confusion Matrix and Classification Metric Suite. Classification performance will be measured through the four-cell confusion matrix and the metrics derived from it. Consistent with the operational definitions of the study, the forged receipt will be treated as the positive class throughout. A true positive (TP) is a forged receipt correctly identified as forged, a true negative (TN) an authentic receipt correctly identified as authentic, a false positive (FP) an authentic receipt incorrectly flagged as forged, and a false negative (FN) a forged receipt incorrectly accepted as authentic. The metrics will be computed as follows:

Accuracy = (TP + TN) / (TP + TN + FP + FN)

Precision = TP / (TP + FP)

Recall = TP / (TP + FN)

F1-score = 2 × (Precision × Recall) / (Precision + Recall)


To answer Research Question 2, subtype-specific accuracy will be computed separately for digitally edited and programmatically generated forged receipts. Each subtype evaluation will use the same prespecified authentic test subset alongside only the forged images of that subtype; the forged category remains the positive class. Accuracy_subtype = (TP_subtype + TN_subtype) / (TP_subtype + TN_subtype + FP_subtype + FN_subtype). Because the same authentic subset is reused, the two subtype-specific accuracy estimates are not independent and will be interpreted descriptively rather than treated as independent experimental groups. Class-specific forged detection recall will also be reported to show the number of each subtype that is detected, without substituting it for the requested accuracy metric.

The false negative is the error of principal practical consequence in this domain, since it corresponds to a forged receipt accepted as genuine and to goods released without payment. Recall will therefore be interpreted with particular attention, and the F1-score will be used to summarize the balance between the two error types, following the evaluation literature reviewed earlier, which holds that accuracy alone is insufficient [32]–[34].

The Efficiency Measurement Instrument. Processing efficiency will be measured by a timing and profiling harness written for this study. It will record the end-to-end elapsed time required to process a single receipt image, timed from the reading of the stored file through decoding, preprocessing, and inference to the returned classification, and excluding a warm-up series. The interval will be deliberately bounded at the stored file rather than at the input tensor, because the cost a merchant actually incurs in checking a receipt includes the decoding and preprocessing of whatever file arrives, and because the two image conditions differ in file size and encoding and therefore in the cost of those stages. Were timing to begin at the input tensor, every image would already have been resized to identical dimensions and the image condition could exert no effect on the measurement by construction. The resident set size of the process will be sampled across the same interval, and the highest value reached will be recorded as the memory load. Because sampling will begin after the model has been loaded, this figure will include the static footprint of the model weights together with the memory allocated during decoding, preprocessing, and inference, which is the quantity that determines whether an architecture fits within the memory available on merchant-grade hardware. This instrument follows the practice of the edge-focused forgery detection work reviewed earlier, which measured single-image latency directly in milliseconds when comparing architectures [29].

The Forgery Realism Validation Rubric. A short rubric will be provided to the validators for the assessment of a random sample of forged receipts. Each sampled image will be rated on a four-point scale across four criteria: visual plausibility at a glance, fidelity to the layout of a genuine GCash receipt, internal consistency of the transaction details, and absence of conspicuous editing artifacts. The rubric will establish that the forged images represent a realistic fraud attempt rather than an implausibly crude one, and its use is described further below.

The classification measures will be computed as defined above, while the efficiency measures produced by the timing and profiling harness are defined operationally in Table 2. Both families of measures will be recorded for each of the six architecture-condition combinations.

Table 2. Operational Definitions of the Efficiency Measures

| Measure | Operational Definition | Unit |
| --- | --- | --- |
| End-to-end processing time | Mean end-to-end elapsed time to process one receipt image, from file read through decoding and preprocessing to classification | Milliseconds |
| Memory load | Peak resident set size of the detection process, inclusive of the loaded model, sampled across the same interval as the end-to-end processing time | Megabytes |


## 2.9 Validity and Reliability of the Instruments


The validity of the instruments rests on the design of the dataset and the measurement procedure rather than on the psychometric testing appropriate to questionnaires. Content validity will be secured through expert review: a random sample of the forged receipts will be rated by the three validators using the rubric described above, images judged implausible or conspicuously crude will be revised before the dataset is finalized, and the agreement among the three validators will be reported as Kendall's coefficient of concordance, which is appropriate to ordinal ratings supplied by a fixed set of raters. Construct validity rests on measuring classification performance through the four metrics standard in the forensic classification literature [32]–[34] and processing efficiency directly as latency and memory consumption rather than inferring it from parameter counts [29], [30]. Internal validity will be protected by holding the dataset, preprocessing sequence, training configuration, and benchmarking hardware constant across the three architectures and by reserving the testing partition for final evaluation, while the unseen-tool holdout set described in Phase 6 will expose any dependence on the toolchain that produced the forgeries. External validity is bounded by the delimitations of the study.

Reliability will be addressed as repeatability of both training and measurement. Random seeds, library versions, hyperparameters, preprocessing settings and hardware specifications will be fixed and documented. Five independent training runs using matched seeds will be performed for each architecture–image-condition combination; these five runs will supply the repeated model-level observations for the primary descriptive and inferential comparisons. A separate five-fold stratified, group-aware cross-validation exercise will be conducted only on the non-test portion of the experimental dataset as a supplementary check of split sensitivity. It will not replace the predefined training/validation/test partition, will not include the held-out test or unseen-tool holdout images, and will not be pooled with the five primary seed repetitions as though they were independent observations. Related authentic, forged and compressed images will stay in the same fold. Efficiency will be measured repeatedly on the same fixed benchmarking machine after warm-up and under controlled settings, with measurement summaries and variability reported.

## 2.10 Statistical Tools and Treatment of Data


The study will use descriptive and inferential statistics, with a significance level of α = 0.05 for prespecified hypothesis tests. For Research Questions 1 and 2, each architecture’s test-set accuracy, precision, recall, and F1-score will be reported by image condition, with mean and standard deviation across five matched training seeds. Research Question 2 will additionally report subtype-specific accuracy for digitally edited and programmatically generated forged receipts, using the common authentic comparison subset described in Section 2.8. The same seed identifiers and test receipt groups will be used for paired comparisons. The small number of training seeds limits the power of normality tests and the reliability of p-values, so effect sizes, uncertainty intervals where feasible, and descriptive comparisons will accompany inferential results. The testing partition and unseen-tool holdout will remain untouched for model tuning.

For Research Question 4, a 3 × 2 within-block factorial analysis of model-level classification metrics will assess the architecture main effect (H₀1), the image-condition main effect (H₀2), and the architecture × image-condition interaction in accuracy (H₀4), with the same five prespecified seeds treated as matched blocks. Separate models will be fitted to accuracy, precision, recall, and F1-score, but the interaction test specified by H₀4 will concern accuracy. Residual distributions, dependence, and sphericity will be assessed where applicable; Greenhouse–Geisser adjustment will be used if sphericity is violated. Because only five matched seeds are planned, inference will be interpreted cautiously and the observed paired differences will be reported. If assumptions cannot be supported, the study will prioritize descriptive paired contrasts with uncertainty intervals and clearly label any exploratory nonparametric tests rather than claiming that separate Friedman tests provide a full replacement for the factorial interaction analysis. For Research Question 3, latency and peak memory will be compared among architectures on the fixed benchmarking machine using matched image sets and repeated measurement summaries; architecture comparisons will use a within-block analysis or an appropriate paired nonparametric alternative, with multiplicity-adjusted post hoc comparisons. Benchmarked receipt-level measurements will not be treated as independent training repetitions.

For Research Question 5, the primary decision rule will combine classification accuracy and deployment efficiency using prespecified min–max normalization across the three architectures, calculated from experimental test-set means on the same benchmarking hardware. For a metric in which higher is better, normalized value = (value − minimum) / (maximum − minimum); for latency or memory, in which lower is better, normalized value = (maximum − value) / (maximum − minimum). If all architectures have an identical value for a metric, each will receive a neutral normalized score of 0.5 for that metric. The proposed composite score is 0.50 × normalized accuracy + 0.25 × normalized processing-time efficiency + 0.25 × normalized memory efficiency, with higher scores considered better. Accuracy will be averaged equally over original and compressed test conditions before normalization, and efficiency metrics will be averaged over those same conditions. Mean forged-class recall, performance on the unseen-tool holdout, and observed hardware limits will be reported alongside the score; they will not be concealed by the composite ranking. The proposed weights and normalizing rule require adviser approval before running the experiments and must not be changed after inspecting test results. Table 3 maps these analyses to the research questions.

Table 3. Statistical Treatment of Data by Research Question

| Research Question | Data Required | Statistical Treatment |
| --- | --- | --- |
| 1. Precision, recall, and F1-score | Confusion matrices by architecture and image condition across matched runs | Descriptive metrics; mean and standard deviation across five seeds |
| 2. Classification accuracy by forgery subtype | Separate authentic-versus-digitally-edited and authentic-versus-programmatically-generated evaluation subsets | Subtype-specific accuracy, mean, standard deviation, and forged-class recall for context |
| 3. Differences in end-to-end processing time and memory load (H₀3) | Paired latency and peak-memory summaries for the same receipt sets on fixed hardware | Within-block comparisons by architecture, assumption checks, multiplicity-adjusted contrasts; paired nonparametric alternatives when appropriate |
| 4. Accuracy difference by architecture and condition (H₀1, H₀2, H₀4) | Model accuracy across three architectures and two image conditions with matched seeds; precision, recall, and F1-score as supporting measures | 3 × 2 matched-block factorial analysis: architecture effect, condition effect, and their interaction on accuracy; report effect sizes and uncertainty; assess assumptions |
| 5. Most practical balance of accuracy and efficiency | Mean accuracy, latency, and memory on fixed hardware; unseen-tool holdout and forged-class recall as supporting evidence | Prespecified weighted min–max composite: 50% accuracy, 25% latency, 25% memory; practical interpretation and sensitivity caveats |


## 2.11 Ethical Consideration


This study will handle authentic financial documents and will deliberately produce forged ones, so its ethical obligations extend beyond the treatment of participants to the handling of the data and the dissemination of the findings. The following safeguards will be observed.

Institutional Approval. The study will be conducted only after the endorsement of the thesis adviser and the approval of the CITE department have been secured, and it will adhere throughout to the research policies of Notre Dame of Midsayap College.

Informed Consent and Voluntary Participation. Receipt contributors and validators will participate voluntarily and will record their consent electronically before participating, contributors through the submission form and validators through the validation instrument. Each will be informed of the purpose of the study, the use to which the material will be put, the duration of storage, and the right to withdraw at any time without penalty and to have submitted material removed. No inducement will be offered.

Privacy and Data Protection. GCash transaction receipts contain personal information and will be handled in accordance with the Data Privacy Act of 2012 [46]. Receipts will be received through a Google Form accessible only to the researchers, then moved to the study's encrypted storage with contributor identities replaced by codes; access will be restricted to the researchers and the thesis adviser, and the dataset will be neither published nor shared with any third party. Personal details will not be erased from the images, because altering pixels would introduce artifacts indistinguishable from tampering and would invalidate the classification task itself; confidentiality will therefore be protected by restricting access to the dataset rather than by modifying it. Each receipt also carries the details of a counterparty who is not a participant and whose consent cannot be obtained through the contributor, so no counterparty name, mobile number, transaction amount, or reference number will be extracted, transcribed, indexed, or analyzed at any stage, and no receipt will be retrieved or cross-referenced by the name or number of any person appearing in it. Contributors will be asked, where feasible, to submit receipts whose recipient was a business or merchant rather than a private individual. Any receipt reproduced in the manuscript or presentation will be redacted before display and will never be used as training or testing data, and the dataset will be permanently deleted from all storage locations one year after the acceptance of the study.

Responsible Handling of Forged Material. The forged receipts created for this study will be produced solely for training and testing. They will never be sent to any merchant, used in any actual transaction, or presented as proof of payment, and the forged images, the templates, and the scripts used to generate them will not be published or distributed. The manuscript will report the comparative performance of the architectures without providing instructions that would assist in producing convincing forgeries, resolving the dual-use character of the work in favor of restricting the means of forgery while disseminating the means of detection.

Lawful Access. All authentic receipts will be obtained through the ordinary and legitimate use of the GCash application by their rightful account holders. At no point will the researchers attempt to access the systems, servers, databases, or programming interfaces of the platform, and no security control will be circumvented in the course of the study.

Use of Artificial-Intelligence Tools. The researchers acknowledge the use of artificial-intelligence (AI) tools as supplementary aids in the conduct of this study, employed to improve clarity, organization, and efficiency in the writing of the manuscript and in the handling of data. All core ideas, interpretations, model implementations, and measurement results remain the original work of the researchers. The use of these tools is governed by the principle of academic integrity, so that they serve only as an aid to improvement and never as a substitute for the researchers' own knowledge, critical thinking, and contribution, and such use will be disclosed in accordance with institutional policy.



# References


[1] Bangko Sentral ng Pilipinas, “2024 Report on the Status of Digital Payments in the Philippines,” Bangko Sentral ng Pilipinas, Manila, Philippines, 2025. [Online]. Available: https://www.bsp.gov.ph/PaymentAndSettlement/2024_Report_on_E-payments_Measurement.pdf

[2] G-Xchange, Inc., “GCash warns public on emerging AI-generated fake receipts scams, urges users to always check transactions tab,” Mynt Newsroom, Jul. 2025. [Online]. Available: https://mynt.com.ph/newsroom/gcash-warns-public-on-emerging-ai-generated-fake-receipts-scams-urges-users-to-always-check-transactions-tab

[3] J. H. Bappy, C. Simons, L. Nataraj, B. S. Manjunath, and A. K. Roy-Chowdhury, “Hybrid LSTM and Encoder-Decoder Architecture for Detection of Image Forgeries,” IEEE Transactions on Image Processing, vol. 28, no. 7, pp. 3286–3300, Jul. 2019, doi: 10.1109/TIP.2019.2895466.

[4] K. He, X. Zhang, S. Ren, and J. Sun, “Deep Residual Learning for Image Recognition,” 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Las Vegas, NV, USA, 2016, pp. 770–778, doi: 10.1109/CVPR.2016.90.

[5] M. Sandler, A. Howard, M. Zhu, A. Zhmoginov, and L. Chen, “MobileNetV2: Inverted Residuals and Linear Bottlenecks,” 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition, Salt Lake City, UT, USA, 2018, pp. 4510–4520, doi: 10.1109/CVPR.2018.00474.

[6] H. Wu, J. Zhou, J. Tian, J. Liu, and Y. Qiao, “Robust Image Forgery Detection Against Transmission Over Online Social Networks,” IEEE Transactions on Information Forensics and Security, vol. 17, pp. 443–456, 2022, doi: 10.1109/TIFS.2022.3144878.

[7] B. M. Tornés et al., “Receipt Dataset for Document Forgery Detection,” in Document Analysis and Recognition – ICDAR 2023, Lecture Notes in Computer Science, vol. 14189, Springer, Cham, 2023, pp. 454–469, doi: 10.1007/978-3-031-41682-8_28.

[8] Y. Wu, W. AbdAlmageed, and P. Natarajan, “ManTra-Net: Manipulation Tracing Network for Detection and Localization of Image Forgeries With Anomalous Features,” 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Long Beach, CA, USA, 2019, pp. 9535–9544, doi: 10.1109/CVPR.2019.00977.

[9] V. Laxman, N. Ramesh, S. K. Jaya Prakash, and R. Aluvala, “Emerging threats in digital payment and financial crime: A bibliometric review,” Journal of Digital Economy, vol. 3, pp. 205–222, Apr. 2025, doi: 10.1016/j.jdec.2025.04.002.

[10] J. Wang, “Fraud Detection in Digital Payment Technologies Using Machine Learning,” Journal of Economic Theory and Business Management, vol. 1, no. 2, pp. 1–6, Apr. 2024, doi: 10.5281/zenodo.10926495.

[11] M. I. Ayub, B. Bhattacharjee, A. K. Gharami, M. S. Rahman, and M. A. Hossain, “Deep Learning for Real-Time Fraud Detection: Enhancing Credit Card Security in Banking Systems,” The American Journal of Engineering and Technology, vol. 7, no. 4, pp. 141–150, 2025, doi: 10.37547/tajet/Volume07Issue04-19.

[12] P. Vanini, S. Rossi, E. Zvizdic, and T. Domenig, “Online payment fraud: From anomaly detection to risk management,” Financial Innovation, vol. 9, art. 66, pp. 1–25, 2023, doi: 10.1186/s40854-023-00470-w.

[13] B. Borketey, “Real-Time Fraud Detection Using Machine Learning,” Journal of Data Analysis and Information Processing, vol. 12, pp. 189–209, 2024, doi: 10.4236/jdaip.2024.122011.

[14] D. P. Timothy, and A. K. Santra, “Deep Learning-based Copy-Move and Spliced Image Forgery Detection,” International Journal on Recent and Innovation Trends in Computing and Communication, vol. 11, no. 10, pp. 854–861, 2023, doi: 10.17762/ijritcc.v11i10.8602.

[15] F. Z. Mehrjardi, A. M. Latif, M. S. Zarchi, and R. Sheikhpour, “A survey on deep learning-based image forgery detection,” Pattern Recognition, vol. 144, art. 109778, 2023, doi: 10.1016/j.patcog.2023.109778.

[16] M. A. Anwar, S. F. Tahir, L. G. Fahad, and K. Kifayat, “Image forgery detection by transforming local descriptors into deep-derived features,” Applied Soft Computing, vol. 147, art. 110730, 2023, doi: 10.1016/j.asoc.2023.110730.

[17] M. Zanardelli, F. Guerrini, R. Leonardi, and N. Adami, “Image Forgery Detection: A Survey of Recent Deep-Learning Approaches,” Multimedia Tools and Applications, vol. 82, pp. 17521–17566, 2023, doi: 10.1007/s11042-022-13797-w.

[18] K. D. Kadam, S. Ahirrao, and K. Kotecha, “Multiple Image Splicing Dataset (MISD): A Dataset for Multiple Splicing,” Data, vol. 6, no. 10, art. 102, 2021, doi: 10.3390/data6100102.

[19] M. Barni et al., “Aligned and non-aligned double JPEG detection using convolutional neural networks,” Journal of Visual Communication and Image Representation, vol. 49, pp. 153–163, Nov. 2017, doi: 10.1016/j.jvcir.2017.09.003.

[20] Q. Wang, and R. Zhang, “Double JPEG compression forensics based on a convolutional neural network,” EURASIP Journal on Information Security, vol. 2016, no. 1, art. 23, 2016, doi: 10.1186/s13635-016-0047-y.

[21] I. Amerini, T. Uricchio, L. Ballan, and R. Caldelli, “Localization of JPEG double compression through multi-domain convolutional neural networks,” in Proc. 2017 IEEE Conf. Computer Vision and Pattern Recognition Workshops (CVPRW), Honolulu, HI, USA, Jul. 2017, pp. 1865–1871.

[22] C. Pasquini, I. Amerini, and G. Boato, “Media forensics on social media platforms: a survey,” EURASIP Journal on Information Security, vol. 2021, no. 1, 2021, doi: 10.1186/s13635-021-00117-2.

[23] X. Qing, “A Comparison Study of Convolutional Neural Network and Recurrent Neural Network on Image Classification,” in Proc. 2022 10th Int. Conf. Information Technology: IoT and Smart City (ICIT 2022), Shanghai, China, Dec. 2022, doi: 10.1145/3582197.3582215.

[24] N. V. Gawali, K. Pagare, S. Daundkar, and D. Wagh, “Image Classification Using Convolutional Neural Networks,” International Journal for Research in Applied Science and Engineering Technology, vol. 11, no. 6, 2023, doi: 10.22214/ijraset.2023.52435.

[25] L. Wang, and Y. Sun, “Image classification using convolutional neural network with wavelet domain inputs,” IET Image Processing, vol. 16, no. 8, pp. 2037–2048, 2022, doi: 10.1049/ipr2.12466.

[26] W. Rawat, and Z. Wang, “Deep Convolutional Neural Networks for Image Classification: A Comprehensive Review,” Neural Computation, vol. 29, no. 9, pp. 2352–2449, 2017, doi: 10.1162/neco_a_00990.

[27] X. Zhao, L. Wang, Y. Zhang, X. Han, M. Deveci, and M. Parmar, “A review of convolutional neural networks in computer vision,” Artificial Intelligence Review, vol. 57, no. 4, art. 99, 2024, doi: 10.1007/s10462-024-10721-6.

[28] H. Hartatik, and M. K. Anam, “Comparison of Convolutional Neural Network Architecture on Detection of Helmet Use by Humans,” ELINVO (Electronics, Informatics, and Vocational Education), vol. 8, no. 1, pp. 44–54, 2023, doi: 10.21831/elinvo.v8i1.52104.

[29] Y.-Y. Bae, D.-J. Cho, and K.-H. Jung, “Enhancing Document Forgery Detection with Edge-Focused Deep Learning,” Symmetry, vol. 17, no. 8, art. 1208, 2025, doi: 10.3390/sym17081208.

[30] I. T. Ahmed, F. A. Abdulazeez, and B. T. Hammad, “Employing Different Algorithms of Lightweight Convolutional Neural Network Models in Image Distortion Classification,” Computers, vol. 13, no. 10, art. 268, 2024, doi: 10.3390/computers13100268.

[31] M. A. Khan, “Comparative Analysis of Resource-Efficient CNN Architectures for Brain Tumor Classification,” arXiv:2411.15596, 2024, doi: 10.48550/arXiv.2411.15596.

[32] K. M. Sujon, R. Hassan, K. Choi, and M. A. Samad, “Accuracy, precision, recall, f1-score, or MCC? Empirical evidence from advanced statistics, ML, and XAI for evaluating business predictive models,” Journal of Big Data, vol. 12, art. 268, 2025, doi: 10.1186/s40537-025-01313-4.

[33] A. Tasnim, M. Saiduzzaman, M. A. Rahman, J. Akhter, and A. S. M. M. Rahaman, “Performance Evaluation of Multiple Classifiers for Predicting Fake News,” Journal of Computer and Communications, vol. 10, pp. 1–21, 2022, doi: 10.4236/jcc.2022.109001.

[34] M. C. Hinojosa-Lee, J. Braet, and J. Springael, “Performance Metrics for Multilabel Emotion Classification: Comparing Micro, Macro, and Weighted F1-Scores,” Applied Sciences, vol. 14, no. 21, art. 9863, 2024, doi: 10.3390/app14219863.

[35] A. A. Abdirahman, A. O. Hashi, U. M. Dahir, M. A. Elmi, and O. E. R. Rodriguez, “Enhancing Security in Mobile Wallet Payments: Machine Learning-Based Fraud Detection Across Prominent Wallet Platforms,” International Journal of Electronics and Communication Engineering, vol. 11, no. 3, pp. 96–105, 2024, doi: 10.14445/23488549/IJECE-V11I3P110.

[36] A. M. Bhunje, R. Ghorpade, O. Dhumal, S. Chavan, and A. Khalate, “TrustBill AI: An Intelligent GST Invoice Fraud Detection and Verification System Using OCR, Machine Learning, and Deep Learning,” International Journal of Engineering Research & Technology, vol. 15, no. 5, pp. 1–15, May 2026, doi: 10.5281/zenodo.20445360.

[37] H. Arslan, “End to End Invoice Processing Application Based on Key Fields Extraction,” IEEE Access, vol. 10, pp. 78398–78413, 2022, doi: 10.1109/ACCESS.2022.3192828.

[38] A. Amari et al., “An Efficient Deep Learning-Based Approach to Automating Invoice Document Validation,” in Proc. 2024 IEEE/ACS 21st Int. Conf. Computer Systems and Applications (AICCSA), 2024, pp. 1–8, doi: 10.1109/AICCSA63423.2024.10912544.

[39] R. Raoui-Outach, C. Million-Rousseau, A. Benoit, and P. Lambert, “Deep Learning for Automatic Sale Receipt Understanding,” in Proc. 2017 Int. Conf. Image Processing Theory, Tools and Applications (IPTA), Montreal, QC, Canada, 2017, pp. 1–6, doi: 10.1109/IPTA.2017.8310088.

[40] A. Naveh, and E. Tromer, “PhotoProof: Cryptographic Image Authentication for Any Set of Permissible Transformations,” in Proc. 2016 IEEE Symposium on Security and Privacy (SP), San Jose, CA, USA, 2016, pp. 255–271, doi: 10.1109/SP.2016.23.

[41] E. Casey, Digital Evidence and Computer Crime: Forensic Science, Computers, and the Internet, 3rd ed. Waltham, MA, USA: Academic Press, 2011.

[42] H. Farid, “Image Forgery Detection,” IEEE Signal Processing Magazine, vol. 26, no. 2, pp. 16–25, Mar. 2009, doi: 10.1109/MSP.2008.931079.

[43] D. H. Hubel, and T. N. Wiesel, “Receptive fields, binocular interaction and functional architecture in the cat’s visual cortex,” The Journal of Physiology, vol. 160, no. 1, pp. 106–154, Jan. 1962, doi: 10.1113/jphysiol.1962.sp006837.

[44] K. Fukushima, “Neocognitron: A Self-Organizing Neural Network Model for a Mechanism of Pattern Recognition Unaffected by Shift in Position,” Biological Cybernetics, vol. 36, no. 4, pp. 193–202, Apr. 1980, doi: 10.1007/BF00344251.

[45] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner, “Gradient-Based Learning Applied to Document Recognition,” Proceedings of the IEEE, vol. 86, no. 11, pp. 2278–2324, Nov. 1998, doi: 10.1109/5.726791.

[46] Republic Act No. 10173, “An Act Protecting Individual Personal Information in Information and Communications Systems in the Government and the Private Sector, Creating for this Purpose a National Privacy Commission, and for Other Purposes (Data Privacy Act of 2012),” Congress of the Philippines, Manila, Philippines, Aug. 15, 2012.

[47] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei, “ImageNet: A Large-Scale Hierarchical Image Database,” in Proc. 2009 IEEE Conf. Computer Vision and Pattern Recognition (CVPR), Miami, FL, USA, 2009, pp. 248–255, doi: 10.1109/CVPR.2009.5206848.

[48] D. P. Kingma, and J. Ba, “Adam: A Method for Stochastic Optimization,” in Proc. 3rd Int. Conf. Learning Representations (ICLR), San Diego, CA, USA, 2015, arXiv:1412.6980.


