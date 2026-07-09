---
type: summary
title: "Day 23 – Track 3: LangGraph & Agentic Orchestration"
description: "State machine cho AI Agents: Core API, Persistence, Human-in-the-Loop, và Error Recovery với LangGraph."
tags: [ai, 20k, day23, track3, langgraph, agent, orchestration]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/23/day08_langgraph_student.pdf"]
---


# Day 23 – Track 3: LangGraph & Agentic Orchestration






## 3. Persistence & Time Travel

## 4. Human-in-the-Loop (HITL) & Error Recovery

## 5. Observability cho Graph
- Task success rate, Nodes visited.
- Retry count, Interrupt count, State validation errors.
- Architecture diagram & state schema.

- [[day9_overview]] – Multi-Agent & MCP (foundation)
- [[day23_overview]]

---

### Day 23 Review Questions

1. When is a linear pipeline (LCEL) no longer sufficient for an agent?
   - A. When only a simple processing flow is needed, with no branching.
   - B. When the agent needs loop retries, human-in-the-loop, dynamic routing, and crash recovery.
   - C. When the number of tools is less than 5.
   - D. When checkpointing is not needed.

2. What is a reducer used for in LangGraph?
   - A. Determines which node runs next.
   - B. Merges state during updates, e.g., appending to message history.
   - C. Creates a checkpoint after each step.
   - D. Calls an external tool.

3. What does the "Time Travel" feature in LangGraph allow you to do?
   - A. Run multiple graphs in parallel at the same time.
   - B. Replay from any checkpoint for debugging or trying a different approach.
   - C. Automatically retry failed nodes.
   - D. Send a notification to the user upon completion.

4. Which function is used to pause the graph to wait for human approval?
   - A. `interrupt()`
   - *A. `interrupt()`*
   - B. `checkpoint()`
   - *B. `checkpoint()`*
   - C. `retry()`
   - *C. `retry()`*
   - D. `breakpoint()`
   - *D. `breakpoint()`*
