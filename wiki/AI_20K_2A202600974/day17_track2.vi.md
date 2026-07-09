---
type: summary
title: "Data Pipeline Engineering (Track 2)"
description: "Summary of Day 17 Track 2 on building robust data pipelines, Medallion Architecture, and streaming ingestion."
tags: [AI_20K_2A202600974, Day17, Data_Pipeline, ETL, Kafka]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/17/Day 17 - Track 2 - Data Pipeline.pdf"]
---
# Kỹ thuật Pipeline Dữ liệu (Ngày 17 - Track 2)

Track này nhấn mạnh rằng các pipeline dữ liệu là một phụ thuộc quan trọng của các mô hình AI. Một pipeline bị lỗi có thể âm thầm phá hủy độ chính xác của mô hình trong môi trường sản xuất ("Rác vào, rác ra").

## Các khái niệm chính

### ETL so với ELT & Kiến trúc Medallion

  * **ELT (Trích xuất, Tải, Biến đổi)** là mặc định cho các pipeline AI gốc đám mây nhờ chi phí tính toán rẻ trong lakehouse.
   **Kiến trúc Medallion:*
    * **Bronze:** Dữ liệu thô, chỉ nối thêm, được giữ vĩnh viễn.
    * **Silver:** Đã được làm sạch, chuẩn hóa, loại bỏ trùng lặp và áp đặt lược đồ.
    * **Gold:** Sẵn sàng cho kinh doanh, tổng hợp, đặc trưng ML.

### Mẫu trích xuất và tiếp nhận dữ liệu

  * **Các mẫu trích xuất:** Toàn bộ, Tăng dần (dựa trên con trỏ), CDC (Capture dữ liệu thay đổi sử dụng Debezium để đọc log giao dịch).
  * **Tiếp nhận dữ liệu cho LLM:** Tiếp nhận dữ liệu phi cấu trúc bao gồm phân tích cú pháp, chia nhỏ (ví dụ: đệ quy 512 token) và nhúng vào kho Vector.

### Điều phối

  * **Airflow 3.0:** Chuyển đổi từ quy trình làm việc thuần túy dựa trên tác vụ sang quy trình làm việc nhận biết tài sản, lập lịch theo sự kiện và tài sản dữ liệu.
  * **Pipeline tài sản khai báo (Dagster, DLT):** Tập trung vào khai báo *cái gì* là các tập dữ liệu và phụ thuộc, thay vì *làm thế nào* để chạy chúng. Ví dụ: `Materialized View` so với `Streaming Table`.

### Tiếp nhận dữ liệu luồng

  * **Kiến trúc Kafka:** Được sử dụng cho tiếp nhận dữ liệu luồng. Kafka 4.0 loại bỏ ZooKeeper (chế độ KRaft).
  * **Luồng so với Hàng loạt:** Luồng (ví dụ: Kafka + Flink) đảm bảo độ trễ rất thấp cho việc tạo đặc trưng thời gian thực, giảm độ lệch giữa huấn luyện và phục vụ so với xử lý hàng loạt.

### Xác thực, Cổng chất lượng và Hợp đồng

  * **Cổng xác thực:** Triển khai chiến lược "thất bại sớm" bằng các công cụ như Pandera hoặc Great Expectations (GX). Các bản ghi xấu được đưa vào Hàng đợi cách ly/DLQ (hàng đợi thư chết) thay vì làm hỏng pipeline.
  * **LLM-as-a-Judge:** Được sử dụng để kiểm tra chất lượng dữ liệu mà các quy tắc tiêu chuẩn bỏ sót, chẳng hạn như trùng lặp ngữ nghĩa hoặc bất thường ngữ cảnh.
  * **Hợp đồng dữ liệu:** Thiết lập thỏa thuận giữa nhà sản xuất và người tiêu dùng dữ liệu, xác định lược đồ, ngữ nghĩa, chất lượng và SLA để ngăn chặn sự trôi dạt lược đồ thầm lặng.

### Pipeline dành riêng cho AI

  * **Bánh đà dữ liệu:** Sử dụng dấu vết tác nhân (prompt, lời gọi công cụ, phản hồi, phản hồi người dùng) như một nguồn dữ liệu thô (lớp Bronze) để xây dựng tập dữ liệu đánh giá và tinh chỉnh.
  * **Loại bỏ trùng lặp:** Cực kỳ quan trọng cho việc huấn luyện AI để ngăn chặn sự lặp lại nguyên văn. Các kỹ thuật bao gồm loại bỏ trùng lặp từ vựng (MinHash+LSH) và loại bỏ trùng lặp ngữ nghĩa (SemDeDup).
  * **Feature Store:** Hệ thống tập trung để định nghĩa các đặc trưng một lần và phục vụ chúng giống hệt nhau cho huấn luyện ngoại tuyến và suy luận trực tuyến, giải quyết độ lệch giữa huấn luyện và phục vụ.

---

### *Câu hỏi ôn tập Ngày 17*

   Trong Medallion Architecture, lớp nào chứa dữ liệu đã được làm sạch, khử trùng lặp và áp dụng schema?
   ***Đáp án:** B*

   Kỹ thuật nào được sử dụng để phát hiện các bản ghi lỗi trong pipeline mà không làm hỏng toàn bộ luồng xử lý?
     A. Ghi log lỗi vào file tạm
     B. Chuyển bản ghi lỗi vào Dead-Letter Queue (DLQ)
     C. Dừng pipeline ngay lập tức
     D. Ghi đè dữ liệu lỗi bằng giá trị null
   ***Đáp án:** B*

   Phương pháp nào giúp giảm thiểu training-serving skew bằng cách tạo features theo thời gian thực?
     A. Batch processing hàng ngày
     B. Streaming với Kafka và Flink
     C. Sử dụng File Store thay vì Feature Store
     D. Chỉ dùng CDC từ database
   ***Đáp án:** B*

   Trong quy trình ingestion cho LLM, bước nào diễn ra sau khi parsing dữ liệu phi cấu trúc?
     A. Embedding vào Vector Store
     B. Chunking (ví dụ: 512 token)
     C. Lưu trữ dạng raw
     D. Kiểm tra schema
   ***Đáp án:** B*

   "Data Flywheel" trong AI pipeline sử dụng loại dữ liệu nào làm nguồn cho lớp Bronze?
     A. Dữ liệu giao dịch tài chính
     B. Agent traces (prompt, tool calls, phản hồi người dùng)
     C. Dữ liệu cảm biến IoT
     D. Log hệ thống thuần túy
   ***Đáp án:** B*
