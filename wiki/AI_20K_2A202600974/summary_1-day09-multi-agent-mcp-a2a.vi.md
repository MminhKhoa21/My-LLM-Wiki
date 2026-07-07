---
type: summary
title: "Summary: 1-day09-multi-agent-mcp-a2a"
description: "A detailed summary of the 1-day09-multi-agent-mcp-a2a.pdf document."
tags: [day09, multi-agent, mcp, a2a]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/9/1-day09-multi-agent-mcp-a2a.pdf"]
---

# Multi-Agent & Kết Nối Hệ Thống (AICB-P1 · Ngày 9)

## 1. Giới hạn của Single-Agent
Một agent duy nhất thường bị quá tải khi bài toán lớn dần, gây ra các vấn đề:
- **Context bottleneck:** LLM bị quá tải context window, dẫn đến việc "quên" thông tin ở giữa tài liệu (hiện tượng lost-in-the-middle).
- **Specialization trade-off:** Khi agent ôm quá nhiều vai trò, prompt trở nên dài, phức tạp và kém ổn định, khó có thể làm xuất sắc một vai trò cụ thể.
- **Parallelism hạn chế:** Single-agent hoạt động tuần tự, chờ đợi nhau làm tăng độ trễ (latency).
- **Reliability yếu:** Sai sót ở một bước dễ làm hỏng toàn bộ quy trình, khó khoanh vùng lỗi.

*Dấu hiệu cần chuyển sang multi-agent:* Bài toán có nhiều bước và nhiều vai trò khác nhau, có thể chia việc chạy độc lập, và đặc biệt là khi cần debug lỗi rõ ràng từ từng khâu.

## 2. Mental Model: Tư Duy Hệ Thống
Chuyển từ câu hỏi "Làm thế nào để agent thông minh hơn?" sang tư duy hệ thống: "Bài toán gồm bao nhiêu loại trách nhiệm? Ai cần biết gì, khi nào? Lỗi cần được khoanh vùng ở đâu?". 
- **Nguyên tắc cốt lõi:** Parallelize Reads (Song song hoá việc đọc) và Serialize Writes (Tuần tự hoá việc tạo kết quả chung).

Có 4 pattern tổ chức đa tác tử phổ biến:
1. **Supervisor-Worker:** Một supervisor làm nhiệm vụ điều phối và tổng hợp từ nhiều worker chuyên biệt. Dễ kiểm soát, dễ trace lỗi. (Đây là pattern tập trung ở bài giảng này).
2. **Pipeline:** Flow dạng chuỗi cố định (A -> B -> C), mỗi bước phụ thuộc đầu ra bước trước.
3. **Debate:** Nhiều agent giải cùng bài toán rồi đối chiếu để giảm "điểm mù".
4. **Hierarchical:** Các supervisor lồng vào nhau thành nhiều tầng, phù hợp với hệ thống quy mô lớn.

Thay vì để 1 agent kiêm nhiệm tất cả, hệ thống sử dụng:
- **Supervisor:** Làm nhiệm vụ phân tích yêu cầu, quyết định gọi worker nào phù hợp, theo dõi trạng thái và tổng hợp kết quả. Không làm thay việc của worker.
- **Worker:** Chuyên trách 1 năng lực hẹp (ví dụ: retrieve, dùng tool, tổng hợp). Yêu cầu input/output rõ ràng, càng stateless càng dễ test.
- **Thiết kế State:** Nên dùng Shared State (dễ quan sát toàn cảnh) chứa thông tin như `task`, `plan`, `worker_results`, `status`, `final_answer` và đặc biệt là `trace`.
- **Anti-patterns cần tránh:** God Supervisor (Supervisor ôm đồm tính toán), Chatty Workers (Worker gọi ngược Supervisor liên tục để hỏi), Implicit State, và No Fallback (Không có đường lui khi lỗi).

- **MCP là gì?** Một chuẩn giao tiếp thống nhất (dựa trên JSON-RPC) giúp các agent kết nối với external capabilities mà không cần viết riêng mã tích hợp (hard-code).
- **Các thành phần:** MCP Server công bố 3 thứ chính: `Tools` (hành động, ví dụ: search), `Resources` (dữ liệu, ví dụ: database), và `Prompts`.
- **Lợi ích:** Tách biệt rõ ràng layer Agent và Tool, các thay đổi API từ tool không làm ảnh hưởng đến mã Agent. Hệ thống "khám phá" capability động.

Khác với MCP (Agent giao tiếp với Tool), A2A chuẩn hoá việc **Agent giao tiếp với Agent** để chia sẻ việc và đồng bộ dữ liệu.
- Được bảo trợ bởi Linux Foundation, quy định chuẩn định dạng cho AgentCard, Task, Message, Artifact.
- Cần có Message Contract tối thiểu: Chỉ truyền "need to know" (thông tin vừa đủ để agent kia thực thi, không thừa không thiếu), quy định rõ output format.
- Thiết lập ranh giới bảo mật (Trust boundary): Validate đầu ra, giới hạn dữ liệu nhạy cảm (PII) truyền qua lại.

## 7. Orchestration với LangGraph
Framework trực quan giúp biểu diễn đồ thị (graph) luồng chạy của Multi-agent.
- **Thành phần:** `Node` (hàm Python cập nhật State, tương ứng Agent), `Edge` (có thể conditional để điều hướng route) và `State` (dữ liệu truyền giữa các bước).
- Chuyển việc routing từ một câu prompt mông lung thành mã lập trình (code) cụ thể và rõ ràng, có điểm kết thúc hoặc điểm có người kiểm duyệt (`interrupt()` cho human-in-the-loop).
- Khả năng duy trì Persistence nhờ Checkpointer (gắn theo `thread_id`).

Rất quan trọng trong hệ Multi-agent vì lỗi không báo dạng "crash" mà thường sai về logic/ngữ nghĩa.
- Bắt buộc ghi **Trace Log** rõ ràng cho mỗi bước: `timestamp`, `agent_id`, `action`, I/O summary, `status`, `latency`. 
- Cần quan tâm Distributed Tracing: Sử dụng `trace_id` duy nhất chạy xuyên suốt (waterfall) từ router agent đến tận MCP tool.
- Có thể kết hợp chuẩn OTel GenAI Semconv cùng với các tool như LangSmith, Phoenix.

Multi-agent không phải là "nâng cấp miễn phí", mà là một sự đánh đổi lớn:
- **Cost và Latency:** Gọi LLM nhiều lần tăng đáng kể số lượng token và chi phí. Do đó, cần tối ưu bằng cách dùng model nhỏ cho routing (Supervisor), model lớn cho reasoning hẹp (Worker).
- **Reliability:** Cần phải thiết kế timeout, retry logic và Graceful degradation (Thất bại có kiểm soát, có phương án báo cáo rõ hoặc lấy partial data khi một worker bị fail thay vì chết toàn bộ hệ thống).
