---
type: summary
title: "Summary: Day 10 Data Pipeline Observability E402"
description: "Detailed summary of the VinUniversity AICB Day 10 lecture focusing on Data Pipeline fundamentals, ETL/ELT, Observability pillars, and Orchestration."
tags: [data-pipeline, observability, etl, elt, orchestration, rag]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/10/Day10 data pipeline observability E402.pdf"]
---

# Summary: Day 10 Data Pipeline Observability E402
# Tóm tắt: Ngày 10 - Data Pipeline Observability E402

This document summarizes the VinUniversity AICB Phase 1 (2026) lecture on Data Pipelines and Data Observability. It explores why data pipelines are the foundation of all AI products, detailing ingestion, transformation, quality gates, and orchestration.
Tài liệu này tóm tắt bài giảng Giai đoạn 1 AICB của Đại học VinUni (2026) về Data Pipelines và Data Observability. Nó khám phá lý do tại sao data pipelines lại là nền tảng của mọi sản phẩm AI, trình bày chi tiết về thu thập dữ liệu (ingestion), biến đổi (transformation), các cổng chất lượng (quality gates), và điều phối (orchestration).

## 1. Why Data Pipelines are Foundational for AI
## 1. Tại sao Data Pipelines là Nền tảng cho AI
- **Time Investment**: 60–80% of real-world AI project time is spent on data work (collection, cleaning, pipelines, monitoring), not on model building.
- **Đầu tư Thời gian**: 60–80% thời gian của dự án AI thực tế được dành cho công việc liên quan đến dữ liệu (thu thập, làm sạch, pipelines, giám sát), chứ không phải là xây dựng mô hình.
- **Garbage In, Garbage Out**: An excellent RAG agent will still hallucinate if its vector store contains dirty data. 
- **Rác Vào, Rác Ra (Garbage In, Garbage Out)**: Một RAG agent xuất sắc vẫn sẽ bị ảo giác nếu vector store của nó chứa dữ liệu bẩn.
- **The Core Difference**: In traditional BI, bad data means a wrong number on a dashboard. In AI, bad data means an Agent takes the wrong action or gives incorrect advice directly to the user.
- **Sự Khác biệt Cốt lõi**: Trong BI truyền thống, dữ liệu hỏng đồng nghĩa với một con số sai trên bảng điều khiển. Trong AI, dữ liệu hỏng có nghĩa là Agent thực hiện hành động sai hoặc đưa ra lời khuyên không chính xác trực tiếp cho người dùng.

## 2. Data Pipeline Fundamentals (ETL vs. ELT)
## 2. Các Kiến thức Cơ bản về Data Pipeline (ETL vs. ELT)
A standard AI data stack moves from Sources -> Pipeline -> Storage -> Serving -> Agent.
Một ngăn xếp (stack) dữ liệu AI tiêu chuẩn di chuyển từ Nguồn (Sources) -> Pipeline -> Lưu trữ (Storage) -> Phục vụ (Serving) -> Agent.
- **ETL (Extract, Transform, Load)**: Data is transformed *before* loading into the warehouse. Ideal when data is sensitive and needs PII masking, or when the schema is highly stable.
- **ETL (Trích xuất, Biến đổi, Tải)**: Dữ liệu được biến đổi *trước khi* đưa vào kho. Lý tưởng khi dữ liệu mang tính nhạy cảm và cần che giấu PII, hoặc khi lược đồ (schema) có độ ổn định cao.
- **ELT (Extract, Load, Transform)**: Raw data is loaded into a data lake/warehouse first, and transformed later. Ideal for handling big data, multiple diverse sources, and allowing easy replay/backfilling of raw data when experimenting with new chunking strategies.
- **ELT (Trích xuất, Tải, Biến đổi)**: Dữ liệu thô được đưa vào hồ/kho dữ liệu trước và được biến đổi sau. Lý tưởng cho việc xử lý dữ liệu lớn (big data), nhiều nguồn đa dạng và cho phép dễ dàng chạy lại/điền bù (replay/backfilling) dữ liệu thô khi thử nghiệm với các chiến lược phân đoạn (chunking) mới.
- **Batch vs. Streaming**:
- **Xử lý Hàng loạt (Batch) vs. Xử lý Luồng (Streaming)**:
  - *Batch*: Scheduled processing (hourly/daily). Low cost, high latency.
  - *Batch*: Xử lý theo lịch trình (hàng giờ/hàng ngày). Chi phí thấp, độ trễ cao.
  - *Streaming*: Real-time processing. Low latency, but higher complexity and cost.
  - *Streaming*: Xử lý thời gian thực. Độ trễ thấp, nhưng độ phức tạp và chi phí cao hơn.

## 3. Ingestion Strategies
## 3. Chiến lược Thu thập Dữ liệu (Ingestion Strategies)
Ingestion pulls data from Structured DBs (PostgreSQL via CDC), Unstructured Files (PDFs, HTML), and Event Streams (Kafka, Webhooks).
Quá trình thu thập (Ingestion) lấy dữ liệu từ các DB có Cấu trúc (PostgreSQL qua CDC), Tệp Phi cấu trúc (PDFs, HTML), và Luồng Sự kiện (Kafka, Webhooks).
- **Key Requirements for AI Ingestion**:
- **Yêu cầu Chính đối với Thu thập Dữ liệu AI**:
  - Incremental Syncs: Only fetch what changed.
  - Đồng bộ Tăng dần (Incremental Syncs): Chỉ lấy những gì đã thay đổi.
  - Idempotent Upserts: Prevent duplicate chunking on reruns.
  - Cập nhật Không đổi (Idempotent Upserts): Ngăn chặn việc phân đoạn (chunking) lặp lại trong các lần chạy lại.
  - Source Versioning: Track the exact timestamp of the sync.
  - Phiên bản hóa Nguồn (Source Versioning): Theo dõi chính xác mốc thời gian của quá trình đồng bộ.
- **Handling Constraints**: Implement rate limiting (exponential backoff) for external APIs and backpressure buffers for consumers to prevent system overload.
- **Xử lý Ràng buộc (Constraints)**: Thực hiện giới hạn tỷ lệ (rate limiting) (chờ bù đắp theo cấp số nhân) đối với các API bên ngoài và các bộ đệm áp lực ngược (backpressure buffers) cho phía trình tiêu thụ để ngăn ngừa quá tải hệ thống.

## 4. Transform for AI and Chunking
## 4. Biến đổi dữ liệu cho AI và Phân đoạn (Chunking)
Transformation for AI is heavily optimized for context retrieval.
Việc biến đổi dữ liệu cho AI được tối ưu hóa mạnh mẽ để phục vụ cho truy xuất ngữ cảnh (context retrieval).
- **Data Cleaning**: Address missing values, outliers, duplicates, and encoding issues (enforce UTF-8). Normalize text by stripping HTML and handling whitespace.
- **Làm sạch Dữ liệu**: Xử lý các giá trị bị thiếu, ngoại lệ (outliers), bản ghi trùng lặp và sự cố mã hóa (bắt buộc dùng UTF-8). Chuẩn hóa văn bản bằng cách loại bỏ HTML và xử lý khoảng trắng.
- **Chunking**: Balancing semantic completeness with token limits. 
- **Phân đoạn (Chunking)**: Cân bằng giữa tính trọn vẹn về ngữ nghĩa với giới hạn token.
  - *Too large*: Retrieval becomes ambiguous; wastes token budget.
  - *Quá lớn*: Quá trình truy xuất trở nên mơ hồ; gây lãng phí ngân sách token.
  - *Too small*: Loses vital context, leading to answers missing exceptions.
  - *Quá nhỏ*: Làm mất bối cảnh quan trọng, dẫn đến các câu trả lời bị thiếu những trường hợp ngoại lệ.
- **Metadata Enrichment**: It's crucial to append metadata to chunks (e.g., `chunk_id`, `source_doc_id`, `effective_date`, `owner`). Without metadata, the Agent cannot filter policies by date or department, leading to incorrect citations.
- **Làm giàu Siêu dữ liệu (Metadata Enrichment)**: Việc gắn thêm siêu dữ liệu vào các phân đoạn là vô cùng quan trọng (ví dụ: `chunk_id`, `source_doc_id`, `effective_date`, `owner`). Không có siêu dữ liệu, Agent sẽ không thể lọc chính sách theo ngày tháng hoặc bộ phận, dẫn đến việc trích dẫn sai sót.

## 5. Data Quality: The 6 Dimensions & Gates
## 5. Chất lượng Dữ liệu: 6 Khía cạnh & Các cổng kiểm soát
Data must pass through Quality Gates before being embedded:
Dữ liệu phải vượt qua các Cổng Chất lượng (Quality Gates) trước khi được nhúng (embedded):
1. **Completeness**: No missing critical fields.
1. **Tính đầy đủ (Completeness)**: Không thiếu các trường quan trọng.
2. **Accuracy**: Aligns with ground truth.
2. **Tính chính xác (Accuracy)**: Phù hợp với sự thật chuẩn (ground truth).
3. **Consistency**: Standardized formats across systems.
3. **Tính nhất quán (Consistency)**: Các định dạng được chuẩn hóa trên toàn hệ thống.
4. **Timeliness**: Meets freshness SLAs.
4. **Tính kịp thời (Timeliness)**: Đáp ứng các SLA về tính cập nhật.
5. **Validity**: Adheres to defined schema/contracts.
5. **Tính hợp lệ (Validity)**: Tuân thủ các lược đồ/hợp đồng đã định nghĩa.
6. **Uniqueness**: Deduplication prevents vector store clutter.
6. **Tính duy nhất (Uniqueness)**: Loại bỏ trùng lặp để tránh làm rối vector store.
- **Implementation**: Write pipeline code that actively asserts these conditions (e.g., dropping empty documents or flagging old policies).
- **Triển khai**: Viết mã pipeline (pipeline code) để chủ động kiểm tra các điều kiện này (ví dụ: loại bỏ các tài liệu trống hoặc gắn cờ các chính sách cũ).

## 6. The 5 Pillars of Data Observability
## 6. 5 Trụ cột của Khả năng Quan sát Dữ liệu
Monitoring the pipeline ensures that bad data is intercepted early:
Việc giám sát pipeline đảm bảo rằng dữ liệu bẩn bị chặn lại từ sớm:
1. **Freshness**: Is the data up-to-date?
1. **Tính cập nhật (Freshness)**: Dữ liệu có được cập nhật không?
2. **Distribution**: Are there anomalous shifts in data values or null rates?
2. **Phân phối (Distribution)**: Có bất kỳ sự thay đổi bất thường nào trong giá trị dữ liệu hoặc tỷ lệ lỗi (null rates) không?
3. **Volume**: Is the incoming row count stable?
3. **Khối lượng (Volume)**: Số lượng hàng đầu vào có ổn định không?
4. **Schema**: Have source columns changed unexpectedly?
4. **Lược đồ (Schema)**: Các cột nguồn có bị thay đổi một cách bất ngờ không?
5. **Lineage**: Can an output chunk be traced back to its raw source file?
5. **Nguồn gốc (Lineage)**: Một đoạn mã đầu ra (output chunk) có thể được truy xuất lại tệp nguồn thô của nó không?

## 7. Debugging Agent Hallucinations
## 7. Gỡ lỗi Ảo giác của Agent (Agent Hallucinations)
When an Agent fails, debug through these 5 layers:
Khi Agent gặp lỗi, hãy gỡ lỗi thông qua 5 lớp sau:
1. **Output Layer**: What did the agent say and cite?
1. **Lớp Đầu ra (Output Layer)**: Agent đã nói và trích dẫn điều gì?
2. **Retrieval Layer**: Which top-k chunks were fetched?
2. **Lớp Truy xuất (Retrieval Layer)**: Những đoạn mã (chunks) top-k nào đã được lấy về?
3. **Index Layer**: What embedding model and version was used?
3. **Lớp Chỉ mục (Index Layer)**: Mô hình nhúng (embedding model) và phiên bản nào đã được sử dụng?
4. **Pipeline Layer**: Which pipeline run produced that chunk?
4. **Lớp Pipeline**: Lần chạy pipeline nào đã tạo ra đoạn mã đó?
5. **Source Layer**: Is the original document correct and updated?
5. **Lớp Nguồn (Source Layer)**: Tài liệu gốc có chính xác và được cập nhật không?
- Trace logs must capture `request_id`, `pipeline_run_id`, `retrieved_chunk_ids`, and `source_version`.
- Các bản ghi theo dõi (trace logs) phải ghi lại `request_id`, `pipeline_run_id`, `retrieved_chunk_ids`, và `source_version`.

## 8. ETL Automation & Orchestration
## 8. Tự động hóa ETL & Điều phối (Orchestration)
Orchestrating the pipeline ensures reliable execution and error recovery.
Việc điều phối pipeline đảm bảo thực thi đáng tin cậy và khôi phục lỗi.
- **Tools**:
- **Công cụ (Tools)**:
  - *Apache Airflow*: DAG-based, mature, ideal for complex batch multi-step jobs.
  - *Apache Airflow*: Dựa trên DAG, trưởng thành, lý tưởng cho các tác vụ hàng loạt (batch) nhiều bước phức tạp.
  - *Prefect*: Python-native, less boilerplate, great for rapid development.
  - *Prefect*: Hỗ trợ tốt Python (Python-native), ít mã rườm rà (boilerplate), tuyệt vời cho phát triển nhanh chóng.
  - *Dagster*: Asset-centric, excellent for data-heavy teams needing built-in lineage.
  - *Dagster*: Tập trung vào tài sản (Asset-centric), xuất sắc cho các nhóm chuyên về dữ liệu cần nguồn gốc (lineage) được tích hợp sẵn.
- **Best Practices**:
- **Các Phương pháp Thực hành Tốt nhất (Best Practices)**:
  - Implement idempotency to allow safe retries.
  - Áp dụng tính Lặp lại không đổi (idempotency) để cho phép thử lại (retries) an toàn.
  - Use Dead Letter Queues (DLQ) for failed records.
  - Sử dụng Hàng đợi Tin nhắn Lỗi (DLQ) cho các bản ghi bị lỗi.
  - Set up alerts for SLA breaches and quality gate failures.
  - Thiết lập cảnh báo cho các vi phạm SLA và các lỗi cổng chất lượng (quality gate).
  - Smoke test retrieval automatically after updating the vector store.
  - Tự động thực hiện bài kiểm tra cơ bản (Smoke test) cho việc truy xuất sau khi cập nhật vector store.
