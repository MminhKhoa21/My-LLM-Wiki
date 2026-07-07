---
type: summary
title: "Summary: day09-lecture-slide"
description: "A detailed summary of the day09-lecture-slide.pdf document."
tags: [day09, multi-agent, lecture-slides]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/9/day09-lecture-slide.pdf"]
---

# Summary: AI in Action - Day 09 (Multi-Agent & System Integration)
# Tóm tắt: AI in Action - Ngày 09 (Đa tác nhân & Tích hợp Hệ thống)

This document summarizes the Day 09 lecture slides of the "AI in Action" course, focusing on transitioning from a single overloaded agent to a robust multi-agent system with clear roles, leveraging tools like LangGraph, MCP, and A2A communication.
Tài liệu này tóm tắt các trang trình bày bài giảng Ngày 09 của khóa học "AI in Action", tập trung vào việc chuyển đổi từ một tác nhân đơn lẻ bị quá tải sang một hệ thống đa tác nhân mạnh mẽ với các vai trò rõ ràng, tận dụng các công cụ như LangGraph, MCP, và giao tiếp A2A.

## 1. Context & Use Case
## 1. Bối cảnh & Trường hợp Sử dụng
- **Use Case:** Internal assistant for CS (Customer Success) and IT Helpdesk. Tasks include handling refund policies (e.g., 7-day refund policy), P1 SLA (Service Level Agreements), and access approval workflows.
- **Trường hợp Sử dụng:** Trợ lý nội bộ cho CS (Thành công của Khách hàng - Customer Success) và bộ phận Hỗ trợ CNTT. Các tác vụ bao gồm xử lý các chính sách hoàn tiền (ví dụ: chính sách hoàn tiền trong 7 ngày), P1 SLA (Thỏa thuận Mức Dịch vụ cho sự cố ưu tiên cao), và các quy trình phê duyệt quyền truy cập.
- **Goal of Day 09:** Add an orchestration layer (Supervisor + Workers) to the RAG pipeline built in Day 08. Emphasizes clear roles, traceability, and extensibility.
- **Mục tiêu của Ngày 09:** Thêm một lớp điều phối (Người giám sát + Công nhân) vào đường ống RAG đã xây dựng ở Ngày 08. Nhấn mạnh các vai trò rõ ràng, khả năng truy xuất nguồn gốc và khả năng mở rộng.

## 2. The Limits of Single Agents
## 2. Giới hạn của Các Tác nhân Đơn lẻ
A single monolithic agent can become a bottleneck when it is forced to plan, retrieve, call tools, synthesize, monitor, and retry all at once. The core limits are:
Một tác nhân nguyên khối đơn lẻ có thể trở thành nút thắt cổ chai khi nó bị buộc phải lập kế hoạch, truy xuất, gọi công cụ, tổng hợp, giám sát và thử lại tất cả cùng một lúc. Các giới hạn cốt lõi là:
- **Context bottleneck:** Prompt size bloats.
- **Nút thắt ngữ cảnh:** Kích thước câu lệnh phình to.
- **Specialization trade-off:** Hard to perform many different tasks well with a single prompt.
- **Đánh đổi sự chuyên môn hóa:** Khó để thực hiện tốt nhiều tác vụ khác nhau chỉ với một câu lệnh đơn lẻ.
- **Parallelism limits:** Independent tasks are forced to run sequentially.
- **Giới hạn tính song song:** Các tác vụ độc lập bị buộc phải chạy tuần tự.
- **Reliability:** A routing error early on ruins the entire workflow. 
- **Độ tin cậy:** Một lỗi định tuyến ngay từ đầu sẽ phá hỏng toàn bộ quy trình làm việc.
*Rule of thumb:* Multi-agent systems should be used not just to sound impressive, but to decouple logic and improve system observability.
*Nguyên tắc chung:* Hệ thống đa tác nhân nên được sử dụng không chỉ để nghe cho ấn tượng, mà là để tách biệt logic và cải thiện khả năng quan sát hệ thống.

## 3. Multi-Agent Patterns
## 3. Các Mô hình Đa tác nhân
Four common patterns were introduced:
Bốn mô hình phổ biến đã được giới thiệu:
1. **Supervisor-Worker:** Clear routing, easy to trace. (Focus of Day 09).
1. **Người giám sát - Công nhân (Supervisor-Worker):** Định tuyến rõ ràng, dễ truy xuất. (Trọng tâm của Ngày 09).
2. **Pipeline:** Linear flow, good for fixed SOPs (Standard Operating Procedures).
2. **Đường ống (Pipeline):** Luồng tuyến tính, tốt cho các SOP (Quy trình Vận hành Tiêu chuẩn) cố định.
3. **Debate:** Multiple perspectives to reduce blind spots.
3. **Tranh luận (Debate):** Nhiều góc nhìn để giảm thiểu điểm mù.
4. **Hierarchical:** Excellent scaling for separate domains.
4. **Phân cấp (Hierarchical):** Khả năng mở rộng tuyệt vời cho các miền tách biệt.

### Supervisor-Worker Pattern Deep Dive
### Đi sâu vào Mô hình Người giám sát - Công nhân
- **Supervisor:** Responsible for making routing decisions and keeping track of the state. It does *not* need to be the smartest agent; it just delegates cleanly.
- **Người giám sát:** Chịu trách nhiệm đưa ra các quyết định định tuyến và theo dõi trạng thái. Nó *không* cần phải là tác nhân thông minh nhất; nó chỉ cần phân quyền một cách rõ ràng.
- **Workers:** Specialized agents (e.g., Retrieval Worker, Tool/Policy Worker, Synthesis Worker) with narrow, well-defined skills.
- **Công nhân:** Các tác nhân chuyên trách (ví dụ: Công nhân Truy xuất, Công nhân Công cụ/Chính sách, Công nhân Tổng hợp) với các kỹ năng hẹp, được xác định rõ.
- **Contracts:** Communication relies on clear JSON contracts (tasks, constraints, expected output, errors) which makes workers testable and replaceable.
- **Hợp đồng (Contracts):** Giao tiếp dựa trên các hợp đồng JSON rõ ràng (các tác vụ, các ràng buộc, đầu ra mong đợi, lỗi) giúp cho các công nhân có thể kiểm thử và thay thế được.

## 4. MCP (Model Context Protocol) vs. A2A (Agent-to-Agent)
## 4. MCP (Giao thức Ngữ cảnh Mô hình) vs. A2A (Tác nhân-với-Tác nhân)
- **MCP (Client-Server Architecture):** A standard interface for connecting agents to external capabilities (Tools, Resources, Prompts) without hard-coding integrations.
- **MCP (Kiến trúc Máy khách - Máy chủ):** Một giao diện tiêu chuẩn để kết nối các tác nhân với các khả năng bên ngoài (Công cụ, Tài nguyên, Câu lệnh) mà không cần lập trình tích hợp cứng (hard-coding).
  - *Tools:* Actions with side effects (e.g., Zendesk, Jira APIs).
  - *Công cụ:* Các hành động có tác dụng phụ (ví dụ: API của Zendesk, Jira).
  - *Resources:* Static data (e.g., schemas, docs).
  - *Tài nguyên:* Dữ liệu tĩnh (ví dụ: lược đồ, tài liệu).
  - *Prompts:* Predefined instructions/templates.
  - *Câu lệnh:* Các hướng dẫn/mẫu được định nghĩa trước.
- **A2A:** Agents delegating tasks or cooperating with other agents (e.g., Handoff, Cooperative Search, Concurrent Debate, Self-Correction, Joint Decision).
- **A2A:** Các tác nhân ủy thác tác vụ hoặc hợp tác với các tác nhân khác (ví dụ: Chuyển giao, Tìm kiếm Hợp tác, Tranh luận Đồng thời, Tự Sửa lỗi, Quyết định Chung).
- *Rule of thumb:* Use MCP to fetch a capability or execute a tool. Use A2A to assign a task to another intelligent role.
- *Nguyên tắc chung:* Sử dụng MCP để lấy một khả năng hoặc thực thi một công cụ. Sử dụng A2A để giao một nhiệm vụ cho một vai trò thông minh khác.

## 5. LangGraph & Orchestration Implementation
## 5. LangGraph & Triển khai Điều phối
- **Core Components:** Nodes (who acts), Edges (where to go next), State (what the system knows), Checkpointer (memory/time travel), and Routing (the decision logic).
- **Các Thành phần Cốt lõi:** Nodes (ai hành động), Edges (đi đâu tiếp theo), State (hệ thống biết gì), Checkpointer (bộ nhớ/du hành thời gian), và Routing (logic quyết định).
- **HITL (Human-in-the-Loop):** Essential for high-risk actions (refunds, access changes) or low confidence scenarios. LangGraph supports adding breakpoints for human review.
- **HITL (Con người trong Vòng lặp):** Cực kỳ cần thiết cho các hành động có rủi ro cao (hoàn tiền, thay đổi quyền truy cập) hoặc các tình huống có độ tin cậy thấp. LangGraph hỗ trợ thêm các điểm dừng (breakpoints) để con người đánh giá.
- **Sub-graphs:** Breaking down massive flows into modular, reusable team-based graphs (e.g., `IT_Graph`, `Sales_Graph`).
- **Đồ thị con (Sub-graphs):** Chia nhỏ các luồng khổng lồ thành các đồ thị dạng mô-đun, có thể tái sử dụng dựa trên nhóm (ví dụ: `IT_Graph`, `Sales_Graph`).
- **State vs. Message Passing:** Use *shared state* to orchestrate the entire flow and *message contracts* to assign tasks across worker boundaries.
- **Trạng thái (State) vs. Truyền Tin nhắn:** Sử dụng *trạng thái chia sẻ* để điều phối toàn bộ luồng và *hợp đồng tin nhắn* để giao nhiệm vụ xuyên qua ranh giới của các công nhân.

## 6. Hands-on Lab Overview
## 6. Tổng quan Bài thực hành
Students are expected to refactor their single-agent RAG from Day 08 into a multi-agent orchestration setup consisting of:
Học viên được kỳ vọng sẽ tái cấu trúc (refactor) RAG tác nhân đơn lẻ từ Ngày 08 thành một thiết lập điều phối đa tác nhân bao gồm:
1. **Refactoring the graph:** Establish a basic Supervisor flow.
1. **Tái cấu trúc đồ thị:** Thiết lập một luồng Người giám sát cơ bản.
2. **Building workers:** Retrieval, Tool/Policy, and Synthesis workers.
2. **Xây dựng công nhân:** Các công nhân Truy xuất, Công cụ/Chính sách, và Tổng hợp.
3. **Adding MCP:** Connect at least one real or mocked external capability.
3. **Thêm MCP:** Kết nối ít nhất một khả năng bên ngoài thực tế hoặc được mô phỏng.
4. **Trace & Documentation:** Provide a readable execution trace showing route logic, node inputs/outputs, and compare single vs. multi-agent performance.
4. **Theo dõi (Trace) & Tài liệu:** Cung cấp một bản theo dõi thực thi dễ đọc cho thấy logic định tuyến, đầu vào/đầu ra của node, và so sánh hiệu suất giữa tác nhân đơn lẻ và đa tác nhân.

## Key Takeaway
## Điểm chính Rút ra
Multi-agent isn't about simply having more agents; it's about separating concerns so the system's reasoning path is observable, testable, and reliable. Proper tracing is the foundation for Day 10's focus on observability and data pipelines.
Đa tác nhân không chỉ đơn giản là có nhiều tác nhân hơn; mà là việc tách biệt các mối quan tâm để con đường suy luận của hệ thống có thể quan sát được, kiểm thử được và đáng tin cậy. Việc theo dõi (tracing) đúng cách là nền tảng cho trọng tâm của Ngày 10 về khả năng quan sát và các đường ống dữ liệu.
