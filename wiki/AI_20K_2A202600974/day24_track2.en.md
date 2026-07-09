---
type: summary
title: "Day 24 Track 2: Data Governance & Security"
description: "Summary of Day 24 Track 2 covering data governance frameworks, RBAC, IAM, encryption, PII anonymization, and compliance for AI systems."
tags: [data-governance, security, rbac, encryption, pii, compliance, track2]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/24/day24-Track02-data-governance-security.pdf"]
---
# Day 24 Track 2: Data Governance & Security

This page summarizes the lecture and lab on Data Governance and Security for AI platforms in Track 2.

## Key Concepts

### Data Governance Framework

- **Data Catalog:** Tools like Apache Atlas or DataHub to discover and document data.
- **Classification:** Categorizing data into Public, Internal, Confidential, and Restricted to drive access policies.
- **Lineage:** Tracking data from source → transform → training → predict to provide an audit trail for compliance.
- **Business Glossary:** Ensuring consistent terminology across the organization.

### Principle of Least Privilege & RBAC

Implementing Role-Based Access Control (RBAC) ensures users and services only have the minimum access necessary.

- **Admin:** Full access.
- **ML Engineer:** Access to training data and model artifacts, but cannot delete production data.
- **Data Analyst:** Access to aggregated metrics and reports, but no raw PII data.
- **Service Accounts:** Each ML pipeline gets its own service account with scoped permissions, rotating credentials weekly, and using OIDC federation instead of long-lived keys.

### Encryption Strategy

- **In Transit:** TLS 1.3 is mandatory.
- **At Rest:** AES-256 for storage (S3, EBS, databases) using KMS managed keys.
- **Column-Level:** Encrypting specific PII fields separately.
- **Envelope Encryption:** Data Encryption Keys (DEK) are encrypted by Key Encryption Keys (KEK). DEKs are rotated monthly, KEKs annually. Never store plaintext keys in code.

### PII Detection & Anonymization (Presidio)

- **De-identification vs. Anonymization:** De-identification is reversible (using a lookup table) and suitable for internal analytics. Anonymization is irreversible and used for public datasets or research sharing.
- **Tools:** Microsoft Presidio is used to detect PII via NER (Named Entity Recognition) and custom regex (e.g., Vietnamese phone numbers, CCCD), and then anonymize it via masking, replacement, or hashing.
- **Rule of Thumb:** Anonymize data *before* ingestion into the training pipeline. PII encoded in model weights is a permanent liability.

### Compliance & Security Testing

- **Security Testing Pyramid:**
  - Dependency Scanning (pip-audit, Snyk)
  - SAST (Bandit for Python)
    - SAST (Bandit cho Python)
  - Secret Scanning (git-secrets, truffleHog)
  - Prompt Injection Testing (Garak)
  - Periodic Pentesting
- **AI-Specific Threats:** Include prompt injection, data poisoning, model extraction, membership inference, and PII leakage. Defense requires input guardrails, model hardening, output validation, and continuous monitoring.

## Lab 24: Data Governance & PII Pipeline

Students implement an RBAC-enabled data platform in FastAPI, build a PII detection and anonymization pipeline using Presidio with custom Vietnamese recognizers (aiming for >95% detection rate), and perform a security audit using git-secrets and truffleHog.

---

### Day 24 Review Questions

1. **According to the Least Privilege principle, which of the following roles has permission to delete production data?**  
   - A. ML Engineer  
     *A. ML Engineer*  
   - B. Data Analyst  
     *B. Data Analyst*  
   - C. Admin  
     *C. Admin*  
   - D. Service Account  
     *D. Service Account*  
   **Answer:** C  

2. **In the envelope encryption model, how is the Data Encryption Key (DEK) protected?**  
   - A. Stored as plaintext in code  
   - B. Encrypted by a Key Encryption Key (KEK)  
   - C. Rotated annually instead of monthly  
   - D. Embedded directly into the model  
   **Answer:** B  

3. **Which PII processing technique is reversible and commonly used for internal analysis?**  
   - A. Anonymization  
     *A. Anonymization*  
   - B. Masking  
     *B. Masking*  
   - C. Hashing  
     *C. Hashing*  
   - D. De-identification  
     *D. De-identification*  
   **Answer:** D  

4. **In the Security Testing Pyramid, which tool is used to detect exposed secrets in a source code repository?**  
   - A. Bandit (SAST)  
     *A. Bandit (SAST)*  
   - B. pip-audit (Dependency Scanning)  
     *B. pip-audit (Dependency Scanning)*  
   - C. truffleHog (Secret Scanning)  
     *C. truffleHog (Secret Scanning)*  
   - D. Garak (Prompt Injection Testing)  
     *D. Garak (Prompt Injection Testing)*  
   **Answer:** C
