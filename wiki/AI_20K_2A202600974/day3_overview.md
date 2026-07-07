---
type: overview
title: "Day 3 Overview - Từ Chatbot đến Agentic Agent"
description: "Kiến trúc của Agent, ReAct Pattern, Function Calling và quy trình xây dựng Agent thực tế."
tags: [ai, 20k, day3]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/3/day03-tu-chatbot-den-agentic-agent-react-v7.pdf"]
---

# Day 3: Từ Chatbot Đến Agentic Agent
# Day 3: From Chatbot to Agentic Agent

## 1. 3 Kiểu Hệ Thống AI
## 1. 3 Types of AI Systems
- **Rule-based Bot**: Logic tĩnh (if/else), không gọi LLM, kiểm soát dễ nhưng thiếu linh hoạt.
- **Rule-based Bot**: Static logic (if/else), no LLM calls, easy to control but lacks flexibility.
- **LLM Chatbot**: Dùng LLM sinh câu trả lời mượt mà, nhưng thường chỉ đáp ứng tác vụ 1 lượt, dễ bị Hallucination.
- **LLM Chatbot**: Uses LLM to generate fluent responses, but typically handles only single-turn tasks, prone to Hallucination.
- **Agent**: LLM hoạt động theo chu trình `Plan -> Act -> Observe -> Adapt`. Khả năng dùng Tools để lấy dữ liệu thực và quyết định linh hoạt nhiều bước. 
- **Agent**: LLM operates in a `Plan -> Act -> Observe -> Adapt` loop. Ability to use Tools to fetch real data and make flexible multi-step decisions.

## 2. Agentic Fit Framework
## 2. Agentic Fit Framework
Framework gồm 4 tiêu chí đánh giá khi nào cần sử dụng Agent:

The framework consists of 4 criteria to evaluate when to use an Agent:
1. **Multi-step Reasoning**: Bài toán chia thành nhiều bước phụ thuộc nhau.
1. **Multi-step Reasoning**: The problem is divided into multiple interdependent steps.
2. **Tool Interaction**: Hệ thống cần sử dụng API, DB, Web Search,...
2. **Tool Interaction**: The system needs to use APIs, DBs, Web Search, etc.
3. **Dynamic Decision**: Mỗi bước tiếp theo phụ thuộc kết quả bước trước.
3. **Dynamic Decision**: Each subsequent step depends on the result of the previous step.
4. **Long Horizon**: Giữ mục tiêu xuyên suốt qua nhiều vòng lặp.
4. **Long Horizon**: Maintains the objective across multiple iterations.

## 3. Kiến Trúc Agent (Perception, Reasoning, Action, Memory)
## 3. Agent Architecture (Perception, Reasoning, Action, Memory)
- **Perception**: Agent nhận input (từ user, tools, feedback).
- **Perception**: The agent receives input (from users, tools, feedback).
- **Reasoning**: LLM Core phân tích và chọn hành động tiếp theo.
- **Reasoning**: The LLM Core analyzes and selects the next action.
- **Action**: Gọi tools và xuất câu trả lời.
- **Action**: Calls tools and outputs the response.
- **Memory**: Gồm *Short-term* (Context window, chứa lịch sử hội thoại gần nhất) và *Long-term* (Cơ sở dữ liệu, Vector Store, chứa kiến thức và user profile).
- **Memory**: Consists of *Short-term* (Context window, containing recent conversation history) and *Long-term* (Databases, Vector Stores, containing knowledge and user profiles).

## 4. ReAct Pattern (Reasoning + Acting)
## 4. ReAct Pattern (Reasoning + Acting)
Vòng lặp ReAct giúp LLM suy luận theo từng bước:

The ReAct loop helps the LLM reason step-by-step:
- **Thought**: Suy nghĩ cần làm gì tiếp theo.
- **Thought**: Thinking about what to do next.
- **Action**: Quyết định gọi công cụ gì với tham số nào.
- **Action**: Deciding which tool to call and with what parameters.
- **Observation**: Quan sát kết quả từ công cụ trả về.
- **Observation**: Observing the results returned by the tool.
- Vòng lặp dừng khi thu thập đủ thông tin để đưa ra Final Answer. Điểm mạnh là giúp debug dễ dàng vì agent bộc lộ cách suy luận ra ngoài.
- The loop stops when enough information is gathered to provide the Final Answer. Its strength is making debugging easier because the agent's reasoning process is exposed.

## 5. ReAct vs Native Function Calling
## 5. ReAct vs Native Function Calling
- **ReAct text-based**: Yêu cầu LLM trả về text có định dạng (thường là regex), dễ vỡ.
- **ReAct text-based**: Requires the LLM to return formatted text (usually parsed by regex), which is fragile.
- **Native Function Calling**: LLM xuất ra JSON có cấu trúc để gọi hàm, ổn định hơn. Hiện tại ở môi trường production nên dùng *Hybrid* (Function Calling + Reasoning trace).
- **Native Function Calling**: The LLM outputs structured JSON to call functions, which is more stable. Currently, in production environments, a *Hybrid* approach (Function Calling + Reasoning trace) should be used.

## 6. Agent Loop & Debugging
## 6. Agent Loop & Debugging
- Vòng lặp Agent cần cơ chế an toàn (Guardrails) như: Giới hạn số vòng lặp (Max Iterations), Timeout, Quản lý lỗi (Error Handling, Graceful Degradation) và Fallback khi các công cụ bị hỏng.
- The Agent loop needs safety mechanisms (Guardrails) such as: Limiting the number of loops (Max Iterations), Timeouts, Error Handling (Graceful Degradation), and Fallbacks when tools fail.
- Evaluation cho Agent phức tạp hơn Chatbot: Không chỉ đánh giá câu trả lời cuối, mà còn đánh giá chất lượng suy luận, chọn công cụ, tham số và điều kiện dừng.
- Evaluation for Agents is more complex than for Chatbots: It not only evaluates the final answer but also evaluates the reasoning quality, tool selection, parameters, and stopping conditions.
