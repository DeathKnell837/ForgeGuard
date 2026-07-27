# BSCS Thesis Writing 1 - Customization Rules

This workspace customizations file provides context and instructions to the Antigravity coding assistant to ensure continuity of work on the BSCS Thesis for Notre Dame of Midsayap College (NDMC).

---

## 1. Project Context & Profiles

### Group Members
* **Rogie P. Bacanto** (BSCS-4)
* **Daniela S. Ungab** (BSCS-4)
* **School:** Notre Dame of Midsayap College (NDMC), College of Information Technology and Engineering (CITE)
* **Adviser:** Ms. Doris Ann Mariano
* **Current Subject:** CS Thesis Writing 1 (Enrolled, June 2026)

### Timeline & Milestones
* **Current Date:** July 26, 2026
* **Current Stage:** **Week 5+ — Proposal Writing & System Implementation (Chapters 1 & 2)**
* **Title Defense Status:** **PASSED / COMPLETED (July 2026)**
* **Approved Title:** *Securing Mobile Transaction: A Comparative Evaluation of CNN Architectures in Detecting Digital Receipt Forgery* (ForgeGuard System)

---

## 2. Mandatory Rules for Antigravity

> [!IMPORTANT]
> **Rule 1: Reference Integrity & Verification**
> Every reference added to this project MUST be verified by actually visiting the URL/DOI. Never hallucinate academic papers or links. Ensure no 404 errors. Check and verify each link.

> [!IMPORTANT]
> **Rule 2: Paper Specifications**
> * **Paper Size:** A4
> * **Margins:** Left 1.50 in, Right 1.0 in, Top 1.20 in, Bottom 1.0 in
> * **Spacing:** 3 single spaces between Chapter Title $\rightarrow$ Section Title $\rightarrow$ Body Text. Double-spaced body text.
> * **Background of the Study (1.1):** Must be exactly 2-3 pages long.
> * **Citation Style:** IEEE format (numeric citations, e.g., [1], [2]).
> * **Tenses:** Past tense for specific research findings (e.g., *"...tested the system [1]"*), present tense for general concepts (e.g., *"...argues that [2]"*).

> [!WARNING]
> **Rule 3: Exclude IT/IS Guidelines & OJT Domain**
> * Do NOT use any guidelines, formats, or agendas meant for BSIT, BSIS, or Engineering programs.
> * Do NOT recommend or use any topics related to Rogie's OJT at CENRO DENR. Focus strictly on core BSCS topics.

> [!IMPORTANT]
> **Rule 4: Algorithm-Focused Titles for 100% CS Alignment**
> All thesis titles must contain the specific algorithms or mathematical models directly in the text (e.g., *Explainable Transfer Learning*, *Hybrid Neural Networks*, *Multi-Engine Neural Networks*, *Steganography*, *Genetic Algorithms*). This ensures that the topic is classified as **100% Computer Science** rather than Information Technology (IT) capstones. Avoid generic prefixes like "Automated System" or "Monitoring".

> [!CRITICAL]
> **Rule 5: Single Workspace (`c:\Users\USER\Desktop\THESIS`) with Dual Remotes**
> The single local workspace is `c:\Users\USER\Desktop\THESIS`. Never create separate clones on Desktop.
>
> | Remote Name | Target Repository | Purpose |
> |:------------|:------------------|:--------|
> | `origin` | `DeathKnell837/NDMC-BSCS-THESIS-PREP` | Primary thesis workspace repository (`thesis-docs/`, `thesis-system/`, `README.md`) |
> | `forgeguard` | `DeathKnell837/ForgeGuard` | Live Streamlit Cloud deployment target (`forgeguard.streamlit.app`) |
>
> **MANDATORY RULES:**
> * All work is conducted inside `c:\Users\USER\Desktop\THESIS`.
> * Thesis documentation and writing stay inside `thesis-docs/`.
> * System implementation, dataset, models, and webapp stay inside `thesis-system/` and `webapp/`.
> * Push to `origin` for thesis prep sync; push to `forgeguard` when deploying webapp changes to Streamlit Cloud.

> [!IMPORTANT]
> **Rule 6: Approved Title is Final**
> The title defense is **PASSED**. The single approved title is:
> *"Securing Mobile Transaction: A Comparative Evaluation of CNN Architectures in Detecting Digital Receipt Forgery"*
> (ForgeGuard System). Do NOT reference or propose the 3 old pre-defense candidate titles (Concrete Crack, Phishing URL, Deepfake Detection) in any new documents. They may remain in archival files only.

---

## 3. Approved Thesis Title

* **Title:** *Securing Mobile Transaction: A Comparative Evaluation of CNN Architectures in Detecting Digital Receipt Forgery*
* **System Name:** ForgeGuard
* **Domain:** Image Forensics / Cybersecurity & Mobile Payment Security
* **Scope:** Upload GCash/Maya mobile wallet receipt screenshots → compute Error Level Analysis (ELA) → classify as authentic or forged using three CNN architectures (Basic CNN, ResNet50, MobileNetV2) → display comparative confidence scores, latency, and forensic heatmaps.
* **Live Demo:** [forgeguard.streamlit.app](https://forgeguard.streamlit.app/)

---

## 4. Key Project Files
Refer to these files in the workspace for details:
* [student_info.md](file:///c:/Users/USER/Desktop/THESIS/thesis-docs/student_info.md) — Student profile and schedule
* [bscs_thesis_guidelines.md](file:///c:/Users/USER/Desktop/THESIS/thesis-docs/bscs_thesis_guidelines.md) — Formatted BSCS thesis outline and formatting rules
* [implementation_plan.md](file:///c:/Users/USER/Desktop/THESIS/thesis-docs/implementation_plan.md) — Complete 10-phase thesis preparation plan
* [summary_for_daniela.md](file:///c:/Users/USER/Desktop/THESIS/thesis-docs/summary_for_daniela.md) — Summary sheet for Daniela's review
* [README.md](file:///c:/Users/USER/Desktop/THESIS/README.md) — Central project status and links hub

