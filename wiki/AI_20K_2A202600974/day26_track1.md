---
type: summary
title: "Day 26 – Track 1: Lab MCP/A2A Routing (không dùng K8s)"
description: "Lab thực hành triển khai Agentic Routing với MCP và A2A protocol, không cần Kubernetes."
tags: [ai, 20k, day26, track1, mcp, a2a, lab]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/26/day26-track1-lab.pdf", "raw/AI_20K_2A202600974/26/day26-mcp-a2a-infrastructure-agentic-routing-no-k8s.pdf"]
---

> **Lộ trình:** [[track1_ba|Track 1: AI Product / BA]]


# Day 26 – Track 1: Lab MCP/A2A Agentic Routing

---

## Mục tiêu Lab

Triển khai một hệ thống multi-agent đơn giản sử dụng MCP + A2A mà không cần Kubernetes – dùng Docker Compose thay thế.

---

## Stack không dùng K8s

```
Nginx (reverse proxy)
  └── FastAPI Agent 1 (Researcher)
  └── FastAPI Agent 2 (Writer)
  └── MCP Server (Tool Registry)
  └── Redis (Shared State)
```

---

## Các bước thực hành

1. **Setup MCP Server**: Khởi tạo server, đăng ký các tools (search, write_file, send_email)
2. **Định nghĩa Message Contract**: Schema rõ ràng cho input/output giữa agents
3. **Implement Semantic Router**: Agent điều phối dựa trên nội dung request
4. **Test end-to-end**: Gửi request → Router → Agent → Tool → Response
5. **Đánh giá**: Latency, error rate, observability

---

## Liên kết
- [[day9_overview]] – Multi-Agent & MCP (nền tảng)
- [[day26_track2]] – MCP/A2A Infrastructure (lý thuyết)
- [[day26_track3]] – MCP Tool Integration (chi tiết protocol)
- [[day26_overview]]
