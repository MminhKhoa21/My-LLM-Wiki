---
type: summary
title: "Day 26 – Track 2: MCP/A2A Infrastructure & Agentic Routing"
description: "Comprehensive guide on building scalable multi-agent systems using Model Context Protocol (MCP) and Agent-to-Agent (A2A) protocols."
tags: [mcp, a2a, multi-agent, routing, orchestration, observability, infrastructure]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/26/day26-mcp-a2a-infrastructure-agentic-routing-no-k8s.pdf"]
---
```markdown
> **Lộ trình:** [[track2_ai_engineer|Track 2: AI Engineer]]
> * **Lộ trình:** [[track2_ai_engineer|Track 2: Kỹ sư AI]]*

# Day 26 – Track 2: MCP/A2A Infrastructure & Agentic Routing
Ngày 26 – Track 2: Hạ tầng MCP/A2A & Định tuyến Tác tử

This document summarizes the theory and practical architecture for building robust multi-agent systems. It covers the Model Context Protocol (MCP) as an infrastructure layer, the Agent-to-Agent (A2A) protocol for communication, routing strategies, state management, and essential observability practices.
Tài liệu này tóm tắt lý thuyết và kiến trúc thực hành để xây dựng các hệ thống đa tác tử mạnh mẽ. Nó bao gồm Giao thức Ngữ cảnh Mô hình (MCP) với vai trò là một lớp hạ tầng, giao thức Tác tử-với-Tác tử (A2A) cho giao tiếp, các chiến lược định tuyến, quản lý trạng thái, và các thực tiễn quan sát thiết yếu.

---

## 1. MCP: Infrastructure Layer for LLM Tools
1. MCP: Lớp Hạ tầng cho Công cụ LLM

**Model Context Protocol (MCP)** acts as the universal open protocol for LLMs to interface with tools, resources, and templates. It standardizes tool integrations so that developers only build servers once, enabling them to work across Claude, GPT, ADK, LangChain, etc.
***Giao thức Ngữ cảnh Mô hình (MCP)** đóng vai trò là một giao thức mở phổ quát để các LLM giao tiếp với các công cụ, tài nguyên và template. Nó chuẩn hóa việc tích hợp công cụ để các nhà phát triển chỉ cần xây dựng máy chủ một lần, cho phép chúng hoạt động trên các môi trường Claude, GPT, ADK, LangChain, v.v.*

- **Primitives:** 
- **Các thành phần cơ bản (Primitives):**
  - `Tools Server` (execute functions)
  - `Máy chủ Công cụ (Tools Server)` (thực thi các hàm)
  - `Resources Server` (expose data)
  - `Máy chủ Tài nguyên (Resources Server)` (trình bày dữ liệu)
  - `Prompts Server` (templates)
  - `Máy chủ Prompt (Prompts Server)` (các template)
- **Transports:** `stdio` (local subprocess), `HTTP+SSE` (remote), `WebSocket` (streaming).
- **Phương thức truyền dẫn (Transports):** `stdio` (tiến trình con cục bộ), `HTTP+SSE` (từ xa), `WebSocket` (truyền phát).
- **Implementation:** Defined using Python SDK decorators (e.g., `@app.tool()`). Clear docstrings are critical because LLMs read them to decide tool usage.
- **Triển khai:** Được định nghĩa bằng các decorator của Python SDK (ví dụ: `@app.tool()`). Các docstring rõ ràng là rất quan trọng vì các LLM sẽ đọc chúng để quyết định việc sử dụng công cụ.
- **Hosting & Registry:** Deployed locally or via remote APIs (FastAPI + uvicorn). Systems use an **Agent Registry pattern** to discover tools and capabilities (`/.well-known/agent-card.json`).
- **Lưu trữ & Đăng ký (Hosting & Registry):** Được triển khai cục bộ hoặc qua API từ xa (FastAPI + uvicorn). Các hệ thống sử dụng **mô hình Đăng ký Tác tử (Agent Registry pattern)** để khám phá công cụ và khả năng (`/.well-known/agent-card.json`).

## 2. A2A Protocol: Microservices for AI Agents
2. Giao thức A2A: Microservices cho Tác tử AI

The **Agent-to-Agent (A2A)** protocol treats individual AI agents as microservices. It standardizes how a primary orchestrator agent dispatches tasks and messages to specialist agents.
Giao thức **Tác tử-với-Tác tử (A2A)** coi các tác tử AI riêng lẻ như những microservices. Nó chuẩn hóa cách một tác tử điều phối (orchestrator) chính phân phát nhiệm vụ và tin nhắn cho các tác tử chuyên gia.

- **Communication:** Facilitated via Agent Cards, Tasks, and Messages.
- **Giao tiếp:** Được tạo điều kiện thông qua Thẻ Tác tử (Agent Cards), Nhiệm vụ (Tasks), và Tin nhắn (Messages).
- **Task Lifecycle:** `Submitted` -> `Working` -> `Input Required` -> `Completed` (or Failed/Canceled). Crucially, tasks can pause to ask the caller for more context rather than failing outright.
- **Vòng đời Nhiệm vụ:** `Đã nộp (Submitted)` -> `Đang xử lý (Working)` -> `Yêu cầu Đầu vào (Input Required)` -> `Hoàn thành (Completed)` (hoặc Thất bại/Bị hủy). Điểm mấu chốt là các nhiệm vụ có thể tạm dừng để yêu cầu người gọi cung cấp thêm bối cảnh thay vì thất bại hoàn toàn.
- **Orchestrator Pattern:** An orchestrator agent decomposes a user request, routes sub-tasks to specialists (e.g., Search Agent, Database Agent), and synthesizes the final response.
- **Mô hình Điều phối (Orchestrator Pattern):** Một tác tử điều phối sẽ phân tách yêu cầu của người dùng, định tuyến các nhiệm vụ phụ đến các chuyên gia (ví dụ: Tác tử Tìm kiếm, Tác tử Cơ sở dữ liệu), và tổng hợp câu trả lời cuối cùng.

## 3. Agentic Routing Strategies
3. Các Chiến lược Định tuyến Tác tử

Routing ensures tasks are dispatched to the right specialist agent.
Định tuyến đảm bảo các nhiệm vụ được phân phát cho đúng tác tử chuyên gia.
- **Keyword-based:** Fast but brittle (best for ≤ 5 agents).
- **Dựa trên từ khóa:** Nhanh nhưng dễ vỡ (tốt nhất cho ≤ 5 tác tử).
- **Embedding-based (Semantic Routing):** Embeds requests and calculates cosine similarity with agent capabilities (robust for 5-50 agents).
- **Dựa trên nhúng (Định tuyến Ngữ nghĩa):** Nhúng các yêu cầu và tính toán độ tương đồng cosine với khả năng của tác tử (mạnh mẽ cho 5-50 tác tử).
- **LLM-based:** Highly flexible but slow and expensive.
- **Dựa trên LLM:** Độ linh hoạt cao nhưng chậm và tốn kém.
- **Fallback chains:** Designing systems so tasks move from primary -> fallback -> human escalation to prevent dead-ends.
- **Chuỗi dự phòng (Fallback chains):** Thiết kế hệ thống sao cho nhiệm vụ chuyển từ chính -> dự phòng -> leo thang tới con người để tránh ngõ cụt.

## 4. State Management
4. Quản lý Trạng thái

- **Stateless (Recommended initially):** Easily scales horizontally. Context is externalized to databases like Redis (short-lived context) or PostgreSQL (persistent history).
- **Phi trạng thái (Được khuyến nghị ban đầu):** Dễ dàng mở rộng theo chiều ngang. Bối cảnh được kết xuất ra các cơ sở dữ liệu bên ngoài như Redis (bối cảnh tồn tại trong thời gian ngắn) hoặc PostgreSQL (lịch sử lưu trữ lâu dài).
- **Stateful:** Used for long-running conversations requiring sticky sessions, but harder to scale.
- **Có trạng thái:** Được sử dụng cho các cuộc trò chuyện kéo dài cần phiên dính (sticky sessions), nhưng khó mở rộng hơn.

## 5. Security & Governance
5. Bảo mật & Quản trị

A "Defense in Depth" principle is required for production agentic systems:
Một nguyên tắc "Phòng thủ Chiều sâu" là bắt buộc đối với các hệ thống tác tử trong môi trường sản xuất:
- **Rate Limiting:** Per-agent and per-user limits.
- **Giới hạn Tỷ lệ (Rate Limiting):** Các giới hạn trên mỗi tác tử và trên mỗi người dùng.
- **Sandbox Execution:** Running agent code in isolated environments.
- **Thực thi Sandbox:** Chạy mã tác tử trong các môi trường bị cô lập.
- **Human-in-the-Loop (HITL):** Requiring human approval for high-stakes actions (e.g., DB writes, sending emails, spending budgets).
- **Người trong Vòng lặp (HITL):** Yêu cầu sự phê duyệt của con người đối với các hành động rủi ro cao (ví dụ: ghi vào DB, gửi email, chi tiêu ngân sách).
- **Minimal Capability:** Agents are only granted the specific tools they need (Capability Matrix).
- **Khả năng Tối thiểu:** Tác tử chỉ được cấp các công cụ cụ thể mà chúng cần (Ma trận Khả năng).
- **Audit Logging:** Every invocation must log timestamps, agent IDs, and I/O payload.
- **Ghi log Kiểm toán:** Mỗi lần gọi phải ghi nhận timestamp, ID tác tử, và tải trọng (payload) I/O.

## 6. Observability for Multi-Agent Systems
6. Khả năng Quan sát cho Hệ thống Đa tác tử

- **Distributed Tracing:** Implementing W3C Trace Context across A2A calls. A single Trace ID maps the orchestrator span to all sub-agent and tool call spans.
- **Truy vết Phân tán:** Triển khai W3C Trace Context xuyên suốt các lệnh gọi A2A. Một Trace ID duy nhất sẽ ánh xạ span của điều phối viên đến tất cả các span của tác tử phụ và lệnh gọi công cụ.
- **Metrics:** Tracking task completion rates, average durations, tool call counts, and token costs per agent.
- **Số liệu:** Theo dõi tỷ lệ hoàn thành nhiệm vụ, thời lượng trung bình, số lượng cuộc gọi công cụ, và chi phí token cho mỗi tác tử.

## 7. Lab: Multi-Agent Research System
7. Lab: Hệ thống Nghiên cứu Đa tác tử

The lab focuses on implementing a 4-agent system (1 Orchestrator + 3 Specialists) utilizing A2A, MCP, and strict governance audits without relying on Kubernetes (using a local Conda/ADK setup).
Bài lab tập trung vào việc triển khai một hệ thống 4 tác tử (1 Điều phối viên + 3 Chuyên gia) tận dụng A2A, MCP, và các đợt kiểm toán quản trị nghiêm ngặt mà không phụ thuộc vào Kubernetes (sử dụng thiết lập Conda/ADK cục bộ).
```
