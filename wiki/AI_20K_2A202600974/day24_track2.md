---
type: summary
title: "Day 24 Track 2: Data Governance & Security"
description: "Summary of Day 24 Track 2 covering data governance frameworks, RBAC, IAM, encryption, PII anonymization, and compliance for AI systems."
tags: [data-governance, security, rbac, encryption, pii, compliance, track2]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/24/day24-Track02-data-governance-security.pdf"]
---
# Day 24 Track 2: Data Governance & Security
*# Ngày 24 Track 2: Quản trị & Bảo mật Dữ liệu*

This page summarizes the lecture and lab on Data Governance and Security for AI platforms in Track 2.
*Trang này tóm tắt bài giảng và phòng thí nghiệm về Quản trị & Bảo mật Dữ liệu cho các nền tảng AI trong Track 2.*

## Key Concepts
## *Các Khái niệm Chính*

### Data Governance Framework
### *Khung Quản trị Dữ liệu*

- **Data Catalog:** Tools like Apache Atlas or DataHub to discover and document data.
  - **Danh mục Dữ liệu:** Các công cụ như Apache Atlas hoặc DataHub để khám phá và tài liệu hóa dữ liệu.
- **Classification:** Categorizing data into Public, Internal, Confidential, and Restricted to drive access policies.
  - **Phân loại:** Phân loại dữ liệu thành Công khai, Nội bộ, Bảo mật và Hạn chế để thúc đẩy các chính sách truy cập.
- **Lineage:** Tracking data from source → transform → training → predict to provide an audit trail for compliance.
  - **Dòng dữ liệu:** Theo dõi dữ liệu từ nguồn → biến đổi → huấn luyện → dự đoán để cung cấp dấu vết kiểm toán cho việc tuân thủ.
- **Business Glossary:** Ensuring consistent terminology across the organization.
  - **Bảng thuật ngữ Doanh nghiệp:** Đảm bảo thuật ngữ nhất quán trên toàn tổ chức.

### Principle of Least Privilege & RBAC
### *Nguyên tắc Đặc quyền Tối thiểu & RBAC*

Implementing Role-Based Access Control (RBAC) ensures users and services only have the minimum access necessary.
*Việc triển khai Kiểm soát Truy cập Dựa trên Vai trò (RBAC) đảm bảo người dùng và dịch vụ chỉ có quyền truy cập tối thiểu cần thiết.*

- **Admin:** Full access.
  - **Quản trị viên:** Toàn quyền truy cập.
- **ML Engineer:** Access to training data and model artifacts, but cannot delete production data.
  - **Kỹ sư ML:** Truy cập dữ liệu huấn luyện và các tạo tác mô hình, nhưng không thể xóa dữ liệu sản xuất.
- **Data Analyst:** Access to aggregated metrics and reports, but no raw PII data.
  - **Nhà phân tích Dữ liệu:** Truy cập vào các chỉ số tổng hợp và báo cáo, nhưng không có dữ liệu PII thô.
- **Service Accounts:** Each ML pipeline gets its own service account with scoped permissions, rotating credentials weekly, and using OIDC federation instead of long-lived keys.
  - **Tài khoản Dịch vụ:** Mỗi pipeline ML có tài khoản dịch vụ riêng với các quyền được giới hạn, xoay vòng thông tin xác thực hàng tuần và sử dụng liên kết OIDC thay vì khóa tồn tại lâu dài.

### Encryption Strategy
### *Chiến lược Mã hóa*

- **In Transit:** TLS 1.3 is mandatory.
  - **Khi truyền tải:** TLS 1.3 là bắt buộc.
- **At Rest:** AES-256 for storage (S3, EBS, databases) using KMS managed keys.
  - **Khi lưu trữ:** AES-256 cho lưu trữ (S3, EBS, cơ sở dữ liệu) sử dụng khóa được quản lý KMS.
- **Column-Level:** Encrypting specific PII fields separately.
  - **Cấp cột:** Mã hóa riêng các trường PII cụ thể.
- **Envelope Encryption:** Data Encryption Keys (DEK) are encrypted by Key Encryption Keys (KEK). DEKs are rotated monthly, KEKs annually. Never store plaintext keys in code.
  - **Mã hóa Phong bì:** Các Khóa Mã hóa Dữ liệu (DEK) được mã hóa bởi các Khóa Mã hóa Khóa (KEK). DEK được xoay vòng hàng tháng, KEK hàng năm. Không bao giờ lưu trữ khóa dạng văn bản thuần trong mã.

### PII Detection & Anonymization (Presidio)
### *Phát hiện & Ẩn danh PII (Presidio)*

- **De-identification vs. Anonymization:** De-identification is reversible (using a lookup table) and suitable for internal analytics. Anonymization is irreversible and used for public datasets or research sharing.
  - **Khử nhận dạng so với Ẩn danh:** Khử nhận dạng có thể đảo ngược (sử dụng bảng tra cứu) và phù hợp cho phân tích nội bộ. Ẩn danh là không thể đảo ngược và được sử dụng cho các tập dữ liệu công khai hoặc chia sẻ nghiên cứu.
- **Tools:** Microsoft Presidio is used to detect PII via NER (Named Entity Recognition) and custom regex (e.g., Vietnamese phone numbers, CCCD), and then anonymize it via masking, replacement, or hashing.
  - **Công cụ:** Microsoft Presidio được sử dụng để phát hiện PII thông qua NER (Nhận dạng Thực thể có Tên) và regex tùy chỉnh (ví dụ: số điện thoại Việt Nam, CCCD), sau đó ẩn danh nó qua che giấu, thay thế hoặc băm.
- **Rule of Thumb:** Anonymize data *before* ingestion into the training pipeline. PII encoded in model weights is a permanent liability.
  - **Nguyên tắc chung:** Ẩn danh dữ liệu *trước khi* đưa vào pipeline huấn luyện. PII được mã hóa trong trọng số mô hình là một rủi ro vĩnh viễn.

### Compliance & Security Testing
### *Kiểm thử Tuân thủ & Bảo mật*

- **Compliance Automation:** Mapping regulations (GDPR, ISO 27001, NĐ13/2023) to technical controls using tools like OPA (Open Policy Agent) for Policy as Code in CI/CD.
  - **Tự động hóa Tuân thủ:** Ánh xạ các quy định (GDPR, ISO 27001, NĐ13/2023) sang các biện pháp kiểm soát kỹ thuật bằng các công cụ như OPA (Open Policy Agent) cho Chính sách dưới dạng Mã trong CI/CD.
- **Security Testing Pyramid:**
  - **Kim tự tháp Kiểm thử Bảo mật:**
  - Dependency Scanning (pip-audit, Snyk)
    - Quét phụ thuộc (pip-audit, Snyk)
  - SAST (Bandit for Python)
    - SAST (Bandit cho Python)
  - Secret Scanning (git-secrets, truffleHog)
    - Quét bí mật (git-secrets, truffleHog)
  - Prompt Injection Testing (Garak)
    - Kiểm thử Chèn lệnh (Garak)
  - Periodic Pentesting
    - Kiểm thử xâm nhập định kỳ
- **AI-Specific Threats:** Include prompt injection, data poisoning, model extraction, membership inference, and PII leakage. Defense requires input guardrails, model hardening, output validation, and continuous monitoring.
  - **Các mối đe dọa Đặc thù AI:** Bao gồm chèn lệnh, đầu độc dữ liệu, trích xuất mô hình, suy luận thành viên và rò rỉ PII. Phòng thủ yêu cầu các rào chắn đầu vào, củng cố mô hình, xác thực đầu ra và giám sát liên tục.

## Lab 24: Data Governance & PII Pipeline
## *Phòng thí nghiệm 24: Quản trị Dữ liệu & Pipeline PII*

Students implement an RBAC-enabled data platform in FastAPI, build a PII detection and anonymization pipeline using Presidio with custom Vietnamese recognizers (aiming for >95% detection rate), and perform a security audit using git-secrets and truffleHog.
*Học viên triển khai một nền tảng dữ liệu hỗ trợ RBAC trong FastAPI, xây dựng pipeline phát hiện và ẩn danh PII bằng Presidio với các bộ nhận dạng tiếng Việt tùy chỉnh (nhắm đến tỷ lệ phát hiện >95%), và thực hiện kiểm toán bảo mật bằng git-secrets và truffleHog.*
