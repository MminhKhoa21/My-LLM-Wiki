---
type: summary
title: "Day 20 Track 3: Multi-Agent Systems"
description: "Kiến trúc hệ thống Multi-Agent"
tags: [ai, 20k, day20]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/20/day05-multi-agent-systems-student.pdf"]
---

> **Lộ trình:** [[track3_ai_app|Track 3: AI Application]]


# Multi-Agent Systems

Khám phá cách tổ chức nhiều Agent làm việc cùng nhau khi các task trở nên quá phức tạp đối với Single Agent.
- **Supervisor Pattern (Orchestration)**: Hub-and-Spoke, một router trung tâm (Supervisor) điều phối các agent vệ tinh (Workers).
- **Debate / Adversarial**: Giảm hallucination bằng cách để các agent tranh luận với nhau trước khi tổng hợp kết quả (Judge).
- **Parallel Execution & Shared State**: Sử dụng Map-Reduce và AsyncIO để tăng tốc độ.
- **Multi-Agent Frameworks**: So sánh LangGraph, AutoGen, và CrewAI dựa trên control và linh hoạt.
