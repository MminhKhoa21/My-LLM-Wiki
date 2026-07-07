---
type: summary
title: "Day 3 Track 1: Từ Chatbot Đến Agentic Agent (v7 & Material)"
description: "Slide bài giảng chi tiết Ngày 3 về việc nâng cấp từ Chatbot lên Agentic Agent sử dụng ReAct pattern và Tool Calling."
tags: [ai, 20k, day3, track1, agent, react, chatbot, tool-calling]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/3/day03-tu-chatbot-den-agentic-agent-react-v7.pdf", "raw/AI_20K_2A202600974/3/day3-material.pdf"]
---
# Day 3 Track 1: Từ Chatbot Đến Agentic Agent  

Tài liệu này tổng hợp kiến thức từ slide bài giảng Ngày 3 (v7) và các bài tập thực hành (material). Nội dung tập trung vào việc định hình các hệ thống AI, kiến trúc Agent, pattern ReAct, và các nguyên tắc thiết kế an toàn.  

## 1. 3 Kiểu Hệ Thống AI  
- **Rule-based Bot**: Dựa trên logic if/else cứng, dễ đoán, chi phí thấp, linh hoạt kém (VD: Tổng đài IVR).  
- **LLM Chatbot**: Khả năng sinh văn bản tốt theo context, tập trung vào hội thoại 1 lượt (reactive). Nguy cơ Hallucination cao hơn.  
- **Agent**: Chủ động định hướng theo mục tiêu (Goal-driven). Lặp qua `Plan -> Act -> Observe -> Adapt`. Tích hợp khả năng sử dụng Tools, xử lý bài toán nhiều bước phức tạp (Booking, Coding assistant).  

4 tiêu chí để quyết định có nên dùng Agent:  
1. **Multi-step Reasoning**: Đòi hỏi suy luận qua nhiều bước phụ thuộc lẫn nhau.  
2. **Tool Interaction**: Tương tác với môi trường bên ngoài (API, DB, Web search).  
3. **Dynamic Decision**: Bước tiếp theo phụ thuộc vào kết quả quan sát được từ bước trước.  
4. **Long Horizon**: Cần duy trì mục tiêu dài hạn.  

> Luôn benchmark với Rule-based hoặc Chatbot trước khi áp dụng Agent để tránh Overkill. Nếu bài toán chỉ cần 1 bước và không có tools, Chatbot (hoặc RAG) là đủ.  
>   

## 3. Kiến Trúc Agent  
Một Agent gồm 4 khối chính:  
- **Perception**: Cổng tiếp nhận input từ user và môi trường (tools).  
- **Reasoning**: Khối xử lý cốt lõi (LLM Core).  
- **Action**: Ra quyết định và gọi tools (API) hoặc trả kết quả.  
  - *Short-term*: Trong context window, phục vụ task hiện tại.  
  - *Long-term*: Trong Store/Vector DB, lưu trữ thông tin lâu dài (facts, preferences).  

ReAct giúp Agent suy luận theo từng bước:  
- **Thought**: Suy nghĩ cần làm gì tiếp theo.  
- **Action**: Gọi tool nào với tham số gì.  
- **Observation**: Quan sát kết quả từ tool.  
- Điểm mạnh lớn nhất của ReAct là tính **Debuggable**: Các bước suy luận được hiển thị rõ, cho phép người dùng can thiệp và đánh giá quá trình thay vì chỉ nhìn kết quả cuối.  

- **Text-based ReAct (2022)**: LLM sinh ra text định dạng. Dễ bị vỡ (parse error).  
- **Native Function Calling (2023)**: LLM trả về JSON có cấu trúc.  
- **Hybrid (2024+)**: Kết hợp Function Calling (cho độ ổn định) và Reasoning Trace (để dễ debug). Đây là kiến trúc tối ưu cho môi trường Production.  

- Vòng lặp Agent cần được kiểm soát bằng:  
  - **Max Iterations**: Ngăn lặp vô hạn.  
  - **Timeout/Error Handling**: Xử lý Graceful Degradation khi tool hỏng.  
  - Đánh đổi giữa tính tự chủ và chi phí (Agent đắt và chậm hơn Chatbot).  
  - Nguy cơ Prompt Injection từ tool output. Cần áp dụng 3 lớp Guard: Input Guard, Tool Guard, và Output Guard.  

## 7. Thực Hành Lab 3 & Hoạt Động (Material)  
- Tham gia hoạt động nhóm: Chấm điểm use case theo Agentic Fit.  
- Xác định các yếu tố tăng/giảm khả năng dùng tool đúng của Agent (chất lượng tool description, số lượng tool).  
- **Thực hành Lab**: Xây dựng Chatbot baseline và nâng cấp lên ReAct Agent cho e-commerce (check_stock, get_discount, calc_shipping).  
- **Evaluation**: Đánh giá dựa trên Trace (Token, Latency, Loop Count, Reasoning Quality) thay vì chỉ đánh giá Final Answer.  
