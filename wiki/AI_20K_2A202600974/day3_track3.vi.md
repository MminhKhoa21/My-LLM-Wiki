---
type: summary
title: "Day 3 Track 3: Từ Chatbot Đến Agentic Agent (Hieu)"
description: "Slide bài giảng Ngày 3 do giảng viên Hiếu trình bày về sự tiến hóa từ chatbot sang agent và cơ chế ReAct."
tags: [ai, 20k, day3, track3, agent, react, chatbot]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/3/day03-tu-chatbot-den-agentic-agent-react_hieu_e403.pdf", "raw/AI_20K_2A202600974/3/day3-material.pdf"]
---
# Day 3 Track 3: Từ Chatbot Đến Agentic Agent

Tài liệu này tóm tắt slide bài giảng Ngày 3 (phiên bản GV Hiếu) kết hợp với các bài tập thực hành. Nội dung đi sâu vào việc phát triển Agent thông qua ReAct pattern, ứng dụng Native Tool Calling và cách thức phân tích lỗi (failure analysis).

## 1. Mức Độ Thông Minh Của Hệ Thống AI

  - **Rule-based Bot**: Dựa trên quy tắc cố định (if/else), chi phí rẻ, giới hạn cao.
  - **LLM Chatbot**: Trả lời linh hoạt nhưng thường chỉ phản ứng tốt với hội thoại đơn lẻ. Nguy cơ tự bịa thông tin.
  - **Agent**: Định hướng theo mục tiêu (goal-driven). Sử dụng khả năng của LLM để quyết định gọi tool, đọc kết quả, rồi lặp lại để tiếp cận đích đến.


Hướng dẫn đánh giá khi nào bài toán thực sự cần Agent với 4 tiêu chí cốt lõi:


## 3. Kiến Trúc Agent

  - **Perception**: Tiếp nhận truy vấn từ người dùng và phản hồi từ tool.
  - **Reasoning**: Core xử lý tư duy (LLM), ra quyết định bước tiếp.
  - **Action**: Thực thi hành động bằng Native Tool Calling.
    - *Short-term*: Ngắn hạn trong Session/Context.
    - *Long-term*: Nằm trong CSDL/Vector Store, duy trì facts theo thời gian.


  - **ReAct (Reasoning + Acting)**: Kết hợp việc lập luận (Thought) cùng hành động gọi công cụ (Action) và theo dõi kết quả (Observation). Ưu điểm chính là bộc lộ tư duy của AI giúp con người kiểm soát.
  - **Text-ReAct (Cổ điển)**: Bắt model tự sinh văn bản định dạng (ví dụ `Action: get_weather()`), dễ bị gãy vỡ khi parsing (đặc biệt với local model nhỏ).
  - **Native Tool Calling (Hiện đại)**: LLM sinh ra output bằng JSON schema tiêu chuẩn từ API provider (như OpenAI), giúp tăng tính ổn định đáng kể.

## 5. Failure Modes (5 Kiểu Lỗi Của Agent)

Trong quá trình code và debug, học viên sẽ thường xuyên gặp 5 lỗi:

   1. **Parse Error**: Model in ra sai định dạng.
   2. **Hallucinated Tool**: Tự gọi tool không có thật.
   3. **Hallucinated Args**: Truyền sai dữ liệu hoặc bịa ra tham số không tồn tại.
   4. **Empty Observation**: Tool trả về không có dữ liệu nhưng Agent không biết cách rẽ nhánh tiếp.
   5. **Timeout/Loop**: Agent bị mắc kẹt, liên tục gọi một tool không hồi kết.


Đánh giá chất lượng của Agent không thể chỉ nhìn kết quả cuối. Cần **Eval-by-Trace**:

  - Đo lường *Tokens* và *Latency*.
  - Đếm số vòng lặp (*Loop count*).
  - Ghi log (Telemetry) ở mỗi bước để xác định chính xác Agent sai ở "Reasoning" hay do "Tool Result".

## 7. Thực Hành Lab 3 & Material

  - **Lab 3**: Xây dựng Chatbot baseline và nâng cấp lên ReAct Agent cho e-commerce (check_stock, get_discount, calc_shipping).
  - **Failure Analysis**: Học viên được yêu cầu đọc log JSON để tìm lỗi (parse error, hallucinated tool) và cải thiện Tool Description.
  - Đánh giá khả năng của Agent thông qua việc thảo luận nhóm (Discord activity) về các trường hợp sử dụng tối ưu.

---

Câu hỏi ôn tập Ngày 3

   Theo nội dung bài giảng, yếu tố nào sau đây **không** thuộc 4 tiêu chí của Agentic Fit Framework?
   - A. Lập luận nhiều bước
   - B. Tương tác công cụ
   - C. Phản hồi một lượt
   - D. Tầm nhìn dài
   **Đáp án / Answer:** C

   Trong ReAct pattern, thành phần nào đại diện cho bước "quan sát kết quả của hành động"?
   - A. Suy nghĩ
   - B. Hành động
   - C. Quan sát
   - D. Bộ nhớ
   **Đáp án / Answer:** C

   Ưu điểm chính của Native Tool Calling so với Text-ReAct là gì?
   - A. Tiêu tốn ít token hơn
   - B. Bắt buộc model tự sinh văn bản định dạng
   - C. Tăng tính ổn định nhờ JSON schema chuẩn từ API provider
   - D. Cho phép agent tự tạo tool mới
   **Đáp án / Answer:** C

   Loại lỗi nào xảy ra khi agent liên tục gọi một tool không hồi kết, không thoát được vòng lặp?
   - A. Công cụ tạo ảo giác
   - B. Quan sát trống
   - C. Hết thời gian/Vòng lặp
   - D. Lỗi phân tích
   **Đáp án / Answer:** C

   Để đánh giá chất lượng Agent, phương pháp nào được đề xuất thay vì chỉ nhìn kết quả cuối?
   - A. Đánh giá theo vết (đo tokens, độ trễ, số vòng lặp)
   - B. Kiểm tra mù với người dùng
   - C. So sánh với bot dựa trên quy tắc
   - D. Chỉ kiểm tra độ chính xác của tool
   **Đáp án / Answer:** A
