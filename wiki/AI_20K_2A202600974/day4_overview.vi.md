---
type: overview
title: "Day 4 Overview - Prompt, Context Engineering và Tool Calling"
description: "Kỹ thuật thiết kế Prompt, xây dựng Context Packet và khai báo Tool cho Agent."
tags: [ai, 20k, day4]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/4/2-day04-lecture-slide-v3.pdf"]
---


- Prompt là lớp can thiệp đầu tiên: định hướng nhiệm vụ, phạm vi xử lý và cách model trả lời.
- Phân biệt giữa **System Prompt** (luật nền, ràng buộc, ưu tiên cao) và **User Prompt** (yêu cầu ở lượt hiện tại).
- Cấu trúc prompt tốt (sử dụng XML tags / delimiters) tách biệt rõ `role`, `task`, `context`, `boundaries`, và `format`.
- Tránh những prompt khổng lồ; nên chia task phức tạp thành các bước nhỏ (Decompose). Sử dụng các phương pháp: Zero-shot, One-shot, Few-shot, Chain-of-Thought (CoT), Tree of Thought (ToT).

- LLM không chỉ đọc prompt, nó xử lý **toàn bộ context** (bàn làm việc của model).
- Context bao gồm: instructions, user request, conversation history, known facts/states, retrieved docs, tool schemas, tool results.
- Vấn đề quá tải context: "Lost in the middle" (thông tin ở giữa bị bỏ sót), "Context rot" (thông tin cũ kỹ, trùng lặp gây nhiễu). 
- Kỹ thuật **Context Compaction**: Summarize (tóm tắt), Drop (bỏ bớt rác), Archive (lưu trữ ngoài).
- Dữ liệu truy xuất từ Web/bên ngoài là *Untrusted Context* và phải được cách ly (Isolation) bằng tag/delimiter.

- Agent cần gọi đúng tool, truyền đúng tham số và xử lý đúng kết quả.
- **Tool Taxonomy**: Knowledge Tool (bổ sung thông tin), Capability Tool (toán, code), Write Action (thay đổi trạng thái - cần cẩn trọng).
- **Tool Declaration**: Phải mô tả chính xác Name, Description (khi nào dùng, làm gì), Parameters, Return format, Error modes. Tên rõ ràng và Schema chi tiết giúp hạn chế agent gọi sai.
- **Tool Result**: Khi tool trả kết quả, kết quả này thành *context mới*. Cần có một lớp xử lý (Result Processor) để parse, clean, và lọc lấy dữ liệu thiết yếu trước khi nhồi lại vào prompt.

- **Read/Write Boundary**: Phân biệt rủi ro của từng tool. Các Write Actions có rủi ro cao (Send email, Pay, Cancel) cần cơ chế **Human-in-the-loop (HITL)** / Phê duyệt (Approval).
- **Workflow Patterns**: Tăng dần theo độ phức tạp: Prompt Chaining -> Routing -> Parallelization -> Orchestrator-Workers -> Evaluator-Optimizer -> Agent. Bắt đầu từ cấp độ đơn giản nhất đủ giải quyết bài toán.
- **Eval & Versioning**: Coi Prompt là một "Artifact vận hành". Mọi thay đổi đều phải được đánh giá qua tập dữ liệu thử nghiệm (Eval cases) và lưu vết (Version log).
