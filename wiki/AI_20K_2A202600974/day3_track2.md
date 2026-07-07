---
type: summary
title: "Day 3 Track 2: Từ Chatbot Đến Agentic Agent (Manh)"
description: "Slide bài giảng Ngày 3 do giảng viên Phạm Mạnh trình bày về quá trình nâng cấp hệ thống AI từ Rule-based đến Agentic Agent."
tags: [ai, 20k, day3, track2, agent, react, chatbot]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/3/day03-tu-chatbot-den-agentic-agent-react_manh_v2.pdf", "raw/AI_20K_2A202600974/3/day3-material.pdf"]
---

# Day 3 Track 2: Từ Chatbot Đến Agentic Agent
# Day 3 Track 2: From Chatbot To Agentic Agent

Tài liệu này tóm tắt bài giảng Ngày 3 dựa trên phiên bản slide của GV Phạm Mạnh và các hoạt động lớp học. Bài giảng hướng dẫn cách xác định khi nào cần sử dụng Agent và kiến trúc cơ bản để xây dựng hệ thống Agent hiệu quả.
This document summarizes the Day 3 lecture based on instructor Pham Manh's slides and classroom activities. The lecture guides how to determine when to use an Agent and the basic architecture to build an effective Agent system.

## 1. 3 Kiểu Hệ Thống AI
## 1. 3 Types of AI Systems
Hệ thống AI được phân làm 3 cấp độ:
AI systems are classified into 3 levels:
- **Rule-based Bot**: Hoạt động dựa trên các quy tắc cố định (If/else), không gọi LLM, tính linh hoạt thấp.
- **Rule-based Bot**: Operates based on fixed rules (If/else), does not call LLM, low flexibility.
- **LLM Chatbot**: Trả lời thông minh theo context nhưng mang tính chất phản ứng (reactive), thiếu vòng lặp tư duy dài hạn.
- **LLM Chatbot**: Answers intelligently based on context but is reactive in nature, lacking a long-term reasoning loop.
- **Agent**: Hoạt động theo vòng lặp sử dụng tools và quan sát từng bước. Có thể giải quyết mục tiêu dài hạn (long-horizon goal) qua nhiều quyết định liên tiếp.
- **Agent**: Operates in a loop using tools and observing step-by-step. Can solve long-horizon goals through multiple consecutive decisions.

## 2. Khi Nào Cần Agent? (Agentic Fit)
## 2. When is an Agent Needed? (Agentic Fit)
Dùng Agentic Fit Framework để đánh giá với 4 tiêu chí:
Use the Agentic Fit Framework to evaluate with 4 criteria:
1. **Multi-step Reasoning**
1. **Multi-step Reasoning**
2. **Tool Interaction**
2. **Tool Interaction**
3. **Dynamic Decision**
3. **Dynamic Decision**
4. **Long Horizon**
4. **Long Horizon**

> [!WARNING]
> Không nên dùng Agent nếu bài toán chỉ có 1 bước đơn giản, yêu cầu deterministic tuyệt đối, không có tools để tương tác, hoặc đòi hỏi thời gian phản hồi (latency) cực ngắn.
> 
> Do not use an Agent if the problem is a simple 1-step task, requires absolute determinism, has no tools to interact with, or requires extremely short response latency.

## 3. Kiến Trúc Agent
## 3. Agent Architecture
- **Perception**: Đầu vào (Input) từ user và tool results.
- **Perception**: Input from user and tool results.
- **Reasoning**: Cốt lõi của mô hình (LLM Core) để đưa ra quyết định.
- **Reasoning**: The core of the model (LLM Core) for making decisions.
- **Action**: Thực hiện tác vụ (API, Exploration tool).
- **Action**: Executes the task (API, Exploration tool).
- **Memory**: Ngắn hạn (Context window) và dài hạn (Store/DB). Memory chỉ hiệu quả khi có chiến lược đọc/ghi rõ ràng.
- **Memory**: Short-term (Context window) and long-term (Store/DB). Memory is only effective with a clear read/write strategy.

## 4. ReAct Pattern (Reasoning + Acting)
## 4. ReAct Pattern (Reasoning + Acting)
- Vòng lặp: `Thought` (Suy nghĩ bước tiếp) -> `Action` (Gọi tool) -> `Observation` (Kết quả trả về).
- Loop: `Thought` (Think next step) -> `Action` (Call tool) -> `Observation` (Result returned).
- **Lợi ích**: Tăng khả năng gỡ lỗi (debug) nhờ vào trace hành động minh bạch.
- **Benefits**: Increases debugging capability thanks to a transparent action trace.
- **LangGraph Integration**: Bài giảng định hướng từ vòng lặp ReAct truyền thống (code thủ công) sẽ được phát triển lên graph approach bằng LangGraph ở các bài sau để quản lý state và routing tốt hơn.
- **LangGraph Integration**: The lecture points from the traditional ReAct loop (manual code) towards developing a graph approach using LangGraph in later lessons to better manage state and routing.

## 5. Agent Loop & Troubleshooting
## 5. Agent Loop & Troubleshooting
- **Code Anatomy**: Thiết lập system prompt chặt chẽ, đăng ký tools rõ ràng (Tool Registry) với mô tả chi tiết, và cài đặt Max Iterations.
- **Code Anatomy**: Set up strict system prompts, clearly register tools (Tool Registry) with detailed descriptions, and configure Max Iterations.
- **Debug Checklist**:
- **Debug Checklist**:
  - Xem xét Thought có đúng mục tiêu không.
  - Check if Thought aligns with the goal.
  - Kiểm tra Agent có chọn sai tool hoặc truyền tham số sai.
  - Check if the Agent selected the wrong tool or passed wrong parameters.
  - Khắc phục bằng cách cải thiện Tool description hoặc cài đặt fallback retry.
  - Fix by improving Tool description or configuring fallback retry.

## 6. Bài Tập Nhóm & Lab 3
## 6. Group Exercises & Lab 3
- Chấm điểm use case tự chọn bằng Agentic Fit (đăng lên Discord).
- Score a chosen use case using Agentic Fit (post to Discord).
- Thực hành phân tích các yếu tố tăng/giảm khả năng chọn tool của Agent (VD: tool description rõ ràng).
- Practice analyzing factors that increase/decrease the Agent's tool selection capability (e.g., clear tool description).
- Nâng cấp Chatbot baseline thành ReAct agent với tối thiểu 1-2 tools cho use case.
- Upgrade the baseline Chatbot to a ReAct agent with at least 1-2 tools for the use case.
- Chạy 5 test cases so sánh và vẽ flowchart thể hiện ưu thế của Agent trong những ngữ cảnh phức tạp.
- Run 5 comparison test cases and draw a flowchart illustrating the Agent's advantages in complex contexts.
