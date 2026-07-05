---
type: summary
title: "Summary of day03-tu-chatbot-den-agentic-agent-react_manh.pdf"
description: "Tổng quan về Agentic AI, framework đánh giá Agentic Fit, kiến trúc Agent và mẫu thiết kế ReAct (Reasoning + Acting)."
tags: [ai, 20k, day03]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/3/day03-tu-chatbot-den-agentic-agent-react_manh.pdf"]
---

# Tóm tắt: Từ Chatbot Đến Agentic Agent (Design Pattern ReAct)

## 1. Spectrum: Từ Bot đến Agent
Hệ thống AI không chỉ gói gọn trong một loại mà phân chia thành các cấp độ từ thấp lên cao:
- **Rule-based Bot:** Bot hoạt động dựa trên luật if/else cố định.
- **LLM Chatbot:** Sinh câu trả lời mượt mà, hiểu context nhưng thường chỉ thao tác 1 lượt, không có khả năng chủ động tìm kiếm dữ liệu thực tế.
- **Reactive Agent:** Kết hợp sử dụng công cụ (tool use) + khả năng lặp lại quan sát theo từng bước (loop).
- **Autonomous Agent:** Theo đuổi mục tiêu dài hạn với nhiều quyết định liên tiếp và có trí nhớ (memory).

## 2. Agentic Fit Framework (Khi nào nên dùng Agent?)
Đánh giá độ phức tạp qua 4 tiêu chí:
1. **Multi-step Reasoning:** Có cần suy luận logic nhiều bước không?
2. **Tool Interaction:** Có cần gọi external APIs, DBs hay search không?
3. **Dynamic Decision:** Tùy từng bước mà thay đổi hành động dựa trên kết quả trả về không?
4. **Long Horizon:** Có cần lưu trạng thái qua nhiều vòng lặp dài không?
*Lưu ý:* Luôn benchmark bằng Rule/Chatbot trước khi dùng đến Agent vì Agent tốn chi phí và phức tạp hơn.

## 3. Kiến trúc của một Agent
Gồm 4 khối cốt lõi:
- **Perception (Nhận thức):** Tiếp nhận input từ user và kết quả từ các tool.
- **Reasoning (Suy luận):** Bộ não LLM phân tích trạng thái để chọn bước đi tiếp theo.
- **Action (Hành động):** Gọi tools (Search, API) hoặc trả lời cho người dùng.
- **Memory (Trí nhớ):** Gồm *Short-term* (nằm trong context window) và *Long-term* (Vector DB, DB truyền thống để lưu trữ dài hạn).

## 4. Mẫu thiết kế ReAct (Reasoning + Acting)
Là pattern kết hợp giữa tư duy theo từng bước và hành động gọi công cụ. Thay vì vội trả lời, Agent sẽ lặp lại chu kỳ sau:
- **Thought (Suy nghĩ):** "Mình đang thiếu gì, mình cần làm gì?"
- **Action (Hành động):** Gọi tool nào với tham số nào?
- **Observation (Quan sát):** Kết quả của tool đưa về là gì?
*(Chu kỳ lặp lại cho tới khi thu thập đủ dữ kiện để đưa ra "Final Answer")*

> **Ưu điểm của ReAct:** Traces rõ ràng, dễ debug, dễ phát hiện xem Agent chọn sai tool hay bị rơi vào vòng lặp vô hạn.

## 5. Agent Loop & Debugging
- **Safeguard (Bảo vệ):** Cần thiết lập giới hạn vòng lặp (Max Iterations), timeouts, chi phí token, và fallback.
- **LangGraph:** Khi dự án lớn, ReAct vòng lặp tự viết sẽ khó quản lý. LangGraph hỗ trợ vẽ các luồng Graph (Nodes, Edges, State) để scale dễ dàng hơn.
- **Hybrid Pattern:** Cách tiếp cận thực dụng là dùng Chatbot xử lý nhanh tác vụ đơn giản, khi nào cần multi-step mới chuyển sang hướng Agent.
