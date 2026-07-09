---
type: summary
title: "Day 23 – Track 3: LangGraph & Agentic Orchestration"
description: "State machine cho AI Agents: Core API, Persistence, Human-in-the-Loop, và Error Recovery với LangGraph."
tags: [ai, 20k, day23, track3, langgraph, agent, orchestration]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/23/day08_langgraph_student.pdf"]
---

> **Lộ trình:** [[track3_ai_app|Track 3: AI Application]]


**Giảng viên**: VinUniversity  
**Khóa**: AICB Phase 2 · Track 3 · Tuần 5

> **Câu hỏi trọng tâm**: Khi agent cần loop, retry, human approval và resume sau crash, chain một chiều (LCEL) còn đủ không?

## 1. Khi Nào Chain Không Đủ?
LCEL (LangChain Expression Language) phù hợp cho các pipeline tuyến tính một chiều. Tuy nhiên, production agent thường cần:
- **Loop & Retry**: Vòng lặp tự động sửa lỗi và thử lại khi tool bị lỗi.
- **Human-in-the-loop (HITL)**: Tạm dừng để con người duyệt trước các hành động phá hủy (destructive actions).
- **Dynamic Routing**: Quyết định rẽ nhánh linh hoạt (conditional edges) dựa trên kết quả bước trước.
- **Crash Recovery**: Checkpointing để tiếp tục lại luồng từ điểm dừng.

=> Giải pháp là LangGraph - orchestration framework thiết kế theo dạng State Machine.

## 2. Core API của LangGraph
Bốn khái niệm nền tảng của StateGraph:
- **State**: Một `TypedDict` chia sẻ giữa tất cả các nodes. Thiết kế cần flat, có reducer (overwrite hoặc append).
- **Nodes**: Các Python functions nhận vào state và trả về bản cập nhật state (partial update).
- **Edges & Conditional Edges**: Các đường kết nối (tĩnh hoặc có điều kiện) quyết định nhánh chạy tiếp theo.
- **Reducer**: Luật merge state khi cập nhật (ví dụ mặc định là overwrite, dùng append cho message history hoặc errors).

- **Checkpointing**: State snapshot lại sau mỗi bước. Các adapter gồm `MemorySaver` (nhanh, in-memory), `SqliteSaver` (bền vững), hoặc `Postgres` cho production.
- **Thread ID**: Định danh riêng biệt cho một phiên làm việc/workflow (vd một request hay một ticket).
- **Time Travel**: Tính năng replay lại từ một checkpoint bất kỳ để debug hoặc A/B testing hướng đi khác. Cập nhật state (Update State) ở checkpoint rồi resume.

- **Interrupt / Resume**: Dùng `interrupt()` để tạm dừng graph. Sau khi nhận được duyệt (approve), resume đồ thị bằng `Command(resume=...)`.
- **Error Recovery (3 Tầng)**:
  1. Retry node bị lỗi với giới hạn (`max attempts`).
  2. Fallback sang mô hình hoặc công cụ dự phòng.
  3. Đẩy vào Dead-letter queue để đợi human review.

Cần báo cáo và theo dõi:

## 6. Liên Kết
- [[day27_track1]] – Human-in-the-Loop UX (nâng cao)

---

Câu hỏi ôn tập Ngày 23

   Khi nào một pipeline tuyến tính (LCEL) không còn đủ cho agent?
   - A. Khi chỉ cần một luồng xử lý đơn giản, không có rẽ nhánh.
   - B. Khi agent cần loop retry, human-in-the-loop, dynamic routing và crash recovery.
   - C. Khi số lượng tool nhỏ hơn 5.
   - D. Khi không cần checkpointing.
   **Đáp án / Answer:** B

   Trong LangGraph, reducer được dùng để làm gì?
   - A. Xác định node nào chạy tiếp theo.
   - B. Merge state khi cập nhật, ví dụ append cho message history.
   - C. Tạo checkpoint sau mỗi bước.
   - D. Gọi tool bên ngoài.
   **Đáp án / Answer:** B

   Tính năng "Time Travel" trong LangGraph cho phép làm gì?
   - A. Chạy song song nhiều graph cùng lúc.
   - B. Replay lại từ một checkpoint bất kỳ để debug hoặc thử hướng đi khác.
   - C. Tự động retry node bị lỗi.
   - D. Gửi thông báo cho người dùng khi hoàn thành.
   **Đáp án / Answer:** B

   Để tạm dừng graph chờ con người phê duyệt, ta sử dụng hàm nào?
   **Đáp án / Answer:** A
