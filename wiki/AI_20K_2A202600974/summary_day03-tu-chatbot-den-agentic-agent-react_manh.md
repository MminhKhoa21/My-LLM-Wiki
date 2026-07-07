---
type: summary
title: "Summary of day03-tu-chatbot-den-agentic-agent-react_manh.pdf"
description: "Tổng quan về Agentic AI, framework đánh giá Agentic Fit, kiến trúc Agent và mẫu thiết kế ReAct (Reasoning + Acting)."
tags: [ai, 20k, day03]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/3/day03-tu-chatbot-den-agentic-agent-react_manh.pdf"]
---

# Tóm tắt: Từ Chatbot Đến Agentic Agent (Design Pattern ReAct)
# Summary: From Chatbot to Agentic Agent (ReAct Design Pattern)

## 1. Spectrum: Từ Bot đến Agent
## 1. Spectrum: From Bot to Agent
Hệ thống AI không chỉ gói gọn trong một loại mà phân chia thành các cấp độ từ thấp lên cao:
*AI systems are not confined to a single type but are divided into levels from low to high:*
- **Rule-based Bot:** Bot hoạt động dựa trên luật if/else cố định.
  *(Rule-based Bot: Bots operate based on fixed if/else rules.)*
- **LLM Chatbot:** Sinh câu trả lời mượt mà, hiểu context nhưng thường chỉ thao tác 1 lượt, không có khả năng chủ động tìm kiếm dữ liệu thực tế.
  *(LLM Chatbot: Generates smooth responses, understands context but usually only operates in a single turn, lacking the ability to actively search for real-world data.)*
- **Reactive Agent:** Kết hợp sử dụng công cụ (tool use) + khả năng lặp lại quan sát theo từng bước (loop).
  *(Reactive Agent: Combines tool use with the ability to repeat step-by-step observations in a loop.)*
- **Autonomous Agent:** Theo đuổi mục tiêu dài hạn với nhiều quyết định liên tiếp và có trí nhớ (memory).
  *(Autonomous Agent: Pursues long-term goals with multiple consecutive decisions and has memory.)*

## 2. Agentic Fit Framework (Khi nào nên dùng Agent?)
## 2. Agentic Fit Framework (When to use an Agent?)
Đánh giá độ phức tạp qua 4 tiêu chí:
*Assess complexity through 4 criteria:*
1. **Multi-step Reasoning:** Có cần suy luận logic nhiều bước không?
   *(Multi-step Reasoning: Is multi-step logical reasoning required?)*
2. **Tool Interaction:** Có cần gọi external APIs, DBs hay search không?
   *(Tool Interaction: Do you need to call external APIs, DBs, or perform searches?)*
3. **Dynamic Decision:** Tùy từng bước mà thay đổi hành động dựa trên kết quả trả về không?
   *(Dynamic Decision: Do actions need to change step-by-step based on returned results?)*
4. **Long Horizon:** Có cần lưu trạng thái qua nhiều vòng lặp dài không?
   *(Long Horizon: Is it necessary to save states across multiple long loops?)*
*Lưu ý:* Luôn benchmark bằng Rule/Chatbot trước khi dùng đến Agent vì Agent tốn chi phí và phức tạp hơn.
*(Note: Always benchmark with a Rule-based bot or Chatbot before using an Agent, because Agents are more costly and complex.)*

## 3. Kiến trúc của một Agent
## 3. Architecture of an Agent
Gồm 4 khối cốt lõi:
*Consists of 4 core blocks:*
- **Perception (Nhận thức):** Tiếp nhận input từ user và kết quả từ các tool.
  *(Perception: Receives input from the user and results from tools.)*
- **Reasoning (Suy luận):** Bộ não LLM phân tích trạng thái để chọn bước đi tiếp theo.
  *(Reasoning: The LLM brain analyzes the state to choose the next step.)*
- **Action (Hành động):** Gọi tools (Search, API) hoặc trả lời cho người dùng.
  *(Action: Calls tools like Search, APIs, or replies to the user.)*
- **Memory (Trí nhớ):** Gồm *Short-term* (nằm trong context window) và *Long-term* (Vector DB, DB truyền thống để lưu trữ dài hạn).
  *(Memory: Includes Short-term (within the context window) and Long-term (Vector DB, traditional DB for long-term storage).)*

## 4. Mẫu thiết kế ReAct (Reasoning + Acting)
## 4. ReAct Design Pattern (Reasoning + Acting)
Là pattern kết hợp giữa tư duy theo từng bước và hành động gọi công cụ. Thay vì vội trả lời, Agent sẽ lặp lại chu kỳ sau:
*A pattern that combines step-by-step thinking with tool-calling actions. Instead of rushing to answer, the Agent repeats the following cycle:*
- **Thought (Suy nghĩ):** "Mình đang thiếu gì, mình cần làm gì?"
  *(Thought: "What am I missing, what do I need to do?")*
- **Action (Hành động):** Gọi tool nào với tham số nào?
  *(Action: Which tool to call with what parameters?)*
- **Observation (Quan sát):** Kết quả của tool đưa về là gì?
  *(Observation: What are the results returned by the tool?)*
*(Chu kỳ lặp lại cho tới khi thu thập đủ dữ kiện để đưa ra "Final Answer")*
*(The cycle repeats until enough data is collected to provide a "Final Answer")*

> **Ưu điểm của ReAct:** Traces rõ ràng, dễ debug, dễ phát hiện xem Agent chọn sai tool hay bị rơi vào vòng lặp vô hạn.
> *(Advantages of ReAct: Clear traces, easy to debug, easy to detect if the Agent chooses the wrong tool or falls into an infinite loop.)*

## 5. Agent Loop & Debugging
## 5. Agent Loop & Debugging
- **Safeguard (Bảo vệ):** Cần thiết lập giới hạn vòng lặp (Max Iterations), timeouts, chi phí token, và fallback.
  *(Safeguard: Need to set loop limits (Max Iterations), timeouts, token costs, and fallbacks.)*
- **LangGraph:** Khi dự án lớn, ReAct vòng lặp tự viết sẽ khó quản lý. LangGraph hỗ trợ vẽ các luồng Graph (Nodes, Edges, State) để scale dễ dàng hơn.
  *(LangGraph: For large projects, custom ReAct loops are hard to manage. LangGraph supports drawing graph flows (Nodes, Edges, State) for easier scaling.)*
- **Hybrid Pattern:** Cách tiếp cận thực dụng là dùng Chatbot xử lý nhanh tác vụ đơn giản, khi nào cần multi-step mới chuyển sang hướng Agent.
  *(Hybrid Pattern: A pragmatic approach is to use a Chatbot for quickly handling simple tasks, switching to an Agent only when multi-step processing is needed.)*
