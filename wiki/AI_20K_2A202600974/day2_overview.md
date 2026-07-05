---
type: overview
title: "Day 2 Overview - Xác định bài toán cho AI"
description: "Hướng dẫn xác định bài toán, thiết lập Problem Statement và đánh giá mức độ phù hợp của AI."
tags: [ai, 20k, day2]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/2/5-day02-lecture-slides-v2.pdf"]
---

# Day 2: Xác định bài toán cho AI (Problem Statement)

## 1. Problem Discovery (Khám phá vấn đề)
Thay vì vội vàng áp dụng AI, cần áp dụng phương pháp **Human-Centered Design (HCD)** và mô hình **Double Diamond**.
- Phải xác định đúng **điểm đau (pain points)** thực tế. Đôi khi quy trình hiện tại có thể giải quyết bằng các phương pháp tự động hóa truyền thống thay vì AI.
- Không nên thiết kế giải pháp cho một vấn đề không tồn tại ("Never solve the problem I am asked to solve" - Don Norman).

## 2. Problem Statement Hoàn Chỉnh
Một bài toán chuẩn bị tốt để ứng dụng AI cần xác định rõ 6 yếu tố cốt lõi và 3 yếu tố quyết định AI:
- **Actor**: Đối tượng trực tiếp chịu ảnh hưởng.
- **Workflow**: Quy trình vận hành hiện tại (từng bước cụ thể).
- **Bottleneck**: Khâu gây chậm trễ, sai sót, lặp lại.
- **Impact**: Tổn thất lượng hóa (thời gian, chi phí, chất lượng).
- **Success Metric**: Chỉ số đo lường cải thiện cụ thể.
- **Boundary**: Giới hạn của AI (những việc bắt buộc cần con người).
- *Điểm AI can thiệp (Entry)*, *Mức chọn giải pháp (Level)*, *Rủi ro & HITL (Safety)*.

## 3. Có nên ứng dụng AI? (Agentic Fit)
AI chỉ thực sự mang lại giá trị khi tích hợp chính xác vào quy trình nghiệp vụ và giải quyết đúng điểm đau.
- Đánh giá khả thi qua **Khung quyết định Go / Not Yet / No-Go**.
- Dấu hiệu cần AI: Khối lượng lớn, tốn thời gian, tác vụ lặp lại nhưng có độ biến thiên vừa phải, cần phân tích ngữ cảnh.

## 4. Các mức độ giải pháp (Rule / Workflow / Agent)
- **Cấp độ 1: Rule-based / Script**. Phù hợp khi logic rành mạch, kết quả dự đoán được 100%. Tối ưu chi phí và độ an toàn.
- **Cấp độ 2: Workflow (LLM Feature)**. Khi quy trình có cấu trúc, AI được sử dụng tại các bước linh hoạt (dịch, tóm tắt, phân loại). Tránh dùng chatbot tự do.
- **Cấp độ 3: Agent**. Chỉ nên áp dụng khi quy trình có nhiều biến số đòi hỏi thay đổi kế hoạch linh hoạt, nhiều bước cần suy luận và giao tiếp với tools, và có thể thiết lập vòng phản hồi an toàn. 

## 5. Thiết lập kỳ vọng và Đánh giá (Evaluation Plan)
- Từ Problem Statement, thiết lập kế hoạch kiểm thử (**Eval Plan**).
- Xác định Output Metric (kết quả cuối cùng cần đạt) và Input Metrics (các đòn bẩy có thể thay đổi để đạt kết quả).
- Phải có Baseline (hiện trạng), Target (mục tiêu) và Measurement (cách đo lường) trước khi bắt tay vào triển khai AI.
