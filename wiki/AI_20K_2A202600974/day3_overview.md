---
type: overview
title: "Day 3 Overview - Từ Chatbot đến Agentic Agent"
description: "Kiến trúc của Agent, ReAct Pattern, Function Calling và quy trình xây dựng Agent thực tế."
tags: [ai, 20k, day3]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/3/day03-tu-chatbot-den-agentic-agent-react-v7.pdf"]
---

# Day 3: Từ Chatbot Đến Agentic Agent

## 1. 3 Kiểu Hệ Thống AI
- **Rule-based Bot**: Logic tĩnh (if/else), không gọi LLM, kiểm soát dễ nhưng thiếu linh hoạt.
- **LLM Chatbot**: Dùng LLM sinh câu trả lời mượt mà, nhưng thường chỉ đáp ứng tác vụ 1 lượt, dễ bị Hallucination.
- **Agent**: LLM hoạt động theo chu trình `Plan -> Act -> Observe -> Adapt`. Khả năng dùng Tools để lấy dữ liệu thực và quyết định linh hoạt nhiều bước. 

## 2. Agentic Fit Framework
Framework gồm 4 tiêu chí đánh giá khi nào cần sử dụng Agent:
1. **Multi-step Reasoning**: Bài toán chia thành nhiều bước phụ thuộc nhau.
2. **Tool Interaction**: Hệ thống cần sử dụng API, DB, Web Search,...
3. **Dynamic Decision**: Mỗi bước tiếp theo phụ thuộc kết quả bước trước.
4. **Long Horizon**: Giữ mục tiêu xuyên suốt qua nhiều vòng lặp.

## 3. Kiến Trúc Agent (Perception, Reasoning, Action, Memory)
- **Perception**: Agent nhận input (từ user, tools, feedback).
- **Reasoning**: LLM Core phân tích và chọn hành động tiếp theo.
- **Action**: Gọi tools và xuất câu trả lời.
- **Memory**: Gồm *Short-term* (Context window, chứa lịch sử hội thoại gần nhất) và *Long-term* (Cơ sở dữ liệu, Vector Store, chứa kiến thức và user profile).

## 4. ReAct Pattern (Reasoning + Acting)
Vòng lặp ReAct giúp LLM suy luận theo từng bước:
- **Thought**: Suy nghĩ cần làm gì tiếp theo.
- **Action**: Quyết định gọi công cụ gì với tham số nào.
- **Observation**: Quan sát kết quả từ công cụ trả về.
- Vòng lặp dừng khi thu thập đủ thông tin để đưa ra Final Answer. Điểm mạnh là giúp debug dễ dàng vì agent bộc lộ cách suy luận ra ngoài.

## 5. ReAct vs Native Function Calling
- **ReAct text-based**: Yêu cầu LLM trả về text có định dạng (thường là regex), dễ vỡ.
- **Native Function Calling**: LLM xuất ra JSON có cấu trúc để gọi hàm, ổn định hơn. Hiện tại ở môi trường production nên dùng *Hybrid* (Function Calling + Reasoning trace).

## 6. Agent Loop & Debugging
- Vòng lặp Agent cần cơ chế an toàn (Guardrails) như: Giới hạn số vòng lặp (Max Iterations), Timeout, Quản lý lỗi (Error Handling, Graceful Degradation) và Fallback khi các công cụ bị hỏng.
- Evaluation cho Agent phức tạp hơn Chatbot: Không chỉ đánh giá câu trả lời cuối, mà còn đánh giá chất lượng suy luận, chọn công cụ, tham số và điều kiện dừng.
