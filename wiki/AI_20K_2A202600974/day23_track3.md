---
type: summary
title: "Day 23 – Track 3: LangGraph & Agentic Orchestration"
description: "State machine cho AI Agents: Core API, Persistence, Human-in-the-Loop, và Error Recovery với LangGraph."
tags: [ai, 20k, day23, track3, langgraph, agent, orchestration]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/23/day08_langgraph_student.pdf"]
---

> **Lộ trình:** [[track3_ai_app|Track 3: AI Application]]


# Day 23 – Track 3: LangGraph & Agentic Orchestration

**Giảng viên**: VinUniversity  
**Khóa**: AICB Phase 2 · Track 3 · Ngày 23

> **Câu hỏi trọng tâm**: Khi agent cần loop, retry, human approval và resume sau crash, chain một chiều còn đủ không?

---

## Khi nào Chain không đủ?

| Vấn đề | Chain truyền thống | LangGraph |
|--------|-------------------|-----------|
| Loop & retry | ❌ Không hỗ trợ | ✅ State machine |
| Human approval giữa chừng | ❌ Không thể pause | ✅ Interrupt + resume |
| Resume sau crash | ❌ Mất state | ✅ Checkpointing |
| Nhánh điều kiện phức tạp | ❌ Khó viết | ✅ Conditional edges |

---

## Core API

| Thành phần | Vai trò |
|-----------|---------|
| **StateGraph** | Container chứa toàn bộ workflow |
| **Nodes** | Các hàm xử lý (llm call, tool call, router...) |
| **Edges** | Kết nối giữa nodes (normal hoặc conditional) |
| **State** | TypedDict chia sẻ giữa tất cả nodes |
| **Callbacks** | Hook để log, trace, monitor |

---

## Persistence & Time Travel

- **Checkpointer**: Lưu state sau mỗi node (dùng `MemorySaver` hoặc `SqliteSaver`)
- **Time Travel**: Replay lại từ bất kỳ checkpoint nào để debug hoặc branch
- **Thread ID**: Mỗi conversation có thread riêng → hỗ trợ multi-user

---

## Human-in-the-Loop & Error Recovery

```python
# Pause tại node cần human approval
graph.add_node("human_review", human_review_node)
graph.interrupt_before(["human_review"])

# Resume sau khi human approve
graph.invoke(state, config={"configurable": {"thread_id": "abc"}})
```

---

## Liên kết
- [[day9_overview]] – Multi-Agent & MCP (foundation)
- [[day27_track1]] – Human-in-the-Loop UX (nâng cao)
- [[day23_overview]]
