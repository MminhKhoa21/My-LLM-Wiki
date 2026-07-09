---
type: summary
title: "Day 3 Track 2: Từ Chatbot Đến Agentic Agent (Manh)"
description: "Slide bài giảng Ngày 3 do giảng viên Phạm Mạnh trình bày về quá trình nâng cấp hệ thống AI từ Rule-based đến Agentic Agent."
tags: [ai, 20k, day3, track2, agent, react, chatbot]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/3/day03-tu-chatbot-den-agentic-agent-react_manh_v2.pdf", "raw/AI_20K_2A202600974/3/day3-material.pdf"]
---
# *Day 3 Track 2: Từ Chatbot Đến Agentic Agent*

Tài liệu này tóm tắt bài giảng Ngày 3 dựa trên phiên bản slide của GV Phạm Mạnh và các hoạt động lớp học. Bài giảng hướng dẫn cách xác định khi nào cần sử dụng Agent và kiến trúc cơ bản để xây dựng hệ thống Agent hiệu quả.

## *1. 3 Kiểu Hệ Thống AI*

Hệ thống AI được phân làm 3 cấp độ:

  - **Rule-based Bot**: Hoạt động dựa trên các quy tắc cố định (If/else), không gọi LLM, tính linh hoạt thấp.

  - **LLM Chatbot**: Trả lời thông minh theo context nhưng mang tính chất phản ứng (reactive), thiếu vòng lặp tư duy dài hạn.

  - **Agent**: Hoạt động theo vòng lặp sử dụng tools và quan sát từng bước. Có thể giải quyết mục tiêu dài hạn (long-horizon goal) qua nhiều quyết định liên tiếp.

## *2. Khi Nào Cần Agent? (Agentic Fit)*

Dùng Agentic Fit Framework để đánh giá với 4 tiêu chí:

   1. **Multi-step Reasoning** (Lý luận đa bước)

   2. **Tool Interaction** (Tương tác công cụ)

   3. **Dynamic Decision** (Quyết định động)

   4. **Long Horizon** (Tầm nhìn dài hạn)

> *Không nên dùng Agent nếu bài toán chỉ có 1 bước đơn giản, yêu cầu deterministic tuyệt đối, không có tools để tương tác, hoặc đòi hỏi thời gian phản hồi (latency) cực ngắn.*

## *3. Kiến Trúc Agent*

  - **Perception**: Đầu vào (Input) từ user và tool results.

  - **Reasoning**: Cốt lõi của mô hình (LLM Core) để đưa ra quyết định.

  - **Action**: Thực hiện tác vụ (API, Exploration tool).

  - **Memory**: Ngắn hạn (Context window) và dài hạn (Store/DB). Memory chỉ hiệu quả khi có chiến lược đọc/ghi rõ ràng.


  - Vòng lặp: `Thought` (Suy nghĩ bước tiếp) -> `Action` (Gọi tool) -> `Observation` (Kết quả trả về).

  - **Lợi ích**: Tăng khả năng gỡ lỗi (debug) nhờ vào trace hành động minh bạch.

  - **LangGraph Integration**: Bài giảng định hướng từ vòng lặp ReAct truyền thống (code thủ công) sẽ được phát triển lên graph approach bằng LangGraph ở các bài sau để quản lý state và routing tốt hơn.


  - **Code Anatomy**: Thiết lập system prompt chặt chẽ, đăng ký tools rõ ràng (Tool Registry) với mô tả chi tiết, và cài đặt Max Iterations.


    - Xem xét Thought có đúng mục tiêu không.

    - Kiểm tra Agent có chọn sai tool hoặc truyền tham số sai.

    - Khắc phục bằng cách cải thiện Tool description hoặc cài đặt fallback retry.

## *6. Bài Tập Nhóm & Lab 3*

  - Chấm điểm use case tự chọn bằng Agentic Fit (đăng lên Discord).

  - Thực hành phân tích các yếu tố tăng/giảm khả năng chọn tool của Agent (VD: tool description rõ ràng).

  - Nâng cấp Chatbot baseline thành ReAct agent với tối thiểu 1-2 tools cho use case.

  - Chạy 5 test cases so sánh và vẽ flowchart thể hiện ưu thế của Agent trong những ngữ cảnh phức tạp.

---

### *Câu hỏi ôn tập Ngày 3*

   Theo bài giảng, điểm khác biệt chính giữa Agent và LLM Chatbot là gì?
     A. Agent không sử dụng mô hình ngôn ngữ lớn (LLM).
     B. Agent có vòng lặp tư duy dài hạn (long-horizon goal) và sử dụng tools để quan sát từng bước.
     C. LLM Chatbot có khả năng thực hiện nhiều quyết định liên tiếp hơn Agent.
     D. Agent chỉ hoạt động dựa trên quy tắc cố định (rule-based).
   ***Đáp án:** B*

   Tiêu chí nào sau đây KHÔNG thuộc bộ bốn tiêu chí của Agentic Fit Framework?
   ***Đáp án:** C*

   Trong ReAct Pattern, thứ tự đúng của một vòng lặp cơ bản là:
   ***Đáp án:** C*

   Khi gỡ lỗi (debug) Agent loop, bước đầu tiên nên kiểm tra là gì?
     A. Kiểm tra tool description có đủ chi tiết không.
     B. Xem xét "Thought" của Agent có đúng mục tiêu không.
     C. Cài đặt fallback retry ngay lập tức.
     D. Tăng số lượng tools tối đa.
   ***Đáp án:** B*
