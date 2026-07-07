---
type: summary
title: "Summary: Day 10 Data Pipeline and Data Observability"
description: "A detailed summary of the Day 10 lecture covering Data Pipeline architecture, Data Quality, and Observability for AI systems."
tags: [data-pipeline, observability, etl, data-quality, ai-agent, rag]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/10/Day 10 Data Pipeline and Data Observability.pdf"]
---

# Summary: Day 10 Data Pipeline and Data Observability
# Tóm tắt: Ngày 10 - Data Pipeline và Data Observability

This document provides a comprehensive summary of the lecture "Data Pipeline & Data Observability" from Day 10 of the AI in Action course. It addresses the "garbage in, garbage out" problem in AI systems by focusing on ETL processes, data quality, and system observability before data reaches the Agent or Vector Store.
Tài liệu này cung cấp bản tóm tắt toàn diện về bài giảng "Data Pipeline & Data Observability" từ Ngày 10 của khóa học AI in Action. Bài giảng giải quyết vấn đề "rác vào, rác ra" (garbage in, garbage out) trong các hệ thống AI bằng cách tập trung vào các quy trình ETL, chất lượng dữ liệu và khả năng quan sát hệ thống (observability) trước khi dữ liệu đến Agent hoặc Vector Store.

## 1. The Core Problem: Garbage In, Garbage Out
## 1. Vấn đề Cốt lõi: Rác Vào, Rác Ra (Garbage In, Garbage Out)
Even a powerful AI Agent will hallucinate or provide incorrect answers if the underlying data is dirty, outdated (stale), or missing context. 
Ngay cả một AI Agent mạnh mẽ cũng sẽ bị ảo giác hoặc đưa ra câu trả lời sai nếu dữ liệu cơ sở bị bẩn, lỗi thời (cũ) hoặc thiếu ngữ cảnh.
- **Key Insight**: Do not debug the AI model before debugging the data pipeline.
- **Quan điểm chính**: Đừng gỡ lỗi (debug) mô hình AI trước khi gỡ lỗi hệ thống dữ liệu (data pipeline).
- **Observability**: The goal is to detect issues (e.g., failed syncs, stale data) *before* users complain.
- **Khả năng quan sát (Observability)**: Mục tiêu là phát hiện sớm các sự cố (ví dụ: quá trình đồng bộ thất bại, dữ liệu cũ) *trước khi* người dùng phàn nàn.
- **Example Scenario**: A data pipeline fails to sync the latest refund policy. The vector store retains the old policy, and the Agent confidently outputs outdated information (e.g., "14 days" instead of "7 days").
- **Tình huống ví dụ**: Data pipeline không đồng bộ được chính sách hoàn tiền mới nhất. Vector store vẫn giữ chính sách cũ và Agent tự tin đưa ra thông tin lỗi thời (ví dụ: "14 ngày" thay vì "7 ngày").

## 2. RACI and Roles in Data Pipelines
## 2. RACI và Các vai trò trong Data Pipelines
Managing an AI data pipeline requires clear boundaries and responsibilities to avoid overloading the AI Engineer:
Việc quản lý một AI data pipeline đòi hỏi ranh giới và trách nhiệm rõ ràng để tránh làm quá tải Kỹ sư AI (AI Engineer):
- **AI / Applied Data**: Define data contracts for the agent's corpus and conduct before/after evaluations.
- **AI / Dữ liệu Ứng dụng (Applied Data)**: Xác định các hợp đồng dữ liệu (data contracts) cho kho dữ liệu (corpus) của agent và thực hiện đánh giá trước/sau.
- **Data Engineer**: Ensure robust ingestion, data modeling, and pipeline SLA adherence.
- **Kỹ sư Dữ liệu (Data Engineer)**: Đảm bảo khả năng thu thập dữ liệu (ingestion) mạnh mẽ, mô hình hóa dữ liệu và tuân thủ các cam kết dịch vụ (SLA) của pipeline.
- **SRE / Platform**: Manage alerts, on-call runbooks, and quota/secrets.
- **SRE / Nền tảng (Platform)**: Quản lý cảnh báo, quy trình xử lý sự cố trực ban (on-call runbooks) và hạn ngạch (quota)/bảo mật (secrets).
- **Product / SME (Subject Matter Expert)**: Define the "correct" policy and sign-off on the source of truth.
- **Sản phẩm (Product) / Chuyên gia (SME)**: Xác định chính sách "chuẩn xác" và phê duyệt nguồn dữ liệu gốc (source of truth).

## 3. Data Pipeline Architecture: ETL vs. ELT & Batch vs. Streaming
## 3. Kiến trúc Data Pipeline: ETL vs. ELT & Batch vs. Streaming
A data pipeline moves data from sources (DB, API, Files) to serving layers (Vector Store, Agent).
Một data pipeline di chuyển dữ liệu từ các nguồn (DB, API, Files) sang các lớp phục vụ (Vector Store, Agent).
- **ETL (Extract, Transform, Load)**: Transform data before loading. Good for masking PII before it enters the warehouse.
- **ETL (Trích xuất, Biến đổi, Tải - Extract, Transform, Load)**: Biến đổi dữ liệu trước khi tải. Tốt cho việc che giấu thông tin nhận dạng cá nhân (PII) trước khi dữ liệu vào kho.
- **ELT (Extract, Load, Transform)**: Load data first, transform later. Suitable for large batch jobs like monthly CSVs.
- **ELT (Trích xuất, Tải, Biến đổi - Extract, Load, Transform)**: Tải dữ liệu trước, biến đổi sau. Phù hợp cho các tác vụ xử lý hàng loạt (batch) lớn như các tệp CSV hàng tháng.
- **Batch**: Processing data in scheduled blocks (e.g., nightly PDF syncs).
- **Xử lý Hàng loạt (Batch)**: Xử lý dữ liệu theo các khối theo lịch trình (ví dụ: đồng bộ PDF hàng đêm).
- **Streaming**: Processing data continuously (e.g., webhook for P1 support tickets).
- **Xử lý Luồng (Streaming)**: Xử lý dữ liệu liên tục (ví dụ: webhook cho các ticket hỗ trợ ưu tiên P1).

## 4. Ingestion Layer and Risks
## 4. Lớp Thu thập Dữ liệu (Ingestion Layer) và Rủi ro
Ingestion from diverse sources (PostgreSQL, APIs, PDFs) involves unique failure points:
Thu thập dữ liệu từ các nguồn đa dạng (PostgreSQL, APIs, PDFs) có những điểm dễ xảy ra sự cố (failure points) đặc thù:
- **PostgreSQL**: Handled via CDC (Change Data Capture) or snapshots. Risks: CDC lag, schema drift.
- **PostgreSQL**: Xử lý thông qua CDC (Thu thập Thay đổi Dữ liệu) hoặc ảnh chụp (snapshots). Rủi ro: độ trễ CDC, sai lệch lược đồ (schema drift).
- **External API**: Handled via polling or pagination. Risks: Rate limits (HTTP 429), auth issues, checkpoint stalls. Mitigation involves exponential backoff, jitter, and pagination cursors.
- **API Ngoài**: Xử lý thông qua hỏi vòng (polling) hoặc phân trang (pagination). Rủi ro: Giới hạn lưu lượng (HTTP 429), vấn đề xác thực, gián đoạn tại các điểm lưu (checkpoint stalls). Biện pháp giảm thiểu bao gồm chờ bù đắp theo cấp số nhân (exponential backoff), độ trễ ngẫu nhiên (jitter), và con trỏ phân trang (pagination cursors).
- **PDF / HTML**: Handled via parsers and OCR. Risks: Bad OCR confidence, missing metadata. Mitigation requires content hashing and logical versioning.
- **PDF / HTML**: Xử lý thông qua trình phân tích cú pháp (parsers) và OCR (Nhận dạng Ký tự Quang học). Rủi ro: Độ tin cậy OCR kém, thiếu siêu dữ liệu (metadata). Biện pháp giảm thiểu đòi hỏi hàm băm nội dung (content hashing) và phiên bản hóa logic (logical versioning).
- **Event Streams/Webhooks**: Risks include consumer lag and backpressure. Recommended architecture uses a Message Queue + Buffer (Redis/SQS) feeding into a Consumer (Worker) with a Dead-Letter Queue (DLQ) for poison messages.
- **Luồng Sự kiện (Event Streams)/Webhooks**: Rủi ro bao gồm độ trễ của trình tiêu thụ (consumer lag) và áp lực ngược (backpressure). Kiến trúc được đề xuất sử dụng Hàng đợi Tin nhắn (Message Queue) + Bộ đệm (Buffer - Redis/SQS) cấp dữ liệu cho một Trình tiêu thụ (Consumer/Worker) kèm theo một Hàng đợi Tin nhắn Lỗi (Dead-Letter Queue - DLQ) dành cho các tin nhắn không hợp lệ (poison messages).

## 5. Transformation and Dirty Data Repair
## 5. Biến đổi Dữ liệu và Khắc phục Dữ liệu Bẩn
Transformation is required to clean and normalize data before it reaches the AI agent.
Biến đổi (Transformation) là bước cần thiết để làm sạch và chuẩn hóa dữ liệu trước khi nó đến hệ thống AI agent.
- **Cleaning Rules**: Trim whitespace, parse dates consistently (YYYY-MM-DD UTC), normalize Unicode (NFC), and standardise formats.
- **Quy tắc Làm sạch**: Xóa khoảng trắng thừa (trim whitespace), phân tích ngày tháng đồng nhất (YYYY-MM-DD UTC), chuẩn hóa Unicode (NFC), và tiêu chuẩn hóa các định dạng.
- **Rejection/Quarantine**: Drop empty content, deduplicate based on primary keys, and flag records with missing critical fields (e.g., missing dates) for manual review rather than failing the entire batch.
- **Từ chối/Cách ly (Quarantine)**: Bỏ qua các nội dung trống, loại bỏ dữ liệu trùng lặp dựa trên khóa chính, và gắn cờ các bản ghi bị thiếu các trường dữ liệu quan trọng (ví dụ: thiếu ngày tháng) để kiểm tra thủ công thay vì làm hỏng toàn bộ đợt xử lý (batch).

## 6. Data Quality as Code
## 6. Chất lượng Dữ liệu dưới dạng Code (Data Quality as Code)
Implementing Data Quality checks ensures that only valid data progresses through the pipeline.
Triển khai các bài kiểm tra Chất lượng Dữ liệu đảm bảo rằng chỉ có dữ liệu hợp lệ mới được tiếp tục chuyển trong pipeline.
- **6 Dimensions**:
- **6 Khía cạnh (Dimensions)**:
  1. **Completeness**: Essential fields (like content) must not be null.
  1. **Tính đầy đủ (Completeness)**: Các trường bắt buộc (như nội dung) không được phép trống (null).
  2. **Accuracy**: Dates and facts must align with business truth.
  2. **Tính chính xác (Accuracy)**: Ngày tháng và dữ kiện phải phù hợp với thực tế nghiệp vụ.
  3. **Consistency**: Consistent formats and keys.
  3. **Tính nhất quán (Consistency)**: Các định dạng và khóa (keys) đồng nhất.
  4. **Timeliness**: Data must meet freshness SLAs.
  4. **Tính kịp thời (Timeliness)**: Dữ liệu phải đáp ứng các SLA về tính cập nhật (freshness).
  5. **Validity**: Conformance to schema and data contracts.
  5. **Tính hợp lệ (Validity)**: Tuân thủ theo các lược đồ (schema) và hợp đồng dữ liệu.
  6. **Uniqueness**: No duplicate records.
  6. **Tính duy nhất (Uniqueness)**: Không có các bản ghi trùng lặp.
- **Expectation Suites**: Using tools like Great Expectations to enforce these rules programmatically. Violations can Halt the pipeline, Quarantine the row, or simply Warn the operators depending on severity.
- **Bộ Kiểm tra Kỳ vọng (Expectation Suites)**: Sử dụng các công cụ như Great Expectations để thực thi các quy tắc này một cách lập trình. Các vi phạm có thể làm Dừng (Halt) pipeline, Cách ly (Quarantine) hàng dữ liệu, hoặc đơn giản là Cảnh báo (Warn) người vận hành tùy thuộc vào mức độ nghiêm trọng.

## 7. The 5 Pillars of Data Observability
## 7. 5 Trụ cột của Khả năng Quan sát Dữ liệu (Data Observability)
Observability provides visibility into the pipeline's health to preemptively stop bad data:
Khả năng quan sát cung cấp tầm nhìn rõ ràng về tình trạng (health) của pipeline để chặn trước dữ liệu hỏng:
1. **Freshness**: Is the data updating on time? (e.g., tracking `freshness_hours`).
1. **Tính cập nhật (Freshness)**: Dữ liệu có đang được cập nhật đúng giờ không? (ví dụ: theo dõi `freshness_hours`).
2. **Distribution**: Are there abnormal spikes in null rates or content length?
2. **Phân phối (Distribution)**: Có bất kỳ sự gia tăng bất thường nào về tỷ lệ lỗi (null rates) hoặc độ dài nội dung không?
3. **Volume**: Did the number of ingested records suddenly drop?
3. **Khối lượng (Volume)**: Số lượng bản ghi được nhập vào có bị sụt giảm đột ngột không?
4. **Schema**: Are there breaking changes or schema drifts from the source?
4. **Lược đồ (Schema)**: Có thay đổi gây lỗi (breaking changes) hoặc sai lệch lược đồ (schema drifts) từ nguồn gốc không?
5. **Lineage**: Can an error be traced from the output back to the specific source table or file?
5. **Nguồn gốc (Lineage)**: Một lỗi ở đầu ra có thể được truy xuất ngược lại đúng bảng hoặc tệp nguồn đã gây ra nó không?

## 8. Incident Triage Workflow
## 8. Quy trình Phân loại Sự cố (Incident Triage Workflow)
When an Agent gives a bad answer, follow a structured, time-boxed debugging flow:
Khi một Agent đưa ra câu trả lời không tốt, hãy làm theo một quy trình gỡ lỗi có cấu trúc, giới hạn thời gian (time-boxed):
1. **Detect (0-5 mins)**: Check Freshness and SLA breach metrics.
1. **Phát hiện (0-5 phút)**: Kiểm tra Tính cập nhật (Freshness) và các chỉ số vi phạm SLA.
2. **Isolate (5-12 mins)**: Check Volume drops and error rates by pipeline step.
2. **Cô lập (5-12 phút)**: Kiểm tra việc sụt giảm Khối lượng (Volume) và tỷ lệ lỗi trên mỗi bước của pipeline.
3. **Validate (12-20 mins)**: Look for Schema drift or parsing errors.
3. **Xác nhận (12-20 phút)**: Tìm kiếm sự sai lệch Lược đồ (Schema drift) hoặc lỗi phân tích cú pháp (parsing errors).
4. **Trace Lineage**: Trace the exact source file and step that failed.
4. **Truy xuất Nguồn gốc (Trace Lineage)**: Truy ngược lại chính xác tệp nguồn và bước xử lý đã gặp lỗi.
5. **Fix & Rerun**: Fix the root cause and rerun the pipeline safely utilizing **Idempotency** (rerunning should not create duplicate vectors).
5. **Sửa lỗi & Chạy lại**: Khắc phục nguyên nhân gốc rễ và chạy lại pipeline một cách an toàn thông qua tính **Lặp lại Không đổi (Idempotency)** (chạy lại không nên tạo ra các vector trùng lặp).

## 9. Orchestration and Idempotency
## 9. Điều phối (Orchestration) và Tính Lặp lại Không đổi (Idempotency)
Pipelines must be robust and re-runnable.
Các pipelines phải mạnh mẽ và có khả năng chạy lại được (re-runnable).
- **Idempotency**: Essential for safe reruns. Use natural keys (upsert by doc_id + version) instead of random UUIDs. Delete-then-insert within a transaction, or swap staging collections.
- **Tính Lặp lại Không đổi (Idempotency)**: Yếu tố then chốt cho các lần chạy lại an toàn. Hãy sử dụng các khóa tự nhiên (upsert theo doc_id + phiên bản) thay vì các UUID ngẫu nhiên. Thực hiện xóa-rồi-thêm (delete-then-insert) bên trong một giao dịch (transaction), hoặc hoán đổi các tập hợp ở môi trường trung gian (staging collections).
- **Orchestrators** (e.g., Airflow, Prefect, Dagster): Manage Directed Acyclic Graphs (DAGs) of tasks, handling triggers, retry policies (backoffs), DLQs, and alerting for SLA breaches.
- **Công cụ Điều phối (Orchestrators)** (ví dụ: Airflow, Prefect, Dagster): Quản lý các Đồ thị Rời rạc Có hướng (DAGs) của các tác vụ, xử lý các trình kích hoạt (triggers), chính sách thử lại (backoffs), DLQs, và cảnh báo đối với các vi phạm SLA.

## 10. Service Level Indicators (SLIs) for RAG
## 10. Chỉ số Đo lường Dịch vụ (SLIs) cho RAG
Connect data observability directly to user experience:
Kết nối khả năng quan sát dữ liệu trực tiếp vào trải nghiệm người dùng:
- **Citation Freshness**: Average age of the chunks cited by the Agent.
- **Tính cập nhật Trích dẫn (Citation Freshness)**: Độ tuổi trung bình của các phân đoạn dữ liệu (chunks) được Agent trích dẫn.
- **Grounding Rate**: Percentage of answers strictly grounded in retrieved context.
- **Tỷ lệ Căn cứ (Grounding Rate)**: Tỷ lệ phần trăm các câu trả lời thực sự dựa trên bối cảnh đã truy xuất.
- **Retrieval hit@k**: Quality of retrieval on a golden test set.
- **Chất lượng Truy xuất (Retrieval hit@k)**: Chất lượng truy xuất trên một tập kiểm thử đạt chuẩn (golden test set).
- **Pipeline Latency**: Time from source ingestion to vector publish. 
- **Độ trễ Pipeline (Pipeline Latency)**: Thời gian từ khi thu thập nguồn dữ liệu cho đến khi phát hành ra vector.
