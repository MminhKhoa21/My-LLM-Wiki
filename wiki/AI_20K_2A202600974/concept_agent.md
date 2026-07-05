---
type: concept
title: "AI Agents & Orchestration"
description: "Tổng hợp kiến thức về AI Agent, Multi-Agent và Agentic Orchestration qua các ngày."
tags: [ai, 20k, concept, agent, orchestration]
timestamp: 2026-07-05
sources: []
---

# AI Agents & Orchestration

Trang này tổng hợp các kiến thức liên quan đến AI Agent, từ thiết kế Single Agent đến Multi-Agent Orchestration trong suốt khóa học.

## 1. Single Agent Foundation (Day 1 - 7)
- **Định nghĩa**: Agent = LLM + Memory + Tools + Planning. Khác với LLM chat bình thường, Agent có khả năng nhận task, lập kế hoạch, gọi tool để tương tác với thế giới thực và tự sửa lỗi (self-reflection).
- **Tool Calling**: Khả năng cơ bản nhất của Agent để chạy code, query database, gọi API.

## 2. Multi-Agent & Routing (Day 9, Day 26)
- **Vấn đề**: Một Agent làm mọi việc sẽ bị quá tải context, dễ nhầm lẫn tool và mất focus.
- **Giải pháp Multi-Agent**: Chia bài toán thành các Specialist Agents (VD: Researcher, Writer, Reviewer).
- **Agentic Routing**: Sử dụng Semantic Router để phân loại request và chuyển đến đúng Agent.
- **MCP & A2A Protocol ([[day26_track2]], [[day26_track3]])**:
  - **MCP (Model Context Protocol)**: Chuẩn hóa giao tiếp giữa Agent và Tool, giải quyết vấn đề N models × M tools = N×M integrations.
  - **A2A**: Chuẩn hóa giao tiếp Agent ↔ Agent.

## 3. Orchestration với LangGraph (Day 23)
- Các cấu trúc Chain một chiều (LangChain) không đủ khi Agent cần:
  - Loop & Retry (VD: Tự sửa lỗi code).
  - Human-in-the-Loop (Pause và Resume).
  - Checkpointing (Lưu state sau mỗi bước, resume sau khi crash).
- **LangGraph** giải quyết bằng **State Machine** (StateGraph, Nodes, Edges, State dict).
- Chi tiết: [[day23_track3]]

## 4. Human-in-the-Loop UX (Day 27)
- Cấp quyền tự quyết (Full Autonomy) cho Agent có thể nguy hiểm ở production.
- Cần thiết kế UX hợp lý: **Always ask** (high risk), **Ask if uncertain**, **Show then do**, **Do then show**, **Silent execution**.
- **Confidence Routing**: Routing request dựa trên độ tự tin của Agent.
- Chi tiết: [[day27_track1]]

## 5. AgentOps (Day 23)
- Giám sát Agent phức tạp hơn giám sát phần mềm truyền thống: cần theo dõi luồng suy nghĩ (trace loop), lịch sử gọi tool, chi phí (cost/FinOps) và tình trạng state.
- Chi tiết: [[day23_track2]]
