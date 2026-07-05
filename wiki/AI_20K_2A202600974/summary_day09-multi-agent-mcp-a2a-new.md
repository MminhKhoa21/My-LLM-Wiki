---
type: summary
title: "Summary: day09-multi-agent-mcp-a2a-new"
description: "A detailed summary of the day09-multi-agent-mcp-a2a-new.pdf document."
tags: [day09, multi-agent, mcp, a2a]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/9/day09-multi-agent-mcp-a2a-new.pdf"]
---

# Summary: Multi-Agent & System Integration (Day 09)

## 1. Giới thiệu (Introduction)
Tài liệu là bài giảng **Ngày 9** trong chương trình AICB Phase 1 (VinUniversity). Bài giảng tập trung vào cách chuyển đổi từ một hệ thống **Single-Agent** sang **Multi-Agent**, cách kết nối với các công cụ bằng chuẩn **MCP (Model Context Protocol)**, cách các agent giao tiếp qua **A2A (Agent to Agent)**, và cách điều phối (orchestration) bằng **LangGraph**.

## 2. Giới hạn của Single-Agent
Khi hệ thống phức tạp dần, một agent không thể gồng gánh toàn bộ do 4 giới hạn:
1. **Context bottleneck**: Agent phải nhớ mục tiêu, output của tool, lịch sử chat... dẫn tới vượt quá context window và bị "lost-in-the-middle".
2. **Specialization trade-off**: Yêu cầu agent làm quá nhiều vai khiến prompt phình to, độ ổn định giảm.
3. **Parallelism hạn chế**: Agent chạy tuần tự khiến độ trễ (latency) tăng cao.
4. **Reliability yếu**: Lỗi ở một bước đầu (như route sai công cụ) làm hỏng cả chuỗi xử lý.

## 3. Các mẫu thiết kế (Patterns) Multi-Agent
Có 4 pattern phổ biến:
- **Supervisor-Worker**: Một quản lý (Supervisor) phân việc cho các chuyên viên (Worker). Dễ kiểm soát, dễ theo dõi trace.
- **Pipeline**: Chạy tuần tự, phù hợp workflow tĩnh.
- **Debate**: Phản biện giữa nhiều agent, hợp với tác vụ cần nhiều góc nhìn.
- **Hierarchical**: Phân cấp quản lý tầng tầng lớp lớp, cho hệ thống quy mô doanh nghiệp.

*Khóa học ưu tiên mẫu **Supervisor-Worker** vì dễ hiểu, rõ ràng định tuyến và dễ cắm thêm worker/tool.*

## 4. Kiến trúc Supervisor-Worker
- **Supervisor**: Phân tích yêu cầu, chọn worker phù hợp, theo dõi, retry khi lỗi và tổng hợp đầu ra.
- **Worker**: Chuyên trách 1 nghiệp vụ (ví dụ: Retrieval, Tool call, Synthesis). Càng stateless càng tốt và phải testable độc lập.
- **Shared State**: Trạng thái chia sẻ phải có schema rõ, gồm: `task`, `plan`, `worker_results`, `status`, `final_answer`, và quan trọng nhất là **`trace`** (lịch sử hành động).

## 5. Giao tiếp: MCP và A2A
- **MCP (Model Context Protocol)**: Chuẩn kết nối giữa Agent và External Capabilities (Tools/DB). MCP cho phép agent "khám phá" các công cụ khả dụng một cách linh hoạt như cắm USB vào máy tính mà không cần code hard-code adapter riêng.
- **A2A (Agent to Agent)**: Cách thức các agent giao việc. Yêu cầu có Message Contract rõ ràng bao gồm: `Task` (làm gì), `Context` (cần biết gì) và `Expected Output` (trả về định dạng nào).

## 6. Điều phối bằng LangGraph
LangGraph giúp chuyển hóa logic ẩn trong prompt thành code định tuyến tường minh, dưới dạng đồ thị:
- **Node**: Ai làm (Agent/Worker).
- **Edge**: Đi đâu tiếp theo (Luồng định tuyến - Routing logic).
- **State**: Trạng thái chung của hệ thống.
LangGraph còn giúp dễ dàng triển khai **Human-in-the-loop** (Dừng luồng chờ con người duyệt) khi thao tác có độ rủi ro cao hoặc cần quyết định quan trọng.

## 7. Quan sát (Observability) & Debugging
Multi-agent phức tạp và rất khó debug nếu không có **Trace log** tốt.
- Mỗi log entry tối thiểu cần có: `timestamp`, `agent_id`, `action`, `input_summary`, `output_summary`, `status`, `latency_ms`.
- Trace log không chỉ để sửa lỗi mà còn là dữ liệu nền tảng để cải tiến hệ thống định kỳ.

## 8. Cân nhắc Trade-off
- **Chi phí & Độ trễ**: Multi-agent tốn chi phí LLM cao hơn và độ trễ có thể cao nếu chạy tuần tự.
- **Reliability & Graceful Degradation**: Khi worker gặp sự cố, hệ thống cần có cơ chế retry hoặc fallback, chấp nhận xử lý thiếu hoàn thiện chứ không sụp đổ toàn bộ.

## Tổng kết
Đưa hệ thống lên Multi-Agent là câu chuyện của việc **phân chia vai trò** cho hệ thống dễ kiểm soát hơn, kết hợp với các **giao thức chuẩn (MCP/A2A)** để giảm độ khó trong liên kết, và **Trace log** để có thể nắm bắt đường đi của hệ thống.
