---
type: summary
title: "Day 3 Track 1: Từ Chatbot Đến Agentic Agent (v7 & Material)"
description: "Slide bài giảng chi tiết Ngày 3 về việc nâng cấp từ Chatbot lên Agentic Agent sử dụng ReAct pattern và Tool Calling."
tags: [ai, 20k, day3, track1, agent, react, chatbot, tool-calling]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/3/day03-tu-chatbot-den-agentic-agent-react-v7.pdf", "raw/AI_20K_2A202600974/3/day3-material.pdf"]
---

# Day 3 Track 1: Từ Chatbot Đến Agentic Agent
# Day 3 Track 1: From Chatbot To Agentic Agent

Tài liệu này tổng hợp kiến thức từ slide bài giảng Ngày 3 (v7) và các bài tập thực hành (material). Nội dung tập trung vào việc định hình các hệ thống AI, kiến trúc Agent, pattern ReAct, và các nguyên tắc thiết kế an toàn.
This document summarizes the knowledge from the Day 3 lecture slides (v7) and practical exercises (material). The content focuses on shaping AI systems, Agent architecture, the ReAct pattern, and safe design principles.

## 1. 3 Kiểu Hệ Thống AI
## 1. 3 Types of AI Systems
- **Rule-based Bot**: Dựa trên logic if/else cứng, dễ đoán, chi phí thấp, linh hoạt kém (VD: Tổng đài IVR).
- **Rule-based Bot**: Based on rigid if/else logic, predictable, low cost, poor flexibility (e.g., IVR switchboard).
- **LLM Chatbot**: Khả năng sinh văn bản tốt theo context, tập trung vào hội thoại 1 lượt (reactive). Nguy cơ Hallucination cao hơn.
- **LLM Chatbot**: Good text generation capability according to context, focused on 1-turn conversation (reactive). Higher risk of Hallucination.
- **Agent**: Chủ động định hướng theo mục tiêu (Goal-driven). Lặp qua `Plan -> Act -> Observe -> Adapt`. Tích hợp khả năng sử dụng Tools, xử lý bài toán nhiều bước phức tạp (Booking, Coding assistant).
- **Agent**: Proactively goal-driven. Loops through `Plan -> Act -> Observe -> Adapt`. Integrates the ability to use Tools, solving complex multi-step problems (Booking, Coding assistant).

## 2. Agentic Fit Framework
## 2. Agentic Fit Framework
4 tiêu chí để quyết định có nên dùng Agent:
4 criteria to decide whether to use an Agent:
1. **Multi-step Reasoning**: Đòi hỏi suy luận qua nhiều bước phụ thuộc lẫn nhau.
1. **Multi-step Reasoning**: Requires reasoning through multiple interdependent steps.
2. **Tool Interaction**: Tương tác với môi trường bên ngoài (API, DB, Web search).
2. **Tool Interaction**: Interacts with the external environment (API, DB, Web search).
3. **Dynamic Decision**: Bước tiếp theo phụ thuộc vào kết quả quan sát được từ bước trước.
3. **Dynamic Decision**: The next step depends on the results observed from the previous step.
4. **Long Horizon**: Cần duy trì mục tiêu dài hạn.
4. **Long Horizon**: Needs to maintain long-term goals.

> [!TIP]
> Luôn benchmark với Rule-based hoặc Chatbot trước khi áp dụng Agent để tránh Overkill. Nếu bài toán chỉ cần 1 bước và không có tools, Chatbot (hoặc RAG) là đủ.
> 
> Always benchmark with a Rule-based system or Chatbot before applying an Agent to avoid overkill. If the problem only requires 1 step and no tools, a Chatbot (or RAG) is sufficient.

## 3. Kiến Trúc Agent
## 3. Agent Architecture
Một Agent gồm 4 khối chính:
An Agent consists of 4 main blocks:
- **Perception**: Cổng tiếp nhận input từ user và môi trường (tools).
- **Perception**: Gateway to receive input from the user and environment (tools).
- **Reasoning**: Khối xử lý cốt lõi (LLM Core).
- **Reasoning**: Core processing block (LLM Core).
- **Action**: Ra quyết định và gọi tools (API) hoặc trả kết quả.
- **Action**: Makes decisions and calls tools (API) or returns results.
- **Memory**: 
- **Memory**: 
  - *Short-term*: Trong context window, phục vụ task hiện tại.
  - *Short-term*: In the context window, serves the current task.
  - *Long-term*: Trong Store/Vector DB, lưu trữ thông tin lâu dài (facts, preferences).
  - *Long-term*: In Store/Vector DB, stores long-term information (facts, preferences).

## 4. ReAct Pattern (Reasoning + Acting)
## 4. ReAct Pattern (Reasoning + Acting)
ReAct giúp Agent suy luận theo từng bước:
ReAct helps the Agent reason step-by-step:
- **Thought**: Suy nghĩ cần làm gì tiếp theo.
- **Thought**: Thinking about what to do next.
- **Action**: Gọi tool nào với tham số gì.
- **Action**: Which tool to call and with what parameters.
- **Observation**: Quan sát kết quả từ tool.
- **Observation**: Observing the results from the tool.
- Điểm mạnh lớn nhất của ReAct là tính **Debuggable**: Các bước suy luận được hiển thị rõ, cho phép người dùng can thiệp và đánh giá quá trình thay vì chỉ nhìn kết quả cuối.
- The biggest strength of ReAct is its **Debuggable** nature: The reasoning steps are clearly displayed, allowing users to intervene and evaluate the process instead of just looking at the final result.

## 5. ReAct vs Function Calling
## 5. ReAct vs Function Calling
- **Text-based ReAct (2022)**: LLM sinh ra text định dạng. Dễ bị vỡ (parse error).
- **Text-based ReAct (2022)**: LLM generates formatted text. Prone to breaking (parse error).
- **Native Function Calling (2023)**: LLM trả về JSON có cấu trúc.
- **Native Function Calling (2023)**: LLM returns structured JSON.
- **Hybrid (2024+)**: Kết hợp Function Calling (cho độ ổn định) và Reasoning Trace (để dễ debug). Đây là kiến trúc tối ưu cho môi trường Production.
- **Hybrid (2024+)**: Combines Function Calling (for stability) and Reasoning Trace (for easy debugging). This is the optimal architecture for Production environments.

## 6. Agent Loop & Safeguards
## 6. Agent Loop & Safeguards
- Vòng lặp Agent cần được kiểm soát bằng:
- The Agent loop needs to be controlled by:
  - **Max Iterations**: Ngăn lặp vô hạn.
  - **Max Iterations**: Prevents infinite loops.
  - **Timeout/Error Handling**: Xử lý Graceful Degradation khi tool hỏng.
  - **Timeout/Error Handling**: Handles Graceful Degradation when tools fail.
- **Cost & Security**: 
- **Cost & Security**: 
  - Đánh đổi giữa tính tự chủ và chi phí (Agent đắt và chậm hơn Chatbot).
  - Trade-off between autonomy and cost (Agents are more expensive and slower than Chatbots).
  - Nguy cơ Prompt Injection từ tool output. Cần áp dụng 3 lớp Guard: Input Guard, Tool Guard, và Output Guard.
  - Risk of Prompt Injection from tool output. Need to apply 3 Guard layers: Input Guard, Tool Guard, and Output Guard.

## 7. Thực Hành Lab 3 & Hoạt Động (Material)
## 7. Lab 3 Practice & Activities (Material)
- Tham gia hoạt động nhóm: Chấm điểm use case theo Agentic Fit.
- Join group activities: Score use cases according to Agentic Fit.
- Xác định các yếu tố tăng/giảm khả năng dùng tool đúng của Agent (chất lượng tool description, số lượng tool).
- Identify factors that increase/decrease the Agent's ability to use tools correctly (quality of tool description, number of tools).
- **Thực hành Lab**: Xây dựng Chatbot baseline và nâng cấp lên ReAct Agent cho e-commerce (check_stock, get_discount, calc_shipping).
- **Lab Practice**: Build a Chatbot baseline and upgrade to a ReAct Agent for e-commerce (check_stock, get_discount, calc_shipping).
- **Evaluation**: Đánh giá dựa trên Trace (Token, Latency, Loop Count, Reasoning Quality) thay vì chỉ đánh giá Final Answer.
- **Evaluation**: Evaluate based on Trace (Token, Latency, Loop Count, Reasoning Quality) instead of just the Final Answer.
