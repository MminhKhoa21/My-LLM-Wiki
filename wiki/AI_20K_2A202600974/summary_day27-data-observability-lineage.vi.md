---
type: summary
title: "Summary of day27-data-observability-lineage.pdf"
description: "Tổng hợp kiến thức về Data Observability, 7 chiều đo lường chất lượng dữ liệu, Data Contracts, Lineage và các thách thức trong hạ tầng AI."
tags: [ai, 20k, day27]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/27/day27-data-observability-lineage.pdf"]
---

# Tóm tắt: Data Observability & Lineage

## 1. Tại sao cần quan sát dữ liệu (Data Observability)?
- **Sự khác biệt cốt lõi:** Việc giám sát hệ thống (System Monitoring) như đo CPU, RAM, độ trễ không giúp bắt lỗi về nội dung dữ liệu. Một pipeline báo "thành công" vẫn có thể xuất ra dữ liệu sai. Schema checks (kiểm tra cấu trúc) chỉ phát hiện được khoảng 7.8% sự cố thật.
- **Data Downtime:** Là chỉ số KPIs cốt lõi của chất lượng dữ liệu, đo bằng thời gian từ lúc phát hiện lỗi đến khi sửa xong. Công thức: $N \times (TTD + TTR)$.
- **Hậu quả:** Dữ liệu sai gây tốn kém thời gian dọn dẹp (chiếm ~40% thời gian của Data Engineer) và dẫn đến thiệt hại tài chính thật sự nếu đưa vào model dự đoán.

## 2. 7 Chiều của Data Observability
Từ 5 trụ cột gốc của Monte Carlo, hệ thống được mở rộng thành 7 chiều:
1. **Freshness (Độ tươi):** Dữ liệu có mới không? Trễ bao lâu?
2. **Volume (Khối lượng):** Có đủ số dòng (records) không? Có bị đột biến giảm/tăng không?
3. **Distribution (Phân phối):** Giá trị có nằm trong khoảng hợp lý? Có outlier (dữ liệu ngoại lai) không?
4. **Schema (Cấu trúc):** Cột có bị đổi tên/đổi kiểu dữ liệu không?
5. **Lineage (Truy vết):** Dữ liệu đến từ đâu và tác động đến báo cáo/model nào?
6. **Contract (Hợp đồng):** Có đúng theo các cam kết ban đầu (Data Contract) hay không?
7. **Trust (Sự tin cậy):** Điểm tin cậy tổng hợp của bộ dữ liệu.

## 3. Công cụ & Hệ sinh thái
- **Công cụ OSS (Mã nguồn mở):**
  - **Great Expectations (GX 1.0):** Xác thực dữ liệu qua Python API.
  - **Soda Core 4.0:** Định nghĩa quality rules thông qua "Contracts".
  - **Pandera:** Dùng validate ở biên Python DataFrame.
  - **dbt-expectations / dbt unit tests:** Dành cho các hệ thống dùng dbt.
- **SaaS (Rules vs ML):** Monte Carlo, Anomalo, Bigeye... sử dụng Machine Learning để tự động phát hiện bất thường thay vì tạo ra các quy tắc/ngưỡng tĩnh (rules) để tránh các cảnh báo giả.

## 4. Bắt bất thường (Anomaly & Drift Detection)
- Dùng các khoảng ngưỡng động hoặc phân tích phân phối thay vì mức tĩnh. Decompose-then-detect (loại bỏ trend & seasonality trước khi cảnh báo) để giảm báo động giả.
- Đo khoảng cách phân phối với các công thức: PSI, Wasserstein, KS, JS, MMD.

## 5. Data Contracts (Hợp đồng dữ liệu)
- **Chuẩn ODCS (Open Data Contract Standard):** Mô tả schema, chất lượng, SLA, tính sở hữu... dưới dạng YAML (ví dụ v3.1.0).
- Data Contracts cần được thực thi qua 3 tầng (Shift-left CI gate, streaming runtime, post-ingest batch) chứ không chỉ nằm trên Catalog (kho lưu trữ dạng text).

## 6. Lineage (Truy xuất nguồn gốc)
- **OpenLineage:** Chuẩn hóa JSON mô tả luồng sự kiện lineage. Quality (chất lượng dữ liệu) là một thuộc tính gắn trên các bước của lineage.
- **Truy vấn đa chiều:** 
  - **Xuôi (Blast radius):** Lỗi này gây tác động tới ai?
  - **Ngược (Root cause):** Dữ liệu sai do xuất phát từ khâu nào?

## 7. AI-Infra (Hạ tầng AI)
- **Feature Stores:** Quản lý *Training-serving skew* (lệch cấu trúc dữ liệu giữa lúc học và lúc chạy thật) và *Point-in-time correctness* (tránh tình trạng nhìn trộm vào tương lai).
- **Embeddings & RAG:** Cần kiểm tra embedding drift (sự thay đổi khoảng cách vector theo thời gian) và tính chất lỗi thời của corpus trong RAG.
- **Telemetry:** Cần theo dõi cả pipeline của LLM, đảm bảo chống nhiễm (contamination) và làm sạch dữ liệu huấn luyện.
