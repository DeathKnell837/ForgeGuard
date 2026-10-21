# Database and Audit Ledger Specifications

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

This folder contains the persistent transaction ledger database for the **ForgeGuard** forensics system. In compliance with academic auditability guidelines, every inference run executed through the system is timestamped and recorded in structured JSON format.

### Database File Inventory
| Filename | Format | Description |
| :--- | :--- | :--- |
| `benchmark_records_log.json` | JSON Array | Primary audit ledger recording verification sessions, inference telemetry, verdicts, and confidence scores |

---

## 2. Ledger Schema Specification

Each entry in `benchmark_records_log.json` adheres to the following JSON schema:

```json
{
  "Date and time": "YYYY-MM-DD HH:MM:SS",
  "Architecture": "Basic CNN | MobileNetV2 | ResNet50",
  "Prediction result": "Authentic | Forged",
  "Confidence score": "XX.X%",
  "Processing time": "XX.X ms",
  "Memory load": "XX.X MB",
  "Receipt": "filename.jpg | Sample_authentic | Sample_edited | Sample_generated"
}
```

### Schema Attribute Definitions
1. **`Date and time` (String):** Standard local timestamp indicating exact moment of neural inference.
2. **`Architecture` (String):** The specific CNN architecture evaluated (`Basic CNN`, `MobileNetV2`, or `ResNet50`).
3. **`Prediction result` (String):** Binary classification verdict (`Authentic` or `Forged`).
4. **`Confidence score` (String):** Calibrated percentage output from the sigmoid activation unit.
5. **`Processing time` (String):** Wall-clock inference latency measured in milliseconds (`ms`).
6. **`Memory load` (String):** Physical process memory footprint monitored via `psutil` in megabytes (`MB`).
7. **`Receipt` (String):** Target receipt image filename or benchmark preset label.

---

## 3. Persistence and Synchronization Guarantees

* **Atomic Serialization:** Records are updated upon completion of inference across all three architectures and serialized with indent formatting.
* **Rolling History:** Maintains the most recent 100 historical verification events to prevent unbounded growth while preserving audit records.
* **Redundant Mirroring:** The system automatically mirrors records across `04_Database_Files/`, `models/`, and `database/` directories if present, ensuring data integrity across different execution environments.
