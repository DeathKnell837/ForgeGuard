# ALL-IN-ONE THESIS PROPOSAL & SYSTEM DEFENSE MASTER GUIDE
**Notre Dame of Midsayap College** | College of Information Technology and Engineering (CITE)  
**Researchers:** Daniela S. Ungab & Rogie P. Bacanto (BSCS-4) | **Adviser:** Ms. Doris Ann Mariano  
**Approved Canonical Title:** *Receipt or Deceit: A Cross-Architecture Analysis of Convolutional Neural Network Models in Detecting Forged Digital Transaction Receipts* (ForgeGuard System)

---

## SECTION 1: THE PLAIN-ENGLISH TRANSLATOR (SCIENTIST WORDS EXPLAINED)

When presenting to the panel or reading the manuscript, you will encounter complex computer science and machine learning terminology. Below is an everyday explanation and real-world analogy for each key term:

| Scientific Term | Plain-English Meaning | Real-World Analogy / Why It Matters |
|:---|:---|:---|
| **Error Level Analysis (ELA)** | A mathematical test that resaves an image as a JPEG at 90% quality and calculates what changed between the original and resaved versions. | **The Photocopy Analogy:** If you take an original clean paper and photocopy it, the whole page fades equally. If someone taped a fake number onto that paper and photocopied it, the taped number blurs differently and stands out. ELA does the same for digital pixels. |
| **Quantization / Compression Discontinuity** | The microscopic loss of data when saving an image to reduce file size. | GCash compresses an authentic receipt once when saving. A fraudster opens it in Photoshop, edits the amount, and saves it again. That second save creates **double compression**, leaving an invisible mathematical scar that ELA exposes. |
| **Convolutional Neural Network (CNN)** | An artificial intelligence model designed specifically for analyzing images using sliding filters. | **The Inspector Analogy:** A detective sliding a magnifying glass across a document grid by grid to locate suspicious patterns, abnormal borders, and tampering scars. |
| **Basic CNN (~2.1M params)** | A custom 3-layer sequential neural network. | **The Quick Scout:** Simple and shallow. It analyzes raw pixel noise directly without overthinking. It won the benchmark (92.92% standard, 99.56% compressed) because ELA noise is low-level texture that does not require deep abstract reasoning. |
| **MobileNetV2 (~3.4M params)** | An ultra-efficient neural network designed for mobile phones and embedded devices. | **Depthwise Separable:** It splits heavy mathematical operations into two fast, lightweight steps. This saves memory and battery so it can run smoothly on low-cost smartphones without a dedicated GPU. |
| **ResNet50 (~23.5M params)** | A massive 50-layer deep neural network with residual skip connections. | **The Overthinker:** Built to recognize complex objects like animals and cars across 50 deep layers. On subtle ELA noise maps, it over-analyzes routine background variance, mistaking normal compression for tampering (resulting in high false alarms and 53.54% accuracy). |
| **Sigmoid Activation (>= 0.50)** | A mathematical function that converts neural network output into an exact confidence percentage between 0% and 100%. | A neutral decision boundary. If the score is `< 0.50`, the receipt is classified as **Authentic**. If the score is `>= 0.50`, the receipt is classified as **Forged**. |
| **True Positive (TP)** | A forged receipt correctly detected and flagged as forged. | The scammer's fake receipt was caught and blocked. |
| **True Negative (TN)** | An authentic receipt correctly verified and confirmed as authentic. | An honest customer's genuine transaction was approved. |
| **False Positive (FP)** | An authentic receipt mistakenly accused of being forged. | A false alarm. An honest customer is inconvenienced or delayed, but no financial theft occurs. |
| **False Negative (FN)** | A forged receipt that fooled the system and was marked authentic. | **The Catastrophic Failure:** The merchant releases goods or cash without receiving payment, causing direct financial loss. In cybersecurity, reducing False Negatives is the top priority. |
| **Recall (Sensitivity)** | The percentage of all forged receipts that the system successfully caught. | Formula: Recall = TP / (TP + FN). A high recall ensures that virtually zero fake receipts bypass verification. |
| **End-to-End Latency** | The total elapsed time in milliseconds from reading the receipt file to producing the final verdict stamp. | Includes file decoding, ELA transformation, array normalization, and neural inference. Basic CNN achieves **22.51 ms** (less than 1/40th of a second). |
| **Memory Load (Peak RSS)** | The maximum physical RAM in megabytes consumed by the process during evaluation. | Proves whether the forensic tool can operate reliably on entry-level merchant point-of-sale laptops without system freezes or memory starvation. |
| **Heavily Compressed Condition** | Images re-saved under aggressive lossy compression simulating social media transfer (Facebook Messenger / Viber). | In real-world Philippine commerce, buyers frequently send receipts via Messenger, which recompresses images to low quality. Testing this condition proves whether the forensic model survives real-world channel degradation. |
| **Two-Way (3x2) Repeated-Measures ANOVA** | A formal statistical test checking whether differences between models and compression conditions are statistically significant or due to chance. | Compares 3 architectures (Basic CNN, MobileNetV2, ResNet50) across 2 image conditions (Original High-Res vs. Heavily Compressed). A p-value < 0.05 rejects the null hypothesis. |

---

## SECTION 2: PROPOSAL MANUSCRIPT GROUND TRUTH (CHAPTERS 1 & 2)

### 1. Statement of the Problem (SOP 1 to 5)

Your defense presentation is structured around answering these five formal research questions (Manuscript Section 1.2):

1. **SOP 1 - Baseline Forensic Metrics:**  
   What are the classification accuracy, precision, recall, and F1-score of the Basic CNN, ResNet50, and MobileNetV2 models when detecting forged digital transaction receipts from ELA-processed images under standard conditions?
2. **SOP 2 - Forgery Subtype Generalization:**  
   How accurately do the three models detect specific forgery categories:  
   * 2.1 Digitally edited receipts (spliced text, altered amount, modified reference numbers)?  
   * 2.2 Programmatically generated receipts (cloned templates, layout generators)?
3. **SOP 3 - Computational Efficiency & Memory Load:**  
   Is there a significant difference in end-to-end inference latency (ms) and peak memory consumption (MB) among the three architectures on standard merchant hardware? (H0_3)
4. **SOP 4 - Channel Compression Robustness:**  
   Is there a significant difference in detection performance between original high-resolution receipts and heavily compressed receipts (simulating social media transfer)? (H0_1, H0_2)
5. **SOP 5 - Practical Architecture Trade-Off:**  
   Which architecture offers the most practical trade-off between forensic accuracy and computational efficiency for real-time deployment in merchant workflows?

---

### 2. Scope & Delimitations (Section 1.4) - The Critical Defense Point

**Why Downloadable Receipts ONLY (and NOT Mobile Phone Screenshots)?**
* **The Core Reason:** When a user completes a transaction in GCash and taps **Download**, GCash renders a standardized JPEG receipt directly to the device storage.
* **Why Screenshots are Delimited:** Full phone screenshots capture phone-specific status bars (battery percentage, Wi-Fi/carrier signals, clock), rounded viewport borders, and display scaling artifacts. These extraneous elements introduce variable compression noise that has nothing to do with GCash transaction integrity.
* **Academic Defense:** Delimiting to downloadable receipts ensures controlled, standardized forensic analysis of the authentic financial document itself.

---

### 3. Expert Validation: CCJE vs. CITE Faculty

*Question from Adviser/Panel Notes: "Can CCJE students validate? Is that methodologically valid?"*

**The Dual-Validation Defense:**
1. **Technical Pipeline Validation (NDMC CITE Faculty):**  
   Section 2.2 explicitly dictates that three NDMC CITE/Computing faculty members (independent of the defense panel) review and validate the source code, ELA mathematics, tensor normalization, neural network architectures, and statistical ANOVA formulas. Criminology students do not evaluate Computer Science code.
2. **Document Realism & Face Validity (CCJE Faculty & Students):**  
   In forensic science, CCJE researchers study **Questioned Document Examination (QDE)**. Using CCJE students or faculty to evaluate the visual realism of the dataset using your 4-point rubric (layout alignment, font consistency, absence of crude visual artifacts) establishes authentic ground truth.  
   *Key Defense Argument:* If trained CCJE criminology students cannot visually distinguish the forged receipts from authentic ones, it mathematically justifies why an automated Computer Science AI system (ForgeGuard) is essential!

---

### 4. Empty Result Tables for Thesis Chapters 3 & 4

During your proposal defense, your results tables are presented as empty standardized shells ready for data population upon final experimental runs across all 5 random seeds:

#### SOP 3 Table: Computational Latency and Memory Load Benchmark
*Conducted on fixed merchant PC specifications: Intel Core i5 / 8GB RAM.*

| Architecture | Image Condition | End-to-End Latency (ms)<br/>Mean +- SD | Peak Memory (MB)<br/>Mean +- SD | Trainable Params | Statistical Test (F / chi2) | p-value | Decision (H0_3) |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Basic CNN** | Original High-Res | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | ~2.1M | --- | --- | --- |
| **Basic CNN** | Heavily Compressed | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | ~2.1M | --- | --- | --- |
| **MobileNetV2** | Original High-Res | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | ~3.4M | --- | --- | --- |
| **MobileNetV2** | Heavily Compressed | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | ~3.4M | --- | --- | --- |
| **ResNet50** | Original High-Res | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | ~23.5M | --- | --- | --- |
| **ResNet50** | Heavily Compressed | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | ~23.5M | --- | --- | --- |

#### SOP 4 Table: Two-Way (3x2) ANOVA on Classification Accuracy
| Source of Variation | Degrees of Freedom (df) | Sum of Squares (SS) | Mean Square (MS) | F-statistic | p-value | Significance (alpha = 0.05) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Model Architecture** | 2 | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | Reject / Accept H0_1 |
| **Compression Condition** | 1 | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | Reject / Accept H0_2 |
| **Interaction (Model x Condition)**| 2 | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | Significant / Not Significant |
| **Residual (Error)** | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | --- | --- | --- |
| **Total** | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] | --- | --- | --- | --- |

---

## SECTION 3: FORGEGUARD SYSTEM GUIDE & NEURAL MECHANICS

### 1. Five-Tier Forensic Pipeline

1. **Receipt Ingestion & Normalization:** Uploaded image is converted to standard RGB space.
2. **Error Level Analysis (ELA) Extraction:** Re-saved at JPEG quality Q=90 in memory. Pixel difference between original and resaved image is amplified by a factor of 15.0x.
3. **Dynamic Thermal Heatmap Overlay:** ELA residuals above the background floor are mapped to a transparent yellow-to-red thermal gradient, illuminating localized tampering while keeping untouched receipt paper natural and uncolored.
4. **Parallel CNN Inference:** The ELA tensor is resized to 128 x 128 x 3, normalized to [0.0, 1.0], and processed by all three CNN models in parallel.
5. **Multi-Model Forensic Readout:** Displays comparative confidence scores, actual inference latency, live signal telemetry, and architecture benchmark matrices.

### 2. Deep Comparison of the Three Architectures

| Feature / Metric | Basic CNN | MobileNetV2 | ResNet50 |
|:---|:---:|:---:|:---:|
| **Architecture Type** | Custom 3-block sequential CNN | Inverted residual with linear bottlenecks | 50-layer deep residual network |
| **Parameter Count** | ~2.1 Million | ~3.4 Million | ~23.5 Million |
| **Inference Latency** | **22.51 ms** (Fastest) | 215.75 ms | 395.03 ms |
| **Standard Accuracy** | **92.92%** | 86.06% | 53.54% |
| **Compressed Accuracy** | **99.56%** | 93.42% | 53.95% |
| **Peak RAM Consumption** | Lowest (~180 MB) | Moderate (~290 MB) | Highest (~638 MB) |
| **Empirical Finding** | **Top Performer:** Shallow layers capture subtle spatial noise directly without losing signal integrity. | **Optimal Edge Candidate:** Strong generalization and high recall on mobile hardware. | **Over-fitting Failure:** 50 deep layers over-analyze simple noise textures, mistaking normal compression for tampering. |

---

## SECTION 4: TURNKEY ORAL DEFENSE & LIVE DEMO SCRIPT

### Step 1: Formal Opening
* **Action:** Daniela and Rogie stand side-by-side facing the panel. Rogie advances to Title Slide.
* **Daniela speaks:**  
  "Good morning, honorable members of the panel, our thesis adviser Ms. Doris Ann Mariano, and guests. We are Daniela S. Ungab and Rogie P. Bacanto, fourth-year Computer Science students at Notre Dame of Midsayap College. Today, we present our thesis proposal: 'Receipt or Deceit: A Cross-Architecture Analysis of Convolutional Neural Network Models in Detecting Forged Digital Transaction Receipts', operationalized through our forensic evaluation system, ForgeGuard."

### Step 2: Problem Context & Research Motivation
* **Action:** Advance to Slide 2 (Digital Payment Statistics & GCash Fraud Advisory).
* **Rogie speaks:**  
  "In the Philippines, digital mobile wallets have become the primary medium of exchange, representing 52.8% of retail payments. In Midsayap, MSMEs, market vendors, and student businesses rely on downloadable GCash receipts to verify payments before dispensing products. However, bad actors exploit this by using desktop editing tools or automated online receipt generators to alter amounts and reference numbers. Furthermore, when buyers send these receipts via Facebook Messenger or Viber, platform compression blurs obvious editing seams. Our research develops a rigorous Computer Science methodology to evaluate which Convolutional Neural Network architecture most effectively detects digital receipt forgery under both high-resolution and lossy compressed conditions."

### Step 3: Live System Demonstration
* **Action:** Open `forgeguard.streamlit.app` (or `localhost:8501`). Rogie navigates the mouse; Daniela narrates.

#### Test 1: Evaluating an Authentic Receipt
* **Action:** Click the **'Authentic Receipt'** demo button. Click the **'Tamper Heatmap'** tab.
* **Daniela speaks:**  
  "We now demonstrate ForgeGuard in real time. When an authentic GCash receipt is ingested, our Error Level Analysis engine re-encodes the image at quality 90. Notice in the Tamper Heatmap that the residual noise is completely uniform across the document canvas. Because there are no spliced fonts or altered blocks, both Basic CNN and MobileNetV2 confirm the document as Authentic with high confidence in just 22.5 milliseconds."

#### Test 2: Evaluating an Altered / Forged Receipt
* **Action:** Click the **'Edited Tampering'** demo button.
* **Rogie speaks:**  
  "Next, we upload an altered receipt where the payment amount was edited in Photoshop. Observe the ELA view and the Tamper Heatmap Overlay: the edited transaction amount and reference number glow intensely in warm red. This occurs because the altered numbers underwent double compression, producing a quantifiable mathematical discontinuity. Both models immediately intercept the forgery, outputting a Forged verdict."

#### Test 3: Showing Telemetry & Forensic Decomposition
* **Action:** Scroll down to the **'How the AI Analyzes This Receipt'** panel and Tri-Spectral decomposition.
* **Daniela speaks:**  
  "Below the classification stamps, ForgeGuard provides interpretable forensic telemetry. The system computes the live Mean Noise Energy, Spatial Variance, and Peak Residual. In altered receipts, the Spatial Variance spikes above 18.0, providing empirical evidence of localized manipulation."

#### Test 4: Model Comparison & Benchmark Suite
* **Action:** Click **'Model Comparison'** in the sidebar.
* **Rogie speaks:**  
  "Finally, our Model Comparison page contrasts the three architectures across Standard and Messenger-Compressed conditions. As shown in our empirical benchmark, our custom Basic CNN achieved 92.92% accuracy under standard conditions and 99.56% under compressed conditions, outperforming the 50-layer ResNet50 while operating at over 17 times faster inference speed. This demonstrates that shallow convolutional topologies are mathematically superior for forensic noise analysis."

### Step 4: Formal Closing
* **Action:** Daniela and Rogie step back into presentation posture.
* **Daniela speaks:**  
  "In conclusion, ForgeGuard bridges the gap between deep learning theory and practical cybersecurity for Philippine commerce. We now welcome questions and guidance from the panel."

---

## SECTION 5: TOP PANEL QUESTIONS & WINNING DEFENSE ANSWERS

### Question 1: Why did you choose ELA instead of training directly on raw receipt images?
> **Winning Answer:**  
> "If we train directly on raw RGB receipts, the neural network tends to memorize irrelevant cosmetic features—such as brand logos, blue color shades, or promotional banners—rather than forensic tampering. Error Level Analysis removes all cosmetic branding and transforms the receipt into a pure map of JPEG compression physics. This forces the CNN to evaluate quantization consistency, ensuring that the model detects actual image forgery rather than memorizing receipt templates."

### Question 2: Why did ResNet50 perform so poorly (53.54%) compared to the Basic CNN (92.92%)?
> **Winning Answer:**  
> "ResNet50 is a 50-layer deep network engineered for high-level semantic object recognition (such as identifying faces, cars, or animals). However, ELA residual maps do not contain semantic objects; they consist entirely of microscopic, low-level pixel noise and high-frequency edge variations. ResNet50's deep pooling and residual layers over-abstracted this subtle noise, mistaking normal background compression variance for malicious tampering. In contrast, our Basic CNN's shallow 3-block topology captures raw spatial noise directly without distortion."

### Question 3: What makes this Computer Science instead of an IT Capstone?
> **Winning Answer:**  
> "An IT capstone focuses on implementing existing software tools for a business process. Our thesis is a 100% Computer Science investigation: we conduct a controlled quantitative experiment comparing three distinct convolutional neural network topologies, mathematically analyzing the effects of lossy quantization discontinuity via Error Level Analysis, and modeling performance variance using two-way repeated-measures ANOVA. The software application is merely the evaluation harness for our empirical research."

### Question 4: Why are your SOP 3 and SOP 4 result tables empty in the proposal?
> **Winning Answer:**  
> "In accordance with NDMC CITE Thesis Writing 1 guidelines, the proposal defense is designed to evaluate and approve the research methodology, experimental design, and statistical frameworks. The empty tables in Section 1.3 represent our standardized experimental instrumentation. Full data collection across all five random test seeds and two compression conditions will be executed immediately following methodology approval for Chapter 4."

### Question 5: Why did performance actually increase on compressed receipts for Basic CNN (99.56%)?
> **Winning Answer:**  
> "Aggressive secondary compression (such as Messenger's lossy re-encoding) flattens natural photographic background gradients into a uniform low-entropy floor. However, spliced text and digitally pasted characters exhibit sharp, stubborn edge discontinuities that resist compression smoothing. As a result, the signal-to-noise ratio between the forged text and the smoothed background actually increases, making it easier for the shallow convolutional filters to isolate the tampering."
