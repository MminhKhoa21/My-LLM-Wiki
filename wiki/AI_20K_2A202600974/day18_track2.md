---
type: summary
title: "Day 18 Track 2: Data Lakehouse Architecture"
description: "Summary of Data Lakehouse concepts, including Delta Lake, Apache Iceberg, and Medallion architecture for AI workloads."
tags: [Data Lakehouse, Delta Lake, Apache Iceberg, Medallion Architecture, ACID, Storage]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/18/2-Day 18 - Track 2 - Data Lakehouse Architecture.pdf"]
---
# Data Lakehouse Architecture (Day 18 - Track 2)
# Kiến trúc Data Lakehouse (Ngày 18 - Track 2)

## 1. Evolution of Data Platforms
## 1. Sự tiến hóa của các nền tảng dữ liệu

- **Traditional (1990s-2010s):** Data Warehouses (Structured, SQL, rigid schema, high cost).
- **Truyền thống (thập niên 1990-2010):** Kho dữ liệu (có cấu trúc, SQL, schema cứng nhắc, chi phí cao).

- **ML Era (2010s-2020s):** Data Lakes (S3, cheap, flexible, but prone to becoming "data swamps").
- **Kỷ nguyên ML (thập niên 2010-2020):** Hồ dữ liệu (S3, rẻ, linh hoạt, nhưng dễ trở thành "đầm lầy dữ liệu").

- **LLM Era (2020s+):** Data Lakehouses combining ACID transactions, open formats (Delta/Iceberg), and cheap object storage. Ideal for multi-modal data, embeddings, and RAG.
- **Kỷ nguyên LLM (thập niên 2020 trở đi):** Data Lakehouses kết hợp giao dịch ACID, định dạng mở (Delta/Iceberg) và lưu trữ đối tượng giá rẻ. Lý tưởng cho dữ liệu đa phương thức, embeddings và RAG.

## 2. Core Technologies: Delta Lake, Iceberg, and Hudi
## 2. Công nghệ cốt lõi: Delta Lake, Iceberg và Hudi

- **Delta Lake:** Uses a JSON transaction log (`_delta_log/`) to provide ACID properties on object storage. Supports schema evolution, Time Travel, and Deletion Vectors.
- **Delta Lake:** Sử dụng nhật ký giao dịch JSON (`_delta_log/`) để cung cấp các thuộc tính ACID trên lưu trữ đối tượng. Hỗ trợ schema evolution, Time Travel và Deletion Vectors.

- **Apache Iceberg:** Renowned for **Hidden Partitioning** (prevents full table scans by abstracting partition logic from users) and partition evolution without rewriting data.
- **Apache Iceberg:** Nổi tiếng với **Hidden Partitioning** (ngăn quét toàn bộ bảng bằng cách trừu tượng hóa logic phân vùng khỏi người dùng) và khả năng tiến hóa phân vùng mà không cần ghi lại dữ liệu.

- **Apache Hudi:** Strong for mutation-heavy workloads (Merge-On-Read).
- **Apache Hudi:** Mạnh mẽ cho khối lượng công việc có nhiều thay đổi (Merge-On-Read).

- **UniForm / XTable:** Tools enabling interoperability between Delta, Iceberg, and Hudi.
- **UniForm / XTable:** Các công cụ cho phép tương tác giữa Delta, Iceberg và Hudi.

## 3. Storage Optimization and Anti-Patterns
## 3. Tối ưu hóa lưu trữ và các Anti-Patterns

- **Columnar Storage (Parquet):** Highly efficient for reading specific columns compared to row-oriented formats (JSON/CSV). Uses compression (Snappy, ZSTD) and min/max stats to skip files.
- **Lưu trữ cột (Parquet):** Hiệu quả cao khi đọc các cột cụ thể so với định dạng hướng hàng (JSON/CSV). Sử dụng nén (Snappy, ZSTD) và thống kê min/max để bỏ qua tệp tin.

- **Z-ORDER and Partitioning:** Co-locating data to optimize queries. Avoid partitioning by high-cardinality columns (e.g., `user_id`).
- **Z-ORDER và Phân vùng:** Đặt dữ liệu gần nhau để tối ưu truy vấn. Tránh phân vùng theo cột có độ phân giải cao (ví dụ: `user_id`).

- **Anti-Patterns to Avoid:**
- **Các Anti-Patterns cần tránh:**
  1. "Dump everything into S3" (Data Swamp).
  1. "Đổ tất cả vào S3" (Đầm lầy dữ liệu).
  2. Partitioning by high-cardinality columns.
  2. Phân vùng theo cột có độ phân giải cao.
  3. Ignoring `OPTIMIZE` (leading to the small-file problem).
  3. Bỏ qua `OPTIMIZE` (dẫn đến vấn đề tệp tin nhỏ).
  4. Setting `VACUUM 0 HOURS` (destroys Time Travel and concurrent reads).
  4. Đặt `VACUUM 0 HOURS` (phá hủy Time Travel và đọc đồng thời).
  5. Using Spark clusters for tiny queries (use DuckDB instead).
  5. Sử dụng cụm Spark cho các truy vấn nhỏ (thay vào đó hãy dùng DuckDB).

## 4. Medallion Architecture for AI
## 4. Kiến trúc Medallion cho AI

- **Bronze (Raw):** Immutable, append-only raw data (e.g., raw JSON logs, user inputs).
- **Bronze (Thô):** Dữ liệu thô bất biến, chỉ nối thêm (ví dụ: nhật ký JSON thô, đầu vào của người dùng).

- **Silver (Cleaned):** Validated, deduplicated, and schema-enforced data (using `MERGE`).
- **Silver (Đã làm sạch):** Dữ liệu đã được xác thực, loại bỏ trùng lặp và áp dụng schema (sử dụng `MERGE`).

- **Gold (Aggregated):** Analytics-ready, feature store, or refined doc chunks for RAG pipelines.
- **Gold (Tổng hợp):** Dữ liệu sẵn sàng cho phân tích, kho đặc trưng (feature store) hoặc các đoạn tài liệu tinh chỉnh cho pipeline RAG.

## 5. Production Ops and Governance
## 5. Vận hành sản xuất và Quản trị

- **Data Versioning:** Integrating Delta versions with MLflow run IDs to ensure model reproducibility.
- **Phiên bản dữ liệu:** Tích hợp các phiên bản Delta với ID chạy MLflow để đảm bảo khả năng tái tạo mô hình.

- **Change Data Capture (CDC):** Streaming changes from OLTP databases (like Postgres) via Debezium and Kafka into Lakehouses.
- **CDC (Capture dữ liệu thay đổi):** Truyền trực tiếp các thay đổi từ cơ sở dữ liệu OLTP (như Postgres) qua Debezium và Kafka vào Lakehouses.

- **Data Contracts:** Enforcing schemas and constraints to maintain data quality.
- **Hợp đồng dữ liệu:** Áp dụng schemas và các ràng buộc để duy trì chất lượng dữ liệu.

- **Security:** Handling PII with tokenization, encryption, RBAC/ABAC, and respecting Right-to-Forget laws (PDPL, GDPR).
- **Bảo mật:** Xử lý PII bằng mã hóa, tokenization, RBAC/ABAC và tuân thủ luật Right-to-Forget (PDPL, GDPR).
