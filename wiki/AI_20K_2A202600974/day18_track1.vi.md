---
type: summary
title: "Day 18 Track 1: Human-Centered AI Design"
description: "Summary of Human-Centered AI design principles, focusing on trust calibration, agency, and feedback loops."
tags: [UX, Human-Centered AI, Trust, Agency, Feedback, Design]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/18/1-d18-slide-v1-track1.pdf", "raw/AI_20K_2A202600974/18/day18-track1-lab.pdf"]
---


---

1. Nguyên tắc cốt lõi & Kỳ vọng

  Đặt kỳ vọng: Tránh để giao diện người dùng hứa hẹn nhiều hơn những gì AI có thể thực hiện. Người dùng cần hiểu AI có thể làm gì, không thể làm gì và có thể thất bại như thế nào.

  Tính cách AI: Kết hợp giữa sự ấm áp (thân thiện, dễ tiếp cận) và năng lực. Năng lực được hiệu chỉnh phù hợp giúp xây dựng lòng tin bền vững. Phát tín hiệu "không quá hoàn hảo" có thể làm giảm kỳ vọng ban đầu và cải thiện sự hài lòng lâu dài.

  Khung tham khảo: Sổ tay PAIR của Google (định hình sản phẩm AI) và Bộ công cụ HAX của Microsoft (thiết kế tương tác AI).

---

2. Hiệu chỉnh lòng tin

  Tin tưởng thái quá: Người dùng tin tưởng AI vượt quá khả năng thực sự, dẫn đến ủy thác nhiệm vụ quá mức mà không kiểm tra lại.

  Thiếu tin tưởng: Người dùng tin tưởng AI ít hơn khả năng thực tế, dẫn đến sử dụng không đầy đủ.

  Công thức cho lòng tin: Hiệu chỉnh lòng tin = Kỳ vọng + Khả năng giải thích + Kiểm soát
    Kỳ vọng: Làm rõ giới hạn của AI.
    Khả năng giải thích: Giúp người dùng hiểu tại sao AI đưa ra đầu ra cụ thể.
    Kiểm soát: Cho phép người dùng chỉnh sửa, hoàn tác, xem trước hoặc phê duyệt các hành động.

---

3. Tăng cường so với Tự động hóa (Quyền chủ động)

Xác định mức độ tự chủ của AI dựa trên chi phí sai sót và mức độ chắc chắn về ý định của người dùng.

  Hành động (Tự động hóa): Độ chắc chắn cao, chi phí sai sót thấp. Dễ hoàn tác. AI tự động thực hiện hành động để tiết kiệm thời gian.

  Hỏi (Sáng kiến hỗn hợp): Độ chắc chắn vừa phải, tác động đáng kể. AI yêu cầu xác nhận trước khi tiến hành.

  Không hành động (Bất động): Chi phí sai sót cao, độ chắc chắn thấp. Hệ thống hoàn toàn để quyết định cho người dùng.

---

4. Xử lý lỗi AI và sự không chắc chắn

  Giải thích lý do tại sao hệ thống đưa ra quyết định (ví dụ: ánh xạ hành vi hoặc đầu vào của người dùng thành đầu ra).

  Hiển thị kết quả kèm mức độ tin cậy.

  Cung cấp các lối thoát rõ ràng (ví dụ: chuyển sang nhân viên hỗ trợ, đưa ra các tùy chọn dự phòng).

  Hoàn tác / Quay lại: Cho phép người dùng dễ dàng khôi phục các hành động của AI.

  Sử dụng trạng thái lỗi như cơ hội để thu thập phản hồi và hướng dẫn người dùng cách sử dụng đúng.

---

5. Vòng phản hồi

Phản hồi cho phép hệ thống học hỏi từ người dùng và người dùng học hỏi từ hệ thống.

  Phản hồi của người dùng (Rõ ràng): Thích/không thích, đánh giá, báo cáo lỗi.

  Phản hồi của người dùng (Ngầm định): Các hành vi của người dùng như hoàn tác, bỏ qua tác vụ hoặc chấp nhận gợi ý.

  Phản hồi của hệ thống (Rõ ràng): Thông báo giải thích giới hạn, trạng thái hoặc các bước tiếp theo.

  Phản hồi của hệ thống (Ngầm định): Các gợi ý của giao diện, trạng thái mặc định và tiết lộ dần dần giúp định hướng mô hình tinh thần của người dùng.

---

6. Thiết kế kịch bản thực hành

Bài tập thực hành nhấn mạnh việc thiết kế một phân đoạn liên tục của trải nghiệm AI qua bốn giai đoạn:

   Khởi tạo: Đặt kỳ vọng mà không làm người dùng choáng ngợp.

   Trong quá trình hành động: Hiển thị suy luận của AI, yêu cầu ngữ cảnh hoặc đề xuất giải pháp.

   Sau hành động: Xem xét kết quả, chỉnh sửa và xác nhận.

   Sai sót & Khắc phục: Tạo vòng phản hồi để sửa lỗi và tiếp tục quy trình làm việc một cách liền mạch.

---

### *Câu hỏi ôn tập Ngày 18*

   Công thức **Trust Calibration** bao gồm Expectation, Explainability và Control. Yếu tố nào giúp người dùng hiểu tại sao AI đưa ra một kết quả cụ thể?
     A. Kỳ vọng
     B. Khả năng giải thích
     C. Kiểm soát
     D. Tự động hóa
   **Answer / Đáp án:** B

   Trong quyết định **Augmentation vs Automation**, khi nào AI nên tự động thực hiện hành động (Act)?
     A. Độ chắc chắn thấp, chi phí sai lầm cao
     B. Độ chắc chắn cao, chi phí sai lầm thấp
     C. Độ chắc chắn trung bình, tác động đáng kể
     D. Luôn luôn tự động để tiết kiệm thời gian
   **Answer / Đáp án:** B

   Khi AI gặp lỗi hoặc không chắc chắn, cách xử lý nào sau đây được khuyến khích?
     A. Ẩn kết quả để tránh gây nhầm lẫn
     B. Hiển thị kết quả với mức độ tin cậy và cung cấp lối thoát
     C. Bắt buộc người dùng chấp nhận kết quả
     D. Không thu thập phản hồi từ lỗi
   **Answer / Đáp án:** B

   "Người dùng nhấn nút **thích/không thích** hoặc đánh giá sản phẩm" thuộc loại phản hồi nào?
     A. Phản hồi người dùng (Implicit)
     B. Phản hồi người dùng (Explicit)
     C. Phản hồi hệ thống (Explicit)
     D. Phản hồi hệ thống (Implicit)
   **Answer / Đáp án:** B
