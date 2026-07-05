---
type: summary
title: "Summary: day09-multi-agent-mcp-a2a-v3"
description: "A detailed summary of the day09-multi-agent-mcp-a2a-v3.pdf document."
tags: [day09, multi-agent, mcp, a2a]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/9/day09-multi-agent-mcp-a2a-v3.pdf"]
---

# Tổng quan (Overview)

Tài liệu "AICB-P1 · Ngày 9 · MCP, A2A & LangGraph" tập trung vào việc tổ chức hệ thống AI khi bài toán vượt quá khả năng của một **Single-Agent**. Giải pháp được đưa ra là xây dựng hệ thống **Multi-Agent**, sử dụng chuẩn kết nối công cụ **MCP (Model Context Protocol)**, giao thức giao tiếp giữa các agents **A2A (Agent-to-Agent)**, và sử dụng **LangGraph** để điều phối (orchestration).

---

## 1. Giới hạn của Single-Agent
Một agent duy nhất thường bị quá tải khi phải gánh vác nhiều trách nhiệm, đối mặt với 4 giới hạn cốt lõi:
1. **Context bottleneck**: Phải nạp quá nhiều thông tin, context window dễ bị tràn, dẫn đến hiện tượng quên hoặc mất thông tin ở giữa (lost-in-the-middle).
2. **Specialization trade-off**: Càng ôm nhiều vai, prompt càng phức tạp, chất lượng phản hồi giảm, "giỏi đều" nhưng không xuất sắc ở phần nào.
3. **Parallelism hạn chế**: Hoạt động tuần tự khiến latency cao vì các công việc không phụ thuộc nhau không được xử lý song song.
4. **Reliability yếu**: Nếu chọn sai tool từ đầu luồng, sai số sẽ làm hỏng toàn bộ quy trình do không có ranh giới cô lập lỗi.

## 2. Các Multi-Agent Patterns
Thay vì "god agent", ta thiết kế hệ thống thành nhiều phần dựa trên trách nhiệm. 4 pattern phổ biến:
- **Supervisor-worker**: 1 Supervisor đóng vai trò điều phối các Workers làm phần việc hẹp. Pattern này dễ kiểm soát, dễ theo dõi lỗi (trace) và được chọn làm trọng tâm của Day 09.
- **Pipeline**: Luồng tuyến tính (A -> B -> C), thích hợp với quy trình cố định.
- **Debate**: Nhiều agent cùng giải quyết và phản biện, giảm blind spot.
- **Hierarchical**: Phân nhánh thành nhiều tầng supervisor để xử lý quy mô enterprise.

## 3. Kiến trúc Supervisor-Worker
- **Supervisor**: Không cần mô hình (model) lớn, chuyên trách nhiệm vụ điều hướng (routing): phân tích yêu cầu, gọi các worker tương ứng, theo dõi và tổng hợp đầu ra.
- **Worker**: Phụ trách một năng lực nhỏ, hẹp (như *Retrieval Worker*, *Tool Worker*, *Synthesis Worker*). Worker nên được thiết kế stateless, có đầu vào/ra rõ ràng. Lỗi ở worker sẽ được khoanh vùng.
- **Shared State vs Message Passing**: Dữ liệu có thể truyền qua trạng thái chung (shared state) hoặc thông điệp. Cần quản lý cấu trúc state rõ ràng, bắt buộc có `trace` log để lưu lịch sử hoạt động.

## 4. MCP (Model Context Protocol)
- **Vấn đề cũ**: Việc nối tools cho agent trước đây đòi hỏi viết custom adapter, khó maintain.
- **Giải pháp**: MCP cung cấp một tiêu chuẩn giao tiếp duy nhất giữa agent và các external capabilities (tools, resources, prompts). MCP giống như cổng USB để cắm bất kì thiết bị nào chuẩn hóa.
- **Hoạt động**: Agent gọi server để list tools, nhận schema, và sử dụng tool phù hợp mà không cần lập trình cứng (hard-code).

## 5. A2A (Agent-to-Agent Communication)
- Khác với MCP (nối với hệ thống không có tri giác/agency), **A2A** quy định cách các agents trao đổi công việc với nhau.
- Cốt lõi của A2A là **Message Contract**: Supervisor phải truyền đúng/đủ context (cần làm gì, với thông tin nào, format đầu ra mong đợi).
- Nguyên tắc "need to know": Không ném toàn bộ lịch sử trò chuyện cho worker, chỉ đưa đúng phần context nó cần thiết để hoàn thành nhiệm vụ.

## 6. Orchestration với LangGraph
- LangGraph biểu diễn hệ thống thành một luồng minh bạch:
  - **Node**: Hàm xử lý, tương ứng agent hoặc bước thao tác.
  - **Edge**: Luồng đi đến đâu (Unconditional hoặc Conditional route).
  - **State**: Bộ nhớ của graph đi qua các node.
- Việc sử dụng LangGraph giúp gỡ rối việc route bị giấu sâu trong prompt điều phối lớn. Graph hỗ trợ can thiệp của con người (Human-in-the-loop) để kiểm duyệt kết quả rủi ro cao.

## 7. Observability & Debugging
- Debugging ở hệ thống nhiều tác nhân là cực kì khó nếu thiếu Trace Log. 
- Trace Log cần ghi lại chi tiết: ai làm (agent), làm gì (action), đầu vào là gì, kết quả ra sao, latency, error status.
- Dữ liệu trace dùng để cải tiến các bước (như sửa lại prompt của worker hay logic của route), hoặc sử dụng công cụ chuyên nghiệp như LangSmith.

## 8. Đánh đổi (Trade-off): Cost, Latency & Reliability
- **Cost và Latency**: Multi-agent tốn token và phí LLM cao hơn do nhiều calls rời rạc. Tuy nhiên, nó cho phép chạy song song và tối ưu chi phí bằng cách xài model nhỏ cho supervisor.
- **Reliability (Độ tin cậy)**: Hệ thống phải được thiết kế có fallback, retry, và Graceful Degradation (hệ thống chịu lỗi cục bộ mà không chết toàn bộ).

---

## Tóm lại (Key Takeaways)
1. Multi-agent không phải là phép màu, chỉ dùng khi một agent quá tải.
2. Supervisor route công việc, Worker chuyên sâu một tác vụ.
3. MCP là chuẩn nối tools từ bên ngoài, A2A là contract giao tiếp giữa các agents.
4. LangGraph giúp trực quan hóa và lập trình luồng state một cách rõ ràng.
5. Observability (Trace) là điều kiện bắt buộc để debug và hoàn thiện multi-agent.
