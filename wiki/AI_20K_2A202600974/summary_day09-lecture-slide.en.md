---
type: summary
title: "Summary: day09-lecture-slide"
description: "A detailed summary of the day09-lecture-slide.pdf document."
tags: [day09, multi-agent, lecture-slides]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/9/day09-lecture-slide.pdf"]
---

# Summary: AI in Action - Day 09 (Multi-Agent & System Integration)

This document summarizes the Day 09 lecture slides of the "AI in Action" course, focusing on transitioning from a single overloaded agent to a robust multi-agent system with clear roles, leveraging tools like LangGraph, MCP, and A2A communication.

## 1. Context & Use Case
- **Use Case:** Internal assistant for CS (Customer Success) and IT Helpdesk. Tasks include handling refund policies (e.g., 7-day refund policy), P1 SLA (Service Level Agreements), and access approval workflows.
- **Goal of Day 09:** Add an orchestration layer (Supervisor + Workers) to the RAG pipeline built in Day 08. Emphasizes clear roles, traceability, and extensibility.

## 2. The Limits of Single Agents
A single monolithic agent can become a bottleneck when it is forced to plan, retrieve, call tools, synthesize, monitor, and retry all at once. The core limits are:
- **Context bottleneck:** Prompt size bloats.
- **Specialization trade-off:** Hard to perform many different tasks well with a single prompt.
- **Parallelism limits:** Independent tasks are forced to run sequentially.
- **Reliability:** A routing error early on ruins the entire workflow. 
*Rule of thumb:* Multi-agent systems should be used not just to sound impressive, but to decouple logic and improve system observability.

## 3. Multi-Agent Patterns
Four common patterns were introduced:
1. **Supervisor-Worker:** Clear routing, easy to trace. (Focus of Day 09).
2. **Pipeline:** Linear flow, good for fixed SOPs (Standard Operating Procedures).
3. **Debate:** Multiple perspectives to reduce blind spots.
4. **Hierarchical:** Excellent scaling for separate domains.

### Supervisor-Worker Pattern Deep Dive
- **Supervisor:** Responsible for making routing decisions and keeping track of the state. It does *not* need to be the smartest agent; it just delegates cleanly.
- **Workers:** Specialized agents (e.g., Retrieval Worker, Tool/Policy Worker, Synthesis Worker) with narrow, well-defined skills.
- **Contracts:** Communication relies on clear JSON contracts (tasks, constraints, expected output, errors) which makes workers testable and replaceable.

## 4. MCP (Model Context Protocol) vs. A2A (Agent-to-Agent)
- **MCP (Client-Server Architecture):** A standard interface for connecting agents to external capabilities (Tools, Resources, Prompts) without hard-coding integrations.
  - *Tools:* Actions with side effects (e.g., Zendesk, Jira APIs).
  - *Resources:* Static data (e.g., schemas, docs).
  - *Prompts:* Predefined instructions/templates.
- **A2A:** Agents delegating tasks or cooperating with other agents (e.g., Handoff, Cooperative Search, Concurrent Debate, Self-Correction, Joint Decision).
- *Rule of thumb:* Use MCP to fetch a capability or execute a tool. Use A2A to assign a task to another intelligent role.

## 5. LangGraph & Orchestration Implementation
- **Core Components:** Nodes (who acts), Edges (where to go next), State (what the system knows), Checkpointer (memory/time travel), and Routing (the decision logic).
- **HITL (Human-in-the-Loop):** Essential for high-risk actions (refunds, access changes) or low confidence scenarios. LangGraph supports adding breakpoints for human review.
- **Sub-graphs:** Breaking down massive flows into modular, reusable team-based graphs (e.g., `IT_Graph`, `Sales_Graph`).
- **State vs. Message Passing:** Use *shared state* to orchestrate the entire flow and *message contracts* to assign tasks across worker boundaries.

## 6. Hands-on Lab Overview
Students are expected to refactor their single-agent RAG from Day 08 into a multi-agent orchestration setup consisting of:
1. **Refactoring the graph:** Establish a basic Supervisor flow.
2. **Building workers:** Retrieval, Tool/Policy, and Synthesis workers.
3. **Adding MCP:** Connect at least one real or mocked external capability.
4. **Trace & Documentation:** Provide a readable execution trace showing route logic, node inputs/outputs, and compare single vs. multi-agent performance.

## Key Takeaway
Multi-agent isn't about simply having more agents; it's about separating concerns so the system's reasoning path is observable, testable, and reliable. Proper tracing is the foundation for Day 10's focus on observability and data pipelines.
