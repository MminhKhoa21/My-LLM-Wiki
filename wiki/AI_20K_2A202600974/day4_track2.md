---
type: summary
title: "Day 4 Track 2 - Prompt, Context Engineering, Tool & Control"
description: "Tổng hợp kỹ thuật về Prompt, tối ưu Context, gọi Tool an toàn và cơ chế kiểm soát Agent."
tags: [ai, 20k, day4, track2, context-engineering, control, tool-calling]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/4/2-day04-lecture-slide-v3.pdf"]
---

# Day 4 Track 2: Prompt, Context Engineering, Tool & Control

Tài liệu này tập trung vào cách debug và xây dựng một Agent đáng tin cậy: không chỉ biết gọi tool mà còn gọi đúng, hiểu đúng thông tin và biết khi nào nên dừng.

## 1. Tầm nhìn: Từ Agent chạy được đến Agent đáng tin
Một Agent tốt được xây dựng trên 4 trụ cột:
- **Prompt**: Chỉ dẫn nhiệm vụ rõ ràng.
- **Context**: Thông tin đủ, đúng lúc, đúng nguồn.
- **Tool**: Năng lực đọc dữ liệu và hành động.
- **Control**: Phê duyệt (Approval), đánh giá (Eval), lưu log và rào chắn (Guardrail).

## 2. Prompt Fundamentals
- Thiết lập ranh giới rõ ràng thông qua Role, Task, Format và Boundary.
- Quyết định khi nào cần sử dụng ví dụ (Examples), khi nào cần suy luận từng bước (Chain-of-Thought - CoT).
- Prompt là nền móng, sai lệch ở prompt sẽ làm hỏng toàn bộ chuỗi xử lý.

## 3. Context Engineering (Kỹ nghệ ngữ cảnh)
- **Context = Bàn làm việc của LLM**. Prompt chỉ là một tờ chỉ dẫn trên bàn. Những thứ khác bao gồm: User request, Lịch sử hội thoại, Data truy xuất (RAG), Kết quả Tool.
- Tránh việc nhồi nhét mọi thứ. Chọn đúng thông tin để đặt lên bàn:
  - Lọc bỏ thông tin thừa để chống nhiễu (Context Rot).
  - Khắc phục hiện tượng "Lost in the Middle" bằng cách sắp xếp thông tin quan trọng ở đầu và cuối (Recency Bias).

## 4. Tool Calling: Khai báo & Kết quả
- **Tool Declaration**: 
  - Khai báo tool chi tiết là cách định hướng Agent (routing) chính xác. 
  - Tên tool và mô tả đóng vai trò như instruction để LLM quyết định.
- **Tool Result as Context**: 
  - Kết quả trả về từ tool không chỉ là dữ liệu, nó trở thành ngữ cảnh mới.
  - Cần format lại kết quả tool cho gọn gàng và dễ hiểu trước khi nhồi lại vào Context Window.

## 5. Control & Harness (Kiểm soát hệ thống)
- **Ranh giới an toàn**:
  - Các thao tác đọc dữ liệu (Read) có rủi ro thấp.
  - Các thao tác thay đổi trạng thái (Write Action như thanh toán, gửi mail, xóa DB) cần cơ chế kiểm soát nghiêm ngặt.
- **Human-in-the-Loop (HITL)**: Tạm dừng luồng để con người phê duyệt trước khi gọi các tool nguy hiểm.
- **Evaluation & Versioning**: 
  - Hệ thống cần bộ test (Eval cases) để đánh giá: phiên bản prompt mới có tốt hơn bản cũ không? Tool chạy có bắt được ngoại lệ không?
  - Retry mechanisms: Xử lý khi API fail hoặc LLM format sai JSON.

## Tổng Kết
Việc debug một AI App cần xác định lỗi ở lớp nào: do Prompt không rõ ràng, Context thiếu/nhiễu, Tool mô tả sai lệch, hay thiếu Control flow an toàn.
