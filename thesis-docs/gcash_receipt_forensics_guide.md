# 🔍 GCash Receipt Forensic & Design Specifications Guide

**BSCS Thesis Reference Document** — *Securing Mobile Transaction: A Comparative Evaluation of CNN Architectures in Detecting Digital Receipt Forgery* (NDMC CITE, 2026)

---

## 🎨 1. Official Brand Color System

| Color Name | Hex Code | Purpose in Receipt |
|:---|:---:|:---|
| **Blue Ribbon** (Primary GCash Blue) | `#1972F9` | Primary headers, transaction amounts, checkmarks |
| **Downriver** (Dark Navy) | `#0B2757` | Main text titles, recipient names, card labels |
| **Dodger Blue** (Accent Light Blue) | `#518FFB` | Active highlights, button outlines |
| **Muted Slate Grey** | `#64748B` | Timestamp text, reference number labels |
| **Background Off-White / Soft Blue** | `#F8FAFC` / `#EFF6FF` | Receipt card background container |

---

## 🔤 2. Official Typography Hierarchy

| Font Family | Styles | Usage in GCash Receipts |
|:---|:---|:---|
| **Karla** | `Karla-Regular.ttf`, `Karla-Bold.ttf` | Transaction amounts (`₱ 500.00`), 13-digit reference numbers (`Ref No. 1001 543 610110`), body text, timestamps |
| **Poppins** | `Poppins-Regular.ttf`, `Poppins-SemiBold.ttf`, `Poppins-Bold.ttf` | Main title headers (`Express Send`), section dividers, status text (`Successfully Sent`) |

---

## 🔐 3. Security & Authentic Receipt Features

1. **13-Digit Reference Number Format:**
   - Always exactly 13 digits, formatted in 4-3-6 or 4-3-3-3 clusters (e.g., `Ref No. 1001 847 920 184`).
2. **BSP Privacy Name Masking:**
   - Recipient names are partially masked to comply with Data Privacy rules:
   - Example: `JUAN DELA CRUZ` $\rightarrow$ `JU•• D••• C••Z` or `MA••• C•••• S.`.
3. **gForest Carbon Footprint Banner:**
   - Contains eco-friendly reminder text (*"By going digital, you reduce your carbon footprint"*).
4. **No Physical Paper Tear Lines:**
   - Real mobile app screenshot receipts are digital cards and do NOT feature physical paper receipt tear perforations.

---

## 🚨 4. Key Indicators of Digital Receipt Forgeries

| Forgery Indicator | Visual / Forensic Feature | How ELA & CNN Flags It |
|:---|:---|:---|
| **Amount Alteration** | Photoshop / Markup text edit over amount field | High ELA compression error variance over amount bounding box |
| **Font Mismatch** | Using Arial / Calibri / System Monospace instead of Karla/Poppins | Structural CNN feature discrepancy in letter geometry |
| **Unmasked Names** | Full unmasked recipient names displayed | Policy & visual template anomaly |
| **Invalid Ref No Length** | Reference numbers with fewer or more than 13 digits | Sequence & pixel density anomaly |
| **Re-compression Artifacts** | Screenshot edited in Gallery app and saved multiple times | ELA highlights double-compression grid discontinuities |
