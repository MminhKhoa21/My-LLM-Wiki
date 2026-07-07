---
type: summary
title: "Data Pipeline Engineering (Track 2)"
description: "Summary of Day 17 Track 2 on building robust data pipelines, Medallion Architecture, and streaming ingestion."
tags: [AI_20K_2A202600974, Day17, Data_Pipeline, ETL, Kafka]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/17/Day 17 - Track 2 - Data Pipeline.pdf"]
---
# Data Pipeline Engineering (Day 17 - Track 2)
*# Kỹ thuật Pipeline Dữ liệu (Ngày 17 - Track 2)*

This track emphasizes that data pipelines are a critical dependency of AI models. A faulty pipeline can silently destroy model accuracy in production ("Garbage in, garbage out").
*Track này nhấn mạnh rằng các pipeline dữ liệu là một phụ thuộc quan trọng của các mô hình AI. Một pipeline bị lỗi có thể âm thầm phá hủy độ chính xác của mô hình trong môi trường sản xuất ("Rác vào, rác ra").*

## Key Concepts
## Các khái niệm chính

### ETL vs. ELT & Medallion Architecture
### ETL so với ELT & Kiến trúc Medallion

- **ELT (Extract, Load, Transform)** is the default for cloud-native AI pipelines due to cheap compute in the lakehouse.
  * **ELT (Trích xuất, Tải, Biến đổi)** là mặc định cho các pipeline AI gốc đám mây nhờ chi phí tính toán rẻ trong lakehouse.
- **Medallion Architecture:**
  * **Kiến trúc Medallion:**
  - **Bronze:** Raw, append-only, kept forever.
    * **Bronze:** Dữ liệu thô, chỉ nối thêm, được giữ vĩnh viễn.
  - **Silver:** Cleaned, conformed, deduplicated, and schema-enforced.
    * **Silver:** Đã được làm sạch, chuẩn hóa, loại bỏ trùng lặp và áp đặt lược đồ.
  - **Gold:** Business-ready, aggregated, ML features.
    * **Gold:** Sẵn sàng cho kinh doanh, tổng hợp, đặc trưng ML.

### Extract Patterns and Ingestion
### Mẫu trích xuất và tiếp nhận dữ liệu

- **Extract Patterns:** Full, Incremental (cursor-based), CDC (Change Data Capture using Debezium to read transaction logs).
  * **Các mẫu trích xuất:** Toàn bộ, Tăng dần (dựa trên con trỏ), CDC (Capture dữ liệu thay đổi sử dụng Debezium để đọc log giao dịch).
- **Ingestion for LLMs:** Ingesting unstructured data involves parsing, chunking (e.g., recursive 512 tokens), and embedding into a Vector store.
  * **Tiếp nhận dữ liệu cho LLM:** Tiếp nhận dữ liệu phi cấu trúc bao gồm phân tích cú pháp, chia nhỏ (ví dụ: đệ quy 512 token) và nhúng vào kho Vector.

### Orchestration
### Điều phối

- **Airflow 3.0:** Transitioning from pure task-based workflows to asset-aware workflows, event-driven scheduling, and data assets.
  * **Airflow 3.0:** Chuyển đổi từ quy trình làm việc thuần túy dựa trên tác vụ sang quy trình làm việc nhận biết tài sản, lập lịch theo sự kiện và tài sản dữ liệu.
- **Declarative Asset Pipelines (Dagster, DLT):** Focus on declaring *what* the datasets and dependencies are, rather than *how* to run them. Example: `Materialized View` vs `Streaming Table`.
  * **Pipeline tài sản khai báo (Dagster, DLT):** Tập trung vào khai báo *cái gì* là các tập dữ liệu và phụ thuộc, thay vì *làm thế nào* để chạy chúng. Ví dụ: `Materialized View` so với `Streaming Table`.

### Streaming Ingestion
### Tiếp nhận dữ liệu luồng

- **Kafka Architecture:** Used for streaming ingestion. Kafka 4.0 removes ZooKeeper (KRaft mode).
  * **Kiến trúc Kafka:** Được sử dụng cho tiếp nhận dữ liệu luồng. Kafka 4.0 loại bỏ ZooKeeper (chế độ KRaft).
- **Streaming vs Batch:** Streaming (e.g., Kafka + Flink) ensures very low latency for real-time feature generation, reducing training-serving skew compared to batch processing.
  * **Luồng so với Hàng loạt:** Luồng (ví dụ: Kafka + Flink) đảm bảo độ trễ rất thấp cho việc tạo đặc trưng thời gian thực, giảm độ lệch giữa huấn luyện và phục vụ so với xử lý hàng loạt.

### Validation, Quality Gates, and Contracts
### Xác thực, Cổng chất lượng và Hợp đồng

- **Validation Gates:** Implement "fail early" strategies using tools like Pandera or Great Expectations (GX). Bad records go into a Quarantine/DLQ (dead-letter queue) rather than breaking the pipeline.
  * **Cổng xác thực:** Triển khai chiến lược "thất bại sớm" bằng các công cụ như Pandera hoặc Great Expectations (GX). Các bản ghi xấu được đưa vào Hàng đợi cách ly/DLQ (hàng đợi thư chết) thay vì làm hỏng pipeline.
- **LLM-as-a-Judge:** Used for data quality checks that standard rules miss, such as semantic duplicates or contextual anomalies.
  * **LLM-as-a-Judge:** Được sử dụng để kiểm tra chất lượng dữ liệu mà các quy tắc tiêu chuẩn bỏ sót, chẳng hạn như trùng lặp ngữ nghĩa hoặc bất thường ngữ cảnh.
- **Data Contracts:** Establish agreements between data producers and consumers defining schema, semantics, quality, and SLAs to prevent silent schema drift.
  * **Hợp đồng dữ liệu:** Thiết lập thỏa thuận giữa nhà sản xuất và người tiêu dùng dữ liệu, xác định lược đồ, ngữ nghĩa, chất lượng và SLA để ngăn chặn sự trôi dạt lược đồ thầm lặng.

### AI-Specific Pipelines
### Pipeline dành riêng cho AI

- **Data Flywheel:** Using agent traces (prompts, tool calls, responses, user feedback) as a raw data source (Bronze layer) to build evaluation and fine-tuning datasets.
  * **Bánh đà dữ liệu:** Sử dụng dấu vết tác nhân (prompt, lời gọi công cụ, phản hồi, phản hồi người dùng) như một nguồn dữ liệu thô (lớp Bronze) để xây dựng tập dữ liệu đánh giá và tinh chỉnh.
- **Deduplication:** Extremely important for AI training to prevent verbatim regurgitation. Techniques include lexical dedup (MinHash+LSH) and semantic dedup (SemDeDup).
  * **Loại bỏ trùng lặp:** Cực kỳ quan trọng cho việc huấn luyện AI để ngăn chặn sự lặp lại nguyên văn. Các kỹ thuật bao gồm loại bỏ trùng lặp từ vựng (MinHash+LSH) và loại bỏ trùng lặp ngữ nghĩa (SemDeDup).
- **Feature Store:** Centralized system to define features once and serve them identically for offline training and online inference, solving training-serving skew.
  * **Feature Store:** Hệ thống tập trung để định nghĩa các đặc trưng một lần và phục vụ chúng giống hệt nhau cho huấn luyện ngoại tuyến và suy luận trực tuyến, giải quyết độ lệch giữa huấn luyện và phục vụ.
