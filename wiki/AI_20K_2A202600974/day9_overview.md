---
type: overview
title: "Day 9: Multi-Agent & System Integration"
description: "Kiến trúc hệ thống Multi-Agent, thiết kế các pattern (Supervisor-worker) và giao thức kết nối Model Context Protocol (MCP)."
tags: [ai, 20k, day9, multi-agent, mcp]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/9/day09-multi-agent-mcp-a2a-v3.pdf"]
---

# Day 9: Multi-Agent & Kết Nối Hệ Thống

## Nội dung chính
Bài học tập trung vào cách tổ chức hệ thống AI khi một Agent đơn lẻ ("God Agent") trở nên quá tải.
- **Giới hạn của Single-Agent**: Bị thắt cổ chai về context window, đánh đổi về sự chuyên biệt (specialization trade-off), hạn chế chạy song song, và độ tin cậy yếu.
- **Các mô hình (patterns) Multi-Agent**: 
  - **Supervisor-worker**: Một supervisor điều phối các worker chuyên biệt. Routing rõ ràng, dễ kiểm soát.
  - **Pipeline**: Flow tuyến tính, tuần tự, phù hợp khi các bước gần như cố định.
  - **Debate**: Cần nhiều góc nhìn cho một bài toán, tăng cường phản biện.
  - **Hierarchical**: Mở rộng cho hệ thống lớn, quản lý nhiều tầng.

## Kết nối hệ thống và Giao tiếp
- **Model Context Protocol (MCP)**: Một chuẩn giao tiếp duy nhất giữa Agent và Tool/Resource, giúp loại bỏ việc hard-code từng API một. Agent tự động khám phá và thực thi tools thông qua server MCP.
- **Agent-to-Agent (A2A)**: Thiết kế giao tiếp giữa các agent. Thay vì chỉ trao đổi qua lại tự do (chatty workers gây tốn kém và khó theo dõi), A2A hiệu quả hơn khi định nghĩa **Message Contract** rõ ràng về định dạng input/output.
- **Shared State vs Message Passing**: Shared state (ví dụ lưu trong LangGraph) mang lại cái nhìn toàn cảnh và dễ phối hợp, nhưng cần định nghĩa cấu trúc (schema) chặt chẽ.

## Orchestration và CI/CD
- **LangGraph**: Framework chuyên dụng quản lý đồ thị các Agent, giúp định nghĩa rõ ràng nodes (hành động), edges (điều kiện route) và state. Giúp debug và tích hợp Human-in-the-loop dễ dàng hơn.
- Cần có sự minh bạch và có các công cụ quan sát (**Trace Log**) tốt để debug nhanh khi hệ thống gặp trục trặc, xem rõ agent nào gọi tool gì, quyết định ra sao.
