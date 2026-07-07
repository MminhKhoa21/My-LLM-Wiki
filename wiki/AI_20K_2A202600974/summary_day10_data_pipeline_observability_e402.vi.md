---
type: summary
title: "Summary: Day 10 Data Pipeline Observability E402"
description: "Detailed summary of the VinUniversity AICB Day 10 lecture focusing on Data Pipeline fundamentals, ETL/ELT, Observability pillars, and Orchestration."
tags: [data-pipeline, observability, etl, elt, orchestration, rag]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/10/Day10 data pipeline observability E402.pdf"]
---

# Tóm tắt: Ngày 10 - Data Pipeline Observability E402

Tài liệu này tóm tắt bài giảng Giai đoạn 1 AICB của Đại học VinUni (2026) về Data Pipelines và Data Observability. Nó khám phá lý do tại sao data pipelines lại là nền tảng của mọi sản phẩm AI, trình bày chi tiết về thu thập dữ liệu (ingestion), biến đổi (transformation), các cổng chất lượng (quality gates), và điều phối (orchestration).

## 1. Tại sao Data Pipelines là Nền tảng cho AI
- **Đầu tư Thời gian**: 60–80% thời gian của dự án AI thực tế được dành cho công việc liên quan đến dữ liệu (thu thập, làm sạch, pipelines, giám sát), chứ không phải là xây dựng mô hình.
- **Rác Vào, Rác Ra (Garbage In, Garbage Out)**: Một RAG agent xuất sắc vẫn sẽ bị ảo giác nếu vector store của nó chứa dữ liệu bẩn.
- **Sự Khác biệt Cốt lõi**: Trong BI truyền thống, dữ liệu hỏng đồng nghĩa với một con số sai trên bảng điều khiển. Trong AI, dữ liệu hỏng có nghĩa là Agent thực hiện hành động sai hoặc đưa ra lời khuyên không chính xác trực tiếp cho người dùng.

## 2. Các Kiến thức Cơ bản về Data Pipeline (ETL vs. ELT)
Một ngăn xếp (stack) dữ liệu AI tiêu chuẩn di chuyển từ Nguồn (Sources) -> Pipeline -> Lưu trữ (Storage) -> Phục vụ (Serving) -> Agent.
- **ETL (Trích xuất, Biến đổi, Tải)**: Dữ liệu được biến đổi *trước khi* đưa vào kho. Lý tưởng khi dữ liệu mang tính nhạy cảm và cần che giấu PII, hoặc khi lược đồ (schema) có độ ổn định cao.
- **ELT (Trích xuất, Tải, Biến đổi)**: Dữ liệu thô được đưa vào hồ/kho dữ liệu trước và được biến đổi sau. Lý tưởng cho việc xử lý dữ liệu lớn (big data), nhiều nguồn đa dạng và cho phép dễ dàng chạy lại/điền bù (replay/backfilling) dữ liệu thô khi thử nghiệm với các chiến lược phân đoạn (chunking) mới.
- **Xử lý Hàng loạt (Batch) vs. Xử lý Luồng (Streaming)**:
  - *Batch*: Xử lý theo lịch trình (hàng giờ/hàng ngày). Chi phí thấp, độ trễ cao.
  - *Streaming*: Xử lý thời gian thực. Độ trễ thấp, nhưng độ phức tạp và chi phí cao hơn.

## 3. Chiến lược Thu thập Dữ liệu (Ingestion Strategies)
Quá trình thu thập (Ingestion) lấy dữ liệu từ các DB có Cấu trúc (PostgreSQL qua CDC), Tệp Phi cấu trúc (PDFs, HTML), và Luồng Sự kiện (Kafka, Webhooks).
- **Yêu cầu Chính đối với Thu thập Dữ liệu AI**:
  - Đồng bộ Tăng dần (Incremental Syncs): Chỉ lấy những gì đã thay đổi.
  - Cập nhật Không đổi (Idempotent Upserts): Ngăn chặn việc phân đoạn (chunking) lặp lại trong các lần chạy lại.
  - Phiên bản hóa Nguồn (Source Versioning): Theo dõi chính xác mốc thời gian của quá trình đồng bộ.
- **Xử lý Ràng buộc (Constraints)**: Thực hiện giới hạn tỷ lệ (rate limiting) (chờ bù đắp theo cấp số nhân) đối với các API bên ngoài và các bộ đệm áp lực ngược (backpressure buffers) cho phía trình tiêu thụ để ngăn ngừa quá tải hệ thống.

## 4. Biến đổi dữ liệu cho AI và Phân đoạn (Chunking)
Việc biến đổi dữ liệu cho AI được tối ưu hóa mạnh mẽ để phục vụ cho truy xuất ngữ cảnh (context retrieval).
- **Làm sạch Dữ liệu**: Xử lý các giá trị bị thiếu, ngoại lệ (outliers), bản ghi trùng lặp và sự cố mã hóa (bắt buộc dùng UTF-8). Chuẩn hóa văn bản bằng cách loại bỏ HTML và xử lý khoảng trắng.
- **Phân đoạn (Chunking)**: Cân bằng giữa tính trọn vẹn về ngữ nghĩa với giới hạn token.
  - *Quá lớn*: Quá trình truy xuất trở nên mơ hồ; gây lãng phí ngân sách token.
  - *Quá nhỏ*: Làm mất bối cảnh quan trọng, dẫn đến các câu trả lời bị thiếu những trường hợp ngoại lệ.
- **Làm giàu Siêu dữ liệu (Metadata Enrichment)**: Việc gắn thêm siêu dữ liệu vào các phân đoạn là vô cùng quan trọng (ví dụ: `chunk_id`, `source_doc_id`, `effective_date`, `owner`). Không có siêu dữ liệu, Agent sẽ không thể lọc chính sách theo ngày tháng hoặc bộ phận, dẫn đến việc trích dẫn sai sót.

## 5. Chất lượng Dữ liệu: 6 Khía cạnh & Các cổng kiểm soát
Dữ liệu phải vượt qua các Cổng Chất lượng (Quality Gates) trước khi được nhúng (embedded):
1. **Tính đầy đủ (Completeness)**: Không thiếu các trường quan trọng.
2. **Tính chính xác (Accuracy)**: Phù hợp với sự thật chuẩn (ground truth).
3. **Tính nhất quán (Consistency)**: Các định dạng được chuẩn hóa trên toàn hệ thống.
4. **Tính kịp thời (Timeliness)**: Đáp ứng các SLA về tính cập nhật.
5. **Tính hợp lệ (Validity)**: Tuân thủ các lược đồ/hợp đồng đã định nghĩa.
6. **Tính duy nhất (Uniqueness)**: Loại bỏ trùng lặp để tránh làm rối vector store.
- **Triển khai**: Viết mã pipeline (pipeline code) để chủ động kiểm tra các điều kiện này (ví dụ: loại bỏ các tài liệu trống hoặc gắn cờ các chính sách cũ).

## 6. 5 Trụ cột của Khả năng Quan sát Dữ liệu
Việc giám sát pipeline đảm bảo rằng dữ liệu bẩn bị chặn lại từ sớm:
1. **Tính cập nhật (Freshness)**: Dữ liệu có được cập nhật không?
2. **Phân phối (Distribution)**: Có bất kỳ sự thay đổi bất thường nào trong giá trị dữ liệu hoặc tỷ lệ lỗi (null rates) không?
3. **Khối lượng (Volume)**: Số lượng hàng đầu vào có ổn định không?
4. **Lược đồ (Schema)**: Các cột nguồn có bị thay đổi một cách bất ngờ không?
5. **Nguồn gốc (Lineage)**: Một đoạn mã đầu ra (output chunk) có thể được truy xuất lại tệp nguồn thô của nó không?

## 7. Gỡ lỗi Ảo giác của Agent (Agent Hallucinations)
Khi Agent gặp lỗi, hãy gỡ lỗi thông qua 5 lớp sau:
1. **Lớp Đầu ra (Output Layer)**: Agent đã nói và trích dẫn điều gì?
2. **Lớp Truy xuất (Retrieval Layer)**: Những đoạn mã (chunks) top-k nào đã được lấy về?
3. **Lớp Chỉ mục (Index Layer)**: Mô hình nhúng (embedding model) và phiên bản nào đã được sử dụng?
4. **Lớp Pipeline**: Lần chạy pipeline nào đã tạo ra đoạn mã đó?
5. **Lớp Nguồn (Source Layer)**: Tài liệu gốc có chính xác và được cập nhật không?
- Các bản ghi theo dõi (trace logs) phải ghi lại `request_id`, `pipeline_run_id`, `retrieved_chunk_ids`, và `source_version`.

## 8. Tự động hóa ETL & Điều phối (Orchestration)
Việc điều phối pipeline đảm bảo thực thi đáng tin cậy và khôi phục lỗi.
- **Công cụ (Tools)**:
  - *Apache Airflow*: Dựa trên DAG, trưởng thành, lý tưởng cho các tác vụ hàng loạt (batch) nhiều bước phức tạp.
  - *Prefect*: Hỗ trợ tốt Python (Python-native), ít mã rườm rà (boilerplate), tuyệt vời cho phát triển nhanh chóng.
  - *Dagster*: Tập trung vào tài sản (Asset-centric), xuất sắc cho các nhóm chuyên về dữ liệu cần nguồn gốc (lineage) được tích hợp sẵn.
- **Các Phương pháp Thực hành Tốt nhất (Best Practices)**:
  - Áp dụng tính Lặp lại không đổi (idempotency) để cho phép thử lại (retries) an toàn.
  - Sử dụng Hàng đợi Tin nhắn Lỗi (DLQ) cho các bản ghi bị lỗi.
  - Thiết lập cảnh báo cho các vi phạm SLA và các lỗi cổng chất lượng (quality gate).
  - Tự động thực hiện bài kiểm tra cơ bản (Smoke test) cho việc truy xuất sau khi cập nhật vector store.
