---
type: summary
title: "Summary: grading_questions.pdf"
description: "A detailed summary of the Day 8 RAG grading questions dataset, illustrating how to evaluate complex RAG capabilities like cross-document synthesis, temporal scoping, and hallucination resistance."
tags: [ai, 20k, day8, rag, evaluation, dataset]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/8/grading_questions.pdf"]
---

# Tóm tắt: Các câu hỏi chấm điểm RAG (Ngày 08)

## Tổng quan
Tài liệu này tóm tắt nội dung của `grading_questions.pdf`, bao gồm một bộ 10 câu hỏi kiểm tra được thiết kế để đánh giá độ mạnh và độ chính xác của một quy trình RAG (Retrieval-Augmented Generation). Những câu hỏi này được cấu trúc để kiểm tra các khả năng cụ thể của RAG, làm nổi bật các kiểu lỗi phổ biến và các tiêu chí kỳ vọng cho những câu trả lời chất lượng cao.

## Các chủ đề chính và khả năng của RAG được kiểm tra

### 1. Sự mới mẻ & Suy luận theo phiên bản (Câu hỏi: `gq01`)
- **Trọng tâm:** Phân biệt giữa các số liệu đã được cập nhật và đã lỗi thời (ví dụ: thời gian giải quyết SLA giảm từ 6 giờ xuống 4 giờ trong v2026.1).
- **Kỹ năng được kiểm tra:** Đánh giá xem quy trình có truy xuất được đoạn văn bản mới nhất hay bị nhầm lẫn bởi siêu dữ liệu (metadata) cũ.
- **Hành vi kỳ vọng:** Phải đề cập rõ ràng đến sự thay đổi trong lịch sử và trích dẫn đúng phiên bản.

### 2. Tổng hợp đa tài liệu (Câu hỏi: `gq02`, `gq06`)
- **Trọng tâm:** Trả lời các câu hỏi yêu cầu kết hợp thông tin từ nhiều tài liệu riêng biệt.
  - *Ví dụ (`gq02`):* Các yêu cầu về VPN từ Chính sách Nghỉ phép của Nhân sự kết hợp với giới hạn thiết bị từ bộ câu hỏi thường gặp (FAQ) của bộ phận IT Helpdesk.
  - *Ví dụ (`gq06`):* Kết hợp các bước leo thang khẩn cấp từ quy trình thao tác chuẩn (SOP) Kiểm soát Truy cập với thông tin liên lạc từ tài liệu SLA P1.
- **Kỹ năng được kiểm tra:** Truy xuất thông tin xuyên suốt nhiều tài liệu và tổng hợp hoàn chỉnh mà không bỏ sót bất kỳ phần nào của câu trả lời.

### 3. Sự đầy đủ & Xử lý ngoại lệ (Câu hỏi: `gq03`)
- **Trọng tâm:** Xác định nhiều điều kiện hoặc ngoại lệ trong một chính sách duy nhất (ví dụ: ngoại lệ hoàn tiền cho các mặt hàng Flash Sale *và* các mặt hàng đã được kích hoạt).
- **Kỹ năng được kiểm tra:** Đảm bảo bộ truy xuất lấy được toàn bộ phần có liên quan (sự đầy đủ của đoạn dữ liệu) và LLM đề cập đến *tất cả* các ngoại lệ, chứ không chỉ cái đầu tiên mà nó gặp.

### 4. Truy xuất số liệu thực tế cụ thể (Câu hỏi: `gq04`)
- **Trọng tâm:** Trích xuất một tỷ lệ phần trăm hoặc một con số chính xác ẩn bên trong văn bản (ví dụ: thay thế hoàn tiền bằng 110% tín dụng cửa hàng).
- **Kỹ năng được kiểm tra:** Sự trung thực và chính xác. Mô hình không được bịa ra (hallucinate) một con số tiêu chuẩn như 100% hay 120%.

### 5. Truy xuất nhiều chi tiết & Xác định phạm vi (Câu hỏi: `gq05`, `gq09`)
- **Trọng tâm:** Trích xuất nhiều điều kiện tiên quyết cho một hành động (ví dụ: việc cấp Quyền Admin yêu cầu sự phê duyệt của IT Manager + CISO, 5 ngày xử lý, và khóa đào tạo bắt buộc; khoảng thời gian đặt lại mật khẩu và thời điểm nhắc nhở).
- **Kỹ năng được kiểm tra:** Suy luận trên nhiều đoạn dữ liệu trong cùng một tài liệu và trích xuất các chi tiết tổng hợp từ nội dung có định dạng hỏi đáp (FAQ).

### 6. Khả năng chống ảo giác & Từ chối trả lời (Câu hỏi: `gq07`)
- **Trọng tâm:** Đặt một câu hỏi nghe có vẻ hợp lý nhưng câu trả lời lại *không* tồn tại trong kho dữ liệu (ví dụ: "Hình phạt khi vi phạm SLA P1 là gì?").
- **Kỹ năng được kiểm tra:** Khả năng của mô hình tự tin thông báo rằng thông tin bị thiếu ("Ngữ cảnh không đủ") thay vì phỏng đoán hay bịa ra một hình phạt dựa trên kiến thức chung trên internet.

### 7. Xử lý sự mơ hồ (Câu hỏi: `gq08`)
- **Trọng tâm:** Xử lý các trường hợp khi cùng một từ khóa/con số xuất hiện trong các ngữ cảnh khác nhau (ví dụ: thông báo trước "3 ngày" cho phép năm so với "3 ngày" nghỉ ốm cần có giấy chứng nhận y tế).
- **Kỹ năng được kiểm tra:** Khử tính mơ hồ về ngữ nghĩa. Quy trình không được trộn lẫn các quy tắc đi kèm với các giá trị số giống hệt nhau.

### 8. Phạm vi thời gian & Truy xuất nhận biết siêu dữ liệu (Câu hỏi: `gq10`)
- **Trọng tâm:** Truy vấn các chính sách dựa trên các ngày cụ thể (ví dụ: chỉ áp dụng Chính sách Hoàn tiền v4 đối với các đơn hàng được đặt sau ngày 01/02/2026).
- **Kỹ năng được kiểm tra:** Xác minh xem quy trình có sử dụng siêu dữ liệu `effective_date` (ngày có hiệu lực) để lọc và suy luận về các ràng buộc thời gian nhằm tránh trả lời bằng các tài liệu cũ hay không.

## Kết luận
Tập dữ liệu này đóng vai trò như một bộ tiêu chuẩn xuất sắc ("Golden Dataset") để đánh giá một quy trình RAG dựa trên các số liệu cốt lõi là Độ bao phủ ngữ cảnh (Context Recall), Tính trung thực (Faithfulness) và Độ liên quan của câu trả lời (Answer Relevance) - hay còn gọi là RAGAS Triad. Nó đặc biệt nhắm đến các trường hợp phức tạp (edge cases) mà tìm kiếm ngữ nghĩa cơ bản thường không xử lý được.
