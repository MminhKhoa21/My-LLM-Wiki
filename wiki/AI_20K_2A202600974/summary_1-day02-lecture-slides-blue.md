---
type: summary
title: "Summary: Day 02 Lecture Slides Blue"
description: "A summary of the Day 02 lecture slides on defining AI problems, frameworks, and solution levels."
tags: [AI Problem, Double Diamond, Workflow, Problem Statement]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/2/1-day02-lecture-slides-blue.pdf"]
---

# Summary: Day 02 Lecture Slides Blue
# Tóm tắt: Bài giảng Ngày 02 Slides Blue

## Overview
## Tổng quan
This document summarizes the lecture slides from Day 02 of the VinUni AI 20K program, instructed by Mai Anh Nguyen (Blue). The core focus is on transforming vague business requirements into clear, actionable AI Problem Statements, evaluating whether AI is genuinely needed, and choosing the right level of solution (Rule, Workflow, or Agent).
Tài liệu này tóm tắt các slide bài giảng từ Ngày 02 của chương trình VinUni AI 20K, do giảng viên Mai Anh Nguyen (Blue) hướng dẫn. Trọng tâm cốt lõi là chuyển đổi các yêu cầu kinh doanh mơ hồ thành các Tuyên bố Vấn đề AI (AI Problem Statements) rõ ràng, có thể hành động, đánh giá xem AI có thực sự cần thiết hay không, và lựa chọn cấp độ giải pháp phù hợp (Quy tắc, Quy trình làm việc, hoặc Tác nhân).

## Key Concepts
## Các khái niệm chính

### Problem Discovery and the Double Diamond Model
### Khám phá Vấn đề và Mô hình Kim cương Đôi (Double Diamond Model)
- The **Double Diamond Model** emphasizes finding the right problem before finding the right solution. It consists of two diamonds:
- **Mô hình Kim cương Đôi** nhấn mạnh việc tìm đúng vấn đề trước khi tìm giải pháp phù hợp. Nó bao gồm hai viên kim cương:
  - **Diamond 1 (Problem):** Discover (diverge to explore) and Define (converge to pinpoint the root problem).
  - **Kim cương 1 (Vấn đề):** Khám phá (Discover - phân kỳ để tìm hiểu) và Định nghĩa (Define - hội tụ để xác định chính xác gốc rễ vấn đề).
  - **Diamond 2 (Solution):** Develop (diverge to explore solutions) and Deliver (converge to select and implement).
  - **Kim cương 2 (Giải pháp):** Phát triển (Develop - phân kỳ để khám phá các giải pháp) và Cung cấp (Deliver - hội tụ để chọn và triển khai).
- Prioritize **Human-Centered Design (HCD)** by observing users, understanding their pain points (bottlenecks), and avoiding "solution-first" anti-patterns.
- Ưu tiên **Thiết kế Lấy Con người làm Trung tâm (HCD)** bằng cách quan sát người dùng, hiểu những điểm đau của họ (những nút thắt cổ chai), và tránh các khuôn mẫu "giải pháp trước tiên" (solution-first) sai lầm.

### Defining the Problem Statement
### Định nghĩa Tuyên bố Vấn đề (Problem Statement)
A clear **Problem Statement** is essential before considering an AI solution. It comprises:
Một **Tuyên bố Vấn đề** rõ ràng là điều cần thiết trước khi xem xét giải pháp AI. Nó bao gồm:
1. **Actor**: Who is impacted?
1. **Đối tượng (Actor)**: Ai là người bị ảnh hưởng?
2. **Workflow**: What is the current step-by-step process?
2. **Quy trình làm việc (Workflow)**: Quá trình từng bước hiện tại là gì?
3. **Bottleneck**: Where is the exact delay, error, or repetition?
3. **Nút thắt cổ chai (Bottleneck)**: Sự chậm trễ, lỗi hoặc lặp lại chính xác nằm ở đâu?
4. **Impact**: What is the quantifiable loss (time, cost)?
4. **Tác động (Impact)**: Tổn thất có thể định lượng được là gì (thời gian, chi phí)?
5. **Success Metric**: How will improvement be measured?
5. **Chỉ số Thành công (Success Metric)**: Sự cải thiện sẽ được đo lường như thế nào?
6. **Boundary**: What are the strict limitations (e.g., AI cannot auto-send emails)?
6. **Ranh giới (Boundary)**: Những giới hạn nghiêm ngặt là gì (ví dụ: AI không thể tự động gửi email)?
7. **AI Intervention Point**: Exactly where in the workflow does AI step in?
7. **Điểm can thiệp AI (AI Intervention Point)**: Chính xác vị trí nào trong quy trình làm việc mà AI sẽ bước vào?
8. **Level of Solution**: Rule, Workflow, or Agent?
8. **Cấp độ Giải pháp (Level of Solution)**: Quy tắc, Quy trình làm việc hay Tác nhân?
9. **Risk & Human-in-the-Loop (HITL)**: How to handle AI errors and where human approval is required.
9. **Rủi ro & Sự tham gia của con người (HITL)**: Cách xử lý các lỗi của AI và những nơi cần sự phê duyệt của con người.

### AI Solution Levels: Rule vs. Workflow vs. Agent
### Cấp độ Giải pháp AI: Quy tắc vs. Quy trình làm việc vs. Tác nhân
Always opt for the simplest solution that works:
Luôn ưu tiên giải pháp đơn giản nhất mà vẫn mang lại hiệu quả:
- **Level 1 - Rule**: Use when logic is deterministic (If/Else) and exactness is required. No AI needed.
- **Cấp độ 1 - Quy tắc (Rule)**: Sử dụng khi logic mang tính tất định (If/Else) và yêu cầu sự chính xác. Không cần đến AI.
- **Level 2 - Workflow (LLM Feature)**: Use when steps are defined, but some steps need AI for language processing, summarization, or classification. Retains full human control.
- **Cấp độ 2 - Quy trình làm việc (LLM Feature)**: Sử dụng khi các bước đã được xác định, nhưng một số bước cần AI để xử lý ngôn ngữ, tóm tắt hoặc phân loại. Vẫn giữ toàn quyền kiểm soát của con người.
- **Level 3 - Agent**: Use when the environment is highly dynamic, requiring autonomous planning and multi-tool coordination. Higher risk and operational cost.
- **Cấp độ 3 - Tác nhân (Agent)**: Sử dụng khi môi trường mang tính động cao, đòi hỏi khả năng lên kế hoạch tự chủ và phối hợp nhiều công cụ. Rủi ro và chi phí vận hành cao hơn.

### Workflow Patterns
### Các mẫu Quy trình làm việc
Based on Anthropic's guidelines:
Dựa trên hướng dẫn của Anthropic:
- **Basic Patterns**: Prompt Chaining, Routing, Parallelization.
- **Mẫu Cơ bản**: Chuỗi lệnh (Prompt Chaining), Điều hướng (Routing), Song song hóa (Parallelization).
- **Advanced Patterns**: Orchestrator-Workers, Evaluator-Optimizer, Autonomous Agents.
- **Mẫu Nâng cao**: Người điều phối - Công nhân (Orchestrator-Workers), Người đánh giá - Người tối ưu hóa (Evaluator-Optimizer), Tác nhân Tự chủ (Autonomous Agents).

### Decision Making
### Ra Quyết định
The final step in problem framing is making a conscious decision:
Bước cuối cùng trong việc thiết lập vấn đề là đưa ra một quyết định có ý thức:
- **Go**: Problem is clear, metrics are measurable, and AI provides a distinct advantage.
- **Tiến hành (Go)**: Vấn đề rõ ràng, các chỉ số có thể đo lường và AI mang lại lợi thế vượt trội.
- **Not Yet**: Needs more data, process standardization, or clearer metrics.
- **Chưa thể thực hiện (Not Yet)**: Cần thêm dữ liệu, chuẩn hóa quy trình, hoặc các chỉ số rõ ràng hơn.
- **No-Go**: Too risky, or non-AI solutions are more effective.
- **Không thực hiện (No-Go)**: Quá rủi ro, hoặc các giải pháp phi AI hiệu quả hơn.

## Workflow Integration
## Tích hợp Quy trình làm việc
- **UX & HITL**: Ensure proper UI design to manage AI shortcomings (e.g., asking for clarification, providing citations, requiring manual approval).
- **Trải nghiệm người dùng & Sự tham gia của con người (UX & HITL)**: Đảm bảo thiết kế giao diện người dùng (UI) phù hợp để xử lý những thiếu sót của AI (ví dụ: yêu cầu làm rõ, cung cấp trích dẫn, yêu cầu phê duyệt thủ công).
- **Evaluation**: The Problem Statement serves as the blueprint for the Evaluation Plan (baseline, test cases, and success thresholds).
- **Đánh giá (Evaluation)**: Tuyên bố Vấn đề đóng vai trò như bản thiết kế cho Kế hoạch Đánh giá (đường cơ sở, các trường hợp kiểm thử và ngưỡng thành công).
