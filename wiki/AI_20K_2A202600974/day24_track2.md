---
type: summary
title: "Day 24 – Track 2: Data Governance & Security"
description: "Quản trị dữ liệu và bảo mật cho hệ thống AI: RBAC, encryption, PII detection, GDPR compliance."
tags: [ai, 20k, day24, track2, data-governance, security, gdpr, rbac]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/24/day24-Track02-data-governance-security.pdf"]
---

> **Lộ trình:** [[track2_ai_engineer|Track 2: AI Engineer]]


# Day 24 – Track 2: Data Governance & Security

**Giảng viên**: VinUniversity  
**Khóa**: AICB Phase 2 · Track 2 · Ngày 24

> **Case study thực tế**: Samsung employees paste confidential code vào ChatGPT → leaked trade secrets → company-wide ban. Data governance không phải optional.

---

## Mục tiêu học tập

1. Implement **RBAC** với least-privilege cho AI data platform
2. Build **PII detection & anonymization** pipeline (Presidio)
3. Áp dụng **encryption** at rest & in transit cho AI workloads
4. Map compliance requirements (**GDPR/NĐ13/ISO 27001**) vào technical controls

---

## Nội dung chính

### 1. Data Governance Framework
- **Data Catalog**: Inventory tất cả data assets, classification theo sensitivity
- **Data Lineage**: Theo vết dữ liệu từ nguồn đến điểm tiêu thụ
- **Data Quality**: Định nghĩa và enforce data contracts

### 2. RBAC & IAM cho AI Platform

| Role | Quyền |
|------|-------|
| Data Engineer | Read/Write raw data, create pipelines |
| ML Engineer | Read processed data, deploy models |
| Data Scientist | Read processed data, run experiments |
| Product Manager | Read aggregated metrics only |

### 3. PII Detection & Anonymization

```python
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

results = analyzer.analyze(text=user_input, language="vi")
anonymized = anonymizer.anonymize(text=user_input, analyzer_results=results)
```

### 4. Encryption

| Loại | Công cụ | Mục đích |
|------|---------|---------|
| **At Rest** | AWS KMS, HashiCorp Vault | Bảo vệ data trong storage |
| **In Transit** | TLS 1.3, mTLS | Bảo vệ data khi truyền qua mạng |

### 5. Compliance

| Quy định | Phạm vi | Yêu cầu chính |
|----------|---------|--------------|
| **GDPR** | EU users | Right to be forgotten, data minimization |
| **NĐ13/2023** | Người dùng Việt Nam | Consent, data localization |
| **ISO 27001** | Toàn cầu | Information security management system |

---

## Liên kết
- [[day24_track1]] – AI Ethics & Responsible AI
- [[day27_track2]] – Data Observability & Lineage
- [[day24_overview]]
