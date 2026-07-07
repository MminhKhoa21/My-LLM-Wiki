---
type: overview
title: "Day 10: Data Pipeline & Data Observability"
description: "Comprehensive overview of managing the data pipeline for AI systems, covering ETL/ELT architecture, data quality dimensions, and observability pillars to prevent data-induced hallucinations."
tags: [ai, 20k, day10, data-pipeline, observability, etl, rag]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/10/Day 10 Data Pipeline and Data Observability.pdf", "raw/AI_20K_2A202600974/10/Day10 data pipeline observability E402.pdf"]
---
*Ngày 10: Đường Ống Dữ Liệu & Khả Năng Quan Sát Dữ Liệu*

*Giới thiệu*

*Chất lượng đầu ra của một AI Agent gắn liền trực tiếp với chất lượng dữ liệu đầu vào của nó. Ngày 10 khám phá khái niệm nền tảng "Dữ liệu rác vào -> Kết quả rác ra" trong các hệ thống AI. Ngay cả một agent Truy xuất Tăng cường Sinh (RAG) tiên tiến cũng sẽ bị ảo giác nếu kho vector của nó chứa đầy dữ liệu bẩn, thiếu sót hoặc lỗi thời. Các tác vụ kỹ thuật dữ liệu thường chiếm 60-80% nỗ lực trong các dự án AI thực tế.*

*Kiến trúc Đường Ống Dữ Liệu*

*Một đường ống dữ liệu AI tiêu chuẩn di chuyển dữ liệu qua các giai đoạn sau: **Nguồn → Đường Ống → Lưu Trữ → Phục Vụ → Agent**.*

  *ETL (Trích xuất, Biến đổi, Tải): Dữ liệu được biến đổi trước khi tải vào kho dữ liệu. Lý tưởng cho các tình huống yêu cầu che giấu PII hoặc thực thi lược đồ nghiêm ngặt trước khi lưu trữ.*

  *ELT (Trích xuất, Tải, Biến đổi): Dữ liệu thô được tải vào hồ dữ liệu/kho dữ liệu trước, sau đó mới biến đổi. Phù hợp để xử lý dữ liệu lớn từ nhiều nguồn khác nhau và cho phép dễ dàng xử lý lại dữ liệu thô (ví dụ: thử nghiệm các chiến lược phân đoạn khác nhau).*

  *Xử lý Hàng loạt so với Xử lý Luồng:*
    *Hàng loạt: Xử lý theo lịch trình (ví dụ: đồng bộ hàng đêm). Đơn giản và chi phí thấp, nhưng có độ trễ cao hơn.*
    *Luồng: Xử lý sự kiện theo thời gian thực (ví dụ: webhook cho các ticket P1). Độ trễ thấp, nhưng phức tạp và chi phí cao hơn.*

*Tiếp nhận và Biến đổi*

*Lớp Tiếp nhận*

*Việc tiếp nhận dữ liệu bao gồm thu thập dữ liệu từ nhiều nguồn khác nhau như Cơ sở dữ liệu (PostgreSQL qua CDC), API, PDF và Luồng sự kiện.*

  *Thách thức: Xử lý giới hạn tốc độ (HTTP 429), hết thời gian chờ, sai lệch lược đồ và lỗi OCR.*

  *Giải pháp: Triển khai cơ chế backoff theo cấp số nhân, con trỏ phân trang, bộ đệm áp suất ngược (hàng đợi) và Hàng đợi Thư Chết (DLQ) để ngăn ngừa lỗi hệ thống. Nhấn mạnh vào đồng bộ gia tăng và upsert đơn tốt (idempotent) để đảm bảo an toàn khi chạy lại.*

*Biến đổi cho AI*

*Biến đổi dữ liệu cho AI khác biệt đáng kể so với Business Intelligence (BI) truyền thống. Nó được tối ưu hóa cho ngữ cảnh mô hình và khả năng truy xuất.*

  *Làm sạch: Khử trùng lặp, phân tích ngày tháng, chuẩn hóa Unicode và xử lý các giá trị bị thiếu.*

  *Phân đoạn: Cân bằng giữa ngân sách token và ý nghĩa ngữ nghĩa. Các đoạn quá lớn gây nhầm lẫn cho việc truy xuất, trong khi các đoạn quá nhỏ sẽ mất đi ngữ cảnh quan trọng.*

  *Siêu dữ liệu: Làm giàu các đoạn với siêu dữ liệu (`chunk_id`, `source_doc_id`, `version`, `effective_date`) là rất quan trọng để có trích dẫn chính xác và lọc dữ liệu.*

*Chất lượng Dữ liệu: 6 Khía cạnh*

*Dữ liệu phải vượt qua các cổng chất lượng nghiêm ngặt trước khi được nhúng (embedding):*

   *Tính đầy đủ: Không thiếu các trường quan trọng.*
   *Tính chính xác: Dữ liệu phản ánh đúng trạng thái thực tế của doanh nghiệp.*
   *Tính nhất quán: Định dạng và biểu diễn thực thể thống nhất.*
   *Tính kịp thời: Dữ liệu đáp ứng SLA về độ tươi mới.*
   *Tính hợp lệ: Dữ liệu tuân thủ nghiêm ngặt các lược đồ (hợp đồng) dự kiến.*
   *Tính duy nhất: Không có đoạn trùng lặp làm ô nhiễm kho vector.*

*Việc triển khai "Bộ Kỳ vọng" (ví dụ: sử dụng Great Expectations) cho phép các đường ống tự động dừng, cách ly hoặc cảnh báo người vận hành khi chất lượng giảm.*

*5 Trụ cột của Khả năng Quan sát Dữ liệu*

*Khả năng quan sát cho phép các nhóm phát hiện và sửa lỗi dữ liệu trước khi người dùng gặp phải ảo giác AI:*

   *Độ tươi mới: Dữ liệu có được cập nhật đúng giờ không?*
   *Phân phối: Có sự thay đổi bất ngờ trong các giá trị dữ liệu hoặc tỷ lệ null không?*
   *Khối lượng: Số lượng hàng được tiếp nhận có giảm hoặc tăng đột biến bất ngờ không?*
   *Lược đồ: Các cột có thay đổi bất ngờ không?*
   *Dòng dõi: Một đoạn đầu ra có thể được truy xuất ngược về tệp nguồn thô của nó không?*

*Quy trình Gỡ lỗi và Phân loại Sự cố*

*Khi một Agent cung cấp thông tin không chính xác, hãy tuân theo một quy trình gỡ lỗi có cấu trúc để truy vết từ đầu ra trở về nguồn:*

   *Phát hiện: Bắt các độ trễ tín hiệu hoặc vi phạm SLA (Độ tươi mới).*
   *Cô lập: Xác định vị trí dữ liệu bị rơi hoặc bị đình trệ (Khối lượng).*
   *Xác thực: Xác nhận xem vấn đề là sai lệch lược đồ hay lỗi phân tích cú pháp.*
   *Truy vết Dòng dõi: Theo dõi chính xác bước nào và tệp nguồn nào đã thất bại.*
   *Sửa & Chạy lại: Thực hiện sửa lỗi và chạy lại đường ống, sử dụng tính đơn tốt (idempotency) để tránh trùng lặp.*

*Điều phối*

*Các đường ống dữ liệu mạnh mẽ yêu cầu các Bộ điều phối như **Apache Airflow**, **Prefect** hoặc **Dagster**. Các công cụ này quản lý các Đồ thị có hướng không chu trình (DAG) của các tác vụ, xử lý lập lịch, chính sách thử lại, chạy lại dữ liệu quá khứ (backfill) và cảnh báo, đảm bảo đường ống chạy an toàn và đáng tin cậy.*
