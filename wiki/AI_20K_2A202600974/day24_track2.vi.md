---
type: summary
title: "Day 24 Track 2: Data Governance & Security"
description: "Summary of Day 24 Track 2 covering data governance frameworks, RBAC, IAM, encryption, PII anonymization, and compliance for AI systems."
tags: [data-governance, security, rbac, encryption, pii, compliance, track2]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/24/day24-Track02-data-governance-security.pdf"]
---
# Ngày 24 Track 2: Quản trị & Bảo mật Dữ liệu

Trang này tóm tắt bài giảng và phòng thí nghiệm về Quản trị & Bảo mật Dữ liệu cho các nền tảng AI trong Track 2.

## *Các Khái niệm Chính*

### *Khung Quản trị Dữ liệu*

  - **Danh mục Dữ liệu:** Các công cụ như Apache Atlas hoặc DataHub để khám phá và tài liệu hóa dữ liệu.
  - **Phân loại:** Phân loại dữ liệu thành Công khai, Nội bộ, Bảo mật và Hạn chế để thúc đẩy các chính sách truy cập.
  - **Dòng dữ liệu:** Theo dõi dữ liệu từ nguồn → biến đổi → huấn luyện → dự đoán để cung cấp dấu vết kiểm toán cho việc tuân thủ.
  - **Bảng thuật ngữ Doanh nghiệp:** Đảm bảo thuật ngữ nhất quán trên toàn tổ chức.

### *Nguyên tắc Đặc quyền Tối thiểu & RBAC*

Việc triển khai Kiểm soát Truy cập Dựa trên Vai trò (RBAC) đảm bảo người dùng và dịch vụ chỉ có quyền truy cập tối thiểu cần thiết.

  - **Quản trị viên:** Toàn quyền truy cập.
  - **Kỹ sư ML:** Truy cập dữ liệu huấn luyện và các tạo tác mô hình, nhưng không thể xóa dữ liệu sản xuất.
  - **Nhà phân tích Dữ liệu:** Truy cập vào các chỉ số tổng hợp và báo cáo, nhưng không có dữ liệu PII thô.
  - **Tài khoản Dịch vụ:** Mỗi pipeline ML có tài khoản dịch vụ riêng với các quyền được giới hạn, xoay vòng thông tin xác thực hàng tuần và sử dụng liên kết OIDC thay vì khóa tồn tại lâu dài.

### *Chiến lược Mã hóa*

  - **Khi truyền tải:** TLS 1.3 là bắt buộc.
  - **Khi lưu trữ:** AES-256 cho lưu trữ (S3, EBS, cơ sở dữ liệu) sử dụng khóa được quản lý KMS.
  - **Cấp cột:** Mã hóa riêng các trường PII cụ thể.
  - **Mã hóa Phong bì:** Các Khóa Mã hóa Dữ liệu (DEK) được mã hóa bởi các Khóa Mã hóa Khóa (KEK). DEK được xoay vòng hàng tháng, KEK hàng năm. Không bao giờ lưu trữ khóa dạng văn bản thuần trong mã.

### *Phát hiện & Ẩn danh PII (Presidio)*

  - **Khử nhận dạng so với Ẩn danh:** Khử nhận dạng có thể đảo ngược (sử dụng bảng tra cứu) và phù hợp cho phân tích nội bộ. Ẩn danh là không thể đảo ngược và được sử dụng cho các tập dữ liệu công khai hoặc chia sẻ nghiên cứu.
  - **Công cụ:** Microsoft Presidio được sử dụng để phát hiện PII thông qua NER (Nhận dạng Thực thể có Tên) và regex tùy chỉnh (ví dụ: số điện thoại Việt Nam, CCCD), sau đó ẩn danh nó qua che giấu, thay thế hoặc băm.
  - **Nguyên tắc chung:** Ẩn danh dữ liệu *trước khi* đưa vào pipeline huấn luyện. PII được mã hóa trong trọng số mô hình là một rủi ro vĩnh viễn.

### *Kiểm thử Tuân thủ & Bảo mật*

- **Compliance Automation:** Mapping regulations (GDPR, ISO 27001, NĐ13/2023) to technical controls using tools like OPA (Open Policy Agent) for Policy as Code in CI/CD.
  - **Tự động hóa Tuân thủ:** Ánh xạ các quy định (GDPR, ISO 27001, NĐ13/2023) sang các biện pháp kiểm soát kỹ thuật bằng các công cụ như OPA (Open Policy Agent) cho Chính sách dưới dạng Mã trong CI/CD.
  - **Kim tự tháp Kiểm thử Bảo mật:**
    - Quét phụ thuộc (pip-audit, Snyk)
    - Quét bí mật (git-secrets, truffleHog)
    - Kiểm thử Chèn lệnh (Garak)
    - Kiểm thử xâm nhập định kỳ
  - **Các mối đe dọa Đặc thù AI:** Bao gồm chèn lệnh, đầu độc dữ liệu, trích xuất mô hình, suy luận thành viên và rò rỉ PII. Phòng thủ yêu cầu các rào chắn đầu vào, củng cố mô hình, xác thực đầu ra và giám sát liên tục.

## *Phòng thí nghiệm 24: Quản trị Dữ liệu & Pipeline PII*

Học viên triển khai một nền tảng dữ liệu hỗ trợ RBAC trong FastAPI, xây dựng pipeline phát hiện và ẩn danh PII bằng Presidio với các bộ nhận dạng tiếng Việt tùy chỉnh (nhắm đến tỷ lệ phát hiện >95%), và thực hiện kiểm toán bảo mật bằng git-secrets và truffleHog.
