---
type: summary
title: "Summary: Day 02 Lecture Slides v2"
description: "A summary of the alternative version of Day 02 lecture slides on defining AI problems and workflows."
tags: [AI Problem, Double Diamond, Workflow, Problem Statement]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/2/5-day02-lecture-slides-v2.pdf", "raw/AI_20K_2A202600974/2/6-day02-lecture-slides-v2.pdf"]
---

# Summary: Day 02 Lecture Slides v2
# Tóm tắt: Bài giảng Ngày 02 v2

## Overview
## Tổng quan
This document summarizes the Day 02 lecture slides (versions 5 and 6), which mirror the core curriculum of identifying AI problems, structuring Problem Statements, and determining the appropriate level of AI integration. It reinforces the transition from vague ideas to concrete workflows.

Tài liệu này tóm tắt các slide bài giảng Ngày 02 (phiên bản 5 và 6), phản ánh chương trình cốt lõi về việc xác định các vấn đề AI, cấu trúc Tuyên bố Vấn đề (Problem Statements) và xác định mức độ tích hợp AI phù hợp. Nó củng cố quá trình chuyển đổi từ những ý tưởng mơ hồ sang quy trình làm việc cụ thể.

## Key Concepts
## Các Khái niệm Chính

### Foundation of AI Products
### Nền tảng của Sản phẩm AI
An AI product is built on three pillars:
Một sản phẩm AI được xây dựng trên ba trụ cột:
1. **AI Engineering:** Model deployment, RAG, agents, and evaluation.
   **Kỹ thuật AI:** Triển khai mô hình, RAG, các tác nhân (agents) và đánh giá.
2. **Product Thinking:** Identifying the right problem and understanding user value (Inspired).
   **Tư duy Sản phẩm:** Xác định đúng vấn đề và hiểu giá trị đối với người dùng (Inspired).
3. **Design Thinking:** Designing for mental models, feedback, and graceful handling of errors.
   **Tư duy Thiết kế:** Thiết kế cho các mô hình tinh thần, phản hồi và xử lý lỗi tinh tế.

### The Double Diamond & HCD
### Mô hình Kim cương Đôi (Double Diamond) & Thiết kế Lấy con người làm trung tâm (HCD)
- **Double Diamond:** Focuses on discovering the *real* problem before narrowing down a solution. A great solution to the wrong problem is useless.
  **Kim cương Đôi:** Tập trung vào việc khám phá vấn đề *thực sự* trước khi thu hẹp vào một giải pháp. Một giải pháp tuyệt vời cho một vấn đề sai là vô dụng.
- **Human-Centered Design (HCD):** Emphasizes observation, ideation, prototyping, testing, and continuous iteration.
  **Thiết kế Lấy con người làm trung tâm (HCD):** Nhấn mạnh vào quan sát, lên ý tưởng, tạo nguyên mẫu, thử nghiệm và lặp lại liên tục.

### Problem Formulation
### Hình thành Vấn đề
- Identifying the right problem involves looking for tasks that are repetitive, time-consuming, or have a clear AI advantage.
  Xác định đúng vấn đề bao gồm việc tìm kiếm các tác vụ mang tính lặp đi lặp lại, tốn thời gian hoặc có lợi thế AI rõ ràng.
- Avoid anti-patterns like "Solution-first" (building before knowing the workflow) and "No baseline" (failing to measure current operational costs).
  Tránh các phản mô hình (anti-patterns) như "Giải pháp đi trước" (xây dựng trước khi biết quy trình làm việc) và "Không có đường cơ sở" (không đo lường được chi phí hoạt động hiện tại).
- **Stakeholder Interviews:** Ask questions about current workflows, bottlenecks, costs of errors, and success metrics.
  **Phỏng vấn các bên liên quan:** Đặt câu hỏi về các quy trình làm việc hiện tại, các nút thắt, chi phí của các lỗi và các chỉ số thành công.

### Problem Statement Components
### Các Thành phần của Tuyên bố Vấn đề
The structured Problem Statement requires:
Tuyên bố Vấn đề có cấu trúc yêu cầu:
- **Actor** and **Workflow**
  **Chủ thể (Actor)** và **Quy trình làm việc (Workflow)**
- **Bottleneck** and **Impact**
  **Nút thắt (Bottleneck)** và **Tác động (Impact)**
- **Success Metrics** (Baseline, Target, Measurement)
  **Chỉ số Thành công** (Đường cơ sở, Mục tiêu, Đo lường)
- **Boundary**, **AI Intervention Point**, and **Risk/HITL**
  **Ranh giới**, **Điểm can thiệp của AI**, và **Rủi ro/HITL (Con người trong vòng lặp)**

### Decision Framework: Rule, Workflow, Agent
### Khung Ra quyết định: Quy tắc, Quy trình, Tác nhân
Choose the simplest level of abstraction:
Chọn mức độ trừu tượng đơn giản nhất:
- **Rule:** Deterministic logic. Best for rigid, high-compliance tasks.
  **Quy tắc (Rule):** Logic xác định. Tốt nhất cho các tác vụ cứng nhắc, tuân thủ cao.
- **Workflow:** AI acts within a defined process (e.g., summarizing, drafting). Human remains in control.
  **Quy trình (Workflow):** AI hoạt động trong một quy trình được xác định (ví dụ: tóm tắt, soạn thảo). Con người vẫn nắm quyền kiểm soát.
- **Agent:** Autonomous planning and tool usage. Use only when the environment demands high adaptability.
  **Tác nhân (Agent):** Lập kế hoạch và sử dụng công cụ tự chủ. Chỉ sử dụng khi môi trường đòi hỏi khả năng thích ứng cao.

### Workflow Patterns
### Các Mô hình Quy trình
- Follow Anthropic's guidelines for AI workflows: Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, and Evaluator-Optimizer.
  Tuân theo các nguyên tắc của Anthropic đối với các quy trình AI: Chuỗi lời nhắc (Prompt Chaining), Định tuyến (Routing), Song song hóa (Parallelization), Điều phối viên-Người thực thi (Orchestrator-Workers) và Đánh giá viên-Trình tối ưu hóa (Evaluator-Optimizer).
- Always prefer simpler, pre-defined workflows over fully autonomous agents unless the latter is absolutely necessary.
  Luôn ưu tiên các quy trình đơn giản hơn, được xác định trước so với các tác nhân hoàn toàn tự chủ trừ khi điều sau là hoàn toàn cần thiết.

### Evaluation and Go/No-Go Decision
### Đánh giá và Quyết định Triển khai (Go/No-Go)
- Translate the Problem Statement directly into an Evaluation Plan with defined test cases and thresholds.
  Chuyển đổi trực tiếp Tuyên bố Vấn đề thành một Kế hoạch Đánh giá với các trường hợp thử nghiệm và ngưỡng được xác định.
- Make a calculated decision: **Go** (clear problem, feasible metric), **Not Yet** (needs data/process standardization), or **No-Go** (AI adds no value or risk is too high).
  Đưa ra quyết định có tính toán: **Go** (vấn đề rõ ràng, chỉ số khả thi), **Not Yet** (cần chuẩn hóa dữ liệu/quy trình) hoặc **No-Go** (AI không mang lại giá trị nào hoặc rủi ro quá cao).
