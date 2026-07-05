---
type: overview
title: "Day 10: Data Pipeline & Data Observability"
description: "Quản lý luồng dữ liệu cho hệ thống AI, từ Ingestion đến Transform, và thiết kế Data Observability để phát hiện dữ liệu bẩn sớm."
tags: [ai, 20k, day10, data-pipeline, observability]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/10/Day 10 Data Pipeline and Data Observability.pdf"]
---

# Day 10: Data Pipeline & Data Observability

## Nội dung chính
Bài học đề cập đến phần "mạch máu" của các hệ thống AI: chất lượng dữ liệu và quản lý luồng nạp dữ liệu.
- Vấn đề "Garbage in -> Garbage out": Agent có mạnh đến đâu nhưng nếu dữ liệu đầu vào cũ, sai lệch, thì kết quả sinh ra sẽ mắc lỗi (hallucinate).
- Cần áp dụng Observability từ tầng dữ liệu thay vì đợi user phàn nàn mới kiểm tra.

## Data Pipeline
- Các mô hình kiến trúc luồng dữ liệu: **ETL (Extract, Transform, Load)** vs **ELT**, Batch processing vs Streaming.
- **Ingestion**: Thu thập dữ liệu từ nhiều nguồn khác nhau (Database, External API, File PDF/HTML, Stream Webhooks). Thách thức nằm ở việc quản lý Rate Limit, Timeout, Schema Drift.
- **Transform**: Làm sạch và chuẩn hóa (Deduplication, Date parsing, Unicode normalization). 

## Data Observability
Observability cho Data bao gồm việc đo lường và theo dõi các chỉ số quan trọng nhằm phát hiện bất thường:
- **5 Pillars of Data Observability**:
  1. Freshness (Dữ liệu có cập nhật kịp thời không?)
  2. Distribution (Giá trị phân phối có lệch bất thường không?)
  3. Volume (Số lượng bản ghi thay đổi đột ngột không?)
  4. Schema (Cấu trúc dữ liệu có bị trôi/drift không?)
  5. Lineage (Theo vết dữ liệu từ nguồn đến điểm ra để khoanh vùng lỗi).
- Cảnh báo: Sử dụng các công cụ kiểm tra chất lượng (Data quality as code như Great Expectations). Thay vì dừng toàn bộ hệ thống vì một lỗi nhỏ, có thể áp dụng chiến lược Quarantine/Warn để xử lý sự cố mềm dẻo.

## Triage Incident
Quy trình phát hiện và giải quyết lỗi dữ liệu:
1. **Detect**: Bắt tín hiệu trễ / thiếu (Freshness).
2. **Isolate**: Khoanh vùng sự cố (Volume drop).
3. **Validate**: Xác nhận nguyên nhân (Schema drift / Parse error).
4. **Trace Lineage**: Truy xuất quá trình xử lý để biết bước nào hỏng.
5. **Fix & Rerun**: Xử lý và chạy lại pipeline với idempotency (an toàn khi chạy lại).
