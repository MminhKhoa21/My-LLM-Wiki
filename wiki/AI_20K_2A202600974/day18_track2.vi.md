---
type: summary
title: "Day 18 Track 2: Data Lakehouse Architecture"
description: "Summary of Data Lakehouse concepts, including Delta Lake, Apache Iceberg, and Medallion architecture for AI workloads."
tags: [Data Lakehouse, Delta Lake, Apache Iceberg, Medallion Architecture, ACID, Storage]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/18/2-Day 18 - Track 2 - Data Lakehouse Architecture.pdf"]
---
# Kiến trúc Data Lakehouse (Ngày 18 - Track 2)

## 1. Sự tiến hóa của các nền tảng dữ liệu

- **Truyền thống (thập niên 1990-2010):** Kho dữ liệu (có cấu trúc, SQL, schema cứng nhắc, chi phí cao).

- **Kỷ nguyên ML (thập niên 2010-2020):** Hồ dữ liệu (S3, rẻ, linh hoạt, nhưng dễ trở thành "đầm lầy dữ liệu").

- **Kỷ nguyên LLM (thập niên 2020 trở đi):** Data Lakehouses kết hợp giao dịch ACID, định dạng mở (Delta/Iceberg) và lưu trữ đối tượng giá rẻ. Lý tưởng cho dữ liệu đa phương thức, embeddings và RAG.

## 2. Công nghệ cốt lõi: Delta Lake, Iceberg và Hudi

- **Delta Lake:** Sử dụng nhật ký giao dịch JSON (`_delta_log/`) để cung cấp các thuộc tính ACID trên lưu trữ đối tượng. Hỗ trợ schema evolution, Time Travel và Deletion Vectors.

- **Apache Iceberg:** Nổi tiếng với **Hidden Partitioning** (ngăn quét toàn bộ bảng bằng cách trừu tượng hóa logic phân vùng khỏi người dùng) và khả năng tiến hóa phân vùng mà không cần ghi lại dữ liệu.

- **Apache Hudi:** Mạnh mẽ cho khối lượng công việc có nhiều thay đổi (Merge-On-Read).

- **UniForm / XTable:** Các công cụ cho phép tương tác giữa Delta, Iceberg và Hudi.

## 3. Tối ưu hóa lưu trữ và các Anti-Patterns

- **Lưu trữ cột (Parquet):** Hiệu quả cao khi đọc các cột cụ thể so với định dạng hướng hàng (JSON/CSV). Sử dụng nén (Snappy, ZSTD) và thống kê min/max để bỏ qua tệp tin.

- **Z-ORDER và Phân vùng:** Đặt dữ liệu gần nhau để tối ưu truy vấn. Tránh phân vùng theo cột có độ phân giải cao (ví dụ: `user_id`).

- **Các Anti-Patterns cần tránh:**
  1. "Đổ tất cả vào S3" (Đầm lầy dữ liệu).
  2. Phân vùng theo cột có độ phân giải cao.
  3. Bỏ qua `OPTIMIZE` (dẫn đến vấn đề tệp tin nhỏ).
  4. Đặt `VACUUM 0 HOURS` (phá hủy Time Travel và đọc đồng thời).
  5. Sử dụng cụm Spark cho các truy vấn nhỏ (thay vào đó hãy dùng DuckDB).

## 4. Kiến trúc Medallion cho AI

- **Bronze (Thô):** Dữ liệu thô bất biến, chỉ nối thêm (ví dụ: nhật ký JSON thô, đầu vào của người dùng).

- **Silver (Đã làm sạch):** Dữ liệu đã được xác thực, loại bỏ trùng lặp và áp dụng schema (sử dụng `MERGE`).

- **Gold (Tổng hợp):** Dữ liệu sẵn sàng cho phân tích, kho đặc trưng (feature store) hoặc các đoạn tài liệu tinh chỉnh cho pipeline RAG.

## 5. Vận hành sản xuất và Quản trị

- **Phiên bản dữ liệu:** Tích hợp các phiên bản Delta với ID chạy MLflow để đảm bảo khả năng tái tạo mô hình.

- **CDC (Capture dữ liệu thay đổi):** Truyền trực tiếp các thay đổi từ cơ sở dữ liệu OLTP (như Postgres) qua Debezium và Kafka vào Lakehouses.

- **Hợp đồng dữ liệu:** Áp dụng schemas và các ràng buộc để duy trì chất lượng dữ liệu.

- **Bảo mật:** Xử lý PII bằng mã hóa, tokenization, RBAC/ABAC và tuân thủ luật Right-to-Forget (PDPL, GDPR).
