---
type: summary
title: "Summary: Day 10 Data Pipeline and Data Observability"
description: "A detailed summary of the Day 10 lecture covering Data Pipeline architecture, Data Quality, and Observability for AI systems."
tags: [data-pipeline, observability, etl, data-quality, ai-agent, rag]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/10/Day 10 Data Pipeline and Data Observability.pdf"]
---

# Tóm tắt: Ngày 10 - Data Pipeline và Data Observability

Tài liệu này cung cấp bản tóm tắt toàn diện về bài giảng "Data Pipeline & Data Observability" từ Ngày 10 của khóa học AI in Action. Bài giảng giải quyết vấn đề "rác vào, rác ra" (garbage in, garbage out) trong các hệ thống AI bằng cách tập trung vào các quy trình ETL, chất lượng dữ liệu và khả năng quan sát hệ thống (observability) trước khi dữ liệu đến Agent hoặc Vector Store.

## 1. Vấn đề Cốt lõi: Rác Vào, Rác Ra (Garbage In, Garbage Out)
Ngay cả một AI Agent mạnh mẽ cũng sẽ bị ảo giác hoặc đưa ra câu trả lời sai nếu dữ liệu cơ sở bị bẩn, lỗi thời (cũ) hoặc thiếu ngữ cảnh.
- **Quan điểm chính**: Đừng gỡ lỗi (debug) mô hình AI trước khi gỡ lỗi hệ thống dữ liệu (data pipeline).
- **Khả năng quan sát (Observability)**: Mục tiêu là phát hiện sớm các sự cố (ví dụ: quá trình đồng bộ thất bại, dữ liệu cũ) *trước khi* người dùng phàn nàn.
- **Tình huống ví dụ**: Data pipeline không đồng bộ được chính sách hoàn tiền mới nhất. Vector store vẫn giữ chính sách cũ và Agent tự tin đưa ra thông tin lỗi thời (ví dụ: "14 ngày" thay vì "7 ngày").

## 2. RACI và Các vai trò trong Data Pipelines
Việc quản lý một AI data pipeline đòi hỏi ranh giới và trách nhiệm rõ ràng để tránh làm quá tải Kỹ sư AI (AI Engineer):
- **AI / Dữ liệu Ứng dụng (Applied Data)**: Xác định các hợp đồng dữ liệu (data contracts) cho kho dữ liệu (corpus) của agent và thực hiện đánh giá trước/sau.
- **Kỹ sư Dữ liệu (Data Engineer)**: Đảm bảo khả năng thu thập dữ liệu (ingestion) mạnh mẽ, mô hình hóa dữ liệu và tuân thủ các cam kết dịch vụ (SLA) của pipeline.
- **SRE / Nền tảng (Platform)**: Quản lý cảnh báo, quy trình xử lý sự cố trực ban (on-call runbooks) và hạn ngạch (quota)/bảo mật (secrets).
- **Sản phẩm (Product) / Chuyên gia (SME)**: Xác định chính sách "chuẩn xác" và phê duyệt nguồn dữ liệu gốc (source of truth).

## 3. Kiến trúc Data Pipeline: ETL vs. ELT & Batch vs. Streaming
Một data pipeline di chuyển dữ liệu từ các nguồn (DB, API, Files) sang các lớp phục vụ (Vector Store, Agent).
- **ETL (Trích xuất, Biến đổi, Tải - Extract, Transform, Load)**: Biến đổi dữ liệu trước khi tải. Tốt cho việc che giấu thông tin nhận dạng cá nhân (PII) trước khi dữ liệu vào kho.
- **ELT (Trích xuất, Tải, Biến đổi - Extract, Load, Transform)**: Tải dữ liệu trước, biến đổi sau. Phù hợp cho các tác vụ xử lý hàng loạt (batch) lớn như các tệp CSV hàng tháng.
- **Xử lý Hàng loạt (Batch)**: Xử lý dữ liệu theo các khối theo lịch trình (ví dụ: đồng bộ PDF hàng đêm).
- **Xử lý Luồng (Streaming)**: Xử lý dữ liệu liên tục (ví dụ: webhook cho các ticket hỗ trợ ưu tiên P1).

## 4. Lớp Thu thập Dữ liệu (Ingestion Layer) và Rủi ro
Thu thập dữ liệu từ các nguồn đa dạng (PostgreSQL, APIs, PDFs) có những điểm dễ xảy ra sự cố (failure points) đặc thù:
- **PostgreSQL**: Xử lý thông qua CDC (Thu thập Thay đổi Dữ liệu) hoặc ảnh chụp (snapshots). Rủi ro: độ trễ CDC, sai lệch lược đồ (schema drift).
- **API Ngoài**: Xử lý thông qua hỏi vòng (polling) hoặc phân trang (pagination). Rủi ro: Giới hạn lưu lượng (HTTP 429), vấn đề xác thực, gián đoạn tại các điểm lưu (checkpoint stalls). Biện pháp giảm thiểu bao gồm chờ bù đắp theo cấp số nhân (exponential backoff), độ trễ ngẫu nhiên (jitter), và con trỏ phân trang (pagination cursors).
- **PDF / HTML**: Xử lý thông qua trình phân tích cú pháp (parsers) và OCR (Nhận dạng Ký tự Quang học). Rủi ro: Độ tin cậy OCR kém, thiếu siêu dữ liệu (metadata). Biện pháp giảm thiểu đòi hỏi hàm băm nội dung (content hashing) và phiên bản hóa logic (logical versioning).
- **Luồng Sự kiện (Event Streams)/Webhooks**: Rủi ro bao gồm độ trễ của trình tiêu thụ (consumer lag) và áp lực ngược (backpressure). Kiến trúc được đề xuất sử dụng Hàng đợi Tin nhắn (Message Queue) + Bộ đệm (Buffer - Redis/SQS) cấp dữ liệu cho một Trình tiêu thụ (Consumer/Worker) kèm theo một Hàng đợi Tin nhắn Lỗi (Dead-Letter Queue - DLQ) dành cho các tin nhắn không hợp lệ (poison messages).

## 5. Biến đổi Dữ liệu và Khắc phục Dữ liệu Bẩn
Biến đổi (Transformation) là bước cần thiết để làm sạch và chuẩn hóa dữ liệu trước khi nó đến hệ thống AI agent.
- **Quy tắc Làm sạch**: Xóa khoảng trắng thừa (trim whitespace), phân tích ngày tháng đồng nhất (YYYY-MM-DD UTC), chuẩn hóa Unicode (NFC), và tiêu chuẩn hóa các định dạng.
- **Từ chối/Cách ly (Quarantine)**: Bỏ qua các nội dung trống, loại bỏ dữ liệu trùng lặp dựa trên khóa chính, và gắn cờ các bản ghi bị thiếu các trường dữ liệu quan trọng (ví dụ: thiếu ngày tháng) để kiểm tra thủ công thay vì làm hỏng toàn bộ đợt xử lý (batch).

## 6. Chất lượng Dữ liệu dưới dạng Code (Data Quality as Code)
Triển khai các bài kiểm tra Chất lượng Dữ liệu đảm bảo rằng chỉ có dữ liệu hợp lệ mới được tiếp tục chuyển trong pipeline.
- **6 Khía cạnh (Dimensions)**:
  1. **Tính đầy đủ (Completeness)**: Các trường bắt buộc (như nội dung) không được phép trống (null).
  2. **Tính chính xác (Accuracy)**: Ngày tháng và dữ kiện phải phù hợp với thực tế nghiệp vụ.
  3. **Tính nhất quán (Consistency)**: Các định dạng và khóa (keys) đồng nhất.
  4. **Tính kịp thời (Timeliness)**: Dữ liệu phải đáp ứng các SLA về tính cập nhật (freshness).
  5. **Tính hợp lệ (Validity)**: Tuân thủ theo các lược đồ (schema) và hợp đồng dữ liệu.
  6. **Tính duy nhất (Uniqueness)**: Không có các bản ghi trùng lặp.
- **Bộ Kiểm tra Kỳ vọng (Expectation Suites)**: Sử dụng các công cụ như Great Expectations để thực thi các quy tắc này một cách lập trình. Các vi phạm có thể làm Dừng (Halt) pipeline, Cách ly (Quarantine) hàng dữ liệu, hoặc đơn giản là Cảnh báo (Warn) người vận hành tùy thuộc vào mức độ nghiêm trọng.

## 7. 5 Trụ cột của Khả năng Quan sát Dữ liệu (Data Observability)
Khả năng quan sát cung cấp tầm nhìn rõ ràng về tình trạng (health) của pipeline để chặn trước dữ liệu hỏng:
1. **Tính cập nhật (Freshness)**: Dữ liệu có đang được cập nhật đúng giờ không? (ví dụ: theo dõi `freshness_hours`).
2. **Phân phối (Distribution)**: Có bất kỳ sự gia tăng bất thường nào về tỷ lệ lỗi (null rates) hoặc độ dài nội dung không?
3. **Khối lượng (Volume)**: Số lượng bản ghi được nhập vào có bị sụt giảm đột ngột không?
4. **Lược đồ (Schema)**: Có thay đổi gây lỗi (breaking changes) hoặc sai lệch lược đồ (schema drifts) từ nguồn gốc không?
5. **Nguồn gốc (Lineage)**: Một lỗi ở đầu ra có thể được truy xuất ngược lại đúng bảng hoặc tệp nguồn đã gây ra nó không?

## 8. Quy trình Phân loại Sự cố (Incident Triage Workflow)
Khi một Agent đưa ra câu trả lời không tốt, hãy làm theo một quy trình gỡ lỗi có cấu trúc, giới hạn thời gian (time-boxed):
1. **Phát hiện (0-5 phút)**: Kiểm tra Tính cập nhật (Freshness) và các chỉ số vi phạm SLA.
2. **Cô lập (5-12 phút)**: Kiểm tra việc sụt giảm Khối lượng (Volume) và tỷ lệ lỗi trên mỗi bước của pipeline.
3. **Xác nhận (12-20 phút)**: Tìm kiếm sự sai lệch Lược đồ (Schema drift) hoặc lỗi phân tích cú pháp (parsing errors).
4. **Truy xuất Nguồn gốc (Trace Lineage)**: Truy ngược lại chính xác tệp nguồn và bước xử lý đã gặp lỗi.
5. **Sửa lỗi & Chạy lại**: Khắc phục nguyên nhân gốc rễ và chạy lại pipeline một cách an toàn thông qua tính **Lặp lại Không đổi (Idempotency)** (chạy lại không nên tạo ra các vector trùng lặp).

## 9. Điều phối (Orchestration) và Tính Lặp lại Không đổi (Idempotency)
Các pipelines phải mạnh mẽ và có khả năng chạy lại được (re-runnable).
- **Tính Lặp lại Không đổi (Idempotency)**: Yếu tố then chốt cho các lần chạy lại an toàn. Hãy sử dụng các khóa tự nhiên (upsert theo doc_id + phiên bản) thay vì các UUID ngẫu nhiên. Thực hiện xóa-rồi-thêm (delete-then-insert) bên trong một giao dịch (transaction), hoặc hoán đổi các tập hợp ở môi trường trung gian (staging collections).
- **Công cụ Điều phối (Orchestrators)** (ví dụ: Airflow, Prefect, Dagster): Quản lý các Đồ thị Rời rạc Có hướng (DAGs) của các tác vụ, xử lý các trình kích hoạt (triggers), chính sách thử lại (backoffs), DLQs, và cảnh báo đối với các vi phạm SLA.

## 10. Chỉ số Đo lường Dịch vụ (SLIs) cho RAG
Kết nối khả năng quan sát dữ liệu trực tiếp vào trải nghiệm người dùng:
- **Tính cập nhật Trích dẫn (Citation Freshness)**: Độ tuổi trung bình của các phân đoạn dữ liệu (chunks) được Agent trích dẫn.
- **Tỷ lệ Căn cứ (Grounding Rate)**: Tỷ lệ phần trăm các câu trả lời thực sự dựa trên bối cảnh đã truy xuất.
- **Chất lượng Truy xuất (Retrieval hit@k)**: Chất lượng truy xuất trên một tập kiểm thử đạt chuẩn (golden test set).
- **Độ trễ Pipeline (Pipeline Latency)**: Thời gian từ khi thu thập nguồn dữ liệu cho đến khi phát hành ra vector.
