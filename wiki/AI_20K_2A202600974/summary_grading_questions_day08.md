---
type: summary
title: "Summary: grading_questions.pdf"
description: "A detailed summary of the Day 8 RAG grading questions dataset, illustrating how to evaluate complex RAG capabilities like cross-document synthesis, temporal scoping, and hallucination resistance."
tags: [ai, 20k, day8, rag, evaluation, dataset]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/8/grading_questions.pdf"]
---

# Summary: RAG Grading Questions (Day 08)
# Tóm tắt: Các câu hỏi chấm điểm RAG (Ngày 08)

## Overview
## Tổng quan
This document summarizes the contents of `grading_questions.pdf`, which contains a suite of 10 test questions designed to evaluate the robustness and accuracy of a Retrieval-Augmented Generation (RAG) pipeline. These questions are structured to test specific RAG capabilities, highlighting common failure modes and expected criteria for high-quality responses.
Tài liệu này tóm tắt nội dung của `grading_questions.pdf`, bao gồm một bộ 10 câu hỏi kiểm tra được thiết kế để đánh giá độ mạnh và độ chính xác của một quy trình RAG (Retrieval-Augmented Generation). Những câu hỏi này được cấu trúc để kiểm tra các khả năng cụ thể của RAG, làm nổi bật các kiểu lỗi phổ biến và các tiêu chí kỳ vọng cho những câu trả lời chất lượng cao.

## Key Themes and RAG Capabilities Tested
## Các chủ đề chính và khả năng của RAG được kiểm tra

### 1. Freshness & Version Reasoning (Question: `gq01`)
### 1. Sự mới mẻ & Suy luận theo phiên bản (Câu hỏi: `gq01`)
- **Focus:** Differentiating between updated and outdated metrics (e.g., SLA resolution time dropping from 6 hours to 4 hours in v2026.1).
- **Trọng tâm:** Phân biệt giữa các số liệu đã được cập nhật và đã lỗi thời (ví dụ: thời gian giải quyết SLA giảm từ 6 giờ xuống 4 giờ trong v2026.1).
- **Skill Tested:** Evaluating whether the pipeline retrieves the latest chunk or gets confused by older metadata.
- **Kỹ năng được kiểm tra:** Đánh giá xem quy trình có truy xuất được đoạn văn bản mới nhất hay bị nhầm lẫn bởi siêu dữ liệu (metadata) cũ.
- **Expected Behavior:** Must explicitly mention the historical change and cite the correct version.
- **Hành vi kỳ vọng:** Phải đề cập rõ ràng đến sự thay đổi trong lịch sử và trích dẫn đúng phiên bản.

### 2. Multi-Document Synthesis (Questions: `gq02`, `gq06`)
### 2. Tổng hợp đa tài liệu (Câu hỏi: `gq02`, `gq06`)
- **Focus:** Answering questions that require fusing information from multiple distinct documents.
- **Trọng tâm:** Trả lời các câu hỏi yêu cầu kết hợp thông tin từ nhiều tài liệu riêng biệt.
  - *Example (`gq02`):* VPN requirements from the HR Leave Policy synthesized with device limits from the IT Helpdesk FAQ.
  - *Ví dụ (`gq02`):* Các yêu cầu về VPN từ Chính sách Nghỉ phép của Nhân sự kết hợp với giới hạn thiết bị từ bộ câu hỏi thường gặp (FAQ) của bộ phận IT Helpdesk.
  - *Example (`gq06`):* Synthesizing emergency escalation steps from the Access Control SOP with contact info from the SLA P1 document.
  - *Ví dụ (`gq06`):* Kết hợp các bước leo thang khẩn cấp từ quy trình thao tác chuẩn (SOP) Kiểm soát Truy cập với thông tin liên lạc từ tài liệu SLA P1.
- **Skill Tested:** Cross-document retrieval and complete synthesis without omitting parts of the answer.
- **Kỹ năng được kiểm tra:** Truy xuất thông tin xuyên suốt nhiều tài liệu và tổng hợp hoàn chỉnh mà không bỏ sót bất kỳ phần nào của câu trả lời.

### 3. Completeness & Exception Handling (Question: `gq03`)
### 3. Sự đầy đủ & Xử lý ngoại lệ (Câu hỏi: `gq03`)
- **Focus:** Identifying multiple conditions or exceptions within a single policy (e.g., refund exceptions for Flash Sale items *and* activated items).
- **Trọng tâm:** Xác định nhiều điều kiện hoặc ngoại lệ trong một chính sách duy nhất (ví dụ: ngoại lệ hoàn tiền cho các mặt hàng Flash Sale *và* các mặt hàng đã được kích hoạt).
- **Skill Tested:** Ensuring the retriever fetches the entire relevant section (chunk completeness) and that the LLM mentions *all* exceptions, not just the first one it encounters.
- **Kỹ năng được kiểm tra:** Đảm bảo bộ truy xuất lấy được toàn bộ phần có liên quan (sự đầy đủ của đoạn dữ liệu) và LLM đề cập đến *tất cả* các ngoại lệ, chứ không chỉ cái đầu tiên mà nó gặp.

### 4. Specific Numeric Fact Retrieval (Question: `gq04`)
### 4. Truy xuất số liệu thực tế cụ thể (Câu hỏi: `gq04`)
- **Focus:** Extracting an exact percentage or number buried in a text (e.g., 110% store credit alternative to a refund).
- **Trọng tâm:** Trích xuất một tỷ lệ phần trăm hoặc một con số chính xác ẩn bên trong văn bản (ví dụ: thay thế hoàn tiền bằng 110% tín dụng cửa hàng).
- **Skill Tested:** Faithfulness and precision. The model must not hallucinate a standard number like 100% or 120%.
- **Kỹ năng được kiểm tra:** Sự trung thực và chính xác. Mô hình không được bịa ra (hallucinate) một con số tiêu chuẩn như 100% hay 120%.

### 5. Multi-Detail Retrieval & Scope Identification (Questions: `gq05`, `gq09`)
### 5. Truy xuất nhiều chi tiết & Xác định phạm vi (Câu hỏi: `gq05`, `gq09`)
- **Focus:** Extracting multiple prerequisites for an action (e.g., granting Admin Access requires IT Manager + CISO approval, 5 days processing, and mandatory training; password reset intervals and reminder times).
- **Trọng tâm:** Trích xuất nhiều điều kiện tiên quyết cho một hành động (ví dụ: việc cấp Quyền Admin yêu cầu sự phê duyệt của IT Manager + CISO, 5 ngày xử lý, và khóa đào tạo bắt buộc; khoảng thời gian đặt lại mật khẩu và thời điểm nhắc nhở).
- **Skill Tested:** Multi-chunk reasoning within the same document and extracting composite details from FAQ-style content.
- **Kỹ năng được kiểm tra:** Suy luận trên nhiều đoạn dữ liệu trong cùng một tài liệu và trích xuất các chi tiết tổng hợp từ nội dung có định dạng hỏi đáp (FAQ).

### 6. Hallucination Resistance & Abstention (Question: `gq07`)
### 6. Khả năng chống ảo giác & Từ chối trả lời (Câu hỏi: `gq07`)
- **Focus:** Asking a plausible-sounding question whose answer does *not* exist in the corpus (e.g., "What is the penalty for violating SLA P1?").
- **Trọng tâm:** Đặt một câu hỏi nghe có vẻ hợp lý nhưng câu trả lời lại *không* tồn tại trong kho dữ liệu (ví dụ: "Hình phạt khi vi phạm SLA P1 là gì?").
- **Skill Tested:** The model's ability to confidently state that the information is missing ("Insufficient Context") instead of guessing or fabricating a penalty based on general internet knowledge.
- **Kỹ năng được kiểm tra:** Khả năng của mô hình tự tin thông báo rằng thông tin bị thiếu ("Ngữ cảnh không đủ") thay vì phỏng đoán hay bịa ra một hình phạt dựa trên kiến thức chung trên internet.

### 7. Disambiguation (Question: `gq08`)
### 7. Xử lý sự mơ hồ (Câu hỏi: `gq08`)
- **Focus:** Handling instances where the same keyword/number appears in different contexts (e.g., "3 days" notice for annual leave vs. "3 days" sick leave requiring a medical certificate).
- **Trọng tâm:** Xử lý các trường hợp khi cùng một từ khóa/con số xuất hiện trong các ngữ cảnh khác nhau (ví dụ: thông báo trước "3 ngày" cho phép năm so với "3 ngày" nghỉ ốm cần có giấy chứng nhận y tế).
- **Skill Tested:** Semantic disambiguation. The pipeline must not mix up the rules tied to identical numeric values.
- **Kỹ năng được kiểm tra:** Khử tính mơ hồ về ngữ nghĩa. Quy trình không được trộn lẫn các quy tắc đi kèm với các giá trị số giống hệt nhau.

### 8. Temporal Scoping & Metadata-Aware Retrieval (Question: `gq10`)
### 8. Phạm vi thời gian & Truy xuất nhận biết siêu dữ liệu (Câu hỏi: `gq10`)
- **Focus:** Querying policies based on specific dates (e.g., applying Refund Policy v4 only to orders placed after 01/02/2026).
- **Trọng tâm:** Truy vấn các chính sách dựa trên các ngày cụ thể (ví dụ: chỉ áp dụng Chính sách Hoàn tiền v4 đối với các đơn hàng được đặt sau ngày 01/02/2026).
- **Skill Tested:** Verifying if the pipeline uses `effective_date` metadata to filter and reason about temporal constraints to avoid answering using stale documents.
- **Kỹ năng được kiểm tra:** Xác minh xem quy trình có sử dụng siêu dữ liệu `effective_date` (ngày có hiệu lực) để lọc và suy luận về các ràng buộc thời gian nhằm tránh trả lời bằng các tài liệu cũ hay không.

## Conclusion
## Kết luận
This dataset serves as an excellent benchmark ("Golden Dataset") for evaluating a RAG pipeline across the core metrics of Context Recall, Faithfulness, and Answer Relevance (the RAGAS Triad). It specifically targets complex edge cases that basic semantic search often fails to handle correctly.
Tập dữ liệu này đóng vai trò như một bộ tiêu chuẩn xuất sắc ("Golden Dataset") để đánh giá một quy trình RAG dựa trên các số liệu cốt lõi là Độ bao phủ ngữ cảnh (Context Recall), Tính trung thực (Faithfulness) và Độ liên quan của câu trả lời (Answer Relevance) - hay còn gọi là RAGAS Triad. Nó đặc biệt nhắm đến các trường hợp phức tạp (edge cases) mà tìm kiếm ngữ nghĩa cơ bản thường không xử lý được.
