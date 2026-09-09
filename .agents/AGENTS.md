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
> **Rule 5: Dual Remotes & Repository Boundary Non-Interference Policy**
> The single local workspace is `c:\Users\USER\Desktop\THESIS`. Never create separate clones on Desktop.
>
> | Remote Name | Target Repository | Purpose & Content Scope | Root README Identity |
> |:------------|:------------------|:------------------------|:---------------------|
> | `origin` | `DeathKnell837/NDMC-BSCS-THESIS-PREP` | **Primary Thesis Research Workspace.** Houses all proposal manuscripts (`THESIS1UNGAB_BACANTO.docx`/`.md`), guidelines, literature reviews, defense slides, research outlines, and full codebase backup. | **Master Academic Thesis Workspace Hub** (`README.md` at root on `main`) |
> | `forgeguard` | `DeathKnell837/ForgeGuard` | **Software System & Deployment Repository.** Dedicated host for Streamlit Cloud deployment (`forgeguard.streamlit.app`), Python runtime, models, dataset, ELA engine, and webapp. | **ForgeGuard Software Engineering Guide** (`thesis-system/README.md`) |
>
> **MANDATORY PUSH & SYNCHRONIZATION RULES (NO INTERFERENCE):**
> * **Thesis Documentation & Academic Writing:** All thesis documentation, manuscripts, and writing stay inside `thesis-docs/`. Commit on `main` and push to `origin`.
> * **System Implementation & Webapp:** System implementation, dataset, models, and webapp stay inside `thesis-system/` and `webapp/`.
> * **Pushing without README Interference:**
>   - When pushing thesis prep changes: Push to `origin main`. The root `README.md` in `origin` must ALWAYS be the Academic Thesis Workspace Hub.
>   - When deploying to Streamlit Cloud: Run `.\deploy-forgeguard.ps1` (or temporarily set root `README.md` to `thesis-system/README.md` for the `forgeguard` push, then restore the academic README for `origin`).
>   - NEVER push the software system README directly to `origin/main` root.

> [!IMPORTANT]
> **Rule 6: Approved Title is Final**
> The title defense is **PASSED**. The single approved title is:
> *"Securing Mobile Transaction: A Comparative Evaluation of CNN Architectures in Detecting Digital Receipt Forgery"*
> (ForgeGuard System). Do NOT reference or propose the 3 old pre-defense candidate titles (Concrete Crack, Phishing URL, Deepfake Detection) in any new documents. They may remain in archival files only.

> [!CRITICAL]
> **Rule 7: Strict Zero-Emoji Policy (Professional Enterprise UI & Academic Standards)**
> * **NEVER** use emojis anywhere in the UI, labels, buttons, navigation, headers, tables, charts, or documentation.
> * Always use **clean pure typography** or **custom SVG vector line icons** (Lucide / Feather style SVG masks) for all visual UI elements.
> * Maintain a formal, high-tech, enterprise cybersecurity and image forensics aesthetic matching Sophos / Behance standards.

> [!CRITICAL]
> **Rule 8: UI-Only Polish & Anti-Complexity Policy (No Scope Creep / No Feature Inventions)**
> * **NEVER** add new features, extra buttons, artificial logic, marketing text, or unapproved features to the system.
> * When asked to improve the UI or design, focus **strictly on CSS visual refinement** (alignment, centering, spacing, surface contrast, clean typography, responsive layout).
> * Keep all UI text, labels, and operational flows strictly identical to the approved thesis scope so that the system remains simple, robust, and directly defensible without adding unnecessary complexity to the thesis defense.

> [!CRITICAL]
> **Rule 9: Canonical Manuscript Ground Truth (`THESIS1UNGAB_BACANTO`)**
> * The **ONLY** authoritative, living source of truth for all thesis methodology, research questions, scope, dataset specifications, experimental design, and citations is the newest proposal manuscript:
>   - [`thesis-docs/THESIS1UNGAB_BACANTO.docx`](file:///c:/Users/USER/Desktop/THESIS/thesis-docs/THESIS1UNGAB_BACANTO.docx) / [`thesis-docs/THESIS1UNGAB_BACANTO.md`](file:///c:/Users/USER/Desktop/THESIS/thesis-docs/THESIS1UNGAB_BACANTO.md).
> * **NEVER** consult, extract requirements from, or treat old standalone draft documents (such as `Chapter1_Digital_Deception_Mobile_Wallet.*`, `Chapter2_Review_of_Related_Literature.*`, or older candidate/scratch files) as reference material.
> * If any contradiction arises between `THESIS1UNGAB_BACANTO` and any other document in this workspace, `THESIS1UNGAB_BACANTO` **ALWAYS** takes absolute precedence.

> [!CRITICAL]
> **Rule 10: Strict Explicit Consent Policy (No Autonomous File Edits)**
> * **NEVER** edit, modify, replace, create, delete, or push any code, configuration, models, or documents unless the user has **EXPLICITLY** commanded and confirmed the action.
> * Presenting proposals, options, or asking questions does NOT grant permission to execute.
> * Before making ANY file modification, the assistant MUST outline the exact proposed changes in chat and wait for explicit confirmation from the user.
> * Jumping the gun, making premature assumptions, or applying unauthorized edits is strictly prohibited under all circumstances.

---

## 3. Approved Thesis Title

* **Title:** *Securing Mobile Transaction: A Comparative Evaluation of CNN Architectures in Detecting Digital Receipt Forgery*
* **System Name:** ForgeGuard
* **Domain:** Image Forensics / Cybersecurity & Mobile Payment Security
* **Scope:** Upload GCash mobile wallet receipt screenshots → compute Error Level Analysis (ELA) → classify as authentic or forged using three CNN architectures (Basic CNN, ResNet50, MobileNetV2) → display comparative confidence scores, latency, and forensic heatmaps.
* **Live Demo:** [forgeguard.streamlit.app](https://forgeguard.streamlit.app/)

---

## 4. Key Project Files
Refer to these files in the workspace for details:
* [THESIS1UNGAB_BACANTO.md](file:///c:/Users/USER/Desktop/THESIS/thesis-docs/THESIS1UNGAB_BACANTO.md) — **Canonical Thesis Proposal Manuscript (Latest Living Document & Ground Truth)**
* [THESIS1UNGAB_BACANTO.docx](file:///c:/Users/USER/Desktop/THESIS/thesis-docs/THESIS1UNGAB_BACANTO.docx) — Formal Word proposal manuscript for submission
* [student_info.md](file:///c:/Users/USER/Desktop/THESIS/thesis-docs/student_info.md) — Student profile and schedule
* [bscs_thesis_guidelines.md](file:///c:/Users/USER/Desktop/THESIS/thesis-docs/bscs_thesis_guidelines.md) — Formatted BSCS thesis outline and formatting rules
* [implementation_plan.md](file:///c:/Users/USER/Desktop/THESIS/thesis-docs/implementation_plan.md) — Complete 10-phase thesis preparation plan
* [summary_for_daniela.md](file:///c:/Users/USER/Desktop/THESIS/thesis-docs/summary_for_daniela.md) — Summary sheet for Daniela's review
* [README.md](file:///c:/Users/USER/Desktop/THESIS/README.md) — Central project status and links hub

