---
type: summary
title: "Summary: Day 02 Lecture Slides v2 (Part 2)"
description: "A summary of the alternative version of Day 02 lecture slides on defining AI problems and workflows."
tags: [AI Problem, Double Diamond, Workflow, Problem Statement]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/2/6-day02-lecture-slides-v2.pdf"]
---

# Summary: Day 02 Lecture Slides v2 (Part 2)
# Tóm tắt: Bài giảng Ngày 02 Slides v2 (Phần 2)

## Overview
## Tổng quan
This document summarizes the Day 02 lecture slides (version 6), which mirror the core curriculum of identifying AI problems, structuring Problem Statements, and determining the appropriate level of AI integration. It reinforces the transition from vague ideas to concrete workflows.

Tài liệu này tóm tắt bài giảng Ngày 02 slides (phiên bản 6), phản ánh chương trình cốt lõi về việc xác định các bài toán AI, cấu trúc các Tuyên bố Vấn đề (Problem Statements), và xác định mức độ tích hợp AI phù hợp. Nó củng cố quá trình chuyển đổi từ những ý tưởng mơ hồ sang các quy trình làm việc (workflows) cụ thể.

## Key Concepts
## Các Khái Niệm Chính

### Foundation of AI Products
### Nền Tảng Của Sản Phẩm AI
An AI product is built on three pillars:
Một sản phẩm AI được xây dựng trên ba trụ cột:
1. **AI Engineering:** Model deployment, RAG, agents, and evaluation.
   **Kỹ Thuật AI:** Triển khai mô hình, RAG, các agent (tác tử), và đánh giá.
2. **Product Thinking:** Identifying the right problem and understanding user value (Inspired).
   **Tư Duy Sản Phẩm:** Xác định đúng vấn đề và hiểu giá trị đối với người dùng (Inspired).
3. **Design Thinking:** Designing for mental models, feedback, and graceful handling of errors.
   **Tư Duy Thiết Kế:** Thiết kế cho các mô hình tinh thần, phản hồi, và xử lý lỗi một cách tinh tế.

### The Double Diamond & HCD
### Mô Hình Kim Cương Kép & HCD (Thiết Kế Lấy Con Người Làm Trung Tâm)
- **Double Diamond:** Focuses on discovering the *real* problem before narrowing down a solution. A great solution to the wrong problem is useless.
  **Kim Cương Kép:** Tập trung vào việc khám phá vấn đề *thực sự* trước khi thu hẹp vào một giải pháp. Một giải pháp tuyệt vời cho sai vấn đề là vô dụng.
- **Human-Centered Design (HCD):** Emphasizes observation, ideation, prototyping, testing, and continuous iteration.
  **Thiết Kế Lấy Con Người Làm Trung Tâm (HCD):** Nhấn mạnh sự quan sát, lên ý tưởng, làm nguyên mẫu, thử nghiệm, và lặp lại liên tục.

### Problem Formulation
### Định Hình Vấn Đề
- Identifying the right problem involves looking for tasks that are repetitive, time-consuming, or have a clear AI advantage.
  Xác định đúng vấn đề liên quan đến việc tìm kiếm các tác vụ lặp đi lặp lại, tốn thời gian, hoặc có lợi thế rõ ràng khi áp dụng AI.
- Avoid anti-patterns like "Solution-first" (building before knowing the workflow) and "No baseline" (failing to measure current operational costs).
  Tránh các anti-pattern như "Giải pháp trước" (xây dựng trước khi hiểu rõ quy trình làm việc) và "Không có đường cơ sở" (thất bại trong việc đo lường chi phí vận hành hiện tại).
- **Stakeholder Interviews:** Ask questions about current workflows, bottlenecks, costs of errors, and success metrics.
  **Phỏng Vấn Các Bên Liên Quan:** Đặt các câu hỏi về quy trình làm việc hiện tại, điểm nghẽn, chi phí của các lỗi sai, và các số đo thành công.

### Problem Statement Components
### Các Thành Phần Của Tuyên Bố Vấn Đề
The structured Problem Statement requires:
Tuyên bố Vấn đề được cấu trúc yêu cầu:
- **Actor** and **Workflow**
  **Chủ Thể** và **Quy Trình Làm Việc**
- **Bottleneck** and **Impact**
  **Điểm Nghẽn** và **Tác Động**
- **Success Metrics** (Baseline, Target, Measurement)
  **Các Số Đo Thành Công** (Đường cơ sở, Mục tiêu, Phương pháp đo lường)
- **Boundary**, **AI Intervention Point**, and **Risk/HITL**
  **Phạm Vi**, **Điểm Can Thiệp AI**, và **Rủi Ro/HITL (Con Người Trong Vòng Lặp)**

### Decision Framework: Rule, Workflow, Agent
### Khung Ra Quyết Định: Quy Tắc, Quy Trình, Agent
Choose the simplest level of abstraction:
Chọn mức độ trừu tượng đơn giản nhất:
- **Rule:** Deterministic logic. Best for rigid, high-compliance tasks.
  **Quy Tắc:** Logic tất định. Tốt nhất cho các tác vụ cứng nhắc, tuân thủ cao.
- **Workflow:** AI acts within a defined process (e.g., summarizing, drafting). Human remains in control.
  **Quy Trình:** AI hoạt động trong một quy trình được định nghĩa (ví dụ: tóm tắt, soạn thảo). Con người vẫn nắm quyền kiểm soát.
- **Agent:** Autonomous planning and tool usage. Use only when the environment demands high adaptability.
  **Agent:** Tự lập kế hoạch và sử dụng công cụ. Chỉ sử dụng khi môi trường đòi hỏi sự thích ứng cao.

### Workflow Patterns
### Các Mẫu Quy Trình Làm Việc
- Follow Anthropic's guidelines for AI workflows: Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, and Evaluator-Optimizer.
  Tuân theo các hướng dẫn của Anthropic cho các quy trình AI: Chuỗi Prompt, Định tuyến, Xử lý song song, Mô hình Điều phối - Công nhân, và Đánh giá - Tối ưu.
- Always prefer simpler, pre-defined workflows over fully autonomous agents unless the latter is absolutely necessary.
  Luôn ưu tiên các quy trình đơn giản, được định nghĩa trước hơn là các agent hoàn toàn tự trị trừ khi điều sau là thực sự cần thiết.

### Evaluation and Go/No-Go Decision
### Đánh Giá và Quyết Định Tiếp Tục/Dừng Lại
- Translate the Problem Statement directly into an Evaluation Plan with defined test cases and thresholds.
  Chuyển đổi Tuyên bố Vấn đề trực tiếp thành một Kế Hoạch Đánh Giá với các test case và ngưỡng được xác định.
- Make a calculated decision: **Go** (clear problem, feasible metric), **Not Yet** (needs data/process standardization), or **No-Go** (AI adds no value or risk is too high).
  Đưa ra quyết định đã được tính toán: **Go** (Tiếp tục: vấn đề rõ ràng, số đo khả thi), **Not Yet** (Chưa: cần chuẩn hóa dữ liệu/quy trình), hoặc **No-Go** (Dừng lại: AI không thêm giá trị hoặc rủi ro quá cao).
