---
type: overview
title: "Day 5 Overview - Thiết kế sản phẩm AI"
description: "Thiết kế sản phẩm AI đối phó với sự không chắc chắn, tập trung vào UX, đánh giá và Feedback loop."
tags: [ai, 20k, day5]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/5/1-day05-lecture-slides-v2.pdf"]
---
*# Day 5: Thiết kế sản phẩm AI cho sự không chắc chắn*

*## 1. AI Product ≠ Phần mềm truyền thống*

- *Phần mềm truyền thống chạy theo luật, đưa ra kết quả cố định. AI chạy theo xác suất, kết quả mỗi lần một khác và tồn tại sự không chắc chắn (uncertainty).*

- *Thiết kế AI Product không chỉ là gọi API, mà là thiết kế xoay quanh sự không chắc chắn đó. 3 trụ cột thiết kế AI product: **Yêu cầu (Requirement)**, **Trải nghiệm (UX)**, và **Đánh giá (Eval)**.*


- *Phân biệt giữa **Automation** (AI tự động làm thay, user không thấy, yêu cầu độ chính xác cực cao) và **Augmentation** (AI gợi ý, user duyệt, chấp nhận độ chính xác thấp hơn để đổi lấy tốc độ/hiệu suất). Tốt nhất nên bắt đầu bằng Augmentation và tăng dần Automation.*

- ***Graceful Failure & Trust Recovery**: AI chắc chắn sẽ sai, vấn đề là xử lý lỗi một cách nhẹ nhàng (đưa ra các lựa chọn thay thế, cho phép user sửa, giải thích lý do) để giữ được niềm tin của người dùng.*

- *Tránh việc lấy giao diện Chatbot làm mặc định. UI/UX cho AI nên hiển thị quá trình suy luận, cho phép chỉnh sửa kế hoạch, v.v.*

*## 3. Đánh giá (Evaluation) - Precision vs Recall*

- *Không có câu trả lời "đúng/sai" tuyệt đối mà chỉ có phân phối chất lượng.*

- ***Precision**: Tỷ lệ đúng trong những gì AI dự đoán là đúng (giảm báo nhầm / False Positive). Ưu tiên khi hậu quả của hành động sai là rất lớn (ví dụ: chuyển tiền, xoá email).*

- ***Recall**: Tỷ lệ tìm được trong tất cả những thứ cần tìm (giảm bỏ sót / False Negative). Ưu tiên khi bỏ sót gây hậu quả nghiêm trọng hơn (ví dụ: lọc nội dung trẻ em, y tế).*

- *Chọn ưu tiên Precision hay Recall phụ thuộc vào bài toán và trải nghiệm người dùng (UX).*


- *Sản phẩm AI phải liên tục học hỏi từ tương tác của người dùng.*

- *3 loại feedback signal:*

  - ***Implicit (Ngầm)**: Thời gian xem, cuộn trang, tỷ lệ chấp nhận/bỏ qua.*

  - ***Explicit (Trực tiếp)**: Thích/Không thích (Thumbs up/down), đánh giá sao.*

  - ***Correction (Sửa lỗi)**: User trực tiếp sửa kết quả của AI.*

- ***Data Flywheel**: Dữ liệu từ người dùng giúp cải thiện mô hình, mô hình tốt hơn mang lại trải nghiệm tốt hơn, thu hút nhiều người dùng hơn -> tạo vòng lặp liên tục cải tiến. Đây mới là rào cản cạnh tranh cốt lõi của AI Product.*

*## 5. ROI & Chi phí*

- *Chi phí chạy AI phụ thuộc vào mỗi lượt sử dụng (Inference cost). Càng nhiều người dùng càng tốn tiền. Cần tính toán ROI chi tiết (theo kịch bản thận trọng, thực tế, lạc quan) trước khi scale.*
