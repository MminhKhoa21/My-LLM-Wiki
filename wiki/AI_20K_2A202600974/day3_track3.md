---
type: summary
title: "Day 3 Track 3: Từ Chatbot Đến Agentic Agent (Hieu)"
description: "Slide bài giảng Ngày 3 do giảng viên Hiếu trình bày về sự tiến hóa từ chatbot sang agent và cơ chế ReAct."
tags: [ai, 20k, day3, track3, agent, react, chatbot]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/3/day03-tu-chatbot-den-agentic-agent-react_hieu_e403.pdf", "raw/AI_20K_2A202600974/3/day3-material.pdf"]
---

# Day 3 Track 3: Từ Chatbot Đến Agentic Agent
# Day 3 Track 3: From Chatbot To Agentic Agent

Tài liệu này tóm tắt slide bài giảng Ngày 3 (phiên bản GV Hiếu) kết hợp với các bài tập thực hành. Nội dung đi sâu vào việc phát triển Agent thông qua ReAct pattern, ứng dụng Native Tool Calling và cách thức phân tích lỗi (failure analysis).
This document summarizes the Day 3 lecture slides (instructor Hieu's version) combined with practical exercises. The content delves into developing Agents through the ReAct pattern, applying Native Tool Calling, and failure analysis methods.

## 1. Mức Độ Thông Minh Của Hệ Thống AI
## 1. Intelligence Level of AI Systems
- **Rule-based Bot**: Dựa trên quy tắc cố định (if/else), chi phí rẻ, giới hạn cao.
- **Rule-based Bot**: Based on fixed rules (if/else), cheap cost, highly limited.
- **LLM Chatbot**: Trả lời linh hoạt nhưng thường chỉ phản ứng tốt với hội thoại đơn lẻ. Nguy cơ tự bịa thông tin.
- **LLM Chatbot**: Answers flexibly but often only reacts well to single-turn conversations. Risk of hallucinating information.
- **Agent**: Định hướng theo mục tiêu (goal-driven). Sử dụng khả năng của LLM để quyết định gọi tool, đọc kết quả, rồi lặp lại để tiếp cận đích đến. 
- **Agent**: Goal-driven. Uses LLM's capability to decide on calling tools, reads the results, then loops to reach the destination.

## 2. Agentic Fit Framework
## 2. Agentic Fit Framework
Hướng dẫn đánh giá khi nào bài toán thực sự cần Agent với 4 tiêu chí cốt lõi:
Guide to evaluating when a problem truly needs an Agent using 4 core criteria:
1. **Multi-step Reasoning**
1. **Multi-step Reasoning**
2. **Tool Interaction**
2. **Tool Interaction**
3. **Dynamic Decision**
3. **Dynamic Decision**
4. **Long Horizon**
4. **Long Horizon**

## 3. Kiến Trúc Agent
## 3. Agent Architecture
- **Perception**: Tiếp nhận truy vấn từ người dùng và phản hồi từ tool.
- **Perception**: Receives queries from users and feedback from tools.
- **Reasoning**: Core xử lý tư duy (LLM), ra quyết định bước tiếp.
- **Reasoning**: Core reasoning processing (LLM), makes decisions for the next step.
- **Action**: Thực thi hành động bằng Native Tool Calling.
- **Action**: Executes actions using Native Tool Calling.
- **Memory**: 
- **Memory**: 
  - *Short-term*: Ngắn hạn trong Session/Context.
  - *Short-term*: Short-term in Session/Context.
  - *Long-term*: Nằm trong CSDL/Vector Store, duy trì facts theo thời gian.
  - *Long-term*: Resides in DB/Vector Store, maintains facts over time.

## 4. ReAct Pattern & Text-based vs Native
## 4. ReAct Pattern & Text-based vs Native
- **ReAct (Reasoning + Acting)**: Kết hợp việc lập luận (Thought) cùng hành động gọi công cụ (Action) và theo dõi kết quả (Observation). Ưu điểm chính là bộc lộ tư duy của AI giúp con người kiểm soát.
- **ReAct (Reasoning + Acting)**: Combines reasoning (Thought) with tool-calling actions (Action) and tracking results (Observation). The main advantage is exposing the AI's reasoning to help humans control it.
- **Text-ReAct (Cổ điển)**: Bắt model tự sinh văn bản định dạng (ví dụ `Action: get_weather()`), dễ bị gãy vỡ khi parsing (đặc biệt với local model nhỏ).
- **Text-ReAct (Classic)**: Forces the model to generate formatted text (e.g., `Action: get_weather()`), prone to breaking during parsing (especially with small local models).
- **Native Tool Calling (Hiện đại)**: LLM sinh ra output bằng JSON schema tiêu chuẩn từ API provider (như OpenAI), giúp tăng tính ổn định đáng kể.
- **Native Tool Calling (Modern)**: LLM generates output using standard JSON schema from API providers (like OpenAI), significantly increasing stability.

## 5. Failure Modes (5 Kiểu Lỗi Của Agent)
## 5. Failure Modes (5 Types of Agent Errors)
Trong quá trình code và debug, học viên sẽ thường xuyên gặp 5 lỗi:
During coding and debugging, students will frequently encounter 5 errors:
1. **Parse Error**: Model in ra sai định dạng.
1. **Parse Error**: The model prints in the wrong format.
2. **Hallucinated Tool**: Tự gọi tool không có thật.
2. **Hallucinated Tool**: Spontaneously calls a non-existent tool.
3. **Hallucinated Args**: Truyền sai dữ liệu hoặc bịa ra tham số không tồn tại.
3. **Hallucinated Args**: Passes wrong data or invents non-existent parameters.
4. **Empty Observation**: Tool trả về không có dữ liệu nhưng Agent không biết cách rẽ nhánh tiếp.
4. **Empty Observation**: The tool returns no data but the Agent doesn't know how to branch next.
5. **Timeout/Loop**: Agent bị mắc kẹt, liên tục gọi một tool không hồi kết.
5. **Timeout/Loop**: The Agent gets stuck, continuously calling a tool without an end.

## 6. Evaluation & Telemetry
## 6. Evaluation & Telemetry
Đánh giá chất lượng của Agent không thể chỉ nhìn kết quả cuối. Cần **Eval-by-Trace**:
Evaluating an Agent's quality cannot just look at the final result. It requires **Eval-by-Trace**:
- Đo lường *Tokens* và *Latency*.
- Measure *Tokens* and *Latency*.
- Đếm số vòng lặp (*Loop count*).
- Count the number of loops (*Loop count*).
- Ghi log (Telemetry) ở mỗi bước để xác định chính xác Agent sai ở "Reasoning" hay do "Tool Result".
- Log (Telemetry) at each step to pinpoint exactly whether the Agent failed at "Reasoning" or due to "Tool Result".

## 7. Thực Hành Lab 3 & Material
## 7. Lab 3 Practice & Material
- **Lab 3**: Xây dựng Chatbot baseline và nâng cấp lên ReAct Agent cho e-commerce (check_stock, get_discount, calc_shipping).
- **Lab 3**: Build a Chatbot baseline and upgrade to a ReAct Agent for e-commerce (check_stock, get_discount, calc_shipping).
- **Failure Analysis**: Học viên được yêu cầu đọc log JSON để tìm lỗi (parse error, hallucinated tool) và cải thiện Tool Description.
- **Failure Analysis**: Students are required to read JSON logs to find errors (parse error, hallucinated tool) and improve Tool Descriptions.
- Đánh giá khả năng của Agent thông qua việc thảo luận nhóm (Discord activity) về các trường hợp sử dụng tối ưu.
- Evaluate the Agent's capability through group discussions (Discord activity) on optimal use cases.
