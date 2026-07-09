---
type: summary
title: "Summary: Day 27 Track 2 - Data Observability & Lineage"
description: "A comprehensive guide on data observability, Great Expectations, anomaly detection, SLO engineering, and data incident response."
tags: [data-observability, data-engineering, great-expectations, slo, anomaly-detection]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/27/Day27 - Track 2 - Data-observability-lineage.pdf"]
---
# *Ngày 27 Track 2 - Khả năng Quan sát & Nguồn gốc Dữ liệu*

Tài liệu này tóm tắt bài giảng Ngày 27 Track 2 tập trung vào việc đảm bảo độ tin cậy của dữ liệu, tiến xa hơn việc giám sát luồng dữ liệu (pipeline monitoring) đơn thuần để đạt được khả năng quan sát dữ liệu (data observability) thực sự.

## *1. Giám sát Luồng Dữ liệu (Pipeline Monitoring) vs Khả năng Quan sát Dữ liệu (Data Observability)*

- ***Giám sát Luồng Dữ liệu:** Đặt câu hỏi "Máy có đang chạy không?" (ví dụ: Job Airflow có hoàn thành không? CPU/logs có bình thường không?).*
- ***Khả năng Quan sát Dữ liệu:** Đặt câu hỏi "Dữ liệu có đáng tin cậy không?" (ví dụ: Dữ liệu có mới, đầy đủ, nhất quán không?).*
- ***Lỗi Tiềm ẩn (Silent Failures):** Các hệ thống AI/ML thường thất bại do dữ liệu xấu (lỗi tiềm ẩn) thay vì sập dịch vụ. Việc thực thi pipeline thành công không đảm bảo dữ liệu chính xác.*

## *2. Năm Trụ cột của Khả năng Quan sát Dữ liệu*

Sử dụng khuôn khổ Monte Carlo, khả năng quan sát dữ liệu được xác định bởi 5 trụ cột:
1. ***Độ mới (Freshness):** Dữ liệu có được cập nhật mới không?*
2. ***Khối lượng (Volume):** Số lượng hàng có bất thường không?*
3. ***Phân phối (Distribution):** Các giá trị có nằm trong phạm vi mong đợi không?*
4. ***Lược đồ (Schema):** Tên cột hoặc kiểu dữ liệu có thay đổi không?*
5. ***Nguồn gốc (Lineage):** Những tài sản downstream (phía dưới) nào bị ảnh hưởng bởi một sự cố?*

Việc quan sát dữ liệu AI phi cấu trúc (văn bản, hình ảnh, embeddings) yêu cầu theo dõi các đặc trưng có thể đo lường được suy ra (ví dụ: sự trôi dạt của embedding, phân phối độ dài văn bản, điểm số độ mờ).


Thay vì giữ những giả định ngầm về dữ liệu trong đầu các kỹ sư, các công cụ như Great Expectations mã hóa chúng thành các bài kiểm tra có thể thực thi, được kiểm soát phiên bản.
- ***Expectation Suite (Bộ mong đợi):** Một tập hợp các quy tắc (ví dụ: `ExpectColumnValuesToNotBeNull`, `ExpectColumnValuesToBeBetween`).*
- ***Checkpoints (Điểm kiểm tra):** Tích hợp các bộ mong đợi vào các pipeline production (ví dụ: bên trong Airflow). Nếu một điểm kiểm tra thất bại, các hành động như cảnh báo Slack hoặc chặn các job phía dưới sẽ được kích hoạt.*
- ***Lỗi cứng (Hard Fails):** Chặn pipeline (ví dụ: trùng lặp khóa chính).*
- ***Lỗi mềm (Soft Fails):** Kích hoạt cảnh báo (ví dụ: độ trôi dạt phân phối nhẹ).*

## *4. Phát hiện Bất thường vs Quy tắc*

- ***Quy tắc (ví dụ: GX, dbt tests):** Nắm bắt các vấn đề đã biết, mang tính tất định, gây lỗi cứng trong pipeline.*
- ***Phát hiện Bất thường (ví dụ: Z-score, Prophet):** Nắm bắt các vấn đề chưa biết dựa trên đường cơ sở lịch sử (ví dụ: số lượng hàng giảm 50%). Cần con người đánh giá do cảnh báo sai (false positives). Z-score đánh dấu các bất thường nếu độ lệch vượt quá ngưỡng (ví dụ: > 3 độ lệch chuẩn).*

## *5. dbt Tests (Lớp Chuyển đổi)*

Lớp chuyển đổi SQL yêu cầu giám sát chặt chẽ vì lỗi ở đây hiếm khi làm sập pipeline nhưng lại làm hỏng dữ liệu nghiêm trọng.
- ***Các Bài kiểm tra Tích hợp của dbt:** `not_null`, `unique`, `accepted_values`, `relationships`.*
- ***Các Bài kiểm tra SQL Tùy chỉnh:** Đảm bảo logic kinh doanh là đúng.*
- ***Kim tự tháp Kiểm thử:** Kiểm thử Đơn vị (chạy nhanh, gần với mô hình) nên được ưu tiên hơn các bài kiểm tra End-to-End tốn kém.*

## *6. Kỹ thuật SLO cho Dữ liệu & AI*

Các nền tảng dữ liệu coi độ tin cậy như một tính năng của sản phẩm.
- ***SLI (Chỉ số Mức Dịch vụ):** Một số liệu có thể đo lường (ví dụ: `freshness_minutes`, `null_rate`).*
- ***SLO (Mục tiêu Mức Dịch vụ):** Mục tiêu hướng đến (ví dụ: "độ mới < 60 phút cho 99.5% thời gian").*
- ***Ngân sách Lỗi (Error Budget):** `1 - SLO`. Nếu ngân sách cạn kiệt quá nhanh, việc phát hành tính năng sẽ bị tạm dừng để ưu tiên cho sự ổn định.*

## *7. Ứng phó với Sự cố Dữ liệu*

Khả năng quan sát chỉ có giá trị nếu nhóm biết cách phản ứng.
- ***Vòng đời Sự cố:** Phát hiện → Phân loại → Giảm thiểu → Phân tích Nguyên nhân Gốc rễ → Phục hồi → Rút kinh nghiệm (Postmortem).*
- ***Runbooks:** Các hướng dẫn quy trình được tiêu chuẩn hóa để xử lý các sự cố.*
- ***Mức độ Nghiêm trọng:** Phân loại các sự cố (P0 đến P3) để xác định thời gian phản hồi.*
- ***Rút kinh nghiệm Không đổ lỗi (Blameless Postmortems) & Kỹ thuật Hỗn loạn (Chaos Engineering):** Thúc đẩy việc học hỏi mà không đổ lỗi. Sử dụng "5 Câu hỏi Tại sao" (5 Whys) để tìm ra nguyên nhân gốc rễ mang tính hệ thống.*

---

### *Câu hỏi ôn tập Ngày 27*

   Điểm khác biệt cốt lõi giữa **Pipeline Monitoring** và **Data Observability** là gì?
     A. Pipeline Monitoring chỉ kiểm tra thời gian chạy, còn Data Observability kiểm tra tính đúng đắn của dữ liệu.
     B. Pipeline Monitoring dùng cho batch, Data Observability dùng cho streaming.
     C. Pipeline Monitoring tập trung vào logs, Data Observability tập trung vào schema.
     D. Không có sự khác biệt, cả hai đều giống nhau.
   ***Đáp án:** A*

   Trong 5 trụ cột của Data Observability, trụ cột nào phát hiện sự thay đổi về tên cột hoặc kiểu dữ liệu?
   ***Đáp án:** C*

   Trong Great Expectations, **Checkpoint** có vai trò gì?
     A. Lưu trữ các rule kiểm tra dữ liệu (Expectation Suite).
     B. Tích hợp Expectation Suite vào pipeline sản xuất và kích hoạt hành động (alert, block) khi thất bại.
     C. Tự động sinh dữ liệu mẫu để kiểm tra.
     D. Thay thế hoàn toàn cho dbt tests.
   ***Đáp án:** B*

   Trong SLO Engineering, **Error Budget** được sử dụng để làm gì?
     A. Đo lường mức độ tươi mới của dữ liệu.
     B. Cân bằng giữa tính ổn định và tính năng mới: nếu ngân sách lỗi cạn kiệt, ưu tiên sửa lỗi thay vì phát hành tính năng.
     C. Xác định ngưỡng cảnh báo cho anomaly detection.
     D. Phân loại mức độ nghiêm trọng của sự cố (P0-P3).
   ***Đáp án:** B*
