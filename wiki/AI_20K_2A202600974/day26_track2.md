---
type: summary
title: "Day 26 – Track 2: MCP/A2A Infrastructure & Fundraising"
description: "Thiết kế hạ tầng Agentic Routing với MCP/A2A và kiến thức Fundraising cho startup AI."
tags: [ai, 20k, day26, track2, mcp, a2a, infrastructure, fundraising]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/26/day26-mcp-a2a-infrastructure-agentic-routing-no-k8s.pdf", "raw/AI_20K_2A202600974/26/d26-Fundraising.pdf"]
---

> **Lộ trình:** [[track2_ai_engineer|Track 2: AI Engineer]]


# Day 26 – Track 2: MCP/A2A Infrastructure & Fundraising

**Giảng viên**: VinUniversity  
**Khóa**: AICB Phase 2 · Track 2 · Ngày 26

> **Câu hỏi trọng tâm**: Agent gọi agent – infra của bạn có scale được cho multi-agent choreography không?

---

## MCP/A2A Infrastructure

### Vấn đề: Research system cần 4 specialized agents phối hợp

Nếu không có chuẩn giao tiếp, mỗi agent nói "ngôn ngữ" riêng → **MCP + A2A = universal protocol** cho AI agent ecosystem.

### Nội dung chính

| Chủ đề | Nội dung |
|--------|---------|
| **Model Context Protocol (MCP)** | Chuẩn hóa giao tiếp Agent ↔ Tool |
| **Agent-to-Agent (A2A)** | Chuẩn hóa giao tiếp Agent ↔ Agent |
| **Agentic Routing Patterns** | Semantic routing, load balancing |
| **State Management** | Shared state, distributed checkpoint |
| **Security & Governance** | Auth, rate limiting, audit trail |
| **Observability** | Trace multi-agent flows với OpenTelemetry |
| **Live Demo** | Research System với Google ADK |

### Các Routing Patterns

```
Request → Semantic Router → Agent Pool
                              ├── Researcher Agent
                              ├── Writer Agent
                              └── Critic Agent
```

---

## Fundraising cho AI Startup

**Giảng viên**: Co-founder Fundwise, Head of Incubator VNU

> "Money is the fuel for your company"

### Các giai đoạn funding

| Stage | Amount | Investors |
|-------|--------|-----------|
| **Pre-seed** | $50K–$500K | Friends, Angels |
| **Seed** | $500K–$3M | Seed VCs, Angels |
| **Series A** | $3M–$15M | VCs |
| **Series B+** | $15M+ | Growth VCs |

### Pitch deck essentials

1. Problem & Market size
2. Solution & Demo
3. Traction & Metrics
4. Business model
5. Team
6. Ask & Use of funds

---

## Liên kết
- [[day26_track3]] – MCP Tool Integration (technical detail)
- [[day9_overview]] – Multi-Agent & MCP (foundation)
- [[day26_overview]]
