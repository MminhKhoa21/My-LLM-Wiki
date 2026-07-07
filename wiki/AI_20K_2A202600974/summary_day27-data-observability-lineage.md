---
type: summary
title: "Summary of day27-data-observability-lineage.pdf"
description: "Tổng hợp kiến thức về Data Observability, 7 chiều đo lường chất lượng dữ liệu, Data Contracts, Lineage và các thách thức trong hạ tầng AI."
tags: [ai, 20k, day27]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/27/day27-data-observability-lineage.pdf"]
---

# Tóm tắt: Data Observability & Lineage
# Summary: Data Observability & Lineage

## 1. Tại sao cần quan sát dữ liệu (Data Observability)?
## 1. Why do we need Data Observability?
- **Sự khác biệt cốt lõi:** Việc giám sát hệ thống (System Monitoring) như đo CPU, RAM, độ trễ không giúp bắt lỗi về nội dung dữ liệu. Một pipeline báo "thành công" vẫn có thể xuất ra dữ liệu sai. Schema checks (kiểm tra cấu trúc) chỉ phát hiện được khoảng 7.8% sự cố thật.
- **Core difference:** System Monitoring like measuring CPU, RAM, latency does not help catch errors in data content. A "successful" pipeline can still output wrong data. Schema checks only detect about 7.8% of real incidents.
- **Data Downtime:** Là chỉ số KPIs cốt lõi của chất lượng dữ liệu, đo bằng thời gian từ lúc phát hiện lỗi đến khi sửa xong. Công thức: $N \times (TTD + TTR)$.
- **Data Downtime:** The core KPI of data quality, measured by the time from when an error is detected until it is fixed. Formula: $N \times (TTD + TTR)$.
- **Hậu quả:** Dữ liệu sai gây tốn kém thời gian dọn dẹp (chiếm ~40% thời gian của Data Engineer) và dẫn đến thiệt hại tài chính thật sự nếu đưa vào model dự đoán.
- **Consequences:** Incorrect data costs time to clean up (accounting for ~40% of Data Engineer's time) and leads to real financial damage if fed into prediction models.

## 2. 7 Chiều của Data Observability
## 2. The 7 Dimensions of Data Observability
Từ 5 trụ cột gốc của Monte Carlo, hệ thống được mở rộng thành 7 chiều:
From the original 5 pillars of Monte Carlo, the system is expanded to 7 dimensions:
1. **Freshness (Độ tươi):** Dữ liệu có mới không? Trễ bao lâu?
1. **Freshness:** Is the data new? How long is it delayed?
2. **Volume (Khối lượng):** Có đủ số dòng (records) không? Có bị đột biến giảm/tăng không?
2. **Volume:** Are there enough records? Is there a sudden decrease/increase?
3. **Distribution (Phân phối):** Giá trị có nằm trong khoảng hợp lý? Có outlier (dữ liệu ngoại lai) không?
3. **Distribution:** Are the values within a reasonable range? Are there any outliers?
4. **Schema (Cấu trúc):** Cột có bị đổi tên/đổi kiểu dữ liệu không?
4. **Schema:** Have the columns been renamed/changed data types?
5. **Lineage (Truy vết):** Dữ liệu đến từ đâu và tác động đến báo cáo/model nào?
5. **Lineage:** Where does the data come from and which report/model does it affect?
6. **Contract (Hợp đồng):** Có đúng theo các cam kết ban đầu (Data Contract) hay không?
6. **Contract:** Is it in accordance with the initial commitments (Data Contract)?
7. **Trust (Sự tin cậy):** Điểm tin cậy tổng hợp của bộ dữ liệu.
7. **Trust:** The aggregated trust score of the dataset.

## 3. Công cụ & Hệ sinh thái
## 3. Tools & Ecosystem
- **Công cụ OSS (Mã nguồn mở):**
- **OSS Tools (Open Source Software):**
  - **Great Expectations (GX 1.0):** Xác thực dữ liệu qua Python API.
  - **Great Expectations (GX 1.0):** Data validation via Python API.
  - **Soda Core 4.0:** Định nghĩa quality rules thông qua "Contracts".
  - **Soda Core 4.0:** Defining quality rules via "Contracts".
  - **Pandera:** Dùng validate ở biên Python DataFrame.
  - **Pandera:** Used for validation at the Python DataFrame boundary.
  - **dbt-expectations / dbt unit tests:** Dành cho các hệ thống dùng dbt.
  - **dbt-expectations / dbt unit tests:** For systems using dbt.
- **SaaS (Rules vs ML):** Monte Carlo, Anomalo, Bigeye... sử dụng Machine Learning để tự động phát hiện bất thường thay vì tạo ra các quy tắc/ngưỡng tĩnh (rules) để tránh các cảnh báo giả.
- **SaaS (Rules vs ML):** Monte Carlo, Anomalo, Bigeye... use Machine Learning to automatically detect anomalies instead of creating static rules/thresholds to avoid false alerts.

## 4. Bắt bất thường (Anomaly & Drift Detection)
## 4. Anomaly & Drift Detection
- Dùng các khoảng ngưỡng động hoặc phân tích phân phối thay vì mức tĩnh. Decompose-then-detect (loại bỏ trend & seasonality trước khi cảnh báo) để giảm báo động giả.
- Use dynamic threshold ranges or distribution analysis instead of static levels. Decompose-then-detect (remove trend & seasonality before alerting) to reduce false alarms.
- Đo khoảng cách phân phối với các công thức: PSI, Wasserstein, KS, JS, MMD.
- Measure distribution distance with formulas: PSI, Wasserstein, KS, JS, MMD.

## 5. Data Contracts (Hợp đồng dữ liệu)
## 5. Data Contracts
- **Chuẩn ODCS (Open Data Contract Standard):** Mô tả schema, chất lượng, SLA, tính sở hữu... dưới dạng YAML (ví dụ v3.1.0).
- **ODCS Standard (Open Data Contract Standard):** Describes schema, quality, SLA, ownership... in YAML format (e.g., v3.1.0).
- Data Contracts cần được thực thi qua 3 tầng (Shift-left CI gate, streaming runtime, post-ingest batch) chứ không chỉ nằm trên Catalog (kho lưu trữ dạng text).
- Data Contracts need to be enforced across 3 layers (Shift-left CI gate, streaming runtime, post-ingest batch) rather than just sitting in a Catalog (text repository).

## 6. Lineage (Truy xuất nguồn gốc)
## 6. Lineage
- **OpenLineage:** Chuẩn hóa JSON mô tả luồng sự kiện lineage. Quality (chất lượng dữ liệu) là một thuộc tính gắn trên các bước của lineage.
- **OpenLineage:** Standardized JSON describing the lineage event stream. Quality is an attribute attached to the lineage steps.
- **Truy vấn đa chiều:** 
- **Multi-dimensional querying:**
  - **Xuôi (Blast radius):** Lỗi này gây tác động tới ai?
  - **Forward (Blast radius):** Who does this error affect?
  - **Ngược (Root cause):** Dữ liệu sai do xuất phát từ khâu nào?
  - **Backward (Root cause):** Which stage did the incorrect data originate from?

## 7. AI-Infra (Hạ tầng AI)
## 7. AI-Infra
- **Feature Stores:** Quản lý *Training-serving skew* (lệch cấu trúc dữ liệu giữa lúc học và lúc chạy thật) và *Point-in-time correctness* (tránh tình trạng nhìn trộm vào tương lai).
- **Feature Stores:** Manage *Training-serving skew* (data structure deviation between training and serving) and *Point-in-time correctness* (avoiding looking into the future).
- **Embeddings & RAG:** Cần kiểm tra embedding drift (sự thay đổi khoảng cách vector theo thời gian) và tính chất lỗi thời của corpus trong RAG.
- **Embeddings & RAG:** Need to check for embedding drift (change in vector distance over time) and the staleness of the corpus in RAG.
- **Telemetry:** Cần theo dõi cả pipeline của LLM, đảm bảo chống nhiễm (contamination) và làm sạch dữ liệu huấn luyện.
- **Telemetry:** Need to monitor the entire LLM pipeline, ensuring contamination prevention and training data cleaning.
