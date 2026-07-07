---
type: summary
title: "Summary: Day 27 Track 2 - Data Observability & Lineage"
description: "A comprehensive guide on data observability, Great Expectations, anomaly detection, SLO engineering, and data incident response."
tags: [data-observability, data-engineering, great-expectations, slo, anomaly-detection]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/27/Day27 - Track 2 - Data-observability-lineage.pdf"]
---
# Day 27 Track 2 - Data Observability & Lineage
# *Ngày 27 Track 2 - Khả năng Quan sát & Nguồn gốc Dữ liệu*

This document summarizes the Day 27 Track 2 lecture focusing on ensuring data reliability, moving beyond simple pipeline monitoring to true data observability.
*Tài liệu này tóm tắt bài giảng Ngày 27 Track 2 tập trung vào việc đảm bảo độ tin cậy của dữ liệu, tiến xa hơn việc giám sát luồng dữ liệu (pipeline monitoring) đơn thuần để đạt được khả năng quan sát dữ liệu (data observability) thực sự.*

## 1. Pipeline Monitoring vs Data Observability
## *1. Giám sát Luồng Dữ liệu (Pipeline Monitoring) vs Khả năng Quan sát Dữ liệu (Data Observability)*

- **Pipeline Monitoring:** Asks "Is the machine running?" (e.g., Did the Airflow job finish? Are CPU/logs normal?).
- ***Giám sát Luồng Dữ liệu:** Đặt câu hỏi "Máy có đang chạy không?" (ví dụ: Job Airflow có hoàn thành không? CPU/logs có bình thường không?).*
- **Data Observability:** Asks "Is the data trustworthy?" (e.g., Is the data fresh, complete, consistent?).
- ***Khả năng Quan sát Dữ liệu:** Đặt câu hỏi "Dữ liệu có đáng tin cậy không?" (ví dụ: Dữ liệu có mới, đầy đủ, nhất quán không?).*
- **Silent Failures:** AI/ML systems often fail due to bad data (silent failures) rather than service crashes. A successful pipeline execution does not guarantee correct data.
- ***Lỗi Tiềm ẩn (Silent Failures):** Các hệ thống AI/ML thường thất bại do dữ liệu xấu (lỗi tiềm ẩn) thay vì sập dịch vụ. Việc thực thi pipeline thành công không đảm bảo dữ liệu chính xác.*

## 2. Five Pillars of Data Observability
## *2. Năm Trụ cột của Khả năng Quan sát Dữ liệu*

Using the Monte Carlo framework, data observability is defined by 5 pillars:
*Sử dụng khuôn khổ Monte Carlo, khả năng quan sát dữ liệu được xác định bởi 5 trụ cột:*
1. **Freshness:** Is the data up to date?
1. ***Độ mới (Freshness):** Dữ liệu có được cập nhật mới không?*
2. **Volume:** Is the row count anomalous?
2. ***Khối lượng (Volume):** Số lượng hàng có bất thường không?*
3. **Distribution:** Are the values within expected ranges?
3. ***Phân phối (Distribution):** Các giá trị có nằm trong phạm vi mong đợi không?*
4. **Schema:** Did column names or types change?
4. ***Lược đồ (Schema):** Tên cột hoặc kiểu dữ liệu có thay đổi không?*
5. **Lineage:** Which downstream assets are affected by an incident?
5. ***Nguồn gốc (Lineage):** Những tài sản downstream (phía dưới) nào bị ảnh hưởng bởi một sự cố?*

Observing unstructured AI data (text, images, embeddings) requires monitoring derived measurable features (e.g., embedding drift, text length distribution, blur scores).
*Việc quan sát dữ liệu AI phi cấu trúc (văn bản, hình ảnh, embeddings) yêu cầu theo dõi các đặc trưng có thể đo lường được suy ra (ví dụ: sự trôi dạt của embedding, phân phối độ dài văn bản, điểm số độ mờ).*

## 3. Great Expectations (GX) & Checkpoints
## *3. Great Expectations (GX) & Checkpoints*

Instead of keeping implicit assumptions about data in engineers' heads, tools like Great Expectations encode them as runnable, version-controlled tests.
*Thay vì giữ những giả định ngầm về dữ liệu trong đầu các kỹ sư, các công cụ như Great Expectations mã hóa chúng thành các bài kiểm tra có thể thực thi, được kiểm soát phiên bản.*
- **Expectation Suite:** A collection of rules (e.g., `ExpectColumnValuesToNotBeNull`, `ExpectColumnValuesToBeBetween`).
- ***Expectation Suite (Bộ mong đợi):** Một tập hợp các quy tắc (ví dụ: `ExpectColumnValuesToNotBeNull`, `ExpectColumnValuesToBeBetween`).*
- **Checkpoints:** Integrate suites into production pipelines (e.g., inside Airflow). If a checkpoint fails, actions like Slack alerts or blocking downstream jobs are triggered.
- ***Checkpoints (Điểm kiểm tra):** Tích hợp các bộ mong đợi vào các pipeline production (ví dụ: bên trong Airflow). Nếu một điểm kiểm tra thất bại, các hành động như cảnh báo Slack hoặc chặn các job phía dưới sẽ được kích hoạt.*
- **Hard Fails:** Block the pipeline (e.g., duplicate primary keys).
- ***Lỗi cứng (Hard Fails):** Chặn pipeline (ví dụ: trùng lặp khóa chính).*
- **Soft Fails:** Trigger warnings (e.g., slight distribution drift).
- ***Lỗi mềm (Soft Fails):** Kích hoạt cảnh báo (ví dụ: độ trôi dạt phân phối nhẹ).*

## 4. Anomaly Detection vs Rules
## *4. Phát hiện Bất thường vs Quy tắc*

- **Rules (e.g., GX, dbt tests):** Catch known issues, deterministic, hard fail pipelines.
- ***Quy tắc (ví dụ: GX, dbt tests):** Nắm bắt các vấn đề đã biết, mang tính tất định, gây lỗi cứng trong pipeline.*
- **Anomaly Detection (e.g., Z-score, Prophet):** Catch unknown unknowns based on historical baselines (e.g., row count drops by 50%). Requires human review due to false positives. Z-score flags anomalies if deviations exceed a threshold (e.g., > 3 standard deviations).
- ***Phát hiện Bất thường (ví dụ: Z-score, Prophet):** Nắm bắt các vấn đề chưa biết dựa trên đường cơ sở lịch sử (ví dụ: số lượng hàng giảm 50%). Cần con người đánh giá do cảnh báo sai (false positives). Z-score đánh dấu các bất thường nếu độ lệch vượt quá ngưỡng (ví dụ: > 3 độ lệch chuẩn).*

## 5. dbt Tests (Transformation Layer)
## *5. dbt Tests (Lớp Chuyển đổi)*

The SQL transformation layer requires close monitoring because errors here rarely crash the pipeline but heavily corrupt data.
*Lớp chuyển đổi SQL yêu cầu giám sát chặt chẽ vì lỗi ở đây hiếm khi làm sập pipeline nhưng lại làm hỏng dữ liệu nghiêm trọng.*
- **dbt Built-in Tests:** `not_null`, `unique`, `accepted_values`, `relationships`.
- ***Các Bài kiểm tra Tích hợp của dbt:** `not_null`, `unique`, `accepted_values`, `relationships`.*
- **Custom SQL Tests:** Ensure business logic holds true.
- ***Các Bài kiểm tra SQL Tùy chỉnh:** Đảm bảo logic kinh doanh là đúng.*
- **Test Pyramid:** Unit tests (run fast, close to the model) should be prioritized over costly End-to-End tests.
- ***Kim tự tháp Kiểm thử:** Kiểm thử Đơn vị (chạy nhanh, gần với mô hình) nên được ưu tiên hơn các bài kiểm tra End-to-End tốn kém.*

## 6. SLO Engineering for Data & AI
## *6. Kỹ thuật SLO cho Dữ liệu & AI*

Data platforms treat reliability as a product feature.
*Các nền tảng dữ liệu coi độ tin cậy như một tính năng của sản phẩm.*
- **SLI (Service Level Indicator):** A measurable metric (e.g., `freshness_minutes`, `null_rate`).
- ***SLI (Chỉ số Mức Dịch vụ):** Một số liệu có thể đo lường (ví dụ: `freshness_minutes`, `null_rate`).*
- **SLO (Service Level Objective):** The target goal (e.g., "freshness < 60 mins for 99.5% of the time").
- ***SLO (Mục tiêu Mức Dịch vụ):** Mục tiêu hướng đến (ví dụ: "độ mới < 60 phút cho 99.5% thời gian").*
- **Error Budget:** `1 - SLO`. If the budget burns too fast, feature releases are halted to prioritize stability.
- ***Ngân sách Lỗi (Error Budget):** `1 - SLO`. Nếu ngân sách cạn kiệt quá nhanh, việc phát hành tính năng sẽ bị tạm dừng để ưu tiên cho sự ổn định.*

## 7. Data Incident Response
## *7. Ứng phó với Sự cố Dữ liệu*

Observability is only valuable if the team knows how to react.
*Khả năng quan sát chỉ có giá trị nếu nhóm biết cách phản ứng.*
- **Incident Lifecycle:** Detection → Triage → Mitigation → Root Cause Analysis → Recovery → Postmortem.
- ***Vòng đời Sự cố:** Phát hiện → Phân loại → Giảm thiểu → Phân tích Nguyên nhân Gốc rễ → Phục hồi → Rút kinh nghiệm (Postmortem).*
- **Runbooks:** Standardized procedural guides for handling incidents.
- ***Runbooks:** Các hướng dẫn quy trình được tiêu chuẩn hóa để xử lý các sự cố.*
- **Severity Levels:** Classify incidents (P0 to P3) to determine response times.
- ***Mức độ Nghiêm trọng:** Phân loại các sự cố (P0 đến P3) để xác định thời gian phản hồi.*
- **Blameless Postmortems & Chaos Engineering:** Cultivate learning without pointing fingers. Use "5 Whys" to find systemic root causes.
- ***Rút kinh nghiệm Không đổ lỗi (Blameless Postmortems) & Kỹ thuật Hỗn loạn (Chaos Engineering):** Thúc đẩy việc học hỏi mà không đổ lỗi. Sử dụng "5 Câu hỏi Tại sao" (5 Whys) để tìm ra nguyên nhân gốc rễ mang tính hệ thống.*
